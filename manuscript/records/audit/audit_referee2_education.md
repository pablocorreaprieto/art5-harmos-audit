# Pre-submission audit, referee2 education (2.11.2026)

Separate session (model claude-opus-5-5), launched by the main session (claude-opus-5-5) with no access to the drafting conversation, earlier reviews or the audit in progress. Brief and report verbatim.

## Brief

You are Referee 2 for a manuscript submitted to *Education and Information Technologies* (Springer, journal 10639). Your expertise: literacy and reading instruction in primary school, text difficulty and text selection by teachers, teachers' use of digital and AI tools, and the international educational technology literature that this journal's readers know.

Read these files (read-only):
- /home/claude/art5-harmos-audit/manuscript/build/manuscript.md (the anonymised manuscript, as reviewers receive it)
- /home/claude/art5-harmos-audit/manuscript/build/supplement.md (Supporting Information)
- /home/claude/art5-harmos-audit/PREREG.md (the deposited preregistration text), only if you need it
Do NOT open anything under manuscript/records/, manuscript/verification_report.md, CHANGELOG.md, history/, or any file holding earlier reviews or the authors' own audit: form your own view. Do not create, modify or delete any file in /home/claude/art5-harmos-audit; if you need scratch space use /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/review_r2/.

Read the journal's aims and scope at https://link.springer.com/journal/10639/aims-and-scope, and look at what the journal has published recently on generative AI and teachers, so that you judge fit as its reviewers would.

Write the referee report you would send to the editor:
1. Summary of the study in 3 to 4 sentences.
2. Main strengths (short).
3. Major issues, ranked by importance. For each, quote or locate the exact passage (section and sentence), say why it matters, and give a concrete fix. Say whether the fix can be done without new data (rewording, reframing, added limitation, added literature) or needs new data. Cover in particular: whether the contribution matters beyond French-speaking Switzerland and is framed for an international readership; whether lexical frequency is presented as what it is relative to text difficulty and to what teachers need; whether the practical advice to teachers follows from the results; whether the literature positioning is adequate for this journal; clarity for a non-specialist reader.
4. How you, as a reviewer, react to the manuscript's statement on the use of generative AI (in the Method and in the Statements and Declarations), and whether anything in it would make you or the editor hesitate. Be candid.
5. Minor issues (numbered, one line each).
6. Recommendation (accept, minor revision, major revision, reject) and your estimated probability, as a number, that this manuscript is eventually accepted at this journal. Say what, if anything, would make you recommend desk rejection.

Be adversarial but fair, and do not praise for politeness. Verify every claim you make against the text. Never invent literature: name a missing reference only if you have verified it exists (you may use web search) and give its DOI or URL; otherwise describe the kind of work that is missing. Keep the report under 1,500 words. Your final message must be the report itself.

## Report

**Referee 2 report: "Swiss grade labels and the lexical demand of French reading texts written by large language models"**

*This is a reading by a separate AI session inside the project. It is not an outside peer review. I checked the references I suggest at abstract level.*

**1. Summary**

Six large language models from three providers wrote 7,680 French reading texts for grades 3H to 8H. Each request named the level in one of eight ways. These include the bare labels « 5H » and « 5P », the age alone (the reference) and a « 5e » collision control. The outcome is the mean Zipf frequency of content lemmas. Each label is compared with the same model's age-only texts, and the difference is expressed in "model-internal years". Pooled over models, the H label gave slightly rarer words (0.30 model-years, and the effect rests on one model). The P label gave no detectable difference. In exploratory analyses, individual models departed widely, in both directions.

**2. Strengths**

- The study is preregistered, and its departures from the registration are documented.
- Comparing each label with the same model's age-only texts separates misreading a label from missing an external target.
- The collision control works as intended.
- Results are reported model by model.
- Numbers are filled in by script.
- The limitations are candid.

**3. Major issues, ranked**

**3.1 What the measure captures, compared with text difficulty and what teachers need.**

The Abstract asks whether models write "at the lexical demand of the matching age". The Conclusion promises "a text at about the lexical level of the matching age". The reference is each model's own age-only text, so neither phrase is supported. Several points concern young readers:
- The word frequencies come from adult subtitles and novels, although MANULEX grade-level norms exist (Limitations).
- At 3H–4H, decodability and text length matter as much as frequency, yet length by grade is not reported.
- « à lire » does not say whether pupils read the text themselves or hear it read aloud.
- The pilot's residual SD (0.12 Zipf, Analysis) is about three years on the planning ruler. A single text may therefore barely separate adjacent grades, and a teacher works with one text, not an average.
- The Vikidia–Wikipedia check shows that the measure separates child texts from adult texts. It does not show that it separates ages 6 to 12.

*Fixes without new data:*
- Re-score the texts with MANULEX.
- Report text length, the share of words missing from the lexicon, and the spread within cells, by grade and model.
- Place the rulers against the Vikidia and Wikipedia scores.
- Reword the Abstract and the Conclusion.

*Fix with new data (advised):* have teachers rate a stratified sample of texts blind.

**3.2 The advice to teachers only partly follows from the results** (Implications: "State the age, alone or after the label…"; Conclusion: "The safest practice…").
- The age alone matches the reference by construction.
- The label with the age added (L3) departed from the age-only texts more than the bare H label did (−0.46 against 0.30 years).
- "Every model within a year" separates the two wordings only through Claude Haiku 5.5, which moved from 2.12 to −0.11 years (Table S3).
- With the bare P label (Vaud, Geneva), all six models were already within a year.
- The criterion ignores tracking. Mistral Small 4's P shift (−0.19) and tracking (0.16) imply texts about two years too old at 3H and about two years too young at 8H (my own linear calculation).
- "Read the text" is sound advice but does not say what to look for.

*Fixes by rewording:*
- Present "state the age" as a cheap precaution, not as a finding.
- Say what teachers should check at 3H–4H.
- Drop "safest".

**3.3 Contribution beyond French-speaking Switzerland.**

The journal's aims call for an international forum and strong conceptual frameworks. The recent papers on generative AI and teachers that I looked at mostly concern adoption, readiness and competence. An audit of model outputs fits the journal if it is framed for that readership. Here, though, the title, the Introduction (paragraph 3) and the Discussion address Swiss readers. The claim to generality rests on a single sentence: "The problem is not specifically Swiss…".

*Fixes without new data:*
- Build the paper around what transfers to other systems:
  - comparing each label with the model's own age-only texts;
  - the differences between models that pooling hides;
  - lighter models misreading local labels.
- Add a typology of label collisions:
  - Dutch school years (groepen) also count two kindergarten years.
  - French-speaking Belgium and Quebec number primary school from age six, so « 5P » collides with the Belgian « P5 ».
  - The Belgian collision is an alternative to the Discussion's explanation of the two-year probe errors, which invokes France and Vaud's old numbering.
- Link the misreading to evidence that LLMs do better for cultures that are more present online (Myung et al., 2024, https://proceedings.neurips.cc/paper_files/paper/2024/hash/8eb88844dafefa92a26aaec9f3acad93-Abstract.html).

**3.4 Literature positioning.**

The premise in the Abstract ("Teachers are advised to name their pupils' grade…") rests on a secondary citation. In the arXiv version of Imperial and Tayyar Madabushi (Section 2.1), this advice comes from two 2023 web guides for teachers. I could not load the ACL version. The only regional evidence of use (Introduction, paragraph 1: Avry, 2023) is a news item. It surveyed upper-secondary and private-school teachers, not primary teachers.

Of the 24 references, nine are web pages or official documents. Most of the rest are NLP papers and lexical databases. None is from this journal.

*Fixes without new data:* add a conceptual frame, for example the text, reader and task model, or teachers' competence with generative AI. Engage with work such as:
- Valentini et al. (2023): naming an age group in the prompt barely changed the vocabulary of children's stories written by LLMs (https://aclanthology.org/2023.emnlp-main.218).
- Liu et al. (2025): ChatGPT's simplified texts compared with expert teachers' on 17 lexical, syntactic and cohesion features (https://doi.org/10.1007/s11145-025-10676-2).
- SATO-CALIBRAGE, a French readability tool built to help teachers choose school texts (https://www.erudit.org/revue/rql/1996/v25/n1/603132ar.pdf).
- Kuzu et al. (2025), in this journal, on how prospective teachers write prompts (https://doi.org/10.1007/s10639-025-13673-8).

**3.5 The confirmatory results and the headline messages.**
- The confirmatory results are close to null.
- The one significant contrast disappears without Claude Haiku 5.5 (p = .297; Table S10).
- The take-home sentences of the Abstract and the Conclusion rest on exploratory or post hoc analyses. S1 lists 13 post hoc analyses added later.
- The labels are inconsistent. The comparison between models is called "post hoc" in the Results but "exploratory" in the Implications and the Conclusion.
- That comparison also sets absolute levels side by side for models whose mean text lengths differ by 80% (330 against 594 words).

*Fixes without new data:*
- Lead with the confirmatory results.
- Label each analysis the same way throughout.
- Retest the comparison between models with length adjusted and on the secondary measures.

**3.6 Clarity.**

"Model-internal years" appears in the Abstract but is defined only in the Analysis. Zipf differences need translating for a general reader:
- −0.012 Zipf means words about 3% less frequent.
- The smallest effect of interest (0.04 Zipf) means about 9% less frequent.
- The gap between Vikidia and Wikipedia (0.34 Zipf) means about 2.2 times less frequent.

*Fixes without new data:*
- Add a plain-language box.
- Add a table giving the status of each claim (confirmatory, exploratory or post hoc).
- Add a figure by model and grade. The 4.3-year offset at 3H cited in the Conclusion appears in no table.

**4. The statement on generative AI**

The disclosure, in the Method and in the declarations, is unusually transparent. It is consistent with Springer Nature's stated position: LLMs are not authors, and their use must be documented in the Methods. It would still make me hesitate, and I expect the editor and some reviewers to hesitate too.

By its own account, the AI assistant:
- "designed the study in detail";
- wrote the preregistration and the code;
- ran the analyses;
- drafted the manuscript "including the interpretation of the results".

Claude sessions reviewed the work, and one of them (claude-sonnet-5-5) is also one of the audited models. The author chose the topic, set the protocol's rules, took some design decisions, approved the design and "read the final manuscript".

My concerns:
- *Accountability.* CRediT is a taxonomy of contributions by people. Here it credits the design, analysis, software, validation and first draft to the AI. That fits poorly with the author's claimed roles of "methodology" and "writing – review and editing". The editor should rule on authorship before the review continues. The author should state what they personally checked.
- *Independence.* An assistant made by Anthropic designed, interpreted and reviewed an audit of two Anthropic models, and part of the cost was paid with Anthropic credits. The results do not obviously favour Anthropic, and the preregistration limits the risk. Still, one check by a person or by a non-Anthropic tool would help.
- *Literature.* The reference list reads as if search tools produced it (my inference). That may explain the gaps described in 3.4.

Two smaller requests:
- Rename "records of the internal reviews" (Data availability) so that no reader takes them for peer review.
- Say what "claude-fable-5-1" is.

**5. Minor issues**

1. The Lausanne teacher in the Introduction writes « 5H », but the paper says Vaud uses 1P–8P.
2. Abstract: "no difference" should be "no detectable difference".
3. Figure 3 is cited before Figure 2, and the SI tables are out of order.
4. State whether the mean is taken over tokens or over types.
5. Report, by grade and label, the share of words missing from Lexique (such as onomatopoeia), which get a Zipf of about 1.49.
6. Give Lexique's frequencies for *romand* and *canton*, and re-run L2 without them.
7. Lemmas are assigned without regard to context. Report their accuracy on a sample checked by hand.
8. Cite van Heuven et al. (2014) and Kandel and Moles (1958) directly.
9. L4 (−0.26 years) is called "close to the age", but L1 (0.30 years) is called a difference. Use the same wording for both.
10. Discuss the divergence on the Kandel–Moles measure: H texts were harder and P texts easier (Table S2).
11. List the 16 topics in the SI.

**6. Recommendation**

Major revision. Nearly all the fixes need no new data. The new-data addition I would value most is a small study in which teachers rate the texts.

Probability of eventual acceptance at this journal: 0.25. Most of the risk lies in the editor's view of the AI statement and in fit with the journal.

I would not recommend desk rejection on scientific grounds. I would support it only in two cases:
- the editor judges that the human contribution described in the AI and CRediT statements is not enough for authorship and accountability;
- the author cannot confirm having personally checked the analyses.
