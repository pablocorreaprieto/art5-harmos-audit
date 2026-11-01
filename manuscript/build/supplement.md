---
title: "Supporting Information"
---


# S1. Where each preregistered analysis is reported

The preregistration (AsPredicted, link anonymised for review) listed four primary tests, a manipulation check, secondary analyses, sensitivity analyses, controls and exploratory analyses. All were run as registered, on all 7,680 texts, since none was excluded. The table below gives where each is reported. The two exploratory analyses that the preregistered code did not compute (the direction of the probe errors and the mention of an age or a grade in the texts) were computed after the deposit by a separate script (exploratory.py in the repository) and are labelled as such.

| Preregistered analysis | Where |
|---|---|
| H2-H, H2-P, H3-H, H3-P (primary) | Results, Table 2 |
| H1, slope of each age-only ruler, and its linearity | Results, Figure 1, Table 3 |
| Model-internal age equivalents (shift, tracking) | Results, Figures 2 and 3, Table S3 |
| L3 against L5 and against L1 (secondary) | Results, Table S5 |
| Primary contrasts by OLS with errors clustered by topic (secondary) | Table S1 |
| Primary contrasts on eight secondary measures | Table S2 |
| Sensitivity: length residualised, truncated, duplicated and flagged texts removed, isotonic reading | Table S1 |
| Controls: L6 against L5 at 3H to 5H, L0 on each ruler | Results, Table 3, Table S5 |
| Exploratory: per-model and per-grade contrasts, L2, L4, H against P | Tables S3 to S6 |
| Exploratory: knowledge probes | Results, Table 3, Table S7 |
| Exploratory: refusals, clarification requests, flagged answers and removed lines by label | Below |
| Exploratory: explicit mention of an age or a grade in the texts | Table S8 |

No text was refused or asked for clarification, so the refusal and clarification rates are zero for every label. Of the 11 texts flagged as addressing the user, zero came from « de 5H » and one from « de 5P »; no preface or closing line was removed from any text.

# S2. Sensitivity analyses and secondary measures

Table S1. Primary contrasts under the preregistered sensitivity analyses (levels in Zipf, gradients in Zipf per year). Age equivalents read on an isotonic fit of each ruler: shift 0.19 years and tracking 0.94 for « de 5H », shift −0.05 and tracking 0.87 for « de 5P » (135 cells read inside the ruler, 59 extrapolated, 4 capped at 3 years beyond its ends).

| Analysis | H2-H level | H2-P level | H3-H gradient | H3-P gradient |
|---|---|---|---|---|
| Primary, topic-level *t*-tests | −0.012 (*p* = .002) | −0.001 (*p* = .865) | 0.0027 (*p* = .264) | 0.0040 (*p* = .068) |
| OLS, model × grade cells, errors clustered by topic | −0.012 (*p* = .002) | −0.001 (*p* = .866) | 0.0027 (*p* = .269) | 0.0040 (*p* = .070) |
| Truncated texts removed | −0.012 (*p* = .002) | −0.001 (*p* = .891) | 0.0027 (*p* = .264) | 0.0041 (*p* = .065) |
| Exact duplicates removed | −0.012 (*p* = .002) | −0.001 (*p* = .865) | 0.0027 (*p* = .264) | 0.0040 (*p* = .068) |
| Texts addressing the user removed | −0.012 (*p* = .002) | −0.001 (*p* = .866) | 0.0025 (*p* = .297) | 0.0040 (*p* = .073) |
| Length residualised within model | −0.017 (*p* < .001) | −0.008 (*p* = .077) | 0.0012 (*p* = .629) | 0.0040 (*p* = .077) |


Table S2. The primary contrasts on the eight preregistered secondary measures (label minus age only; gradients per year of age). Higher Kandel–Moles scores mean easier texts.

| Measure | H2-H level | H2-P level | H3-H gradient | H3-P gradient |
|---|---|---|---|---|
| Median Zipf, content lemmas | −0.010 (*p* = .019) | −0.001 (*p* = .780) | 0.0028 (*p* = .295) | 0.0029 (*p* = .226) |
| Content lemmas below Zipf 3 (percentage points) | 0.00 (*p* = .974) | −0.01 (*p* = .867) | −0.029 (*p* = .282) | −0.051 (*p* = .075) |
| Content lemmas below Zipf 4 (percentage points) | 0.21 (*p* = .046) | −0.06 (*p* = .627) | −0.098 (*p* = .144) | −0.134 (*p* = .070) |
| Mean word length (letters) | 0.021 (*p* < .001) | 0.002 (*p* = .632) | −0.0008 (*p* = .821) | −0.0029 (*p* = .297) |
| Words per sentence | 0.05 (*p* = .294) | −0.12 (*p* = .012) | −0.055 (*p* = .120) | −0.007 (*p* = .865) |
| Number of words | −35.2 (*p* < .001) | −35.1 (*p* < .001) | −5.09 (*p* = .013) | −1.73 (*p* = .354) |
| Kandel–Moles readability | −0.39 (*p* = .004) | 0.30 (*p* = .009) | −0.018 (*p* = .852) | −0.033 (*p* = .650) |
| Mean Zipf, word forms in films | −0.001 (*p* = .636) | 0.012 (*p* = .020) | −0.0032 (*p* = .191) | −0.0039 (*p* = .137) |


# S3. Age equivalents and contrasts by model

Table S3. Model-internal age equivalents by label, pooled and model by model (exploratory for single models), with 95% percentile intervals from 2,000 bootstrap resamples of topics.

| Label | Model | Shift, years [95% CI] | Tracking [95% CI] |
|---|---|---|---|
| L1 « de 5H » | All six | 0.30 [0.13, 0.46] | 0.93 [0.82, 1.05] |
| | Claude Sonnet 5.5 | −0.25 [−0.46, −0.04] | 1.17 [0.96, 1.41] |
| | Claude Haiku 5.5 | 2.12 [1.75, 2.56] | 0.18 [−0.02, 0.41] |
| | GPT-6.1 Sol | −0.13 [−0.40, 0.13] | 1.20 [1.03, 1.41] |
| | GPT-6 Luna | −0.77 [−1.48, −0.22] | 1.42 [1.10, 2.01] |
| | Mistral Large 4 | 0.79 [0.33, 1.41] | 1.23 [0.98, 1.64] |
| | Mistral Small 4 | −0.49 [−0.94, 0.03] | 0.46 [0.22, 0.71] |
| L1P « de 5P » | All six | 0.02 [−0.21, 0.21] | 0.90 [0.81, 0.99] |
| | Claude Sonnet 5.5 | −0.09 [−0.44, 0.26] | 0.96 [0.79, 1.14] |
| | Claude Haiku 5.5 | 0.48 [0.06, 0.86] | 0.64 [0.47, 0.83] |
| | GPT-6.1 Sol | 0.15 [−0.07, 0.38] | 0.99 [0.81, 1.19] |
| | GPT-6 Luna | −0.27 [−1.15, 0.47] | 1.43 [1.11, 2.06] |
| | Mistral Large 4 | −0.15 [−0.66, 0.33] | 1.27 [0.95, 1.77] |
| | Mistral Small 4 | −0.19 [−0.75, 0.37] | 0.16 [−0.05, 0.35] |
| L2 « de 5H en Suisse romande » | All six | 0.87 [0.54, 1.23] | 0.97 [0.89, 1.07] |
| | Claude Sonnet 5.5 | 0.64 [0.22, 1.16] | 1.03 [0.86, 1.20] |
| | Claude Haiku 5.5 | 2.04 [1.63, 2.55] | 0.70 [0.54, 0.92] |
| | GPT-6.1 Sol | −0.04 [−0.25, 0.16] | 1.17 [0.99, 1.39] |
| | GPT-6 Luna | −0.11 [−0.85, 0.71] | 1.14 [0.83, 1.64] |
| | Mistral Large 4 | 1.64 [1.01, 2.72] | 1.12 [0.91, 1.46] |
| | Mistral Small 4 | 0.76 [0.01, 1.70] | 0.68 [0.48, 0.92] |
| L3 « de 5H (8 à 9 ans) » | All six | −0.46 [−0.62, −0.33] | 1.06 [0.98, 1.16] |
| | Claude Sonnet 5.5 | −0.48 [−0.81, −0.16] | 0.88 [0.73, 1.08] |
| | Claude Haiku 5.5 | −0.11 [−0.47, 0.29] | 0.75 [0.58, 0.96] |
| | GPT-6.1 Sol | −0.34 [−0.55, −0.15] | 1.18 [1.04, 1.36] |
| | GPT-6 Luna | −0.61 [−1.45, 0.01] | 1.24 [0.93, 1.73] |
| | Mistral Large 4 | −0.46 [−1.01, −0.01] | 1.30 [0.97, 1.83] |
| | Mistral Small 4 | −0.96 [−1.55, −0.38] | 1.07 [0.85, 1.34] |
| L4 « de CE2 » | All six | −0.26 [−0.45, −0.08] | 1.32 [1.22, 1.45] |
| | Claude Sonnet 5.5 | −0.31 [−0.59, −0.07] | 1.35 [1.16, 1.59] |
| | Claude Haiku 5.5 | 0.30 [−0.09, 0.69] | 0.88 [0.65, 1.11] |
| | GPT-6.1 Sol | −0.54 [−0.87, −0.28] | 1.59 [1.39, 1.85] |
| | GPT-6 Luna | −0.94 [−1.73, −0.39] | 1.50 [1.10, 2.17] |
| | Mistral Large 4 | −0.15 [−0.66, 0.34] | 1.45 [1.12, 1.95] |
| | Mistral Small 4 | −0.11 [−0.62, 0.51] | 1.17 [0.87, 1.56] |
| L6 « de 5e » (3H to 5H) | All six | 5.62 [5.31, 5.99] | −0.92 [−1.26, −0.62] |
| | Claude Sonnet 5.5 | 5.23 [4.65, 5.87] | −0.45 [−0.89, −0.05] |
| | Claude Haiku 5.5 | 5.32 [4.81, 5.99] | −0.27 [−0.69, 0.12] |
| | GPT-6.1 Sol | 4.56 [4.15, 5.08] | −0.66 [−1.04, −0.31] |
| | GPT-6 Luna | 4.89 [3.70, 6.76] | −1.41 [−2.56, −0.59] |
| | Mistral Large 4 | 7.84 [6.81, 9.62] | −1.51 [−2.85, −0.59] |
| | Mistral Small 4 | 5.85 [4.88, 7.38] | −1.63 [−2.69, −0.71] |


Table S4. The primary contrasts model by model (exploratory), with 95% confidence intervals over topics; levels in Zipf, gradients in Zipf per year.

| Model | H2-H level | H2-P level | H3-H gradient | H3-P gradient |
|---|---|---|---|---|
| Claude Sonnet 5.5 | 0.011 [0.000, 0.022] | 0.004 [−0.013, 0.022] | −0.0077 [−0.0180, 0.0026] | 0.0019 [−0.0066, 0.0104] |
| Claude Haiku 5.5 | −0.091 [−0.111, −0.071] | −0.020 [−0.040, 0.000] | 0.0351 [0.0215, 0.0488] | 0.0154 [0.0052, 0.0256] |
| GPT-6.1 Sol | 0.006 [−0.008, 0.020] | −0.008 [−0.020, 0.005] | −0.0098 [−0.0188, −0.0008] | 0.0003 [−0.0098, 0.0104] |
| GPT-6 Luna | 0.019 [0.004, 0.033] | 0.007 [−0.014, 0.027] | −0.0104 [−0.0193, −0.0016] | −0.0105 [−0.0196, −0.0013] |
| Mistral Large 4 | −0.033 [−0.052, −0.013] | 0.006 [−0.017, 0.029] | −0.0095 [−0.0217, 0.0027] | −0.0112 [−0.0269, 0.0044] |
| Mistral Small 4 | 0.017 [−0.003, 0.036] | 0.006 [−0.015, 0.027] | 0.0184 [0.0078, 0.0290] | 0.0283 [0.0197, 0.0369] |


# S4. Secondary and exploratory contrasts

Table S5. Secondary (L3) and exploratory contrasts, one-sample *t*-tests over topics, levels in Zipf and gradients in Zipf per year; no correction for multiplicity.

| Contrast | Estimate [95% CI] | *p* |
|---|---|---|
| « de 5H (8 à 9 ans) » − age only, level | 0.018 [0.011, 0.025] | < .001 |
| « de 5H (8 à 9 ans) » − age only, gradient | −0.0023 [−0.0059, 0.0013] | .190 |
| « de 5H (8 à 9 ans) » − « de 5H », level | 0.030 [0.025, 0.035] | < .001 |
| « de 5H (8 à 9 ans) » − « de 5H », gradient | −0.0050 [−0.0088, −0.0011] | .015 |
| « de 5H en Suisse romande » − age only, level | −0.034 [−0.047, −0.021] | < .001 |
| « de 5H en Suisse romande » − age only, gradient | 0.0010 [−0.0028, 0.0048] | .587 |
| « de CE2 » − age only, level | 0.010 [0.002, 0.018] | .020 |
| « de CE2 » − age only, gradient | −0.0126 [−0.0169, −0.0083] | < .001 |
| « de 5P » − « de 5H », level | 0.011 [0.004, 0.018] | .003 |
| « de 5P » − « de 5H », gradient | 0.0013 [−0.0028, 0.0054] | .498 |
| « de 5e » − age only, level at 3H to 5H | −0.221 [−0.252, −0.191] | < .001 |


Table S6. Level differences grade by grade (exploratory; in the second column the label is « de {n}P » for each grade), in Zipf, with 95% confidence intervals over topics.

| Grade | « de 5H » − age | « de 5P » − age | « de 5H (8 à 9 ans) » − age |
|---|---|---|---|
| 3H | −0.030 [−0.052, −0.008] | −0.008 [−0.027, 0.010] | 0.019 [0.003, 0.035] |
| 4H | −0.006 [−0.021, 0.009] | −0.004 [−0.026, 0.018] | 0.031 [0.012, 0.051] |
| 5H | −0.008 [−0.021, 0.004] | 0.000 [−0.021, 0.020] | 0.017 [−0.004, 0.037] |
| 6H | −0.008 [−0.022, 0.005] | −0.015 [−0.028, −0.002] | 0.011 [−0.004, 0.027] |
| 7H | −0.006 [−0.020, 0.008] | 0.009 [−0.006, 0.024] | 0.018 [0.000, 0.036] |
| 8H | −0.011 [−0.027, 0.005] | 0.015 [−0.003, 0.033] | 0.012 [−0.004, 0.028] |


# S5. Knowledge probes and mentions

Table S7. Knowledge probes (60 per model and notation; 99.9% of answers stated an age range, 77% more than one). Too old or too young: midpoint of the first range outside the true range widened by half a year.

| Model | Notation | First range correct (%) | Any range correct (%) | Too old (%) | Too young (%) | Mean error (years) |
|---|---|---|---|---|---|---|
| Claude Sonnet 5.5 | H | 100 | 100 | 0 | 0 | −0.14 |
| Claude Sonnet 5.5 | P | 98 | 100 | 0 | 2 | −0.13 |
| Claude Haiku 5.5 | H | 65 | 67 | 32 | 3 | 1.62 |
| Claude Haiku 5.5 | P | 58 | 63 | 42 | 0 | 1.04 |
| GPT-6.1 Sol | H | 100 | 100 | 0 | 0 | 0.00 |
| GPT-6.1 Sol | P | 100 | 100 | 0 | 0 | 0.00 |
| GPT-6 Luna | H | 100 | 100 | 0 | 0 | 0.00 |
| GPT-6 Luna | P | 95 | 95 | 5 | 0 | 0.10 |
| Mistral Large 4 | H | 62 | 77 | 38 | 0 | 0.79 |
| Mistral Large 4 | P | 55 | 85 | 42 | 2 | 0.68 |
| Mistral Small 4 | H | 37 | 67 | 57 | 7 | 0.97 |
| Mistral Small 4 | P | 33 | 73 | 63 | 3 | 1.21 |


Table S8. Texts whose body (title excluded) names an age (« huit ans », « 8 ans ») or a school grade (« 5H », « CE2 », « 5e »), by label (exploratory; a story character's age counts as a mention).

| Label | Texts naming an age (%) | Texts naming a grade (%) |
|---|---|---|
| L0 | 15 | 1 |
| L1 | 12 | 3 |
| L1P | 13 | 4 |
| L2 | 14 | 11 |
| L3 | 14 | 3 |
| L4 | 12 | 4 |
| L5 | 18 | 2 |
| L6 | 24 | 4 |

