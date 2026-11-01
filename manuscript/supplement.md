---
title: "Supporting Information"
---

<!-- Source of the supporting information of the ART 5 manuscript, rendered by manuscript/render.py.
Every number is a {{name}} placeholder of results/manuscript_numbers.json or of the facts files. -->

# S1. Registration, departures and where each analysis is reported

**Registration and timing.** The preregistration was approved on AsPredicted on {{proc_deposit_day}} at {{proc_deposit_time}} (Zurich time); the deposited text is PREREG.md at the repository tag prereg (commit {{proc_prereg_commit}}), whose status line, written before the deposit, still reads as it did then. The main data collection was run by the repository's workflow (run {{proc_run_id}}) on the same commit, and its first call started at {{collection_start_zurich}} (Zurich time), after the approval. The lexicon was the Lexique {{lexique_version}} file of lexique.org whose SHA-256 begins {{lexique_sha16}}; a copy of the same version distributed in a Python package gives other values for the texts that contain *vrai* or *faux*, which it lists only in capitals.

**Secondary measures.** The eight preregistered secondary measures were the median Zipf frequency of content lemmas, the shares of content lemmas below Zipf 3 and below Zipf 4, mean word length, words per sentence, number of words, the Kandel–Moles adaptation of the Flesch readability formula to French (Kandel & Moles, 1958, as cited in Primpied et al., 2022) and the mean Zipf frequency of word forms in films (Table S2).

**Power simulation.** Besides the residual standard deviation and the age slope, the simulation that fixed the number of topics assumed a label-by-topic variation with a standard deviation of {{pow_tau_label_topic}} Zipf, a prompt effect shared by the six models with a standard deviation of {{pow_tau_prompt}}, heavy-tailed residuals and {{pow_missing_pct}}% missing texts (sim_power.py at tag prereg). The pilot held only age-only texts, so the first two values could not be estimated from it.

**Intervals.** All bootstrap intervals are 95% percentile intervals over topics with {{bootstrap_resamples}} resamples, as registered; with only {{n_topics}} topics they may be somewhat narrow, and their limits move slightly with the resampling (for the tracking of the P label, see Results).

**Topics.** The {{n_topics}} topics were the first {{n_topics}} of a list of {{n_topics_listed}} fixed before the pilot; the preregistration treats them as random in the analysis, but they were not drawn at random.

**Departures from the registration.** The preregistered analyses were run as registered, with two departures. First, the exploratory analysis by provider and model size listed in the registration was not reported in the first draft; it is now reported descriptively in Table S11 (one model per provider and tier, so no test). Second, the contrast of the P and H labels (Table S5) was computed by the registered analysis code but is not in the list of the registration text. The direction of the probe errors, the window of {{probe_window_lo}} to {{probe_window_hi}} years for errors of about two years, and the mention of an age or a grade in the texts were computed after the deposit by a separate script (exploratory.py).

**Post hoc analyses.** After internal readings of a draft, the following analyses were added and are labelled post hoc in the text (computed by the script exploratory_p7.py): the distance between the models' age-only texts at the same grade; the equivalence reading of the two level differences; the tests of differences between models; the reasoning reported by each model (Table S9); the primary contrasts without each model (Table S10); the spread of the six models' readings of each label (Table S11); the contrasts of the region and age wordings with the bare label (Table S5); the observed age offsets per grade; the precision of the P label's tracking interval; intervals for the default reader age (Table 3); counts of two Swiss words; checks of the probe rule; and the ages stated in the reasoning of {{name_mistral_balanced}} (Table S12).

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

No text was refused or asked for clarification, so the refusal and clarification rates are zero for every label. Of the {{n_flag_meta}} texts flagged as addressing the user, {{n_flag_L1_word}} came from « de 5H » and {{n_flag_L1P_word}} from « de 5P »; no preface or closing line was removed from any text.

# S2. Sensitivity analyses and secondary measures

{{table:s1}}

{{table:s2}}

# S3. Age equivalents and contrasts by model

{{table:s3}}

{{table:s4}}

# S4. Secondary, exploratory and post hoc contrasts

{{table:s5}}

{{table:s6}}

{{table:s10}}

{{table:s11}}

# S5. Knowledge probes, mentions and reasoning

{{table:s7}}

{{table:s8}}

{{table:s9}}

{{table:s12}}
