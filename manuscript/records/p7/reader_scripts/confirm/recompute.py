"""Independent recomputation of the post hoc numbers quoted in the revised ART 5 manuscript.
Reads the repository (read only). Does not import exploratory_p7.py; imports analyze only for the
registered probe parser (parse_probe, probe_correct) and compute only for compute.clean (title removal).
Usage: python3 -B recompute.py WORKTREE"""
import sys, json, glob, re, collections
import numpy as np, pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

WT = sys.argv[1]
sys.path.insert(0, WT)
import analyze   # noqa: E402  (registered parser only)
import compute   # noqa: E402  (clean only)

AGE = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
GR = list(AGE); ages = np.array(list(AGE.values()))
TRUTH = {"3H": (6, 7), "4H": (7, 8), "5H": (8, 9), "6H": (9, 10), "7H": (10, 11), "8H": (11, 12)}
MODELS = ["anthropic_balanced", "anthropic_light", "openai_balanced", "openai_light", "mistral_balanced", "mistral_light"]
NAMES = {"anthropic_balanced": "Sonnet", "anthropic_light": "Haiku", "openai_balanced": "Sol", "openai_light": "Luna",
         "mistral_balanced": "Large", "mistral_light": "Small"}
Y = "mean_zipf_content"
cslope = (ages - ages.mean()) / np.sum((ages - ages.mean()) ** 2)

df = pd.read_csv(f"{WT}/results/measures.csv", keep_default_na=False)
df = df[df["kept"].astype(str).str.lower() == "true"].copy()
df[Y] = pd.to_numeric(df[Y])
topics = sorted(df["topic"].unique()); T = len(topics)
print("texts kept", len(df), "topics", T)

# cell means (label, model, grade, topic) over the two genres
cm = df.groupby(["label", "model", "grade", "topic"])[Y].mean()


def topic_series(lab, models, kind):
    """per-topic level or gradient of lab - L5, averaged over the given models (and genres)."""
    out = []
    for t in topics:
        d = np.array([[cm[(lab, m, g, t)] - cm[("L5", m, g, t)] for g in GR] for m in models]).mean(axis=0)
        out.append(d.mean() if kind == "level" else float(cslope @ d))
    return np.array(out)


def tt(x):
    m, se = x.mean(), x.std(ddof=1) / np.sqrt(len(x))
    t = m / se
    return m, se, t, 2 * stats.t.sf(abs(t), len(x) - 1)


print("\n== 1. primary and leave-one-model-out (Table S10)")
tests = [("h2H", "L1", "level"), ("h2P", "L1P", "level"), ("h3H", "L1", "gradient"), ("h3P", "L1P", "gradient")]
for name, lab, kind in tests:
    m, se, t, p = tt(topic_series(lab, MODELS, kind))
    print(f"  all six {name}: {m:+.5f} p={p:.4f}")
for left in MODELS:
    ms = [m for m in MODELS if m != left]
    row = []
    for name, lab, kind in tests:
        m, se, t, p = tt(topic_series(lab, ms, kind))
        row.append(f"{name} {m:+.4f} (p={p:.3f})")
    print(f"  without {NAMES[left]:6s}: " + "; ".join(row))

print("\n== 2. rulers, between-model spread of age-only texts")
l5 = {m: np.array([np.mean([cm[("L5", m, g, t)] for t in topics]) for g in GR]) for m in MODELS}
b = {m: float(np.polyfit(ages, l5[m], 1)[0]) for m in MODELS}
print("  slopes", {NAMES[m]: round(v, 4) for m, v in b.items()})
rng_g = {g: max(l5[m][i] for m in MODELS) - min(l5[m][i] for m in MODELS) for i, g in enumerate(GR)}
print("  between-model range by grade", {g: round(v, 3) for g, v in rng_g.items()}, "min/max", round(min(rng_g.values()), 3), round(max(rng_g.values()), 3))
within = {NAMES[m]: round(abs(b[m]) * 5, 3) for m in MODELS}
print("  within-model change 3H->8H (|slope|*5)", within)
within_obs = {NAMES[m]: round(l5[m][0] - l5[m][-1], 3) for m in MODELS}
print("  observed L5 3H - 8H difference", within_obs)
sesoi_years = {NAMES[m]: round(0.04 / abs(b[m]), 2) for m in MODELS}
print("  SESOI in model-internal years", sesoi_years)

print("\n== 3. per-model and pooled shift/tracking (Table S3), dispersion (Table S11), L2-L1 and L3-L1")
def readings(w=None):
    """returns dict label -> (levels[m], grads[m], slopes[m]) from topic-weighted cell means"""
    w = np.ones(T) if w is None else w
    out = {}
    mean = {}
    for (lab, m, g), s in cm.groupby(level=[0, 1, 2]):
        v = s.to_numpy(); mean[(lab, m, g)] = float(v @ w / w.sum())
    rul = {m: np.array([mean[("L5", m, g)] for g in GR]) for m in MODELS}
    bb = {m: float(cslope @ rul[m]) for m in MODELS}
    for lab in ["L1", "L1P", "L2", "L3", "L4"]:
        lev, grd = {}, {}
        for m in MODELS:
            d = np.array([mean[(lab, m, g)] for g in GR]) - rul[m]
            lev[m], grd[m] = float(d.mean()), float(cslope @ d)
        out[lab] = (lev, grd, bb)
    return out

def pooled(r, lab):
    lev, grd, bb = r[lab]
    return sum(lev.values()) / sum(bb.values()), 1 + sum(grd.values()) / sum(bb.values())

def permodel(r, lab):
    lev, grd, bb = r[lab]
    return {m: lev[m] / bb[m] for m in MODELS}, {m: 1 + grd[m] / bb[m] for m in MODELS}

r0 = readings()
for lab in ["L1", "L1P", "L2", "L3", "L4"]:
    s, t = pooled(r0, lab); sh, tr = permodel(r0, lab)
    print(f"  {lab}: pooled shift {s:+.3f} tracking {t:.3f}; per-model shift", {NAMES[m]: round(v, 2) for m, v in sh.items()},
          "tracking", {NAMES[m]: round(v, 2) for m, v in tr.items()})
    print(f"       SD of six shifts {np.std(list(sh.values()), ddof=1):.3f}, SD of six trackings {np.std(list(tr.values()), ddof=1):.3f}")
    if lab in ("L1", "L1P"):
        for tier, ms in (("balanced", MODELS[0::2]), ("light", MODELS[1::2])):
            print(f"       tier {tier}: mean |shift| {np.mean([abs(sh[m]) for m in ms]):.3f}, mean |tracking-1| {np.mean([abs(tr[m] - 1) for m in ms]):.3f}")
s1, t1 = pooled(r0, "L1")
for lab in ("L2", "L3"):
    s, t = pooled(r0, lab)
    print(f"  {lab} - L1: shift difference {s - s1:+.3f} years, tracking difference {t - t1:+.3f}")

# bootstrap over topics: own seed, and then the script's seed/order to see if it reproduces exactly
def boot_diffs(seed, B=2000):
    rng = np.random.default_rng(seed)
    out = {"L2": [], "L3": [], "haiku3H": [], "sdlev": []}
    for _ in range(B):
        w = np.bincount(rng.integers(0, T, T), minlength=T).astype(float)
        r = readings(w)
        s1b, _ = pooled(r, "L1")
        for lab in ("L2", "L3"):
            out[lab].append(pooled(r, lab)[0] - s1b)
    return out

for seed in (7, 20261101):
    bd = boot_diffs(seed, 2000)
    print(f"  bootstrap seed {seed}: L2-L1 shift 95% [{np.percentile(bd['L2'], 2.5):.3f}, {np.percentile(bd['L2'], 97.5):.3f}]; "
          f"L3-L1 [{np.percentile(bd['L3'], 2.5):.3f}, {np.percentile(bd['L3'], 97.5):.3f}]")

print("\n== 4. between-model SD of mean levels (absolute Zipf) for L1 and L3")
def sd_levels(w=None):
    w = np.ones(T) if w is None else w
    out = {}
    for lab in ("L1", "L1P", "L3", "L5"):
        lev = []
        for m in MODELS:
            v = np.array([[cm[(lab, m, g, t)] for t in topics] for g in GR])  # grades x topics
            lev.append(float((v @ w / w.sum()).mean()))
        out[lab] = float(np.std(lev, ddof=1))
    return out
p0 = sd_levels()
print("  point:", {k: round(v, 4) for k, v in p0.items()}, "L3-L1:", round(p0["L3"] - p0["L1"], 4))
rng = np.random.default_rng(11); dd = []
for _ in range(2000):
    w = np.bincount(rng.integers(0, T, T), minlength=T).astype(float); s = sd_levels(w); dd.append(s["L3"] - s["L1"])
print(f"  bootstrap (seed 11) of SD(L3)-SD(L1): [{np.percentile(dd, 2.5):.4f}, {np.percentile(dd, 97.5):.4f}]")
# also per-grade SD averaged (the R1 quantity), for comparison
pg = {lab: np.mean([np.std([np.mean([cm[(lab, m, g, t)] for t in topics]) for m in MODELS], ddof=1) for g in GR]) for lab in ("L1", "L1P", "L3", "L5")}
print("  (for comparison) mean over grades of per-grade between-model SD:", {k: round(v, 4) for k, v in pg.items()})

print("\n== 5. observed per-grade offsets (label cell mean - L5 cell mean) / b")
def offsets(w=None):
    r = {}
    w = np.ones(T) if w is None else w
    mean = {}
    for (lab, m, g), s in cm.groupby(level=[0, 1, 2]):
        mean[(lab, m, g)] = float(s.to_numpy() @ w / w.sum())
    for m in MODELS:
        rul = np.array([mean[("L5", m, g)] for g in GR]); bb = float(cslope @ rul)
        for lab in ("L1", "L1P", "L3"):
            for i, g in enumerate(GR):
                r[(m, lab, g)] = (mean[(lab, m, g)] - rul[i]) / bb
    return r
o0 = offsets()
for m in ("anthropic_light", "mistral_light"):
    print(f"  {NAMES[m]} L1 offsets by grade:", {g: round(o0[(m, 'L1', g)], 2) for g in GR})
rng = np.random.default_rng(5); bh = collections.defaultdict(list)
for _ in range(2000):
    w = np.bincount(rng.integers(0, T, T), minlength=T).astype(float); o = offsets(w)
    for k in (("anthropic_light", "L1", "3H"), ("anthropic_light", "L1", "8H"), ("mistral_light", "L1", "3H"), ("mistral_light", "L1", "7H"), ("mistral_light", "L1", "8H")):
        bh[k].append(o[k])
for k, v in bh.items():
    print(f"  {NAMES[k[0]]} {k[1]} {k[2]}: {o0[k]:+.2f} [{np.percentile(v, 2.5):.2f}, {np.percentile(v, 97.5):.2f}]")

print("\n== 6. heterogeneity: two-way ANOVA without replication (topic x model), F(5,75)")
for lab in ("L1", "L1P"):
    for kind in ("level", "gradient"):
        Ymat = np.array([topic_series(lab, [m], kind) for m in MODELS]).T  # topics x models
        gm = Ymat.mean(); ss_tot = ((Ymat - gm) ** 2).sum()
        ss_model = T * ((Ymat.mean(axis=0) - gm) ** 2).sum()
        ss_topic = len(MODELS) * ((Ymat.mean(axis=1) - gm) ** 2).sum()
        ss_err = ss_tot - ss_model - ss_topic
        df1, df2 = len(MODELS) - 1, (len(MODELS) - 1) * (T - 1)
        F = (ss_model / df1) / (ss_err / df2)
        print(f"  {lab} {kind}: F({df1},{df2}) = {F:.2f}, p = {stats.f.sf(F, df1, df2):.2g}")

print("\n== 7. equivalence (TOST against +/-0.04, 90% CI)")
for name, lab in (("H", "L1"), ("P", "L1P")):
    x = topic_series(lab, MODELS, "level"); m, se, t, p = tt(x)
    q = stats.t.ppf(0.95, T - 1)
    p_tost = max(stats.t.sf((m + 0.04) / se, T - 1), stats.t.cdf((m - 0.04) / se, T - 1))
    print(f"  {name}: est {m:+.4f} 90% CI [{m - q * se:.4f}, {m + q * se:.4f}] TOST p = {p_tost:.2g}; 95% CI [{m - stats.t.ppf(0.975, T-1)*se:.4f}, {m + stats.t.ppf(0.975, T-1)*se:.4f}]")

print("\n== 8. tracking precision for L1P: pooled tracking with 100,000 resamples (own seed 3)")
cells = {}
for (lab, m, g), s in cm.groupby(level=[0, 1, 2]):
    if lab in ("L1P", "L5"):
        cells[(lab, m, g)] = s.to_numpy()
rng = np.random.default_rng(3); vals = []
Wb = np.stack([np.bincount(rng.integers(0, T, T), minlength=T) for _ in range(100000)]).T.astype(float)
num = np.zeros(Wb.shape[1]); den = np.zeros(Wb.shape[1])
for m in MODELS:
    rul = np.stack([cells[("L5", m, g)] @ Wb / Wb.sum(0) for g in GR])    # grades x B
    lab_ = np.stack([cells[("L1P", m, g)] @ Wb / Wb.sum(0) for g in GR])
    bb = cslope @ rul; gg = cslope @ (lab_ - rul)
    num += gg; den += bb
tr = 1 + num / den
print(f"  95% percentile [{np.percentile(tr, 2.5):.4f}, {np.percentile(tr, 97.5):.4f}], share >= 1: {np.mean(tr >= 1):.3f}")

print("\n== 9. L0 default age intervals")
l0 = df[df["label"] == "L0"]
for m in MODELS:
    s = l0[l0["model"] == m].groupby("topic")[Y].mean().reindex(topics).to_numpy()
    rul = np.stack([cells.get(("L5", m, g), cm.xs(("L5", m, g)).reindex(topics).to_numpy()) for g in GR])
    def age(w):
        r = rul @ w / w.sum(); bb = cslope @ r
        return 9 + (s @ w / w.sum() - r.mean()) / bb
    pt = age(np.ones(T)); rng = np.random.default_rng(9); bs = [age(np.bincount(rng.integers(0, T, T), minlength=T).astype(float)) for _ in range(2000)]
    print(f"  {NAMES[m]}: {pt:.2f} [{np.percentile(bs, 2.5):.2f}, {np.percentile(bs, 97.5):.2f}]")

print("\n== 10. probes: registered parser")
p = pd.read_csv(f"{WT}/results/probes.csv", keep_default_na=False)
wrong = correct = later = tol = multi = parsed = 0
for r in p.itertuples():
    if str(r.ok).lower() not in ("true", "1"): continue
    found = analyze.parse_probe(r.text)
    if not found: continue
    parsed += 1
    multi += len(set(found)) > 1
    lo, hi = found[0]; mid = (lo + hi) / 2
    if analyze.probe_correct(lo, hi, r.truth_age_from, r.truth_age_to):
        correct += 1; tol += not (r.truth_age_from <= mid <= r.truth_age_to)
    else:
        wrong += 1; later += any(analyze.probe_correct(a, c, r.truth_age_from, r.truth_age_to) for a, c in found[1:])
print(f"  parsed {parsed} of {len(p)}; correct first {correct}, wrong first {wrong}, wrong with a correct range later {later}, correct only through tolerance {tol}, multiple ranges {multi/len(p):.3f}")

print("\n== 11. reasoning tokens: share of texts with reasoning > 0, by model and label")
recs = {}
for fn in sorted(glob.glob(f"{WT}/data/raw/calls_2026110*.jsonl")):
    for line in open(fn):
        r = json.loads(line)
        if str(r.get("ok")).lower() == "true": recs[r["call_id"]] = r
rows = []
for r in df.itertuples():
    u = recs[r.call_id]["response"].get("usage", {})
    n = (u.get("output_tokens_details") or {}).get("thinking_tokens") if "output_tokens_details" in u else (u.get("completion_tokens_details") or {}).get("reasoning_tokens")
    rows.append((r.model, r.label, (n or 0) > 0))
rt = pd.DataFrame(rows, columns=["model", "label", "pos"]).groupby(["model", "label"])["pos"].mean().unstack("label")
print((100 * rt).round(0).to_string())

print("\n== 12. Mistral Large 4 reasoning traces")
EN = re.compile(r"(\d{1,2})\s*(?:(?:-|–|—|to|or|and)\s*(\d{1,2})\s*)?[- ]?years?[- ]?olds?\b")
def stated(text):
    t = (text or "").replace("\xa0", " ").lower()
    for w, n in analyze.NUMBER_WORDS.items(): t = re.sub(rf"\b{w}\b", str(n), t)
    f = [(m.start(), int(m.group(1)), int(m.group(2) or m.group(1))) for m in analyze.AGE_RE.finditer(t)]
    f += [(m.start(), int(m.group(1)), int(m.group(2) or m.group(1))) for m in EN.finditer(t)]
    for _, lo, hi in sorted(f):
        if 4 <= (lo + hi) / 2 <= 16: return lo, hi
    return None
def think(rec):
    msg = rec["response"]["choices"][0]["message"]; parts = []
    if isinstance(msg.get("content"), list):
        for x in msg["content"]:
            if x.get("type") == "thinking":
                for y in x.get("thinking") or []:
                    if isinstance(y, dict) and y.get("type") == "text": parts.append(y.get("text", ""))
    return "\n".join(parts)
d = df[(df["model"] == "mistral_balanced") & df["label"].isin(["L1", "L1P", "L2", "L3", "L4", "L5"])].copy()
st = []
for r in d.itertuples():
    f = stated(think(recs[r.call_id]))
    if f:
        lo, hi = f; t0, t1 = TRUTH[r.grade]; err = (lo + hi) / 2 - (t0 + t1) / 2
        st.append((True, err, not analyze.probe_correct(lo, hi, t0, t1), 1.5 <= err <= 2.5))
    else:
        st.append((False, np.nan, np.nan, np.nan))
d[["has", "err", "wrong", "two"]] = pd.DataFrame(st, index=d.index)
for lab, g in d.groupby("label"):
    h = g[g["has"]]
    print(f"  {lab}: stating {g['has'].mean()*100:.0f}%, wrong {h['wrong'].astype(float).mean()*100:.0f}%, two years too old {h['two'].astype(float).mean()*100:.0f}%, mean error {h['err'].mean():.2f}")
l5i = d[d["label"] == "L5"].set_index(["grade", "genre", "topic"])[Y]
slope_large = b["mistral_balanced"]
for lab in ("L1", "L1P"):
    g = d[(d["label"] == lab) & d["has"]].copy()
    g["diff"] = [row[Y] - l5i[(row["grade"], row["genre"], row["topic"])] for _, row in g.iterrows()]
    g["correct"] = ~g["wrong"].astype(bool)
    sub = g[g["correct"] | g["two"].astype(bool)].copy(); sub["old2"] = sub["two"].astype(bool).astype(float)
    grp = pd.factorize(sub["topic"])[0]
    fit = smf.ols("diff ~ old2 + C(grade) + C(genre)", data=sub).fit(cov_type="cluster", cov_kwds={"groups": grp, "use_correction": True})
    raw = smf.ols("diff ~ old2", data=sub).fit(cov_type="cluster", cov_kwds={"groups": grp, "use_correction": True})
    print(f"  {lab}: n correct {int(sub['correct'].sum())}, n two-years-old {int(sub['old2'].sum())}; adjusted diff {fit.params['old2']:+.4f} (SE {fit.bse['old2']:.4f}, p {fit.pvalues['old2']:.3f}); unadjusted {raw.params['old2']:+.4f} (SE {raw.bse['old2']:.4f}); 2 x slope = {2*slope_large:+.4f}; share {fit.params['old2']/(2*slope_large):.2f}")
    print("     two-years-old by grade:", sub.groupby("grade")["old2"].sum().astype(int).to_dict(), " correct by grade:", sub.groupby("grade")["correct"].sum().astype(int).to_dict())

print("\n== 13. Swiss words in L2 and L5 bodies (compute.clean)")
for lab in ("L1", "L2", "L3", "L5"):
    dd_ = df[df["label"] == lab]; c = collections.Counter()
    for r in dd_.itertuples():
        _, lines = compute.clean(recs[r.call_id]["text"]); body = "\n".join(lines).lower()
        c["romand"] += bool(re.search(r"\bromand(?:e|s|es)?\b", body)); c["canton"] += bool(re.search(r"\bcantons?\b", body))
    print(f"  {lab}: n {len(dd_)}, texts with romand* {c['romand']}, with canton(s) {c['canton']}")

print("\n== 14. power grid")
sp = json.load(open(f"{WT}/sim_power_results.json"))
grid = sp["grid"]
print("  sigmas in grid:", sorted({g['sigma'] for g in grid}), "T:", sorted({g['T'] for g in grid}), "slopes:", sorted({g['slope'] for g in grid}))
for g in grid:
    if g["T"] == 16 and g["slope"] == -0.04:
        print(f"  T=16 slope=-0.04 sigma={g['sigma']}: half_tracking {g.get('half_tracking')}, ignored {g.get('ignored')}, keys {list(g.keys())}")
print("  pilot sigma_upper80:", json.load(open(f"{WT}/results/pilot_summary.json"))["ruler"]["sigma_upper80"])
print("  assumptions:", sp.get("assumptions"))
