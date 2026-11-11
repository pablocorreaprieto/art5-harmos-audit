---
title: "Supporting Information"
---


# S1. Registration, departures and where each analysis is reported

**Registration and timing.** The preregistration was approved on AsPredicted on 1 November 2026 at about 08:52 (Zurich time); the deposited text is PREREG.md at the repository tag prereg (commit 6a0a061), whose status line, written before the deposit, still reads as it did then. The main data collection was run by the repository's workflow (run 41286684728) on the same commit, and its first call started at 08:55 (Zurich time), after the approval. The lexicon was the Lexique 3.83 file of lexique.org whose SHA-256 begins 637ba37a767a6667; a copy of the same version distributed in a Python package gives other values for the texts that contain *vrai* or *faux*, which it lists only in capitals.

**Secondary measures.** The eight preregistered secondary measures were the median Zipf frequency of content lemmas, the shares of content lemmas below Zipf 3 and below Zipf 4, mean word length, words per sentence, number of words, the Kandel–Moles adaptation of the Flesch readability formula to French (Kandel & Moles, 1958, as cited in Primpied et al., 2022) and the mean Zipf frequency of word forms in films (Table S2).

**Power simulation.** Besides the residual standard deviation and the age slope, the simulation that fixed the number of topics assumed a label-by-topic variation with a standard deviation of 0.02 Zipf, a prompt effect shared by the six models with a standard deviation of 0.05, heavy-tailed residuals and 2% missing texts (sim_power.py at tag prereg). The pilot held only age-only texts, so the first two values could not be estimated from it.

**Intervals.** All bootstrap intervals are 95% percentile intervals over topics with 2,000 resamples, as registered; with only 16 topics they may be somewhat narrow, and their limits move slightly with the resampling (for the tracking of the P label, see Results).

**Topics.** The 16 topics were the first 16 of a list of 32 fixed before the pilot; the preregistration treats them as random in the analysis, but they were not drawn at random. They were, in the order of the list: des animaux de la forêt; de l'eau; des saisons; de l'amitié à l'école; du corps humain; du métier de boulanger; des volcans; d'une fête de famille; des abeilles; d'un voyage en train; du jardin potager; des dinosaures; de la lune et des étoiles; des pompiers; de la neige en montagne; des oiseaux migrateurs. The pilot used six of them.

**Departures from the registration.** The preregistered analyses were run as registered, with two departures. First, the exploratory analysis by provider and model size listed in the registration was not reported in the first draft; it is now reported descriptively in Table S11 (one model per provider and tier, so no test). Second, the contrast of the P and H labels (Table S5) was computed by the registered analysis code but is not in the list of the registration text. The direction of the probe errors, the window of 1.5 to 2.5 years for errors of about two years, and the mention of an age or a grade in the texts were computed after the deposit by a separate script (exploratory.py).

**Post hoc analyses.** After internal readings of a draft, the following analyses were added and are labelled post hoc in the text (computed by the script exploratory_p7.py): the distance between the models' age-only texts at the same grade; the equivalence reading of the two level differences; the tests of differences between models; the reasoning reported by each model (Table S9); the primary contrasts without each model (Table S10); the spread of the six models' readings of each label (Table S11); the contrasts of the region and age wordings with the bare label (Table S5); the observed age offsets per grade; the precision of the P label's tracking interval; intervals for the default reader age (Table 3); counts of two Swiss words; checks of the probe rule; and the ages stated in the reasoning of Mistral Large 4 (Table S12). At the pre-submission audit, after three further reviews by separate AI sessions, the following were added: the primary contrasts with the content words absent from Lexique left out (script exploratory_audit.py, run on the official lexicon; Table S1); for the reasoning of Mistral Large 4, the 95% CI of the adjusted comparison with the topic-level *t* reference, and two results of the same script already in its output, the comparison run first, without grade and genre effects, and the slope on the stated error; the standardised mean differences of the primary tests (Table 2); and the translation of Zipf differences into percentages of geometric mean frequency. The per-model *t* statistics and linearity tests of the rulers, preregistered and computed by the registered analysis, were added to Table 3.

**Post hoc results given here only.** The models differed in the level and gradient of the H label differences (repeated-measures analyses of variance over topics, *F*(5, 75) = 29.42 and 15.17) and in the gradient of the P label differences (*F* = 9.47; all three *p* < .001), but not detectably in the level of the P label differences (*F* = 1.60, *p* = .169). The preregistered probe rule is strict in one way and lenient in another: 74 of the 177 wrong first answers stated a correct range later, and 49 of the 542 correct ones were accepted only through the half-year tolerance.

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
| Exploratory: per-model and per-grade contrasts, L2, L4 | Tables S3 to S6 |
| Exploratory: provider and model size | Table S11 |
| Exploratory: knowledge probes | Results, Table 3, Table S7 |
| Exploratory: refusals, clarification requests, flagged answers and removed lines by label | Below |
| Exploratory: explicit mention of an age or a grade in the texts | Table S8 |

No text was refused or asked for clarification, so the refusal and clarification rates are zero for every label. Of the 11 texts flagged as addressing the user, zero came from « de 5H » and one from « de 5P »; no preface or closing line was removed from any text.

# S2. Sensitivity analyses and secondary measures

Table S1. Primary contrasts under the preregistered sensitivity analyses and one post hoc analysis (levels in Zipf, gradients in Zipf per year). No text was an exact duplicate, so the duplicate rule removed nothing. Age equivalents read on an isotonic fit of each ruler, averaged over the six models: shift 0.19 years and tracking 0.94 for « de 5H », shift −0.05 and tracking 0.87 for « de 5P »; the linear readings averaged the same way give 0.21 and 0.94, and −0.01 and 0.91 (the main text pools the models as sums of levels over sums of slopes). Over all labels, grades and models, 135 cells were read inside the isotonic ruler, 59 extrapolated and 4 capped at 3 years beyond its ends; no intervals were computed for this reading.

| Analysis | H2-H level | H2-P level | H3-H gradient | H3-P gradient |
|---|---|---|---|---|
| Primary, topic-level *t*-tests | −0.012 (*p* = .002) | −0.001 (*p* = .865) | 0.0027 (*p* = .264) | 0.0040 (*p* = .068) |
| OLS, model × grade cells, errors clustered by topic | −0.012 (*p* = .002) | −0.001 (*p* = .866) | 0.0027 (*p* = .269) | 0.0040 (*p* = .070) |
| Truncated texts removed | −0.012 (*p* = .002) | −0.001 (*p* = .891) | 0.0027 (*p* = .264) | 0.0041 (*p* = .065) |
| Texts addressing the user removed | −0.012 (*p* = .002) | −0.001 (*p* = .866) | 0.0025 (*p* = .297) | 0.0040 (*p* = .073) |
| Length residualised within model | −0.017 (*p* < .001) | −0.008 (*p* = .077) | 0.0012 (*p* = .629) | 0.0040 (*p* = .077) |
| Words absent from Lexique left out (post hoc) | −0.014 (*p* < .001) | −0.003 (*p* = .433) | 0.0031 (*p* = .185) | 0.0043 (*p* = .041) |


Table S2. The primary contrasts on the eight preregistered secondary measures (label minus age only; gradients per year of age; one-sample *t*-tests over topics, no correction for multiplicity). Higher Kandel–Moles scores mean easier texts.

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

Table S3. Model-internal age equivalents by label, pooled and model by model (exploratory for single models), with 95% percentile intervals from 2,000 bootstrap resamples of topics. Models are listed by provider, the mid-priced model first; Table S11 summarises them by price tier. Readings of « de 5e » lie beyond the ages of the rulers and are linear extrapolations.

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


# S4. Secondary, exploratory and post hoc contrasts

Table S5. Secondary (L3), exploratory and post hoc contrasts, one-sample *t*-tests over topics, levels in Zipf and gradients in Zipf per year; no correction for multiplicity. The contrast of the P and H labels was computed by the preregistered analysis code but is not in the list of the registration text.

| Contrast | Estimate [95% CI] | *p* |
|---|---|---|
| « de 5H (8 à 9 ans) » − age only, level | 0.018 [0.011, 0.025] | < .001 |
| « de 5H (8 à 9 ans) » − age only, gradient | −0.0023 [−0.0059, 0.0013] | .190 |
| « de 5H (8 à 9 ans) » − « de 5H », level | 0.030 [0.025, 0.035] | < .001 |
| « de 5H (8 à 9 ans) » − « de 5H », gradient | −0.0050 [−0.0088, −0.0011] | .015 |
| « de 5H en Suisse romande » − age only, level | −0.034 [−0.047, −0.021] | < .001 |
| « de 5H en Suisse romande » − age only, gradient | 0.0010 [−0.0028, 0.0048] | .587 |
| « de 5H en Suisse romande » − « de 5H », level (post hoc) | −0.0224 [−0.0309, −0.0139] | < .001 |
| « de CE2 » − age only, level | 0.010 [0.002, 0.018] | .020 |
| « de CE2 » − age only, gradient | −0.0126 [−0.0169, −0.0083] | < .001 |
| « de 5P » − « de 5H », level (not in the registered list) | 0.011 [0.004, 0.018] | .003 |
| « de 5P » − « de 5H », gradient (not in the registered list) | 0.0013 [−0.0028, 0.0054] | .498 |
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


Table S10. The four primary contrasts without each model in turn (post hoc; topic-level *t*-tests as in the primary analysis, uncorrected *p*-values; levels in Zipf, gradients in Zipf per year).

| Model left out | H2-H level | H2-P level | H3-H gradient | H3-P gradient |
|---|---|---|---|---|
| None (primary) | −0.012 (*p* = .002) | −0.001 (*p* = .865) | 0.0027 (*p* = .264) | 0.0040 (*p* = .068) |
| Claude Sonnet 5.5 | −0.0164 (*p* < .001) | −0.0017 (*p* = .711) | 0.0048 (*p* = .095) | 0.0045 (*p* = .105) |
| Claude Haiku 5.5 | 0.0041 (*p* = .297) | 0.0032 (*p* = .525) | −0.0038 (*p* = .090) | 0.0018 (*p* = .460) |
| GPT-6.1 Sol | −0.0154 (*p* = .002) | 0.0006 (*p* = .912) | 0.0052 (*p* = .058) | 0.0048 (*p* = .029) |
| GPT-6 Luna | −0.0179 (*p* < .001) | −0.0022 (*p* = .623) | 0.0053 (*p* = .061) | 0.0069 (*p* = .009) |
| Mistral Large 4 | −0.0076 (*p* = .022) | −0.0021 (*p* = .624) | 0.0051 (*p* = .082) | 0.0071 (*p* = .007) |
| Mistral Small 4 | −0.0174 (*p* < .001) | −0.0022 (*p* = .627) | −0.0005 (*p* = .838) | −0.0008 (*p* = .672) |


Table S11. How far the six models' readings of each label spread (standard deviation across models of the per-model shift and tracking of Table S3), and, for the bare labels, the mean absolute departure of the three mid-priced and the three lighter models (the preregistered exploratory analysis by provider and model size; one model per cell, so descriptive only). Post hoc except the tier summary.

| Label | SD of the six shifts (years) | SD of the six trackings | Mean absolute shift, mid-priced / lighter (years) | Mean absolute tracking − 1, mid-priced / lighter |
|---|---|---|---|---|
| L1 « de 5H » | 1.07 | 0.50 | 0.39 / 1.13 | 0.20 / 0.60 |
| L1P « de 5P » | 0.28 | 0.45 | 0.13 / 0.31 | 0.11 / 0.54 |
| L2 « de 5H en Suisse romande » | 0.87 | 0.22 |  |  |
| L3 « de 5H (8 à 9 ans) » | 0.28 | 0.21 |  |  |
| L4 « de CE2 » | 0.42 | 0.26 |  |  |


# S5. Knowledge probes, mentions and reasoning

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


Table S9. Share of texts (%) for which the model reported reasoning or thinking tokens, by model and label, from the usage fields of the providers' answers, with reasoning left at each provider's default (post hoc).

| Model | L0 | L1 | L1P | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|---|---|
| Claude Sonnet 5.5 | 38 | 100 | 100 | 100 | 99 | 73 | 85 | 79 |
| Claude Haiku 5.5 | 0 | 65 | 57 | 92 | 62 | 1 | 1 | 2 |
| GPT-6.1 Sol | 94 | 100 | 100 | 100 | 99 | 95 | 87 | 100 |
| GPT-6 Luna | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| Mistral Large 4 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| Mistral Small 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |


Table S12. Age stated for the pupils in the visible reasoning of Mistral Large 4 before writing each text, by label (post hoc). First age range in the trace with a midpoint between 4 and 16 years; wrong by the preregistered probe rule; two years too old: midpoint 1.5 to 2.5 years above the true one. A random sample of 25 traces with the extracted age is in the repository.

| Label | Traces stating an age (%) | Age wrong (%) | Two years too old (%) | Mean error (years) |
|---|---|---|---|---|
| L1 « de 5H » | 100 | 51 | 38 | 1.30 |
| L1P « de 5P » | 100 | 42 | 40 | 0.95 |
| L2 « de 5H en Suisse romande » | 100 | 21 | 17 | 0.57 |
| L3 « de 5H (8 à 9 ans) » | 100 | 0 | 0 | 0.00 |
| L4 « de CE2 » | 100 | 0 | 0 | 0.00 |
| L5 age only | 100 | 0 | 0 | 0.00 |

