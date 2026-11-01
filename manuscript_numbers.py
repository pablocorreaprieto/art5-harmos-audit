"""Every number the ART 5 manuscript quotes, under a stable name, with the rounding used in the text.

Reads only archived outputs and the frozen design: results/numbers.json, results/measures.csv,
results/probes.csv, results/pilot_summary.json, results/validation_vikidia.json, logs/run_*.json,
data/raw/calls_*.jsonl (main study: dates and cost by provider) and design.json.
Writes results/manuscript_numbers.json: {name: {"value": raw value, "text": text as printed}}.
The manuscript source (manuscript/manuscript.md) refers to these names as {{name}};
manuscript/render.py replaces them and fails on an unknown name, and checks/check_numbers.py
fails on a number typed by hand in the source, on a rendered copy that differs from the render of
the source, and on a stale results/manuscript_numbers.json. No number of the manuscript is typed
by hand (protocol rule 3).
Written by the main session (claude-opus-5-5) on 1.11.2026, after the deposit; reporting only.

Usage: python manuscript_numbers.py [--out PATH]   (default results/manuscript_numbers.json)
"""
import argparse
import glob
import json
from datetime import datetime

import pandas as pd

MINUS = "−"
MODELS = ["anthropic_balanced", "anthropic_light", "openai_balanced", "openai_light",
          "mistral_balanced", "mistral_light"]
SHORT = {"h2_level_H": "h2H", "h2_level_P": "h2P", "h3_gradient_H": "h3H", "h3_gradient_P": "h3P"}
# decimals of each secondary measure in the text; shares are printed in percentage points
SECONDARY = {"median_zipf_content": (3, 1), "share_rare_content": (2, 100), "share_below4_content": (2, 100),
             "mean_word_length": (3, 1), "words_per_sentence": (2, 1), "n_words": (1, 1),
             "kandel_moles": (2, 1), "mean_zipf_form_films": (3, 1)}
OUT = {}


def num(x, d):
    s = f"{x:,.{d}f}"
    if s.startswith("-") and float(s.replace(",", "")) == 0:
        s = s[1:]  # never print a negative zero
    return s.replace("-", MINUS)


WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]


def put(name, value, text):
    if name in OUT:
        raise SystemExit(f"duplicate name {name}")
    OUT[name] = {"value": value, "text": text}
    # small counts also get a word form for prose (APA: words below 10), lower case and capitalised
    if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 20 and text == str(value):
        OUT[name + "_word"] = {"value": value, "text": WORDS[value]}
        OUT[name + "_Word"] = {"value": value, "text": WORDS[value].capitalize()}


def p_apa(p):
    """APA style without the leading zero, with its relation sign: '= .008', '< .001'."""
    if p < 0.001:
        return "< .001"
    s = f"{p:.3f}"
    return "= " + (s[1:] if s.startswith("0") else s)


def ci(name, lo, hi, d, scale=1):
    put(name + "_lo", lo, num(scale * lo, d))
    put(name + "_hi", hi, num(scale * hi, d))


def test(prefix, v, d, scale=1, with_t=True):
    """estimate, 95% CI, t, df, p of one t-test block of numbers.json"""
    put(prefix + "_est", v["estimate"], num(scale * v["estimate"], d))
    if "ci95" in v:
        ci(prefix + "_ci", v["ci95"][0], v["ci95"][1], d, scale)
    if with_t:
        put(prefix + "_t", v["t"], num(v["t"], 2))
        put(prefix + "_df", v["df"], str(v["df"]))
    put(prefix + "_p", v["p_two_sided"], p_apa(v["p_two_sided"]))


def flag_count(meas, col):
    return int(meas[col].astype(str).str.lower().isin(["true", "1"]).sum())


def day(ts):
    t = datetime.fromisoformat(ts)
    return f"{t.day} {t.strftime('%B')} {t.year}"


def main(out_path):
    n = json.load(open("results/numbers.json"))
    design = json.load(open("design.json"))
    meas = pd.read_csv("results/measures.csv", keep_default_na=False)
    probes = pd.read_csv("results/probes.csv", keep_default_na=False)
    pilot = json.load(open("results/pilot_summary.json"))
    vik = json.load(open("results/validation_vikidia.json"))
    runs = [json.load(open(f)) for f in sorted(glob.glob("logs/run_*.json"))]
    main_runs = [r for r in runs if r["calls_file"] == "calls.jsonl"]
    pilot_runs = [r for r in runs if r["calls_file"] == "calls_pilot.jsonl"]
    raw = [json.loads(line) for r in main_runs for line in open(r["raw_file"])]

    # design constants (from design.json)
    put("n_models", len(n["models"]), str(len(n["models"])))
    put("n_topics", n["n_topics"], str(n["n_topics"]))
    put("n_grades", len(design["grades"]), str(len(design["grades"])))
    put("n_genres", len(design["genres"]), str(len(design["genres"])))
    put("temperature", design["sampling"]["temperature"], num(design["sampling"]["temperature"], 1))
    put("max_output_tokens", design["sampling"]["max_output_tokens"], num(design["sampling"]["max_output_tokens"], 0))
    put("order_seed", design["order_seed"], str(design["order_seed"]))
    put("min_words", design["exclusion"]["min_words"], str(design["exclusion"]["min_words"]))
    put("sesoi_zipf", design["analysis"]["smallest_effect_of_interest_zipf"],
        num(design["analysis"]["smallest_effect_of_interest_zipf"], 2))
    put("min_ruler_slope", design["analysis"]["min_ruler_slope"], num(design["analysis"]["min_ruler_slope"], 2))
    put("bootstrap_resamples", design["analysis"]["bootstrap_resamples"],
        num(design["analysis"]["bootstrap_resamples"], 0))
    put("probe_repetitions", design["probe_repetitions"], str(design["probe_repetitions"]))
    put("n_probe_templates", len(design["probe_templates"]), str(len(design["probe_templates"])))
    put("l6_grades", len(design["labels"]["L6"]["grades"]), str(len(design["labels"]["L6"]["grades"])))
    for g, v in design["grades"].items():  # ages of each grade (design.json, from the HarmoS agreement)
        put(f"age_{g}_from", v["age_from"], str(v["age_from"]))
        put(f"age_{g}_to", v["age_to"], str(v["age_to"]))
    put("max_share_oov_pct", design["exclusion"]["max_share_out_of_lexicon"],
        num(100 * design["exclusion"]["max_share_out_of_lexicon"], 0))
    put("bootstrap_seed", design["analysis"]["bootstrap_seed"], str(design["analysis"]["bootstrap_seed"]))
    for m in MODELS:  # display names of the models, as in design.json
        put(f"name_{m}", design["models"][m].split(" (")[0], design["models"][m].split(" (")[0])
    lex = json.load(open("logs/lexicon.json"))
    version = lex["url"].rsplit("/", 1)[-1].replace("Lexique", "").split(".")[0]  # Lexique383.tsv -> 383
    put("lexique_version", version, version[0] + "." + version[1:])
    put("lexique_sha16", lex["sha256"], lex["sha256"][:16])
    # alpha and constants of the measure, from the preregistered code
    import importlib.util
    spec = importlib.util.spec_from_file_location("analyze_consts", "analyze.py")
    an = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(an)
    put("alpha", an.ALPHA, num(an.ALPHA, 2).lstrip("0"))
    put("max_extrapolation_years", an.MAX_EXTRAPOLATION, num(an.MAX_EXTRAPOLATION, 0))
    spec = importlib.util.spec_from_file_location("compute_consts", "compute.py")
    co = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(co)
    put("zipf_smoothing", co.SMOOTH, num(co.SMOOTH, 3))

    # data collection
    put("n_texts", n["n_texts"], num(n["n_texts"], 0))
    put("n_kept", n["n_kept"], num(n["n_kept"], 0))
    put("n_probes", len(probes), num(len(probes), 0))
    put("n_calls", main_runs[0]["to_do"], num(main_runs[0]["to_do"], 0))
    put("n_first_pass_failed", main_runs[0]["failed"], str(main_runs[0]["failed"]))
    put("n_excluded", n["n_texts"] - n["n_kept"], str(n["n_texts"] - n["n_kept"]))
    put("n_retries_texts", int((meas["attempt"].astype(int) > 1).sum()), str(int((meas["attempt"].astype(int) > 1).sum())))
    put("n_truncated", flag_count(meas, "truncated"), str(flag_count(meas, "truncated")))
    put("n_flag_meta", flag_count(meas, "flag_meta"), str(flag_count(meas, "flag_meta")))
    put("n_duplicates", flag_count(meas, "duplicate_text"), str(flag_count(meas, "duplicate_text")))
    put("n_meta_lines_removed", int(meas["n_meta_lines"].astype(int).sum()), str(int(meas["n_meta_lines"].astype(int).sum())))
    for lab, v in n["meta_by_label"].items():
        put(f"n_flag_{lab}", int(v["flag_meta"]), str(int(v["flag_meta"])))
    texts_per_topic = n["n_texts"] // n["n_topics"]
    put("texts_per_topic", texts_per_topic, str(texts_per_topic))
    spent = sum(r["spent_usd"] for r in main_runs)
    put("spend_total_usd", spent, num(spent, 2))
    put("spend_cap_usd", main_runs[0]["cap_usd"], num(main_runs[0]["cap_usd"], 0))
    for prov in ("anthropic", "openai", "mistral"):
        c = sum((r.get("cost_usd") or 0) for r in raw if r["provider"] == prov)
        put(f"spend_{prov}_usd", c, num(c, 2))
    put("collection_day", min(r["utc_start"] for r in raw), day(min(r["utc_start"] for r in raw)))
    if day(min(r["utc_start"] for r in raw)) != day(max(r["utc"] for r in raw)):
        raise SystemExit("collection spans several days: add a collection_end name")
    put("n_temperature_omitted", sum(1 for r in raw if "temperature" not in (r.get("sampling") or {})),
        str(sum(1 for r in raw if "temperature" not in (r.get("sampling") or {}))))
    for m in MODELS:
        ids = sorted(set(meas.loc[meas["model"] == m, "model_returned"]))
        if len(ids) != 1:
            raise SystemExit(f"{m} returned several model ids: {ids}")
        put(f"id_{m}", ids[0], ids[0])
        w = meas.loc[meas["model"] == m, "n_words"].astype(float)
        put(f"words_mean_{m}", w.mean(), num(w.mean(), 0))
    w = meas["n_words"].astype(float)
    put("words_mean_all", w.mean(), num(w.mean(), 0))
    put("words_median_all", w.median(), num(w.median(), 0))
    put("words_min_all", w.min(), num(w.min(), 0))
    put("words_max_all", w.max(), num(w.max(), 0))

    # pilot and measure validity
    put("pilot_calls", pilot_runs[0]["to_do"], str(pilot_runs[0]["to_do"]))
    put("pilot_texts", pilot["ruler"]["n_kept"], str(pilot["ruler"]["n_kept"]))
    put("pilot_probes", pilot_runs[0]["to_do"] - pilot["ruler"]["n_planned"],
        str(pilot_runs[0]["to_do"] - pilot["ruler"]["n_planned"]))
    put("pilot_spend_usd", sum(r["spent_usd"] for r in pilot_runs), num(sum(r["spent_usd"] for r in pilot_runs), 2))
    put("pilot_topics", len(design["pilot"]["ruler"]["topics"]), str(len(design["pilot"]["ruler"]["topics"])))
    put("pilot_models", len(design["pilot"]["ruler"]["models"]), str(len(design["pilot"]["ruler"]["models"])))
    put("pilot_sd", pilot["ruler"]["sigma"], num(pilot["ruler"]["sigma"], 3))
    put("pilot_sd_upper80", pilot["ruler"]["sigma_upper80"], num(pilot["ruler"]["sigma_upper80"], 3))
    put("pilot_slope", pilot["ruler"]["pooled_slope"], num(pilot["ruler"]["pooled_slope"], 3))
    put("pilot_slope_p", pilot["ruler"]["pooled_slope_p_one_sided"], p_apa(pilot["ruler"]["pooled_slope_p_one_sided"]))
    pw = pilot["power_level_test_0_04_zipf"]
    for k in ("16", "24", "32"):
        put(f"pilot_power_{k}", pw[k], num(pw[k], 3).lstrip("0"))
    put("vik_subjects", len(vik["pairs"]), str(len(vik["pairs"])))
    put("vik_usable", vik["n_pairs_usable"], str(vik["n_pairs_usable"]))
    put("vik_higher", vik["vikidia_higher"], str(vik["vikidia_higher"]))
    put("vik_p", vik["sign_test_p_one_sided"], p_apa(vik["sign_test_p_one_sided"]))
    put("vik_mean_diff", vik["mean_difference_zipf"], num(vik["mean_difference_zipf"], 2))

    # primary tests
    for k, s in SHORT.items():
        v = n["primary"][k]
        d = 3 if s.startswith("h2") else 4
        test(s, v, d)
        put(s + "_pholm", v["p_holm"], p_apa(v["p_holm"]))
        put(s + "_ntopics", v["n_topics"], str(v["n_topics"]))
    # same contrasts by OLS with clustered standard errors (secondary)
    for k, s in SHORT.items():
        v = n["secondary_ols_clustered"][k]
        test("ols_" + s, v, 3 if s.startswith("h2") else 4)

    # H1, the age-only rulers
    slopes = {m: v["slope"] for m, v in n["h1"].items()}
    put("h1_n_supported", n["h1_models_supported"], str(n["h1_models_supported"]))
    put("h1_slope_min", min(slopes.values()), num(min(slopes.values()), 3))
    put("h1_slope_max", max(slopes.values()), num(max(slopes.values()), 3))
    put("h1_p_max", max(v["p_one_sided"] for v in n["h1"].values()),
        p_apa(max(v["p_one_sided"] for v in n["h1"].values())))
    put("h1_lin_p_min", min(v["linearity_p"] for v in n["h1"].values()),
        p_apa(min(v["linearity_p"] for v in n["h1"].values())))
    for m, v in n["h1"].items():
        put(f"h1_slope_{m}", v["slope"], num(v["slope"], 3))
    m_flat, m_steep = max(slopes, key=slopes.get), min(slopes, key=slopes.get)
    put("h1_slope_max_model", m_flat, design["models"][m_flat].split(" (")[0])
    put("h1_slope_min_model", m_steep, design["models"][m_steep].split(" (")[0])
    put("n_eligible_ae", len(n["age_equivalent"]["eligible_models"]), str(len(n["age_equivalent"]["eligible_models"])))

    # age equivalents (model-internal, years)
    for lab, v in n["age_equivalent"]["by_label"].items():
        put(f"ae_{lab}_shift", v["shift_years"], num(v["shift_years"], 2))
        ci(f"ae_{lab}_shift_ci", v["shift_ci95"][0], v["shift_ci95"][1], 2)
        put(f"ae_{lab}_track", v["tracking"], num(v["tracking"], 2))
        ci(f"ae_{lab}_track_ci", v["tracking_ci95"][0], v["tracking_ci95"][1], 2)
        if "isotonic_shift_years" in v:
            put(f"ae_{lab}_iso_shift", v["isotonic_shift_years"], num(v["isotonic_shift_years"], 2))
            put(f"ae_{lab}_iso_track", v["isotonic_tracking"], num(v["isotonic_tracking"], 2))
        for m, w in v.get("by_model", {}).items():
            put(f"ae_{lab}_{m}_shift", w["shift_years"], num(w["shift_years"], 2))
            ci(f"ae_{lab}_{m}_shift_ci", w["shift_ci95"][0], w["shift_ci95"][1], 2)
            put(f"ae_{lab}_{m}_track", w["tracking"], num(w["tracking"], 2))
            ci(f"ae_{lab}_{m}_track_ci", w["tracking_ci95"][0], w["tracking_ci95"][1], 2)
    for k, v in n["age_equivalent"]["isotonic_cell_flags"].items():
        put(f"iso_cells_{k}", v, str(v))
    l0 = n["age_equivalent"]["l0_default_age"]
    put("l0_age_min", min(l0.values()), num(min(l0.values()), 1))
    put("l0_age_max", max(l0.values()), num(max(l0.values()), 1))
    for m, v in l0.items():
        put(f"l0_age_{m}", v, num(v, 1))

    # secondary contrasts on L3, the L6 control, exploratory contrasts
    for k, v in n["gloss"].items():
        test(k, v, 3 if "level" in k else 4)
    c = n["controls"]["l6_vs_l5_level_3h_to_5h"]
    test("l6_level", c, 3)
    for g, v in n["controls"]["l6_vs_l5_by_grade"].items():
        put(f"l6_level_{g}", v["estimate"], num(v["estimate"], 3))
    for k, v in n["exploratory"]["other_labels"].items():
        test("x_" + k, v, 3 if "level" in k else 4)
    for g, block in n["exploratory"]["grade_profile"].items():
        for lab, v in block.items():
            test(f"gp_{lab}_{g}", v, 3, with_t=False)
    for m, block in n["exploratory"]["per_model"].items():
        for k, s in SHORT.items():
            test(f"pm_{m}_{s}", block[k], 3 if s.startswith("h2") else 4, with_t=False)

    # sensitivity analyses and secondary measures
    for sname, block in n["sensitivity"].items():
        for k, s in SHORT.items():
            if k in block:
                d = 3 if s.startswith("h2") else 4
                put(f"sens_{sname}_{s}_est", block[k]["estimate"], num(block[k]["estimate"], d))
                put(f"sens_{sname}_{s}_p", block[k]["p_two_sided"], p_apa(block[k]["p_two_sided"]))
    for d_kind, keys in (("level", ["h2_level_H", "h2_level_P"]), ("gradient", ["h3_gradient_H", "h3_gradient_P"])):
        diffs = [abs(n["sensitivity"][s][k]["estimate"] - n["primary"][k]["estimate"])
                 for s in ("without_truncated", "without_duplicate_text", "without_flag_meta") for k in keys]
        put(f"sens_max_abs_diff_{d_kind}", max(diffs), num(max(diffs), 4))
    pdiff = max(abs(n["secondary_ols_clustered"][k]["p_two_sided"] - n["primary"][k]["p_two_sided"]) for k in SHORT)
    put("ols_p_max_abs_diff", pdiff, num(pdiff, 3).lstrip("0"))
    for lab in ("L1", "L1P"):
        tr = {m: v["tracking"] for m, v in n["age_equivalent"]["by_label"][lab]["by_model"].items()}
        good = [v for v in tr.values() if v >= 1]
        put(f"ae_{lab}_n_track_ge1", len(good), str(len(good)))
        if good:
            put(f"ae_{lab}_track_ge1_min", min(good), num(min(good), 2))
            put(f"ae_{lab}_track_ge1_max", max(good), num(max(good), 2))
    for mname, block in n["secondary_measures"].items():
        d, scale = SECONDARY[mname]
        for k, s in SHORT.items():
            dd = d if s.startswith("h2") else d + 1
            put(f"sec_{mname}_{s}_est", block[k]["estimate"], num(scale * block[k]["estimate"], dd))
            put(f"sec_{mname}_{s}_p", block[k]["p_two_sided"], p_apa(block[k]["p_two_sided"]))
            if mname == "n_words":
                put(f"sec_{mname}_{s}_abs", abs(block[k]["estimate"]), num(abs(block[k]["estimate"]), 0))

    # knowledge probes, in percent: first stated range correct, any stated range correct
    pr = n["probes"]
    put("probe_parsed_pct", pr["share_parsed"], num(100 * pr["share_parsed"], 1))
    put("probe_multiple_pct", pr["share_multiple"], num(100 * pr["share_multiple"], 0))
    for key, v in pr["accuracy_by_model_notation"].items():
        m, notation = [x.strip() for x in key.split("|")]
        put(f"probe_{m}_{notation}", v["correct_first"], num(100 * v["correct_first"], 0))
        put(f"probe_any_{m}_{notation}", v["correct_any"], num(100 * v["correct_any"], 0))
    for notation, v in pr["accuracy_by_notation"].items():
        put(f"probe_all_{notation}", v["correct_first"], num(100 * v["correct_first"], 0))
        put(f"probe_any_all_{notation}", v["correct_any"], num(100 * v["correct_any"], 0))
    per_cell = pr["accuracy_by_model_notation"]
    put("probes_per_model_notation", int(len(probes) / len(per_cell)), str(int(len(probes) / len(per_cell))))

    # exploratory analyses of exploratory.py (preregistered as exploratory, computed after the deposit)
    ex = json.load(open("results/exploratory.json"))
    for key, v in ex["probe_errors"].items():
        m, notation = [x.strip() for x in key.split("|")]
        put(f"perr_{m}_{notation}", v["mean_signed_error_years"], num(v["mean_signed_error_years"], 2))
        put(f"pold_{m}_{notation}", v["share_too_old"], num(100 * v["share_too_old"], 0))
        put(f"pyoung_{m}_{notation}", v["share_too_young"], num(100 * v["share_too_young"], 0))
    for lab, v in ex["mentions"]["by_label"].items():
        put(f"mention_age_{lab}", v["share_age"], num(100 * v["share_age"], 0))
        put(f"mention_grade_{lab}", v["share_grade"], num(100 * v["share_grade"], 0))

    json.dump(OUT, open(out_path, "w"), indent=1, ensure_ascii=False)
    print(f"wrote {out_path} with {len(OUT)} named numbers")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/manuscript_numbers.json")
    main(ap.parse_args().out)
