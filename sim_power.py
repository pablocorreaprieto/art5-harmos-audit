"""Power and error-rate simulation for ART 5 (design v0.2, unchanged in v0.3 and v0.4). Status of every number: numerical,
under the assumptions written here; nothing in it is a result about language models.

python sim_power.py                 controls and power grid -> sim_power_results.json; exits non-zero
                                    if a control does not behave as required
python sim_power.py --pilot SIGMA SLOPE
                                    power of the level test at T = 16, 24 and 32 for the pilot rule

The tests are the ones the real analysis runs: analyze.primary_from_cubes on cubes drawn by
analyze.simulate_cubes (six models, six grades, two genres, T topics, one text per prompt).
Assumptions: per-model intercepts N(4.9, 0.15) and ruler slopes N(slope, 0.01); topic effects
N(0, 0.1); label x topic effects tau_lt = 0.02 shared by models and grades; prompt effects
tau_ps = 0.05 shared by the six models; text noise t(5) scaled to sigma; 2% of texts excluded
at random.

Controls (R = 2000 each; bound = 99% binomial upper limit around .05, 0.0627)
  C1 null data: family-wise rejection rate of the four primary tests must stay under the bound.
  C2 permuted labels: a one-year offset is planted, then the L1, L1P and L5 texts are shuffled
     within every model x grade x genre x topic cell; same requirement.
  C3 must fail: the text-level analysis of design v0.1 (OLS with HC3, no clustering), on null data
     with prompt effects shared by the six models (tau_ps = 0.1), must reject the level test more
     often than the bound. If it does not, the simulation cannot see the dependence that the
     topic-level test is there to handle.
  C4 the topic-level tests on the C3 data stay under the bound.
Grid (R = 500 per cell): sigma 0.15, 0.2, 0.3, 0.4; ruler slope -0.02, -0.04, -0.06 Zipf per
  year; T 16, 24, 32.
  Scenarios: offset of two years, one year and half a year (power of H2-H), half tracking and
  ignored label (power of H3-H).
"""
import json
import sys

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

import analyze as A

LABELS = ["L1", "L1P", "L5"]
BOUND_R = 2000
BOUND = 0.05 + 2.326 * np.sqrt(0.05 * 0.95 / BOUND_R)
ASSUME = {"tau_lt": 0.02, "tau_ps": 0.05, "missing": 0.02, "heavy": True}
SCENARIOS = {
    "offset_2y": {"L1": 2.0, "L1P": 2.0},
    "offset_1y": {"L1": 1.0, "L1P": 1.0},
    "offset_half_y": {"L1": 0.5, "L1P": 0.5},
    "half_tracking": {"L1": list(9 + 0.5 * (A.AGES - 9)), "L1P": list(9 + 0.5 * (A.AGES - 9))},
    "ignored": {"L1": [9.0] * 6, "L1P": [9.0] * 6},
}


def draw(written, rng, sigma, slope, T, **kw):
    params = dict(ASSUME, **kw)
    return A.simulate_cubes(written, rng, n_topics=T, sigma=sigma, slope=slope, labels=LABELS, **params)


def rates(written, sigma, slope, T, R, seed, permute=False, **kw):
    rng = np.random.default_rng(seed)
    rej = {name: 0 for name, *_ in A.PRIMARY}
    any_rej = 0
    for _ in range(R):
        cubes = draw(written, rng, sigma, slope, T, **kw)
        if permute:
            stack = np.stack([cubes[l] for l in LABELS])  # (3, M, G, E, T)
            order = np.argsort(rng.random(stack.shape), axis=0)
            stack = np.take_along_axis(stack, order, axis=0)
            cubes = {l: stack[i] for i, l in enumerate(LABELS)}
        p = A.primary_from_cubes(cubes)
        hit = False
        for name in rej:
            rej[name] += p[name]["rejected_holm"]
            hit = hit or p[name]["rejected_holm"]
        any_rej += hit
    return {"familywise": any_rej / R, **{k: v / R for k, v in rej.items()}}


def naive_text_level(cubes):
    """Design v0.1 analysis restricted to L1 and L5: OLS with HC3 at the text level."""
    rows = []
    for lab in ("L1", "L5"):
        M, G, E, T = cubes[lab].shape
        idx = np.indices((M, G, E, T)).reshape(4, -1).T
        v = cubes[lab].reshape(-1)
        rows.append(pd.DataFrame({"m": idx[:, 0], "g": idx[:, 1], "e": idx[:, 2], "t": idx[:, 3], "y": v, "lab": lab}))
    d = pd.concat(rows).dropna()
    d["mg"] = d["m"].astype(str) + "_" + d["g"].astype(str)
    d["l1"] = (d["lab"] == "L1").astype(float)
    terms = []
    for m in sorted(d["m"].unique()):
        d[f"l1_{m}"] = d["l1"] * (d["m"] == m)
        terms.append(f"l1_{m}")
    res = smf.ols("y ~ C(mg) + " + " + ".join(terms) + " + C(e) + C(t) - 1", data=d).fit(cov_type="HC3")
    c = np.array([1 / len(terms) if n in terms else 0.0 for n in res.params.index])
    t = res.t_test(c)
    return float(np.asarray(t.pvalue).ravel()[0])


def controls():
    out = {"bound": BOUND, "R": BOUND_R}
    out["C1_null"] = rates({}, 0.3, -0.04, 16, BOUND_R, seed=101)
    out["C2_permuted"] = rates(SCENARIOS["offset_1y"], 0.3, -0.04, 16, BOUND_R, seed=102, permute=True)
    rng = np.random.default_rng(103)
    naive_rej, topic_any = 0, 0
    for _ in range(1000):
        cubes = draw({}, rng, 0.3, -0.04, 16, tau_ps=0.1, missing=0.0)
        naive_rej += naive_text_level(cubes) <= 0.05
        topic_any += any(v["rejected_holm"] for v in A.primary_from_cubes(cubes).values())
    out["C3_naive_text_level_rate"] = naive_rej / 1000
    out["C4_topic_level_familywise_on_C3_data"] = topic_any / 1000
    bound_1000 = 0.05 + 2.326 * np.sqrt(0.05 * 0.95 / 1000)
    checks = {
        "C1 null family-wise rate under the bound": out["C1_null"]["familywise"] <= BOUND,
        "C2 permuted family-wise rate under the bound": out["C2_permuted"]["familywise"] <= BOUND,
        "C3 naive text-level test exceeds the bound (expected to fail)": out["C3_naive_text_level_rate"] > bound_1000,
        "C4 topic-level tests on C3 data under the bound": out["C4_topic_level_familywise_on_C3_data"] <= bound_1000,
    }
    out["checks"] = {k: bool(v) for k, v in checks.items()}
    return out


def grid(R=500):
    rows = []
    for sigma in (0.15, 0.2, 0.3, 0.4):
        for slope in (-0.02, -0.04, -0.06):
            for T in (16, 24, 32):
                row = {"sigma": sigma, "slope": slope, "T": T}
                for i, (name, written) in enumerate(SCENARIOS.items()):
                    r = rates(written, sigma, slope, T, R, seed=int(round(1000 * sigma)) * 1000 + int(round(-slope * 100)) * 100 + T * 4 + i)
                    row[name] = {"h2_level_H": r["h2_level_H"], "h3_gradient_H": r["h3_gradient_H"], "familywise": r["familywise"]}
                rows.append(row)
                print(json.dumps(row))
    return rows


def pilot_power(sigma, slope, R=1000):
    out = {}
    for T in (16, 24, 32):
        r = rates(SCENARIOS["offset_1y"], sigma, slope, T, R, seed=777 + T)
        out[T] = r["h2_level_H"]
    return out


if __name__ == "__main__":
    if "--pilot" in sys.argv:
        i = sys.argv.index("--pilot")
        print(json.dumps(pilot_power(float(sys.argv[i + 1]), float(sys.argv[i + 2]))))
        sys.exit(0)
    c = controls()
    print(json.dumps(c, indent=1, default=float))
    g = grid()
    json.dump({"assumptions": ASSUME, "controls": c, "grid": g}, open("sim_power_results.json", "w"), indent=1, default=float)
    ok = all(c["checks"].values())
    print("OK" if ok else "FAILED: a control did not behave as required")
    sys.exit(0 if ok else 1)
