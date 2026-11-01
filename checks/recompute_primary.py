"""Independent recomputation of the four primary tests from results/measures.csv.

Written without importing analyze.py, from the preregistration text (question 5):
pairs matched on model, grade, genre and topic; d(g,t) = mean over models and genres of (label - L5);
level(t) = mean of d over the six grades; gradient(t) = least-squares slope of d on the grade's age
midpoint; two-sided one-sample t-test over topics; Holm over the four tests.
Compares estimate, SE, t, p and Holm p with results/numbers.json (field "primary").
Prints "PASS recompute_primary" when all 20 values agree within 1e-9, otherwise "FAIL ...".
Failure control: --plant shifts one L1 measure by +0.05 Zipf before recomputing; the check must fail.
Main session (claude-opus-5-5), 1.11.2026.
"""
import json
import sys

import numpy as np
import pandas as pd
from scipy import stats

AGE_MID = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
TESTS = {"h2_level_H": ("L1", "level"), "h2_level_P": ("L1P", "level"),
         "h3_gradient_H": ("L1", "gradient"), "h3_gradient_P": ("L1P", "gradient")}


def per_topic(m, label, kind):
    keys = ["model", "grade", "genre", "topic"]
    a = m[m["label"] == label].set_index(keys)["mean_zipf_content"]
    b = m[m["label"] == "L5"].set_index(keys)["mean_zipf_content"]
    d = (a - b).dropna().reset_index(name="d")
    dg = d.groupby(["topic", "grade"])["d"].mean().reset_index()  # mean over models and genres
    out = []
    for topic, g in dg.groupby("topic"):
        x = g["grade"].map(AGE_MID).to_numpy(float)
        y = g["d"].to_numpy(float)
        if kind == "level":
            out.append(y.mean())
        else:
            xc = x - x.mean()
            out.append(float(np.sum(xc * y) / np.sum(xc * xc)))
    return np.array(out)


def ttest(v):
    T = len(v)
    mean, se = v.mean(), v.std(ddof=1) / np.sqrt(T)
    t = mean / se
    return {"estimate": mean, "se": se, "t": t, "p_two_sided": 2 * stats.t.sf(abs(t), T - 1)}


def holm(ps):
    order = sorted(ps, key=ps.get)
    adj, run = {}, 0.0
    for i, k in enumerate(order):
        run = max(run, min(1.0, (len(order) - i) * ps[k]))
        adj[k] = run
    return adj


def main():
    m = pd.read_csv("results/measures.csv", keep_default_na=False)
    m = m[m["kept"].astype(str).str.lower().isin(["true", "1"])].copy()
    m["mean_zipf_content"] = pd.to_numeric(m["mean_zipf_content"])
    if "--plant" in sys.argv:
        i = m.index[m["label"] == "L1"][0]
        m.loc[i, "mean_zipf_content"] += 0.05
    res = {k: ttest(per_topic(m, lab, kind)) for k, (lab, kind) in TESTS.items()}
    adj = holm({k: v["p_two_sided"] for k, v in res.items()})
    ref = json.load(open("results/numbers.json"))["primary"]
    bad = []
    for k, v in res.items():
        v["p_holm"] = adj[k]
        for f in ("estimate", "se", "t", "p_two_sided", "p_holm"):
            if not abs(v[f] - ref[k][f]) <= 1e-9:
                bad.append(f"{k}.{f}: recomputed {v[f]:.12g} vs numbers.json {ref[k][f]:.12g}")
    print("\n".join(bad) if bad else "all 20 values agree")
    print("FAIL recompute_primary" if bad else "PASS recompute_primary")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
