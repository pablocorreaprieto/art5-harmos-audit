"""Render the ART 5 manuscript and its supporting information from their sources.

python manuscript/render.py            (from the repository root)

Reads manuscript/manuscript.md and manuscript/supplement.md, where every number is a {{name}}
placeholder of results/manuscript_numbers.json, every table a {{table:name}} placeholder and every
figure a {{figure:name}} placeholder. Writes manuscript/build/manuscript.md and .docx, and
manuscript/build/supplement.md and .docx (pandoc). Stops on an unknown placeholder.
Prints the word count of the main text (Introduction to Conclusion, without tables, figure captions,
references and statements), the measure used against the journal's limit.
Written by the main session (claude-opus-5-5) on 1.11.2026; presentation only.
"""
import json
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS = ["anthropic_balanced", "anthropic_light", "openai_balanced", "openai_light",
          "mistral_balanced", "mistral_light"]
MINUS = "−"


def load(root=ROOT):
    nums = json.load(open(os.path.join(root, "results/manuscript_numbers.json")))
    facts = json.load(open(os.path.join(root, "manuscript/process_facts.json")))
    for k, v in facts.items():
        if not k.startswith("_"):
            nums["proc_" + k] = {"value": v["text"], "text": v["text"]}
    src = os.path.join(root, "manuscript/source_facts.json")
    if os.path.exists(src):
        for k, v in json.load(open(src)).items():
            if not k.startswith("_"):
                nums["src_" + k] = {"value": v["text"], "text": v["text"], "ref": v["ref"], "where": v["where"]}
    design = json.load(open(os.path.join(root, "design.json")))
    return nums, design


def T(nums, name):
    if name not in nums:
        raise SystemExit(f"unknown number name: {name}")
    return nums[name]["text"]


def ci(nums, stem):
    return f"[{T(nums, stem + '_lo')}, {T(nums, stem + '_hi')}]"


def label_wording(design, lab, grade="5H"):
    g = design["grades"][grade]
    text = design["labels"][lab]["text"].format(n=g["n"], french=g["french"], age_from=g["age_from"], age_to=g["age_to"])
    return text.strip()


def table_labels(nums, design):
    gloss = {"L1": "bare HarmoS label", "L1P": "bare P label (Vaud, Geneva)", "L2": "H label and region",
             "L3": "H label and age", "L4": "French grade", "L5": "age only (reference)",
             "L6": "same digit, French lower-secondary suffix (collision control)", "L0": "no level (baseline)"}
    grades_of = {"all": "3H to 8H", "none": "one text per model, genre and topic"}
    rows = ["| Code | Wording for 5H | Role | Grades |", "|---|---|---|---|"]
    for lab in ["L1", "L1P", "L2", "L3", "L4", "L5", "L6", "L0"]:
        g = design["labels"][lab]["grades"]
        gtxt = grades_of.get(g, None) if isinstance(g, str) else f"{g[0]} to {g[-1]}"
        w = label_wording(design, lab) if lab != "L0" else ""
        rows.append(f"| {lab} | {'« ' + w + ' »' if w else '(none)'} | {gloss[lab]} | {gtxt} |")
    cap = ("Table 1. The eight labels, with the wording each gives for grade 5H (pupils aged "
           f"{design['grades']['5H']['age_from']} to {design['grades']['5H']['age_to']}). The label follows "
           "« pour des élèves » in the prompt.")
    return cap, "\n".join(rows)


def table_primary(nums, design):
    rows = ["| Test | Contrast | Estimate [95% CI] | *t*(" + T(nums, "h2H_df") + ") | *p* | Holm *p* | In years [95% CI] |",
            "|---|---|---|---|---|---|---|"]
    spec = [("H2-H", "Level, « de 5H » − age", "h2H", "ae_L1_shift", "shift"),
            ("H2-P", "Level, « de 5P » − age", "h2P", "ae_L1P_shift", "shift"),
            ("H3-H", "Gradient, « de 5H » − age", "h3H", "ae_L1_track", "tracking"),
            ("H3-P", "Gradient, « de 5P » − age", "h3P", "ae_L1P_track", "tracking")]
    for test, contrast, s, ae, kind in spec:
        p = T(nums, s + "_p").replace("= ", "")
        ph = T(nums, s + "_pholm").replace("= ", "")
        rows.append(f"| {test} | {contrast} | {T(nums, s + '_est')} {ci(nums, s + '_ci')} | {T(nums, s + '_t')} | "
                    f"{p} | {ph} | {kind} {T(nums, ae)} {ci(nums, ae + '_ci')} |")
    cap = ("Table 2. Primary tests. Levels in Zipf, gradients in Zipf per year of age; one-sample *t*-tests "
           f"over {T(nums, 'n_topics')} topics, Holm correction over the four tests. Shift: years older than the "
           "age requested; tracking: 1 = follows the grade like the age-only texts, 0 = ignores it.")
    return cap, "\n".join(rows)


def table_models(nums, design):
    rows = ["| Model | Ruler slope (Zipf per year) | Default age, no level (years) [95% CI] | Probes correct, H (%) | "
            "Probes correct, P (%) | Mean probe error, H (years) | Mean probe error, P (years) |",
            "|---|---|---|---|---|---|---|"]
    for m in MODELS:
        rows.append(f"| {T(nums, 'name_' + m)} | {T(nums, 'h1_slope_' + m)} | {T(nums, 'l0_age_' + m)} {ci(nums, f'ph_l0_{m}_ci')} | "
                    f"{T(nums, f'probe_{m}_H')} | {T(nums, f'probe_{m}_P')} | {T(nums, f'perr_{m}_H')} | "
                    f"{T(nums, f'perr_{m}_P')} |")
    cap = ("Table 3. Model by model: slope of the age-only ruler (H1), age written for without a level (L0, a "
           "preregistered control, placed on the model's own ruler; intervals from the topic bootstrap, post hoc) and "
           f"knowledge probes ({T(nums, 'probes_per_model_notation')} per notation; first age range stated, Table S7 gives "
           "any range; error = age stated minus true age, positive when too old). The probes are exploratory.")
    return cap, "\n".join(rows)


def table_s1(nums, design):
    rows = ["| Analysis | H2-H level | H2-P level | H3-H gradient | H3-P gradient |", "|---|---|---|---|---|"]
    def cell(prefix, s):
        return f"{T(nums, f'{prefix}{s}_est')} (*p* {T(nums, f'{prefix}{s}_p')})"
    shorts = ["h2H", "h2P", "h3H", "h3P"]
    rows.append("| Primary, topic-level *t*-tests | " + " | ".join(cell("", s) for s in shorts) + " |")
    rows.append("| OLS, model × grade cells, errors clustered by topic | " + " | ".join(cell("ols_", s) for s in shorts) + " |")
    for key, name in [("without_truncated", "Truncated texts removed"),
                      ("without_flag_meta", "Texts addressing the user removed"),
                      ("length_residualised", "Length residualised within model")]:
        rows.append(f"| {name} | " + " | ".join(cell(f"sens_{key}_", s) for s in shorts) + " |")
    cap = ("Table S1. Primary contrasts under the preregistered sensitivity analyses (levels in Zipf, gradients in "
           "Zipf per year). No text was an exact duplicate, so the duplicate rule removed nothing. Age equivalents read "
           f"on an isotonic fit of each ruler, averaged over the six models: shift {T(nums, 'ae_L1_iso_shift')} "
           f"years and tracking {T(nums, 'ae_L1_iso_track')} for « de 5H », shift {T(nums, 'ae_L1P_iso_shift')} and "
           f"tracking {T(nums, 'ae_L1P_iso_track')} for « de 5P »; the linear readings averaged the same way give "
           f"{T(nums, 'ph_unweighted_L1_shift')} and {T(nums, 'ph_unweighted_L1_track')}, and {T(nums, 'ph_unweighted_L1P_shift')} "
           f"and {T(nums, 'ph_unweighted_L1P_track')} (the main text pools the models as sums of levels over sums of slopes). "
           f"Over all labels, grades and models, {T(nums, 'iso_cells_inside')} cells were read inside the isotonic "
           f"ruler, {T(nums, 'iso_cells_extrapolated')} extrapolated and {T(nums, 'iso_cells_capped')} capped at "
           f"{T(nums, 'max_extrapolation_years')} years beyond its ends; no intervals were computed for this reading.")
    return cap, "\n".join(rows)


def table_s2(nums, design):
    names = [("median_zipf_content", "Median Zipf, content lemmas"), ("share_rare_content", "Content lemmas below Zipf 3 (percentage points)"),
             ("share_below4_content", "Content lemmas below Zipf 4 (percentage points)"), ("mean_word_length", "Mean word length (letters)"),
             ("words_per_sentence", "Words per sentence"), ("n_words", "Number of words"),
             ("kandel_moles", "Kandel–Moles readability"), ("mean_zipf_form_films", "Mean Zipf, word forms in films")]
    rows = ["| Measure | H2-H level | H2-P level | H3-H gradient | H3-P gradient |", "|---|---|---|---|---|"]
    for key, name in names:
        rows.append(f"| {name} | " + " | ".join(f"{T(nums, f'sec_{key}_{s}_est')} (*p* {T(nums, f'sec_{key}_{s}_p')})"
                                               for s in ["h2H", "h2P", "h3H", "h3P"]) + " |")
    cap = ("Table S2. The primary contrasts on the eight preregistered secondary measures (label minus age only; "
           "gradients per year of age; one-sample *t*-tests over topics, no correction for multiplicity). Higher "
           "Kandel–Moles scores mean easier texts.")
    return cap, "\n".join(rows)


def table_s3(nums, design):
    labs = [("L1", "« de 5H »"), ("L1P", "« de 5P »"), ("L2", "« de 5H en Suisse romande »"),
            ("L3", "« de 5H (8 à 9 ans) »"), ("L4", "« de CE2 »"), ("L6", "« de 5e » (3H to 5H)")]
    rows = ["| Label | Model | Shift, years [95% CI] | Tracking [95% CI] |", "|---|---|---|---|"]
    for lab, w in labs:
        rows.append(f"| {lab} {w} | All six | {T(nums, f'ae_{lab}_shift')} {ci(nums, f'ae_{lab}_shift_ci')} | "
                    f"{T(nums, f'ae_{lab}_track')} {ci(nums, f'ae_{lab}_track_ci')} |")
        for m in MODELS:
            rows.append(f"| | {T(nums, 'name_' + m)} | {T(nums, f'ae_{lab}_{m}_shift')} {ci(nums, f'ae_{lab}_{m}_shift_ci')} | "
                        f"{T(nums, f'ae_{lab}_{m}_track')} {ci(nums, f'ae_{lab}_{m}_track_ci')} |")
    cap = ("Table S3. Model-internal age equivalents by label, pooled and model by model (exploratory for single "
           f"models), with 95% percentile intervals from {T(nums, 'bootstrap_resamples')} bootstrap resamples of topics. "
           "Models are listed by provider, the mid-priced model first; Table S11 summarises them by price tier. "
           "Readings of « de 5e » lie beyond the ages of the rulers and are linear extrapolations.")
    return cap, "\n".join(rows)


def table_s4(nums, design):
    rows = ["| Model | H2-H level | H2-P level | H3-H gradient | H3-P gradient |", "|---|---|---|---|---|"]
    for m in MODELS:
        rows.append(f"| {T(nums, 'name_' + m)} | " + " | ".join(
            f"{T(nums, f'pm_{m}_{s}_est')} {ci(nums, f'pm_{m}_{s}_ci')}" for s in ["h2H", "h2P", "h3H", "h3P"]) + " |")
    cap = ("Table S4. The primary contrasts model by model (exploratory), with 95% confidence intervals over topics; "
           "levels in Zipf, gradients in Zipf per year.")
    return cap, "\n".join(rows)


def table_s5(nums, design):
    rows = ["| Contrast | Estimate [95% CI] | *p* |", "|---|---|---|"]
    spec = [("« de 5H (8 à 9 ans) » − age only, level", "gloss_level_vs_age"),
            ("« de 5H (8 à 9 ans) » − age only, gradient", "gloss_gradient_vs_age"),
            ("« de 5H (8 à 9 ans) » − « de 5H », level", "gloss_level_vs_bare"),
            ("« de 5H (8 à 9 ans) » − « de 5H », gradient", "gloss_gradient_vs_bare"),
            ("« de 5H en Suisse romande » − age only, level", "x_L2_level"),
            ("« de 5H en Suisse romande » − age only, gradient", "x_L2_gradient"),
            ("« de 5H en Suisse romande » − « de 5H », level (post hoc)", "ph_L2mL1_level"),
            ("« de CE2 » − age only, level", "x_L4_level"), ("« de CE2 » − age only, gradient", "x_L4_gradient"),
            ("« de 5P » − « de 5H », level (not in the registered list)", "x_P_vs_H_level"),
            ("« de 5P » − « de 5H », gradient (not in the registered list)", "x_P_vs_H_gradient"),
            ("« de 5e » − age only, level at 3H to 5H", "l6_level")]
    for name, s in spec:
        rows.append(f"| {name} | {T(nums, s + '_est')} {ci(nums, s + '_ci')} | {T(nums, s + '_p').replace('= ', '')} |")
    cap = ("Table S5. Secondary (L3), exploratory and post hoc contrasts, one-sample *t*-tests over topics, levels in "
           "Zipf and gradients in Zipf per year; no correction for multiplicity. The contrast of the P and H labels was "
           "computed by the preregistered analysis code but is not in the list of the registration text.")
    return cap, "\n".join(rows)


def table_s6(nums, design):
    rows = ["| Grade | « de 5H » − age | « de 5P » − age | « de 5H (8 à 9 ans) » − age |", "|---|---|---|---|"]
    for g in ["3H", "4H", "5H", "6H", "7H", "8H"]:
        rows.append(f"| {g} | " + " | ".join(f"{T(nums, f'gp_{lab}_{g}_est')} {ci(nums, f'gp_{lab}_{g}_ci')}"
                                             for lab in ["L1", "L1P", "L3"]) + " |")
    cap = ("Table S6. Level differences grade by grade (exploratory; in the second column the label is « de "
           "{n}P » for each grade), in Zipf, with 95% confidence intervals over topics.")
    return cap, "\n".join(rows)


def table_s7(nums, design):
    rows = ["| Model | Notation | First range correct (%) | Any range correct (%) | Too old (%) | Too young (%) | Mean error (years) |",
            "|---|---|---|---|---|---|---|"]
    for m in MODELS:
        for nt in ["H", "P"]:
            rows.append(f"| {T(nums, 'name_' + m)} | {nt} | {T(nums, f'probe_{m}_{nt}')} | {T(nums, f'probe_any_{m}_{nt}')} | "
                        f"{T(nums, f'pold_{m}_{nt}')} | {T(nums, f'pyoung_{m}_{nt}')} | {T(nums, f'perr_{m}_{nt}')} |")
    cap = (f"Table S7. Knowledge probes ({T(nums, 'probes_per_model_notation')} per model and notation; "
           f"{T(nums, 'probe_parsed_pct')}% of answers stated an age range, {T(nums, 'probe_multiple_pct')}% more than one). "
           "Too old or too young: midpoint of the first range outside the true range widened by half a year.")
    return cap, "\n".join(rows)


def table_s8(nums, design):
    rows = ["| Label | Texts naming an age (%) | Texts naming a grade (%) |", "|---|---|---|"]
    for lab in ["L0", "L1", "L1P", "L2", "L3", "L4", "L5", "L6"]:
        rows.append(f"| {lab} | {T(nums, 'mention_age_' + lab)} | {T(nums, 'mention_grade_' + lab)} |")
    cap = ("Table S8. Texts whose body (title excluded) names an age (« huit ans », « 8 ans ») or a school grade "
           "(« 5H », « CE2 », « 5e »), by label (exploratory; a story character's age counts as a mention).")
    return cap, "\n".join(rows)


def table_s9(nums, design):
    labs = ["L0", "L1", "L1P", "L2", "L3", "L4", "L5", "L6"]
    rows = ["| Model | " + " | ".join(labs) + " |", "|---|" + "---|" * len(labs)]
    for m in MODELS:
        rows.append(f"| {T(nums, 'name_' + m)} | " + " | ".join(T(nums, f"ph_rt_share_{m}_{lab}") for lab in labs) + " |")
    cap = ("Table S9. Share of texts (%) for which the model reported reasoning or thinking tokens, by model and label, "
           "from the usage fields of the providers' answers, with reasoning left at each provider's default (post hoc).")
    return cap, "\n".join(rows)


def table_s10(nums, design):
    rows = ["| Model left out | H2-H level | H2-P level | H3-H gradient | H3-P gradient |", "|---|---|---|---|---|"]
    rows.append("| None (primary) | " + " | ".join(f"{T(nums, s + '_est')} (*p* {T(nums, s + '_p')})"
                                                 for s in ["h2H", "h2P", "h3H", "h3P"]) + " |")
    for m in MODELS:
        rows.append(f"| {T(nums, 'name_' + m)} | " + " | ".join(
            f"{T(nums, f'ph_loo_{m}_{s}_est')} (*p* {T(nums, f'ph_loo_{m}_{s}_p')})" for s in ["h2H", "h2P", "h3H", "h3P"]) + " |")
    cap = ("Table S10. The four primary contrasts without each model in turn (post hoc; topic-level *t*-tests as in the "
           "primary analysis, uncorrected *p*-values; levels in Zipf, gradients in Zipf per year).")
    return cap, "\n".join(rows)


def table_s11(nums, design):
    names = {"L1": "« de 5H »", "L1P": "« de 5P »", "L2": "« de 5H en Suisse romande »", "L3": "« de 5H (8 à 9 ans) »",
             "L4": "« de CE2 »"}
    rows = ["| Label | SD of the six shifts (years) | SD of the six trackings | Mean absolute shift, mid-priced / lighter (years) | "
            "Mean absolute tracking − 1, mid-priced / lighter |", "|---|---|---|---|---|"]
    for lab, w in names.items():
        tier = (f"{T(nums, f'ph_tier_{lab}_balanced_abs_shift')} / {T(nums, f'ph_tier_{lab}_light_abs_shift')}"
                if f"ph_tier_{lab}_balanced_abs_shift" in nums else "")
        tr = (f"{T(nums, f'ph_tier_{lab}_balanced_abs_track')} / {T(nums, f'ph_tier_{lab}_light_abs_track')}"
              if f"ph_tier_{lab}_balanced_abs_track" in nums else "")
        rows.append(f"| {lab} {w} | {T(nums, f'ph_disp_{lab}_shift')} | {T(nums, f'ph_disp_{lab}_track')} | {tier} | {tr} |")
    cap = ("Table S11. How far the six models' readings of each label spread (standard deviation across models of the "
           "per-model shift and tracking of Table S3), and, for the bare labels, the mean absolute departure of the "
           "three mid-priced and the three lighter models (the preregistered exploratory analysis by provider and model "
           "size; one model per cell, so descriptive only). Post hoc except the tier summary.")
    return cap, "\n".join(rows)


def table_s12(nums, design):
    names = {"L1": "« de 5H »", "L1P": "« de 5P »", "L2": "« de 5H en Suisse romande »", "L3": "« de 5H (8 à 9 ans) »",
             "L4": "« de CE2 »", "L5": "age only"}
    rows = ["| Label | Traces stating an age (%) | Age wrong (%) | Two years too old (%) | Mean error (years) |",
            "|---|---|---|---|---|"]
    for lab, w in names.items():
        rows.append(f"| {lab} {w} | {T(nums, f'ph_mr_state_{lab}')} | {T(nums, f'ph_mr_wrong_{lab}')} | "
                    f"{T(nums, f'ph_mr_two_{lab}')} | {T(nums, f'ph_mr_err_{lab}')} |")
    cap = ("Table S12. Age stated for the pupils in the visible reasoning of " + T(nums, "name_mistral_balanced") +
           " before writing each text, by label (post hoc). First age range in the trace with a midpoint between "
           f"{T(nums, 'ph_mr_window_lo')} and {T(nums, 'ph_mr_window_hi')} years; wrong by the preregistered probe rule; "
           f"two years too old: midpoint {T(nums, 'ph_mr_two_lo')} to {T(nums, 'ph_mr_two_hi')} years above the true one. "
           f"A random sample of {T(nums, 'ph_mr_sample_n')} traces with the extracted age is in the repository.")
    return cap, "\n".join(rows)


TABLES = {"labels": table_labels, "primary": table_primary, "models": table_models, "s1": table_s1, "s2": table_s2,
          "s3": table_s3, "s4": table_s4, "s5": table_s5, "s6": table_s6, "s7": table_s7, "s8": table_s8,
          "s9": table_s9, "s10": table_s10, "s11": table_s11, "s12": table_s12}

FIGURES = {
    "fig1": ("fig1_rulers.png", "Figure 1. Age-only rulers. Mean Zipf frequency of the content lemmas of the texts "
             "requested with the age only, by age requested, for the mid-priced (circles) and lighter (squares) model of "
             "each provider. Bands are 95% confidence intervals of each mean over {n_topics} topics, so they include the "
             "differences between topics, whereas the slopes are estimated within topics. Higher values mean more "
             "frequent words."),
    "fig2": ("fig2_labels.png", "Figure 2. Age equivalents of the label wordings, pooled over the six models: shift "
             "(years older than the age requested) and tracking (1 = follows the grade like the age-only texts, 0 = "
             "ignores it), with 95% bootstrap intervals over topics. The collision control « de 5e » lies far outside "
             "these axes and is reported in the text."),
    "fig3": ("fig3_models.png", "Figure 3. Shift and tracking of the bare labels « de 5H » (circles) and « de 5P » "
             "(squares), model by model, with 95% bootstrap intervals over topics (exploratory)."),
}


def citation_forms(ref):
    """Parenthetical and narrative forms of a reference's in-text citation (APA 7)."""
    par = ref["cite"]
    name, year = par.rsplit(", ", 1)
    return par, f"{name.replace(' & ', ' and ')} ({year})"


def reference_list(text, root=ROOT):
    """APA entries of the references cited in text, in alphabetical order."""
    refs = json.load(open(os.path.join(root, "manuscript/references.json")))
    cited = [r for r in refs if any(f in text for f in citation_forms(r))]
    # APA order ignores diacritics (État sorts as Etat; fixed after the second confirmation reading, 1.11.2026)
    def key(r):
        return unicodedata.normalize("NFKD", r["apa"]).encode("ascii", "ignore").decode().lower()
    return "\n\n".join(r["apa"] for r in sorted(cited, key=key))


def render_text(src, nums, design, fig_dir, root=ROOT):
    def table(m):
        name = m.group(1)
        if name not in TABLES:
            raise SystemExit(f"unknown table: {name}")
        cap, body = TABLES[name](nums, design)
        return f"{cap}\n\n{body}\n"

    def figure(m):
        name = m.group(1)
        if name not in FIGURES:
            raise SystemExit(f"unknown figure: {name}")
        f, cap = FIGURES[name]
        return f"![{cap.format(n_topics=T(nums, 'n_topics'))}]({fig_dir}/{f})\n"

    src = re.sub(r"<!--.*?-->\n?", "", src, flags=re.S)  # comments may name placeholders
    out = re.sub(r"\{\{table:([a-z0-9_]+)\}\}", table, src)
    out = re.sub(r"\{\{figure:([a-z0-9_]+)\}\}", figure, out)
    out = re.sub(r"\{\{(?!references\}\})([A-Za-z0-9_]+)\}\}", lambda m: T(nums, m.group(1)), out)
    if "{{references}}" in out:
        out = out.replace("{{references}}", reference_list(out.split("{{references}}")[0], root))
    left = re.findall(r"\{\{[^}]*\}\}", out)
    if left:
        raise SystemExit(f"unresolved placeholders: {left[:5]}")
    return out


def words(md, start="Introduction", end="Statements", tables=False):
    """Words as a word processor counts them (runs of non-space characters), from the heading `start` to the
    heading `end`, headings included without their # marks. Table rows, figure lines and table captions are
    left out unless tables=True, in which case the cells and captions count and the separator rows do not.
    One rule for the title page and the verification report (after the second confirmation reading, 1.11.2026,
    which found three different counts)."""
    m = re.search(rf"^# {start}\s*$(.*?)^# {end}\s*$", md, flags=re.S | re.M)
    body = (f"# {start}\n" + m.group(1)) if m else ""
    n = 0
    for line in body.splitlines():
        s = line.strip()
        if not s or re.fullmatch(r"\|[-|: ]+\|", s):
            continue
        is_table = s.startswith("|") or s.startswith("![") or re.match(r"^Table S?\d+\.", s)
        if is_table and not tables:
            continue
        if s.startswith("!["):
            s = re.sub(r"^!\[(.*)\]\(.*\)$", r"\1", s)
        s = re.sub(r"^#+\s*", "", s).replace("|", " ")
        n += len(s.split())
    return n


def main_text_words(md):
    """Words from Introduction to Conclusion, without tables, figure lines and table captions."""
    return words(md)


def main():
    nums, design = load()
    os.makedirs(os.path.join(ROOT, "manuscript/build"), exist_ok=True)
    for stem in ("manuscript", "supplement"):
        path = os.path.join(ROOT, f"manuscript/{stem}.md")
        if not os.path.exists(path):
            continue
        md = render_text(open(path).read(), nums, design, "../../results/figures")
        out = os.path.join(ROOT, f"manuscript/build/{stem}.md")
        open(out, "w").write(md)
        docx = out[:-3] + ".docx"
        subprocess.run(["pandoc", out, "-o", docx, "--resource-path", os.path.dirname(out)], check=True)
        print("wrote", out, "and", docx)
        if stem == "manuscript":
            wc = {"main": words(md), "main_tables": words(md, tables=True),
                  "all": words(md, "Abstract", "References", tables=True)}
            print("main text words (Introduction to Conclusion, no tables or captions):", wc["main"])
            print("main text words with tables and captions:", wc["main_tables"])
            print("words from the Abstract to the Statements, tables included (all but the references):", wc["all"])
            ab = re.search(r"^# Abstract\s*$(.*?)^# ", md, flags=re.S | re.M)
            print("abstract words:", len(ab.group(1).split()) if ab else 0)
            # counts for the title page, from the rendered manuscript
            nums["wc_main"] = {"value": wc["main"], "text": f"{wc['main']:,}"}
            nums["wc_main_tables"] = {"value": wc["main_tables"], "text": f"{wc['main_tables']:,}"}
            nums["wc_all"] = {"value": wc["all"], "text": f"{wc['all']:,}"}
            nums["wc_abstract"] = {"value": len(ab.group(1).split()) if ab else 0,
                                   "text": str(len(ab.group(1).split()) if ab else 0)}
            m = re.search(r"^title:\s*\"(.*)\"\s*$", open(path).read(), flags=re.M)
            nums["ms_title"] = {"value": m.group(1) if m else "", "text": m.group(1) if m else ""}
    # submission documents (cover letter, title page): same placeholders, written to manuscript/build/
    for stem in ("cover_letter", "title_page"):
        path = os.path.join(ROOT, f"manuscript/submission/{stem}.md")
        if not os.path.exists(path):
            continue
        md = render_text(open(path).read(), nums, design, "../../results/figures")
        out = os.path.join(ROOT, f"manuscript/build/{stem}.md")
        open(out, "w").write(md)
        subprocess.run(["pandoc", out, "-o", out[:-3] + ".docx"], check=True)
        print("wrote", out)


if __name__ == "__main__":
    sys.exit(main())
