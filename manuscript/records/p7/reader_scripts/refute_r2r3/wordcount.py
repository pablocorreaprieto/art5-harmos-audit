import re
md = open("/home/claude/art5-harmos-audit/manuscript/build/manuscript.md", encoding="utf-8").read()
md = md.split("---", 2)[2]
secs = re.split(r"^# ", md, flags=re.M)[1:]
tot = {}
for s in secs:
    name, body = s.split("\n", 1)
    lines = body.split("\n")
    table = [l for l in lines if l.startswith("|")]
    caps = [l for l in lines if l.startswith("Table ") or l.startswith("![")]
    rest = [l for l in lines if not l.startswith("|") and not (l.startswith("Table ") or l.startswith("!["))]
    w = lambda ls: sum(len(l.split()) for l in ls)
    tot[name.strip()] = (w(lines), w(table), w(caps), w(rest))
    print(f"{name.strip():22s} all {w(lines):5d}  tables {w(table):4d}  captions {w(caps):4d}  prose {w(rest):5d}")
main = ["Introduction", "Background", "Method", "Results", "Discussion", "Conclusion"]
allbutref = [k for k in tot if k != "References"]
print("all except references: with tables+captions", sum(tot[k][0] for k in allbutref), "| without tables", sum(tot[k][0] - tot[k][1] for k in allbutref))
print("Intro..Conclusion: with tables", sum(tot[k][0] for k in main), "| captions, no tables", sum(tot[k][0] - tot[k][1] for k in main),
      "| neither", sum(tot[k][3] for k in main))
abstract = tot["Abstract"][0]
print("abstract words", abstract)
