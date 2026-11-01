"""In-text citations and the reference list of the ART 5 manuscript match (P6.1, offline part).

python checks/check_citations.py [--plant orphan|unread]

1. Every in-text citation of manuscript/manuscript.md (parenthetical "(Name et al., 2023)", "(Name &
   Name, 2023; Name, n.d.)", narrative "Name et al. (2023)", "Name and Name (2023)") names a reference
   of manuscript/references.json by first author and year, except a citation followed by "as cited
   in", whose source is the secondary one (APA 7.21, the primary source is not listed).
2. Every reference cited carries an access label read-directly, or an access label that says why it is
   cited without being read and that the G2 exception list must repeat ("G2 exception").
3. No "CITE" marker is left in the text.
Prints "PASS check_citations" or "FAIL check_citations" with the reasons.
Failure controls: --plant orphan adds "(Smith, 2020)" to a copy of the source; --plant unread changes
the access label of a cited reference to "abstract-only". Both must fail.
Written by the main session (claude-opus-5-5) on 1.11.2026.
"""
import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

YEAR = r"(?:19|20)\d{2}[a-z]?|n\.d\."
NAME = r"(?:[A-Z][\w'’-]+|van [A-Z][\w-]+|de [A-Z][\w-]+)(?: (?:y |de |van )?[A-Z][\w'’-]+)*"
AUTHORS = rf"{NAME}(?: et al\.| (?:&|and) {NAME})?"
PAREN = re.compile(r"\(([^()]*?(?:" + YEAR + r")[^()]*?)\)")
NARRATIVE = re.compile(rf"({AUTHORS}) \(({YEAR})(?:, p+\. [\d–-]+)?\)")


def fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def body(md):
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.S)
    return re.split(r"^# References\s*$", md, maxsplit=1, flags=re.M)[0]


def citations(text):
    """(first author, year, raw) of every citation, secondary 'as cited in' sources skipped."""
    out = []
    for m in PAREN.finditer(text):
        inner = m.group(1)
        parts = [p.strip() for p in inner.split(";")]
        for part in parts:
            chunks = re.split(r",? as cited in ", part)
            for j, chunk in enumerate(chunks):
                if j < len(chunks) - 1:
                    continue  # the primary source of an "as cited in" citation is not listed
                chunk = re.sub(r"^(?:e\.g\.,|see|compare|cf\.)\s+", "", chunk)
                mm = re.match(rf"({AUTHORS}),? ({YEAR})(?:, p+\. [\d–-]+)?$", chunk)
                if mm:
                    out.append((mm.group(1), mm.group(2), chunk))
    for m in NARRATIVE.finditer(text):
        before = text[max(0, m.start() - 15):m.start()]
        if "as cited in" in before:
            continue
        out.append((m.group(1), m.group(2), m.group(0)))
    return out


def first_surname(authors):
    a = re.sub(r" et al\.$", "", authors)
    a = re.split(r" (?:&|and) ", a)[0]
    return fold(a)


def run(md, refs):
    bad = []
    text = body(md)
    if "CITE" in text:
        for m in re.finditer(r"CITE[^)]*", text):
            bad.append(f"CITE marker left: {m.group(0)[:60]}")
    index = {}
    for r in refs:
        index.setdefault((fold(r["first_author"]), str(r["year"])), []).append(r)
    cited = set()
    for authors, year, raw in citations(text):
        key = (first_surname(authors), year.rstrip("abcdefgh") if year != "n.d." else year)
        if key not in index:
            bad.append(f"citation without reference: {raw}")
        else:
            cited.update(r["key"] for r in index[key])
    for r in refs:
        if r["key"] in cited:
            acc = r.get("access", "")
            if not (acc.startswith("read-directly") or "G2 exception" in acc):
                bad.append(f"{r['key']} cited with access '{acc}'")
    return bad, cited


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plant", choices=["orphan", "unread"])
    a = ap.parse_args()
    md = open(os.path.join(REPO, "manuscript/manuscript.md")).read()
    refs = json.load(open(os.path.join(REPO, "manuscript/references.json")))
    if a.plant == "orphan":
        md = md.replace("# Discussion", "# Discussion\n\nAs shown before (Smith, 2020).", 1)
    _, cited = run(md, refs)
    if a.plant == "unread":
        k = sorted(cited)[0]
        refs = [dict(r, access="abstract-only") if r["key"] == k else r for r in refs]
    bad, cited = run(md, refs)
    print(f"{len(cited)} references cited: {', '.join(sorted(cited))}")
    print("\n".join(bad) if bad else "no problem found")
    print("FAIL check_citations" if bad else "PASS check_citations")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
