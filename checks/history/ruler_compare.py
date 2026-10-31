"""Compare two ways of reading label means on a model's age-only ruler (descriptive years):
linear per-model ruler vs isotonic inverse lookup. Simulation only (status: numerical)."""
import sys
sys.path.insert(0, "/home/claude/art5")
import numpy as np
import analyze as A

def per_model_means(cube):
    return np.nanmean(cube, axis=(2, 3))  # (models, grades)

def linear_read(ruler, v):
    b, c = np.polyfit(A.AGES, ruler, 1)
    return (v - c) / b

def iso_read(ruler, v):
    slope = float(np.polyfit(A.AGES, ruler, 1)[0])
    curve = A.pava_decreasing(ruler)
    return np.array([A.age_equivalent(curve, x, slope)[0] for x in v])

scen = {"offset +1": 1.0, "ignored (age 9)": [9.0] * 6, "digit as age -3.5": -3.5,
        "collision 3e..6e then +0": [14.5, 13.5, 12.5, 11.5, 10.5, 11.5], "half tracking": list(9 + 0.5 * (A.AGES - 9))}
for sigma in (0.2, 0.3):
    print(f"sigma {sigma}")
    for name, w in scen.items():
        true_ages = A.AGES + w if np.isscalar(w) else np.array(w)
        res = {"lin": [], "iso": []}
        for s in range(200):
            rng = np.random.default_rng(10000 + s)
            c = A.simulate_cubes({"L1": w}, rng, labels=["L1", "L5"], sigma=sigma)
            m5, m1 = per_model_means(c["L5"]), per_model_means(c["L1"])
            for kind, f in (("lin", linear_read), ("iso", iso_read)):
                sh, tr = [], []
                for m in range(6):
                    if np.polyfit(A.AGES, m5[m], 1)[0] > -0.02:
                        continue
                    a = f(m5[m], m1[m])
                    a = np.clip(a, A.AGES[0] - 3, A.AGES[-1] + 3)
                    sh.append(np.mean(a - A.AGES)); tr.append(np.polyfit(A.AGES, a, 1)[0])
                res[kind].append((np.mean(sh), np.mean(tr)))
        ts, tt = np.mean(true_ages - A.AGES), np.polyfit(A.AGES, true_ages, 1)[0]
        line = f"  {name:28s} true shift {ts:+.2f} tracking {tt:.2f} |"
        for kind in ("lin", "iso"):
            arr = np.array(res[kind])
            line += f" {kind}: shift {np.median(arr[:,0]):+.2f} (sd {arr[:,0].std():.2f}) tracking {np.median(arr[:,1]):.2f} (sd {arr[:,1].std():.2f}) |"
        print(line)
