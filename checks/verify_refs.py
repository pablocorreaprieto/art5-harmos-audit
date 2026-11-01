"""Every reference of the ART 5 manuscript exists, with the metadata the reference list gives it (P6.1).

python checks/verify_refs.py [--plant] [--offline]

Reads manuscript/references.json: a list of {key, apa, doi | arxiv | url, title, year, first_author}.
For a DOI, queries Crossref (api.crossref.org/works/DOI), then OpenAlex for the retraction flag; for an
arXiv identifier, the arXiv API (export.arxiv.org); a reference with only a URL (law, web page, data
set) is listed as "url, not checked here" and must be in the G2 exception list or opened by the
session (Sources tab). For each looked-up reference: title similarity (token Jaccard >= 0.8 after
normalisation), year (equal, or within one year for a preprint or an online-first date), first author
surname, volume, issue and pages when the entry gives them (the registry's values are printed for every
DOI), and any retraction or withdrawal notice (Crossref update-to / relation, OpenAlex is_retracted).
Prints one line per reference and "PASS verify_refs" when every looked-up reference matches, else
"FAIL verify_refs". Failure control: --plant adds a reference with an invented DOI and alters the year
and title of the first DOI reference; the check must fail on both.
Network: Crossref, OpenAlex and DataCite are not reachable from the session's sandbox, so this script
runs in GitHub Actions (.github/workflows/checks.yml); --offline only parses the file.
Written by the main session (claude-opus-5-5) on 1.11.2026.
"""
import argparse
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
UA = "art5-harmos-audit verify_refs (mailto:" + os.environ.get("CONTACT_EMAIL", "unknown") + ")"


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return set(re.findall(r"[a-z0-9]+", s)) - {"a", "an", "the", "of", "and", "in", "on", "for", "to", "with", "de", "la", "le", "les", "des", "et"}


def jaccard(a, b):
    a, b = norm(a), norm(b)
    return len(a & b) / len(a | b) if a | b else 0.0


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def crossref(doi):
    m = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
    title = (m.get("title") or [""])[0]
    parts = (m.get("issued") or {}).get("date-parts") or [[None]]
    year = parts[0][0]
    first = (m.get("author") or [{}])[0].get("family", "")
    notices = [u.get("type", "") for u in m.get("update-to", [])]
    notices += [k for k in (m.get("relation") or {}) if "retract" in k or "withdraw" in k]
    return {"title": title, "year": year, "first_author": first, "notices": notices, "type": m.get("type"),
            "journal": (m.get("container-title") or [""])[0], "volume": m.get("volume"), "issue": m.get("issue"),
            "pages": m.get("page") or m.get("article-number")}


def openalex_retracted(doi):
    try:
        w = get_json("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi))
        return bool(w.get("is_retracted"))
    except Exception:
        return None


def arxiv(aid):
    req = urllib.request.Request("https://export.arxiv.org/api/query?id_list=" + aid, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        root = ET.fromstring(r.read())
    ns = {"a": "http://www.w3.org/2005/Atom"}
    e = root.find("a:entry", ns)
    if e is None or e.find("a:title", ns) is None:
        raise ValueError("no entry")
    title = " ".join(e.find("a:title", ns).text.split())
    year = int(e.find("a:published", ns).text[:4])
    first = e.find("a:author/a:name", ns).text.split()[-1]
    return {"title": title, "year": year, "first_author": first, "notices": [], "type": "preprint"}


def check(ref):
    if ref.get("doi"):
        got = crossref(ref["doi"])
        got["retracted_openalex"] = openalex_retracted(ref["doi"])
        src = "crossref"
    elif ref.get("arxiv"):
        got = arxiv(ref["arxiv"])
        got["retracted_openalex"] = None
        src = "arxiv"
    else:
        return "url", [], None
    problems = []
    j = jaccard(ref["title"], got["title"])
    if j < 0.8:
        problems.append(f"title differs (Jaccard {j:.2f}): registry '{got['title'][:90]}'")
    tol = 1 if (src == "arxiv" or ref.get("online_first")) else 0
    if got["year"] is None or abs(int(got["year"]) - int(ref["year"])) > tol:
        problems.append(f"year {ref['year']} vs registry {got['year']}")
    if norm(ref["first_author"]) - norm(got["first_author"]):
        problems.append(f"first author {ref['first_author']} vs registry {got['first_author']}")
    for field in ("volume", "issue", "pages"):
        if ref.get(field) is not None and got.get(field) is not None and \
                str(ref[field]).replace("\u2013", "-") != str(got[field]).replace("\u2013", "-"):
            problems.append(f"{field} {ref[field]} vs registry {got[field]}")
    if got["notices"] or got.get("retracted_openalex"):
        problems.append(f"notice: {got['notices']} retracted={got.get('retracted_openalex')}")
    return src, problems, got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plant", action="store_true")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--refs", default=os.path.join(REPO, "manuscript/references.json"))
    a = ap.parse_args()
    refs = json.load(open(a.refs))
    if a.plant:
        refs = [dict(r) for r in refs]
        first_doi = next(r for r in refs if r.get("doi"))
        first_doi["year"] = int(first_doi["year"]) + 3
        first_doi["title"] = "A title that this work does not have"
        refs.append({"key": "planted", "doi": "10.1111/bjet.99999999", "title": "Invented work", "year": 2025,
                     "first_author": "Nobody", "apa": "planted"})
    bad = 0
    for r in refs:
        if a.offline:
            print(f"{r['key']}: {'doi ' + r['doi'] if r.get('doi') else 'arxiv ' + r['arxiv'] if r.get('arxiv') else 'url'}")
            continue
        try:
            src, problems, got = check(r)
        except Exception as e:  # not found or not reachable counts as a failure
            src, problems = "error", [f"lookup failed: {type(e).__name__}: {str(e)[:80]}"]
        if src == "url":
            print(f"URL   {r['key']}: url, not checked here (opened by the session, see the Sources tab)")
            continue
        status = "OK  " if not problems else "BAD "
        bad += bool(problems)
        meta = ""
        if got and src == "crossref":
            meta = f" [registry: {got.get('journal')}, vol. {got.get('volume')}, issue {got.get('issue')}, pp. {got.get('pages')}, type {got.get('type')}]"
        print(f"{status} {r['key']} ({src}): " + ("; ".join(problems) if problems else "title, year and first author match, no notice") + meta)
        time.sleep(1)
    if a.offline:
        print("offline: parsed", len(refs), "references")
        return
    print("FAIL verify_refs" if bad else "PASS verify_refs")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
