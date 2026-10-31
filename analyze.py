"""Confirmatory and secondary analyses for ART 5 (analysis v0.4: the tests of v0.2, plus a
sensitivity analysis without the answers flagged as addressing the user).

python analyze.py MEASURES_CSV [PROBES_CSV|-] [OUT_JSON]   every number the manuscript may quote,
                                                            as named fields of OUT_JSON
python analyze.py --self-test                               planted effects must be found with the
                                                            right sign and size, the null must not
                                                            be rejected; exits non-zero otherwise

Data: one row per text call, from compute.py (columns model, grade, label, genre, topic, kept,
mean_zipf_content, secondary measures, n_words, truncated, duplicate_text).

Two ways for a grade label to fail. Its texts can sit at the wrong level (a constant offset from
the age-only text), or fail to follow the grade (a model that ignores "5H" and writes at its default
level gives texts that are too hard for 3H and too easy for 8H, with a mean offset near zero).
Each is tested.

Pairing. A pair is two kept texts of the same model, grade, genre and topic under two labels.
Per topic t and grade g, d(g, t) is the mean over models and genres of the paired differences.
  level(t)    = mean over the six grades of d(g, t)                       (Zipf)
  gradient(t) = least-squares slope of d(g, t) on the grade's age midpoint (Zipf per year)
A topic is dropped when fewer than half of its pairs are kept or a grade has no pair (counted).
Primary tests: two-sided one-sample t-tests over topics (df = number of topics - 1), Holm over the
  four tests, alpha .05.
  H2-H  level of L1 - L5      bare H label ("de 5H") against the age only ("de 8 à 9 ans")
  H2-P  level of L1P - L5     bare P label ("de 5P")
  H3-H  gradient of L1 - L5   does the H label follow the grade as the age does?
  H3-P  gradient of L1P - L5
  The expected direction of the level is L1 below L5 (rarer words: a reading as an older French or
  Belgian grade), but a reading of the digit as an age gives the opposite, hence two-sided tests.
  A model that ignores the label gives a positive gradient.
H1 (manipulation check, per model): within L5, slope of Y on the age midpoint, OLS with genre and
  topic effects, standard errors clustered by topic, one-sided (slope < 0), t with (number of
  topics - 1) degrees of freedom. No correction.
Age equivalent (descriptive, in model-internal years): each model is read on its own age-only
  ruler, the least-squares line through its six L5 cell means (over genres and topics), slope b.
  For a label, with level and gradient computed from each model's own cell means, the summary over
  the eligible models is shift = sum of levels / sum of slopes b and tracking = 1 + sum of
  gradients / sum of slopes (shift in years, positive = written for older children; tracking 1 =
  follows the grade like the age-only text, 0 = ignores it). Per-model ratios level / b are
  reported as exploratory. Only models with b at most -0.02 Zipf per year are read (a rule on size,
  not on significance); numerator and denominator use the same models. 95% percentile intervals
  from 2,000 bootstrap resamples of topics (seed 20261025), eligibility fixed on the full data. L0 is placed at 9 + (mean L0 - mean L5) / b. Sensitivity: the same shift and tracking read
  by inverse lookup on an isotonic non-increasing fit of the six L5 means (flat runs collapsed to
  their mean age, linear extrapolation beyond the ends, at most three years, counted).
Secondary: the gloss (L3, "de 5H (8 à 9 ans)") against L5 and against L1, level and gradient; the
  four primary contrasts by OLS with model x grade cells, label x model level and gradient terms,
  genre and topic, standard errors clustered by topic; the primary contrasts for every secondary
  measure; sensitivity analyses (length residualised within model, truncated texts removed,
  duplicate texts removed, answers flagged as addressing the user removed); linearity of each L5
  ruler (F test of grade categories against a linear age term); flagged answers and removed
  preface or closing lines counted by label.
Controls: L6 - L5 at 3H to 5H (same digit with the French collège suffix); L0 placed on each ruler.
Exploratory: per-model and per-grade contrasts, L2 and L4, knowledge probes.
"""
import json
import re
import sys
import warnings

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats

AGE_MID = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
GRADES = list(AGE_MID)
AGES = np.array(list(AGE_MID.values()))
ALPHA = 0.05
PRIMARY = [("h2_level_H", "L1", "L5", "level"), ("h2_level_P", "L1P", "L5", "level"),
           ("h3_gradient_H", "L1", "L5", "gradient"), ("h3_gradient_P", "L1P", "L5", "gradient")]
GLOSS = [("gloss_level_vs_age", "L3", "L5", "level"), ("gloss_gradient_vs_age", "L3", "L5", "gradient"),
         ("gloss_level_vs_bare", "L3", "L1", "level"), ("gloss_gradient_vs_bare", "L3", "L1", "gradient")]
GRADED_LABELS = ["L1", "L1P", "L2", "L3", "L4", "L5", "L6"]
MIN_SLOPE = -0.02
MAX_EXTRAPOLATION = 3.0
BOOT = 2000
SEED = 20261025
SECONDARY = ["median_zipf_content", "share_rare_content", "share_below4_content", "mean_word_length",
             "words_per_sentence", "n_words", "kandel_moles", "mean_zipf_form_films"]
Y = "mean_zipf_content"

warnings.filterwarnings("ignore", category=RuntimeWarning)


# ---------- data layout ----------

def axes(df):
    return {"models": sorted(df["model"].unique()), "genres": sorted(df["genre"].unique()),
            "topics": sorted(df["topic"].unique())}


def to_cubes(df, y=Y, ax=None):
    """label -> array (models, grades, genres, topics) of y for kept texts, NaN elsewhere."""
    ax = ax or axes(df)
    shape = (len(ax["models"]), len(GRADES), len(ax["genres"]), len(ax["topics"]))
    cubes = {lab: np.full(shape, np.nan) for lab in GRADED_LABELS}
    d = df[(df["kept"]) & (df["label"].isin(GRADED_LABELS)) & df[y].notna()]
    mi = d["model"].map({m: i for i, m in enumerate(ax["models"])}).to_numpy()
    gi = d["grade"].map({g: i for i, g in enumerate(GRADES)}).to_numpy()
    ei = d["genre"].map({e: i for i, e in enumerate(ax["genres"])}).to_numpy()
    ti = d["topic"].map({t: i for i, t in enumerate(ax["topics"])}).to_numpy()
    for lab in GRADED_LABELS:
        sel = (d["label"] == lab).to_numpy()
        cubes[lab][mi[sel], gi[sel], ei[sel], ti[sel]] = d[y].to_numpy(dtype=float)[sel]
    return cubes


# ---------- topic-level statistics and tests ----------

def weights(kind, grades):
    ages = AGES[grades]
    if kind == "level":
        return np.full(len(grades), 1 / len(grades))
    c = ages - ages.mean()
    return c / np.sum(c ** 2)


def topic_stat(a, b, kind, grades=None, models=None):
    """Per-topic level or gradient of a - b, topics failing the completeness rule dropped."""
    grades = list(range(len(GRADES))) if grades is None else list(grades)
    d = (a - b)[:, grades]
    if models is not None:
        d = d[models]
    full = d.shape[0] * d.shape[1] * d.shape[2]
    n = np.sum(~np.isnan(d), axis=(0, 1, 2))
    dg = np.nanmean(d, axis=(0, 2))  # (grades, topics)
    s = weights(kind, grades) @ dg
    keep = (n >= 0.5 * full) & np.isfinite(s)
    return s[keep], int((~keep).sum())


def ttest(x):
    T = len(x)
    nan = float("nan")
    if T < 3:
        return {"estimate": nan, "se": nan, "t": nan, "df": T - 1, "p_two_sided": nan, "ci95": [nan, nan], "n_topics": T}
    mean, sd = float(np.mean(x)), float(np.std(x, ddof=1))
    se = sd / np.sqrt(T)
    t = mean / se if se > 0 else float("inf") * np.sign(mean)
    q = stats.t.ppf(0.975, T - 1)
    return {"estimate": mean, "se": se, "t": float(t), "df": T - 1, "p_two_sided": float(2 * stats.t.sf(abs(t), T - 1)),
            "ci95": [mean - q * se, mean + q * se], "n_topics": T}


def holm(pvals, alpha=ALPHA):
    keys = sorted(pvals, key=lambda k: pvals[k])
    m = len(keys)
    adjusted, rejected, running, stop = {}, {}, 0.0, False
    for i, k in enumerate(keys):
        running = max(running, min(1.0, (m - i) * pvals[k]))
        adjusted[k] = running
        if not stop and pvals[k] <= alpha / (m - i):
            rejected[k] = True
        else:
            stop = True
            rejected[k] = False
    return adjusted, rejected


def contrast_set(cubes, spec, grades=None):
    out = {}
    for name, a, b, kind in spec:
        x, dropped = topic_stat(cubes[a], cubes[b], kind, grades)
        out[name] = dict(ttest(x), contrast=f"{kind} of {a} - {b}", topics_dropped=dropped)
    return out


def primary_from_cubes(cubes):
    out = contrast_set(cubes, PRIMARY)
    adjusted, rejected = holm({k: (v["p_two_sided"] if np.isfinite(v["p_two_sided"]) else 1.0) for k, v in out.items()})
    for k in out:
        out[k]["p_holm"] = adjusted[k]
        out[k]["rejected_holm"] = bool(rejected[k])
    return out


# ---------- H1 and the ruler ----------

def h1_slopes(df):
    res = {}
    l5 = df[(df["kept"]) & (df["label"] == "L5") & df[Y].notna()].copy()
    l5["age"] = l5["grade"].map(AGE_MID)
    for m, sub in l5.groupby("model"):
        groups = pd.factorize(sub["topic"])[0]
        T = len(set(groups))
        r = smf.ols(f"{Y} ~ age + C(genre) + C(topic)", data=sub).fit(
            cov_type="cluster", cov_kwds={"groups": groups, "use_correction": True})
        b, se = float(r.params["age"]), float(r.bse["age"])
        t = b / se
        p = float(stats.t.cdf(t, T - 1))
        lin = smf.ols(f"{Y} ~ age + C(genre) + C(topic)", data=sub).fit()
        cat = smf.ols(f"{Y} ~ C(grade) + C(genre) + C(topic)", data=sub).fit()
        f, p_f, _ = cat.compare_f_test(lin)
        res[m] = {"slope": b, "se": se, "t": t, "df": T - 1, "p_one_sided": p, "supported": bool(p <= ALPHA),
                  "eligible_for_age_equivalent": bool(b <= MIN_SLOPE),
                  "linearity_F": float(f), "linearity_p": float(p_f)}
    return res


def pava_decreasing(y):
    """Isotonic non-increasing least-squares fit with equal weights."""
    blocks = [[float(v), 1] for v in y]
    i = 0
    while i < len(blocks) - 1:
        if blocks[i][0] < blocks[i + 1][0]:
            v = (blocks[i][0] * blocks[i][1] + blocks[i + 1][0] * blocks[i + 1][1]) / (blocks[i][1] + blocks[i + 1][1])
            blocks[i] = [v, blocks[i][1] + blocks[i + 1][1]]
            del blocks[i + 1]
            i = max(i - 1, 0)
        else:
            i += 1
    return np.array([v for v, w in blocks for _ in range(w)])


def age_equivalent(curve, v, slope):
    """Age at which the non-increasing ruler takes value v, and how it was obtained."""
    if not np.isfinite(v) or not np.all(np.isfinite(curve)):
        return float("nan"), "missing"
    vals, ages = [], []
    i = 0
    while i < len(curve):
        j = i
        while j + 1 < len(curve) and abs(curve[j + 1] - curve[i]) < 1e-12:
            j += 1
        vals.append(curve[i])
        ages.append(float(np.mean(AGES[i:j + 1])))
        i = j + 1
    vals, ages = np.array(vals), np.array(ages)
    if len(vals) == 1 or not slope < 0:
        return float("nan"), "flat"
    if v > vals[0]:
        a, flag = ages[0] + (v - vals[0]) / slope, "extrapolated"
    elif v < vals[-1]:
        a, flag = ages[-1] + (v - vals[-1]) / slope, "extrapolated"
    else:
        a, flag = float(np.interp(v, vals[::-1], ages[::-1])), "inside"
    lo, hi = AGES[0] - MAX_EXTRAPOLATION, AGES[-1] + MAX_EXTRAPOLATION
    if a < lo or a > hi:
        a, flag = min(max(a, lo), hi), "capped"
    return float(a), flag


def cell_means(sums, counts, w=None):
    """sums, counts: (labels, models, grades, topics); w: topic weights of a bootstrap resample."""
    if w is None:
        w = np.ones(sums.shape[-1])
    return (sums @ w) / (counts @ w)


def read_on_rulers(means, labs, eligible, l0=None):
    """Age equivalents (labels x models x grades) on each eligible model's own ruler."""
    i5 = labs.index("L5")
    ages = np.full((len(labs), means.shape[1], len(GRADES)), np.nan)
    flags, l0_age = {}, {}
    for mi in eligible:
        ruler = means[i5, mi]
        if not np.all(np.isfinite(ruler)):
            continue
        slope = float(np.polyfit(AGES, ruler, 1)[0])
        curve = pava_decreasing(ruler)
        for li, lab in enumerate(labs):
            if lab == "L5":
                continue
            for gi in range(len(GRADES)):
                a, flag = age_equivalent(curve, means[li, mi, gi], slope)
                if flag != "missing":
                    flags[flag] = flags.get(flag, 0) + 1
                ages[li, mi, gi] = a
        if l0 is not None:
            l0_age[mi] = age_equivalent(curve, l0[mi], slope)[0]
    return ages, flags, l0_age


def shift_and_tracking(ages_lm):
    """ages_lm: (grades,) age equivalents of one label and model."""
    ok = np.isfinite(ages_lm)
    if ok.sum() == 0:
        return float("nan"), float("nan")
    shift = float(np.mean(ages_lm[ok] - AGES[ok]))
    track = float(np.polyfit(AGES[ok], ages_lm[ok], 1)[0]) if ok.sum() >= 3 else float("nan")
    return shift, track


def label_profile(means, li, i5, m, grades=None):
    """Level and gradient of label li minus L5 for model m from cell means (labels, models, grades)."""
    grades = list(range(len(GRADES))) if grades is None else grades
    d = means[li, m, grades] - means[i5, m, grades]
    if not np.all(np.isfinite(d)):
        return float("nan"), float("nan")
    return float(weights("level", grades) @ d), float(weights("gradient", grades) @ d) if len(grades) >= 3 else float("nan")


def linear_reading(means, labs, eligible, l0=None):
    """shift and tracking per label and eligible model on the model's linear L5 ruler."""
    i5 = labs.index("L5")
    out, l0_age = {}, {}
    for m in eligible:
        ruler = means[i5, m]
        if not np.all(np.isfinite(ruler)):
            continue
        b = float(np.polyfit(AGES, ruler, 1)[0])
        for li, lab in enumerate(labs):
            if lab == "L5":
                continue
            grades = [GRADES.index(g) for g in ("3H", "4H", "5H")] if lab == "L6" else None
            lev, grd = label_profile(means, li, i5, m, grades)
            out.setdefault(lab, {})[m] = (lev, grd, b)
        if l0 is not None and np.isfinite(l0[m]):
            l0_age[m] = 9.0 + (l0[m] - float(np.mean(ruler))) / b
    return out, l0_age


def age_equivalent_block(df, h1, ax):
    labs = GRADED_LABELS
    d = df[(df["kept"]) & df[Y].notna()]
    M, G, T = len(ax["models"]), len(GRADES), len(ax["topics"])
    sums = np.zeros((len(labs), M, G, T))
    counts = np.zeros_like(sums)
    l0_sums, l0_counts = np.zeros((M, T)), np.zeros((M, T))
    mi = {m: i for i, m in enumerate(ax["models"])}
    ti = {t: i for i, t in enumerate(ax["topics"])}
    for r in d.itertuples():
        if r.label == "L0":
            l0_sums[mi[r.model], ti[r.topic]] += getattr(r, Y)
            l0_counts[mi[r.model], ti[r.topic]] += 1
        elif r.label in labs:
            k = (labs.index(r.label), mi[r.model], GRADES.index(r.grade), ti[r.topic])
            sums[k] += getattr(r, Y)
            counts[k] += 1
    eligible = [mi[m] for m in ax["models"] if m in h1 and h1[m]["eligible_for_age_equivalent"]]
    l0 = l0_sums.sum(1) / l0_counts.sum(1) if l0_counts.sum() else None
    means = cell_means(sums, counts)
    point, l0_age = linear_reading(means, labs, eligible, l0)

    def pooled(per_model):
        v = np.array([x for x in per_model.values() if np.isfinite(x[0])])
        if not len(v):
            return float("nan"), float("nan")
        return float(v[:, 0].sum() / v[:, 2].sum()), float(1 + v[:, 1].sum() / v[:, 2].sum())

    rng = np.random.default_rng(SEED)
    boot = {lab: np.full((BOOT, 2), np.nan) for lab in point}
    boot_m = {lab: np.full((BOOT, M, 2), np.nan) for lab in point}
    for bi in range(BOOT):
        w = np.bincount(rng.integers(0, T, T), minlength=T).astype(float)
        bp, _ = linear_reading(cell_means(sums, counts, w), labs, eligible)
        for lab, per_model in bp.items():
            boot[lab][bi] = pooled(per_model)
            for m, (lev, grd, b) in per_model.items():
                boot_m[lab][bi, m] = (lev / b, 1 + grd / b)
    iso_ages, iso_flags, _ = read_on_rulers(means, labs, eligible)
    names = ax["models"]

    def ci(x):
        x = x[np.isfinite(x)]
        return [float(np.percentile(x, 2.5)), float(np.percentile(x, 97.5))] if len(x) else None

    by_label = {}
    for lab, per_model in point.items():
        li = labs.index(lab)
        ms = list(per_model)
        iso = [shift_and_tracking(iso_ages[li, m]) for m in ms]
        sh, tr = pooled(per_model)
        by_label[lab] = {
            "shift_years": sh, "shift_ci95": ci(boot[lab][:, 0]),
            "tracking": tr, "tracking_ci95": ci(boot[lab][:, 1]),
            "isotonic_shift_years": float(np.nanmean([v[0] for v in iso])),
            "isotonic_tracking": float(np.nanmean([v[1] for v in iso])),
            "by_model": {names[m]: {"shift_years": per_model[m][0] / per_model[m][2], "shift_ci95": ci(boot_m[lab][:, m, 0]),
                                    "tracking": 1 + per_model[m][1] / per_model[m][2], "tracking_ci95": ci(boot_m[lab][:, m, 1])}
                         for m in ms}}
    return {"eligible_models": [names[m] for m in eligible], "rule": f"L5 slope <= {MIN_SLOPE} Zipf per year",
            "by_label": by_label, "isotonic_cell_flags": iso_flags,
            "l0_default_age": {names[m]: a for m, a in l0_age.items()},
            "bootstrap": {"resamples": BOOT, "seed": SEED, "unit": "topic"}}


# ---------- secondary analyses ----------

def secondary_ols(df):
    d = df[(df["kept"]) & df["label"].isin(["L1", "L1P", "L5"]) & df[Y].notna()].copy()
    d["mg"] = d["model"] + "_" + d["grade"]
    d["age_c"] = d["grade"].map(AGE_MID) - AGES.mean()
    models = sorted(d["model"].unique())
    code = {m: f"m{i}" for i, m in enumerate(models)}
    terms = []
    for m in models:
        for lab in ["L1", "L1P"]:
            lev, grd = f"lev_{lab}_{code[m]}", f"grd_{lab}_{code[m]}"
            d[lev] = ((d["label"] == lab) & (d["model"] == m)).astype(float)
            d[grd] = d[lev] * d["age_c"]
            terms += [lev, grd]
    groups = pd.factorize(d["topic"])[0]
    T = len(set(groups))
    res = smf.ols(f"{Y} ~ C(mg) + " + " + ".join(terms) + " + C(genre) + C(topic) - 1", data=d).fit(
        cov_type="cluster", cov_kwds={"groups": groups, "use_correction": True})
    names = res.params.index.tolist()
    cov = res.cov_params().to_numpy()
    out = {}
    for name, a, _, kind in PRIMARY:
        c = np.zeros(len(names))
        for m in models:
            c[names.index(f"{'lev' if kind == 'level' else 'grd'}_{a}_{code[m]}")] = 1 / len(models)
        est = float(c @ res.params.to_numpy())
        se = float(np.sqrt(c @ cov @ c))
        t = est / se
        out[name] = {"estimate": est, "se": se, "t": t, "df": T - 1, "p_two_sided": float(2 * stats.t.sf(abs(t), T - 1))}
    return out


def length_residualised(df):
    d = df.copy()
    ok = d["kept"] & d[Y].notna() & (d["n_words"] > 0)
    d.loc[ok, "log_n"] = np.log(d.loc[ok, "n_words"].astype(float))
    fit = smf.ols(f"{Y} ~ C(model) + C(model):log_n", data=d[ok]).fit()
    d.loc[ok, Y] = fit.resid + d.loc[ok, Y].mean()
    d.loc[~ok, Y] = np.nan
    return d


# ---------- probes ----------

NUMBER_WORDS = {"quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10, "onze": 11,
                "douze": 12, "treize": 13, "quatorze": 14, "quinze": 15, "seize": 16}
AGE_RE = re.compile(r"(\d{1,2})\s*(?:(?:à|-|–|—|ou|et)\s*(\d{1,2})\s*)?ans\b")


def parse_probe(text):
    """All age statements of an answer, in order: list of (low, high). The first one is the answer."""
    t = (text or "").replace(" ", " ").replace("\xa0", " ").lower()
    for w, n in NUMBER_WORDS.items():
        t = re.sub(rf"\b{w}\b", str(n), t)
    return [(int(m.group(1)), int(m.group(2) or m.group(1))) for m in AGE_RE.finditer(t)]


def probe_correct(lo, hi, truth_from, truth_to):
    return truth_from - 0.5 <= (lo + hi) / 2 <= truth_to + 0.5


def analyze_probes(probes):
    rows = []
    for r in probes.itertuples():
        found = parse_probe(r.text) if str(r.ok).lower() in ("true", "1") else []
        first = found[0] if found else None
        rows.append({"model": r.model, "notation": r.notation, "probe": r.probe, "grade": r.grade,
                     "parsed": first is not None, "multiple": len(set(found)) > 1,
                     "correct_first": bool(first and probe_correct(*first, r.truth_age_from, r.truth_age_to)),
                     "correct_any": any(probe_correct(lo, hi, r.truth_age_from, r.truth_age_to) for lo, hi in found)})
    p = pd.DataFrame(rows)
    out = {"n": len(p), "share_parsed": float(p["parsed"].mean()), "share_multiple": float(p["multiple"].mean())}
    for keys in (["model", "notation"], ["notation"], ["model", "notation", "grade"]):
        g = p.groupby(keys)[["correct_first", "correct_any", "parsed"]].mean()
        out["accuracy_by_" + "_".join(keys)] = {" | ".join(map(str, k if isinstance(k, tuple) else (k,))): v
                                                 for k, v in g.to_dict("index").items()}
    return out


# ---------- full analysis ----------

def as_bool(s):
    return s.astype(str).str.lower().isin(["true", "1"])


def analyze(df, probes=None):
    df = df.copy()
    df["kept"] = as_bool(df["kept"])
    ax = axes(df[df["label"].isin(GRADED_LABELS)])
    cubes = to_cubes(df, Y, ax)
    out = {"n_texts": int(len(df)), "n_kept": int(df["kept"].sum()), "models": ax["models"], "n_topics": len(ax["topics"]),
           "exclusions_by_reason": df.loc[~df["kept"], "exclusion_reason"].value_counts().to_dict() if "exclusion_reason" in df else {},
           "exclusions_by_label_model_grade": {" | ".join(map(str, k)): int(v) for k, v in
                                               df[~df["kept"]].groupby(["label", "model", "grade"]).size().items()}}
    out["primary"] = primary_from_cubes(cubes)
    h1 = h1_slopes(df)
    out["h1"] = h1
    out["h1_models_supported"] = int(sum(v["supported"] for v in h1.values()))
    out["age_equivalent"] = age_equivalent_block(df, h1, ax)
    out["gloss"] = contrast_set(cubes, GLOSS)
    out["secondary_ols_clustered"] = secondary_ols(df)
    out["secondary_measures"] = {meas: contrast_set(to_cubes(df, meas, ax), PRIMARY)
                                 for meas in SECONDARY if meas in df and df[meas].notna().any()}
    sens = {}
    if "n_words" in df:
        sens["length_residualised"] = primary_from_cubes(to_cubes(length_residualised(df), Y, ax))
    for flag in ("truncated", "duplicate_text", "flag_meta"):
        if flag in df:
            mask = as_bool(df[flag])
            sens[f"without_{flag}"] = dict(primary_from_cubes(to_cubes(df[~mask], Y, ax)), n_removed=int(mask.sum()))
    out["sensitivity"] = sens
    if "flag_meta" in df:  # answers addressing the user, and preface or closing lines removed, by label
        meta = df.assign(flag=as_bool(df["flag_meta"]),
                         lines=pd.to_numeric(df.get("n_meta_lines", 0), errors="coerce").fillna(0) > 0)
        out["meta_by_label"] = {lab: {"n": int(len(g)), "flag_meta": int(g["flag"].sum()),
                                      "meta_lines_removed": int(g["lines"].sum())}
                                for lab, g in meta.groupby("label")}
    g3 = [GRADES.index(g) for g in ("3H", "4H", "5H")]
    out["controls"] = {"l6_vs_l5_level_3h_to_5h": contrast_set(cubes, [("x", "L6", "L5", "level")], g3)["x"],
                       "l6_vs_l5_by_grade": {GRADES[g]: contrast_set(cubes, [("x", "L6", "L5", "level")], [g])["x"] for g in g3}}
    expl = {"other_labels": contrast_set(cubes, [("L2_level", "L2", "L5", "level"), ("L2_gradient", "L2", "L5", "gradient"),
                                                 ("L4_level", "L4", "L5", "level"), ("L4_gradient", "L4", "L5", "gradient"),
                                                 ("P_vs_H_level", "L1P", "L1", "level"), ("P_vs_H_gradient", "L1P", "L1", "gradient")])}
    expl["grade_profile"] = {GRADES[g]: contrast_set(cubes, [("L1", "L1", "L5", "level"), ("L1P", "L1P", "L5", "level"),
                                                             ("L3", "L3", "L5", "level")], [g]) for g in range(len(GRADES))}
    expl["per_model"] = {}
    for i, m in enumerate(ax["models"]):
        expl["per_model"][m] = {name: ttest(topic_stat(cubes[a], cubes[b], kind, models=[i])[0]) for name, a, b, kind in PRIMARY}
    out["exploratory"] = expl
    if probes is not None and len(probes):
        out["probes"] = analyze_probes(probes)
    return out


# ---------- simulation used by the self-test and by sim_power.py ----------

def simulate_cubes(written, rng, n_models=6, n_topics=16, sigma=0.3, slope=-0.04, slope_sd=0.01,
                   tau_lt=0.02, tau_ps=0.0, tau_topic=0.1, missing=0.0, heavy=True, labels=None, n_genres=2,
                   l0_age=None):
    """Cubes (models, grades, genres, topics). written[label] is either a shift in years (the text is
    written for children that much older than the grade) or six written ages, one per grade.
    tau_lt: label x topic effect shared by all models and grades; tau_ps: prompt effect (label x grade
    x genre x topic) shared by all models. Noise: t with 5 df scaled to sigma when heavy.
    With l0_age, also returns an L0 array (models, genres, topics) written for that age."""
    labels = labels or list(written)
    a = rng.normal(4.9, 0.15, n_models)
    b = slope + rng.normal(0, slope_sd, n_models)
    topic = rng.normal(0, tau_topic, n_topics)
    genre = np.array([0.0, 0.08][:n_genres])
    shape = (n_models, len(GRADES), n_genres, n_topics)

    def noise(shp):
        return rng.standard_t(5, shp) * np.sqrt(3 / 5) if heavy else rng.normal(0, 1, shp)

    cubes = {}
    for lab in labels:
        w = written.get(lab, 0.0)
        ages = AGES + w if np.isscalar(w) else np.asarray(w, dtype=float)
        mean = a[:, None, None, None] + b[:, None, None, None] * (ages[None, :, None, None] - 9) \
            + topic[None, None, None, :] + genre[None, None, :, None] \
            + rng.normal(0, tau_lt, n_topics)[None, None, None, :] \
            + (rng.normal(0, tau_ps, (len(GRADES), n_genres, n_topics))[None] if tau_ps else 0.0)
        cube = mean + sigma * noise(shape)
        if missing:
            cube[rng.random(shape) < missing] = np.nan
        cubes[lab] = cube
    if l0_age is None:
        return cubes
    l0 = a[:, None, None] + b[:, None, None] * (l0_age - 9) + topic[None, None, :] + genre[None, :, None] \
        + rng.normal(0, tau_lt, n_topics)[None, None, :] + sigma * noise((n_models, n_genres, n_topics))
    return cubes, l0


def cubes_to_df(cubes, l0=None, rng=None):
    rows = []
    for lab, cube in cubes.items():
        M, G, E, T = cube.shape
        for m in range(M):
            for g in range(G):
                if lab == "L6" and GRADES[g] not in ("3H", "4H", "5H"):
                    continue
                for e in range(E):
                    for t in range(T):
                        v = cube[m, g, e, t]
                        rows.append({"model": f"m{m}", "grade": GRADES[g], "label": lab, "genre": f"e{e}",
                                     "topic": f"t{t:02d}", "kept": bool(np.isfinite(v)),
                                     "exclusion_reason": "" if np.isfinite(v) else "under 20 words",
                                     Y: v if np.isfinite(v) else 0.0,  # excluded texts still carry a value
                                     "n_words": float(rng.lognormal(5.3, 0.3)) if rng is not None else 200.0,
                                     "truncated": False, "duplicate_text": False})
    if l0 is not None:
        M, E, T = l0.shape
        for m in range(M):
            for e in range(E):
                for t in range(T):
                    rows.append({"model": f"m{m}", "grade": "nograde", "label": "L0", "genre": f"e{e}",
                                 "topic": f"t{t:02d}", "kept": True, "exclusion_reason": "", Y: l0[m, e, t],
                                 "n_words": 200.0, "truncated": False, "duplicate_text": False})
    return pd.DataFrame(rows)


def self_test():
    ok = True

    def check(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    labels = ["L1", "L1P", "L2", "L3", "L4", "L5", "L6"]
    # 1. offset: bare labels written for children one year older, gloss exact, L6 six years older
    rng = np.random.default_rng(1)
    cubes, l0 = simulate_cubes({"L1": 1.0, "L1P": 1.0, "L2": 0.5, "L6": 6.0}, rng, labels=labels, l0_age=10.5)
    r = analyze(cubes_to_df(cubes, l0, rng))
    p = r["primary"]
    check(p["h2_level_H"]["rejected_holm"] and p["h2_level_H"]["estimate"] < 0, f"offset: H level found, {p['h2_level_H']['estimate']:.4f}, p = {p['h2_level_H']['p_two_sided']:.2g}")
    check(p["h2_level_P"]["rejected_holm"] and p["h2_level_P"]["estimate"] < 0, f"offset: P level found, {p['h2_level_P']['estimate']:.4f}")
    ae = r["age_equivalent"]["by_label"]
    check(0.6 < ae["L1"]["shift_years"] < 1.4, f"offset: L1 shift {ae['L1']['shift_years']:.2f} years (planted 1), CI {np.round(ae['L1']['shift_ci95'], 2)}, isotonic {ae['L1']['isotonic_shift_years']:.2f}")
    check(ae["L1"]["shift_ci95"][0] < ae["L1"]["shift_years"] < ae["L1"]["shift_ci95"][1], "offset: bootstrap interval contains the estimate")
    check(0.7 < ae["L1"]["tracking"] < 1.3, f"offset: L1 tracking {ae['L1']['tracking']:.2f} (planted 1)")
    check(abs(ae["L3"]["shift_years"]) < 0.5, f"offset: L3 shift {ae['L3']['shift_years']:.2f} years (planted 0)")
    check(r["gloss"]["gloss_level_vs_bare"]["estimate"] > 0 and r["gloss"]["gloss_level_vs_bare"]["p_two_sided"] < 0.05, "offset: the gloss moves the level back toward the age")
    check(4.5 < ae["L6"]["shift_years"] < 7.5, f"offset: L6 shift {ae['L6']['shift_years']:.2f} years over 3H to 5H (planted 6)")
    check(r["controls"]["l6_vs_l5_level_3h_to_5h"]["estimate"] < -0.15, f"offset: L6 collision control found, {r['controls']['l6_vs_l5_level_3h_to_5h']['estimate']:.3f}")
    check(r["h1_models_supported"] >= 5, f"offset: H1 ruler found in {r['h1_models_supported']} of 6 models")
    l0_mean = float(np.mean(list(r["age_equivalent"]["l0_default_age"].values())))
    check(abs(l0_mean - 10.5) < 1.0, f"offset: L0 placed at {l0_mean:.2f} years (planted default age 10.5)")
    so = r["secondary_ols_clustered"]
    check(all(abs(so[k]["estimate"] - p[k]["estimate"]) < 1e-6 for k in p), "clustered OLS gives the same point estimates as the topic-level statistics (balanced data)")
    same = primary_from_cubes(cubes)
    check(all(abs(same[k]["p_two_sided"] - p[k]["p_two_sided"]) < 1e-12 for k in same), "cube path and data-frame path agree")
    # 2. the label is ignored: the model writes at age 9 whatever the grade
    rng = np.random.default_rng(2)
    r2 = analyze(cubes_to_df(simulate_cubes({"L1": [9.0] * 6, "L1P": [9.0] * 6}, rng, labels=labels), None, rng))
    p2 = r2["primary"]
    check(p2["h3_gradient_H"]["rejected_holm"] and p2["h3_gradient_H"]["estimate"] > 0, f"ignored: H gradient found, {p2['h3_gradient_H']['estimate']:.4f} Zipf per year")
    check(p2["h3_gradient_P"]["rejected_holm"], "ignored: P gradient found")
    check(abs(p2["h2_level_H"]["estimate"]) < 0.03, f"ignored: the level alone would miss it ({p2['h2_level_H']['estimate']:.4f})")
    check(abs(r2["age_equivalent"]["by_label"]["L1"]["tracking"]) < 0.35, f"ignored: L1 tracking {r2['age_equivalent']['by_label']['L1']['tracking']:.2f} (planted 0)")
    # 3. H digit read as an age (written for children 3.5 years younger), P label understood
    rng = np.random.default_rng(3)
    r3 = analyze(cubes_to_df(simulate_cubes({"L1": -3.5}, rng, labels=labels), None, rng))
    check(r3["primary"]["h2_level_H"]["rejected_holm"] and r3["primary"]["h2_level_H"]["estimate"] > 0, "digit as age: positive level found")
    check(not r3["primary"]["h2_level_P"]["rejected_holm"] and abs(r3["primary"]["h2_level_P"]["estimate"]) < 0.04, "digit as age: the P test does not borrow the H effect")
    check(-4.2 < r3["age_equivalent"]["by_label"]["L1"]["shift_years"] < -2.8, f"digit as age: L1 shift {r3['age_equivalent']['by_label']['L1']['shift_years']:.2f} years (planted -3.5)")
    check(0.7 < r3["age_equivalent"]["by_label"]["L1"]["tracking"] < 1.3, f"digit as age: L1 tracking {r3['age_equivalent']['by_label']['L1']['tracking']:.2f} (planted 1)")
    # 4. null
    rng = np.random.default_rng(4)
    r4 = analyze(cubes_to_df(simulate_cubes({}, rng, labels=labels), None, rng))
    check(not any(v["rejected_holm"] for v in r4["primary"].values()), "null: no primary test rejected (seed 4)")
    # 5. exclusions: 5 % of texts excluded at random, and one topic with most L1 texts excluded
    rng = np.random.default_rng(5)
    c5 = simulate_cubes({"L1": 1.5, "L1P": 1.5}, rng, labels=labels, missing=0.05)
    c5["L1"][2:, :, :, 0] = np.nan  # topic t00: only two models' L1 texts are kept (24 of 72 pairs at most)
    r5 = analyze(cubes_to_df(c5, None, rng))
    e5 = r5["primary"]["h2_level_H"]
    check(e5["rejected_holm"] and r5["n_kept"] < r5["n_texts"], f"exclusions handled, {r5['n_texts'] - r5['n_kept']} texts excluded")
    check(abs(e5["estimate"] + 0.06) < 0.04, f"excluded texts are not used ({e5['estimate']:.4f}, planted -0.06)")
    check(e5["topics_dropped"] == 1 and e5["n_topics"] == 15, f"a topic with most pairs missing is dropped ({e5['topics_dropped']} dropped)")
    # 6. flat ruler: no age equivalent without a ruler
    rng = np.random.default_rng(6)
    r6 = analyze(cubes_to_df(simulate_cubes({"L1": 1.0}, rng, labels=labels, slope=0.0, slope_sd=0.0, sigma=0.1), None, rng))
    check(len(r6["age_equivalent"]["eligible_models"]) == 0, f"flat rulers excluded from the age equivalent ({len(r6['age_equivalent']['eligible_models'])} eligible)")
    rule = all(v["eligible_for_age_equivalent"] == (v["slope"] <= MIN_SLOPE) for v in r["h1"].values())
    check(rule, "eligibility follows the rule (L5 slope at most -0.02)")
    # 7. probe parser: exact parses and decisions
    cases = [("Les élèves de 5H ont entre 8 et 9 ans.", [(8, 9)], True), ("Ils ont huit à neuf ans.", [(8, 9)], True),
             ("En France, la 5e correspond à 12-13 ans, en Suisse à 8-9 ans.", [(12, 13), (8, 9)], False),
             ("Ils ont environ 8 ans.", [(8, 8)], True), ("La 5e année, 10 ou 11 ans.", [(10, 11)], False),
             ("Je ne sais pas.", [], False)]
    for text, parsed, expected in cases:
        found = parse_probe(text)
        check(found == parsed and bool(found and probe_correct(*found[0], 8, 9)) == expected, f"probe parser on {text!r}: {found}")
    # 8. unit checks of the arithmetic
    adj, rej = holm({"a": 0.01, "b": 0.04, "c": 0.03})
    check(np.allclose([adj["a"], adj["c"], adj["b"]], [0.03, 0.06, 0.06]) and rej == {"a": True, "c": False, "b": False},
          f"Holm adjusted p and decisions {adj} {rej}")
    tt = ttest(np.array([1.0, 2.0, 3.0, 4.0]))
    check(abs(tt["t"] - 3.872983) < 1e-5 and abs(tt["p_two_sided"] - 0.030466) < 1e-5 and tt["df"] == 3,
          f"t-test arithmetic t = {tt['t']:.6f}, p = {tt['p_two_sided']:.6f}")
    check(np.allclose(weights("gradient", list(range(6))) @ AGES, 1.0) and np.isclose(weights("gradient", list(range(6))).sum(), 0.0),
          "gradient weights give a slope of 1 for the ages and 0 for a constant")
    print("OK" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(0 if self_test() else 1)
    measures = pd.read_csv(sys.argv[1], keep_default_na=False, na_values=["", "nan", "NaN"])
    probes = None
    if len(sys.argv) > 2 and sys.argv[2] != "-":
        probes = pd.read_csv(sys.argv[2], keep_default_na=False, na_values=["", "nan", "NaN"])
    out = analyze(measures, probes)
    path = sys.argv[3] if len(sys.argv) > 3 else "results/numbers.json"
    json.dump(out, open(path, "w"), indent=1, default=float)
    print(json.dumps(out["primary"], indent=1))
