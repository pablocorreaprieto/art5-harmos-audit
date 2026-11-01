"""Monte Carlo error of the percentile limits of the pooled tracking and shift intervals at B = 2000 (the preregistered B),
and the converged limits at large B. Nothing written to the repo."""
import sys
import numpy as np
import pandas as pd

REPO = sys.argv[1]
df = pd.read_csv(f"{REPO}/results/measures.csv", keep_default_na=False, na_values=["", "nan", "NaN"])
Y = "mean_zipf_content"
AGE = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
G = list(AGE); ages = np.array(list(AGE.values()))
models = sorted(df.model.unique()); topics = sorted(df.topic.unique())
T = len(topics)
def arr(lab):
    a = np.full((len(models), 6, T), np.nan)
    g = df[df.label == lab].groupby(["model", "grade", "topic"])[Y].mean()
    for (m, gr, t), v in g.items():
        a[models.index(m), G.index(gr), topics.index(t)] = v
    return a
L5 = arr("L5"); L1 = arr("L1"); L1P = arr("L1P")
c = ages - ages.mean(); wg = c / (c ** 2).sum()
Xp = np.vstack([np.ones(6), ages]).T
pinv = np.linalg.pinv(Xp)  # slope = pinv[1] @ y

def est_all(W):
    """W: (B, T) topic weights -> arrays (B,) for L1/L1P shift and tracking"""
    out = {}
    w = W / W.sum(axis=1, keepdims=True)
    m5 = np.einsum("mgt,bt->bmg", L5, w)
    b = m5 @ pinv[1]  # (B, M)
    for name, A in (("L1", L1), ("L1P", L1P)):
        mA = np.einsum("mgt,bt->bmg", A, w)
        x = mA - m5
        level = x.mean(axis=2); grad = x @ wg
        out[name] = (level.sum(1) / b.sum(1), 1 + grad.sum(1) / b.sum(1))
    return out

pt = est_all(np.ones((1, T)))
print("point:", {k: (float(v[0][0]), float(v[1][0])) for k, v in pt.items()})
# distribution of the 2.5/97.5 percentile limits across seeds at B = 2000
lims = {k: [] for k in ("L1", "L1P")}
for s in range(200):
    rng = np.random.default_rng(1000 + s)
    W = np.stack([np.bincount(rng.integers(0, T, T), minlength=T) for _ in range(2000)]).astype(float)
    e = est_all(W)
    for k in lims:
        lims[k].append(np.r_[np.percentile(e[k][0], [2.5, 97.5]), np.percentile(e[k][1], [2.5, 97.5])])
for k in lims:
    a = np.array(lims[k])
    print(k, "limits over 200 seeds at B=2000: shift lo/hi mean", a[:, 0].mean().round(3), a[:, 1].mean().round(3), "sd", a[:, 0].std().round(4), a[:, 1].std().round(4),
          "| tracking lo/hi mean", a[:, 2].mean().round(3), a[:, 3].mean().round(3), "sd", a[:, 2].std().round(4), a[:, 3].std().round(4),
          "| share of seeds with tracking hi < 1:", float((a[:, 3] < 1).mean()), " min/max hi", a[:, 3].min().round(4), a[:, 3].max().round(4))
# the preregistered seed, replicating analyze.py's draw order (rng.integers(0, T, T) per resample)
rng = np.random.default_rng(20261025)
W = np.stack([np.bincount(rng.integers(0, T, T), minlength=T) for _ in range(2000)]).astype(float)
e = est_all(W)
for k in e:
    print("prereg seed", k, "shift", np.percentile(e[k][0], [2.5, 97.5]).round(4), "tracking", np.percentile(e[k][1], [2.5, 97.5]).round(4))
# converged limits (B = 400k in chunks)
rng = np.random.default_rng(7)
acc = {k: ([], []) for k in ("L1", "L1P")}
for _ in range(40):
    W = np.stack([np.bincount(rng.integers(0, T, T), minlength=T) for _ in range(10000)]).astype(float)
    e = est_all(W)
    for k in acc:
        acc[k][0].append(e[k][0]); acc[k][1].append(e[k][1])
for k in acc:
    s = np.concatenate(acc[k][0]); t = np.concatenate(acc[k][1])
    print("B=400000", k, "shift", np.percentile(s, [2.5, 97.5]).round(4), "tracking", np.percentile(t, [2.5, 97.5]).round(4),
          "P(tracking>=1)", float((t >= 1).mean()), "P(shift<=0)", float((s <= 0).mean()))
