---
title: "TITLE TO WRITE LAST"
---


# Abstract

ABSTRACT TO WRITE LAST

# Practitioner notes

PRACTITIONER NOTES TO WRITE LAST

# Introduction

INTRODUCTION TO WRITE FROM THE LITERATURE NOTES

# Background

BACKGROUND TO WRITE FROM THE LITERATURE NOTES

# Method

## Design and preregistration

The study is an audit experiment in which the data are texts written by language models under controlled prompts; no person took part. The hypotheses, the measure, the exclusion rules, the sample size and the analyses were preregistered on AsPredicted before the confirmatory data were collected (link anonymised for review). A pilot of 252 calls to three of the models, run the day before, requested texts with the pupils' age only and served to estimate the variance and the age slope of the measure; its texts are excluded from every confirmatory analysis. The prompts, the call plan, the code, the raw outputs and the results are archived in a repository whose states at registration and at data freeze are tagged (link anonymised for review).

## Prompts and conditions

Each prompt asked in French for a reading text on a topic, for pupils of a given level: « Écris {une histoire à lire | un texte documentaire à lire} pour des élèves{label}, sur le thème {topic}. Réponds seulement avec un titre et le texte. » ("Write {a story to read | an informational text to read} for pupils{label}, on the topic {topic}. Answer only with a title and the text.") The label named the readers' level in one of eight ways (Table 1). The bare HarmoS label (L1, « de 5H ») and the bare P label (L1P, « de 5P ») are the two forms a teacher in French-speaking Switzerland is most likely to type. The age-only label (L5, « de 8 à 9 ans ») is the reference: it tells the model what the Swiss label means, so a model that understands the label should write the same kind of text under both. L2 adds the region, L3 adds the age to the H label, and L4 uses the French grade that covers the same ages. L6 is a collision control: the same digit with the suffix of the French lower-secondary grades (« de 5e »), which in France names the second year of lower-secondary school (CITE French system); it was run at 3H to 5H only, because « de 6e » is the L4 prompt of 8H. L0 gives no level and shows each model's default reader.

Table 1. The eight labels, with the wording each gives for grade 5H (pupils aged 8 to 9). The label follows « pour des élèves » in the prompt.

| Code | Wording for 5H | Role | Grades |
|---|---|---|---|
| L1 | « de 5H » | bare HarmoS label | 3H to 8H |
| L1P | « de 5P » | bare P label (Vaud, Geneva) | 3H to 8H |
| L2 | « de 5H en Suisse romande » | H label and region | 3H to 8H |
| L3 | « de 5H (8 à 9 ans) » | H label and age | 3H to 8H |
| L4 | « de CE2 » | French grade | 3H to 8H |
| L5 | « de 8 à 9 ans » | age only (reference) | 3H to 8H |
| L6 | « de 5e » | same digit, French lower-secondary suffix (collision control) | 3H to 5H |
| L0 | (none) | no level (baseline) | one text per model, genre and topic |


The labels were crossed with the six grades of the primary cycle after kindergarten (3H to 8H, pupils aged 6 to 7 up to 11 to 12), two genres (a story and an informational text) and 16 fixed topics, from bees and volcanoes to a train journey and a family celebration. Each model thus wrote 480 texts per topic, 7,680 texts in all. Each prompt was sent once, as an independent call without system prompt or conversation history, in a random order (seed 20261025), with temperature 1.0 and at most 4,000 output tokens; reasoning settings were left at each provider's default.

## Models

We audited six models, two from each of three providers: a mid-tier model and a lighter, cheaper model, as the providers' price lists placed them at the time of the study: Claude Sonnet 5.5 (claude-sonnet-5-5) and Claude Haiku 5.5 (claude-haiku-5-5) from Anthropic, GPT-6.1 Sol (gpt-6.1-sol) and GPT-6 Luna (gpt-6-luna) from OpenAI, and Mistral Large 4 (mistral-large-4-0) and Mistral Small 4 (mistral-small-2603) from Mistral AI. The identifiers are those returned by the APIs, which matched the identifiers requested for every call. All calls were made on 1 November 2026. Every model accepted the requested temperature.

## Knowledge probes

To separate what a model can state about the labels from how it writes, each model also answered 60 knowledge questions per notation, 720 in all: « À quel âge correspondent des élèves de 5H ? » ("What age are pupils in 5H?") and the same question opened by « En Suisse romande, » ("In French-speaking Switzerland,"), for the six grades in the H and P notations, five times each. As preregistered, the first age range stated in an answer counts, and it is correct if its midpoint lies within the true range widened by half a year on each side.

## Measure

The dependent variable is the mean Zipf frequency of the content lemmas of a text, a measure of lexical demand: texts for younger readers use more frequent words, which score higher. Each word form was read as its most frequent lemma in Lexique 3.83 (CITE New et al., 2004), and content words were the forms read as nouns, qualifying adjectives or verbs, without the lemmas *être* and *avoir*, the indefinites *tout*, *autre* and *même*, and proper names. A lemma's frequency is the mean of its frequencies per million words in the film-subtitle and book corpora of Lexique (CITE New et al., 2007), on the Zipf scale (CITE van Heuven et al., 2014) computed as log10(f + 0.031) + 3, so that a lemma absent from Lexique counts as frequency zero. Titles, markdown marks and lines addressed to the user rather than to the pupils (prefaces such as « Voici une histoire… » and closings such as « N'hésitez pas… ») were removed before measurement; no such line was found in the confirmatory texts (0 lines removed). The exact rules, with the test texts that pin them, are in the repository.

The measure passed two checks of validity. Before the pilot, it was run on the articles of the French Wikipedia and of Vikidia, an encyclopedia written for children, on the same 30 subjects; the preregistered criterion was met, with Vikidia scoring higher in 28 of the 29 usable pairs (sign test, one-sided *p* < .001; mean difference 0.34 Zipf). In the confirmatory data, the age-only texts of every model served as a manipulation check (H1, below). Eight secondary measures were preregistered: the median Zipf frequency of content lemmas, the shares of content lemmas below Zipf 3 and below Zipf 4, mean word length, words per sentence, number of words, the Kandel–Moles readability formula for French (CITE) and the mean Zipf frequency of word forms in films.

## Exclusions

A call that failed or returned nothing was requested once more. A text that refused the task or asked for clarification, had fewer than 20 words, or had more than 50% of its word tokens absent from Lexique was requested once more, and excluded if the second answer failed the same rule. Truncated texts, exact duplicates and answers that addressed the user outside the story were kept, flagged and removed in sensitivity analyses. No exclusion rule used the value of any frequency measure.

## Analysis

Texts were paired on model, grade, genre and topic. For topic *t* and grade *g*, *d*(*g*, *t*) is the mean over models and genres of the difference between a label's text and the age-only text. The level of a topic is the mean of *d* over the six grades, and its gradient is the least-squares slope of *d* on the midpoint of the grade's age range. A label read as an older grade gives a negative level (rarer words), and a label that the model ignores, writing at the same level whatever the grade, gives a positive gradient: too hard for the youngest pupils and too easy for the oldest. The four primary tests are two-sided one-sample *t*-tests over topics (df = 15) of the level of L1 minus L5 (H2-H) and of L1P minus L5 (H2-P), and of the gradient of L1 minus L5 (H3-H) and of L1P minus L5 (H3-P), with Holm's correction over the four tests (CITE Holm, 1979) and α = .05. Topics are the unit of inference because the texts of a topic share content that a text-level test would treat as independent; inference is conditional on these six models and this prompt wording.

The smallest effect of interest was a level difference of 0.04 Zipf, about one year of age on the planning ruler. With the pilot's residual standard deviation taken at its upper 80% confidence bound (0.122), 16 topics gave a simulated power of .835 for the H2-H level test at that difference, which fixed the number of topics before the deposit.

The manipulation check H1 asked whether, with the age only, each model's texts get rarer words as the requested age rises: per model, an ordinary least-squares regression of the measure on the age midpoint within L5, with genre and topic effects, standard errors clustered by topic and a one-sided *t*-test with 15 df.

To express effects in years, each model is read on its own age-only ruler, the least-squares line through its six L5 means, with slope *b*. For a label, the shift is the sum over models of the levels divided by the sum of the slopes, in years (positive values mean texts written as for older pupils), and the tracking is 1 plus the sum of the gradients divided by the sum of the slopes (1 means that the texts follow the grade as the age-only texts do, 0 that they ignore it). Only models with a ruler slope of at most −0.02 Zipf per year are read, a rule that all six models met. Intervals are 95% percentile intervals from 2,000 bootstrap resamples of topics. Per-model shifts and tracking, the per-grade profiles, L2 and L4, and the knowledge probes are exploratory. The preregistered secondary and sensitivity analyses are reported in the Supporting Information: the primary contrasts by ordinary least squares with model-by-grade cells and standard errors clustered by topic, on each secondary measure, with length residualised within model, without the flagged texts, and with age equivalents read on an isotonic fit of each ruler.

# Results

## Data

All 8,400 calls were answered: four probe calls to Mistral Large 4, which spent the whole output limit on reasoning and returned no text at the first pass, were answered at the second. None of the 7,680 texts was refused, too short or out of lexicon, so all were analysed; five were truncated, 11 were flagged as addressing the user and none was an exact duplicate. Texts had a mean length of 405 words (median 369), from 330 words on average for GPT-6 Luna to 594 for Claude Sonnet 5.5. The study cost 41.12 USD in API calls.

## Every model lowered word frequency with age

The manipulation check succeeded for all six models. With the age only, the mean Zipf frequency of content lemmas fell as the requested age rose, with slopes from −0.025 Zipf per year for GPT-6 Luna to −0.049 for GPT-6.1 Sol (all one-sided *p* < .001; Figure 1), and no ruler departed from a straight line (linearity tests, smallest *p* = .205). On these rulers, a difference of 0.04 Zipf is roughly one year of age.

![Figure 1. Age-only rulers. Mean Zipf frequency of the content lemmas of the texts requested with the age only, by grade of the age requested, for the larger (circles) and smaller (squares) model of each provider. Bands are 95% confidence intervals over 16 topics. Higher values mean more frequent words.](../../results/figures/fig1_rulers.png)


## Bare labels: almost the age, on average

Table 2 gives the four primary tests. Texts requested with the bare HarmoS label used slightly rarer words than texts requested with the matching age (H2-H: −0.012 Zipf, 95% CI [−0.018, −0.005], *t*(15) = −3.72, *p* = .002, Holm-corrected *p* = .008). The difference is real but small: read on the models' own rulers, the « de 5H » texts were written as for pupils 0.30 years older (95% CI [0.13, 0.46]), and its confidence interval excludes the smallest effect of interest. The bare P label showed no difference (H2-P: −0.001 Zipf [−0.010, 0.009], *p* = .865); its interval excludes differences as large as the smallest effect of interest in either direction, and its shift was 0.02 years [−0.21, 0.21].

Neither label changed how texts followed the grade. The gradients of the differences were small and not significant (H3-H: 0.0027 Zipf per year [−0.0023, 0.0076], Holm *p* = .529; H3-P: 0.0040 [−0.0003, 0.0084], Holm *p* = .203). In years, the tracking of the H label was 0.93 [0.82, 1.05] and that of the P label 0.90 [0.81, 0.99]: from 3H to 8H, the P texts moved through about nine tenths of the age span that the age-only texts covered. The bootstrap interval of the P label's tracking stops just below 1 while its preregistered gradient test did not reject, so the evidence of under-tracking is weak.

Table 2. Primary tests. Levels in Zipf, gradients in Zipf per year of age; one-sample *t*-tests over 16 topics, Holm correction over the four tests. Shift: years older than the age requested; tracking: 1 = follows the grade like the age-only texts, 0 = ignores it.

| Test | Contrast | Estimate [95% CI] | *t*(15) | *p* | Holm *p* | In years [95% CI] |
|---|---|---|---|---|---|---|
| H2-H | Level, « de 5H » − age | −0.012 [−0.018, −0.005] | −3.72 | .002 | .008 | shift 0.30 [0.13, 0.46] |
| H2-P | Level, « de 5P » − age | −0.001 [−0.010, 0.009] | −0.17 | .865 | .865 | shift 0.02 [−0.21, 0.21] |
| H3-H | Gradient, « de 5H » − age | 0.0027 [−0.0023, 0.0076] | 1.16 | .264 | .529 | tracking 0.93 [0.82, 1.05] |
| H3-P | Gradient, « de 5P » − age | 0.0040 [−0.0003, 0.0084] | 1.97 | .068 | .203 | tracking 0.90 [0.81, 0.99] |


## The wording around the label moved the texts more than the label itself

The other wordings, exploratory except for L3, moved the texts further (Figure 2). Adding « en Suisse romande » to the H label made the texts older, with a shift of 0.87 years [0.54, 1.23], whereas adding the age in brackets made them younger than the age alone, with a shift of −0.46 years [−0.62, −0.33]; the L3 texts had more frequent words than both the age-only texts (0.018 Zipf, *p* < .001) and the bare-label texts (0.030 Zipf, *p* < .001). The French grades kept the level close to the age (−0.26 years [−0.45, −0.08]) but stretched the grade span, with a tracking of 1.32 [1.22, 1.45]: CP texts were easier and 6e texts harder than the texts for the same ages.

The collision control behaved as a misreading should. Asked for « élèves de 3e », « de 4e » or « de 5e », the models wrote texts 5.62 years older than for the ages meant by 3H to 5H [5.31, 5.99], that is, for French lower-secondary pupils, with a negative tracking (−0.92) because 3e is the oldest of these grades in France. Without any level, the models wrote for pupils of 9.4 to 11.7 years on their own rulers.

![Figure 2. Age equivalents of the label wordings, pooled over the six models: shift (years older than the age requested) and tracking (1 = follows the grade like the age-only texts, 0 = ignores it), with 95% bootstrap intervals over topics. The collision control « de 5e » lies far outside these axes and is reported in the text.](../../results/figures/fig2_labels.png)


## Two smaller models did not follow the bare labels

The averages hide a split between models (Figure 3, exploratory). Four models followed the bare H label at least as steeply as the age, with point estimates of tracking between 1.17 and 1.42. Claude Haiku 5.5 wrote its « de 5H » texts as for pupils 2.12 years older [1.75, 2.56] and hardly followed the grade (tracking 0.18 [−0.02, 0.41]); with the P label its shift fell to 0.48 years and its tracking rose to 0.64. Mistral Small 4 followed neither label well (tracking 0.46 for H and 0.16 for P): compared with its own age-only texts, its labelled texts were too hard for the youngest grades and too easy for the oldest.

![Figure 3. Shift and tracking of the bare labels « de 5H » (circles) and « de 5P » (squares), model by model, with 95% bootstrap intervals over topics (exploratory).](../../results/figures/fig3_models.png)


The knowledge probes add a second view (Table 3). Claude Sonnet 5.5, GPT-6.1 Sol and GPT-6 Luna gave the correct age for nearly every H and P grade, whereas Claude Haiku 5.5, Mistral Large 4 and Mistral Small 4 were right for 65%, 62% and 37% of the H grades. Their errors were almost all too old: on average, Claude Haiku 5.5 placed an H grade 1.62 years above its true age and Mistral Small 4 0.97 years above. For two of these three models, the probes and the texts erred in the same direction: Claude Haiku 5.5 and Mistral Large 4 also wrote their « de 5H » texts as for older pupils (shifts of 2.12 and 0.79 years). Mistral Large 4 nonetheless followed the grades (tracking 1.23) although it misplaced more than a third of the H grades in the probes, and Mistral Small 4, which placed grades too old, wrote its « de 5H » texts slightly younger on average (shift −0.49 years). In these six models, what a model stated about a label and how it wrote for it went together in some cases and not in others.

Table 3. Model by model: slope of the age-only ruler (H1), age at which each model writes without a level (L0, read on its ruler), and knowledge probes (60 per notation and model; correct when the midpoint of the first age range stated lies within the true range widened by half a year; error = midpoint stated minus true midpoint, positive when too old). Exploratory except the slopes.

| Model | Ruler slope (Zipf per year) | Default age, no level (years) | Probes correct, H (%) | Probes correct, P (%) | Mean probe error, H (years) | Mean probe error, P (years) |
|---|---|---|---|---|---|---|
| Claude Sonnet 5.5 | −0.045 | 10.5 | 100 | 98 | −0.14 | −0.13 |
| Claude Haiku 5.5 | −0.043 | 11.3 | 65 | 58 | 1.62 | 1.04 |
| GPT-6.1 Sol | −0.049 | 10.5 | 100 | 100 | 0.00 | 0.00 |
| GPT-6 Luna | −0.025 | 9.4 | 100 | 95 | 0.00 | 0.10 |
| Mistral Large 4 | −0.041 | 11.2 | 62 | 55 | 0.79 | 0.68 |
| Mistral Small 4 | −0.034 | 11.7 | 37 | 33 | 0.97 | 1.21 |


## Sensitivity analyses

The primary results did not depend on the analytic choices preregistered as sensitivity analyses (Supporting Information, Table S1). Removing the truncated, duplicated or flagged texts changed no estimate by more than 0.0002 Zipf, the regression with errors clustered by topic gave the same estimates with *p*-values within .005 of the topic-level tests, and reading the rulers through an isotonic fit gave shifts of 0.19 years for the H label and −0.05 for the P label. Residualising length within model enlarged the H level difference (−0.017 Zipf, *p* < .001) and left the other three tests non-significant. Both bare labels gave texts shorter than the age-only texts, by about 35 words on average (Table S2).

# Discussion

DISCUSSION TO WRITE

# Conclusion

CONCLUSION TO WRITE

# Statements

STATEMENTS TO WRITE (data availability, preregistration, ethics, conflicts of interest, funding, generative AI)

# References

REFERENCES TO WRITE (only sources read in full text)
