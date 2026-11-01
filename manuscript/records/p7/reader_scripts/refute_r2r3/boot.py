"""Topic bootstrap of pooled and per-model shift/tracking, written independently of analyze.py.
1) registered seed and RNG order (one rng.integers(0, T, T) per resample) -> must reproduce numbers.json
2) seed dependence of the L1P tracking upper limit at B = 2000 (200 other seeds)
3) converged limits at large B
4) bootstrap of between-model SDs (S1, S5)"""
import sys, json
sys.path.insert(0, "/tmp/refute_r2r3")
import numpy as np
from core import *

Y, L0, models, genres, topics = load()
T = len(topics)
labs = ["L1", "L1P", "L2", "L3", "L4", "L5"]
S = np.stack([np.nansum(Y[l], axis=2) for l in labs])          # (labels, M, G, T)
C = np.stack([np.isfinite(Y[l]).sum(axis=2) for l in labs]).astype(float)
cg = AGES - AGES.mean(); cg = cg / np.sum(cg ** 2)


def stats_from_W(W):
    """W: (B, T) topic weights -> dict label -> per-model shift, track (B, M) and pooled (B,)"""
    means = (S @ W.T) / (C @ W.T)                                # (labels, M, G, B)
    L5 = means[labs.index("L5")]
    b = np.einsum("g,mgb->mb", cg, L5)                           # (M, B)
    out = {}
    for i, l in enumerate(labs):
        if l == "L5":
            continue
        d = means[i] - L5
        lev = d.mean(axis=1)                                     # (M, B)
        grd = np.einsum("g,mgb->mb", cg, d)
        out[l] = dict(shift_m=(lev / b).T, track_m=(1 + grd / b).T,
                      shift=lev.sum(0) / b.sum(0), track=1 + grd.sum(0) / b.sum(0))
    return out


def weights_seq(seed, B):
    rng = np.random.default_rng(seed)
    return np.stack([np.bincount(rng.integers(0, T, T), minlength=T) for _ in range(B)]).astype(float)


def pct(x):
    return np.percentile(x, [2.5, 97.5])


point = stats_from_W(np.ones((1, T)))
W = weights_seq(20261025, 2000)
bs = stats_from_W(W)
num = json.load(open(f"{REPO}/results/numbers.json"))["age_equivalent"]["by_label"]
print("== registered seed 20261025, B = 2000 (mine vs numbers.json)")
for l in ["L1", "L1P", "L2", "L3", "L4"]:
    print(l, "shift", np.round(pct(bs[l]["shift"]), 4), np.round(num[l]["shift_ci95"], 4),
          "track", np.round(pct(bs[l]["track"]), 4), np.round(num[l]["tracking_ci95"], 4))

print("== seed dependence at B = 2000, 200 seeds (1..200)")
ups, upsH = [], []
for s in range(1, 201):
    b2 = stats_from_W(weights_seq(s, 2000))
    ups.append(pct(b2["L1P"]["track"])[1]); upsH.append(pct(b2["L1"]["track"])[1])
ups = np.array(ups); upsH = np.array(upsH)
print("L1P tracking upper: mean %.4f SD %.4f min %.4f max %.4f share<1 %.3f" % (ups.mean(), ups.std(ddof=1), ups.min(), ups.max(), (ups < 1).mean()))
print("L1 tracking upper:  mean %.4f SD %.4f min %.4f max %.4f" % (upsH.mean(), upsH.std(ddof=1), upsH.min(), upsH.max()))

print("== large B (200,000, seed 7)")
rng = np.random.default_rng(7)
acc = {k: [] for k in ["L1P_track", "L1_track", "L1_shift", "L1P_shift"]}
for chunk in range(20):
    Wb = np.stack([np.bincount(r, minlength=T) for r in rng.integers(0, T, (10000, T))]).astype(float)
    bb = stats_from_W(Wb)
    acc["L1P_track"].append(bb["L1P"]["track"]); acc["L1_track"].append(bb["L1"]["track"])
    acc["L1_shift"].append(bb["L1"]["shift"]); acc["L1P_shift"].append(bb["L1P"]["shift"])
for k, v in acc.items():
    v = np.concatenate(v)
    print(k, "percentile 95%", np.round(pct(v), 4), "P(>=1)" if "track" in k else "", round(float((v >= 1).mean()), 4) if "track" in k else "")

print("== between-model SD of per-model point estimates, with topic-bootstrap 95% (B = 2000, registered seed)")
for l in ["L1", "L1P", "L2", "L3", "L4"]:
    sd_s = bs[l]["shift_m"].std(axis=1, ddof=1); sd_t = bs[l]["track_m"].std(axis=1, ddof=1)
    print(l, "SD shift %.3f %s  SD track %.3f %s" % (point[l]["shift_m"][0].std(ddof=1), np.round(pct(sd_s), 2),
                                                    point[l]["track_m"][0].std(ddof=1), np.round(pct(sd_t), 2)))
for a in ["L1P", "L2", "L4"]:
    for kind in ["shift_m", "track_m"]:
        diff = bs["L3"][kind].std(axis=1, ddof=1) - bs[a][kind].std(axis=1, ddof=1)
        print(f"SD(L3) - SD({a}) {kind}: point %.3f 95%% %s P(L3 smaller) %.2f" % (
            point["L3"][kind][0].std(ddof=1) - point[a][kind][0].std(ddof=1), np.round(pct(diff), 2), (diff < 0).mean()))
for kind in ["shift_m", "track_m"]:
    diff = bs["L1"][kind].std(axis=1, ddof=1) - bs["L3"][kind].std(axis=1, ddof=1)
    print(f"SD(L1) - SD(L3) {kind}: point %.3f 95%% %s" % (point["L1"][kind][0].std(ddof=1) - point["L3"][kind][0].std(ddof=1), np.round(pct(diff), 2)))
keep = [i for i, m in enumerate(models) if m != "anthropic_light"]
for kind in ["shift_m", "track_m"]:
    print("without Haiku", kind, "SD L1 %.2f SD L3 %.2f SD L1P %.2f" % tuple(point[l][kind][0][keep].std(ddof=1) for l in ["L1", "L3", "L1P"]))

print("== L2 - L1 in years (shift difference) and L3 - L1, bootstrap (registered seed)")
for a, b_ in [("L2", "L1"), ("L3", "L1"), ("L1P", "L1")]:
    d = bs[a]["shift"] - bs[b_]["shift"]
    print(a, "-", b_, "shift diff point %.3f 95%% %s" % (point[a]["shift"][0] - point[b_]["shift"][0], np.round(pct(d), 2)))
