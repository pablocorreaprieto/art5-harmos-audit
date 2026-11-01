Internal reading by a separate AI session. Not peer review.

# Literature reading notes for ART 5

Date of reading: 2026-11-01. Reader: a Claude Sonnet 5.5 session working only from the tools listed in search_log.md (WebSearch, Consensus, Crossref queried through WebFetch, and the alphaXiv readers for arXiv full text and for the raw text of PDFs and web pages). Scite was refused (paid plan). The WebFetch tool passes a page through a small summarising model; every entry that rests on such an extraction says so. Apart from scratch scripts in the session scratchpad (folder p2_tools, outside the output folder), nothing outside the output folder was changed, and nothing was posted or sent.

Companion files: search_log.md (every query and every blocked source) and sources.csv (one row per source, same access labels as here).

## Access labels used

- read-directly: I read the raw text of the source itself (HTML page, PDF or arXiv full text) and the passages noted are in it. Pages or sections that were not returned are listed under each source.
- full-text-extracted: the full text went through a fetch tool that returns a machine-written extraction; I did not see the raw text. Not citable until checked against the PDF (used once: patel2023).
- abstract-only: only an abstract or a landing page was read. Not citable.
- not accessible: the source did not load or was refused. Not citable for its content. Where a reference is confirmed by a source I did read, the entry says so.
- [inference]: my own step across sources; no source states it.
- Quotes are under 15 words and at most one per passage. Locations are PDF page, journal page or section, as stated per source.

## Index

| key | source | access | citable | supports |
|---|---|---|---|---|
| rooein2023 | Rooein et al. (2023) | read-directly | yes | Intro (earlier null result: age and education prompts barely move readability, English); Discussion (Haiku result); Limitations (US formulas do not transfer) |
| huang2024 | Huang, Wei & Huang (2024) | read-directly | yes | Intro (leveled-text generation skews above the requested level); Method/Limitations (frequency is one of several difficulty features for young readers) |
| oh2026 | Oh, Whang, Evans & Wang (2026) | read-directly | yes | Intro (statement that prompted grade labels give text above the target grade; their own contribution is fine-tuning) |
| imperial2023 | Imperial & Tayyar Madabushi (2023) | read-directly | yes | Intro/Discussion (naming a grade shifts output easier but it stays above target; wording of the level matters) |
| ripoll2025 | Ripoll y Schmitz & Sonnleitner (2025) | read-directly | yes | Intro (GPT-4 reading texts for Luxembourg grade 5, German, human ratings); Discussion (human ratings versus an automatic lexical audit) |
| trott2024 | Trott & Rivière (2024) | read-directly | yes | Method (mean word frequency is one partial predictor of rated readability, R2 = 0.36); Discussion (direction is controlled, level is not) |
| farajidizaji2023 | Farajidizaji, Raina & Gales (2023) | read-directly | yes | Discussion (LLMs order grade/age-style targets sensibly but miss absolute levels; label wording is part of the prompt) |
| liu2025 | Liu et al. (2025) | abstract-only | no | Intro candidate (ChatGPT simplification compared with expert teachers) |
| watanabe2025 | Watanabe (2025) | abstract-only | no | Intro candidate (a named grade in the prompt works better than "more readable") |
| patel2023 | Patel et al. (2023) | full-text-extracted | no | Intro/Discussion candidate (earlier GPT-3 grade-targeted prompt study) |
| mesmer2024 | Mesmer (2024) | abstract-only | no | Method/Limitations candidate: closest source to the ART 5 measure (mean word frequency of primary-grade texts and its limits) |
| li2024 | Li et al. (2024) | abstract-only | no | Intro candidate (readability of AI-generated math stories and engagement) |
| nguyen2026 | Nguyen (2026) | abstract-only | no | Intro/Discussion candidate (lexical profile of ChatGPT texts by CEFR target level; closest in measure type) |
| new2004_lexique2 | New et al. (2004) | not accessible | no | Reference for the Lexique database (cite under its true title, Lexique 2) |
| new2007_subtitles | New et al. (2007) | abstract-only | no | Source of the film-subtitle frequencies (Intro/Method) |
| lexique3manual | New & Pallier, Lexique 3 manual (v3.2) | read-directly | yes | Method (what film and book lemma frequencies are); Limitations (both corpora are adult-directed) |
| manulex2004 | Lété, Sprenger-Charolles & Colé (2004) | read-directly | yes | Limitations/Discussion (grade-level French frequency norms exist; SFI is the older analogue of the Zipf scale) |
| peereman2007 | Peereman, Lété & Sprenger-Charolles (2007) | read-directly | yes | Limitations (adult-directed databases are not child-based; frequency is not the only factor) |
| brysbaert2018 | Brysbaert, Mandera & Keuleers (2018) | read-directly | yes | Method (definition and reading of the Zipf scale) |
| vanheuven2014_subtlexuk | van Heuven et al. (2014) | not accessible | no | Origin of the Zipf scale (reach it through Brysbaert et al., 2018, p. 6) |
| kandelmoles1958 | Kandel & Moles (1958) | not accessible | no | Only if the manuscript mentions Flesch-type formulas as an alternative measure |
| javourey2022 | Javourey-Drevet et al. (2022) | read-directly | yes | Method/Limitations (Lexique 3 lemma-frequency statistics differ between simplified and original texts for grade-2 readers) |
| primpied2022 | Primpied, Beauchemin & Khoury (2022) | read-directly | yes | Method/Limitations (French text complexity uses many features including Lexique 3 frequencies; one formula overlaps heavily between levels) |
| harmos2007 | CDIP (2007), HarmoS accord | read-directly | yes | Intro/Method (entry at 4 completed years on 31 July; 8 primary years; 11 years of schooling) |
| vd_deroulement | Canton de Vaud, Déroulement de l'école obligatoire | read-directly | yes | Intro/Method (5P is the first year of cycle 2; ages 8 to 12 en principe; P and S labels) |
| ge_primaire | Canton de Genève, Bienvenue à l'école primaire | read-directly | yes | Intro/Method (Geneva uses P labels; cycle moyen 5P to 8P for ages 8 to 12) |
| fr_cycle2 | Canton de Fribourg, Cycle 2 (and overview page) | read-directly | yes | Intro/Method (source of the label 5H; cycle 2 ages 8 to 12 en principe; 1H to 11H) |
| vd_per | Canton de Vaud, Plan d'études romand (PER) | read-directly | yes | Intro (one sentence on the curriculum frame) |
| eurydice_fr_primary | Eurydice, France, Enseignement primaire | read-directly | yes | Method/Discussion (CE2 = third elementary year; 6e = first collège year) |
| epfl2023_vaud_teachers | Avry (2023), EPFL news item | read-directly | yes | Intro (Vaud evidence that some teachers use ChatGPT for lesson preparation) |
| sclar2024 | Sclar et al. (2024) | read-directly | yes | Limitations/Discussion (general evidence that model outputs depend on surface features of the prompt and that model comparisons can change with the template) |
| new2001_lexique1 | New et al. (2001), Lexique 1 | not accessible | no | Reference for the first version of Lexique |
| new2026_lexique4 | New et al. (2026), Lexique 4 | not accessible | no | Reference for the newer major version (a reviewer may ask why 3.83 was used) |

## Corrections and flags for the manuscript

1. The request calls New, Pallier, Brysbaert & Ferrand (2004) "Lexique 3". The paper with that author list in Behavior Research Methods, Instruments, & Computers 36(3), 516-524 is titled "Lexique 2" (doi 10.3758/BF03195598, Crossref). The Lexique 3 manual tells users to cite that paper together with New et al. (2001) and to state the version. The reference list of Primpied et al. (2022) repeats the same kind of mislabel; do not copy it. Lexique 4.00 (2026) now exists, so a reviewer may ask why 3.83 was used (new2004_lexique2).
2. The HarmoS accord has no "H" labels; it numbers years as ordinals. "5H" is cantonal and PER usage (Fribourg page), and "5P" is Vaud and Geneva usage (harmos2007, fr_cycle2, vd_deroulement, ge_primaire).
3. No page I read says in words that 5P and 5H are the same school year. The equivalence is an [inference] from identical structure (cycle 2 = years 5 to 8, ages 8 to 12 on all three cantonal pages). It needs a source before it is stated as fact. The CIIP and PER documents that would carry it were blocked.
4. The French label "5e" is not supported by any page I read (only CE2 and 6e are). Eurydice's secondary page was refused, and the ministry pages did not load.
5. Oh et al. (2026): the text I read is the arXiv v2 preprint, not the npj Artificial Intelligence PDF. The "exceed the target grade" sentence is background citing Rooein et al., not their own measured result.
6. Rooein et al. (2023): Section 2 says five models; four are described and analysed. ChatGPT rows barely move with age, GPT-3 rows do move; state results per model.
7. Brysbaert et al. (2018): I read the accepted manuscript, not the published pages. The Zipf definition is attributed there to van Heuven et al. (2014), which I could not open.
8. Year ambiguity: Mesmer (online 2024-01-02, volume 38(1)) and Li et al. (online 2024-12-13, BJET 56(3)). The APA year follows the journal volume; I could not verify it.
9. Kandel & Moles (1958): the formula is known to me only as printed in Primpied et al. (2022); the original was not found.
10. The EPFL survey (931 teachers) covers high-school and private-school teachers in Vaud, not primary teachers.

## A. Closest prior work (LLMs, grade, age or level prompts, readability of outputs)

Order: first the works I read in full text (including three I added because the listed ones could not be read), then the works I could only read in part or not at all.

### rooein2023 — Rooein, Cercas Curry & Hovy (2023)
- APA 7: Rooein, D., Cercas Curry, A., & Hovy, D. (2023). *Know your audience: Do LLMs adapt to different age and education levels?* arXiv. https://arxiv.org/abs/2312.02065
- Access label: read-directly (arXiv v1, 4 Dec 2023, full text via alphaXiv `get_paper_content`, fullText=true). The arXiv abstract page lists v1 only and no journal reference or DOI (WebFetch of arxiv.org/abs/2312.02065, 2026-11-01). Cite as a preprint.
- What I read: whole paper including Abstract, 1 Introduction, 2 Methodology (2.1-2.3), 3 Results (3.1-3.3), 4 Discussion, 5 Related Work, 6 Conclusion, Limitations, Appendix A.1-A.3.
- Passages
  1. Abstract. Four LLMs (two commercial, two open-source) answer science questions when prompted for different age groups and education levels; readability is compared with the recommended level for each group. Quote: "current LLMs have set readability ranges and do not adapt well to different audiences" (abstract; the sentence goes on to say that this holds even when the models are prompted).
  2. 2.1-2.2. Readability = Flesch Reading Ease (FKRE), with FKGL for grade mapping; 100 science questions; prompt templates for age (for example "for an 11-year-old"), education level (for example a college-graduate audience), difficulty, and kid/adult; Table 1 maps ages 11-23 to US grades.
  3. 3.1 and Table 4. ChatGPT mean FKRE barely moves with requested age: 17.31 (11 years), 17.48 (22-23 years), 17.25 (no target). Quote (3.1): "a particular “style” that is largely independent of prompting for age or education level". Appendix A.2 gives t-tests of each target against the no-target condition; all 20 listed p-values are above .05, and the table does not say whether models are pooled.
  4. 3.2 and Table 7. Average share of responses inside the recommended FKRE range is about 15% (Table 7, "Average" row: 14.65 / 15.70 / 14.75 / 14.60 by model).
  5. Limitations (last page). FKRE/FKGL were designed for English and the US school system and "are unlikely to translate without adaptation" to other countries, languages and school systems.
- Relevance: Introduction (earlier null result for age/education prompts) and Discussion (our finding that Haiku largely ignores the grade is consistent with a model-specific default register; our main result differs because stronger models do respond). Also the Limitations passage supports not transferring US formulas to French/Swiss grades.
- How it differs from ART 5: English; US grade labels; science question answering, not reading texts for pupils; 2023 models (gpt-3.5-turbo, text-davinci-003, T0, Flan-T5); surface formula (Flesch) not lexical frequency; no contrast between grade labels and age.
- Flags: (a) Section 2 says "33,600 prompt-response pairs from five models over 4 runs" while four models are described and analysed; do not repeat the "five" figure. (b) The claim that readability barely changes is true for the ChatGPT rows of Table 4; GPT-3 rows in Table 4 do decline from 41.86 (age 11) to 32.82 (age 22-23), so state it per model.
- Citable: yes (preprint).

### huang2024 — Huang, Wei & Huang (2024)
- APA 7: Huang, C.-Y., Wei, J., & Huang, T.-H. K. (2024). *Generating educational materials with different levels of readability using LLMs* [Workshop paper]. In2Writing 2024, Honolulu, HI, United States. arXiv:2406.12787. https://arxiv.org/abs/2406.12787
  (Venue as printed on the paper: "In2Writing 2024, May 11, 2024, Honolulu". I did not verify the full workshop title or a proceedings entry; cite it as an arXiv preprint presented at that workshop.)
- Access label: read-directly (arXiv v1, 18 Jun 2024, full text via alphaXiv). Authors' affiliations on the paper: MetaMetrics Inc. (Lexile) and Pennsylvania State University.
- What I read: whole paper (Abstract, 1 Introduction, 2 Related Work, 3.1-3.5, Table 1, Section 4, Section 5, Appendix A prompts). Page numbers are not recoverable from the text extraction, so locations are by section.
- Passages
  1. Abstract and 3.4. "Leveled-text generation": rewrite a source text to a target Lexile level; GPT-3.5, LLaMA-2 70B and Mixtral 8x7B, zero-shot and few-shot; 100 test texts from a leveled corpus.
  2. 3.5, Table 1. Mean absolute error between requested and obtained Lexile ranges from 172.9 (LLaMA-2 70B, 1-shot) to 257.6 (GPT-3.5, zero-shot); proportion within +-50 Lexile of the target is 11.00% to 22.22%.
  3. 3.5 text and Figure 2 caption. Results skew above the requested level. Quote: "tend to skew higher than the intended scores" (Figure 2 caption).
  4. 3.1. Lexile guidance quoted by the authors: for early-level learners (below about grade 4 / 750L) readability depends on many features (decodability, information load, phonetics); for upper-level learners readability "mostly relies on word frequency and sentence length" (citing Fitzgerald et al., 2015 and 2016, which I have not read).
  5. 3.5. Few-shot examples beat zero-shot, which the authors read as showing the target concept "does not inherently exist" in the models (paraphrase; check wording before quoting).
  6. Section 4. Models shorten the text regardless of the direction requested (825 words originally, 350-600 words in output) and edit unevenly.
- Relevance: Introduction (leveled-text generation overshoots the requested level) and Method/Limitations (for young readers word frequency is only one of several difficulty features, so a frequency measure is a partial index).
- How it differs from ART 5: English; Lexile (proprietary scale) with a numeric target; rewriting of an existing text rather than generating from a grade label; 2023-24 models; workshop paper (preprint); no grade-label or age contrast.
- Citable: yes (preprint / workshop paper).

### oh2026 — Oh, Whang, Evans & Wang (2026)
- APA 7: Oh, J., Whang, S. E., Evans, J., & Wang, J. (2026). Classroom AI: Large language models as grade-specific teachers. *npj Artificial Intelligence, 2*(1), Article 28. https://doi.org/10.1038/s44387-026-00081-7
  Bibliographic data from Crossref via WebFetch (volume 2, issue 1, article 28, issued 2026-03-03, licence CC BY-NC-ND 4.0).
- Access label: read-directly, but the text I read is the arXiv v2 preprint (arXiv:2601.06225v2, 6 Mar 2026, which states "This paper was published in npj Artificial Intelligence (2026)"), not the journal PDF. I did not open the Nature page. Wording in the journal version may differ; re-check before quoting.
- What I read: Abstract, Introduction, Results (Compatibility, Accuracy, Perplexity), Methods (Question Generation, Answer Generation, Readability Metrics Integration), Supplementary C.3, C.4, C.5, Table 2 (base-LLM output distribution) and reference list. Figures 2 and 6 are images and could not be read numerically.
- Passages
  1. Introduction, p. 1. Quote: "generate responses that systematically exceed the target grade’s comprehension level" (sentence: even with explicit prompts that name the 3rd grade). The sentence is background; in the text the preceding claim cites Rooein et al. (2023) as reference [17]. I did not find a table or sentence in the text extraction that reports their own prompted-3rd-grade result as a number.
  2. Supplementary C.5. Their Table 2 compares grade-level output distributions of base LLMs (GPT-4o, GPT-4o-mini, LLaMA 3.x, Qwen 2.5, Gemma 2, Phi 4, Mixtral); the text says current models "tend to output with higher-grade readability". Most output mass falls in the Middle/High bands (for example LLaMA 3.1:70B on D_SQ2: 26.73% Middle, 44.47% High). I could not tell from the text whether these base-LLM runs used a grade-specific prompt, so do not use these numbers as evidence of overshoot under a stated grade.
  3. Methods, Answer Generation. Their data-generation prompt names US grade levels (elementary 1st, 3rd and 5th grade, middle-school 7th grade, high-school 10th grade, and college) and a maximum sentence length.
  4. Results, Compatibility. Fine-tuned grade-specific models raise the share of outputs at the intended grade band by 35.64 percentage points on average over the prompt-based baseline.
- Relevance: Introduction (state-of-the-art statement that prompted grade labels yield above-target text; their own contribution is fine-tuning, not auditing prompt wording).
- How it differs from ART 5: English; US grade bands; answers to open questions (explanations), not reading texts; seven readability formulas combined; fine-tuning of open models; no HarmoS/P label contrast; no age-versus-label comparison.
- Flags: arXiv title capitalisation differs from the journal title only in case; cite the journal version. Citable status limited to what the authors state in the Introduction, not as their measured result.
- Citable: yes, for the stated claim and the method; see caveat 1.

### imperial2023 — Imperial & Tayyar Madabushi (2023) [added by me; not on the original list]
- APA 7: Imperial, J. M., & Tayyar Madabushi, H. (2023). Flesch or fumble? Evaluating readability standard alignment of instruction-tuned language models. In *Proceedings of the Third Workshop on Natural Language Generation, Evaluation, and Metrics (GEM)* (pp. 205-223). Association for Computational Linguistics. https://aclanthology.org/2023.gem-1.18/
- Access label: read-directly (PDF pages 1, 2, 4-8, 14-16 of the proceedings pagination 205-220, via alphaXiv `answer_pdf_queries` returning raw page text). Pages 3 and 9-13 (pp. 207, 213-217) were not returned.
- Passages
  1. p. 206 (2.1 Background). Grade-level prompts of the form "Write a story for second-grade readers." are suggested to teachers by educator blogs (Staake, 2023; Herft, 2023), and the paper tests that assumption.
  2. p. 208-209 (3.2). For story completion targeting Grade 2 (acceptable range 1 < FKGL < 3) no model in any prompt condition reached the range. ChatGPT (GPT-3.5-Turbo) mean FKGL (SD): 8.832 (1.549) with no specification, 5.155 (1.087) when the grade is named, 5.224 (1.060) with grade and framework, 4.567 (1.128) with description (Table 3, p. 218).
  3. p. 210 (CEFR). ChatGPT and Dolly reach 0-13% accuracy; the authors report that outputs were "one level higher than the target level" (B1 instead of A2) in over 90% of cases.
  4. p. 211-212 (4.2). Simplification to A2: ChatGPT FKGL 9.570 -> 5.285 -> 5.390 -> 5.210 as the prompt gets more specific (Table 4, p. 218); the authors recommend specifying the reading level and the assessment framework.
- Relevance: Introduction and Discussion (naming a level shifts output toward easier text but leaves it above target; level label wording matters). Method: they use FKGL and a CEFR classifier, not a frequency measure.
- How it differs from ART 5: English; FKGL and CEFR classifier; story completion and simplification from a given text; Grade 2 / A2 targets only; six 2023 models; no age-versus-label contrast; no French.
- Citable: yes.

### ripoll2025 — Ripoll y Schmitz & Sonnleitner (2025)
- APA 7: Ripoll y Schmitz, L. M., & Sonnleitner, P. (2025). Evaluating AI-generated vs. human-written reading comprehension passages: An expert SWOT analysis and comparative study for an educational large-scale assessment. *Large-Scale Assessments in Education, 13*, Article 20. https://doi.org/10.1186/s40536-025-00255-w
  (Author surname printed as "Ripoll Y Schmitz" in the article header; the form "Ripoll y Schmitz" in the request was kept. Check the form the journal uses in its own reference export.)
- Access label: read-directly for PDF pages 1, 6, 13, 14, 16-19, 21-24 of 29 (open-access PDF, raw page text via alphaXiv). Pages 2-5, 7-12, 15, 20 and 25-29 (including Appendix A prompts and the limitations paragraph) were NOT read; two further attempts returned a JavaScript error page. The WebFetch HTML extraction (first 100,000 of 106,051 characters) was used only for the section outline.
- Passages
  1. p. 1 (Abstract). GPT-4 (ChatGPT) is used to generate German reading comprehension texts, narrative and informative, for large-scale assessment in Luxembourg's multilingual setting; mixed methods; N = 89 reviewers in a blinded online review.
  2. p. 13-14. Aim includes judging suitability "for the reading-levels of fifth-graders in Luxembourg" (paraphrase; the sentence is in RQ2 text); texts were prompted directly in German; four CustomGPT configurations (narrative/informative x zero-shot/one-shot); six texts shown (two human-written, four GPT-4).
  3. p. 16 (partial sentence; its beginning is on the unread p. 15). The sentence states that readability prompts including a word limit, the sample text (one-shot) and the target group's age and grade level were expected to regulate the readability of the output. The exact prompt wording is in Appendix A, which I did not read.
  4. p. 16-17. Quality was measured with fifteen Likert statements on readability, correctness, coherence, engagement, appropriateness; no automatic readability or lexical measure appears on the pages I read.
  5. p. 17-19, 22-23. All six texts had mean ratings above 4 of 5; human-written narrative rated higher than the AI narratives on readability; the one-shot informative text was rated higher than the human informative text.
- Relevance: Introduction (an assessment-development use of GPT-4 for primary-grade reading texts in a European multilingual system) and Discussion (human ratings versus the automatic lexical audit used here).
- How it differs from ART 5: German, Luxembourg grade 5; one model; six texts; human quality ratings; one prompt wording; no automatic lexical/readability index (pages read); no label or age contrast.
- Citable: yes for the points above (pages named); not for any claim about the unread pages.

### trott2024 — Trott & Rivière (2024), added source (not on the request list)
- APA 7: Trott, S., & Rivière, P. D. (2024). *Measuring and modifying the readability of English texts with GPT-4* (arXiv:2410.14028v1). arXiv. https://arxiv.org/abs/2410.14028
  (A search result listed an ACL Anthology page with the identifier 2024.tsar-1.13 and the same title; I did not open it, so I give no workshop name or pages.)
- Access label: read-directly (arXiv v1, all 9 pages of text plus references and appendix, via alphaXiv, 2026-11-01). Preprint; peer-review status of this version not checked.
- Passages (page numbers of the arXiv PDF)
  1. Abstract and p. 1. On 4,724 English excerpts, zero-shot GPT-4 Turbo and GPT-4o mini readability ratings correlated r = 0.76 and r = 0.74 with human judgments; in a pre-registered human experiment (N = 59) GPT-4 Turbo made text easier or harder as instructed.
  2. p. 2, Section 2. Prior work shows LLMs move readability in the requested direction "though not necessarily to the desired text level" (quote attributed by the authors to Liu et al., 2023).
  3. p. 3, Section 3.4. Mean log word frequency, concreteness and age of acquisition together explained about 36% of the variance in human readability judgments (R2 = 0.36), each predictor significant; GPT-4 ratings explained more (about 58%). Used here as evidence that average word frequency is one partial predictor of readability, not the whole of it.
  4. p. 4, Section 4.4, and p. 5, Section 5. Easy-version excerpts were rated easiest (M = 4.48) and hard-version least readable (M = 2.5); the modified text's readability still correlated with the original's (Figure 5).
  5. p. 5-6, Section 6 (Limitations). One dataset, 100 excerpts, one model, no faithfulness check, and readability depends on audience and goal (the authors name "school-aged children vs. professionals").
  6. p. 8, Appendix A.1. The prompts say only to make the text easier or harder; they name no grade, age or school label.
- Relevance: Method (lexical frequency as a partial index of readability; the Brysbaert and New 2009 English frequency norm is the one used for the frequency predictor, p. 3) and Discussion (direction is controlled, level is not; construct depends on audience).
- Differences from ART 5: English; CLEAR excerpts rewritten by one model; adult online raters (mean age about 41); prompt gives no grade or age label; no cross-label comparison; no Swiss or French context.
- Citable: yes (as a preprint).

### farajidizaji2023 — Farajidizaji, Raina & Gales (2023), added source
- APA 7: Farajidizaji, A., Raina, V., & Gales, M. (2023). *Is it possible to modify text to a target readability level? An initial investigation using zero-shot large language models* (arXiv:2309.12551v2). arXiv. https://arxiv.org/abs/2309.12551
  (Version read: v2, dated 27 May 2024 on page 1. The text I read does not name a publication venue; I give none.)
- Access label: read-directly (arXiv v2, all 12 pages plus the appendix example).
- Passages (PDF page)
  1. p. 1, Abstract. A readability-controlled text modification task with 8 target levels, baselines with ChatGPT and Llama-2. Zero-shot prompting moves readability in the desired direction, but the final readability "remains correlated" with the source text's readability (the abstract's wording, quoted as two words).
  2. p. 5, Table 3 (prompts). Eight prompts, one per target Flesch level. Six name a US school or college level (or a professional audience) with a difficulty description; two (targets 65 and 95) also give an age, for example target 95 names 5th grade (US) and adds "easily understood by an average 11-year old student". The prompts differ in several words at once (level, difficulty adjective, sometimes an age), so the design cannot isolate a grade label from an age [inference].
  3. p. 6, Table 4 and Results. ChatGPT 1-step rank correlation with the target ordering 87.5 (x100), but RMSE about 19.4 Flesch points and classification accuracy about 23.1%; the authors read this as a sensible ranking without matching the exact target values.
  4. p. 7, Table 5. For every target level the readability of the generated text stays correlated with that of the source text; Pearson's pcc for ChatGPT 1-step runs from 36.9 to 69.7 across the eight targets (the table prints the source row as 100, so the scale is correlation x 100 [inference]).
  5. p. 9, Section 10 (Limitations). One dataset (CLEAR) and one readability formula (Flesch reading ease).
- Relevance: Discussion (LLMs order grade/age-style targets sensibly but do not hit absolute levels; label wording was part of the prompt, which supports looking at label wording as a factor).
- Differences from ART 5: English; paraphrase of an existing passage (source text supplies the content and its difficulty); targets named with US grade labels and Flesch scores; gpt-3.5-turbo and Llama-2-7B; no generation from a topic.
- Citable: yes (as a preprint).

### liu2025 — Liu, Lu, Jin, Kang & Zhang (2025), Reading and Writing
- APA 7: Liu, F., Lu, X., Jin, T., Kang, M., & Zhang, H. (2025). Does ChatGPT simplify texts like expert teachers? Linguistic features of simplified texts. *Reading and Writing*. Advance online publication 24 June 2025. https://doi.org/10.1007/s11145-025-10676-2 (volume and pages not shown on the pages I opened; Crossref record lists none).
- Access label: abstract-only. Springer article page opened via alphaXiv: it shows the abstract, notes, and the reference list, and offers the full text only to subscribers ("preview of subscription content"). Penn State record (pure.psu.edu) also abstract-only. Language of the texts is not stated in the abstract.
- What the abstract states (paraphrase): a comparable corpus of source texts, expert-simplified texts and three sets of ChatGPT-simplified texts (general, example and instructive prompts); 17 lexical, syntactic and cohesion features; significant differences between expert and ChatGPT texts on many features; more detailed prompts increased similarity.
- Relevance: Intro candidate (teachers' use of ChatGPT to prepare reading material), but only on the strength of the abstract.
- Citable: no (abstract-only). Method details (language, grades, lexical measures, direction of lexical differences) are unknown to me.

### watanabe2025 — Watanabe (2025), IJAIED
- APA 7: Watanabe, M. (2025). ChatGPT, can you make this text easier?: Investigating the utility of LLMs in easing text readability. *International Journal of Artificial Intelligence in Education, 35*(6), 3922-3942. https://doi.org/10.1007/s40593-025-00520-7 (bibliographic fields from the Crossref record, one author listed).
- Access label: abstract-only (abstract as listed in a Consensus search result). Full text not opened: Springer article page (client error), Springer PDF (JavaScript wall), doi.org (redirect not followed), Elsevier linking hub (empty), alphaXiv (no output; no title match in its index). Crossref lists a CC BY-NC-ND 4.0 licence for the version of record from 2026-04-22, so an open copy may exist, but none loaded for me.
- What the abstract states (paraphrase): Experiment 1, 30 texts rewritten by ChatGPT 4 to be "more readable"; Experiment 2, the same 30 texts rewritten by ChatGPT 4o and MagicSchool.ai for students at a particular grade; NLP measures of linguistic sophistication, cohesion and holistic readability; only the models and prompts of Experiment 2 showed evidence of easing readability.
- Relevance: Intro candidate (a named grade in the prompt works better than "more readable").
- Citable: no (abstract-only). Which grade, language and measures were used is not stated in the abstract.

### patel2023 — Patel et al. (2023), JCAL
- APA 7: Patel, N., Nagpal, P., Shah, T., Sharma, A., Malvi, S., & Lomas, D. (2023). Improving mathematics assessment readability: Do large language models help? *Journal of Computer Assisted Learning, 39*(3), 804-822. https://doi.org/10.1111/jcal.12776 (fields from Crossref).
- Access label: full-text-extracted, NOT read-directly. The TU Delft repository file (final published version, per the repository record) was processed by the web-fetch tool's extractor, which returned section headings and figures; the alphaXiv reader failed twice ("The user aborted a request"), so I have not seen the raw text. Page numbers below are the extractor's and are unchecked. Wiley pages failed (client error).
- What the extraction reports
  1. Method (about pp. 4-9): 250 grade 3-5 word problems from EngageNY, GPT-3 (davinci-instruct-beta-v3) with seven prompt conditions (rephrase one or two grade levels lower, "second-grade reading level", few-shot), 4,992 usable outputs; 16 readability metrics from CTAP in four groups including lexical sophistication (age of acquisition, imageability, concreteness) and similarity filters.
  2. Results (about pp. 10-14): most metrics moved as expected, outputs were noisy, and only the filtered 1-4% were meaningful simplifications.
  3. Limitations (about pp. 13-16): noisy output, need for human review, short problems for formulas that need about 300 words.
- Relevance: Intro/Discussion (an earlier, GPT-3-era grade-targeted prompt study; prompts named grade levels). Not for numbers.
- Citable: no (verify against the PDF first).

### mesmer2024 — Mesmer (2024/2025), Reading and Writing
- APA 7: Mesmer, H. A. E. (2024). Exploring the frequency contours in close reading texts. *Reading and Writing, 38*(1), 1-35. https://doi.org/10.1007/s11145-023-10493-5 (Crossref: issued 2024-01-02, volume 38, issue 1; the print year is not shown in what I read, so the year may need to change to match the volume).
- Access label: abstract-only (Springer preview page via the web-fetch extractor; full text paywalled; the extractor gave the abstract in summary form, so the wording below is a paraphrase to be checked against the page).
- What the abstract states (summary): word frequency is common in readability formulas, and a single mean is a poor summary of a skewed variable; 249 close-reading texts for grades 2-8 (mean about 640 words) analysed with a new frequency metric; frequency curves nearly identical in shape across grades and text types, with four frequency strata; the rarest words are often "rare but not rich"; narratives often contain one very rare word that can distort the mean.
- Relevance: Method/Limitations candidate (directly concerns using mean word frequency as a text-difficulty index in primary texts). This is the closest source to the ART 5 measure and it could not be read past the abstract.
- Citable: no (abstract-only). Strongly recommended to obtain through a library before submission.

### li2024 — Li, Xing, Li, Zhu & Oh (2024), BJET
- APA 7: Li, H., Xing, W., Li, C., Zhu, W., & Oh, H. (2024). Are simpler math stories better? Automatic readability assessment of GAI-generated multimodal mathematical stories validated by engagement. *British Journal of Educational Technology, 56*(3), 1092-1117. https://doi.org/10.1111/bjet.13554 (Crossref: issued 2024-12-13; the title ends "validated by engagement" per the extractor, which cut it for quote length).
- Access label: abstract-only (Crossref abstract, passed through the extractor as a summary). Wiley pages failed (client error).
- What the abstract states (summary): an automated method to assess AI-generated math stories with images, scoring text-image coherence and text readability and relating them to student engagement (reading time, drawing-tool use); simpler vocabulary and connectives correlated with behavioural engagement.
- Relevance: Intro candidate only.
- Citable: no (abstract-only).

### nguyen2026 — Nguyen (2026), International Journal of TESOL Studies
- APA 7 (incomplete): Nguyen, N. (2026). Lexical profile of ChatGPT-generated reading materials targeting EFL learners across the CEFR levels. *International Journal of TESOL Studies*. (Volume, pages and DOI not found; author given name as "Nhat Nguyen" in a Consensus record.)
- Access label: abstract-only (Consensus search result). The journal site was refused by the fetch tool (provenance), and the search for an open copy returned nothing relevant.
- What the abstract states: six corpora of ChatGPT texts targeting CEFR A1 to C2 were profiled with RANGE and Nation's BNC/COCA 25,000-word-family lists; high-frequency words were the largest share at every level; texts for A1, A2 and B1 were less lexically demanding than B2, C1 and C2, but A1 and A2 texts required the same vocabulary sizes as B1 texts.
- Relevance: Intro/Discussion candidate (lexical profile of LLM texts by target level, English as a foreign language, CEFR labels). Closest in measure type (lexical frequency bands) to ART 5.
- Citable: no (abstract-only).

## B. Measure and method sources (Lexique, subtitle frequencies, Zipf scale, French frequency and text difficulty)

### new2004_lexique2 — New, Pallier, Brysbaert & Ferrand (2004), "Lexique 2"
- APA 7: New, B., Pallier, C., Brysbaert, M., & Ferrand, L. (2004). Lexique 2: A new French lexical database. *Behavior Research Methods, Instruments, & Computers, 36*(3), 516-524. https://doi.org/10.3758/BF03195598 (DOI and bibliographic data from Crossref via WebFetch, 2026-11-01).
- Access label: NOT ACCESSIBLE as full text. HAL copy (hal-02341287 and hal.science) sits behind an Anubis bot wall; the typeset.io copy returned a JavaScript wall; Semantic Scholar page returned no PDF URL. Not citable for its content. Citable only as a reference whose existence and title are confirmed by three sources I did read (Lexique 3 manual p. 2; Manulex paper p. 159; Manulex-infra reference list p. 588).
- FLAG FOR THE MANUSCRIPT: the request describes this 2004 paper as "Lexique 3". The 2004 Behavior Research Methods paper is titled "Lexique 2". The official Lexique 3 manual (p. 2) tells users to cite New et al. (2001) and New et al. (2004, "Lexique 2: A New French Lexical Database") and to name the version used. The film-subtitle frequencies of Lexique 3 are described in New et al. (2007) (next entry). Version 3.83 is cited in the manuscript, so cite the version number explicitly and use New et al. (2004) under its true title.
- Also verified (Crossref): Lexique 1 = New, B., Pallier, C., Ferrand, L., & Matos, R. (2001). Une base de données lexicales du français contemporain sur internet: LEXIQUE. *L'Année Psychologique, 101*(3), 447-462. https://doi.org/10.3406/psy.2001.1341. A newer major version exists: New, B., Pallier, C., Schalchli, G., Bourgin, J., & Gimenes, M. (2026). Lexique 4: A major upgrade of the Lexique French lexical database. *Behavior Research Methods, 58*(5). https://doi.org/10.3758/s13428-026-02967-5 (Crossref: issued 2026-04-24; I did not read it; the lexique.org README for Lexique 4.00 says frequencies come from a 316M-word subtitle corpus, via WebFetch extraction). A reviewer may ask why version 3.83 rather than 4.00 was used.
- Citable: no (content). Reference existence: yes.

### new2007_subtitles — New, Brysbaert, Véronis & Pallier (2007)
- APA 7: New, B., Brysbaert, M., Véronis, J., & Pallier, C. (2007). The use of film subtitles to estimate word frequencies. *Applied Psycholinguistics, 28*(4), 661-677. https://doi.org/10.1017/S014271640707035X (Crossref via WebFetch).
- Access label: abstract-only. Cambridge Core page opened via WebFetch (abstract displayed, full text paywalled, purchase "temporarily unavailable"). HAL copy (hal-02327556 and hal.science/hal-02327556/document) blocked by an Anubis bot wall.
- What the abstract states (WebFetch extraction of the abstract, quoted in short pieces): film subtitles as an approximation of word frequencies in human interactions; "a corpus of 52 million French words, coming from a variety of films"; subtitle-based measures "compared well" with other spoken and written frequencies and explained extra variance in lexical-decision times beyond French written frequencies.
- Cross-check from a source I did read: the Lexique 3 manual (p. 6-7) says the film corpus has 9,474 films or series seasons and 50 million words (not 52), in four sub-corpora, and that a different subtitle corpus has been used since Lexique 3.40 (see next entry). Do not state corpus size for version 3.83 from this article alone.
- Citable: no (abstract-only).

### lexique3manual — New & Pallier, Manuel de Lexique 3 (document version 3.2)
- APA 7: New, B., & Pallier, C. (n.d.). *Manuel de Lexique 3* (Document version 3.2) [Documentation]. Lexique.org. https://lexique.org/_documentation/Manuel_Lexique.3.2.pdf
  (Authors as printed on the cover: Boris New, Christophe Pallier. No date printed. Version 3.2 of the manual, not of the database.)
- Access label: read-directly (PDF pages 1-15, 17, 21-23 via alphaXiv `answer_pdf_queries`, raw page text; pages 16, 18-20 not returned; the manual's conclusion on pp. 19-20 was not read).
- Passages (page = PDF page)
  1. p. 2, section Comment citer Lexique ? Users must state which Lexique version they used; the manual lists New et al. (2001) and New et al. (2004, Lexique 2 : A New French Lexical Database). Quote: "bien citer la version de Lexique que vous avez utilisé".
  2. p. 6, 2.1. Book sub-corpus: 218 literary texts (novels) published 1950-2000 from Frantext, 14.7 million items. 2.2. Film corpus: subtitles of 9,474 films or series seasons, 50 million words, in four sub-corpora (French films 1.9 M words; Anglo-Saxon films 26.5 M; Anglo-Saxon films and series 19.5 M; non-Anglo-Saxon European films 2.5 M). The manual warns that two different subtitle corpora were used before version 3.40 and from version 3.40 on; the passage I read does not say which of the two the 9,474-film figure describes.
  3. p. 7. Frequencies are averaged over the four sub-corpora; subtitles are closer to spoken language and had an advantage over book frequencies in explaining lexical-decision variance (paraphrase, no quote).
  4. p. 11-12. `freqlemfilms2` = lemma frequency per million in the film corpus, the sum of the frequencies of the inflected forms of each lemma; it changed from version 3.40 (bigger corpus, averaging over sub-corpora). `freqlemlivres` = lemma frequency per million in the book corpus (division by 14.8; 14.7 M words).
  5. p. 5. The manual names Manulex (CP-CM2, 1.9 M words) and Novlex (CE2, 417,000 words) as school-textbook-based French databases and says Lexique 1 and 2 frequencies were built from Frantext texts published after 1950.
  6. p. 17, Table 7 (descriptive statistics of the numeric fields; the table does not state the database version). Lemma film frequency: median 1.02, mean 64.83, 3rd quartile 7.71 per million; maximum 33,959.88. The distribution is heavily right-skewed.
- Relevance: Method (what film and book frequencies are, how lemma frequency is defined) and Limitations (both corpora are adult-directed: novels 1950-2000 and subtitles dominated by Anglo-Saxon films; film frequencies from a corpus where French-language films are 1.9 of 50 M words in the passage read).
- Caveat: this is the manual for Lexique 3 at document version 3.2. The 3.83 database may differ in corpus and field details; check against the 3.83 README before stating numbers for 3.83.
- Citable: yes for the statements above, labelled as the version-3.2 manual.

### manulex2004 — Lété, Sprenger-Charolles & Colé (2004), MANULEX
- APA 7: Lété, B., Sprenger-Charolles, L., & Colé, P. (2004). MANULEX: A grade-level lexical database from French elementary school readers. *Behavior Research Methods, Instruments, & Computers, 36*(1), 156-166. https://doi.org/10.3758/BF03195560
  (Volume, issue, pages, issue date 2004-02 and DOI confirmed in the Crossref record through a title query, 2026-11-01.)
- Access label: read-directly (Springer PDF pages 156-162 and Appendix p. 165 via alphaXiv; PDF pages 2, 8, 9, 11 not returned).
- Passages
  1. Abstract (p. 156). Grade-level frequency lists of 48,886 non-lemmatised and 23,812 lemmatised entries from 1.9 million words of 54 French elementary-school readers; levels G1, G2, G3-5 and G1-5; statistics F (frequency), D (dispersion), U (estimated frequency per million) and SFI (standard frequency index).
  2. p. 159. G1 = 6-year-olds, G2 = 7-year-olds, G3-5 = 8- to 11-year-olds; 54 readers (13, 13 and 28) chosen to cover 75% of 1996 sales; the sample is described as reasonably representative of printed French materials for children aged 6-11.
  3. p. 159-160. The authors describe LEXIQUE (New et al., 2001) as the reference tool for French psycholinguistics and note that "frequency" reflects several factors, one of which is conceptual difficulty (paraphrase of the Nagy & Anderson point).
  4. p. 161-162, Table 3. Mean lemma SFI: G1 48, G2 45, G3-5 39, G1-5 37; LEXIQUE 38. The text: from G3-5 on "values approach those of the LEXIQUE database", and a lower mean SFI reflects higher word difficulty for a schoolchild (paraphrase).
  5. p. 161. SFI is a log scale of U (SFI = 10 log10 U + 40; an SFI of 40 = once per million words). It is the older analogue of the Zipf scale (Zipf = log10 frequency per billion words = log10 fpm + 3, see brysbaert2018).
- Relevance: Limitations and Discussion. (a) Grade-specific French frequency norms exist (France, CP to CM2, readers of the mid-1990s); the present measure instead uses adult-directed film/book frequencies and calibrates years with each model's own age-only texts. (b) Because G3-5 lexical statistics approach those of the adult database, a Lexique-based measure may be less sensitive to differences among upper-primary texts than to differences between early and late primary texts [inference, not stated by the authors].
- How it differs from ART 5: French of France, readers sold in 1996, frequencies by school grade (CP, CE1, CE2-CM2), no Swiss HarmoS grades.
- Citable: yes.

### peereman2007 — Peereman, Lété & Sprenger-Charolles (2007), Manulex-infra
- APA 7: Peereman, R., Lété, B., & Sprenger-Charolles, L. (2007). Manulex-infra: Distributional characteristics of grapheme-phoneme mappings, and infralexical and lexical units in child-directed written material. *Behavior Research Methods, 39*(3), 579-589. https://doi.org/10.3758/BF03193029
  (Volume, issue, pages 579-589, issue date 2007-08 and DOI confirmed in the Crossref record by direct DOI lookup, 2026-11-01. An earlier draft of this note gave pages 593-603; that was wrong.) [added by me]
- Access label: read-directly (PDF pages 1, 2, 4, 5, 6, 10 = journal pp. 579-583 and 588).
- Passages
  1. p. 579. Most existing French linguistic databases are based on adult-directed written material (naming New et al., 2004) or give child norms that "do not reflect current usage", which the authors say makes them unsuitable for studying literacy acquisition (paraphrase; the 2004 reference is Lexique 2, book-based).
  2. p. 580. Quote: "word frequency is obviously not the sole factor of performance".
  3. p. 582. Manulex: 1.9 million words, 54 readers, wordform lexicon 48,886 entries, lemma lexicon 23,812 entries; levels G1, G2, G3-5.
- Relevance: Limitations (a published argument that adult-corpus frequencies are not child-based and that frequency is one factor among others).
- Citable: yes (for the pages listed).

### brysbaert2018 — Brysbaert, Mandera & Keuleers (2018), used here as the readable source for the Zipf scale
- APA 7: Brysbaert, M., Mandera, P., & Keuleers, E. (2018). The word frequency effect in word processing: An updated review. *Current Directions in Psychological Science, 27*(1), 45-50. https://doi.org/10.1177/0963721417727521 (bibliographic data from Crossref via WebFetch).
- Access label: read-directly, but the text I read is the 15-page accepted manuscript titled "The word frequency effect in word processing: A review update" ("To be published in Current Directions in Psychological Science"), obtained from a university corpus-server copy (corpus.bfsu.edu.cn) through alphaXiv. Check pagination and wording against the published version before quoting.
- Passages (manuscript page numbers)
  1. p. 6. The Zipf scale was proposed by van Heuven et al. (2014); "Zipf = log10 (frequency per billion words)". The scale runs from 1 (1 per 100 million words) to 6 (1000 per million words); 1-3 = low-frequency words, 4-6 = high-frequency words.
  2. p. 5-6. Frequency per million (fpm) gives wrong intuitions because the frequency effect is logarithmic; the Zipf scale is offered as an alternative.
  3. p. 3. Word frequency typically explains some 30-40% of the variance in word recognition tasks (citing Brysbaert et al., 2016).
  4. p. 4. The best norms are those based on language participants are likely to have been exposed to; for undergraduates, television-subtitle corpora were best; for older participants, book-based measures are sometimes better. Corpora should be large (not below 20 million words), p. 5.
  5. p. 8-9, Figure 2. The word frequency effect appears in different frequency ranges for people with different language exposure (a low-vocabulary reader shows it mainly for high-frequency words, Zipf above 4) [relevant to children].
- Relevance: Method (definition of the Zipf scale and its interpretation) and Limitations (frequency norms and exposure; children have different exposure).
- Why it stands in: van Heuven et al. (2014) could not be opened (see next entry).
- Citable: yes (manuscript version; verify against the published version).

### vanheuven2014_subtlexuk — van Heuven, Mandera, Keuleers & Brysbaert (2014), SUBTLEX-UK
- APA 7: van Heuven, W. J. B., Mandera, P., Keuleers, E., & Brysbaert, M. (2014). SUBTLEX-UK: A new and improved word frequency database for British English. *Quarterly Journal of Experimental Psychology, 67*(6), 1176-1190. https://doi.org/10.1080/17470218.2013.850521 (volume, pages and DOI from the Tilburg University repository record, WebFetch).
- Access label: NOT ACCESSIBLE as full text. Repository records at Nottingham (eprints 2947, worktribe output 721845) and Tilburg list no PDF; the worktribe file URL failed to load via alphaXiv; the Taylor & Francis/informahealthcare page failed to load. The definition of the Zipf scale is therefore taken from brysbaert2018 (which attributes it to this paper).
- Citable: no (content). Citable as the attributed origin of the Zipf scale only through brysbaert2018 p. 6.

### kandelmoles1958 — Kandel & Moles (1958), French adaptation of the Flesch index (SECONDARY reading only)
- APA 7: Kandel, L., & Moles, A. (1958). Application de l'indice de Flesch à la langue française. *Cahiers d'Études de Radio-Télévision, 19*, 253-274. (Title and journal as printed in Primpied et al., 2022, ref. [22]; volume pages 253-274 as printed in the reference list of Javourey-Drevet et al., 2022, p. 508. Both are secondary sources; I did not find or open the original.)
- Access label: NOT ACCESSIBLE (original). Secondary: read-directly in primpied2022 (next entry), which states the formula and the score bands.
- Formula as printed in the secondary source (primpied2022, p. 4, Equation 3.1): KM score = 207 - 1.015 x MLS - 0.736 x MNS, with MLS = "Mean Length of Sentences" (Table 3) and MNS = "Mean Number of Syllables" (named in the text on p. 3). The pages I read do not state the units; in the original Flesch formula they are words per sentence and syllables per word [inference]. The coefficients are therefore NOT verified against the 1958 original.
- Score bands as printed in primpied2022, p. 7, Table 7: 90-100 very easy, 80-90 easy, 70-80 fairly easy, 60-70 standard, 50-60 fairly difficult, 30-50 difficult, 0-30 very difficult.
- Citable: the existence of the 1958 reference: yes (through primpied2022). The formula: only with the wording as reported by Primpied et al. (2022).
- Note for the manuscript: ART 5 uses mean Zipf frequency of content lemmas, not a Flesch-type formula; K&M is relevant only if the manuscript mentions sentence-length/syllable readability as an alternative measure not used here.

### javourey2022 — Javourey-Drevet, Dufau, François, Gala, Ginestié & Ziegler (2022), French grade-2 text simplification
- APA 7: Javourey-Drevet, L., Dufau, S., François, T., Gala, N., Ginestié, J., & Ziegler, J. C. (2022). Simplification of literary and scientific texts to improve reading fluency and comprehension in beginning readers of French. *Applied Psycholinguistics, 43*, 485-512. https://doi.org/10.1017/S014271642100062X
  (Volume 43 and pages 485-512 as printed on the first page and in the citation line on the last page; the issue number is not printed on the pages I read, so none is given. First published online 31 January 2022; open access, CC BY 4.0.)
- Access label: read-directly (open-access PDF; PDF pages 1, 2, 5, 7-11, 18, 24, 25, 28 of 28, via alphaXiv; the remaining pages were not returned: method of participants, statistics, most of the discussion).
- Passages (journal page numbers)
  1. p. 485 (Abstract). 165 children in grade 2; manually simplified informative and narrative texts; reading fluency and comprehension were significantly better for simplified than normal texts; poor readers and children with weaker cognitive skills benefited more.
  2. p. 491-492, Materials. 10 narrative and 10 scientific texts (mean 243 words) taken from French school resources; simplification focused mainly on the lexical and syntactic levels, chiefly substituting "long and infrequent words by shorter and more frequent synonyms" (quote), with substitutes taken from Manulex (Lété et al., 2004) and ReSyf.
  3. p. 492-493, Text readability analysis. Variables were selected from a set of 406 readability variables (François, 2011); frequency variables "were calculated using Lexique3 (New et al., 2007)"; significant lexical differences concerned average frequency of nouns and adjectives and the 75th and 90th percentiles of the lemma frequency distribution.
  4. p. 494, Table 1. Simplified versus original texts: 75th percentile of lemma frequency 183.9 versus 119.4 (p < .001); mean frequency of noun lemmas 202.1 versus 177.1 (p = .015); standard deviations are large (for example 176.2 and 96.8). The table does not state the frequency unit in the rows I read.
  5. p. 492, Text readability analysis. The authors list Flesch (1948) and Kandel & Moles (1958) among the standard variables used in readability formulae; the reference list (p. 508) prints Kandel & Moles pages 253-274.
- Relevance: Method (a French study of beginning readers in which Lexique 3 lemma-frequency statistics differ between simplified and original texts that were made easier for children; supports using a Lexique-based frequency index as a partial correlate of text difficulty for young readers) and Limitations (the study used several lexical and syntactic variables, not one mean; children were in grade 2 in France, ages not stated on the pages read).
- Differences from ART 5: human (not LLM) simplification; France grade 2 (CE1), not Swiss 5H; many variables; frequency statistics from Lexique 3 with the film/book corpus not named in the passage read; reading outcomes measured on children.
- Caution: Table 1 shows that the simplification changed frequency statistics but the study does not show that mean frequency alone predicts comprehension; it does not report a regression of comprehension on frequency on the pages I read.
- Citable: yes (pages named above).

### primpied2022 — Primpied, Beauchemin & Khoury (2022), French document complexity
- APA 7: Primpied, V., Beauchemin, D., & Khoury, R. (2022). *Quantifying French document complexity* (arXiv:2208.12924v1). arXiv. https://arxiv.org/abs/2208.12924 (page 1 header: "The 35th Canadian Conference on Artificial Intelligence"; licence CC BY 4.0; the DOI field on page 1 reads "0", so no DOI).
- Access label: read-directly (all 13 pages via alphaXiv, 2026-11-01).
- Passages (page)
  1. p. 3, Section 3, Table 2 and text. Vocabulary-complexity metrics include a percentage of words absent from the Gougenheim fundamental dictionary and a unigram score "sorted by Lexique3 frequency"; the authors note that French equivalents of English word lists exist, naming the Gougenheim dictionary and the Lexique 3 list of lemmas and their probabilities of occurrence (paraphrase).
  2. p. 3-4, Table 4 and Equation 3.1. The Kandel and Moles formula is described as the French adaptation of Flesch reading ease and is printed as KM = 207 - 1.015 x MLS - 0.736 x MNS (see kandelmoles1958).
  3. p. 4, Section 4.1, and p. 5. A corpus of 118 French documents in 8 genres, chosen mostly in Canadian French, from children's stories to legal texts; the ranking of genres within tiers is "based on our intuition" (paraphrase of the authors' own caveat).
  4. p. 5, Section 4.2. The Kandel and Moles score falls steadily from simple to complex genres but with "too much overlap" between levels to classify a text on that value alone (paraphrase; the two quoted words are from the paper).
  5. p. 7, Table 8. As a baseline the Kandel and Moles score classified genres with accuracy 0.38, against 0.92 for a random forest over about 60 metrics.
  6. p. 11, Section 5. "None of these metrics can, by itself" capture text complexity (paraphrase: no single metric models the whole range).
  7. p. 12, reference [15] lists B. New, C. Pallier and L. Ferrand, with the title "Manuel de lexique 3", in Behavior Research Methods, Instruments, & Computers 36.3 (2005). That label does not match the Crossref record, which gives the 2004 paper as Lexique 2 (see new2004_lexique2). Example of the mislabelling that the request repeats.
- Relevance: Method/Limitations (French text complexity relies on several features and Lexique 3 frequency lists; one formula overlaps heavily between levels). Not about LLMs and not about primary-school levels.
- Citable: yes.

## C. Swiss school context (official texts and cantonal pages)

Reading method for this section: every page below was read as raw text through the alphaXiv reader (which returns the readable text of a web page or the page text of a PDF), on 2026-11-01. Quotes are copied from that text and kept under 15 words. Pages that returned a bot wall or nothing are listed under Blocked in search_log.md.

### harmos2007 — HarmoS intercantonal accord (CDIP, 14 June 2007)
- APA 7: Conférence suisse des directeurs cantonaux de l'instruction publique. (2007). *Accord intercantonal sur l'harmonisation de la scolarité obligatoire (HarmoS)* du 14 juin 2007 (version entrée en vigueur le 01.05.2010 pour le canton de Fribourg) [Texte légal 416.2]. https://fr.lexwork.naz.ch/fr/dta/416.2.pdf
  Second copy read for the signature block and the entry-into-force note: https://axl.cefan.ulaval.ca/EtatsNsouverains/suisse-accord_intercantonal2007.htm (Université Laval language-policy site; a re-publication, not an official source).
- Access label: read-directly. Fribourg legislation PDF: all 7 PDF pages. CEFAN copy: whole page.
- Passages (PDF page of the Fribourg copy; the PDF text separates the superscript e of ordinals from the number, as in 11 e année, and the quotes below restore it)
  1. p. 3, Art. 5 al. 1 (Scolarisation). Pupils start school at the age of four completed years, with 31 July as the reference day. Quote: "dès l'âge de 4 ans révolus (le jour de référence étant le 31 juillet)".
  2. p. 3, Art. 5 al. 2. In the first years of schooling ("enseignement préscolaire et primaire") children consolidate basic language learning; the time needed depends on each child's development (paraphrase).
  3. p. 3, Art. 6 al. 1-2. The primary degree lasts eight years and includes the école enfantine; secondary I normally lasts three. Quote: "Le degré primaire, école enfantine ou cycle élémentaire inclus, dure huit ans."
  4. p. 3, Art. 6 al. 4. Transition to secondary II after the 11th year of schooling. Quote: "Le passage au degré secondaire II a lieu après la 11e année de scolarité."
  5. p. 2, Art. 4 al. 1. The first foreign language is taught at the latest from the 5th year of schooling and the second from the 7th year (paraphrase; this is the reason why years 5 and 7 recur in cantonal pages).
  6. CEFAN copy, closing block. Signed at Berne on 14 June 2007 for the CDIP; a note says the CDIP committee decided on 7 May 2009 that the accord enters into force on 1 August 2009. The Fribourg copy says it entered into force for the canton of Fribourg on 1 May 2010.
- WHAT THE TEXT DOES NOT CONTAIN: in the 7 pages I read, school years are numbered as ordinals ("5e année de scolarité", "11e année"). The letter notation 1H-11H does not occur in the accord. The manuscript should attribute the numbering of years (1 to 11) and the entry rule to the accord, and the label "5H" to cantonal and PER usage (see below), not to the accord text.
- Relevance: Intro and Method (defines what "5H" refers to: the fifth year of schooling counted from entry at about four years; reference day for age).
- Citable: yes.

### vd_deroulement — Canton de Vaud, "Déroulement de l'école obligatoire"
- APA 7: État de Vaud, Direction générale de l'enseignement obligatoire et de la pédagogie spécialisée. (n.d.). *Déroulement de l'école obligatoire dans le canton de Vaud* [Page web]. https://www.vd.ch/formation/enseignement-obligatoire-et-pedagogie-specialisee/deroulement-de-lecole-obligatoire-dans-le-canton-de-vaud/ (no date printed; read 2026-11-01).
- Access label: read-directly (whole page; sections used: "Informations générales", "Premier cycle primaire (1P - 4P)", "Deuxième cycle primaire (5P - 8P)", "Degré secondaire (9S - 11S)").
- Passages
  1. Section Informations générales. Compulsory school in Vaud lasts eleven years in two degrees: primary (eight years in two cycles of four) and secondary I (three years). Children enter "à l'âge de 4 ans révolus au 31 juillet" under the law on compulsory teaching (LEO). Paraphrase for the rest.
  2. Section Premier cycle primaire (1P - 4P). Cycle 1 lasts four years, en principe (as a rule) for children aged 4 to 8.
  3. Section Deuxième cycle primaire (5P - 8P). Cycle 2 covers years 5 to 8. Quote: "Ce cycle accueille les enfants en principe âgés de 8 à 12 ans."
  4. "Degré secondaire (9S - 11S)". Cycle 3 = 9th to 11th years, ages 12 to 15.
- Notation shown: P for primary years (1P-8P) and S for secondary years (9S-11S) in Vaud; the same page also writes "5e année", "8e année". The letter H does not appear on this page.
- Relevance: Intro/Method (shows that "5P" in Vaud names the fifth year, the first year of cycle 2).
- Citable: yes.

### ge_primaire — Canton de Genève, "Bienvenue à l'école primaire"
- APA 7: République et canton de Genève. (2026). *Bienvenue à l'école primaire* [Page web]. ge.ch. https://www.ge.ch/node/11636 (page shows "Dernière mise à jour: 16 octobre 2026"; read 2026-11-01).
- Access label: read-directly (whole page).
- Passage ("L'essentiel en bref"): primary school in Geneva covers pupils aged 4 to 12 over eight years in two cycles. Quote: "le cycle moyen (5P à 8P) pour les élèves de 8 à 12 ans". The cycle élémentaire is 1P-4P, ages 4 to 8.
- Notation: P (1P-8P). The letter H does not appear on this page.
- Relevance: Intro/Method (Geneva uses the same P notation and the same age band for years 5-8 as Vaud).
- Citable: yes.

### fr_cycle2 — Canton de Fribourg, "Organisation et déroulement, Cycle 2" (and overview page)
- APA 7: Canton de Fribourg, Direction de la formation et des affaires culturelles. (2025). *École obligatoire - Organisation et déroulement, Cycle 2* [Page web]. fr.ch. https://www.fr.ch/formation-et-ecoles/scolarite-obligatoire/ecole-obligatoire-organisation-et-deroulement-cycle-2 (page shows "Dernière modification : 18.06.2025"; read 2026-11-01).
  Overview page also read: Canton de Fribourg, Direction de la formation et des affaires culturelles. (2026). *Écoles - la formation dans le canton de Fribourg* [Page web]. https://www.fr.ch/formation-et-ecoles/scolarite-obligatoire/ecoles-la-formation-dans-le-canton-de-fribourg ("Dernière modification : 24.03.2026").
- Access label: read-directly (both pages whole).
- Passages
  1. Cycle 2 page, section Chapeau. Cycle 2 lasts four years and is "en principe fréquenté par des élèves âgé-e-s entre 8 et 12 ans"; pupils start German or French in 5H and English in 7H (paraphrase).
  2. Cycle 2 page, section Organisation. School years are counted 1H to 11H across the three cycles. Quote: "années de scolarité 1H à 11H (du premier au troisième cycle)".
  3. Cycle 2 page, section Grilles horaire. 28 lessons per week in years 5 to 8 (the page writes de la 5 à la 8H).
  4. Cycle 2 page, "Plans d'études". The French-speaking part of Fribourg uses the Plan d'études romand (PER); the German-speaking part uses Lehrplan 21.
  5. Overview page. Compulsory school has 3 cycles and lasts 11 years; "Les enfants y entrent dès l'âge de 4 ans".
- Notation: H (1H-11H). This is the only page of the three cantonal pages read that uses the H label.
- Relevance: Intro/Method (source for the "5H" label and for the age band of cycle 2).
- Citable: yes.

### vd_per — Canton de Vaud, "Plan d'études romand (PER)"
- APA 7: État de Vaud, Direction générale de l'enseignement obligatoire et de la pédagogie spécialisée. (n.d.). *Plan d'études romand (PER)* [Page web]. https://www.vd.ch/formation/enseignement-obligatoire-et-pedagogie-specialisee/deroulement-de-lecole-obligatoire-dans-le-canton-de-vaud/plan-detudes-romand-per (read 2026-11-01).
- Access label: read-directly (whole page).
- Passage: the PER defines learning content for the eleven years of compulsory school in French-speaking Switzerland and sits within HarmoS and the Convention scolaire romande (paraphrase). The page lists PER brochures (domaine Langues among them) on the CIIP portal but gives no grade labels.
- Relevance: Intro (one sentence on the curriculum frame). The PER text itself and the Langues brochure were NOT read (portal returned nothing; see Blocked).
- Citable: yes, for the sentence above only.

### eurydice_fr_primary — Eurydice (European Commission), France, "Enseignement primaire"
- APA 7: Eurydice. (2023). *France: 4. Enseignement primaire* [Page web, dernière mise à jour 14 décembre 2023]. European Education and Culture Executive Agency. https://eurydice.eacea.ec.europa.eu/fr/eurypedia/france/enseignement-primaire (read 2026-11-01).
- Access label: read-directly (whole page; the navigation menu was long and not used).
- Passages ("4. Enseignement primaire", body text)
  1. French elementary school (CITE 1) takes pupils from 6 to 11 years old (paraphrase of the first paragraph).
  2. The elementary course has five years: CP (1st), CE1 (2nd), CE2 (3rd) in the cycle des apprentissages fondamentaux (cycle 2); CM1 (4th) and CM2 (5th) in the cycle de consolidation (cycle 3). Quote: "3ème année : le cours élémentaire deuxième année (CE2)".
  3. The consolidation cycle continues in the first year of collège, written "(6e)" on that page.
- Relevance: Method/Discussion for the control labels "CE2" (third elementary year, in French France) and "5e" (collision control). The page documents CE2 and that 6e is the first collège year. It does not list 5e, 4e, 3e or the ages of collège pupils. That 5e is the second collège year, aged about 12 to 13, is [inference] from the order 6e, 5e, 4e, 3e and from general knowledge, and is NOT supported by anything I read. The secondary Eurydice page that would document it could not be opened (see Blocked in search_log.md).
- Citable: yes for CE2 and for the statement that 6e is the first collège year; no for 5e.

### Summary of what Part C supports, and what it does not
- Supported (read-directly): entry at 4 completed years on 31 July (accord Art. 5; Vaud page); eight primary years then three secondary I years (accord Art. 6; Vaud, Geneva, Fribourg pages); cycle 2 = years 5-8 = ages 8 to 12 "en principe" (Vaud, Geneva, Fribourg); P labels in Vaud and Geneva; H labels in Fribourg.
- NOT found in words on any page read: a sentence saying that "5P" (Vaud, Geneva) and "5H" (HarmoS, PER, Fribourg) name the same school year. That equivalence is an inference [inference] from identical structure (cycle 2 = years 5 to 8, ages 8 to 12 on all three pages). If the manuscript states the equivalence as fact, it needs a source that says so (for example a CIIP or PER table of year names), which I could not open (edudoc.ch and the PER portal were blocked).
- NOT found: the age of a pupil in a given single year. The pages give ages per cycle only. Combining Art. 5 (entry at 4 completed years on 31 July) with eight primary years, a pupil who progresses without delay or advance is about 8 to 9 years old at the start of the 5th year [inference, arithmetic on the accord, not stated by any page].
- Partly covered: the French "CE2" label (third elementary year) is supported by eurydice_fr_primary. The French "5e" label (collège) is not supported by any page read: the official ministry pages (education.gouv.fr, eduscol) failed to load, and the Eurydice secondary page was refused by the fetch tool.

## D. Teachers' use of generative AI; prompt sensitivity

### epfl2023_vaud_teachers — EPFL Center LEARN survey of Vaud teachers and ChatGPT (news item)
- APA 7: Avry, S. (2023, July 18). *ChatGPT is shaking up the world of education: What do teachers say?* EPFL News. https://actu.epfl.ch/news/chatgpt-is-shaking-up-the-world-of-education-wha-2 (CC BY-SA 4.0; the page lists Avry as author and names the survey team: Avry, Mondada, Liégois, Vaucher, Martinez, Dehler Zufferey).
- Access label: read-directly (whole news page). The two full survey reports (PDF links on the page, learn.epfl.ch) were NOT opened.
- Passages (page body)
  1. Survey between 22 February and 22 March 2023 in the canton of Vaud with 931 teachers of public high schools (post-compulsory) and private schools, with the cantonal post-compulsory directorate (DGEP) and the private-school association (paraphrase).
  2. 98% of surveyed teachers knew ChatGPT and 52% had used it; of those, 24% had used it in teaching, "primarily for lesson preparation" (the page's words; I quote four words).
  3. 87% believed ChatGPT can facilitate cheating; 74% believed it would not assist them in their work; 76% wanted information and training (paraphrase of percentages).
- Caveats: figures are from a news item, not from the report; the respondents teach in high schools (gymnases) and private schools, not in primary school; the 2023 date predates the models audited in ART 5; an image caption on the page says "March 2022", which looks like a slip for 2023 [inference].
- Relevance: Intro (Swiss, Vaud evidence that some teachers use ChatGPT for lesson preparation). Not evidence about primary teachers or about reading texts.
- Citable: yes, for the statements above, labelled as a news summary of a survey.

### sclar2024 — Sclar, Choi, Tsvetkov & Suhr (2024), prompt-format sensitivity [added by me; not on the request list]
- APA 7: Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2024). *Quantifying language models' sensitivity to spurious features in prompt design or: How I learned to start worrying about prompt formatting* (arXiv:2310.11324v2). arXiv. https://arxiv.org/abs/2310.11324
  (Page 1 prints "Published as a conference paper at ICLR 2024"; v2 is dated 1 Jul 2024. I did not open the ICLR page or the proceedings version, so I give no proceedings title or pages.)
- Access label: read-directly (arXiv v2 full text via alphaXiv, saved as one file of 99,304 characters; read: title page and Abstract, Section 1, the opening of Section 2, Sections 4.1 and 4.2, Section 6, Appendix C). NOT read: Section 3 beyond its first paragraphs (grammar and algorithm), Sections 4.3-4.5, Section 5 (related work) and Appendix B. Locations are by section because the text extraction has no reliable page numbers.
- Passages
  1. Abstract and Section 1. Several widely used open-source LLMs are very sensitive to meaning-preserving changes in prompt formatting in few-shot settings, with differences of up to 76 accuracy points for LLaMA-2-13B. Quote (Abstract): "performance differences of up to 76 accuracy points".
  2. Abstract and Section 1. The sensitivity is not removed by a larger model, more few-shot examples or instruction tuning, and the effect of a format correlates only weakly between models (paraphrase).
  3. Section 1, last paragraph on page 2. With GPT-3.5 the spread across 320 formats and 53 tasks was up to 56 accuracy points, with a median of 6.4 (paraphrase of the authors' figures).
  4. Section 4.1. 53 tasks from Super-NaturalInstructions (19 multiple-choice and 34 classification), models LLaMA-2 (7B, 13B, 70B), Falcon-7B (base and instruct) and GPT-3.5-Turbo; the few-shot examples and their order were fixed so that only the formatting varied. The tasks are classification and multiple choice scored by accuracy, not free-text generation.
  5. Section 4.2. Across tasks the median spread was 7.5 accuracy points; trends between two models were reversed by changing the format with probability about 0.14 in the two model pairs reported (paraphrase of the authors' figures, with the threshold of 0.02 accuracy given in the text).
  6. Section 6 (Discussion). The authors recommend reporting a range of performance over plausible formats when comparing models, and add that a single well-chosen format "may still be sufficient" for building a system (the quoted words are theirs).
  7. Appendix C (Limitations). The tasks have reasonably short instructions and short input fields; the effect of input length is left to future work (paraphrase).
- Relevance: Discussion/Limitations. It is general evidence that outputs of a model can depend on surface features of the prompt, and that comparisons between models can change with the template. Whether this bears on ART 5 depends on how many prompt wordings were used for each grade label, which I did not check [inference].
- Differences from ART 5: English tasks; formatting changes (separators, casing, spacing), not changes of meaning such as a grade or an age; few-shot classification scored by accuracy; open-source models and GPT-3.5-Turbo, not the six audited models; no text generation and no lexical measure. The effect of a grade label is therefore outside what the paper tests.
- Citable: yes, for the passages above, as an arXiv preprint of a conference paper.

## Unfinished and limits

- Abstract-only, not citable: liu2025, watanabe2025, mesmer2024, li2024, nguyen2026. Full-text-extracted only: patel2023. Not accessible: new2004_lexique2 (content), new2007_subtitles (full text), vanheuven2014_subtlexuk, kandelmoles1958 (original).
- Read only in part: ripoll2025 (Appendix A prompts and limitations not read), imperial2023, lexique3manual, manulex2004, javourey2022. The unread pages are named under each source.
- Not opened: the PER text and CIIP brochures, the full EPFL survey reports, the journal PDF of Oh et al., any source for the French label 5e.
- Section D is thin: one teacher-use item (a news summary of a Vaud survey, high-school level) and one prompt-sensitivity paper (sclar2024: formatting changes in classification tasks, not label wording). Effects of an age or grade label on readability are covered by sources in section A (rooein2023, imperial2023, farajidizaji2023). I read no paper on persona effects, and no Swiss primary-teacher survey was among the listed search results.
- These notes support only a bounded novelty sentence; see the final report. No search covered Google Scholar, ERIC, Scopus, Web of Science, Cairn or Persée.
