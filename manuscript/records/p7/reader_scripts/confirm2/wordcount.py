"""Word counts of the rendered manuscript (manuscript/build/manuscript.md and .docx), read-only.
python3 -I wordcount.py WORKTREE
Counting rule used for the headline numbers: whitespace-separated tokens of the visible text (what a word processor
counts), headings included, table cells included when tables are included. Variants are printed for sensitivity.
"""
import re
import sys
import zipfile

root = sys.argv[1]
md = open(f"{root}/manuscript/build/manuscript.md", encoding="utf-8").read()

# ---------------- markdown route ----------------
md_body = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)           # drop YAML front matter (the title)
parts = re.split(r"^# (.+?)\s*$", md_body, flags=re.M)               # [pre, name1, text1, name2, text2, ...]
sections = {}
for i in range(1, len(parts), 2):
    sections[parts[i]] = parts[i + 1]
print("sections:", list(sections))


def plain(line):
    """Visible text of a markdown line: images keep their alt text, links keep their label, markup removed."""
    line = re.sub(r"!\[(.*?)\]\(.*?\)", r"\1", line)          # image -> alt text (the caption)
    line = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", line)           # link -> label
    line = line.replace("**", "").replace("*", "")
    return line


def classify(line):
    s = line.strip()
    if not s:
        return "blank"
    if s.startswith("|"):
        return "table_row"
    if s.startswith("!["):
        return "figure_caption"
    if re.match(r"^Table S?\d+\.", s):
        return "table_caption"
    if s.startswith("#"):
        return "heading"
    return "text"


def count_section(text, include):
    n = 0
    for line in text.splitlines():
        k = classify(line)
        if k == "blank":
            continue
        if k not in include:
            continue
        if k == "table_row":
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):    # the |---|---| line
                continue
            s = " ".join(cells)
        elif k == "heading":
            s = line.strip().lstrip("#").strip()
        else:
            s = plain(line)
        n += len(plain(s).split())
    return n


MAIN = ["Introduction", "Background", "Method", "Results", "Discussion", "Conclusion"]
body_kinds = {"text", "heading"}
all_kinds = {"text", "heading", "table_row", "table_caption", "figure_caption"}
nohead_kinds = {"text"}

main_text_only = sum(count_section(sections[s], body_kinds) + (len(s.split()) if True else 0) for s in MAIN)
# the "# Introduction" style top headings are not in sections[...] text, add their words once (counted above)
main_with = sum(count_section(sections[s], all_kinds) + len(s.split()) for s in MAIN)
main_nohead_text = sum(count_section(sections[s], nohead_kinds) for s in MAIN)
main_nohead_with = sum(count_section(sections[s], all_kinds - {"heading"}) for s in MAIN)
print("\n== MAIN TEXT, Introduction to Conclusion (markdown route, whitespace tokens)")
print("without tables and captions, headings counted      :", main_text_only)
print("without tables and captions, headings not counted  :", main_nohead_text)
print("with tables and captions, headings counted         :", main_with)
print("with tables and captions, headings not counted     :", main_nohead_with)

# separate pieces
tables_tokens = sum(count_section(sections[s], {"table_row"}) for s in MAIN)
tcap_tokens = sum(count_section(sections[s], {"table_caption"}) for s in MAIN)
fcap_tokens = sum(count_section(sections[s], {"figure_caption"}) for s in MAIN)
print("table cells:", tables_tokens, "| table captions:", tcap_tokens, "| figure captions:", fcap_tokens)

abstract_all = count_section(sections["Abstract"], all_kinds)
abstract_para = 0
for para in sections["Abstract"].split("\n\n"):
    p = para.strip()
    if p and not p.startswith("**Keywords"):
        abstract_para += len(plain(p).split())
kw = [l for l in sections["Abstract"].splitlines() if l.startswith("**Keywords")]
print("\n== OTHER PARTS")
print("abstract paragraph (no keywords):", abstract_para, "| with the keyword line:", abstract_all)
notes = count_section(sections["Practitioner notes"], all_kinds)
print("practitioner notes (incl. 3 bold sub-headings):", notes)
stm = count_section(sections["Statements"], all_kinds)
print("statements (body, without the heading word):", stm, "| with heading word:", stm + 1)
ref = count_section(sections["References"], all_kinds)
print("references:", ref)

title = re.search(r'^title:\s*"(.*)"', md, flags=re.M).group(1)
title_n = len(title.split())
print("title words:", title_n)

head_words = {k: len(k.split()) for k in sections}
everything_except_refs = (abstract_all + head_words["Abstract"] + notes + head_words["Practitioner notes"]
                          + main_with + stm + head_words["Statements"])
print("\n== EVERYTHING EXCEPT THE REFERENCES (abstract, keywords, notes, main text with tables/captions, statements; headings counted)")
print("without the title :", everything_except_refs)
print("with the title    :", everything_except_refs + title_n)
# same but main text without tables and captions
ev2 = (abstract_all + head_words["Abstract"] + notes + head_words["Practitioner notes"]
       + main_text_only + stm + head_words["Statements"])
print("(variant) main text without tables and captions, + abstract, notes, statements:", ev2)

# ---------------- docx route ----------------
try:
    import docx
    d = docx.Document(f"{root}/manuscript/build/manuscript.docx")
    from docx.oxml.ns import qn
    body = d.element.body
    paras = []   # (kind, style, text)
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            p = docx.text.paragraph.Paragraph(child, d)
            paras.append(("p", p.style.name, p.text))
        elif child.tag == qn("w:tbl"):
            tbl = docx.table.Table(child, d)
            for row in tbl.rows:
                for cell in row.cells:
                    paras.append(("cell", "table", cell.text))
    print("\n== DOCX route (python-docx; paragraphs and table cells in document order)")
    styles = {}
    for k, s, t in paras:
        styles[s] = styles.get(s, 0) + 1
    print("styles:", styles)
    cur = None
    tot = {}
    capt = {}
    for k, s, t in paras:
        if s == "Heading 1":
            cur = t.strip()
            tot.setdefault(cur, {"body": 0, "table": 0, "caption": 0, "heading": 0})
            tot[cur]["heading"] += len(t.split())
            continue
        if cur is None:
            continue
        n = len(t.split())
        if k == "cell":
            tot[cur]["table"] += n
        elif s in ("Image Caption", "Table Caption") or re.match(r"^(Table|Figure) S?\d+\.", t.strip()):
            tot[cur]["caption"] += n
        else:
            tot[cur]["body"] += n
    for sec, v in tot.items():
        print(f"{sec:22s}", v)
    main_docx_nohead = sum(tot[s]["body"] for s in MAIN if s in tot)
    main_docx_head = main_docx_nohead + sum(tot[s]["heading"] for s in MAIN if s in tot)
    main_docx_all = sum(tot[s]["body"] + tot[s]["table"] + tot[s]["caption"] for s in MAIN if s in tot) + sum(tot[s]["heading"] for s in MAIN if s in tot)
    print("main text, no tables/captions, headings counted:", main_docx_head, "| headings not counted:", main_docx_nohead)
    print("main text, with tables and captions, headings counted:", main_docx_all)
except Exception as e:  # noqa
    print("docx route failed:", repr(e))
