"""In-text citations and the reference list of the ART 5 manuscript match (P6.1, offline part).

python checks/check_citations.py [--plant orphan|unread|narrative]

1. Every parenthetical citation of manuscript/manuscript.md ("(Name et al., 2023)", "(CDIP, 2007; Name,
   n.d., p. 6)") is, after prefixes such as "e.g.," or "see" and page locators are removed, exactly the
   'cite' string of a reference in manuscript/references.json, except the primary source of an
   "as cited in" citation (APA 7.21: the primary source is not listed).
2. Every narrative citation, a year in brackets after a name ("Huang et al. (2024)", "Imperial and Tayyar
   Madabushi (2023)"), is preceded by the narrative form of a reference ('&' written 'and').
3. Every reference cited carries an access label read-directly, or one that says why it is cited without
   being read and that the G2 exception list must repeat ("G2 exception").
4. No "CITE" marker is left in the text.
Prints "PASS check_citations" or "FAIL check_citations" with the reasons. Failure controls: --plant
orphan adds "(Smith, 2020)", --plant narrative adds "Smith (2020)", --plant unread gives a cited
reference the label "abstract-only"; each must fail.
Written by the main session (claude-opus-5-5) on 1.11.2026.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
YEAR = r"(?:19|20)\d{2}[a-z]?|n\.d\."


def body(md):
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.S)
    md = re.sub(r"\{\{[^}]*\}\}", "N", md)  # placeholders are numbers, not citations
    return re.split(r"^# References\s*$", md, maxsplit=1, flags=re.M)[0]


def forms(ref):
    par = ref["cite"]
    name, year = par.rsplit(", ", 1)
    return par, name.replace(" & ", " and "), year


def run(md, refs):
    bad, cited = [], set()
    text = body(md)
    for m in re.finditer(r"CITE[^)]*", text):
        bad.append(f"CITE marker left: {m.group(0)[:60]}")
    by_cite = {forms(r)[0]: r for r in refs}
    # 1. parenthetical citations
    spans = []
    for m in re.finditer(r"\(([^()]*(?:" + YEAR + r")[^()]*)\)", text):
        inner = m.group(1)
        if not re.search(r"[A-Za-zÀ-ÿ]{2,}", inner.replace("n.d.", "")):
            continue  # a bracketed year after a name is narrative, handled below
        spans.append(m.span())
        for part in inner.split(";"):
            part = part.strip()
            chunks = re.split(r",? as cited in ", part)
            chunk = chunks[-1]
            chunk = re.sub(r"^(?:e\.g\.,|see|compare|cf\.)\s+", "", chunk)
            chunk = re.sub(r",\s*pp?\.\s*[\d–-]+$", "", chunk).strip()
            if not re.search(YEAR, chunk):
                continue
            if chunk in by_cite:
                cited.add(by_cite[chunk]["key"])
            else:
                bad.append(f"parenthetical citation without reference: ({part})")
    # 2. narrative citations: "(YEAR)" or "(YEAR, p. 6)" right after a name
    narrative = {}
    for r in refs:
        par, name, year = forms(r)
        narrative.setdefault(year, []).append((name, r))
    for m in re.finditer(r"\((" + YEAR + r")(?:,\s*pp?\.\s*[\d–-]+)?\)", text):
        year = m.group(1)
        before = text[max(0, m.start() - 80):m.start()].rstrip()
        if before.endswith("as cited in"):
            continue
        hit = [r for name, r in narrative.get(year, []) if before.endswith(name)]
        if hit:
            cited.add(hit[0]["key"])
        else:
            bad.append(f"narrative citation without reference: ...{before[-40:]} ({year})")
    # 3. access labels
    for r in refs:
        if r["key"] in cited:
            acc = r.get("access", "")
            if not (acc.startswith("read-directly") or "G2 exception" in acc):
                bad.append(f"{r['key']} cited with access '{acc}'")
    return bad, cited


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plant", choices=["orphan", "unread", "narrative"])
    a = ap.parse_args()
    md = open(os.path.join(REPO, "manuscript/manuscript.md")).read()
    refs = json.load(open(os.path.join(REPO, "manuscript/references.json")))
    if a.plant == "orphan":
        md = md.replace("# Discussion", "# Discussion\n\nAs shown before (Smith, 2020).", 1)
    if a.plant == "narrative":
        md = md.replace("# Discussion", "# Discussion\n\nAs Smith (2020) showed.", 1)
    if a.plant == "unread":
        _, cited = run(md, refs)
        k = sorted(cited)[0]
        refs = [dict(r, access="abstract-only") if r["key"] == k else r for r in refs]
    bad, cited = run(md, refs)
    unused = sorted(r["key"] for r in refs if r["key"] not in cited)
    print(f"{len(cited)} references cited: {', '.join(sorted(cited))}")
    if unused:
        print(f"in references.json but not cited (not listed in the rendered references): {', '.join(unused)}")
    print("\n".join(bad) if bad else "no problem found")
    print("FAIL check_citations" if bad else "PASS check_citations")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
