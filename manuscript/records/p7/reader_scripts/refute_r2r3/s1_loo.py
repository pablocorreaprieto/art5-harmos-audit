import sys
sys.path.insert(0, "/tmp/refute_r2r3")
import numpy as np
from core import *

Y, L0, models, genres, topics = load()
print("models", models)
print("== primary, all six")
for name, a, kind in [("H2-H", "L1", "level"), ("H2-P", "L1P", "level"), ("H3-H", "L1", "gradient"), ("H3-P", "L1P", "gradient")]:
    r = ttest(topic_stats(Y, a, "L5", kind))
    print(name, {k: round(v, 5) if isinstance(v, float) else v for k, v in r.items()})

print("== leave one model out (two-sided p, uncorrected)")
for name, a, kind in [("H2-H", "L1", "level"), ("H2-P", "L1P", "level"), ("H3-H", "L1", "gradient"), ("H3-P", "L1P", "gradient")]:
    for i, m in enumerate(models):
        keep = [j for j in range(6) if j != i]
        r = ttest(topic_stats(Y, a, "L5", kind, models=keep))
        print(f"{name} without {NAMES[m]:7s} est {r['est']:+.5f} p {r['p']:.4f}")

print("== per-model levels/gradients (topic t-tests) and SD across six")
for name, a, kind in [("H2-H", "L1", "level"), ("H2-P", "L1P", "level"), ("H3-H", "L1", "gradient"), ("H3-P", "L1P", "gradient")]:
    ests = []
    for i, m in enumerate(models):
        r = ttest(topic_stats(Y, a, "L5", kind, models=[i]))
        ests.append(r["est"])
    ests = np.array(ests)
    r5 = ttest(ests)
    print(name, dict(zip([NAMES[m] for m in models], np.round(ests, 4))), "SD", round(ests.std(ddof=1), 4),
          "models-as-sample t(5):", round(r5["est"], 4), [round(r5["lo"], 4), round(r5["hi"], 4)], "p", round(r5["p"], 3))

means = cell_means_w(Y)
print("== shifts and tracking per model, pooled vs mean vs median")
for lab in ["L1", "L1P", "L2", "L3", "L4"]:
    prof = per_model_profile(means, lab)
    sh, tr = per_model_shift_track(prof)
    ps, pt = pooled(prof)
    print(lab, "pooled", round(ps, 3), round(pt, 3), "| mean", round(sh.mean(), 3), round(tr.mean(), 3),
          "| median", round(np.median(sh), 3), round(np.median(tr), 3),
          "| SD shift", round(sh.std(ddof=1), 3), "SD track", round(tr.std(ddof=1), 3),
          "| range shift", round(sh.min(), 2), round(sh.max(), 2), "range track", round(tr.min(), 2), round(tr.max(), 2))
    print("    shifts", dict(zip([NAMES[m] for m in models], np.round(sh, 2))))
    print("    tracks", dict(zip([NAMES[m] for m in models], np.round(tr, 2))))
