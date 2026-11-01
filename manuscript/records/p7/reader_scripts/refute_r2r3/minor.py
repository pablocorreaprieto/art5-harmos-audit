import sys
sys.path.insert(0, "/tmp/refute_r2r3")
import numpy as np
from scipy import stats
from core import *

Y, L0, models, genres, topics = load()
T = len(topics)
means = cell_means_w(Y)
cg = AGES - AGES.mean(); cgn = cg / np.sum(cg ** 2)

print("== m8: linearity of each L5 ruler, topic-level Hotelling T2 on the 4 non-linear orthogonal polynomial contrasts")
P = np.vander(AGES - AGES.mean(), 6, increasing=True)
Q, _ = np.linalg.qr(P)            # orthonormal polynomial basis, columns degree 0..5
NL = Q[:, 2:]                      # degrees 2..5
for i, m in enumerate(models):
    gm = np.nanmean(Y["L5"][i], axis=1)          # grades x topics (mean over genres)
    X = (NL.T @ gm).T                             # topics x 4
    n, p = X.shape
    xb = X.mean(0); S = np.cov(X, rowvar=False)
    T2 = n * xb @ np.linalg.solve(S, xb)
    F = (n - p) / (p * (n - 1)) * T2
    pv = stats.f.sf(F, p, n - p)
    print(f"  {NAMES[m]:7s} Hotelling p = {pv:.3f}")

print("== m3: per-grade offsets of the L1 texts, fitted line vs observed (years)")
from numpy import interp


def pava_dec(y):
    blocks = [[float(v), 1] for v in y]
    i = 0
    while i < len(blocks) - 1:
        if blocks[i][0] < blocks[i + 1][0]:
            v = (blocks[i][0] * blocks[i][1] + blocks[i + 1][0] * blocks[i + 1][1]) / (blocks[i][1] + blocks[i + 1][1])
            blocks[i] = [v, blocks[i][1] + blocks[i + 1][1]]; del blocks[i + 1]; i = max(i - 1, 0)
        else:
            i += 1
    return np.array([v for v, w in blocks for _ in range(w)])


for name in ["mistral_light", "anthropic_light", "openai_light"]:
    i = models.index(name)
    ruler = means["L5"][i]; b = np.polyfit(AGES, ruler, 1)[0]
    d = means["L1"][i] - ruler
    sh = d.mean() / b; tr = 1 + (cgn @ d) / b
    fitted = sh + (tr - 1) * (AGES - AGES.mean())
    obs_ratio = d / b
    iso = pava_dec(ruler)
    # inverse lookup on the isotonic curve (strictly decreasing parts), linear extrapolation outside
    vals, ages = [], []
    k = 0
    while k < 6:
        j = k
        while j + 1 < 6 and abs(iso[j + 1] - iso[k]) < 1e-12:
            j += 1
        vals.append(iso[k]); ages.append(AGES[k:j + 1].mean()); k = j + 1
    vals = np.array(vals); ages = np.array(ages)
    look = []
    for g in range(6):
        v = means["L1"][i, g]
        if v > vals[0]:
            a = ages[0] + (v - vals[0]) / b
        elif v < vals[-1]:
            a = ages[-1] + (v - vals[-1]) / b
        else:
            a = interp(v, vals[::-1], ages[::-1])
        look.append(a - AGES[g])
    print(f"  {NAMES[name]}: fitted", np.round(fitted, 1), "| dZipf/b", np.round(obs_ratio, 1), "| isotonic lookup", np.round(look, 1))

print("== m2: L0 default age, topic bootstrap (registered seed, B = 2000), and L6 readings")
L0m = np.nanmean(L0, axis=1)  # models x topics
rng = np.random.default_rng(20261025)
S5 = np.nansum(Y["L5"], axis=2); C5 = np.isfinite(Y["L5"]).sum(axis=2)
boots = []
for _ in range(2000):
    w = np.bincount(rng.integers(0, T, T), minlength=T).astype(float)
    r = (S5 @ w) / (C5 @ w)
    bb = np.array([np.polyfit(AGES, r[m], 1)[0] for m in range(6)])
    l0 = (L0m @ w) / w.sum()
    boots.append(9 + (l0 - r.mean(1)) / bb)
boots = np.array(boots)
r = means["L5"]; bb = np.array([np.polyfit(AGES, r[m], 1)[0] for m in range(6)])
pt = 9 + (L0m.mean(1) - r.mean(1)) / bb
for m in range(6):
    print(f"  {NAMES[models[m]]:7s} L0 age {pt[m]:.2f} [{np.percentile(boots[:, m], 2.5):.2f}, {np.percentile(boots[:, m], 97.5):.2f}]")
g3 = [0, 1, 2]
for m in range(6):
    d6 = means["L6"][m, g3] - means["L5"][m, g3]
    print(f"  {NAMES[models[m]]:7s} L6 reading per grade AGE + d/b:", np.round(AGES[g3] + d6 / bb[m], 1),
          " via line 9+(L6-mean ruler)/b:", np.round(9 + (means['L6'][m, g3] - r[m].mean()) / bb[m], 1))
