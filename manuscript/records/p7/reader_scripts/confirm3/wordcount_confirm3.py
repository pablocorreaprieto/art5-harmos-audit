"""Word counts of the rendered manuscript by the rule written in manuscript/render.py (function words), written
here from the rule's description and not imported: runs of non-space characters; headings counted without their
# marks; table rows, figure lines and table captions left out unless tables are counted, in which case the
cells and the caption texts count and the separator rows and image paths do not.

python3 -B wordcount_confirm3.py PATH_TO_RENDERED_MANUSCRIPT.md
"""
import re
import sys

md = open(sys.argv[1], encoding="utf-8").read()
lines = md.splitlines()


def heading_index(title, level=1):
    pat = re.compile(r"^" + "#" * level + r"\s+" + re.escape(title) + r"\s*$")
    for i, l in enumerate(lines):
        if pat.match(l):
            return i
    raise KeyError(title)


def count(first, last_exclusive, tables):
    n = 0
    for l in lines[first:last_exclusive]:
        s = l.strip()
        if not s:
            continue
        if re.fullmatch(r"\|[-|: ]+\|", s):          # separator row of a table
            continue
        is_table_row = s.startswith("|")
        is_figure = s.startswith("![")
        is_caption = bool(re.match(r"^Table S?\d+\.", s))
        if (is_table_row or is_figure or is_caption) and not tables:
            continue
        if is_figure:
            s = re.sub(r"^!\[(.*)\]\([^)]*\)$", r"\1", s)
        s = re.sub(r"^#+\s*", "", s)
        s = s.replace("|", " ")
        n += len(s.split())
    return n


i_abs = heading_index("Abstract")
i_pn = heading_index("Practitioner notes")
i_intro = heading_index("Introduction")
i_stat = heading_index("Statements")
i_ref = heading_index("References")

res = {
    "main, Introduction to Conclusion, no tables or captions": count(i_intro, i_stat, False),
    "main, with tables and captions": count(i_intro, i_stat, True),
    "Abstract to end of Statements (before References), tables counted": count(i_abs, i_ref, True),
    "Abstract to end of Statements, tables not counted": count(i_abs, i_ref, False),
    "Abstract to the heading Statements (Statements left out), tables counted": count(i_abs, i_stat, True),
}
for k, v in res.items():
    print(f"{v:6,d}  {k}")

# the abstract: paragraph alone, and with the keywords line (what render.py's abstract count takes)
abs_lines = [l for l in lines[i_abs + 1:i_pn]]
para = [l for l in abs_lines if l.strip() and not l.strip().startswith("**Keywords")]
kw = [l for l in abs_lines if l.strip().startswith("**Keywords")]
print(f"{sum(len(l.split()) for l in para):6,d}  abstract paragraph alone")
print(f"{sum(len(l.split()) for l in para + kw):6,d}  abstract paragraph plus the Keywords line ({sum(len(l.split()) for l in kw)} tokens)")

# sizes of the paragraphs named by the cut list of the verification report
def para_words(first_text):
    for l in lines:
        if l.startswith(first_text):
            return len(l.split())
    raise KeyError(first_text)

def section_text_words(title, level):
    i = heading_index(title, level)
    j = i + 1
    while j < len(lines) and not re.match(r"^#{1,%d}\s" % level, lines[j]):
        j += 1
    return i, j

print()
print("paragraphs named by the cut list (words by whitespace)")
cands = {
    "sensitivity paragraph": "Removing the truncated or flagged texts",
    "background on lexical demand": "Vocabulary is one of the levers of text difficulty",
    "results per-model paragraph (Behind the averages)": "The pooled estimates average models",
    "discussion per-model paragraph": "Each tool a teacher uses runs on one model",
    "discussion equivalence paragraph 1": "Two observations limit what the measure says",
    "discussion equivalence paragraph 2": "The probe answers suggest where misreadings come from",
    "AI statement": "**Use of generative AI.**",
}
for k, t in cands.items():
    print(f"{para_words(t):5d}  {k}")

# Table 3 (caption plus table) and the sensitivity heading
i3 = next(i for i, l in enumerate(lines) if l.startswith("Table 3."))
j3 = i3 + 1
while j3 < len(lines) and (lines[j3].strip() == "" or lines[j3].startswith("|")):
    j3 += 1
t3 = sum(len(re.sub(r"^#+\s*", "", l.replace("|", " ")).split()) for l in lines[i3:j3] if l.strip() and not re.fullmatch(r"\|[-|: ]+\|", l.strip()))
print(f"{t3:5d}  Table 3 caption plus table cells (by the rule)")
sens = para_words("Removing the truncated or flagged texts")
print(f"{sens + t3:5d}  sensitivity paragraph plus Table 3")
print(f"{sens + t3 + 3:5d}  ... plus the two-word heading 'Sensitivity analyses' (+2) ... (shown with +3 for reference)")
