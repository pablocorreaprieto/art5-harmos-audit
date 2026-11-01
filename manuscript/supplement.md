---
title: "Supporting Information"
---

<!-- Source of the supporting information of the ART 5 manuscript, rendered by manuscript/render.py.
Every number is a {{name}} placeholder of results/manuscript_numbers.json. -->

# S1. Where each preregistered analysis is reported

The preregistration (AsPredicted, link anonymised for review) listed four primary tests, a manipulation check, secondary analyses, sensitivity analyses, controls and exploratory analyses. All were run as registered, on all {{n_texts}} texts, since none was excluded. The table below gives where each is reported. The two exploratory analyses that the preregistered code did not compute (the direction of the probe errors and the mention of an age or a grade in the texts) were computed after the deposit by a separate script (exploratory.py in the repository) and are labelled as such.

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

No text was refused or asked for clarification, so the refusal and clarification rates are zero for every label. Of the {{n_flag_meta}} texts flagged as addressing the user, {{n_flag_L1_word}} came from « de 5H » and {{n_flag_L1P_word}} from « de 5P »; no preface or closing line was removed from any text.

# S2. Sensitivity analyses and secondary measures

{{table:s1}}

{{table:s2}}

# S3. Age equivalents and contrasts by model

{{table:s3}}

{{table:s4}}

# S4. Secondary and exploratory contrasts

{{table:s5}}

{{table:s6}}

# S5. Knowledge probes and mentions

{{table:s7}}

{{table:s8}}
