"""Independent recomputation of the numbers that the last corrections added or re-pointed, from results/measures.csv only
(does not import exploratory_p7.py or analyze.py). Read-only.
python3 -I recompute2.py WORKTREE
"""
import json
import sys

import numpy as np
import pandas as pd

W = sys.argv[1]
m = pd.read_csv(f"{W}/results/measures.csv")
m = m[m["kept"] == True]  # noqa: E712
Y = "mean_zipf_content"
AGE = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
MODELS = ["anthropic_balanced", "anthropic_light", "openai_balanced", "openai_light", "mistral_balanced", "mistral_light"]
NAMES = {"anthropic_balanced": "Sonnet 5.5", "anthropic_light": "Haiku 5.5", "openai_balanced": "GPT-6.1 Sol",
         "openai_light": "GPT-6 Luna", "mistral_balanced": "Mistral Large 4", "mistral_light": "Mistral Small 4"}
print("rows kept:", len(m))

# ruler slope per model: least-squares line through the six L5 means by grade, in Zipf per year of age
l5 = m[m["label"] == "L5"].groupby(["model", "grade"])[Y].mean().unstack()
slope = {}
for mo in MODELS:
    ys = np.array([l5.loc[mo, g] for g in AGE])
    xs = np.array([AGE[g] for g in AGE])
    slope[mo] = float(np.polyfit(xs, ys, 1)[0])
print("slopes:", {NAMES[k]: round(v, 4) for k, v in slope.items()})


def paired(label_a, label_b):
    keys = ["model", "grade", "genre", "topic"]
    a = m[m["label"] == label_a].set_index(keys)[Y]
    b = m[m["label"] == label_b].set_index(keys)[Y]
    return (a - b).dropna().rename("d").reset_index()


def level_by_model(a, b):
    d = paired(a, b)
    return d.groupby("model")["d"].mean().to_dict()


def shifts_by_model(a, b="L5"):
    lv = level_by_model(a, b)
    return {mo: lv[mo] / slope[mo] for mo in MODELS}


# (1) L2 - L1 level by model (Zipf) -> sentence: "for four models (level differences from -0.016 to -0.042 Zipf) but hardly for Haiku and Sol (0.004 and -0.004)"
lv21 = level_by_model("L2", "L1")
claimed = json.load(open(f"{W}/results/exploratory_p7.json"))["label_contrasts"]["L2_minus_L1"]["level_by_model"]
print("\n(1) L2 - L1 level by model, recomputed vs exploratory_p7.json")
for mo in MODELS:
    print(f"   {NAMES[mo]:16s} recomputed {lv21[mo]:+.4f}   json {claimed[mo]:+.4f}")
others = [lv21[mo] for mo in MODELS if mo not in ("anthropic_light", "openai_balanced")]
print("   four others: from", f"{max(others):+.3f}", "to", f"{min(others):+.3f}", "| Haiku", f"{lv21['anthropic_light']:+.3f}", "| Sol", f"{lv21['openai_balanced']:+.3f}")

# pooled shift difference L2-L1 and the four-model figure
sum_slope = sum(slope.values())
pooled6 = sum(lv21.values()) / sum_slope
four = [mo for mo in MODELS if mo not in ("anthropic_light", "openai_balanced")]
pooled4 = sum(lv21[mo] for mo in four) / sum(slope[mo] for mo in four)
print(f"   pooled shift difference L2-L1, six models: {pooled6:.3f} (text: 0.57); four models alone: {pooled4:.3f};"
      f" mean of the four per-model shifts: {np.mean([lv21[mo] / slope[mo] for mo in four]):.3f}")

# (2) dispersion: SD across the six models of the per-model shifts, L1, L1P, L2, L3, L4
print("\n(2) SD across models of per-model shift (ddof=1) and of tracking")


def tracking_by_model(a):
    """tracking_m = 1 + gradient_m / slope_m, gradient_m = mean over topics of LS slope of d on age midpoint (by grade)."""
    d = paired(a, "L5")
    out = {}
    for mo in MODELS:
        dm = d[d["model"] == mo]
        # mean over genres and topics per grade, then slope on age
        g = dm.groupby("grade")["d"].mean()
        x = np.array([AGE[k] for k in g.index])
        grad = float(np.polyfit(x, g.values, 1)[0])
        out[mo] = 1 + grad / slope[mo]
    return out


res = {}
for lab in ["L1", "L1P", "L2", "L3", "L4"]:
    sh = shifts_by_model(lab)
    tr = tracking_by_model(lab)
    res[lab] = (np.std(list(sh.values()), ddof=1), np.std(list(tr.values()), ddof=1), sh, tr)
    print(f"   {lab:4s} SD shift {res[lab][0]:.3f}  SD tracking {res[lab][1]:.3f}   shifts " + " ".join(f"{v:+.2f}" for v in sh.values()))
js = json.load(open(f"{W}/results/exploratory_p7.json"))["label_contrasts"]["dispersion_across_models"]
print("   json   :", {k: (round(v["sd_shift"], 3), round(v["sd_tracking"], 3)) for k, v in js.items()})
print(f"   tie check: |SD(L3) - SD(L1P)| = {abs(res['L3'][0] - res['L1P'][0]):.4f}  (text: 'as low as with the bare P label (0.28)')")

# (3) per-model L3 shifts within a year?
sh3 = res["L3"][2]
print("\n(3) L3 per-model shifts:", {NAMES[k]: round(v, 2) for k, v in sh3.items()}, "| max |shift| =", round(max(abs(v) for v in sh3.values()), 2))

# (4) which two models track the H label least (tracking with L1)
tr1 = res["L1"][3]
print("\n(4) tracking with the bare H label:", {NAMES[k]: round(v, 2) for k, v in sorted(tr1.items(), key=lambda kv: kv[1])})
sh1 = res["L1"][2]
print("    |shift| with the bare H label  :", {NAMES[k]: round(abs(v), 2) for k, v in sorted(sh1.items(), key=lambda kv: -abs(kv[1]))})
