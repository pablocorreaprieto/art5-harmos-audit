# Pre-submission audit, referee1 methods (2.11.2026)

Separate session (model claude-opus-5-5), launched by the main session (claude-opus-5-5) with no access to the drafting conversation, earlier reviews or the audit in progress. Brief and report verbatim.

## Brief

You are Referee 1 for a manuscript submitted to *Education and Information Technologies* (Springer, journal 10639). Your expertise: quantitative methods, evaluation of large language models, readability and lexical measures, preregistration and statistical reporting.

Read these files (read-only):
- /home/claude/art5-harmos-audit/manuscript/build/manuscript.md (the anonymised manuscript, as reviewers receive it)
- /home/claude/art5-harmos-audit/manuscript/build/supplement.md (Supporting Information)
- /home/claude/art5-harmos-audit/PREREG.md (the deposited preregistration text)
You may open the analysis code and result files in /home/claude/art5-harmos-audit (for example analyze.py, compute.py, exploratory.py, exploratory_p7.py, validate_measure.py, design.json, results/) to check a specific claim, as a reviewer with access to the anonymised repository could. Do NOT open anything under manuscript/records/, manuscript/verification_report.md, CHANGELOG.md, history/, or any file holding earlier reviews or the authors' own audit: form your own view. Do not create, modify or delete any file in that repository; if you need scratch space use /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/review_r1/.

You may read the journal's aims and scope at https://link.springer.com/journal/10639/aims-and-scope.

Write the referee report you would send to the editor:
1. Summary of the study in 3 to 4 sentences.
2. Main strengths (short).
3. Major issues, ranked by importance. For each, quote or locate the exact passage (section and sentence), say why it matters, and give a concrete fix. Say whether the fix can be done without new data collection (re-analysis, rewording, added limitation, added table) or needs new data.
4. Check the preregistration against the manuscript: list every difference you find between what was preregistered (hypotheses, measure, exclusions, sample size, analyses) and what is reported, and whether the manuscript declares it.
5. Check statistical reporting: test, estimates, effect sizes with confidence intervals, exact p values, multiplicity, model and software versions, sampling parameters, and whether confirmatory and exploratory results are clearly separated. Flag any claim stronger than its evidence.
6. Minor issues (numbered, one line each).
7. Recommendation (accept, minor revision, major revision, reject) and your estimated probability, as a number, that this manuscript is eventually accepted at this journal. Say what, if anything, would make you recommend desk rejection.

Be adversarial but fair, and do not praise for politeness. Verify every claim you make against the text or files. Never invent literature: name a missing reference only if you have verified it exists (you may use web search) and give its DOI or URL; otherwise describe the kind of work that is missing. Keep the report under 1,500 words. Your final message must be the report itself.

## Report

**Referee 1 report** (an in-project reading by an AI session acting as referee; not an outside peer review)

Checks made: besides reading the manuscript, the Supporting Information (SI) and PREREG.md, I recomputed the primary measure from the raw outputs with a Lexique 3.83 copy whose vrai/faux casing I corrected (the issue S1 flags). My scripts are in /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/review_r1/scripts/. The recomputed measure matched results/measures.csv exactly for all 7,680 texts, and H2-H reproduced (−0.0117, p = .0021).

## 1. Summary
Six LLMs from three providers wrote 7,680 French reading texts, crossing eight level wordings, grades 3H–8H, two genres and 16 topics. For each model, texts requested with bare Swiss grade labels were compared with its texts for the matching age, using the mean Zipf frequency of content lemmas. Of the four preregistered topic-level t-tests (Holm), only the level of the bare H label differed (−0.012 Zipf, "0.30 model-internal years"). Exploratory analyses show large per-model departures in opposite directions, a strong « 5e » collision effect and probe errors. The paper advises teachers to state the age.

## 2. Strengths
- A real preregistration, a small Holm-corrected confirmatory family and a pilot-based power analysis. The timing fits the raw logs (first call 07:55:47 UTC).
- Complete raw outputs and code; the measure reproduces exactly.
- A paired within-model design with a positive control (L6), and unusually full disclosure of AI use, funding and conflicts.

## 3. Major issues

**M1. The practical recommendations go beyond the evidence and partly contradict it.**
- Where: Abstract ("Teachers should state the age"), Implications and Conclusion ("with the age stated every model's point estimate stayed within a year").
- (a) On the paper's pooled metric, L3 departs from the age-only texts more than the bare H label does: +0.018 Zipf and a shift of −0.46 years [−0.62, −0.33], against −0.012 and 0.30 (Tables 2, S3, S5).
- (b) The bare P label also keeps every model within a year (shifts −0.27 to 0.48), with the same SD of shifts (0.28). Compared with P, L3 improves only the spread of tracking (SD 0.21 vs 0.45, Table S11).
- (c) The age alone is the reference, so this design cannot evaluate "state the age".
- "The model matters more than the wording" (Discussion) compares a post hoc max–min range across models with averaged wording effects. At the same granularity, the bare H label moved Haiku's 3H texts by 0.184 Zipf (my computation), more than the spread of the six models at 3H (0.166).
- Why: these are the paper's take-home messages.
- Fix: present them as exploratory and model-specific. Replace the range comparison with a variance decomposition (model, label, model × label, with intervals), or drop it. No new data.

**M2. The confirmatory estimand averages six chosen models that depart in opposite directions.**
- Where: Abstract ("0.30 model-internal years", "the P label showed no difference"); Conclusion ("will on average get a text at about the lexical level of the matching age").
- Why: without Haiku, H2-H is +0.0041 (p = .297, Table S10). The P null averages trackings from 0.16 to 1.43 (Table S3). No teacher uses an average of six models that were not sampled.
- Fix: put the leave-one-out dependence and the heterogeneity in the Abstract, and frame the pooled tests as conditional on this set of models. Test heterogeneity with Wald tests on the label × model terms that analyze.py already estimates (secondary_ols), rather than only with post hoc RM-ANOVAs that have no sphericity correction. No new data.

**M3. The measure's validity is thin for the inferences drawn from it.**
- Why: every estimate and every "year" rests on it.
- (a) The only external check (Vikidia vs Wikipedia) contrasts encyclopedias for children and for adults. Nothing shows that the measure resolves one-year differences in children's texts or in narratives, and the "years" are calibrated on the models' own outputs.
- (b) Every token absent from Lexique is scored as a content word at Zipf 1.49 (compute.py, line 22 and lines 342–346). The Measure section ("a lemma absent from Lexique counts as frequency zero") misdescribes this. These tokens make up 0.53% of content tokens, and most are artefacts:
  - *tandis* (862 tokens; Lexique lists only *tandis que*)
  - units: *h*, *kg*
  - onomatopoeia: *glou*, *bzzz*
  - feminised titles: *pompière*, *cheffe*
  - unlisted inflections of common verbs: *aèrent*, *semèrent*
- *Tandis* becomes more frequent with grade (GPT-6 Luna: 0.05 to 0.36 per text from 3H to 8H), which slightly steepens the rulers. In my re-analysis, dropping these tokens leaves the primary conclusions intact (H2-H −0.0138, p < .001; H2-P −0.0030, p = .43).
- Fix: report that sensitivity analysis and correct the description. Handle multiword entries and lemmatise unknown forms. Re-score with MANULEX grade-level frequencies (already cited), and validate on graded children's texts, for example the original and simplified Alector texts (Gala et al., 2020, https://aclanthology.org/2020.lrec-1.169). This needs existing corpora only; no new LLM data.

**M4. The Mistral Large 4 reasoning analysis is selectively reported and overstated.**
- Where: Results, "What the models said about the labels", paragraph 2 ("reached the words only in part … −0.043 Zipf (SE 0.020) … about half").
- The exploratory_p7.py docstring (lines 30–34) records that the unadjusted comparison gave −0.016 (SE 0.017) and that grade and genre effects were added afterwards. Only the adjusted estimate is reported.
- Its p = .033 uses a normal reference. With t(15), as used elsewhere in the paper, t = 2.13, p = .050 and the 95% CI is [−0.086, 0.000], which contains the full two-year expectation (−0.083).
- The slope specification in the same output gives about 70% of the expectation (−0.029 vs −0.041 per year).
- The analysis also conditions on a post-treatment variable (the reasoning trace).
- Why: a specification chosen after the fact supports a mechanistic claim that its interval cannot support.
- Fix: report all specifications and the order in which they were run, use t(15), and delete "about half" and "only in part". No new data.

## 4. Preregistration versus manuscript
Hypotheses, conditions, prompt, sampling, sample size, exclusions and primary tests match. Differences:
1. Measure: the registration ("Tokens absent from Lexique that are not names count as frequency 0") and the code agree, but the manuscript's "a lemma absent from Lexique" misstates the rule. Undeclared.
2. Topics are "treated as random" but are the first 16 of a fixed list. Declared (S1).
3. The P-vs-H contrast was not registered. Declared.
4. The registered provider/model-size analysis is reported by tier only. Partly declared.
5. The registered linearity F tests appear only as "smallest p = .205", and the per-model H1 t statistics are missing. Undeclared.
6. Heterogeneity is tested with unregistered RM-ANOVAs, although the registered OLS includes label × model terms. Declared post hoc.
7. The specification of the Mistral reasoning analysis changed after its results were seen. Undeclared.
8. The equivalence reading, the 100,000-resample interval, the L0 intervals, the leave-one-out analysis and the reasoning tokens. Declared post hoc.
9. Six pilot topics are among the 16 confirmatory topics (design.json). Not stated; harmless.
10. Reviewers cannot verify the 08:52 approval. The editor should check the AsPredicted record, whose Q3 contains a repository URL that identifies the author.

## 5. Statistical reporting
- Primary tests: complete (t(15), exact p, Holm p, CIs). I confirmed the Holm values.
- Effect sizes: add dz and the topic-level SDs. "Model-internal years" divide by slopes that vary twofold (−0.025 to −0.049), so the same Zipf departure counts double for GPT-6 Luna. Give Fieller or delta-method intervals.
- Intervals: a percentile bootstrap over 16 clusters tends to under-cover (S1 concedes the intervals may be narrow). The P tracking interval [0.81, 0.99] conflicts with the t-test (p = .068). Use studentized or BCa intervals.
- Multiplicity: there is no correction outside the primary family. Yet the Discussion asserts per-model findings ("two wrote for older and two for younger pupils") that rest on borderline unadjusted results among at least 24 contrasts. For example, Claude Sonnet 5.5's level CI is [0.0004, 0.022], p = .043 (Table S4, numbers.json).
- Models and parameters: only undated aliases were used, and the returned IDs equal the aliases, so they identify no snapshot. Report the listed creation dates, top_p (provider default) and the default reasoning effort.
- Software: the manuscript gives no versions (requirements.txt pins numpy 2.5.3, pandas 2.3.3, scipy 1.18.1, statsmodels 0.15.0).
- Separation of confirmatory and exploratory results: every sentence is labelled, but both kinds share sections, and the Abstract's practical message rests on exploratory results. Split the Results.
- Over-claims: M1 and M4. "Showed no difference" should read "no detectable difference". The ±0.04 Zipf "equivalence" margin equals 0.8–1.6 model-internal years, which is large for beginning readers.

## 6. Minor issues
1. Report the pooled ratio shift (0.30) next to the mean of the per-model shifts (0.21, Table S1 note).
2. Add the per-model H1 t statistics and linearity F tests to Table 3.
3. Head Table S6's columns L1, L1P and L3.
4. Haiku reasoned mainly when given Swiss labels (Table S9). Discuss reasoning as a mediator that is confounded with the label.
5. There is one template and one sample per cell. Cite work on multi-prompt evaluation (Mizrahi et al., 2024, https://doi.org/10.1162/tacl_a_00681). A replication with other templates would need new data.
6. State in the Conclusion that the results concern API calls without a system prompt on 1 November 2026, not chat interfaces.
7. Report share_oov by model and label (compute.py already produces it).
8. The internal reviews used models of an audited provider, one of them an audited model. Present them as process, not validation.
9. The CRediT statement assigns roles to an AI tool. The editor should check this against the publisher's policy.

## 7. Recommendation
Major revision. Most fixes need only re-analysis and rewording, and external validation needs existing corpora, not new LLM data. Estimated probability of eventual acceptance at this journal: 0.40. I would recommend desk rejection only in two cases: if the editor cannot confirm from the AsPredicted record that registration preceded data collection, or if the editor judges the AI tool's role in design, analysis and drafting to be incompatible with the publisher's authorship policy.
