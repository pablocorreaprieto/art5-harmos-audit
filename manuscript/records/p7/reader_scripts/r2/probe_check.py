"""Independent parse of the knowledge-probe answers (first age range stated), compared with the pipeline's parse."""
import re, sys, json
import numpy as np, pandas as pd
REPO = sys.argv[1]
p = pd.read_csv(f"{REPO}/results/probes.csv", keep_default_na=False)
W = {"quatre":4,"cinq":5,"six":6,"sept":7,"huit":8,"neuf":9,"dix":10,"onze":11,"douze":12,"treize":13,"quatorze":14,"quinze":15,"seize":16}
num = r"(\d{1,2}|" + "|".join(W) + r")"
# an age statement: N [sep N] ans   (sep: à, -, –, —, ou, et, /, jusqu'à)
pat = re.compile(rf"\b{num}\s*(?:(?:à|a|-|–|—|ou|et|/)\s*{num}\s*)?ans?\b", re.I)
def val(x):
    x = x.lower()
    return int(x) if x.isdigit() else W[x]
def ranges(t):
    t = t.replace("\xa0", " ").replace(" ", " ")
    out = []
    for m in pat.finditer(t):
        lo = val(m.group(1)); hi = val(m.group(2)) if m.group(2) else lo
        out.append((lo, hi))
    return out
rows = []
for r in p.itertuples():
    rg = ranges(r.text)
    first = rg[0] if rg else None
    mid = None if first is None else sum(first) / 2
    ok = (mid is not None) and (r.truth_age_from - .5 <= mid <= r.truth_age_to + .5)
    rows.append(dict(model=r.model, notation=r.notation, parsed=first is not None, correct=ok, err=None if mid is None else mid - (r.truth_age_from + r.truth_age_to) / 2,
                     any_ok=any(r.truth_age_from - .5 <= (a + b) / 2 <= r.truth_age_to + .5 for a, b in rg), n_ranges=len(set(rg))))
q = pd.DataFrame(rows)
mine = q.groupby(["model", "notation"]).agg(correct=("correct", "mean"), any_ok=("any_ok", "mean"), parsed=("parsed", "mean"), err=("err", "mean")).round(3)
n = json.load(open(f"{REPO}/results/numbers.json"))["probes"]["accuracy_by_model_notation"]
ex = json.load(open(f"{REPO}/results/exploratory.json"))["probe_errors"]
print("parsed share (mine) %.4f ; multiple-range share %.3f" % (q.parsed.mean(), (q.n_ranges > 1).mean()))
for (m, nt), row in mine.iterrows():
    theirs = n[f"{m} | {nt}"]; e = ex[f"{m} | {nt}"]
    flag = "" if (abs(theirs["correct_first"] - row.correct) < 1e-9 and abs(theirs["correct_any"] - row.any_ok) < 1e-9) else "   <-- differs"
    print(f"{m:20s} {nt}: first-correct mine {row.correct:.3f} theirs {theirs['correct_first']:.3f} | any mine {row.any_ok:.3f} theirs {theirs['correct_any']:.3f} | mean err mine {row.err:.2f} theirs {e['mean_signed_error_years']:.2f}{flag}")
