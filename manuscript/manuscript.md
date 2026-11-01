---
title: "TITLE TO WRITE LAST"
---

<!-- Source of the ART 5 manuscript. Every number is a {{name}} placeholder resolved from
results/manuscript_numbers.json by manuscript/render.py; tables are {{table:name}} placeholders
built by render.py from the same file and design.json. checks/check_numbers.py fails on a number
typed by hand outside the allowlist it documents. Draft of the main session (claude-opus-5-5). -->

# Abstract

Teachers are advised to name their pupils' grade when they ask a language model for a reading text, but grade labels are local. In French-speaking Switzerland, grades are counted from the first year of kindergarten: « 5H » or, in Vaud and Geneva, « 5P » names pupils aged {{age_5H_from}} to {{age_5H_to}}, two years younger than pupils in the fifth year of primary school in France. This preregistered audit asked whether {{n_models_word}} large language models from three providers write French reading texts for these labels at the same lexical demand as for the matching age. We generated {{n_texts}} stories and informational texts for grades 3H to 8H on {{n_topics}} topics and measured the mean frequency of their content words. Every model used rarer words as the requested age rose. Pooled over models, the bare HarmoS label gave texts written as for pupils {{ae_L1_shift}} years older than the age (95% CI [{{ae_L1_shift_ci_lo}}, {{ae_L1_shift_ci_hi}}]), below the smallest effect of interest, and the P label showed no difference; neither label changed how texts followed the grade. Two lighter models misread the bare labels, one writing as for pupils about two years older and hardly following the grade, and knowledge probes showed that wrong answers about the labels placed grades mostly two years too old. Adding the age to the label made the models more consistent, while naming the region made texts harder. Teachers and tool developers can keep local labels if they add the age; audits of leveled text generation should report results model by model.

# Practitioner notes

**What is already known about this topic**

- Teachers are advised to ask language models for reading texts and to state the pupils' grade in the prompt.
- Studies in English found that outputs often stay above the requested grade or adapt little to the requested age.
- Grade labels differ between school systems; in French-speaking Switzerland, grades are counted from kindergarten.

**What this paper adds**

- A preregistered audit of {{n_texts}} French reading texts from {{n_models_word}} models shows that, on average, « de 5H » and « de 5P » give texts with nearly the lexical demand of the matching age.
- Two lighter models misread the bare labels, one by about two years, which a pooled analysis would hide.
- Adding the age to the label narrowed the differences between models; naming the region made texts harder.

**Implications for practice and/or policy**

- When asking a model for a reading text, state the pupils' age, alone or after the grade label.
- Tools built for Swiss schools can map grade labels to ages before the prompt reaches the model.
- Evaluations of AI tools for teachers should report results for each model, not only on average.

# Introduction

A primary teacher in Lausanne who needs a short text about bees for tomorrow's reading lesson can now ask a chatbot for « une histoire à lire pour des élèves de 5H ». Teachers have begun to work this way: in a survey of upper-secondary and private-school teachers in Vaud, about half had used ChatGPT, and a quarter of these had used it in their teaching, mainly to prepare lessons (Avry, 2023). Advice written for teachers recommends naming the readers' grade in the prompt so that the model pitches the text accordingly (Imperial & Tayyar Madabushi, 2023, p. 206). The advice assumes that the model knows what the grade means. For a label like « 5H », which belongs to the school system of French-speaking Switzerland, that assumption has not been tested.

Evidence from English-language studies is not reassuring. Asked to answer science questions for readers of different ages, ChatGPT produced answers whose readability barely moved with the requested age (Rooein et al., 2023). Asked for stories for second-grade readers, ChatGPT wrote easier stories when the grade was named, but no model reached the target range under any wording (Imperial & Tayyar Madabushi, 2023), and models asked to rewrite texts to a target Lexile level tended to overshoot it (Huang et al., 2024). These studies used United States grades, CEFR levels or Lexile scores.

School grade labels are local, and some collide. Under the intercantonal HarmoS agreement, children in Switzerland start school once they are four years old on {{src_harmos_reference_day}}, and the primary degree lasts eight years, kindergarten included (CDIP, 2007). Counting from the first year of kindergarten, Fribourg numbers the school years 1H to 11H (Canton de Fribourg, 2025), while Vaud and Geneva write the primary years 1P to 8P (État de Vaud, n.d.; République et canton de Genève, 2026), and all three cantons place 5H or 5P at the start of a cycle for pupils aged {{src_cycle2_age_from}} to {{src_cycle2_age_to}}. A pupil who has neither repeated nor skipped a year is thus {{age_5H_from}} or {{age_5H_to}} years old in 5H, a grade that France calls CE2 (Ministère de l'Éducation nationale, 2024a), while « 5e » names the second year of French lower-secondary school (Ministère de l'Éducation nationale, 2024b). A model that reads « 5H » as the fifth year of an elementary school starting at six would write for pupils two years older, and a model that confuses it with « 5e » would miss by four years. Nothing in the text it returns would tell the teacher.

This article reports a preregistered audit of how {{n_models_word}} large language models from three providers read Swiss grade labels when they write French reading texts for primary pupils. We compared texts requested with the bare HarmoS and P labels with texts requested with the matching age, on a measure of lexical demand, the mean frequency of the content words, and asked two questions. Do the labels give texts at the same level as the age? Do they follow the grade from 3H to 8H as the age does? Variants of the label, a collision control and knowledge probes then show where the differences come from. Searches of Consensus, alphaXiv and the web, in English and French, found no earlier study of how language models read Swiss or other non-US school grade labels; Scite and Elicit could not be searched (the search log is in the repository).

# Background

## Generating texts for a reading level

Studies of leveled text generation by language models agree that naming a level can move the output, but not always far enough. In the study by Imperial and Tayyar Madabushi (2023), naming the second grade lowered the Flesch–Kincaid grade level of ChatGPT's stories but left it above the target range, and describing the level brought the stories closer to it than naming the grading framework did. Rooein et al. (2023) found that the readability of ChatGPT's answers stayed within a narrow band whatever the requested age or education level, a "style" that prompting hardly moved, although another model of the same provider did respond to age. Huang et al. (2024) asked three models to rewrite texts to Lexile levels and found that a minority of outputs landed within the target band, with a skew toward harder texts. Oh et al. (2026) describe prompted grade labels as producing responses above the target grade and propose fine-tuned grade-specific models instead. When models rewrite a given text, prompting moves readability in the requested direction, but the output's readability stays correlated with that of the source (Farajidizaji et al., 2023; Trott & Rivière, 2024).

This research shares three features that limit what it says about classroom practice outside the English-speaking world. The targets are formal scales (Lexile, CEFR, United States grades) rather than the labels teachers use locally. The readability measures are formulas built for English and for the United States school system, which their own authors note may not transfer to other languages and school systems (Rooein et al., 2023). And the reference is an external target, so a model's failure to reach it cannot be separated from a disagreement about what the target means. In a European assessment context, Ripoll y Schmitz and Sonnleitner (2025) used GPT-4 to write German reading passages for fifth graders in Luxembourg and had reviewers rate them blind against passages written by people, an evaluation by human judgement rather than by a text measure.

## Measuring the lexical demand of a text

Word frequency accounts for a large share of the differences in how quickly words are recognised (Brysbaert et al., 2018); in English, mean word frequency, concreteness and age of acquisition together explained about a third of the variance in readers' judgements of text readability (Trott & Rivière, 2024). In French, the readers used in the first years of primary school draw on more frequent words than those of the later years (Lété et al., 2004). On the Zipf scale, frequencies are expressed as the base-10 logarithm of occurrences per billion words, so that values from {{src_zipf_low_from}} to {{src_zipf_low_to}} mark rare words and values from {{src_zipf_high_from}} to {{src_zipf_high_to}} common ones (Brysbaert et al., 2018). For French, the Lexique database gives lemma frequencies from film subtitles and from novels (New & Pallier, n.d.; New et al., 2004), and Manulex gives frequencies by grade from the readers used in French primary schools (Lété et al., 2004). Frequency is not the only source of difficulty: sentence length matters too, and for beginning readers so do decodability and information load (Huang et al., 2024; Peereman et al., 2007).

# Method

## Design and preregistration

The study is an audit experiment in which the data are texts written by language models under controlled prompts; no person took part. The hypotheses, the measure, the exclusion rules, the sample size and the analyses were preregistered on AsPredicted before the confirmatory data were collected (link anonymised for review). A pilot of {{pilot_calls}} calls to {{pilot_models_word}} of the models, run the day before, requested texts with the pupils' age only and served to estimate the variance and the age slope of the measure; its texts are excluded from every confirmatory analysis. The prompts, the call plan, the code, the raw outputs and the results are archived in a repository whose states at registration and at data freeze are tagged (link anonymised for review).

## Prompts and conditions

Each prompt asked in French for a reading text on a topic, for pupils of a given level: « Écris {une histoire à lire | un texte documentaire à lire} pour des élèves{label}, sur le thème {topic}. Réponds seulement avec un titre et le texte. » ("Write {a story to read | an informational text to read} for pupils{label}, on the topic {topic}. Answer only with a title and the text.") The label named the readers' level in one of eight ways (Table 1). The bare HarmoS label (L1, « de 5H ») and the bare P label (L1P, « de 5P ») are the two notations the cantons use, H in Fribourg and P in Vaud and Geneva. The age-only label (L5, « de 8 à 9 ans ») is the reference: it tells the model what the Swiss label means, so a model that understands the label should write the same kind of text under both. L6 is a collision control: the same digit with the suffix of the French lower-secondary grades (« de 5e »), which in France names the second year of lower-secondary school (Ministère de l'Éducation nationale, 2024b); it was run at 3H to 5H only, because « de 6e » is the L4 prompt of 8H. L0 gives no level and shows each model's default reader.

{{table:labels}}

The labels were crossed with the six grades of the primary cycle after kindergarten (3H to 8H, pupils aged {{age_3H_from}} to {{age_3H_to}} up to {{age_8H_from}} to {{age_8H_to}}), two genres (a story and an informational text) and {{n_topics}} fixed topics, from bees and volcanoes to a train journey and a family celebration. Each model thus wrote {{texts_per_topic}} texts per topic, {{n_texts}} texts in all. Each prompt was sent once, as an independent call without system prompt or conversation history, in a random order (seed {{order_seed}}), with temperature {{temperature}} and at most {{max_output_tokens}} output tokens; reasoning settings were left at each provider's default.

## Models

We audited {{n_models_word}} models, two from each of three providers: a mid-tier model and a lighter, cheaper model, as the providers' price lists placed them at the time of the study: {{name_anthropic_balanced}} ({{id_anthropic_balanced}}) and {{name_anthropic_light}} ({{id_anthropic_light}}) from Anthropic, {{name_openai_balanced}} ({{id_openai_balanced}}) and {{name_openai_light}} ({{id_openai_light}}) from OpenAI, and {{name_mistral_balanced}} ({{id_mistral_balanced}}) and {{name_mistral_light}} ({{id_mistral_light}}) from Mistral AI. The identifiers are those returned by the APIs, which matched the identifiers requested for every call. All calls were made on {{collection_day}}. Every model accepted the requested temperature.

## Knowledge probes

To separate what a model can state about the labels from how it writes, each model also answered {{probes_per_model_notation}} knowledge questions per notation, {{n_probes}} in all: « À quel âge correspondent des élèves de 5H ? » ("What age are pupils in 5H?") and the same question opened by « En Suisse romande, » ("In French-speaking Switzerland,"), for the six grades in the H and P notations, {{probe_repetitions_word}} times each. As preregistered, the first age range stated in an answer counts, and it is correct if its midpoint lies within the true range widened by half a year on each side.

## Measure

The dependent variable is the mean Zipf frequency of the content lemmas of a text, a measure of lexical demand: texts for younger readers use more frequent words, which score higher. Each word form was read as its most frequent lemma in the French lexical database Lexique {{lexique_version}} (New & Pallier, n.d.; New et al., 2004), and content words were the forms read as nouns, qualifying adjectives or verbs, without the lemmas *être* and *avoir*, the indefinites *tout*, *autre* and *même*, and proper names. A lemma's frequency is the mean of its frequencies per million words in the two corpora of Lexique, film subtitles and novels published from {{src_lexique_books_from}} to {{src_lexique_books_to}} (New & Pallier, n.d.), expressed on the Zipf scale, the base-10 logarithm of the frequency per billion words (van Heuven et al., 2014, as cited in Brysbaert et al., 2018). We computed it as log10(f + {{zipf_smoothing}}) + 3, so that a lemma absent from Lexique counts as frequency zero. Titles, markdown and lines addressed to the user rather than to the pupils (« Voici une histoire… », « N'hésitez pas… ») were removed before measurement, although none was found in the confirmatory texts; the exact rules and the test texts that pin them are in the repository.

The measure passed two checks of validity. Before the pilot, it was run on the articles of the French Wikipedia and of Vikidia, an online encyclopedia for readers aged {{src_vikidia_age_from}} to {{src_vikidia_age_to}} (Vikidia, n.d.), on the same {{vik_subjects}} subjects; the preregistered criterion was met, with Vikidia scoring higher in {{vik_higher}} of the {{vik_usable}} usable pairs (sign test, one-sided *p* {{vik_p}}; mean difference {{vik_mean_diff}} Zipf). In the confirmatory data, the age-only texts of every model served as a manipulation check (H1, below). Eight secondary measures were preregistered: the median Zipf frequency of content lemmas, the shares of content lemmas below Zipf 3 and below Zipf 4, mean word length, words per sentence, number of words, the Kandel–Moles adaptation of the Flesch readability formula to French (Kandel & Moles, 1958, as cited in Primpied et al., 2022) and the mean Zipf frequency of word forms in films.

## Exclusions

A call that failed or returned nothing was requested once more. A text that refused the task or asked for clarification, had fewer than {{min_words}} words, or had more than {{max_share_oov_pct}}% of its word tokens absent from Lexique was requested once more, and excluded if the second answer failed the same rule. Truncated texts, exact duplicates and answers that addressed the user outside the story were kept, flagged and removed in sensitivity analyses. No exclusion rule used the value of any frequency measure.

## Analysis

Texts were paired on model, grade, genre and topic. For topic *t* and grade *g*, *d*(*g*, *t*) is the mean over models and genres of the difference between a label's text and the age-only text. The level of a topic is the mean of *d* over the six grades, and its gradient is the least-squares slope of *d* on the midpoint of the grade's age range. A label read as an older grade gives a negative level (rarer words), and a label that the model ignores, writing at the same level whatever the grade, gives a positive gradient: too hard for the youngest pupils and too easy for the oldest. The four primary tests are two-sided one-sample *t*-tests over topics (df = {{h2H_df}}) of the level of L1 minus L5 (H2-H) and of L1P minus L5 (H2-P), and of the gradient of L1 minus L5 (H3-H) and of L1P minus L5 (H3-P), with Holm's correction over the four tests and α = {{alpha}}. Topics are the unit of inference because the texts of a topic share content that a text-level test would treat as independent; inference is conditional on these six models and this prompt wording.

The smallest effect of interest was a level difference of {{sesoi_zipf}} Zipf, about one year of age on the planning ruler. With the pilot's residual standard deviation taken at its upper 80% confidence bound ({{pilot_sd_upper80}}), {{n_topics}} topics gave a simulated power of {{pilot_power_16}} for the H2-H level test at that difference, which fixed the number of topics before the deposit.

The manipulation check H1 asked whether, with the age only, each model's texts get rarer words as the requested age rises: per model, an ordinary least-squares regression of the measure on the age midpoint within L5, with genre and topic effects, standard errors clustered by topic and a one-sided *t*-test with {{h2H_df}} df.

To express effects in years, each model is read on its own age-only ruler, the least-squares line through its six L5 means, with slope *b*. For a label, the shift is the sum over models of the levels divided by the sum of the slopes, in years (positive values mean texts written as for older pupils), and the tracking is 1 plus the sum of the gradients divided by the sum of the slopes (1 means that the texts follow the grade as the age-only texts do, 0 that they ignore it). Only models with a ruler slope of at most {{min_ruler_slope}} Zipf per year are read, a rule that all six models met. Intervals are 95% percentile intervals from {{bootstrap_resamples}} bootstrap resamples of topics. Per-model estimates, per-grade profiles, L2, L4 and the knowledge probes are exploratory; Supporting Information S1 lists where every preregistered analysis is reported.

# Results

## Data

All {{n_calls}} calls were answered: {{n_first_pass_failed_word}} probe calls to {{name_mistral_balanced}}, which spent the whole output limit on reasoning and returned no text at the first pass, were answered at the second. None of the {{n_texts}} texts was refused, too short or out of lexicon, so all were analysed; {{n_truncated_word}} were truncated, {{n_flag_meta}} were flagged as addressing the user and none was an exact duplicate. Texts had a mean length of {{words_mean_all}} words (median {{words_median_all}}), from {{words_mean_openai_light}} words on average for {{name_openai_light}} to {{words_mean_anthropic_balanced}} for {{name_anthropic_balanced}}. The study cost {{spend_total_usd}} USD in API calls.

## Every model lowered word frequency with age

The manipulation check succeeded for all {{h1_n_supported_word}} models. With the age only, the mean Zipf frequency of content lemmas fell as the requested age rose, with slopes from {{h1_slope_max}} Zipf per year for {{h1_slope_max_model}} to {{h1_slope_min}} for {{h1_slope_min_model}} (all one-sided *p* {{h1_p_max}}; Figure 1), and no ruler departed from a straight line (linearity tests, smallest *p* {{h1_lin_p_min}}). On these rulers, a difference of {{sesoi_zipf}} Zipf is roughly one year of age.

{{figure:fig1}}

## Bare labels: almost the age, on average

Table 2 gives the four primary tests. Texts requested with the bare HarmoS label used slightly rarer words than texts requested with the matching age (H2-H: {{h2H_est}} Zipf, 95% CI [{{h2H_ci_lo}}, {{h2H_ci_hi}}], *t*({{h2H_df}}) = {{h2H_t}}, *p* {{h2H_p}}, Holm-corrected *p* {{h2H_pholm}}). The difference is real but small: read on the models' own rulers, the « de 5H » texts were written as for pupils {{ae_L1_shift}} years older (95% CI [{{ae_L1_shift_ci_lo}}, {{ae_L1_shift_ci_hi}}]), and its confidence interval excludes the smallest effect of interest. The bare P label showed no difference (H2-P: {{h2P_est}} Zipf [{{h2P_ci_lo}}, {{h2P_ci_hi}}], *p* {{h2P_p}}); its interval excludes differences as large as the smallest effect of interest in either direction, and its shift was {{ae_L1P_shift}} years [{{ae_L1P_shift_ci_lo}}, {{ae_L1P_shift_ci_hi}}].

Neither label changed how texts followed the grade. The gradients of the differences were small and not significant (H3-H: {{h3H_est}} Zipf per year [{{h3H_ci_lo}}, {{h3H_ci_hi}}], Holm *p* {{h3H_pholm}}; H3-P: {{h3P_est}} [{{h3P_ci_lo}}, {{h3P_ci_hi}}], Holm *p* {{h3P_pholm}}). In years, the tracking of the H label was {{ae_L1_track}} [{{ae_L1_track_ci_lo}}, {{ae_L1_track_ci_hi}}] and that of the P label {{ae_L1P_track}} [{{ae_L1P_track_ci_lo}}, {{ae_L1P_track_ci_hi}}]: from 3H to 8H, the P texts moved through about nine tenths of the age span that the age-only texts covered. The bootstrap interval of the P label's tracking stops just below 1 while its preregistered gradient test did not reject, so the evidence of under-tracking is weak.

{{table:primary}}

## The wording around the label moved the texts more than the label itself

The other wordings, exploratory except for L3, moved the texts further (Figure 2). Adding « en Suisse romande » to the H label made the texts older, with a shift of {{ae_L2_shift}} years [{{ae_L2_shift_ci_lo}}, {{ae_L2_shift_ci_hi}}], whereas adding the age in brackets made them younger than the age alone, with a shift of {{ae_L3_shift}} years [{{ae_L3_shift_ci_lo}}, {{ae_L3_shift_ci_hi}}]; the L3 texts had more frequent words than both the age-only texts ({{gloss_level_vs_age_est}} Zipf, *p* {{gloss_level_vs_age_p}}) and the bare-label texts ({{gloss_level_vs_bare_est}} Zipf, *p* {{gloss_level_vs_bare_p}}). The French grades kept the level close to the age ({{ae_L4_shift}} years [{{ae_L4_shift_ci_lo}}, {{ae_L4_shift_ci_hi}}]) but stretched the grade span, with a tracking of {{ae_L4_track}} [{{ae_L4_track_ci_lo}}, {{ae_L4_track_ci_hi}}]: CP texts were easier and 6e texts harder than the texts for the same ages.

The collision control behaved as a misreading should. Asked for « élèves de 3e », « de 4e » or « de 5e », the models wrote texts {{ae_L6_shift}} years older than for the ages meant by 3H to 5H [{{ae_L6_shift_ci_lo}}, {{ae_L6_shift_ci_hi}}], that is, for French lower-secondary pupils, with a negative tracking ({{ae_L6_track}}) because 3e is the oldest of these grades in France. Without any level, the models wrote for pupils of {{l0_age_min}} to {{l0_age_max}} years on their own rulers.

{{figure:fig2}}

## Two smaller models did not follow the bare labels

The averages hide a split between models (Figure 3, exploratory). {{ae_L1_n_track_ge1_Word}} models followed the bare H label at least as steeply as the age, with point estimates of tracking between {{ae_L1_track_ge1_min}} and {{ae_L1_track_ge1_max}}. {{name_anthropic_light}} wrote its « de 5H » texts as for pupils {{ae_L1_anthropic_light_shift}} years older [{{ae_L1_anthropic_light_shift_ci_lo}}, {{ae_L1_anthropic_light_shift_ci_hi}}] and hardly followed the grade (tracking {{ae_L1_anthropic_light_track}} [{{ae_L1_anthropic_light_track_ci_lo}}, {{ae_L1_anthropic_light_track_ci_hi}}]); with the P label its shift fell to {{ae_L1P_anthropic_light_shift}} years and its tracking rose to {{ae_L1P_anthropic_light_track}}. {{name_mistral_light}} followed neither label well (tracking {{ae_L1_mistral_light_track}} for H and {{ae_L1P_mistral_light_track}} for P): compared with its own age-only texts, its labelled texts were too hard for the youngest grades and too easy for the oldest.

{{figure:fig3}}

The knowledge probes add a second view (Table 3). {{name_anthropic_balanced}}, {{name_openai_balanced}} and {{name_openai_light}} gave the correct age for nearly every H and P grade, whereas {{name_anthropic_light}}, {{name_mistral_balanced}} and {{name_mistral_light}} were right for {{probe_anthropic_light_H}}%, {{probe_mistral_balanced_H}}% and {{probe_mistral_light_H}}% of the H grades. Their errors were almost all too old: on average, {{name_anthropic_light}} placed an H grade {{perr_anthropic_light_H}} years above its true age and {{name_mistral_light}} {{perr_mistral_light_H}} years above. For two of these three models, the probes and the texts erred in the same direction: {{name_anthropic_light}} and {{name_mistral_balanced}} also wrote their « de 5H » texts as for older pupils (shifts of {{ae_L1_anthropic_light_shift}} and {{ae_L1_mistral_balanced_shift}} years). {{name_mistral_balanced}} nonetheless followed the grades (tracking {{ae_L1_mistral_balanced_track}}) although it misplaced more than a third of the H grades in the probes, and {{name_mistral_light}}, which placed grades too old, wrote its « de 5H » texts slightly younger on average (shift {{ae_L1_mistral_light_shift}} years). In these six models, what a model stated about a label and how it wrote for it went together in some cases and not in others.

{{table:models}}

## Sensitivity analyses

The primary results did not depend on the analytic choices preregistered as sensitivity analyses (Supporting Information, Table S1). Removing the truncated, duplicated or flagged texts changed no estimate by more than {{sens_max_abs_diff_level}} Zipf, the regression with errors clustered by topic gave the same estimates with *p*-values within {{ols_p_max_abs_diff}} of the topic-level tests, and reading the rulers through an isotonic fit gave shifts of {{ae_L1_iso_shift}} years for the H label and {{ae_L1P_iso_shift}} for the P label. Residualising length within model enlarged the H level difference ({{sens_length_residualised_h2H_est}} Zipf, *p* {{sens_length_residualised_h2H_p}}) and left the other three tests non-significant. Both bare labels gave texts shorter than the age-only texts, by about {{sec_n_words_h2H_abs}} words on average (Table S2).

# Discussion

## A local label is mostly understood, on average

Does naming the grade with a Swiss label give reading texts of the same lexical demand as giving the pupils' age? Averaged over {{n_models_word}} current models, nearly. The bare HarmoS label gave slightly rarer words, a shift of about a third of a year, below the difference we had set in advance as the smallest worth detecting; the bare P label of Vaud and Geneva gave no detectable difference, and neither label weakened how texts followed the grade from 3H to 8H.

This contrasts with earlier audits in English, where prompting for an age or a grade changed the readability of the outputs little or left it above the target (Imperial & Tayyar Madabushi, 2023; Rooein et al., 2023). Here every model lowered word frequency as the requested age rose. The difference may come from newer models, from the genre (reading texts rather than answers to questions), from the measure (lemma frequency rather than surface formulas) or from the language, and our design cannot separate these. Our reference also differs: we compared each label with the text the same model writes for the matching age, so we can say whether a label is read as its age, not whether either text is right for real pupils of that age.

## The average hides models that misread the label

A teacher does not meet an average; each tool runs on one model. Two of the six models, both the lighter model of their provider, followed the bare labels poorly. Read on its own ruler, {{name_anthropic_light}}'s « de 5H » texts were pitched {{ae_L1_anthropic_light_offset_3H}} years above the age of 3H pupils but close to it at 8H ({{ae_L1_anthropic_light_offset_8H}} years). {{name_mistral_light}}'s were {{ae_L1_mistral_light_offset_3H}} years too old at 3H and {{ae_L1_mistral_light_offset_8H_abs}} years too young at 8H. The youngest pupils are the ones most likely to receive a text that is too hard.

The knowledge probes suggest where such errors come from. Of the {{probe_n_wrong}} wrong answers, {{probe_wrong_two_years_pct}}% placed the grade {{probe_window_lo}} to {{probe_window_hi}} years too old. That is the error of reading the digit as the year of a primary school that starts the year pupils turn six: the fifth year of the French école élémentaire is CM2 (Ministère de l'Éducation nationale, 2024a), the grade of pupils aged {{age_7H_from}} to {{age_7H_to}}, two years above 5H. This reading fits {{name_anthropic_light}} and {{name_mistral_balanced}}, whose texts and probe answers erred in the same direction, but not {{name_mistral_light}}, whose probe answers were too old while its labelled texts were, on average, slightly younger. A quick question to a model about the age of a grade is therefore a weak screen: the {{probe_ok_n_word}} models that stated the right ages wrote « de 5H » texts within a year of the age (shifts from {{ae_L1_probe_ok_shift_min}} to {{ae_L1_probe_ok_shift_max}} years), but a wrong answer did not predict how the texts would go wrong.

## The words around the label matter as much as the label

Wordings that a teacher might use to be helpful moved the texts more than the bare labels did. Naming the region made texts harder by almost a year, an effect we did not predict and cannot explain from these data. Adding the age to the label made texts slightly easier than the age alone and, in exploratory per-model estimates, brought the models closer together: with the gloss, per-model shifts ranged from {{ae_L3_shift_min}} to {{ae_L3_shift_max}} years and tracking from {{ae_L3_track_min}} to {{ae_L3_track_max}}, against {{ae_L1_shift_min}} to {{ae_L1_shift_max}} years and {{ae_L1_track_min}} to {{ae_L1_track_max}} with the bare H label. The French grade names kept the average level but stretched the span between CP and 6e, perhaps because these names are tied more closely than ages to learning to read and to entering secondary school. The collision control shows how far a label can mislead when its digit is read in another system: « de 5e » moved texts by more than five years.

## Implications

For teachers, the practical rule is simple: state the age, alone or after the label (« pour des élèves de 5H (8 à 9 ans) »); of the wordings that contained a label, the second gave the most consistent texts across models. With the three larger models audited here, the bare labels gave texts within a year of the age on average, but a teacher cannot always tell which model a tool runs on. For the developers of tools for Swiss schools, the same rule can be applied before the prompt reaches the model, by mapping the label to its ages. For research on generative AI in education, the results show that audits of leveled text generation should report results by model, because pooled estimates can hide models that fail, and that model-internal age equivalents give a scale on which label wordings, models and languages can be compared.

## Limitations

The measure covers one dimension of text difficulty: sentence length matters too, and for beginning readers so do decodability and information load (Huang et al., 2024). The frequencies come from Lexique, whose corpora are films and novels for adults; grade-level norms from French school readers exist (Lété et al., 2004), and adult-based norms are a weaker guide to what children have met in print (Peereman et al., 2007). The reference is each model's own idea of an age, so the study shows equivalence between wordings, not appropriateness for pupils, and no teacher or pupil judged the texts (compare Ripoll y Schmitz & Sonnleitner, 2025). Each condition was sampled once per topic and genre, in French, with one prompt template and a temperature of {{temperature}}; other wordings, conversation histories or settings could behave differently. The models were those available on {{collection_day}}, and providers update them; the code and prompts are public so that the audit can be repeated. The study was powered for the pooled tests, and the per-model estimates are exploratory, with wide intervals for some models. Finally, the study was designed, run and written with an AI assistant made by one of the audited providers; the analyses were preregistered, the code that produced every number is public and the checks were scripted, which limits but does not remove the risk this poses.

# Conclusion

Swiss teachers can name a grade the way they do in class, « de 5H » or « de 5P », and most of the current models we audited will write a reading text at about the lexical level of the matching age. Not every model does: two lighter models misread the bare labels, one by about two years. Adding the age to the label narrowed the differences between models, which makes it the wording to recommend in teacher education and to build into classroom tools.

# Statements

**Data availability.** The prompts, call plans, raw model outputs with their SHA-256 hashes, analysis code, results and the scripts that check every number of this article are available in the study repository (link anonymised for review; it will be archived with a DOI on acceptance).

**Preregistration.** The hypotheses, measure, exclusion rules, sample size and analyses were preregistered on AsPredicted on {{proc_deposit_day}}, before the confirmatory data were collected (link anonymised for review). The Supporting Information (S1) lists where each preregistered analysis is reported; there were no deviations.

**Ethics.** The study involved no human participants and no personal data: its data are texts generated by language models through their public APIs. No ethical approval was required.

**Conflicts of interest.** AUTHOR INPUT: the author declares no conflict of interest (to confirm).

**Funding.** AUTHOR INPUT: no specific funding (to confirm). The API calls cost {{spend_total_usd}} USD for the main study and {{pilot_spend_usd}} USD for the pilot. The OpenAI and Mistral calls were paid by the author; the Anthropic calls were paid from API credits attached to the author's account (wording to confirm).

**Use of generative AI.** This study was conceived and designed with the assistance of {{proc_assistant_name}} ({{proc_assistant_id}}, Anthropic), which also searched and summarised the literature, wrote the code for data collection and analysis, drafted the manuscript and ran internal error checks. Anthropic is one of the three providers whose models were audited. The outputs of the six audited models were generated as the research data of this study; the prompts, parameters and outputs are archived in the repository. Reference and number checks were performed by scripted tools and by separate AI sessions, whose reports the author reviewed. The author approved the study design before data collection, reviewed and edited the full manuscript, and takes full responsibility for its content.

# References

{{references}}
