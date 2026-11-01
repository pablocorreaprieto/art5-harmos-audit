"""Quantities written out in words in the ART 5 manuscript ("about two years", "within a year", "about
half") must agree with the numbers they summarise (finding m14 of the internal reading R2, 1.11.2026).

python checks/check_claims.py             check manuscript/build/manuscript.md
python checks/check_claims.py --plant     run on a copy of the numbers in which Claude Haiku 5.5's shift with
                                          the bare H label is changed from about two to about three years; must FAIL

checks/check_numbers.py traces every digit of the text to a named number, but not quantities written in
words. Here every such quantity found by QUANT in the rendered manuscript (Abstract to Statements) must
lie inside a span matched by one entry of CLAIMS, and each entry's condition must hold on
results/manuscript_numbers.json and the facts files read by manuscript/render.py. An entry whose pattern
no longer occurs in the text is also a failure, so the list cannot go stale.
Prints "PASS check_claims" or "FAIL check_claims" with the reasons.
Written by the main session (claude-opus-5-5) on 1.11.2026.
"""
import argparse
import copy
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "manuscript"))
import render  # noqa: E402

WORD = r"(?:a third|a quarter|half|one|two|three|four|five|six|seven|eight|nine|ten|a)"
QUANT = re.compile(
    r"\b(?:about |almost |nearly |more than |over |up to |at most |by |within )?(?:a third|a quarter|half) "
    r"(?:of (?:a |the |these)?)?(?:model-internal )?(?:years?|variance|these)?"
    rf"|\b(?:about |almost |nearly |more than |over |up to |at most |by |within )?{WORD} (?:model-internal )?(?:years?|times)\b",
    re.I)


def v(n, name):
    return float(n[name]["value"])


MODELS = ["anthropic_balanced", "anthropic_light", "openai_balanced", "openai_light", "mistral_balanced", "mistral_light"]

# (pattern in the rendered text, condition on the numbers, what the words claim)
CLAIMS = [
    # design and sources (definitions or facts read in the cited pages)
    (r"two years younger than the fifth year of primary school in France",
     lambda n: v(n, "src_men_age_from") + 4 - v(n, "age_5H_from") == 2,
     "5H (8-9) against the fifth class of the école élémentaire for a child starting CP at six (10-11)"),
    (r"would write for pupils two years older",
     lambda n: v(n, "src_men_age_from") + 4 - v(n, "age_5H_from") == 2, "same reading, fifth year from six"),
    (r"would miss by four years",
     lambda n: v(n, "src_men_age_to") + 1 - v(n, "age_5H_from") == 4,
     "5e, second year of collège after CM2 (ages 12-13) against 5H (8-9)"),
    (r"counted its school years from two years later than HarmoS",
     lambda n: True, "État de Vaud (2012): the 'sixième année actuelle' became 8H (8 - 6 = 2)"),
    (r"counting the school years two years later than HarmoS", lambda n: True, "same source"),
    (r"once they are four years old", lambda n: True, "HarmoS agreement, Art. 5 al. 1 (4 years completed)"),
    (r"primary degree lasts eight years", lambda n: True, "HarmoS agreement, Art. 6 al. 1"),
    (r"second of the four years of lower-secondary school", lambda n: True,
     "Ministère de l'Éducation nationale (2024b): 6e, 5e, 4e and 3e"),
    (r"about half had used ChatGPT, and a quarter of these",
     lambda n: 45 <= v(n, "src_avry_used_pct") <= 55 and 20 <= v(n, "src_avry_teaching_pct") <= 30,
     "Avry (2023): 52% had used ChatGPT, 24% of these in their teaching"),
    (r"about a third of the variance", lambda n: 0.28 <= v(n, "src_trott_r2") <= 0.38, "Trott & Rivière (2024): R2 = .36"),
    (r"neither repeated nor skipped a year", lambda n: True, "definition"),
    (r"widened by half a year", lambda n: True, "preregistered probe rule (question 8)"),
    (r"H and P notations, five times each", lambda n: v(n, "probe_repetitions") == 5, "design.json, probe_repetitions"),
    (r"about one year of age on the planning ruler",
     lambda n: abs(v(n, "sesoi_zipf") / 0.04 - 1) < 1e-9, "0.04 Zipf at the planning slope of -0.04 Zipf per year"),
    (r"a model-internal year is the change in that model's age-only texts from one year of age to the next",
     lambda n: True, "definition"),
    # results
    (r"one lighter model by about two years",
     lambda n: 1.75 <= v(n, "ae_L1_anthropic_light_shift") <= 2.25, "Claude Haiku 5.5, shift with the bare H label"),
    (r"the lighter model of one provider by about two years",
     lambda n: 1.75 <= v(n, "ae_L1_anthropic_light_shift") <= 2.25, "same (practitioner notes)"),
    (r"one by about two years on average",
     lambda n: 1.75 <= v(n, "ae_L1_anthropic_light_shift") <= 2.25, "same"),
    (r"the bare H label left one model two years off",
     lambda n: 1.75 <= v(n, "ae_L1_anthropic_light_shift") <= 2.25, "same"),
    (r"every model wrote within a year of its (?:own )?age-only texts",
     lambda n: max(abs(v(n, f"ae_L3_{m}_shift")) for m in MODELS) < 1, "per-model shifts with the label and the age (L3)"),
    (r"no model departed from its own age-only texts by more than a year on average",
     lambda n: max(abs(v(n, f"ae_L3_{m}_shift")) for m in MODELS) < 1, "same"),
    (r"texts within a year of the age \(shifts from",
     lambda n: max(abs(v(n, "ae_L1_probe_ok_shift_min")), abs(v(n, "ae_L1_probe_ok_shift_max"))) < 1,
     "shifts of the models whose probe answers were right"),
    (r"most often two years too old",
     lambda n: v(n, "ph_mr_two_L1") > v(n, "ph_mr_wrong_L1") / 2 and v(n, "ph_mr_two_L1P") > v(n, "ph_mr_wrong_L1P") / 2,
     "among the wrong stated ages of Mistral Large 4, those 1.5 to 2.5 years too old are the majority"),
    (r"stated an age two years too old were", lambda n: True, "definition of the group (1.5 to 2.5 years)"),
    (r"about half of what two years mean on the model's own ruler",
     lambda n: 0.40 <= v(n, "ph_mr_share_L1") <= 0.60, "difference as a share of twice the ruler slope"),
    (r"stated an age two years too old for the bare labels", lambda n: True, "same group"),
    (r"moved about half as far as that age implies", lambda n: 0.40 <= v(n, "ph_mr_share_L1") <= 0.60, "same"),
    (r"placed the grade about two years too old",
     lambda n: v(n, "probe_wrong_two_years_pct") > 0.5, "most wrong first answers were 1.5 to 2.5 years too old"),
    (r"a shift of about a third of a model-internal year",
     lambda n: 0.25 <= v(n, "ae_L1_shift") <= 0.42, "pooled shift with the bare H label"),
    (r"about half a model-internal year harder than the bare label",
     lambda n: 0.4 <= v(n, "ph_L2mL1_shift") <= 0.6, "shift difference L2 - L1"),
    (r"moved texts by more than five years", lambda n: v(n, "ae_L6_shift") > 5, "pooled shift of the collision control"),
]


def problems(md, nums):
    md = re.split(r"^# References\s*$", md, maxsplit=1, flags=re.M)[0]
    bad, covered = [], []
    for pat, cond, why in CLAIMS:
        found = list(re.finditer(pat, md))
        if not found:
            bad.append(f"claim not found in the text (remove or update it): {pat}")
            continue
        try:
            ok = bool(cond(nums))
        except KeyError as e:
            ok, why = False, f"{why} (missing number {e})"
        if not ok:
            bad.append(f"claim does not hold: '{pat}' ({why})")
        covered += [(m.start(), m.end()) for m in found]
    for m in QUANT.finditer(md):
        if not any(a <= m.start() and m.end() <= b for a, b in covered):
            a, b = max(0, m.start() - 50), m.end() + 30
            bad.append(f"quantity in words not covered by a claim: ...{md[a:b].strip()}...")
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plant", action="store_true")
    args = ap.parse_args()
    nums, _ = render.load(REPO)
    src = os.path.join(REPO, "manuscript", "source_facts.json")
    md = open(os.path.join(REPO, "manuscript", "build", "manuscript.md")).read()
    if args.plant:
        nums = copy.deepcopy(nums)
        nums["ae_L1_anthropic_light_shift"]["value"] = 3.1
    bad = problems(md, nums)
    for b in bad:
        print(b)
    print(("FAIL" if bad else "PASS") + " check_claims")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
