"""Independent recomputation of the primary tests from results/measures.csv (no import from analyze.py).
Writes nothing into the repository; prints to stdout."""
import json
import sys
import itertools

import numpy as np
import pandas as pd
from scipy import stats

REPO = sys.argv[1]
df = pd.read_csv(f"{REPO}/results/measures.csv", keep_default_na=False, na_values=["", "nan", "NaN"])
Y = "mean_zipf_content"
AGE = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
ages = np.array(list(AGE.values()))
grades = list(AGE)
topics = sorted(df.topic.unique())
models = sorted(df.model.unique())
genres = sorted(df.genre.unique())

def wide(label):
    d = df[(df.label == label)].copy()
    d = d.set_index(["model", "grade", "genre", "topic"])[Y]
    return d

L5 = wide("L5")

def topic_stats(label, ref="L5", grade_subset=None):
    a = wide(label)
    b = wide(ref)
    diff = (a - b).dropna()
    t = diff.reset_index()
    t.columns = ["model", "grade", "genre", "topic", "d"]
    if grade_subset is not None:
        t = t[t.grade.isin(grade_subset)]
    g = t.groupby(["topic", "grade"]).d.mean().unstack("grade")
    gs = [x for x in grades if x in g.columns]
    g = g[gs]
    a_ = np.array([AGE[x] for x in gs])
    level = g.mean(axis=1)
    c = a_ - a_.mean()
    grad = g.values @ (c / (c ** 2).sum())
    return level, pd.Series(grad, index=g.index), t

def tt(x):
    x = np.asarray(x, float)
    n = len(x)
    m = x.mean(); s = x.std(ddof=1); se = s / np.sqrt(n)
    t = m / se
    p = 2 * stats.t.sf(abs(t), n - 1)
    q = stats.t.ppf(.975, n - 1)
    return m, se, t, p, (m - q * se, m + q * se)

def signflip_p(x, nmax=2**16):
    x = np.asarray(x, float)
    n = len(x)
    # exact, enumerating all 2^n sign patterns
    signs = np.array(list(itertools.product([-1, 1], repeat=n)), dtype=np.int8)
    means = (signs * x).mean(axis=1)
    obs = abs(x.mean())
    return float(np.mean(np.abs(means) >= obs - 1e-15))

def holm(ps):
    keys = sorted(ps, key=lambda k: ps[k])
    m = len(keys)
    adj, run = {}, 0
    for i, k in enumerate(keys):
        run = max(run, min(1, (m - i) * ps[k]))
        adj[k] = run
    return adj

res = {}
for name, lab, kind in [("H2-H", "L1", "level"), ("H2-P", "L1P", "level"), ("H3-H", "L1", "gradient"), ("H3-P", "L1P", "gradient")]:
    level, grad, t = topic_stats(lab)
    x = level if kind == "level" else grad
    m, se, tv, p, ci = tt(x)
    psf = signflip_p(x)
    sw = stats.shapiro(x)
    res[name] = dict(x=x, p=p, psf=psf)
    print(f"{name}: est {m:.6f} se {se:.6f} t {tv:.4f} p {p:.5f} CI [{ci[0]:.5f},{ci[1]:.5f}] signflip p {psf:.5f} "
          f"Shapiro W {sw.statistic:.3f} p {sw.pvalue:.3f} skew {stats.skew(x):.2f} exkurt {stats.kurtosis(x):.2f} n={len(x)}")
adj = holm({k: v["p"] for k, v in res.items()})
adjsf = holm({k: v["psf"] for k, v in res.items()})
print("Holm (t):", {k: round(v, 4) for k, v in adj.items()})
print("Holm (sign-flip):", {k: round(v, 4) for k, v in adjsf.items()})

# leave-one-topic-out for the four tests
for name, v in res.items():
    x = v["x"].values
    loo = [tt(np.delete(x, i)) for i in range(len(x))]
    ps = [l[3] for l in loo]; ms = [l[0] for l in loo]
    print(f"LOO {name}: est range [{min(ms):.5f},{max(ms):.5f}], p range [{min(ps):.4f},{max(ps):.4f}]")
    z = (x - x.mean()) / x.std(ddof=1)
    print("   topic-level values (sorted):", np.round(np.sort(x), 4).tolist(), " max |z| =", round(np.abs(z).max(), 2))
