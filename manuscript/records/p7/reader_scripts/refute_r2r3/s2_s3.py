import sys
sys.path.insert(0, "/tmp/refute_r2r3")
import numpy as np, pandas as pd
from scipy import stats
from core import *

Y, L0, models, genres, topics = load()
print("== S2(iii) leave-one-topic-out for H3-P; sign count")
x = topic_stats(Y, "L1P", "L5", "gradient")
print("positive gradients:", int((x > 0).sum()), "of", len(x))
res = []
for i, t in enumerate(topics):
    r = ttest(np.delete(x, i))
    res.append((r["p"], t))
res.sort()
print("min", res[0], "max", res[-1])
# Holm with the other three p-values fixed: would the smallest LOTO p pass?
print("== S2(ii) gradient CI limits x 5-year span; 90% CIs (TOST view)")
for name, a, kind in [("H2-H", "L1", "level"), ("H2-P", "L1P", "level"), ("H3-H", "L1", "gradient"), ("H3-P", "L1P", "gradient")]:
    xx = topic_stats(Y, a, "L5", kind)
    r95, r90 = ttest(xx), ttest(xx, 0.90)
    span = 5.0 if kind == "gradient" else 1.0
    print(name, "95%", round(r95["lo"] * span, 4), round(r95["hi"] * span, 4), "| 90%", round(r90["lo"] * span, 4), round(r90["hi"] * span, 4),
          "(gradient x 5 years)" if kind == "gradient" else "")

print("== S2(i) Table S6 3H row for L1")
r = ttest(topic_stats(Y, "L1", "L5", "level", grades=[0]))
print("3H L1-L5", round(r["est"], 4), round(r["lo"], 4), round(r["hi"], 4))

print("== S7: L2 - L1 level and gradient (topic t-tests), per model")
for kind in ["level", "gradient"]:
    r = ttest(topic_stats(Y, "L2", "L1", kind))
    print("L2-L1", kind, round(r["est"], 4), [round(r["lo"], 4), round(r["hi"], 4)], "t", round(r["t"], 2), "p", r["p"])
for i, m in enumerate(models):
    r = ttest(topic_stats(Y, "L2", "L1", "level", models=[i]))
    print("   ", NAMES[m], round(r["est"], 4), [round(r["lo"], 4), round(r["hi"], 4)])

print("== S3: length")
df = pd.read_csv(f"{REPO}/results/measures.csv")
df["log_n"] = np.log(df["n_words"])
d = df[df["label"].isin(["L1", "L1P", "L5"])]
for m, g in df[df["label"].isin(["L1", "L1P", "L2", "L3", "L4", "L5"])].groupby("model"):
    b = np.polyfit(g["log_n"], g["mean_zipf_content"], 1)[0]
    print("  slope of mean Zipf on log words (all graded labels pooled, raw)", NAMES[m], round(b, 4))
# within-cell analysis: cells model x grade x genre x topic with L1, L1P, L5 -> demeaned regression
d = d.copy()
d["cell"] = d["model"] + d["grade"] + d["genre"] + d["topic"]
for col in ["mean_zipf_content", "log_n"]:
    d[col + "_c"] = d[col] - d.groupby("cell")[col].transform("mean")
b = np.sum(d["mean_zipf_content_c"] * d["log_n_c"]) / np.sum(d["log_n_c"] ** 2)
print("within model x grade x genre x topic cells over L1, L1P, L5: slope", round(b, 4))
# L5 only, within model x grade x genre (across topics) -- one text per model x grade x genre x topic in L5
l5 = df[df["label"] == "L5"].copy()
l5["cell"] = l5["model"] + l5["grade"] + l5["genre"]
for col in ["mean_zipf_content", "log_n"]:
    l5[col + "_c"] = l5[col] - l5.groupby("cell")[col].transform("mean")
b5 = np.sum(l5["mean_zipf_content_c"] * l5["log_n_c"]) / np.sum(l5["log_n_c"] ** 2)
print("L5 only, within model x grade x genre cells (across topics): slope", round(b5, 4))
l5["cell2"] = l5["model"] + l5["grade"] + l5["genre"] + l5["topic"]
print("L5 texts per model x grade x genre x topic cell:", l5.groupby("cell2").size().max())
