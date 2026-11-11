"""Every number of the ART 5 manuscript traces to a named field (protocol rule 3, phase P6.3).

python checks/check_numbers.py                 run the four checks on the repository
python checks/check_numbers.py --plant KIND    run them on a copy with one planted fault; must FAIL
       KIND = source (a number typed by hand in the source), rendered (a digit changed in the rendered
       text), stale (a value changed in results/manuscript_numbers.json), docx (a digit changed in the
       .docx), quote (a French label wording that no prompt contains)
python checks/check_numbers.py --docx PATH     also compare the numbers of a .docx (for example the
                                               final Google Doc exported as .docx) with the rendered text

Checks:
 1. stale     results/manuscript_numbers.json equals a fresh run of manuscript_numbers.py
 2. source    manuscript/manuscript.md and supplement.md contain no digit outside {{placeholders}},
              the References section, links, and the structural tokens of ALLOW (each with its reason)
 3. quotes    every French wording in « » that contains a digit occurs in one of the 8,652 prompts
              (calls.jsonl, calls_pilot.jsonl), so label examples cannot drift from design.json
 4. rendered  manuscript/build/*.md equal the render of the sources (no edit after rendering), and,
              with --docx, the sequence of numbers in the .docx equals that of the rendered manuscript
Prints "PASS check_numbers" when all pass, otherwise "FAIL check_numbers" with the reasons.
Written by the main session (claude-opus-5-5) on 1.11.2026.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "manuscript"))
import render  # noqa: E402

# Structural tokens that may contain digits in the source, with the reason each is not a result.
ALLOW = [
    (r"\b(?:1[01]|[1-9])[HP]\b", "HarmoS and P grade names (3H, 5P), the conditions of the design"),
    (r"\bL[0-6]P?\b", "label codes of design.json"),
    (r"\bH[1-3](?:-[HP])?\b", "hypothesis codes of the preregistration"),
    (r"\b(?:CE1|CE2|CM1|CM2)\b", "French grade names (design.json, grades)"),
    (r"\b(?:Figures?|Tables?) S?\d+(?:(?:,| and| to) S?\d+)*\b", "references to figures and tables"),
    (r"\bS[1-9]\b", "sections and tables of the Supporting Information"),
    (r"\b95% (?:CI|confidence|percentile|bootstrap)", "conventional level of the intervals (design.json, analysis)"),
    (r"\bupper 80% confidence bound", "pilot SD bound named by the preregistration (question 7)"),
    (r"\bZipf [34]\b", "thresholds of two secondary measures (compute.py, share_rare_content and share_below4_content)"),
    (r"log10\(f \+\s*\) \+ 3", "Zipf formula of the preregistration (question 3); the smoothing is a placeholder"),
    (r"tracking is 1 plus|\(1 means that|\b0 that they ignore|\b1 = follows|\b0 = ignores",
     "anchors of the definition of tracking (1 = follows the grade like the age, 0 = ignores it)"),
    (r"\b[3-6]e\b", "French lower-secondary grades (6e, 5e, 4e, 3e); wordings in quotes are checked against the prompts"),
    (r"\bSHA-256\b", "name of the hash function"),
    (r"\bbase-10\b", "base of the logarithm in the definition of the Zipf scale"),
    (r", pp?\. \d+(?:[\u2013-]\d+)?(?=[);])", "page locator of a citation (checked with the sentence-citation pairs, Sources tab)"),
    (r"\bGPT-4\b", "name of the model used in a cited study (Ripoll y Schmitz & Sonnleitner, 2025), not one of ours"),
    (r"\bexploratory_p7\.py\b", "file name of the post hoc script (added after the readings of the draft, P7)"),
    (r"\bexploratory_audit\.py\b", "file name of the post hoc script of the pre-submission audit (2.11.2026)"),
    (r"\bP1 to P6\b", "names of the primary years in French-speaking Belgium (Fédération Wallonie-Bruxelles, 2025, p. 5)"),
    (r"tracking intervals lie below 1\b", "the tracking anchor 1 (texts follow the grade like the age-only texts)"),
]
CITATION_YEAR = re.compile(r"(?:\(|; |, |et al\.,? |& [A-Z][\w'-]+,? |[A-Z][\w'-]+,? )(?:19|20)\d{2}[a-z]?(?=[);,]| \()")


def strip(md):
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.S)
    md = re.split(r"^# References\s*$", md, maxsplit=1, flags=re.M)[0]
    md = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)  # YAML title block
    md = re.sub(r"https?://\S+|doi:\S+|10\.\d{4,}/\S+", " ", md)
    md = re.sub(r"\{\{[^}]*\}\}", "", md)
    return md


def source_problems(md, name):
    text = CITATION_YEAR.sub(" ", strip(md))
    for pat, _ in ALLOW:
        text = re.sub(pat, " ", text)
    text = re.sub(r"«[^»]*»", " ", text)  # French wordings: checked by quote_problems
    bad = []
    for m in re.finditer(r"\d", text):
        a, b = max(0, m.start() - 40), m.end() + 40
        bad.append(f"{name}: digit typed by hand: ...{text[a:b].strip()}...")
    return bad


def prompts(root):
    out = []
    for f in ("calls.jsonl", "calls_pilot.jsonl"):
        for line in open(os.path.join(root, f)):
            out.append(json.loads(line)["prompt"])
    return out


def quote_problems(md, name, all_prompts):
    text = re.sub(r"\{\{[^}]*\}\}", "", re.sub(r"<!--.*?-->", " ", md, flags=re.S))
    text = re.split(r"^# References\s*$", text, maxsplit=1, flags=re.M)[0]
    bad = []
    for q in re.findall(r"«\s*([^»]*?)\s*»", text):
        if re.search(r"\d", q) and not any(q in p for p in all_prompts):
            bad.append(f"{name}: quoted wording in no prompt: « {q} »")
    return bad


def numbers_in(text):
    text = re.split(r"^#+ References\s*$|^References\s*$", text, maxsplit=1, flags=re.M)[0]
    text = re.sub(r"\]\([^)]*\)", "]", text)  # targets of links and images (figure files) are not in the .docx text
    return re.findall(r"\d+(?:[.,]\d+)*", text)


def docx_text(path):
    import docx
    d = docx.Document(path)
    parts = []
    for el in d.element.body.iterchildren():
        tag = el.tag.split("}")[-1]
        if tag == "p":
            parts.append("".join(t.text or "" for t in el.iter() if t.tag.endswith("}t")))
        elif tag == "tbl":
            for t in el.iter():
                if t.tag.endswith("}t"):
                    parts.append(t.text or "")
    return "\n".join(parts)


def run(root, docx_path=None):
    bad = []
    # 1. stale
    with tempfile.TemporaryDirectory() as tmp:
        fresh = os.path.join(tmp, "fresh.json")
        subprocess.run([sys.executable, "-B", "manuscript_numbers.py", "--out", fresh], cwd=REPO, check=True,
                       stdout=subprocess.DEVNULL)
        a = json.load(open(fresh))
        b = json.load(open(os.path.join(root, "results/manuscript_numbers.json")))
        diff = sorted(k for k in set(a) | set(b) if a.get(k, {}).get("text") != b.get(k, {}).get("text"))
        if diff:
            bad.append(f"stale results/manuscript_numbers.json, differs on {len(diff)} names, e.g. {diff[:3]}")
    # 2 and 3. sources
    all_prompts = prompts(REPO)
    nums, design = render.load(root)
    refs_path = os.path.join(root, "manuscript/references.json")
    keys = {r["key"] for r in json.load(open(refs_path))} if os.path.exists(refs_path) else set()
    for k, v in nums.items():
        if k.startswith("src_") and v.get("ref") not in keys:
            bad.append(f"source fact {k} cites {v.get('ref')}, which is not in manuscript/references.json")
    for stem in ("manuscript", "supplement"):
        src = open(os.path.join(root, f"manuscript/{stem}.md")).read()
        bad += source_problems(src, stem + ".md")
        bad += quote_problems(src, stem + ".md", all_prompts)
        # 4. rendered copy
        built = os.path.join(root, f"manuscript/build/{stem}.md")
        expected = render.render_text(src, nums, design, "../../results/figures", root)
        if not os.path.exists(built) or open(built).read() != expected:
            bad.append(f"manuscript/build/{stem}.md differs from the render of manuscript/{stem}.md")
        if stem == "manuscript" and docx_path:
            got, want = numbers_in(docx_text(docx_path)), numbers_in(expected)
            if got != want:
                i = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
                bad.append(f"{os.path.basename(docx_path)}: numbers differ from the rendered manuscript at number "
                           f"{i + 1} ({got[i] if i < len(got) else 'end'} vs {want[i] if i < len(want) else 'end'}); "
                           f"{len(got)} vs {len(want)} numbers")
    return bad


def planted_copy(kind, tmp, docx_path):
    for d in ("manuscript/build", "results"):
        os.makedirs(os.path.join(tmp, d), exist_ok=True)
    for f in ("manuscript/manuscript.md", "manuscript/supplement.md", "manuscript/process_facts.json",
              "manuscript/source_facts.json", "manuscript/references.json",
              "manuscript/build/manuscript.md", "manuscript/build/supplement.md", "results/manuscript_numbers.json",
              "design.json"):
        shutil.copy(os.path.join(REPO, f), os.path.join(tmp, f))
    if kind == "source":
        p = os.path.join(tmp, "manuscript/manuscript.md")
        s = open(p).read().replace("written as for pupils {{ae_L1_shift}} years older",
                                   "written as for pupils 0.31 years older", 1)
        open(p, "w").write(s)
    elif kind == "rendered":
        p = os.path.join(tmp, "manuscript/build/manuscript.md")
        s = open(p).read()
        i = s.index("Holm-corrected *p* = .0") + len("Holm-corrected *p* = .0")
        open(p, "w").write(s[:i] + str((int(s[i]) + 1) % 10) + s[i + 1:])
    elif kind == "stale":
        p = os.path.join(tmp, "results/manuscript_numbers.json")
        d = json.load(open(p))
        d["ae_L1_shift"]["text"] = "0.31"
        json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
    elif kind == "quote":
        p = os.path.join(tmp, "manuscript/manuscript.md")
        s = open(p).read().replace("(L5, « de 8 à 9 ans »)", "(L5, « de 8 à 10 ans »)", 1)
        open(p, "w").write(s)
    elif kind == "docx":
        import docx
        d = docx.Document(docx_path)
        for para in d.paragraphs:
            for r in para.runs:
                if "0.30" in r.text:
                    r.text = r.text.replace("0.30", "0.31", 1)
                    break
            else:
                continue
            break
        docx_path = os.path.join(tmp, "planted.docx")
        d.save(docx_path)
    return docx_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plant", choices=["source", "rendered", "stale", "quote", "docx"])
    ap.add_argument("--docx")
    a = ap.parse_args()
    docx_path = a.docx or (os.path.join(REPO, "manuscript/build/manuscript.docx") if a.plant == "docx" else None)
    if a.plant:
        with tempfile.TemporaryDirectory() as tmp:
            docx_path = planted_copy(a.plant, tmp, docx_path)
            bad = run(tmp, docx_path)
    else:
        bad = run(REPO, docx_path)
    print("\n".join(bad) if bad else "no problem found")
    print("FAIL check_numbers" if bad else "PASS check_numbers")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
