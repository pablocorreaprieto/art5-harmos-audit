"""Independent implementation of shift/tracking (pooled and per model) and of the topic bootstrap, with checks of the
percentile interval against alternatives (BCa, jackknife-t, delta method, Fieller-like). Nothing written to the repo."""
import sys
import numpy as np
import pandas as pd
from scipy import stats

REPO = sys.argv[1]
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 99
B = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
df = pd.read_csv(f"{REPO}/results/measures.csv", keep_default_na=False, na_values=["", "nan", "NaN"])
Y = "mean_zipf_content"
AGE = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
G = list(AGE); ages = np.array(list(AGE.values()))
models = sorted(df.model.unique()); topics = sorted(df.topic.unique())
labs = ["L1", "L1P", "L2", "L3", "L4", "L5"]
# array: label, model, grade, topic  (mean over genres)
A = np.full((len(labs) + 1, len(models), 6, len(topics)), np.nan)
for i, lab in enumerate(labs + ["L6"]):
    d = df[df.label == lab]
    g = d.groupby(["model", "grade", "topic"])[Y].mean()
    for (m, gr, t), v in g.items():
        A[i, models.index(m), G.index(gr), topics.index(t)] = v
labs = labs + ["L6"]
T = len(topics)
c = ages - ages.mean(); wg = c / (c ** 2).sum()

def est(w, lab, grades=None):
    """pooled shift, tracking and per-model arrays, topic weights w"""
    grades = list(range(6)) if grades is None else grades
    mean = np.tensordot(A, w / w.sum(), axes=([3], [0]))  # label, model, grade
    r = mean[labs.index("L5")]  # model, grade
    b = np.array([np.polyfit(ages, r[m], 1)[0] for m in range(len(models))])
    x = mean[labs.index(lab)][:, grades] - r[:, grades]
    a = ages[grades]; cc = a - a.mean(); wgl = cc / (cc ** 2).sum()
    level = x.mean(axis=1); grad = x @ wgl
    return level.sum() / b.sum(), 1 + grad.sum() / b.sum(), level / b, 1 + grad / b, b

rng = np.random.default_rng(SEED)
W = np.stack([np.bincount(rng.integers(0, T, T), minlength=T).astype(float) for _ in range(B)])
for lab, grades in [("L1", None), ("L1P", None), ("L2", None), ("L3", None), ("L4", None), ("L6", [0, 1, 2])]:
    p = est(np.ones(T), lab, grades)
    bs = np.array([est(w, lab, grades)[:2] for w in W])
    # jackknife over topics
    jk = np.array([est(np.where(np.arange(T) == i, 0.0, 1.0), lab, grades)[:2] for i in range(T)])
    print(f"=== {lab}: shift {p[0]:.4f} tracking {p[1]:.4f}")
    for k, nm in enumerate(["shift", "tracking"]):
        pc = np.percentile(bs[:, k], [2.5, 97.5])
        # BCa
        z0 = stats.norm.ppf((bs[:, k] < p[k]).mean())
        jm = jk[:, k].mean(); num = ((jm - jk[:, k]) ** 3).sum(); den = 6 * (((jm - jk[:, k]) ** 2).sum()) ** 1.5
        acc = num / den
        al = stats.norm.cdf(z0 + (z0 + stats.norm.ppf([.025, .975])) / (1 - acc * (z0 + stats.norm.ppf([.025, .975]))))
        bca = np.percentile(bs[:, k], 100 * al)
        # jackknife SE and t(15) interval
        se_jk = np.sqrt((T - 1) / T * ((jk[:, k] - jm) ** 2).sum())
        tq = stats.t.ppf(.975, T - 1)
        se_b = bs[:, k].std(ddof=1)
        print(f"  {nm}: percentile [{pc[0]:.3f},{pc[1]:.3f}] (width {pc[1]-pc[0]:.3f}) | BCa [{bca[0]:.3f},{bca[1]:.3f}] | "
              f"jackknife-SE {se_jk:.4f} t15-interval [{p[k]-tq*se_jk:.3f},{p[k]+tq*se_jk:.3f}] (width {2*tq*se_jk:.3f}) | boot-SE {se_b:.4f} z-interval width {2*1.96*se_b:.3f}")
    if lab in ("L1", "L1P"):
        # per-model
        for mi, m in enumerate(models):
            bsm = np.array([[est(w, lab, grades)[2][mi], est(w, lab, grades)[3][mi]] for w in W[:2000]])
            print(f"   {m}: shift {p[2][mi]:.3f} [{np.percentile(bsm[:,0],2.5):.2f},{np.percentile(bsm[:,0],97.5):.2f}] tracking {p[3][mi]:.3f} [{np.percentile(bsm[:,1],2.5):.2f},{np.percentile(bsm[:,1],97.5):.2f}]  ruler slope {p[4][mi]:.4f}")
print("sum of slopes", est(np.ones(T), "L1")[4].sum(), "mean slope", est(np.ones(T), "L1")[4].mean())
