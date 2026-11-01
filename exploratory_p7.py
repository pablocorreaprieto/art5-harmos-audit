"""Post hoc analyses added after the internal readings of the manuscript (phase P7, 1.11.2026).

None of these analyses was preregistered. Each answers a question raised by a separate AI reading
of the draft (R1 to R3, records in manuscript/records/), uses only data already collected, and is
labelled post hoc wherever the manuscript reports it. No test is added to the confirmatory family.

1. spread: how far the six models' age-only texts (L5) lie from one another at the same grade, in
   Zipf, compared with each model's own change from 3H to 8H; and the between-model standard
   deviation of each label's mean level, with a topic bootstrap of its difference between L3 and L1.
2. equivalence: two one-sided tests (TOST) of the two primary level contrasts against plus or minus
   the smallest effect of interest (0.04 Zipf), at the topic level, with 90% intervals.
3. heterogeneity: whether the six models differ in the level and gradient of L1 - L5 and L1P - L5
   (repeated-measures ANOVA over topics, model as within-topic factor).
4. reasoning: reasoning or thinking tokens per text, by model and label, from the providers' usage
   fields kept in the raw records.
5. probes: wrong first answers that state a correct range later in the same answer, and correct
   answers accepted only through the half-year tolerance of the preregistered rule.
6. offsets: observed age offsets per grade, (label cell mean - age-only cell mean) / ruler slope, for
   each model and for L1, L1P and L3, with 95% percentile intervals from topic resamples (the
   discussion of the draft gave offsets read from fitted lines).
7. mistral_reasoning: the age that Mistral Large 4, the only audited model whose reasoning is
   returned as text, states for the pupils in its reasoning (first age range with a plausible
   midpoint, French patterns of the probe parser plus their English equivalents), by label; and, for
   L1 and L1P, the paired difference (label text - age-only text of the same model, grade, genre and
   topic) for texts whose reasoning stated a correct age and for texts whose reasoning stated an age
   two years too old, compared with grade and genre effects and errors clustered by topic, and the
   slope of the paired difference on the stated error. A random sample of 25 traces with the
   extracted age is written out for reading by hand. A first version that took the first age range
   of any size, without the English patterns, picked up a few non-pupil ages (up to 70 years off);
   the plausibility window and the English patterns were added after reading that sample. A second
   version compared the two groups without grade and genre effects (difference -0.016, SE 0.017); a
   separate reading (refutation of R1) found the relation with grade and genre effects, and since the
   stated errors are concentrated at some grades (6H for H; 3H and 6H for P), the comparison now holds
   grade and genre constant; the unadjusted difference is kept in the output.

Reads results/measures.csv, results/probes.csv, results/numbers.json and the raw files of the main
run; writes results/exploratory_p7.json. Seeded; rerunning gives the same file.
Written by the main session (claude-opus-5-5) on 1.11.2026, after the deposit and the data freeze.
"""
import glob
import json
import random
import re
import sys

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
from statsmodels.stats.anova import AnovaRM

import analyze

SESOI = 0.04
BOOT = 2000
SEED = 20261101
TRUTH = {"3H": (6, 7), "4H": (7, 8), "5H": (8, 9), "6H": (9, 10), "7H": (10, 11), "8H": (11, 12)}
MODELS = ["anthropic_balanced", "anthropic_light", "openai_balanced", "openai_light", "mistral_balanced", "mistral_light"]


def load():
    df = pd.read_csv("results/measures.csv", keep_default_na=False)
    df["kept"] = analyze.as_bool(df["kept"])
    df[analyze.Y] = pd.to_numeric(df[analyze.Y], errors="coerce")
    return df[df["kept"]].copy()


def raw_records():
    recs = {}
    for f in sorted(glob.glob("data/raw/calls_2026110*.jsonl")):
        for line in open(f):
            r = json.loads(line)
            if str(r.get("ok")).lower() == "true":
                recs[r["call_id"]] = r  # a retried call keeps the answer of its last successful attempt
    return recs


def cell_table(df, labels):
    """Mean of Y per (label, model, grade, topic), averaged over the two genres."""
    d = df[df["label"].isin(labels)]
    return d.groupby(["label", "model", "grade", "topic"])[analyze.Y].mean()


def spread(df):
    l5 = df[df["label"] == "L5"]
    cm = l5.groupby(["model", "grade"])[analyze.Y].mean().unstack("grade")[analyze.GRADES]
    slopes = {m: float(np.polyfit(analyze.AGES, cm.loc[m].to_numpy(), 1)[0]) for m in cm.index}
    rng_by_grade = (cm.max() - cm.min()).to_dict()
    sd_by_grade = cm.std(ddof=1).to_dict()
    within = {m: abs(b) * (analyze.AGES[-1] - analyze.AGES[0]) for m, b in slopes.items()}
    # between-model SD of each label's mean level (absolute Zipf), and bootstrap of SD(L3) - SD(L1)
    cells = cell_table(df, ["L1", "L1P", "L3", "L5"]).unstack("topic")
    topics = list(cells.columns)
    def sd_levels(w):
        lev = (cells.to_numpy() @ w) / w.sum()
        s = pd.Series(lev, index=cells.index).groupby(level=["label", "model"]).mean()
        return {lab: float(s[lab].std(ddof=1)) for lab in ["L1", "L1P", "L3", "L5"]}
    point = sd_levels(np.ones(len(topics)))
    rng = np.random.default_rng(SEED)
    diffs = []
    for _ in range(BOOT):
        w = np.bincount(rng.integers(0, len(topics), len(topics)), minlength=len(topics)).astype(float)
        s = sd_levels(w)
        diffs.append(s["L3"] - s["L1"])
    return {"l5_cell_means": {m: cm.loc[m].round(6).to_dict() for m in cm.index},
            "l5_slope_by_model": slopes,
            "between_model_range_by_grade": rng_by_grade,
            "between_model_sd_by_grade": sd_by_grade,
            "between_model_range_min": float(min(rng_by_grade.values())),
            "between_model_range_max": float(max(rng_by_grade.values())),
            "within_model_change_3H_to_8H": within,
            "within_model_change_min": float(min(within.values())),
            "within_model_change_max": float(max(within.values())),
            "between_model_sd_of_level": point,
            "sd_L3_minus_L1": point["L3"] - point["L1"],
            "sd_L3_minus_L1_ci95": [float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))],
            "bootstrap": {"resamples": BOOT, "seed": SEED, "unit": "topic"}}


def equivalence(df):
    ax = analyze.axes(df[df["label"].isin(analyze.GRADED_LABELS)])
    cubes = analyze.to_cubes(df, analyze.Y, ax)
    out = {}
    for name, a, b in (("h2_level_H", "L1", "L5"), ("h2_level_P", "L1P", "L5")):
        x, _ = analyze.topic_stat(cubes[a], cubes[b], "level")
        T = len(x)
        mean, se = float(np.mean(x)), float(np.std(x, ddof=1) / np.sqrt(T))
        p_lower = float(stats.t.sf((mean + SESOI) / se, T - 1))   # H0: diff <= -SESOI
        p_upper = float(stats.t.cdf((mean - SESOI) / se, T - 1))  # H0: diff >= +SESOI
        q = stats.t.ppf(0.95, T - 1)
        out[name] = {"estimate": mean, "se": se, "df": T - 1, "bounds": [-SESOI, SESOI],
                     "p_tost": max(p_lower, p_upper), "ci90": [mean - q * se, mean + q * se]}
    return out


def heterogeneity(df):
    ax = analyze.axes(df[df["label"].isin(analyze.GRADED_LABELS)])
    cubes = analyze.to_cubes(df, analyze.Y, ax)
    out = {}
    for lab in ("L1", "L1P"):
        for kind in ("level", "gradient"):
            rows = []
            for i, m in enumerate(ax["models"]):
                x, dropped = analyze.topic_stat(cubes[lab], cubes["L5"], kind, models=[i])
                assert dropped == 0
                rows += [{"topic": t, "model": m, "y": float(v)} for t, v in zip(ax["topics"], x)]
            res = AnovaRM(pd.DataFrame(rows), "y", "topic", within=["model"]).fit()
            t = res.anova_table.loc["model"]
            out[f"{lab}_{kind}"] = {"F": float(t["F Value"]), "df1": float(t["Num DF"]), "df2": float(t["Den DF"]),
                                    "p": float(t["Pr > F"])}
    return out


def reasoning_tokens(df, recs):
    rows = []
    for r in df.itertuples():
        u = recs[r.call_id]["response"].get("usage", {})
        if "output_tokens_details" in u:
            n = (u.get("output_tokens_details") or {}).get("thinking_tokens", 0)
        else:
            n = (u.get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
        rows.append({"model": r.model, "label": r.label, "n": n or 0})
    d = pd.DataFrame(rows)
    g = d.groupby(["model", "label"])["n"]
    return {"mean": {f"{m} | {lab}": float(v) for (m, lab), v in g.mean().items()},
            "share_positive": {f"{m} | {lab}": float(v) for (m, lab), v in g.apply(lambda s: (s > 0).mean()).items()}}


def probes_parse(p):
    wrong = wrong_with_correct_later = 0
    tolerance_only = {}
    correct = 0
    for r in p.itertuples():
        if str(r.ok).lower() not in ("true", "1"):
            continue
        found = analyze.parse_probe(r.text)
        if not found:
            continue
        lo, hi = found[0]
        mid = (lo + hi) / 2
        if analyze.probe_correct(lo, hi, r.truth_age_from, r.truth_age_to):
            correct += 1
            if not (r.truth_age_from <= mid <= r.truth_age_to):
                tolerance_only[r.model] = tolerance_only.get(r.model, 0) + 1
        else:
            wrong += 1
            wrong_with_correct_later += any(analyze.probe_correct(a, b, r.truth_age_from, r.truth_age_to) for a, b in found[1:])
    return {"n_correct_first": correct, "n_wrong_first": wrong,
            "n_wrong_first_with_a_correct_range_later": wrong_with_correct_later,
            "n_correct_only_through_tolerance": int(sum(tolerance_only.values())),
            "correct_only_through_tolerance_by_model": tolerance_only}


def offsets(df):
    cells = cell_table(df, ["L1", "L1P", "L3", "L5"]).unstack("topic")
    topics = list(cells.columns)
    def compute(w):
        mean = pd.Series((cells.to_numpy() @ w) / w.sum(), index=cells.index)
        out = {}
        for m in MODELS:
            ruler = np.array([mean[("L5", m, g)] for g in analyze.GRADES])
            b = np.polyfit(analyze.AGES, ruler, 1)[0]
            for lab in ("L1", "L1P", "L3"):
                for gi, g in enumerate(analyze.GRADES):
                    out[(m, lab, g)] = (mean[(lab, m, g)] - ruler[gi]) / b
        return out
    point = compute(np.ones(len(topics)))
    rng = np.random.default_rng(SEED)
    boots = {k: [] for k in point}
    for _ in range(BOOT):
        w = np.bincount(rng.integers(0, len(topics), len(topics)), minlength=len(topics)).astype(float)
        for k, v in compute(w).items():
            boots[k].append(v)
    return {f"{m} | {lab} | {g}": {"offset_years": float(v),
                                   "ci95": [float(np.percentile(boots[(m, lab, g)], 2.5)),
                                            float(np.percentile(boots[(m, lab, g)], 97.5))]}
            for (m, lab, g), v in point.items()}


def reasoning_text(rec):
    msg = rec["response"]["choices"][0]["message"]
    parts = []
    content = msg.get("content")
    if isinstance(content, list):
        for x in content:
            if x.get("type") == "thinking":
                for y in x.get("thinking") or []:
                    if isinstance(y, dict) and y.get("type") == "text":
                        parts.append(y.get("text", ""))
    return "\n".join(parts)


EN_AGE_RE = re.compile(r"(\d{1,2})\s*(?:(?:-|–|—|to|or|and)\s*(\d{1,2})\s*)?[- ]?years?[- ]?olds?\b")
PLAUSIBLE = (4, 16)  # midpoint of a stated range that can be a pupil's age


def stated_age(text):
    """First age range stated in a reasoning trace whose midpoint is a plausible pupil age: the French
    patterns of analyze.parse_probe and their English equivalents ("9-10 year olds"), in text order."""
    t = (text or "").replace("\xa0", " ").lower()
    for w, n in analyze.NUMBER_WORDS.items():
        t = re.sub(rf"\b{w}\b", str(n), t)
    found = [(m.start(), int(m.group(1)), int(m.group(2) or m.group(1))) for m in analyze.AGE_RE.finditer(t)]
    found += [(m.start(), int(m.group(1)), int(m.group(2) or m.group(1))) for m in EN_AGE_RE.finditer(t)]
    for _, lo, hi in sorted(found):
        if PLAUSIBLE[0] <= (lo + hi) / 2 <= PLAUSIBLE[1]:
            return lo, hi
    return None


def mistral_reasoning(df, recs):
    m = "mistral_balanced"
    d = df[(df["model"] == m) & df["label"].isin(["L1", "L1P", "L2", "L3", "L4", "L5"])].copy()
    stated = []
    for r in d.itertuples():
        found = stated_age(reasoning_text(recs[r.call_id]))
        if found:
            lo, hi = found
            t0, t1 = TRUTH[r.grade]
            err = (lo + hi) / 2 - (t0 + t1) / 2
            stated.append({"call_id": r.call_id, "has_age": True, "error": err,
                           "wrong": not analyze.probe_correct(lo, hi, t0, t1), "two_years_old": 1.5 <= err <= 2.5})
        else:
            stated.append({"call_id": r.call_id, "has_age": False, "error": np.nan, "wrong": np.nan, "two_years_old": np.nan})
    d = d.merge(pd.DataFrame(stated), on="call_id")
    by_label = {}
    for lab, g in d.groupby("label"):
        h = g[g["has_age"]]
        by_label[lab] = {"n": int(len(g)), "share_stating_an_age": float(g["has_age"].mean()),
                         "share_wrong_among_stated": float(h["wrong"].astype(float).mean()) if len(h) else None,
                         "mean_signed_error_years": float(h["error"].mean()) if len(h) else None,
                         "share_two_years_too_old_among_stated": float(h["two_years_old"].astype(float).mean()) if len(h) else None}
    l5 = d[d["label"] == "L5"].set_index(["grade", "genre", "topic"])[analyze.Y]
    paired = {}
    for lab in ("L1", "L1P"):
        g = d[(d["label"] == lab) & d["has_age"]].copy()
        g["diff"] = [row[analyze.Y] - l5[(row["grade"], row["genre"], row["topic"])] for _, row in g.iterrows()]
        g["correct"] = ~g["wrong"].astype(bool)
        sub = g[g["correct"] | g["two_years_old"].astype(bool)].copy()
        sub["old2"] = sub["two_years_old"].astype(bool).astype(float)
        groups = pd.factorize(sub["topic"])[0]
        # grade and genre held constant: the stated errors are concentrated at some grades, and the paired
        # differences vary with grade
        fit = smf.ols("diff ~ old2 + C(grade) + C(genre)", data=sub).fit(
            cov_type="cluster", cov_kwds={"groups": groups, "use_correction": True})
        raw_fit = smf.ols("diff ~ old2", data=sub).fit(cov_type="cluster", cov_kwds={"groups": groups, "use_correction": True})
        gl = pd.factorize(g["topic"])[0]
        lin = smf.ols("diff ~ error + C(grade) + C(genre)", data=g).fit(cov_type="cluster", cov_kwds={"groups": gl, "use_correction": True})
        exp2 = 2 * json.load(open("results/numbers.json"))["h1"][m]["slope"]
        paired[lab] = {"n_correct": int(sub["correct"].sum()), "n_two_years_old": int(sub["old2"].sum()),
                       "two_years_old_by_grade": {gr: int(v) for gr, v in sub.groupby("grade")["old2"].sum().items()},
                       "difference": float(fit.params["old2"]), "se": float(fit.bse["old2"]), "p": float(fit.pvalues["old2"]),
                       "difference_without_grade_and_genre": float(raw_fit.params["old2"]),
                       "se_without_grade_and_genre": float(raw_fit.bse["old2"]),
                       "slope_per_year_of_stated_error": float(lin.params["error"]), "slope_se": float(lin.bse["error"]),
                       "slope_p": float(lin.pvalues["error"]),
                       "expected_on_own_ruler_for_two_years": exp2, "share_of_expected": float(fit.params["old2"] / exp2)}
    rng = random.Random(SEED)
    sample = rng.sample([r for r in d.itertuples() if r.label in ("L1", "L1P")], 25)
    lines = []
    for r in sample:
        t = reasoning_text(recs[r.call_id]).replace("\n", " ")
        lines.append(f"{r.call_id} | {r.label} | {r.grade} | stated {stated_age(t)} | {t[:260]}")
    with open("results/exploratory_p7_mistral_sample.txt", "w") as f:
        f.write("Random sample of 25 reasoning traces of Mistral Large 4 (L1 and L1P), seed 20261101, with the stated "
                "age extracted by exploratory_p7.stated_age, for reading by hand. First 260 characters of each trace.\n\n")
        f.write("\n".join(lines) + "\n")
    return {"model": m, "by_label": by_label, "paired_difference_by_stated_age": paired,
            "rule": "first age range in the visible reasoning (French or English patterns) whose midpoint lies between "
                    f"{PLAUSIBLE[0]} and {PLAUSIBLE[1]} years; wrong if its midpoint is outside the true range widened by "
                    "half a year (the preregistered probe rule); two years too old if the midpoint is 1.5 to 2.5 years "
                    "above the true midpoint",
            "validation_sample": "results/exploratory_p7_mistral_sample.txt",
            "plausible_window_years": list(PLAUSIBLE), "two_years_window": [1.5, 2.5], "validation_sample_n": len(sample)}


def leave_one_model_out(df):
    """The four primary tests without each model in turn (topic-level t-tests, as analyze.py)."""
    ax = analyze.axes(df[df["label"].isin(analyze.GRADED_LABELS)])
    cubes = analyze.to_cubes(df, analyze.Y, ax)
    out = {}
    for i, m in enumerate(ax["models"]):
        keep = [j for j in range(len(ax["models"])) if j != i]
        out[m] = {name: analyze.ttest(analyze.topic_stat(cubes[a], cubes[b], kind, models=keep)[0])
                  for name, a, b, kind in analyze.PRIMARY}
    return out


def cell_arrays(df, labels):
    """sums and counts (labels, models, grades, topics) of Y, as in analyze.age_equivalent_block."""
    ax = analyze.axes(df[df["label"].isin(analyze.GRADED_LABELS)])
    M, G, T = len(ax["models"]), len(analyze.GRADES), len(ax["topics"])
    sums, counts = np.zeros((len(labels), M, G, T)), np.zeros((len(labels), M, G, T))
    mi = {m: i for i, m in enumerate(ax["models"])}
    ti = {t: i for i, t in enumerate(ax["topics"])}
    for r in df[df["label"].isin(labels)].itertuples():
        k = (labels.index(r.label), mi[r.model], analyze.GRADES.index(r.grade), ti[r.topic])
        sums[k] += getattr(r, analyze.Y)
        counts[k] += 1
    return sums, counts, ax


def readings(means, li, i5):
    """Per-model level, gradient and slope of label li against L5, from cell means (labels, models, grades[, B])."""
    ages = analyze.AGES
    c = (ages - ages.mean()) / np.sum((ages - ages.mean()) ** 2)
    d = means[li] - means[i5]                                    # (models, grades, ...)
    level = d.mean(axis=1)
    grad = np.tensordot(c, d, axes=([0], [1]))
    slope = np.tensordot(c, means[i5], axes=([0], [1]))
    return level, grad, slope


def label_contrasts(df):
    """Adding words to the bare H label: L2 - L1 and L3 - L1, at the topic level in Zipf and as pooled
    shift and tracking differences in years with the topic bootstrap of analyze.py; and the dispersion
    (SD across the six models) of the per-model shifts and tracking of each label."""
    ax = analyze.axes(df[df["label"].isin(analyze.GRADED_LABELS)])
    cubes = analyze.to_cubes(df, analyze.Y, ax)
    labels = ["L1", "L1P", "L2", "L3", "L4", "L5"]
    sums, counts, _ = cell_arrays(df, labels)
    T = sums.shape[-1]
    i5 = labels.index("L5")
    def pooled(means, lab):
        lev, grd, b = readings(means, labels.index(lab), i5)
        return lev.sum(0) / b.sum(0), 1 + grd.sum(0) / b.sum(0), lev / b, 1 + grd / b
    rng = np.random.default_rng(SEED)
    W = np.stack([np.bincount(rng.integers(0, T, T), minlength=T) for _ in range(BOOT)]).T.astype(float)  # (T, B)
    means_b = (sums @ W) / (counts @ W)
    means_0 = sums.sum(-1) / counts.sum(-1)
    out = {}
    for lab in ("L2", "L3"):
        lev_t = {kind: analyze.ttest(analyze.topic_stat(cubes[lab], cubes["L1"], kind)[0]) for kind in ("level", "gradient")}
        s0, t0, _, _ = pooled(means_0, lab)
        s1, t1, _, _ = pooled(means_0, "L1")
        sb, tb, _, _ = pooled(means_b, lab)
        s1b, t1b, _, _ = pooled(means_b, "L1")
        out[f"{lab}_minus_L1"] = {"level": lev_t["level"], "gradient": lev_t["gradient"],
                                  "shift_diff_years": float(s0 - s1),
                                  "shift_diff_ci95": [float(np.percentile(sb - s1b, 2.5)), float(np.percentile(sb - s1b, 97.5))],
                                  "tracking_diff": float(t0 - t1),
                                  "tracking_diff_ci95": [float(np.percentile(tb - t1b, 2.5)), float(np.percentile(tb - t1b, 97.5))]}
        by_model = {}
        for i, m in enumerate(ax["models"]):
            by_model[m] = analyze.ttest(analyze.topic_stat(cubes[lab], cubes["L1"], "level", models=[i])[0])["estimate"]
        out[f"{lab}_minus_L1"]["level_by_model"] = by_model
    disp = {}
    for lab in ("L1", "L1P", "L2", "L3", "L4"):
        _, _, sh0, tr0 = pooled(means_0, lab)
        _, _, shb, trb = pooled(means_b, lab)
        disp[lab] = {"sd_shift": float(np.std(sh0, ddof=1)), "sd_tracking": float(np.std(tr0, ddof=1)),
                     "sd_shift_boot": shb.std(axis=0, ddof=1), "sd_tracking_boot": trb.std(axis=0, ddof=1)}
    for lab in ("L1P", "L2", "L3", "L4"):
        for k in ("shift", "tracking"):
            dd = disp["L1"][f"sd_{k}_boot"] - disp[lab][f"sd_{k}_boot"]
            disp[lab][f"sd_{k}_L1_minus_this_ci95"] = [float(np.percentile(dd, 2.5)), float(np.percentile(dd, 97.5))]
    for lab in disp:
        disp[lab].pop("sd_shift_boot"), disp[lab].pop("sd_tracking_boot")
    out["dispersion_across_models"] = disp
    # mean of the six per-model readings (unweighted), the pooling used by analyze.py for the isotonic reading
    unweighted = {}
    for lab in ("L1", "L1P"):
        _, _, sh0, tr0 = pooled(means_0, lab)
        unweighted[lab] = {"mean_shift": float(sh0.mean()), "mean_tracking": float(tr0.mean())}
    out["linear_reading_unweighted_mean"] = unweighted
    return out


def tracking_precision(df, B=100_000, seed=SEED):
    """Percentile interval of the pooled L1P tracking with many more resamples than the registered 2,000,
    to show how far the registered upper limit depends on the resampling."""
    labels = ["L1P", "L5"]
    sums, counts, _ = cell_arrays(df, labels)
    T = sums.shape[-1]
    rng = np.random.default_rng(seed)
    out = {}
    for lab_i, lab in enumerate(["L1P"]):
        vals = []
        for start in range(0, B, 10_000):
            W = np.stack([np.bincount(rng.integers(0, T, T), minlength=T) for _ in range(min(10_000, B - start))]).T.astype(float)
            means = (sums @ W) / (counts @ W)
            lev, grd, b = readings(means, 0, 1)
            vals.append(1 + grd.sum(0) / b.sum(0))
        v = np.concatenate(vals)
        out[lab] = {"resamples": B, "seed": seed, "ci95": [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))],
                    "share_at_least_1": float(np.mean(v >= 1))}
    return out


def l0_intervals(df, nums):
    """Topic-bootstrap intervals of each model's default reader age (L0 placed on its linear L5 ruler, as
    analyze.linear_reading does: 9 + (L0 mean - ruler mean) / slope)."""
    ax = analyze.axes(df[df["label"].isin(analyze.GRADED_LABELS)])
    sums, counts, _ = cell_arrays(df, ["L5"])
    T = sums.shape[-1]
    l0 = df[df["label"] == "L0"]
    ti = {t: i for i, t in enumerate(ax["topics"])}
    out = {}
    rng = np.random.default_rng(SEED)
    W = np.stack([np.bincount(rng.integers(0, T, T), minlength=T) for _ in range(BOOT)]).T.astype(float)
    for i, m in enumerate(ax["models"]):
        g = l0[l0["model"] == m]
        s, c = np.zeros(T), np.zeros(T)
        for r in g.itertuples():
            s[ti[r.topic]] += getattr(r, analyze.Y)
            c[ti[r.topic]] += 1
        def age(w):
            ruler = (sums[0, i] @ w) / (counts[0, i] @ w)            # (grades, B) or (grades,)
            ages = analyze.AGES
            cc = (ages - ages.mean()) / np.sum((ages - ages.mean()) ** 2)
            b = np.tensordot(cc, ruler, axes=([0], [0]))
            return 9.0 + ((s @ w) / (c @ w) - ruler.mean(axis=0)) / b
        point = float(age(np.ones(T)))
        assert abs(point - nums["age_equivalent"]["l0_default_age"][m]) < 1e-9, m
        bs = age(W)
        out[m] = {"age": point, "ci95": [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]}
    return out


def by_tier(nums):
    """Descriptive summary by provider and price tier (preregistered as exploratory: 'provider and model
    size'); one model per cell, so no test."""
    bl = nums["age_equivalent"]["by_label"]
    tiers = {"balanced": [m for m in MODELS if m.endswith("balanced")], "light": [m for m in MODELS if m.endswith("light")]}
    out = {}
    for lab in ("L1", "L1P"):
        for tier, ms in tiers.items():
            out[f"{lab} | {tier}"] = {"mean_abs_shift": float(np.mean([abs(bl[lab]["by_model"][m]["shift_years"]) for m in ms])),
                                      "mean_abs_tracking_minus_1": float(np.mean([abs(bl[lab]["by_model"][m]["tracking"] - 1) for m in ms]))}
    return out


SWISS_WORDS = {"romand": r"\bromand(?:e|s|es)?\b", "canton": r"\bcantons?\b"}


def swiss_words(df, recs):
    """Lexicon-free count of two Swiss words in the measured bodies (title removed by compute.clean), by label:
    occurrences, and texts containing them."""
    import compute
    out = {}
    for lab in ("L1", "L2", "L3", "L5"):
        d = df[df["label"] == lab]
        counts = {w: 0 for w in SWISS_WORDS}
        texts = {w: 0 for w in SWISS_WORDS}
        for r in d.itertuples():
            _, lines = compute.clean(recs[r.call_id]["text"])
            body = "\n".join(lines).lower()
            for w, rx in SWISS_WORDS.items():
                k = len(re.findall(rx, body))
                counts[w] += k
                texts[w] += k > 0
        out[lab] = {"n_texts": int(len(d)), "occurrences": counts, "texts_containing": texts}
    return out


def main():
    df = load()
    recs = raw_records()
    p = pd.read_csv("results/probes.csv", keep_default_na=False)
    nums = json.load(open("results/numbers.json"))
    out = {"note": "post hoc analyses after the internal readings of the draft (P7); not preregistered",
           "spread": spread(df), "equivalence": equivalence(df), "heterogeneity": heterogeneity(df),
           "reasoning_tokens": reasoning_tokens(df, recs), "probes_parse": probes_parse(p),
           "offsets": offsets(df), "mistral_reasoning": mistral_reasoning(df, recs),
           "leave_one_model_out": leave_one_model_out(df), "label_contrasts": label_contrasts(df),
           "tracking_precision": tracking_precision(df), "l0_intervals": l0_intervals(df, nums),
           "by_tier": by_tier(nums), "swiss_words": swiss_words(df, recs)}
    # the vectorised readings used by label_contrasts must reproduce analyze.py's pooled point values
    labels = ["L1", "L1P", "L2", "L3", "L4", "L5"]
    sums, counts, _ = cell_arrays(df, labels)
    means_0 = sums.sum(-1) / counts.sum(-1)
    for lab in ("L1", "L1P", "L2", "L3", "L4"):
        lev, grd, b = readings(means_0, labels.index(lab), labels.index("L5"))
        v = nums["age_equivalent"]["by_label"][lab]
        assert abs(lev.sum() / b.sum() - v["shift_years"]) < 1e-9, lab
        assert abs(1 + grd.sum() / b.sum() - v["tracking"]) < 1e-9, lab
    # L3 - L1 at the topic level is the preregistered secondary contrast of analyze.py (gloss_level_vs_bare)
    assert abs(out["label_contrasts"]["L3_minus_L1"]["level"]["estimate"] - nums["gloss"]["gloss_level_vs_bare"]["estimate"]) < 1e-12
    # with all six models, the leave-one-out function must give the frozen primary estimates
    ax = analyze.axes(df[df["label"].isin(analyze.GRADED_LABELS)])
    cubes = analyze.to_cubes(df, analyze.Y, ax)
    for name, a, b, kind in analyze.PRIMARY:
        est = analyze.ttest(analyze.topic_stat(cubes[a], cubes[b], kind, models=list(range(len(ax["models"]))))[0])["estimate"]
        assert abs(est - nums["primary"][name]["estimate"]) < 1e-12, name
    # consistency checks against the frozen confirmatory results (stop if any fails)
    for name in ("h2_level_H", "h2_level_P"):
        assert abs(out["equivalence"][name]["estimate"] - nums["primary"][name]["estimate"]) < 1e-12, name
    bl = nums["age_equivalent"]["by_label"]
    for m in MODELS:
        for lab in ("L1", "L1P", "L3"):
            mean_offset = np.mean([out["offsets"][f"{m} | {lab} | {g}"]["offset_years"] for g in analyze.GRADES])
            assert abs(mean_offset - bl[lab]["by_model"][m]["shift_years"]) < 1e-9, (m, lab)
    n_wrong = out["probes_parse"]["n_wrong_first"]
    assert n_wrong == json.load(open("results/exploratory.json"))["probe_wrong_by_size"]["n_wrong"], n_wrong
    json.dump(out, open("results/exploratory_p7.json", "w"), indent=1)
    print(json.dumps({k: out[k] for k in ("equivalence", "heterogeneity", "probes_parse")}, indent=1))
    print(json.dumps(out["mistral_reasoning"], indent=1))
    sp = out["spread"]
    print("between-model range by grade", {k: round(v, 3) for k, v in sp["between_model_range_by_grade"].items()})
    print("within-model change 3H-8H", {k: round(v, 3) for k, v in sp["within_model_change_3H_to_8H"].items()})
    print("between-model SD of level", sp["between_model_sd_of_level"], sp["sd_L3_minus_L1_ci95"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
