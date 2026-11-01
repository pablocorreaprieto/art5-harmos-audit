# P7 et P6.2, relectures et vérifications par sessions IA séparées, ART 5 (1 novembre 2026)

Lectures internes par IA, pas une évaluation par les pairs. Chaque entrée garde la consigne complète et le rapport complet, tels quels.

## Consigne commune aux trois relecteurs (common.md)

Context for every reviewer (same text for R1, R2 and R3)

- Manuscript to review (rendered, every number filled in): /home/claude/art5-harmos-audit/manuscript/build/manuscript.md
  Supporting Information: /home/claude/art5-harmos-audit/manuscript/build/supplement.md
  Figures: /home/claude/art5-harmos-audit/results/figures/*.png (open them with the Read tool to see them)
- Repository (local clone, read only for you): /home/claude/art5-harmos-audit
  Preregistration text as deposited: PREREG.md. Design: design.json. Analysis: analyze.py. Measure: compute.py.
  Frozen results: results/numbers.json (every confirmatory number), results/manuscript_numbers.json (the
  number as printed in the text, by name), results/measures.csv (one row per text), results/probes.csv.
  The manuscript source with its placeholders is manuscript/manuscript.md; the rendered file is what a
  journal would receive.
- Target journal: British Journal of Educational Technology (BJET, Wiley, for the British Educational
  Research Association). Recorded constraints: manuscripts "should not normally exceed 6000 words,
  excluding references"; double-anonymous review; BJET articles carry Practitioner Notes; Wiley's policy
  allows AI to "substantially edit, develop, or translate any part of a manuscript" if its use is
  "described transparently". A BJET editorial of 2025 asks authors to name the model, its version and
  provider and to give prompt details.
- Rules for you: do not edit, create or delete any file in the repository; write nothing except your
  report, which you return as your final message. Do not call any model provider API and do not run
  pipeline.py steps that call models (generate, pilot, list-models, validate). You may run Python
  locally on the repository files (python3, pandas, numpy, scipy, statsmodels are installed), for
  example `python3 analyze.py results/measures.csv results/probes.csv /tmp/x.json` to recompute.
- Do not praise. Every finding needs a location (section and sentence, table or file and line), the
  problem, why it matters, a severity (must-fix, should-fix or minor) and a concrete fix. Distinguish
  what you checked (say how) from what you infer.
- Begin your report with exactly: "Internal reading by a separate AI session. Not peer review."

## R1, fond (modèle demandé : opus, claude-opus-5-5), consigne

You are an external referee for the British Journal of Educational Technology. You did not see how this paper was produced.
Read the manuscript and the repository described below.
Find errors, unsupported claims, missing baselines or controls, and threats to validity: construct validity of the measure (mean Zipf frequency of content lemmas as lexical demand), the choice of the age-only texts as the reference, internal validity of the comparisons, external validity (models, prompt wording, language, classroom use), and whether the conclusions and the practical recommendations follow from the evidence. Check that exploratory results are not presented as confirmatory, and that every claim about prior work is phrased within what such a study could show.
For each finding give the location, the problem, why it matters, a severity (must-fix, should-fix or minor) and a concrete fix. Do not praise.
Begin your report with: "Internal reading by a separate AI session. Not peer review."

## R2, méthode et statistiques (modèle demandé : sonnet, claude-sonnet-5-5), consigne

You are a methods and statistics referee.
Check that every analysis matches the preregistration (PREREG.md, as deposited), that each reported number appears in results/numbers.json (or results/manuscript_numbers.json, which is derived from it) with the same value and rounding, that the assumptions of each model hold (one-sample t-tests over 16 topics, Holm correction, OLS with errors clustered by topic with 16 clusters, percentile bootstrap over topics for ratio estimators), and that the sample-size and power claims follow from the code (sim_power.py, sim_power_results.json, results/pilot_summary.json).
Re-run the analysis from the frozen data if needed (python3 analyze.py results/measures.csv results/probes.csv /tmp/numbers_check.json), and look for any analytic choice in the text that the preregistration did not fix.
For each finding give the location, the problem, the evidence, a severity (must-fix, should-fix or minor) and a fix.
Begin your report with: "Internal reading by a separate AI session. Not peer review."

## R3, rédaction de la revue (modèle demandé : fable, claude-fable-5-1), consigne

You are the handling editor of the British Journal of Educational Technology.
Using the journal's aims and scope (educational technology research, including artificial intelligence in education, with implications for practice), the constraints recorded below and Wiley's AI policy, decide whether you would desk-reject this submission.
List the reasons an editor would give, in order of weight, and the change that would remove each one.
Check length (count the words yourself, excluding references), structure, the abstract and practitioner notes, fit with recent articles in the journal (for example Li, Xing, Li, Zhu and Oh 2024, doi 10.1111/bjet.13554, on the readability of generated mathematics stories for grades 3 to 5), anonymisation for double-anonymous review, and the AI-use declaration.
Begin your report with: "Internal reading by a separate AI session. Not peer review."

## Vérification des couples phrase et citation (P6.2, modèle demandé : sonnet, claude-sonnet-5-5), consigne

Citation verification for the ART 5 manuscript (protocol phase P6.2). You did not write the manuscript.

Input: /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/p6_pairs.json, a list of 44
sentence-citation pairs taken from the rendered manuscript (/home/claude/art5-harmos-audit/manuscript/build/manuscript.md).
Each pair gives the sentence, the reference key, the in-text citation, where the source is (DOI, arXiv or URL) and the
access level the author recorded. The full reference entries are in /home/claude/art5-harmos-audit/manuscript/references.json.

Task. For each sentence and the source cited for it, find the passage in the full text that supports the sentence.
Report, for every pair: n, the source key, the access level you obtained yourself (read-directly, abstract-only or not
accessible), the location of the passage (section, page or heading), a short quote of at most 15 words from the passage,
and a verdict: supports, partly supports, does not support, or cannot check. Never mark a pair as supported from an
abstract, a search snippet or a summary; read the passage itself. When a sentence cites several sources, judge the part of
the sentence each source is cited for. When a verdict is "partly supports" or "does not support", say what the sentence
should say instead, in one line. For the two secondary citations ("as cited in"), check that the secondary source
attributes the point to the primary one.

Also check, from the same readings, every number the sentences take from a source (for example ages, years, shares).

How to read. arXiv papers: the alphaXiv tools (get_paper_content, answer_pdf_queries). Web pages and PDFs on the web:
WebFetch, asking for verbatim sentences; alphaXiv's answer_pdf_queries also reads web PDFs. Scite is not available
(subscription expired). Crossref, OpenAlex and publisher pages may be blocked; say so when they are. Do not use the
reading notes of the earlier session (files under scratchpad/p2_literature) as evidence: open the sources yourself.
Do not edit any file. Return the whole report as your final message, as a table followed by a list of the pairs that
need a change. Begin your report with: "Internal reading by a separate AI session. Not peer review."


## R3, rapport complet (lancée à 12:32, reçu à 12:47, 60 appels d'outils, claude-fable-5-1), texte intégral

Internal reading by a separate AI session. Not peer review.

# R3 — Handling-editor reading for BJET (desk decision)

## Verdict

As the file stands today I would not send it to reviewers: I would return it unassessed ("unsubmit") for an incomplete submission, and on resubmission I would send it to review rather than desk-reject it, with one caveat on fit (reason 4). The science is within BJET's scope (AI in education, implications for practice), preregistered and reproducible (I recomputed the four primary tests from results/measures.csv and matched Table 2 to three decimals), but the manuscript is not submittable: it has no title, no keywords and placeholder text in its declarations, its conflict-of-interest statement is contradicted by the repository's own record of how the API calls were paid, its AI-use declaration is thinner than the journal's 2025 editorial asks and than the repository shows, and the companion materials for double-anonymous review (preregistration text, repository bundle) would identify the author. Reasons in order of weight, then the checklist the task asked for, then what I could not verify.

## What I checked and how

- Manuscript and SI as a journal would receive them: /home/claude/art5-harmos-audit/manuscript/build/manuscript.md and supplement.md, plus manuscript.docx (metadata, embedded media, strings) and the three figure PNGs (viewed) and PDFs (metadata).
- Repository: README.md, PREREG.md, CHANGELOG.md (Deposit section), manuscript/make_anonymous_bundle.py, manuscript/submission/title_page.md and cover_letter.md (tracked in git), manuscript/verification_report.md, process_facts.json, source_facts.json; `git ls-files` and `git grep` for identifying strings; a dry simulation of the anonymisation script in memory (nothing written).
- Numbers: independent recomputation of H2-H, H2-P, H3-H, H3-P from results/measures.csv (pandas/scipy, topic-level t-tests) and comparison with results/numbers.json and Table 2; counts of texts, truncations, flags, duplicates, mean/median length, per-model length. All matched.
- Word count: Python whitespace tokenisation of the rendered manuscript.md, by level-1 section (see Length below).
- Web: Wiley's Best Practice Guidelines (AI section) fetched; the BJET author-guidelines pages (onlinelibrary.wiley.com/page/journal/14678535/homepage/forauthors.html and the bera-journals hub) refused automated reading (client error), as did the Wiley abstract page of the 2025 editorial and the Lancaster eprint PDF (robots); the Lancaster research-portal page gave the editorial's citation (Mavrikis, Lewin, Cukurova, Major, Outhwaite & Rubegni, 2025, BJET 56(3), 1118–1121, doi 10.1111/bjet.13581) and OpenAlex gave a summary of its content; an EdTech Hub copy of a BJET call for papers confirmed "Manuscripts should not normally exceed 6000 words, excluding references", "double-anonymous peer review" and abstracts "around 250 words"; Consensus confirmed Li et al. 2024 (BJET) and surfaced other precedents. Scite's MCP tools returned "paid plan required"; Crossref and OpenAlex via curl were blocked by the proxy (OpenAlex worked through WebFetch).
- No fact in this report comes from the memory store; all come from the repository, the manuscript, and the tool results above.

## Reasons an editor would give, in order of weight

### 1. The submission is incomplete (must-fix; would be returned before any assessment)

- Location: manuscript.md line 2 (`title: "TITLE TO WRITE LAST"`), also the docx core property dc:title; line 207 ("AUTHOR INPUT: the author declares no conflict of interest (to confirm)"); line 209 ("AUTHOR INPUT: no specific funding (to confirm) … (wording to confirm)"); no Keywords line anywhere (grep for "Keywords" finds nothing); title_page.md ("Title. TITLE", "Word count … COUNT words", "AUTHOR INPUT: affiliation", "AUTHOR INPUT: e-mail"); cover_letter.md ("AUTHOR INPUT: confirm", "AUTHOR INPUT: affiliation").
- Why it matters: Wiley's submission checks and the editorial office return files with placeholders; an editor who sees "to confirm" in a conflict-of-interest statement cannot accept the declaration at all.
- Fix: write the title (the preregistration's 79-character name, "Swiss grade labels and the lexical demand of LLM-generated French reading texts", is a usable base), add 4–6 keywords under the abstract, replace every AUTHOR INPUT/COUNT/TITLE token in the manuscript, title page and cover letter, and re-render so the docx title property changes too.

### 2. The conflict-of-interest and funding statements are contradicted by the repository (must-fix)

- Location: manuscript.md lines 207–209 and 211; CHANGELOG.md line 18: "Provider credit before the run: Anthropic 206.87 USD (5.00 purchased, 201.87 promotional)". The manuscript says the Anthropic calls "were paid from API credits attached to the author's account" and that there is no conflict of interest.
- Problem (checked, not inferred): the Anthropic calls were paid almost entirely with promotional credits granted by Anthropic, which is (a) one of the three audited providers, (b) the maker of the assistant that designed, coded and drafted the study, and (c) the provider whose lighter model is the paper's headline failure. The declaration of "no conflict" with a vague "credits attached to the author's account" would read, once the repository is opened, as an undisclosed in-kind contribution from an audited company.
- Why it matters: Wiley's guidelines require disclosure of financial support and competing interests; an editor who finds the CHANGELOG line after publication would have to issue a correction. This is the kind of omission that turns a desk decision negative.
- Fix: in Funding, state plainly "The Anthropic calls (X USD of the 41.12 USD) were paid with promotional API credits granted by Anthropic; the OpenAI and Mistral calls were paid by the author"; in Conflicts of interest, state that the author received promotional credits from Anthropic, that the assistant used is Anthropic's, and that Anthropic had no role in the design, analysis or reporting (if true); keep the Limitations sentence (line 193) that already acknowledges the assistant's provenance. Also split the 41.12 USD by provider (results or CHANGELOG hold the per-provider spend).

### 3. The AI-use declaration meets Wiley's minimum but not the journal's 2025 editorial, and it understates what the repository records (must-fix for a, b, c; should-fix for d, e)

- Location: manuscript.md line 211 ("Use of generative AI"), line 193 (Limitations), line 38 (Introduction, search-tools sentence).
- What is right (checked against Wiley's AI section): the model, its identifier and provider are named (Claude Opus 5.5, claude-opus-5-5, Anthropic); the use is "described transparently and integrated into the manuscript"; no AI is listed as author; the author accepts responsibility. Wiley's page does not itself ask for prompts or versions.
- (a) No prompt or protocol details. The recorded constraint (common.md) and the OpenAlex summary of the editorial (authors should "describe AI systems, models, and datasets in more detail") call for the model, version, provider and prompt details. The declaration gives none of the assistant's prompts; the sentence "the prompts, parameters and outputs are archived in the repository" refers to the audited models' prompts, not to the prompts that produced the study. The CHANGELOG (line 6) says the briefs and reports of the nine internal readings are kept outside the repository (a Claude project and a Drive document). Fix: add the protocol and the reading briefs as Supporting Information S9 or a repository folder, and say in the declaration which document holds them.
- (b) The "separate AI sessions" that checked references and numbers are unnamed, while CHANGELOG line 10 names them (claude-fable-5-1, claude-sonnet-5-5). Fix: name them, with provider.
- (c) The division of labour is softer in the manuscript than in the repository. The manuscript says the study "was conceived and designed with the assistance of" the model; the repository says the design versions v0.1–v0.4.9, the code, the preregistration text, the manuscript, the cover letter, the title page and the anonymisation script were "written by the main session (claude-opus-5-5)" and that the author decides at two gates (title_page.md comment; make_anonymous_bundle.py docstring; CHANGELOG line 14 "approved by its only author"). An editor who opens the bundle will see the gap. Under Wiley's policy the editor decides whether the use is permissible, and the question that will be asked is whether the human contribution meets authorship criteria (conception or design or analysis; drafting or critical revision; approval; accountability). Fix: state the structure as it was ("under a written protocol, the assistant X; the author set the question [if so], approved the design at gate G1 on 1 November 2026, decided the exceptions listed at gate G2, edited the manuscript and approved it"), and add a CRediT-style contribution statement for the author. Do not describe it as less than it was.
- (d) Line 38: "Searches of Consensus, alphaXiv and the web … found no earlier study …; Scite and Elicit could not be searched (the search log is in the repository)". Naming AI search products and reporting which could not be searched is a log entry, not journal prose; it also signals to an editor that the literature review was tool-driven. Fix: "To our knowledge no earlier study has examined how language models read non-US grade labels (search log in the repository)", and keep the tool names in the search log and the AI declaration.
- (e) Voice: "We" throughout the body (lines 38, 76, 80 and elsewhere) and "the author" in the Statements (lines 207–211). Pick one; single-author "we" is tolerated, but the mix reads as two writers.

### 4. Fit with the journal and with its recent articles is asserted in the cover letter, not shown in the manuscript (should-fix; the one place where a desk reject on contribution could happen)

- Location: reference list lines 215–255 (21 entries); cover_letter.md paragraph 3; Background lines 44–50; Introduction line 34.
- Checked: not one BJET article is cited. Li, Xing, Li, Zhu and Oh (2024), "Are simpler math stories better? Automatic readability assessment of GAI-generated multimodal mathematical stories validated by engagement" (BJET; title, journal and year confirmed through Consensus; the DOI 10.1111/bjet.13554 is the one given in the task, which I could not resolve because Crossref was blocked) is the journal's closest precedent: GAI-generated stories for grades 3–5, text readability features including vocabulary simplicity, validated against pupils' engagement. The cover letter says the manuscript "adds to the journal's recent work … such as the study by Li, Xing, Li, Zhu and Oh (2024)", but the manuscript never mentions it. An editor reads both; the mismatch undermines the letter. Yan et al. (2023, BJET), the scoping review of LLMs in education whose recommendations include better reporting standards, is also absent although the paper's own implication ("report results by model") speaks to it.
- Five of the 21 references are arXiv preprints (Farajidizaji 2023, Huang 2024, Primpied 2022, Rooein 2023, Trott & Rivière 2024), and the Background's three central comparators are a workshop paper and two preprints. A quick Consensus search surfaced peer-reviewed work that does the same kind of thing and is not cited: Shen et al. (2025, Learning Disabilities Research & Practice; six AI tools, grade-level prompts, outputs above the requested grade), Nguyen (2026, International Journal of TESOL Studies; lexical-frequency profile of ChatGPT reading texts across CEFR levels), Murgia et al. (2023, UMAP adjunct; 4th-grade readability of ChatGPT answers judged by children). I read their abstracts only, not the full texts; the main session should check them before citing.
- Contribution as an education journal sees it: the educational framing is thin (why lexical demand matters for primary reading instruction, how teachers level texts, what "reading level" means in Swiss practice: none of this is in the Background), the measure is one lexical dimension with no human judgement (acknowledged at line 193), and the practical result is a prompt-wording rule. Against an acceptance rate that the 2025 editorial reports as falling, an editor could call this "limited contribution to educational technology" and desk-reject. I rate that risk moderate, not high, because the preregistration, the scale and the model-by-model finding are the kind of methodological contribution BJET's AIED editorial asks for.
- Framing: the title-less abstract and the Introduction present a Swiss problem; the general point (grade labels collide across systems: "Year 5", "5th grade", "5e", "5H", "Primary 5", "Klasse 5") is stated only through the French collision. Fix: one sentence in the Introduction and one in the Conclusion that place the Swiss case as an instance of a general problem for any non-US system, and a title that says so.
- Fix for this reason as a whole: cite and position against Li et al. (2024) and Yan et al. (2023) in the Background and Discussion; replace or supplement preprints with the peer-reviewed versions where they exist; add an educational paragraph to the Background (Lété et al. 2004 and Peereman et al. 2007 are already cited and can carry it); say in the Implications what a teacher should do with a text whose lexical demand is right but whose sentence length is not.

### 5. Double-anonymous review: the manuscript is clean, the companion materials are not (must-fix before any link reaches reviewers)

- Manuscript and SI (checked): "link anonymised for review" at lines 56, 201, 203 and supplement line 8; no name, affiliation, ORCID, e-mail or repository URL; docx creator property empty; figure PNG/PDF metadata carry only the Matplotlib software string; nothing identifying in the figures.
- Preregistration text (checked): PREREG.md line 46, deposited verbatim as AsPredicted #321415 (CHANGELOG line 14), contains "https://github.com/pablocorreaprieto/art5-harmos-audit (made public at submission)". AsPredicted's anonymised PDF hides author names, not the body text, so the anonymised preregistration link that the manuscript promises (line 203) would hand reviewers the author's GitHub user name. Fix: give the unredacted AsPredicted link to the editor only (title page) and provide reviewers with a redacted copy of the preregistration text in the Supporting Information, with the editor's confirmation that it matches the deposit; or ask AsPredicted whether the field can be redacted for the review copy.
- Repository bundle (checked by simulating manuscript/make_anonymous_bundle.py in memory at HEAD): the script would stop with "identifying strings left in" manuscript/make_anonymous_bundle.py (its own FORBIDDEN regex contains the forbidden strings), manuscript/submission/cover_letter.md and manuscript/submission/title_page.md (committed in ea43d9d, after the script was written; they contain the name "Correa"). If the stop were bypassed, the bundle would still leak the ORCID 0009-0009-1844-7453 and the UNIR affiliation through manuscript/verification_report.md (lines 58–59) and the two submission files, because neither "0009-0009-1844-7453" nor "UNIR" is in FORBIDDEN. Fix: exclude manuscript/submission/ and manuscript/verification_report.md from the archive (or move them out of the tracked tree), exempt the script's own source from the check, add the ORCID, "UNIR", "Universidad Internacional de La Rioja" and the e-mail addresses to FORBIDDEN, and run the script before submission so the ANONYMISATION.md it writes exists.
- Stale headers reviewers would read: README.md line 5 ("before the deposit of the preregistration … Nothing here is a result of the study") and PREREG.md line 3 ("not yet deposited") contradict the manuscript. Should-fix: update both to the post-freeze state (tags prereg and data-v1, deposit on 1 November 2026).
- Timing optics (minor, checked): CHANGELOG line 14 and 17 record the AsPredicted approval at about 08:52 and the main run at about 08:54 Zurich time; the first raw file is calls_20261101T075547530698Z (08:55 CET). "Before the confirmatory data were collected" is true, by two minutes. Reviewers who see this may call the deposit perfunctory even though the text was frozen at tag prereg beforehand. Fix: state the deposit and run times in S1 and point to the tag.

### 6. Length (minor; no action needed now, but no headroom for reason 4)

- Counted myself (whitespace tokens of the rendered manuscript.md, references excluded):
  - Abstract 244; Practitioner notes 198; Introduction 561; Background 525; Method 1,742 (1,584 without Table 1); Results 1,554 (1,290 without Table 2 and 3, captions kept; 1,151 without captions); Discussion 1,038; Conclusion 86; Statements 300; References 516 (excluded).
  - Everything except references: 6,248 with tables and captions; 5,826 without the tables.
  - Main text Introduction to Conclusion: 5,506 with tables; 5,084 with captions but no tables; 4,945 with neither.
- Against "should not normally exceed 6000 words, excluding references" (constraint recorded in common.md; same sentence seen on the EdTech Hub copy of a BJET call), the paper is inside the limit on any usual reading and over it only if abstract, notes, tables, captions and statements all count. The additions under reason 4 will push it over unless the Method (1,742 words, the longest section) gives up the list of eight secondary measures (lines 90) and part of the Analysis (lines 98–104) to S1.

### 7. Abstract, practitioner notes and structure (checked; minor)

- Abstract: 244 words, unstructured, states the design, the numbers and the implications; within the "around 250 words" seen on the BJET call-for-papers copy (the official limit on the guidelines page could not be read). Two minor points: "below the smallest effect of interest" (line 8) is unexplained at abstract level (say "below the one-year difference set in advance"); "0.30 years" needs the unit the first time.
- Practitioner notes: the three BJET headings are present and exactly worded as in BJET articles (confirmed against the Li et al. 2024 record); three bullets each, 198 words. Fine.
- Structure: Abstract, Practitioner notes, Introduction, Background, Method, Results, Discussion, Conclusion, Statements, References, plus SI S1–S5 with eight tables. The "Statements" block covers data availability, preregistration, ethics, conflicts, funding and AI use, which is what BJET asks for; keywords are missing (reason 1). Figures are embedded in the docx with captions; Table 1 and Tables 2–3 are in the text.
- Numbers (checked): the four primary tests, the counts of texts, truncations, flags and duplicates, and the length statistics in the Data paragraph (line 110) reproduce from results/measures.csv.

## What I could not verify

- The official BJET author guidelines (word limit wording, abstract length, keyword count, practitioner-note length, AI-declaration placement): both Wiley URLs refused automated reading. The limits above come from the recorded constraints and from the EdTech Hub copy of a BJET call; a SciSpace template page claims "up to 4,000 words", which contradicts the journal's own text and which I disregard.
- The body of the 2025 editorial (doi 10.1111/bjet.13581): only its citation and a summary were obtainable; the "model, version, provider, prompt details" requirement is taken from the recorded constraint.
- The DOI 10.1111/bjet.13554 for Li et al. 2024: title, journal and year confirmed, DOI not resolved (Crossref blocked).

## Items worth recording by the main session (each with where I learned it)

- CHANGELOG.md line 18: Anthropic credit before the run was 206.87 USD, of which 201.87 promotional and 5.00 purchased; this is what the COI statement must disclose.
- CHANGELOG.md line 10: the reader sessions were claude-fable-5-1 and claude-sonnet-5-5 (to name in the AI declaration).
- manuscript/make_anonymous_bundle.py at HEAD cannot produce a bundle (my dry run): it trips on its own source and on manuscript/submission/*, and its FORBIDDEN list lacks the ORCID and "UNIR".
- PREREG.md line 46 (deposited text) carries the GitHub user name; the AsPredicted anonymised PDF will not hide it.
- The Scite MCP connector answered "requires a paid scite plan or an active free trial" (1 November 2026); Wiley/BJET pages and the Lancaster eprint PDF refuse automated fetches; Crossref and the Lancaster eprint are blocked at the proxy for curl, OpenAlex works through WebFetch.
- 2025 BJET editorial: Mavrikis, Lewin, Cukurova, Major, Outhwaite & Rubegni (2025), BJET 56(3), 1118–1121, doi 10.1111/bjet.13581 (Lancaster research portal).

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Une première copie de 12:50 avait remplacé le numéro AsPredicted, le nom de famille de l'auteur et l'ORCID par des mentions génériques et omis « (Lancaster research portal) » à la dernière ligne ; elle a été remplacée par le texte exact vers 12:58, puisque ce dossier est exclu de la copie anonymisée. Correction du 1.11.2026, après la lecture de confirmation : depuis la révision P7, ce dossier n'est plus exclu de la copie anonymisée ; manuscript/make_anonymous_bundle.py y remplace les chaînes qui identifient l'auteur et s'arrête s'il en reste.)

## R1, rapport complet (lancée à 12:32, reçu à 12:59, 75 appels d'outils, claude-opus-5-5), texte intégral

Internal reading by a separate AI session. Not peer review.

(Method: research-desk:paper-critique. Its "what is strong" section is replaced by a neutral "what the paper rests on", because the brief says not to praise. Tags: [checked] means I verified it, and the tag says how. [inference] is my reading.)

## Verdict

Major revision. The arithmetic is sound: I reproduced exactly, from results/measures.csv, the four primary tests, the H1 rulers, the L0 ages and every pooled shift and tracking. The problems are in interpretation, recommendations and disclosure.

- **Reference over-read.** The paper reads "the same mean lemma frequency as the model's own age-only text" as "the label is understood". Its own data contradict this.
- **Pooled nulls.** The pooled "no difference" results average opposite-signed model effects.
- **Unlabelled exploratory results.** Exploratory and post hoc results lead the abstract, the practitioner notes and the conclusion.
- **Unsupported recommendation.** "Add the age" is not supported in the units a teacher meets.
- **Disclosure and submission blockers.** Anthropic promotional credits, an audited model used as an internal design reader, missing AI prompt details, placeholders, and a preregistration text that names the author.

## What I was given and what I could not check

Given: the rendered manuscript and SI, the three figures, and the repository (code, frozen results, raw outputs, CHANGELOG, logs, manuscript sources).

Not checked:
- **AsPredicted record.** The deposit time comes only from CHANGELOG.md.
- **Official Lexique file.** The lexique.org file (SHA-256 637ba37a…) is not on this machine. I used the pylexique copy (fe2cb931…), which reproduces the frozen measure for 90.5% of texts and the frozen L2−L5 level. My re-measurements in S1 are therefore approximate.
- **BJET author guidelines.** Not opened.
- **ACL Anthology page.** The fetch was blocked, so I read Imperial & Tayyar Madabushi as arXiv v2 through alphaXiv.
- **Model identities and prices.** Taken only from models.json and logs/models_2026-10-31.json.

No provider was called and the repository is unchanged (git status clean).

## 1. How it reads

The paper claims three things:
- Six current LLMs asked for French reading texts "pour des élèves de 5H/5P" write at nearly the lexical demand they use for the matching age.
- Two lighter models are the exception.
- Teachers and tool builders should add the age to the label.

A reader will take away that Swiss labels are mostly safe and that "5H (8 à 9 ans)" is the wording to teach.

The evidence supports something narrower. Averaged over six models, bare-label texts are within about a third of a model-internal year of each model's own age-only text. Behind that average, the models differ widely and in opposite directions. The Limitations already say the study "shows equivalence between wordings, not appropriateness for pupils". The gap between that sentence and the abstract, notes and conclusion is the first finding.

## 2. Claims against evidence

| Claim | Where | Evidence offered | Verdict | Fix |
|---|---|---|---|---|
| Teachers are advised to name the grade in the prompt | Abstract s1; Intro ¶1; Practitioner notes (PN) "known" 1 | Imperial & Tayyar Madabushi 2023, p. 206 | partly. That page reports English-language advice by Staake (2023) and Herft (2023) [checked, arXiv 2309.05454v2 p. 2]. Nothing Swiss or French | "English-language guidance recommends… (as reported by Imperial & Tayyar Madabushi, 2023)", or cite the primary guidance |
| Every model used rarer words as age rose | Abstract; Results H1 | slopes −0.025 to −0.049, all p < .001 | supported [reproduced] | none |
| Bare H label: 0.30 years older [0.13, 0.46], below the smallest effect of interest (SESOI) | Abstract; Results "Bare labels" | H2-H and the pooled ratio | partly. Numbers reproduce, but the years are model-internal, the per-model shifts run from −0.77 to +2.12, the effect vanishes on the form-frequency secondary measure (−0.001, p = .636, Table S2), and the equivalence reading was not preregistered | "Averaged over six models, −0.012 Zipf, 0.3 years on the models' own age rulers. Model estimates −0.8 to +2.1 years (exploratory)" |
| "The P label showed no difference" | Abstract; Results | H2-P −0.001 [−0.010, 0.009] | overstated. On three secondary measures the P texts were easier: Kandel–Moles +0.30, p = .009; form frequency +0.012, p = .020; words per sentence −0.12, p = .012 (uncorrected). Mistral Large 4's reasoning misreads the P label in about half its texts (M1) | "No detectable difference in mean lemma frequency. The CI excludes ±0.04 Zipf (a post hoc equivalence reading)" |
| "Neither label changed how texts followed the grade" | Abstract; Results; Discussion ¶1 | H3 not significant | overstated. The P tracking CI [0.81, 0.99] excludes 1. For H, 4 of 6 models' tracking CIs exclude 1, in opposite directions. H3 power is never reported | "The pooled gradient tests did not reject. The design could detect a halving of tracking" (S5) |
| Two lighter models misread the bare labels | Abstract; PN; Results; Conclusion | per-model estimates | partly. Exploratory and unlabelled, and "misread" is inferred from text measures. The "mid-tier" Mistral Large 4 also misreads: probes 62%/55%, and its reasoning gives the wrong age in about 60% of L1 texts. Size is confounded with provider and with reasoning defaults (S3) | "In exploratory per-model analyses, Claude Haiku 5.5 and Mistral Small 4 departed most from their age-only texts" |
| Most wrong probe answers placed grades two years too old | Abstract; Discussion | exploratory.py, run after the deposit | partly. Post hoc and unlabelled. 74 of the 177 "wrong" first answers also state the correct range, and some errors are parser artefacts (S4) | label as post hoc; hand-code the answers |
| Adding the age made the models more consistent | Abstract; PN; Discussion; Conclusion | range of six point estimates | overstated. No test, and it holds only in model-internal units. In absolute Zipf the between-model SD is 0.058 (L3), 0.061 (L1), 0.064 (L5), and the CI of L3−L1 is [−0.008, 0.003] [my check]. L3 itself sits −0.46 years from the reference | "On each model's own ruler, the gloss narrowed the range of tracking (exploratory). It did not make models agree in absolute terms" |
| Naming the region made texts harder | Abstract; PN; Discussion | L2 shift 0.87 [0.54, 1.23] | partly. Exploratory, and about 30% of it is Swiss-French vocabulary rated rare by France-based norms (S1) | label exploratory; report the lemma decomposition |
| Keep local labels if you add the age; the wording "to recommend in teacher education and to build into classroom tools" | Abstract last s; PN implications; Conclusion s3 | L3 consistency | unsupported (row above, and M3). The reference is not validated for pupils (Limitations ¶1) | rewrite to what was shown (M3) |
| Audits should report results model by model | Abstract; PN; Implications | Tables S3 and S4 | supported | none |
| "Most of the current models we audited will write… at about the lexical level of the matching age" | Conclusion s1 | per-model shifts | overstated. Averaged over grades, 5 of 6 H shifts are within one model-year. Grade by grade, on the fitted lines from Table S3, only 2 of 6 models (H) and 3 of 6 (P) stay within one model-year at both 3H and 8H [my computation]. API conditions only | "With the API settings and prompt tested, three of six models…" |
| "A local label is mostly understood, on average" | Discussion heading | lexical equivalence | overstated (M1) | "Bare labels gave texts of similar lexical demand, on average" |
| "That is the error of reading the digit as the year of a primary school that starts at six (CM2)" | Discussion, probes ¶ | 86% within 1.5–2.5 years | overstated. Only 28% of those answers mention France and 13% Belgium. Other readings occur (S4) | "consistent with" |
| Model-internal age equivalents let wordings, models "and languages" be compared | Implications | none | unsupported for languages (one language, a French lexicon) | drop "and languages" |
| The youngest pupils are most likely to get a text that is too hard | Discussion | fitted per-model offsets | partly. True for H in the pooled per-grade table (3H −0.030 [−0.052, −0.008], S6), but "too hard" means relative to the model's own age-only text | qualify |
| No earlier study of how LLMs read Swiss or other non-US labels | Intro ¶4 | search log | partly. The wording is bounded, but the log's P2 section is empty, the web searches were title-level, and Ripoll y Schmitz & Sonnleitner prompted for Luxembourg grade 5 | narrow to Swiss labels; complete the log |

## 3. Major issues, ranked

### M1 (must-fix). The age-only reference cannot carry "the label is read as its age"

**Location.** Method, Prompts and conditions: "a model that understands the label should write the same kind of text under both". Discussion heading and ¶2: "so we can say whether a label is read as its age". Abstract: "misread".

**Problem.** Equivalence with the age-only text is neither necessary nor sufficient for understanding, and the paper's own data show it.
- (a) L4 «de CE2», a label the models presumably know, departs from L5 as much as the bare H label does: shift −0.26 [−0.45, −0.08], tracking 1.32 [1.22, 1.45] (Table S3). GPT-6.1 Sol is 100% correct on H probes, yet its CE2 tracking is 1.59.
- (b) L3, which states the correct age, departs by −0.46 years [−0.62, −0.33].
- (c) Mistral Large 4's visible reasoning [checked in data/raw; regex on the first "X-Y ans", spot-checked; exploratory]:
  - The reasoning states an age in 89% of L1/L1P texts.
  - The stated age is wrong, mostly by +2 years ("6P (6ème année primaire, environ 11-12 ans en Suisse)"), in about 60% of L1 and 51% of L1P texts. For L5 it restates the requested age every time.
  - For L1, the paired L1−L5 difference falls by −0.025 Zipf per year of stated error (SE 0.007), against a ruler slope of −0.041.
  - For L1P the slope is −0.013 (SE 0.014, p = .36), and the model's P shift is −0.15 years. A model that misreads the P label in half its texts shows no lexical shift.
- (d) The secondary measures disagree with the primary (Table S2: form frequency H2-H −0.001, p = .636; H2-P +0.012, p = .020; Kandel–Moles H2-P +0.30, p = .009). The text does not discuss this.

**Why it matters.** "Misread", the Discussion heading and the recommendations all rest on this inference. [inference] A grade label changes the framing of a text (school register, grade-typical content) independently of the age it implies. L1−L5 therefore mixes framing with misreading, and lexical equivalence can coexist with misreading.

**Fix.**
- Call the construct "lexical equivalence with the model's own age-only text". Keep "misread" for probe answers only.
- Add exploratory L1−L4 and L1P−L4 contrasts, using L4 as a known-label benchmark.
- Report the Mistral Large 4 reasoning-trace analysis.
- Discuss the secondary-measure divergence and drop "The difference is real but small".

### M2 (must-fix). Pooled results average opposite-signed model effects

**Location.** Abstract s6–7; Results "Bare labels…"; Discussion ¶1; Conclusion s1.

**Problem.**
- Per-model H2-H runs from −0.091 (Haiku) to +0.019 (Luna) (Table S4).
- For the H label, per-model shift CIs exclude 0 for 4 of 6 models: Sonnet −0.25, Haiku 2.12, Luna −0.77, Large 0.79.
- Tracking CIs exclude 1 for 4 of 6: two below (0.18, 0.46) and two above (1.20, 1.42) (Table S3). The pooled 0.93 is a cancellation.
- Results call tracking above 1 "at least as steeply as the age", yet over-tracking is also a departure. L4's 1.32 is described as "stretched".

**Why it matters.** "Neither label changed…" describes none of the six models.

**Fix.**
- Keep the preregistered pooled tests.
- Beside them, report label × model heterogeneity. The preregistered secondary OLS already has label × model terms: test their equality, labelled exploratory.
- State the spread in the abstract.
- Treat |tracking − 1| symmetrically.

### M3 (must-fix). The practical recommendations do not follow

**Location.** Abstract last sentence; PN Implications 1–2; Discussion "Implications" ¶1; Conclusion s3.

**Problem.**
- (a) L3 is −0.46 years from the reference. That is further than the bare H label (0.30) and the bare P label (0.02).
- (b) "More consistent" holds only for per-model tracking ranges in model-internal units, from six point estimates, with no test. In absolute Zipf, the between-model SD is 0.058 (L3), 0.061 (L1), 0.063 (L1P), 0.064 (L5). The CI of L3−L1 is [−0.008, 0.003] [checked: bootstrap over topics, 300 resamples].
- (c) The models disagree about the age-only text itself. At the same grade they span 0.14–0.23 Zipf, which is 3.6–5.8 years at the mean ruler slope [checked from measures.csv; visible in Figure 1]. That is an order of magnitude more than any bare-label effect.
- (d) The reference is not validated for pupils (Limitations), yet the Conclusion recommends the wording for teacher education.

**Why it matters.** The Practitioner Notes will be read as guidance. The data support "model choice matters more than label choice" better than "add the age".

**Fix.** Rewrite the implications to what was shown:
- Report results per model.
- Label wording moved texts less than model choice.
- The gloss aligned each model's grade gradient with its own age-only gradient (exploratory), but did not make models agree.

Drop the teacher-education recommendation unless S2 is done.

### M4 (must-fix). Exploratory and post hoc results are unlabelled, and the equivalence reading was not preregistered

**Location.** Abstract s8–9; PN "adds" 2–3; Conclusion s2–3; the H2-P paragraph ("its interval excludes … SESOI in either direction").

**Problem.**
- The per-model results, L2, the probes and the 86% figure (computed after the deposit, SI S1) appear as findings.
- PREREG Q5 registers two-sided difference tests only.

**Fix.**
- Mark each exploratory claim as exploratory.
- Call the equivalence reading post hoc. If it is kept, use TOST with 90% CIs against ±0.04 Zipf.

### M5 (must-fix). Conflict of interest and AI disclosure

**Location.** Statements (COI, Funding, Use of generative AI); CHANGELOG.md, "Deposit" section and header.

**Problem.**
- [checked] The CHANGELOG records the Anthropic balance before the run as "206.87 USD (5.00 purchased, 201.87 promotional)". The manuscript says the calls were "paid from API credits attached to the author's account (wording to confirm)" and declares no conflict.
- The CHANGELOG states that the internal design readings were done by claude-fable-5-1 or claude-sonnet-5-5. Claude Sonnet 5.5 is an audited model. The manuscript names only Claude Opus 5.5.
- No prompt details are given, although the BJET editorial asks for them.
- The CHANGELOG says the briefs live outside the repository.

**Why it matters.** Anthropic models are audited, and Haiku is the main negative case.

**Fix.**
- Disclose where the credits came from, in both COI and Funding.
- Name every model used in the research process.
- Archive the assistant prompts and briefs, or summarise them in the SI.

### M6 (must-fix, submission). Placeholders and anonymity

**Location.** Title "TITLE TO WRITE LAST"; "AUTHOR INPUT … (to confirm)"; "(wording to confirm)". PREREG.md Q3: the deposited text includes the repository URL with the author's account name. CHANGELOG names the author.

**Fix.**
- Complete the statements.
- Give the editor a redacted copy of the preregistration, and say in the cover letter that the deposited text contains the URL.
- Let reviewers see only the anonymised bundle.

### S1 (should-fix). France-French norms penalise Swiss French, and part of the region effect is vocabulary

**Location.** Method "Measure"; Results L2 paragraph; Discussion ("cannot explain from these data").

**Problem.** [checked, approximate re-measurement]
- L2 texts contain words that Lexique's France-based corpora rate rare:
  - "romand": 258 occurrences in L2, 0 in L5 (lemma Zipf 1.82)
  - "grand-papa": 159 vs 0
  - "suisse": 148 vs 0
  - "tresse": 120 vs 6
  - "canton": 58 vs 0
- Dropping a narrow Swiss-French lemma set moves L2−L5 from −0.034 to −0.024 Zipf (about 0.87 to about 0.6 years). L1−L5 barely moves (−0.0117 to −0.0108).
- Tokens absent from Lexique score as frequency 0 (Zipf 1.49). These include onomatopoeia ("tchou", "bzzz"), the unit "h", and "tandis" from "tandis que". [inference] The official lexicon file lacks "tandis" too: frozen and local values agree for texts containing it at the usual rate.
- Excluding all such tokens changes the primary contrasts little (H2-H −0.012 to −0.014).

**Fix.**
- Report a lemma decomposition of L2−L5.
- Run a sensitivity analysis without regionalisms and without out-of-lexicon tokens.
- State in the Method that the norms come from France-French adult corpora.

### S2 (should-fix). No external anchor

**Location.** Method "Measure" ¶2; Abstract ("years older"); Limitations.

**Problem.**
- Vikidia versus Wikipedia (0.34 Zipf) contrasts adult and children's encyclopedias, about 30 times the H2-H effect.
- Nothing shows the measure orders real French texts across ages 6–12, or how large one real year is.
- The years are model-internal, and the SESOI's "one year" is 0.04 Zipf on a planning slope, which is 0.8–1.6 years across models.

**Fix.**
- Run a sensitivity analysis with Manulex grade frequencies (already cited).
- Calibrate Zipf per year on a small graded corpus of human-written texts.
- Write "model-internal years" in the abstract.
- Justify the SESOI educationally.

### S3 (should-fix). Reasoning defaults and tiers confound "lighter models"

**Location.** Method "Models" and "Prompts" ("reasoning … default"); Results and Discussion on lighter models.

**Problem.** [checked in raw usage fields]
- Mean reasoning tokens per text:
  - Mistral Large 4: about 930–1,360 in every condition
  - Mistral Small 4: 0 everywhere
  - Claude Haiku 5.5: 163 (L1), 107 (L1P), 291 (L2), but 0 (L5) and 1 (L4). The label also switches Haiku's reasoning on.
- Tiers are not comparable. Mistral Large 4 replaced Mistral Medium 3.5 (design.json) and costs 0.7/2.1 USD per million tokens, against 2/10 for Sonnet 5.5 and GPT-6.1 Sol (models.json).
- 5 of the 6 model identifiers have no dated snapshot.
- The preregistered exploratory analysis "provider and model size" (PREREG Q8) is not reported, yet SI S1 says "All were run as registered".

**Fix.**
- Report reasoning tokens by model × label.
- Drop size language from the abstract and notes, or report the registered analysis with caveats.
- Correct S1.
- Give the snapshot status of each model.

### S4 (should-fix). Probe scoring and the mechanism claim

**Location.** Method "Knowledge probes"; Results ¶ on Table 3; Discussion probe paragraph.

**Problem.** [checked with analyze.parse_probe]
- The first-range rule catches contextual ages. Claude Sonnet 5.5's only P "error" reads "l'école enfantine, qui commence vers 4 ans. Les élèves de 5P ont donc environ 8 à 9 ans". At least seven "too young" errors are of this kind.
- 74 of the 177 wrong answers also state a correct range.
- The ±0.5-year tolerance accepts ranges one full year off ("11-12 ans" for 7H). That is 49 of 542 correct answers, including 52% of Mistral Small 4's correct ones.
- Haiku's mean error of 1.62 includes eleven answers 6–9 years too old (Belgian "humanités", French collège).
- One Mistral Large 4 answer cites the pre-HarmoS 1P–6P numbering. That numbering (primary counted from age 6, for example in Geneva until about 2011–2013; from memory, check) yields exactly the two-year error.

**Fix.**
- Double-code the answers (at least the 177 wrong ones and the 49 boundary cases) for the stated age and the school system invoked, and report agreement.
- Phrase the mechanism as "consistent with".
- Discuss the pre-HarmoS numbering.

### S5 (should-fix). H3 power is not reported

**Location.** Method "Analysis" ¶2; Results ¶2.

**Problem.** sim_power_results.json gives H3-H power of about .90 for half tracking (sigma 0.15, slope −0.04, 16 topics). Smaller departures, such as tracking 0.9, are not detectable.

**Fix.** Report the H3 power and the smallest detectable tracking change, and phrase the null accordingly.

### S6 (should-fix). Per-grade offsets are fitted endpoints without intervals

**Location.** Discussion "The average hides…" ("4.2… 0.1… 0.9 years too old at 3H and 1.8 years too young at 8H"); manuscript_numbers.py lines 288–298.

**Problem.** [checked: cell difference divided by the model's own slope, 2,000 topic resamples]
- Haiku: 3H 4.29 [3.30, 5.45], 8H −0.13 [−1.14, 0.88]. Consistent with the text.
- Mistral Small 4: 3H 1.75 [0.41, 3.27], 8H −0.76 [−1.99, 0.43]. The printed values are 0.9 and −1.8.

**Fix.** Report the observed per-grade values with CIs, or label the printed ones as fitted and give bootstrap CIs.

### S7 (should-fix). Length

**Location.** Results "Sensitivity"; Table S1.

**Problem.**
- The preregistered residualisation is fitted across grades, labels and topics, with slopes of −0.015 to −0.172 per log-word, so it absorbs part of the age gradient.
- Within model × label × grade × genre, with topic effects, the slope is −0.020 (SE 0.006). That implies only about +0.002 Zipf of bias in H2-H [checked].
- The text says the results "did not depend" on the sensitivity analyses, yet H2-P moved from −0.001 to −0.008.

**Fix.** Add a within-cell length adjustment, and describe how much the estimates moved, not just whether significance changed.

### S8 (should-fix). External validity of the conclusion

**Location.** Conclusion s1; Implications.

**Problem.** The study used one template, API calls with no system prompt, temperature 1.0 and default reasoning, in French, on 16 topics, mostly with undated model aliases. The Introduction's scenario is a chat interface.

**Fix.** Put these conditions in the conclusion sentence. If possible, add a second wording or a chat-interface replication.

### S9 (should-fix). Phrasing of prior work

[checked: full texts via alphaXiv; Avry via the EPFL page]
- **Imperial & Tayyar Madabushi.** "No model reached the target range under any wording" holds for the Flesch–Kincaid Grade 2 target in a story-completion task (continuing 50–70-word prompts). On CEFR A2, BLOOMZ and FlanT5 reached 0.76–0.85 accuracy (pp. 4–6). Write "asked to complete stories" and give the scope.
- **Rooein et al.** "Studies … agree that naming a level can move the output" does not fit their finding that ChatGPT did not move (no target significant; only GPT-3 moved slightly).
- **Avry (2023).** The survey covered 931 upper-secondary and private-school teachers in Vaud, February–March 2023, with no primary teachers. Say so where it supports the primary-teacher scenario.
- **Accurate as written:** Rooein (ChatGPT's narrow band; the limitation sentence), Huang (11–22% within the band, a skew toward harder texts, decodability and information load), Trott & Rivière (R² = .36), Farajidizaji (residual correlation with the source), Oh (above-grade outputs, fine-tuning).
- **Not checked:** Lété 2004, Peereman 2007, Brysbaert 2018, New 2004, Ripoll y Schmitz & Sonnleitner 2025, the cantonal and ministry pages, Vikidia.

## 4. Minor issues

- m1. Method, Prompts ¶ last: "Each model thus wrote 480 texts per topic". It is 80 per model per topic, 480 per topic across models.
- m2. Design ¶: the 252 pilot calls were 216 texts and 36 probes, not all age-only texts.
- m3. Table 3 caption, "Exploratory except the slopes": the L0 placement is a preregistered control.
- m4. "H in Fribourg": the H notation is also used in other cantons such as Valais, Neuchâtel, Jura and the Bernese Jura (from memory, check).
- m5. Intro, "Nothing in the text it returns would tell the teacher": 12–24% of texts name an age (Table S8).
- m6. Implications, "the second gave the most consistent texts": unclear referent. Name L3.
- m7. "Lighter", "smaller", "larger" and "mid-tier" are used interchangeably. Define one term by price.
- m8. Percentile bootstrap with 16 clusters may be narrow, and Luna's slope (−0.025) is near the −0.02 rule, which makes its ratio estimates unstable. Add BCa or studentised intervals.
- m9. Two copies of "Lexique 3.83" differ for 729 texts, by up to 0.13 Zipf (verification_report.md §2). Give the SHA-256 in the Method.
- m10. "No ruler departed from a straight line" should read "no significant departure". Figure 1 shows flat segments.
- m11. The Figure 1 x-axis labels age-only texts by H grade. Label by age.
- m12. Give the deposit time (about 07:52 UTC) and the run start (07:55 UTC) with the workflow run ID. AsPredicted shows dates only.
- m13. Outdated status lines: README ("before the deposit… Nothing here is a result"), PREREG.md ("not yet deposited"), verification_report ("RESULT PENDING").
- m14. No label × genre breakdown. Add it to the SI.
- m15. The text is about 5,950 words before references (my count). Move probe and per-grade detail to the SI to make room.

## 5. Questions a reviewer will ask

1. Why is the model's own age-only text the test of "understanding", when CE2 and the label with the correct age both depart from it?
2. Does mean lemma frequency register a misreading at all? Mistral Large 4 states P ages two years too old in about half its texts with no lexical shift.
3. How do the age-only texts compare with real French texts for ages 6–12, and how big is one real year on this measure?
4. Would the results hold in teachers' chat interfaces, with another wording, and with reasoning fixed?
5. What did Anthropic provide, which audited models took part in the research process, and how was that kept from shaping the Anthropic results?

## 6. What the paper rests on (neutral)

The confirmatory core (H1 and the four pooled tests) rests on the frozen measures and reproduces exactly. Every interpretive and practical claim rests on the age-only reference and on exploratory per-model comparisons, so that is where the revision has to work.

## 7. If you change three things

1. **Reframe.** Make the claims about lexical equivalence with each model's own age-only text, in model-internal years. Put model heterogeneity first and label everything exploratory (M1, M2, M4).
2. **Test the reference and the measure.** Use data already collected: L1/L1P against L4, the Mistral Large 4 reasoning traces, the absolute between-model spread, the Swiss-French decomposition and hand-coded probes. Add one external anchor, either Manulex or a graded corpus (M1, M3, S1, S2, S4).
3. **Rewrite the recommendations and statements.** Model choice matters more than label wording, so report results per model. Fix the COI and credits disclosure, the AI prompt disclosure, anonymity and the placeholders (M3, M5, M6).

## Checks I ran

- **Recomputation.** Ran analyze.analyze() in memory with python3 -B. It matches numbers.json and the manuscript.
- **Raw outputs.** Read the usage and reasoning fields in data/raw/calls_20261101T*.jsonl. Checked cost (41.12 USD), lengths, truncations (5) and flagged texts (11): all as reported.
- **Probes.** Re-parsed the answers and read every answer with an error of 3.5 years or more.
- **Re-measurement.** Re-measured all 7,680 texts with compute.py functions and the local Lexique copy. Scripts and output, outside the repository:
  - /tmp/r1_review/oov_check.py
  - /tmp/r1_review/lemma_check.py
  - /tmp/r1_review/lemma_check2.py
  - /tmp/r1_review/remeasured.csv

Nothing from the user's memory was used. I did not read the project memory notes, to keep this reading independent.

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Les scripts cités (/tmp/r1_review/oov_check.py, lemma_check.py, lemma_check2.py) sont gardés dans records/reader_scripts/r1/ ; remeasured.csv, une nouvelle mesure faite avec la copie pylexique du lexique, n'est pas gardé.)

## Vérification des couples phrase et citation (P6.2), rapport complet (lancée à 12:31, reçu à 13:05, 109 appels d'outils, claude-sonnet-5-5), texte intégral

Internal reading by a separate AI session. Not peer review.

RESULT. All 44 pairs were read at the passage level. 37 supports, 7 partly supports (n10, n18, n25, n30, n31, n33, n40), 0 does not support, 0 cannot check. No pair rests on an abstract, a snippet or a summary. Numbers taken from sources match: 52% and 24% (EPFL) for "about half" and "a quarter"; 4 years on 31 July and 8 years (HarmoS); ages 8 to 12 (three cantonal pages); Zipf 1-3 and 4-6; Vikidia 8 to 13; 30-40% (Brysbaert); R2 = .36 (Trott); eight secondary measures (count checked); one-sided sign test 28 of 29 gives p = 5.6e-8. Three figures are derived, not stated by the cited page: "8 or 9 in 5H", "10 to 11 in CM2", "5e = second year". One is not in the cited source: "Lexique 3.83".

ACCESS CODES (all count as read-directly; none abstract-only; none not accessible)
- RD-full: whole text read as raw text.
- RD-pages: the listed PDF pages read as raw text.
- RD-raw: web page returned in full as raw text (alphaXiv).
- RD-web: web page read through WebFetch, which passes the page through its own small model and returns short "verbatim" sentences. I did not see the raw HTML for these six pages (EPFL, vd.ch, ge.ch, two MEN pages, Vikidia).
Rows are grouped by source. Page numbers are those of the printed article unless stated. For Trott, Primpied, Rooein, Huang and Farajidizaji I give sections, not pages.

TABLE (n | key | access | location | quote | verdict)

| n | key | access | location | quote (max 15 words) | verdict |
|---|---|---|---|---|---|
| 1 | avry2023 | RD-web | EPFL news page (S. Avry, 18.07.2023), results paragraph | "24% have done so as part of their teaching, primarily for lesson preparation" | supports. 52% had used it, 24% of users. Wording W1 |
| 2 | imperial2023 | RD-pages (pp. 205-206, 208-212, 218-219, 222) | p. 206, section 2.1 | "often used and suggested by academic groups for teachers and educators" | supports. Wording W2 |
| 5 | imperial2023 | RD-pages | p. 208 section 3.2; p. 209 | "none of the models in any of the prompt iterations ... achieved acceptable performance" | supports. Target 1 < FKGL < 3; ChatGPT 8.832 (no level) to 5.155 (grade named). Wording W5 |
| 12 | imperial2023 | RD-pages | p. 209; Table 3 p. 218; Table 2 p. 210 | "mean trend of 8.832 → 5.155 → 5.224 → 4.567" | supports. Wording W12 |
| 38 | imperial2023 | RD-pages | p. 209 | "none of the models were able to provide generations within the acceptable boundary for FKGL" | supports (the "above the target" half; the "little change" half is Rooein, n39) |
| 3 | rooein2023 | RD-full | section 3.1; Table 4 | "ChatGPT generates responses that are in a narrow range of FKRE scores" | supports. Table 4: ChatGPT FKRE 16.84-17.63 across all age targets |
| 13 | rooein2023 | RD-full | section 3.1; Table 4 | "a particular "style" that is largely independent of prompting for age or education level" | supports. Wording W13 |
| 18 | rooein2023 | RD-full | Limitations (after Ethical Considerations) | "FKRE and FKGL are desigend for the US education system and English" | partly supports. See C-n18 |
| 39 | rooein2023 | RD-full | section 6 Conclusion | "not hugely affected by prompting for specific age or education groups" | supports (Rooein half of the sentence) |
| 4 | huang2024 | RD-full | section 3.5; captions of Figs. 2-3 | "the generated texts are generally more complex than the intended level" | supports. Wording W4 |
| 14 | huang2024 | RD-full | section 3.5; Table 1 | "a higher proportion of the data points are located above the red-shaded area" | supports. Match within +/-50 L is 11.00% to 22.22% over the six settings; three models |
| 27 | huang2024 | RD-full | section 3.1 | "readability relies on many specific features, such as decodability [19], information load [15]" | supports. Huang relays the Lexile Framework and refs 10, 11, 15, 19; not its own finding |
| 41 | huang2024 | RD-full | section 1; section 3.1 | "with sentence length and word frequency identified as key factors in previous studies" | supports |
| 6 | harmos2007 | RD-full (all 7 pages) | Art. 5 al. 1 and Art. 6 al. 1, p. 3 | "dès l'âge de 4 ans révolus (le jour de référence étant le 31 juillet)" | supports. Art. 6 al. 1: "école enfantine ou cycle élémentaire inclus, dure huit ans". Wording W6 |
| 7 | fr_cycle2 | RD-raw | Chapeau; Grilles horaire; Organisation | «1H à 11H» ; «entre 8 et 12 ans» ; «de la 5 à la 8H» | supports. Wording W7 |
| 8 | vd_deroulement | RD-web | cycles section | "le cycle moyen (5P à 8P) pour les élèves de 8 à 12 ans" | supports (1P-8P: "huit années") |
| 9 | ge_primaire | RD-web | heading "Deuxième cycle primaire (5P - 8P)" | "Ce cycle accueille les enfants en principe âgés de 8 à 12 ans" | supports (entry "4 ans révolus au 31 juillet" also stated) |
| 10 | men_elementaire | RD-web | "L'école élémentaire", classes and ages (updated July 2024) | "L'école élémentaire accueille les enfants scolarisés de 6 à 11 ans." | partly supports. See C-n10 |
| 40 | men_elementaire | RD-web | same page, classes | "L'école élémentaire comprend les classes du CP au CM2." | partly supports. See C-n40 |
| 11 | men_college | RD-web | "Le collège" (updated May 2024) | "quatre années : la 6e, la 5e, la 4e et la 3e" | supports. Wording W11 |
| 29 | men_college | RD-web | same page | same passage | supports. Wording W11 |
| 15 | oh2026 | RD-pages (arXiv v2 pp. 1-3, 5-6, 8-9, 13, 17-20, 22) | Introduction, p. 1 | "LLMs generate responses that systematically exceed the target grade's comprehension level" | supports. Stated as background (ref. 17); the abstract reports +35.64 points against prompting |
| 16 | trott2024 | RD-full | section 5 Discussion (also sections 2, 4.4) | "a correlation between the readability of the original text passage and the modified passage" | supports |
| 21 | trott2024 | RD-full | section 3.4 Results | "explained approximately 36% of the variance in human readability judgments (R2 = 0.36)" | supports. Wording W21 |
| 17 | farajidizaji2023 | RD-full | section 6 Results and Discussion; Fig. 3; Table 5 | "albeit correctly ordered, is highly correlated with the source text readability" | supports. Abstract and section 8 say the same |
| 19 | ripoll2025 | RD-pages (PDF pp. 1, 4, 8, 13-16, 22, 24, 27 of 29) | p. 13; abstract p. 1 | "the suitability of the texts for the reading-levels of fifth-graders in Luxembourg" | supports. GPT-4, German texts, blinded online review, N = 89 (abstract) |
| 44 | ripoll2025 | RD-pages | p. 8, Methods | "Native German speakers, teachers, and test developers partook in an online survey" | supports as a contrast: adult raters, no pupils |
| 20 | brysbaert2018 | RD-full (accepted manuscript; pagination differs from the journal) | p. 3 | "Word frequency typically explains some 30-40% of the variance in word recognition tasks" | supports |
| 23 | brysbaert2018 | RD-full | p. 6 | "The lower half of the scale (1-3) represents the low-frequency words" | supports. Upper half 4-6 = high frequency; Zipf = log10 (frequency per billion words) |
| 32 | brysbaert2018 | RD-full | p. 6 | "Zipf = log10 (frequency per billion words)" | supports (the Zipf part only; the averaging of two corpora is the study's own, see n33) |
| 34 | secondary: van Heuven et al., 2014 | RD-full (secondary only) | Brysbaert et al., p. 6 | "van Heuven, Mandera, Keuleers, and Brysbaert (2014) proposed the Zipf scale as an alternative" | supports: the secondary attributes the scale and formula to the primary. Primary not opened |
| 22 | manulex2004 | RD-pages (pp. 156-163, 165) | p. 162, Table 3 and text | "An important drop is observed at level G3–5" | supports. Lemma mean SFI: G1 48, G2 45, G3-5 39 (lower = harder) |
| 24 | manulex2004 | RD-pages | p. 159 Corpus Sampling; Table 1 p. 161 | "compiled from reading, spelling, and grammar books by the leading French publishers" | supports. Frequencies for G1, G2, G3-5, G1-5 |
| 42 | manulex2004 | RD-pages | p. 157; abstract p. 156 | "The use of word frequency norms computed from adult corpora raises problems" | supports (grade-level norms exist) |
| 25 | new2004 | RD-full (pp. 516-524) | pp. 516-518 | "two cues: a contemporary corpus of texts and the number of Web pages" | partly supports. See C-n25 |
| 30 | new2004 | RD-full | p. 517, Tables 1-2 | "Lemmes presents an inflectional family organization" | partly supports. See C-n30/31 |
| 26 | newpallier_manual | RD-pages (pp. 1-15, 17, 20-23, 26) | section 3 end p. 8; Tableau 1 legend p. 9 | "freqlemfilms: la fréquence du lemme selon le corpus de sous-titres (par million d'occurrences)" | supports. freqlemlivres gives the same for books |
| 31 | newpallier_manual | RD-pages | p. 2; pp. 10-11, Tableau 3 | "ADJ Adjectif ... NOM Nom commun ... VER Verbe" | partly supports. See C-n30/31 |
| 33 | newpallier_manual | RD-pages | section 2.1 p. 6; Tableau 1 legend p. 9 | "218 textes littéraires (romans) publiés entre 1950 et 2000" | partly supports. See C-n33 |
| 28 | peereman2007 | RD-pages (pp. 579-582, 587) | p. 580 (and p. 579) | "word frequency is obviously not the sole factor of performance" | supports for "not the only factor" and decodability (grapheme-phoneme consistency, p. 579). Wording W28 |
| 43 | peereman2007 | RD-pages | p. 579 | "based on adult-directed written material ... that makes them unsuitable for studying literacy acquisition" | supports. The passage names Lexique 2 (New et al., 2004) among these databases |
| 35 | vikidia_about | RD-web | "Vikidia:À propos" | "une encyclopédie en ligne, libre et participative, pour les 8-13 ans" | supports. 28/29, p < .001 and 0.34 are the study's own results; the sign-test arithmetic holds |
| 36 | primpied2022 | RD-full | section 3 Metrics; Table 4; Eq. 3.1 | "his adaptation in French the Kandel and Moles formula [22]" | supports. The sentence lists eight measures (count checked) |
| 37 | secondary: Kandel & Moles, 1958 | RD-full (secondary only) | Primpied section 3; reference [22] | "Application de l'indice de Flesch à la langue française" | supports: the secondary attributes the French adaptation to Kandel & Moles; its reference list prints 1958. Primary not opened |

PAIRS THAT NEED A CHANGE (partly supports), one-line corrected wording

- C-n10. The page gives CP to CM2, cycle 2 = CP, CE1, CE2, and one 6-to-11 age band for the whole école élémentaire. It gives no age per class and no link to 5H. "8 or 9" and "5H = CE2" are derived (HarmoS entry age plus counting; inference). Write: "...is thus 8 or 9 years old in 5H, which is the third class of the French école élémentaire, CE2, if CP starts at six (class order and 6-to-11 range: Ministère de l'Éducation nationale, 2024a)."
- C-n40. The fifth class = CM2 is on the page. "Aged 10 to 11" is not. Write: "the fifth year of the French école élémentaire is CM2 (Ministère de l'Éducation nationale, 2024a), the grade of pupils of about 10 to 11 if CP starts at six, two years above 5H."
- C-n18. Rooein's note is that paper's own caveat and covers FKRE and FKGL only, not Lexile or CEFR. "Their own authors" can be read as the formulas' authors or as every study's authors. Write: "The readability measures most used, Flesch–Kincaid reading ease and grade level, are formulas built for English and for the United States school system, which Rooein et al. (2023) themselves note are unlikely to translate without adaptation to other countries, languages and education systems." Optional second source: Ripoll y Schmitz & Sonnleitner (2025, p. 15) deemed Flesch-Kincaid and the Wiener Sachtextformel unsuitable for transfer to Luxembourgish students.
- C-n25. New et al. (2004) describes Lexique 2: frequencies from Frantext texts after 1950 (487 texts, mostly novels and essays, 31 million words) and from Web-page hit counts. No film subtitles. Subtitle frequencies come with Lexique 3 (manual p. 4; New et al., 2007). Lexique 3's novel corpus is different (218 novels, 14.7 million words, manual p. 6). Write: "For French, the Lexique database gives lemma frequencies from novels (New et al., 2004, for Lexique 2) and, from version 3, from film subtitles (New & Pallier, n.d.)." Optional: add New et al. (2007), which the manual cites on p. 6. I did not read it.
- C-n30/31 (same sentence). "3.83" appears nowhere in the manual (documentation version 3.2; it mentions database versions up to 3.7 and the change at 3.40). New et al. (2004) is Lexique 2. The "most frequent lemma" rule, the content-word rule and the exclusion list are the study's own. The manual supplies only the lemme and cgram fields and the NOM, ADJ, VER codes. Write: "...in the French lexical database Lexique, version 3.83 [state where the file comes from] (New & Pallier, n.d.; New et al., 2004, for Lexique 2). We read each word form as its most frequent lemma and counted as content words the forms read as nouns, qualifying adjectives or verbs, without ..."
- C-n33. The manual gives the two corpora and the per-million unit as two separate fields (freqlemfilms, freqlemlivres). It defines no combined frequency, so the mean is the study's definition. Write: "We took a lemma's frequency as the mean of its two frequencies per million words in Lexique, from film subtitles and from novels published from 1950 to 2000 (New & Pallier, n.d.), expressed on the Zipf scale ..."

WORDING NOTES ON PAIRS MARKED SUPPORTS (optional)
- W1 (n1): the page says "public high schools and private institutions". "Upper-secondary" is an inference from the post-compulsory directorate named as partner. The figures come from the news page; the two linked survey reports were not opened.
- W2 (n2): say "as described by Imperial & Tayyar Madabushi (2023, p. 206), who cite Staake (2023) and Herft (2023)". The advice documents themselves were not opened.
- W4 (n4): "tended to overshoot it" -> "tended to produce texts harder than the target". The skew is upward whatever the direction of the request.
- W5 (n5): the claim holds on Flesch–Kincaid grade level (Grade 2: 1 < FKGL < 3). On CEFR several models did well (BLOOMZ 0.84 for A2), so keep "no model reached the target range" tied to Flesch–Kincaid.
- W6 (n6): "children in Switzerland" -> "children in the cantons that joined the agreement" (Art. 1 and 13 "cantons concordataires"; the text does not list them). The PDF is the canton of Fribourg's compilation of the CDIP text (version in force 1.5.2010).
- W7 (n7): "Counting from the first year of kindergarten" is not on the fr.ch page. It rests on HarmoS Art. 6 al. 1, so add CDIP, 2007 there.
- W11 (n11, n29): "second year" is read from the listed order 6e, 5e, 4e, 3e. The page writes neither "deuxième année" nor ages.
- W12 (n12): "describing the level" -> "describing the scale". The added text was "The Flesch-Kincaid Grade scale looks at total words, total sentences, and total syllables".
- W13 (n13): "did respond to age" -> "responded slightly". The paper says "only GPT3 slightly decreases" (Table 4: 41.86 to 32.82). ChatGPT and GPT-3 both being OpenAI models is known fact, not stated in the paper.
- W21 (n21): "about a third" -> "about 36%". The judgments are teachers' pairwise ratings of 4,724 excerpts (CLEAR, section 3.1), not general readers' judgments.
- W28 (n28): Peereman covers "frequency is not the only factor" and decodability. Sentence length and information load rest on Huang alone.

SOURCES OR PARTS I COULD NOT OPEN
- Oh et al. publisher page (doi.org/10.1038/s44387-026-00081-7): WebFetch returned client_error. I read arXiv v2 (2601.06225v2, "published in npj Artificial Intelligence (2026)") and did not compare it with the version of record. I did not resolve the DOI.
- Ripoll y Schmitz & Sonnleitner article HTML page: WebFetch returned PROVENANCE_REQUIRED. I read the open-access PDF instead (pages listed above).
- fr.ch via WebFetch: PROVENANCE_REQUIRED. The raw page text came through alphaXiv. alphaXiv failed on the two education.gouv.fr pages and on Vikidia, so WebFetch was used for those.
- Primary documents behind "as cited in" and inner citations, not opened: Kandel & Moles (1958), van Heuven et al. (2014), Staake (2023), Herft (2023), New et al. (2007), and the two EPFL survey reports linked from the news page.
- Crossref, OpenAlex and Scite were not used. Scite is unavailable; the other two were not needed.

DISCLOSURES AND OBSERVATIONS
- The recorded access for new2004 ("not accessible in full text", G2 exception) is outdated. I read the full article (Springer PDF, pp. 516-524) through alphaXiv.
- RD-web rows: see the access codes above. Re-reading the raw pages of those six sources would remove the model layer.
- A Grep I ran for the Kandel–Moles coefficients also printed a few matching lines from manuscript/literature (litnotes.md, search_log.md, sources.csv; the earlier session's notes). I did not open those files and used nothing from them. My reading of Primpied was done before that grep.
- Kandel–Moles code check (inference): Primpied Eq. 3.1 gives 207 − 1.015 × MLS − 0.736 × MNS without defining MNS's unit. compute.py line 365 uses 207 − 1.015·wps − 73.6·(syllables per word). That equals 0.736 per 100 syllables. It matches Primpied only if MNS is syllables per 100 words (classic form; the 1958 original was not opened).
- Not in the brief: the stray "593-603" in the first-page text of the Peereman PDF is a text-layer glitch. Springer's article page gives pages 579–589, as in references.json.

POSSIBLY WORTH SAVING (tool notes, learned this session)
- alphaXiv answer_pdf_queries reads Springer PDFs (link.springer.com/content/pdf/...) and open-access publisher PDFs when WebFetch returns PROVENANCE_REQUIRED.
- WebFetch with verbatim-quote prompts works for education.gouv.fr and Vikidia, where alphaXiv fails.

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Les textes intégraux que la session a extraits (scratchpad/p6_verifier/tr/) ne sont pas versés au dépôt pour des raisons de droits ; la liste des 44 couples vérifiés est dans p6_pairs.json.)

## R2, rapport complet (lancée à 12:32, reçu à 13:15, 146 appels d'outils, claude-sonnet-5-5), texte intégral

Internal reading by a separate AI session. Not peer review.

R2 report: methods and statistics, ART 5 audit.
Object: /home/claude/art5-harmos-audit, read only (tag `prereg` = 6a0a061). Rendered texts cited as M:line (manuscript/build/manuscript.md) and S:line (manuscript/build/supplement.md). Scratchpad files read: r2.md, common.md and my own files under r2_work/ only.

Summary: 1 must-fix, 8 should-fix, 14 minor. Every reported number I could recompute reproduces. The problems are the compliance statements and how pooled results are worded.

## 1. How I checked, and what I could not check

Checked by re-running or independent recomputation (copy of the repo in r2_work/repo; nothing written to the repo):
- analyze.py re-run on results/measures.csv: numbers.json identical. manuscript_numbers.py regenerated: manuscript_numbers.json identical. check_numbers.py passes.
- The four primary tests re-implemented without importing analyze.py. All Table 2 values reproduce: H2-H -0.011749, t(15) -3.7186, p .002059, CI [-0.01848, -0.00501], Holm .00824; H2-P -0.000761, p .8647; H3-H 0.002686, p .2644, Holm .5288; H3-P 0.004025, p .0677, Holm .2031. Sign-flip permutation p: .0035, .869, .266, .069. Shapiro-Wilk p: .086, .083, .061, .136.
- H1 re-implemented (OLS, genre and topic effects, CR1 clustered by topic, one-sided t(15)): slopes -0.0246 to -0.0489, p from 3.2e-9 to 1.6e-5. Wild cluster bootstrap p <= .0006.
- 45 table rows (Table 2, S1, S2, S4, S5, S6) recomputed independently and string-compared with the rendered tables: all match. The same script fails on a copy with a planted fault (r2_work/plant).
- Bootstrap of shift and tracking re-implemented. With the registered seed and RNG order it reproduces the reported L1P tracking interval [0.814, 0.9947] exactly.
- sim_power.controls() and grid() re-run: identical to sim_power_results.json (power .835, .974, .994 for T = 16, 24, 32). pilot_summary.json reproduced (sigma .11686, df 192, upper 80% .12228).
- Probe answers re-parsed with an independent parser: first-range correct, any-range correct and mean error agree with the pipeline in all 12 model x notation cells. 719 of 720 answers parsed.
- Data: 7,680 unique model x label x grade x genre x topic cells, 192 per label x grade (L6 at 3H to 5H only, L0 192), no missing values, 7,680 distinct text hashes.
- Git: analyze.py, compute.py, sim_power.py, make_prompts.py, design.json, generate.py, pipeline.py and PREREG.md are identical at tag prereg (2026-11-01 07:29:40 +01:00) and HEAD. HEAD adds exploratory.py, figures.py, manuscript_numbers.py, a workflow and CHANGELOG lines. The first confirmatory raw file is stamped 2026-11-01 07:55:47Z, after the tag (06:29:40Z).

Not possible or not done:
- I could not reproduce measures.csv from the raw texts with the official lexique.org file (SHA-256 637ba37a...). It is unreachable from my sandbox, as the CHANGELOG says of the authors' sandbox. With the pylexique package's lexicon copy (fe2cb931...), 6,951 of 7,680 text measures are identical and 729 differ. Primary results under that copy: H2-H -0.01146 (Holm .0091), H2-P -0.0004 (.928), H3-H 0.0027 (.505), H3-P 0.00405 (.209). Same conclusions. The authors' GitHub Actions run on the official file is the only evidence in the repository for that step.
- The AsPredicted record (#321415) is not in the repository. I cannot check that the deposited text equals PREREG.md at the tag, nor the deposit time. The data-v1 tag named in figures.py is not in this checkout (only `prereg`); manuscript/verification_report.md says it exists on the remote.
- I did not re-fetch the Wikipedia and Vikidia texts. From the stored pairs I recomputed 28 of 29 usable pairs, one-sided sign test p = 5.6e-8, mean difference 0.341. The 29th-vs-30th pair is excluded by a mechanical 100-word rule in validate_measure.py.
- No model-provider calls. The generate, pilot, list-models and validate steps were not run.

"Inference" below marks my reasoning, not something I computed.

## 2. Findings

### Must-fix

**M1. "All were run as registered" and "there were no deviations" contradict PREREG.md**
- Where: S:8 ("All were run as registered"); S:20 (table row "Exploratory: per-model and per-grade contrasts, L2, L4, H against P"); M:203 ("there were no deviations").
- Problem and evidence (PREREG.md lines 124-127 read against the manuscript, supplement, numbers.json and exploratory.json by grep):
  - The registered exploratory list contains "provider and model size". It is reported nowhere. No table, number or sentence compares providers or the balanced and light tiers. The manuscript only calls the two poor followers "the lighter model of their provider" (M:179).
  - "H against P" (S:131-132, rows "« de 5P » − « de 5H »") is reported, and S1 maps it to the registration. The registered list does not contain it.
  - Two choices behind reported numbers were made after the deposit and are not named in S1: the 1.5 to 2.5-year window behind "86%" (M:181, from exploratory.py) and the line-implied per-grade offsets (M:179).
  - S1 does disclose that exploratory.py computed the probe-error direction and the age and grade mentions after the deposit. That disclosure is accurate.
- Why it matters: the registration is the study's main safeguard and its text is public. A categorical sentence that a reader can falsify against Q8 in a minute costs more credibility than the two small departures it hides.
- Fix: replace both sentences with an itemised statement, for example "Two departures from the registration: the exploratory analysis by provider and model size was not run; the contrast L1P − L1 was added after the deposit." Name the other post-deposit choices. Mark the L1P − L1 rows of Table S5 "not registered". Either add a short descriptive provider and tier table (six models, so descriptive only) or drop the registered item explicitly.

### Should-fix

**S1. The only significant primary test, and the H3-P near-miss, each rest on one model; between-model heterogeneity is not reported where pooled statements are made**
- Where: M:8 (Abstract sentences 4-5); M:121 and M:123; M:173; M:197.
- Evidence (loo_model.py, disp_check.py; topic-level two-sided p, uncorrected):
  - H2-H without Claude Haiku 5.5: +0.0041, p = .297, sign reversed. Without any other single model: p <= .022 (estimates -0.0076 to -0.0179).
  - H3-P with all six: p = .068. Without Mistral Small 4 (gradient +0.0283): -0.0008, p = .672. Without Mistral Large 4: p = .007. Without GPT-6 Luna: p = .009.
  - Per-model H2-H levels (Table S4) run from -0.091 to +0.019. Their SD is 0.043 Zipf, 3.7 times the pooled -0.012. The SD of the six per-model shifts for the bare H label is 1.07 years (bootstrap 95% [0.88, 1.36]); for tracking, 0.50 [0.39, 0.69].
  - The pooled H3 values average two directions. Four models over-track the H label (gradients -0.0077, -0.0098, -0.0104, -0.0095; Sol and Luna exclude 0, uncorrected). Two under-track (Haiku +0.0351, Mistral Small 4 +0.0184; Table S4).
  - Descriptive generalisation check, six per-model estimates treated as a sample (t(5)): H2-H -0.012 [-0.057, +0.034]; H2-P -0.001 [-0.012, +0.011]; H3-H +0.003 [-0.018, +0.023]; H3-P +0.004 [-0.012, +0.020].
- Why it matters: the Method says inference is conditional on these six models (M:98). The Abstract and Conclusion carry the pooled statements without that condition. Positive and negative per-model deviations cancel: the pooled shift is 0.30 years, the mean of the six per-model shifts is 0.21 and their median -0.19.
- Fix: add one Results sentence, "Without Claude Haiku 5.5 the pooled H2-H difference is +0.004 Zipf (p = .30)", and the between-model SD of shift and tracking. Write "for these six models" and "on average" into the Abstract and Conclusion. Keep the leave-one-model-out and models-as-sample numbers in the Supplement, labelled exploratory.

**S2. Equivalence and absence-of-evidence statements go beyond what was registered and powered**
- Where: M:8 ("below the smallest effect of interest", "the P label showed no difference; neither label changed how texts followed the grade"); M:121 ("its interval excludes differences as large as the smallest effect of interest in either direction"); M:123 ("Neither label changed how texts followed the grade"); M:173; M:193 ("The study was powered for the pooled tests").
- Evidence:
  - (i) No equivalence margin or test is in PREREG. 0.04 Zipf is the effect used for the sample-size simulation (Q7), then used as an equivalence margin with no argument that one year on a model's own ruler is negligible for a teacher. Table S6 has the H label at 3H at -0.030 [-0.052, -0.008], about 0.75 year.
  - (ii) The registered power calculation covers H2-H only (Q7). H3-H and H3-P, two of the four primary tests, have no margin and no power statement in the paper. The upper gradient limits (0.0076 and 0.0084 Zipf per year) times the 5-year span from 3H to 8H are 0.038 and 0.042 Zipf, which is the SESOI itself. The lower limits of tracking are 0.82 and 0.81.
  - (iii) H3-P is fragile (loto.py). Leave-one-topic-out p runs from .008 (without "des saisons"; that value would pass Holm) to .124 (without "des abeilles"). The gradient is positive in 12 of 16 topics.
  - For comparison: the equivalence reading for the P-label level survives treating models as a sample (CI ±0.012, inside ±0.04). The H-label reading does not (S1).
- Why it matters: "not significant" with 16 topics is read as "no effect" for gradients and as equivalence for levels.
- Fix: write "did not detect" for H3 and for the P level unless a margin is stated with its reason. If equivalence is claimed, name the margin and the interval used (90% for TOST; 95% is conservative), and apply it to the H3 bounds expressed over the grade span. Restrict M:193 to "powered for H2-H".

**S3. "The primary results did not depend on the analytic choices" is contradicted by the length row of Table S1**
- Where: M:167 (first sentence and the length sentence); S:33-38.
- Evidence: the length-residualised row gives H2-H -0.017 (primary -0.012), H2-P -0.008 with p = .077 (primary -0.001, p = .865), H3-P p = .077 (primary .068). The bare labels give texts about 35 words shorter than age-only texts (Table S2, p < .001). Within model, mean Zipf falls with length (slopes on log words -0.016 to -0.172 by model). The L5-only slope within model x grade x genre x topic cells is +0.005 (SE 0.014), against -0.038 (naive SE 0.007) within the same cells over L1, L1P and L5. Length is therefore not separable from the label effect with these data. Inference: length plausibly lies on the causal path, since labels change length and lexical level together. I did not test this.
- Why it matters: the P-label conclusion ("no difference") changes under the registered length adjustment, while the first sentence of the paragraph says nothing changes.
- Fix: rewrite it, for example "Removing truncated, duplicate or flagged texts and clustering by topic changed nothing; holding length constant enlarged the H difference (-0.017) and moved the P difference to -0.008 (p = .077)". Do not present the adjusted row as the better or worse estimate.

**S4. "Stops just below 1" is a Monte Carlo accident**
- Where: M:123 (last sentence); Table 2 last column ("0.90 [0.81, 0.99]"); Figure 2.
- Evidence (boot_mc.py, boot_check.py): the registered seed (20261025, B = 2000) gives 0.9947, reproduced exactly. Across 200 other seeds at B = 2000 the upper limit has mean 1.001, SD 0.0035, range 0.9915-1.011, and is below 1 in 43% of seeds. Converged (B = 400,000): [0.815, 1.0013], P(resampled tracking >= 1) = .026. BCa [0.822, 1.014]. Jackknife-SE with t(15) [0.796, 1.000]. The H label's limit is not at the boundary ([0.823, 1.046]; converged 1.040).
- Why it matters: a qualitative contrast ("excludes 1") hangs on the third decimal of a limit that changes with the seed. The text already calls the evidence weak, and the sentence suggests a boundary the data do not locate.
- Fix: report "0.90 [0.81, 1.00]" and say the upper limit is at 1. Delete "stops just below 1". If B = 2,000 stays the registered rule, add a B = 100,000 line in the Supplement as a precision check.

**S5. "Most consistent" and "narrowed the differences between models" rest on an unregistered, unnamed dispersion measure, and L3 ties with other wordings**
- Where: M:8; M:22; M:185; M:189 ("of the wordings that contained a label, the second gave the most consistent texts across models"); M:197 ("the wording to recommend in teacher education and to build into classroom tools").
- Evidence (disp_check.py; SD across the six per-model point estimates; bootstrap over topics):
  - Shift SD: L1 1.07, L1P 0.28, L2 0.87, L3 0.28, L4 0.42.
  - Tracking SD: L1 0.50, L1P 0.45, L2 0.22, L3 0.21, L4 0.26.
  - L3 ties L1P on shift and L2 on tracking. L3 is tighter than L1: SD difference in shift 0.79 years [0.49, 0.98], in tracking 0.29 [0.14, 0.38]; without Haiku 0.59 against 0.24. These SDs include the sampling error of six estimates.
  - L3 is also consistently offset: all six per-model shifts are negative (-0.11 to -0.96), pooled -0.46 [-0.62, -0.33].
- Why it matters: the Conclusion recommends a wording for teacher education from an exploratory comparison that holds against the bare H label only.
- Fix: name the metric, give the SDs for all five wordings, state the ties, label it exploratory. In the Abstract write "relative to the bare HarmoS label". Soften M:197 to "reduced the spread between models relative to the bare H label (exploratory)".

**S6. "Two lighter models" is a post hoc grouping**
- Where: M:8; M:21; M:144 (heading) and M:146; M:179 ("both the lighter model of their provider"); M:197.
- Evidence (Tables S3, S4, S7):
  - GPT-6 Luna, the third lighter model, has H shift -0.77 [-1.48, -0.22] and tracking 1.42 [1.10, 2.01]. That is a deviation of the size of Mistral Small 4's (shift -0.49, tracking 0.46) in the other direction, yet Luna is counted among the models that "followed ... at least as steeply" (M:146). Its tracking interval, and GPT-6.1 Sol's [1.03, 1.41], exclude 1 from above.
  - Mistral Large 4 (balanced tier) has H2-H -0.033 [-0.052, -0.013], the second-largest level difference, shift +0.79, and 62% first-range probe accuracy against Haiku's 65%. Luna's probes are 100% correct.
  - No tier contrast is reported (M1), no criterion for "followed poorly" is stated, and with three tier pairs the contrast cannot be separated from provider.
- Why it matters: it offers a cause (model size) that the design cannot test, in the Abstract.
- Fix: name the two models, or write "two of the three lighter models". State a criterion and apply it to all six; it must say what to do with the over-tracking of Sol and Luna. Present size as a hypothesis, not an explanation.

**S7. The effect of "en Suisse romande" is quoted against the wrong reference**
- Where: M:137 (first sentence: "Adding « en Suisse romande » to the H label made the texts older, with a shift of 0.87 years"); M:185 ("made texts harder by almost a year").
- Evidence (l2l1_len.py): 0.87 years is L2 against the age-only text. The effect of adding the region to the H label is L2 − L1: -0.0224 Zipf [-0.0309, -0.0139], t(15) = -5.62, and a pooled shift difference of +0.57 years [0.37, 0.81] (same bootstrap). By model, L2 − L1 level: Sonnet -0.040, Mistral Large -0.035, Mistral Small -0.042, Luna -0.016, Sol -0.004, Haiku +0.004. The same applies to L3: -0.46 years against the age, -0.76 [-0.89, -0.64] against L1.
- Why it matters: the sentence attributes to the added words a shift that includes the 0.30 of the bare label. The Discussion headline overstates the effect by about half.
- Fix: report L2 − L1 and L3 − L1 (Table S5 has L3 − L1 in Zipf but not L2 − L1). Write "about half a year harder than the bare label" in M:185, and say the effect is absent for Haiku and Sol.

**S8. "Each model thus wrote 480 texts per topic" is wrong**
- Where: M:76 (second sentence); source manuscript/manuscript.md:68 ({{texts_per_topic}}); manuscript_numbers.py:155 (texts_per_topic = n_texts // n_topics).
- Evidence (measures.csv): 480 texts per topic over the six models (PREREG Q4 states it correctly), 80 per model and topic, 1,280 per model.
- Why it matters: a numeric misstatement in the Method that check_numbers.py cannot catch. It verifies that a digit string comes from the dictionary, not which quantity the sentence assigns it to.
- Fix: "Each topic thus received 480 texts, 80 from each model; each model wrote 1,280 texts, 7,680 in all."

### Minor

**m1. Power assumptions undisclosed; the simulation is about three times more variable than the data** (M:100; PREREG Q7; M:193)
- Evidence (sim_repro.py, power_check.py): .835 reproduces exactly at R = 1000. With R = 4000 and seeds 11 to 13 it is .853, .863, .859; the MC SE of .835 at R = 1000 is .012.
- Besides sigma, the simulation assumes a label-by-topic SD of 0.02, a prompt effect shared by the six models with SD 0.05, t(5) noise and 2% missing (sim_power.py header). The pilot held only L5 texts (PREREG Q8), so the first two could not be estimated.
- Simulated SD of the topic-level H2-H level is 0.040 (0.021 from sigma alone); observed 0.0126. Gradient: 0.0167 simulated, 0.0093 observed. The confirmatory L5 residual SD is 0.104 (pilot 0.117).
- Planning was conservative and the results are not harmed, but ".835" cannot be reproduced from the Method's description.
- The PREREG Q7 pilot slope p ("one-sided p < .001") used HC3 with a normal reference. The topic-clustered t(5) gives 1.7e-6. No impact.
- Fix: add "(plus assumed label-by-topic and prompt variation, SD 0.02 and 0.05)" to M:100 and state the realised SD. Restrict M:193 to H2-H (see S2).

**m2. L0 and L6 age equivalents: no intervals, and extrapolation** (M:139; Table 3)
- Evidence (l0_check.py, same topic bootstrap), L0 default age: Sonnet 10.53 [9.91, 11.12]; Haiku 11.33 [10.84, 11.89]; Mistral Large 11.18 [10.32, 12.39]; Mistral Small 11.66 [10.36, 13.24] (point above the ruler's top, 11.5); Sol 10.53 [10.06, 11.00]; Luna 9.40 [8.47, 10.66]. Each rests on 32 texts per model.
- L6: the pooled shift 5.62 puts readings at about 12 to 14 years. Per model, up to 16.3 (Mistral Large 4, shift 7.84), 4.8 years above a ruler that ends at 11.5. The isotonic reading (3-year cap) gives L6 tracking -0.45 against -0.92 (numbers.json).
- Fix: give intervals for L0. State that L6 years are linear extrapolations and lead with the Zipf difference (-0.221 [-0.252, -0.191], Table S5).

**m3. Per-grade offsets for Mistral Small 4 are fitted-line values** (M:179)
- Evidence (offset_check.py): +0.9 and -1.8 years equal shift + (tracking − 1) x (age − 9) from the linear summary. Observed L1 readings for Mistral Small 4 (isotonic lookup; ΔZipf/slope): +1.1 (+1.7) at 3H, -1.3 (-0.8) at 8H, largest deficit at 7H (-2.4; -2.1). For Haiku the fitted and observed values agree (4.2 and 4.6 at 3H; 0.1 and -0.1 at 8H).
- Fix: use per-grade values or write "implied by the fitted line".

**m4. Table S2: 32 uncorrected tests; the P label differs on four secondary measures** (S:41-52; M:8)
- Evidence: 10 of 32 uncorrected p-values are below .05. For the P label: number of words -35.1 (p < .001), words per sentence -0.12 (.012), Kandel-Moles +0.30 (.009), forms in films +0.012 (.020). The caption does not say "no correction" (S5's does).
- Fix: caption note. In the Abstract write "no difference in mean lemma frequency".

**m5. Probe scoring choices change the reading of Table 3** (M:84; M:151; M:181; S:150-165)
- Evidence (probe_check.py): 77% of answers state more than one range. "Any range correct" is 77% for Mistral Large 4 (first range 62%), 67% for Mistral Small 4 (37%) and 67% for Haiku (65%). The ±0.5-year window accepts a stated midpoint a year off at the edge of the true range. The "1.5 to 2.5 years too old" window behind "86%" (152 of 177) is a post hoc choice from exploratory.py. The Abstract's "two years" rests on it.
- Fix: say in the Method that most answers contain several ranges, show the any-range column in Table 3, and name the window as post hoc.

**m6. Interval type and precision** (M:104; PREREG Q5)
- Evidence (boot_check.py): the registration says "95% intervals from 2,000 bootstrap resamples", not percentile. With 16 topics, percentile intervals are narrower than jackknife-t(15) ones (L1 shift width 0.324 against 0.370; L1P tracking 0.188 against 0.204). BCa differs at the low end of the L1 shift ([0.103, 0.438] against [0.134, 0.457]). At B = 2000 the limits move with SD 0.002 to 0.008 across seeds. Only S4's boundary case is affected.
- Fix: say "percentile" in the registration-derived sentence and add a precision remark.

**m7. The isotonic sensitivity reading is not like-for-like** (M:167; S:29)
- Evidence: analyze.py pools the isotonic readings as the unweighted mean of per-model shift and tracking (np.nanmean). The primary pools as Σlevels/Σslopes. With the same unweighted pooling the linear readings are 0.21 and 0.94 (H) and -0.01 and 0.91 (P), against isotonic 0.19 and 0.94, and -0.05 and 0.87. Most of the gap to 0.30 and 0.93 (H), 0.02 and 0.90 (P) is pooling, not ruler shape. No intervals are given.
- The caption counts (135 inside, 59 extrapolated, 4 capped) cover 198 cells = 6 models x (5 labels x 6 grades + L6 x 3), not the 72 cells of the two labels named in the same sentence.
- Fix: report both poolings, add intervals or say there are none, and say what the counts cover.

**m8. Linearity wording** (M:114)
- Evidence (lin_check2.py): the registered F test ignores topic clustering (classical p .591, .726, .679, .424, .205, .632, reproduced). A topic-level version (Hotelling T² on the four non-linear contrasts; sign-flip p similar) gives .171, .563, .494, .444, .068, .217, smallest for GPT-6.1 Sol. "No ruler departed from a straight line" is an absence-of-evidence statement with 4 df and 16 topics. Local slopes of the Mistral Small 4 and GPT-6 Luna rulers are non-monotone (offset_check.py). Conclusions are unaffected, since the isotonic reading differs little.
- Fix: "no evidence of departure", and give the topic-level p.

**m9. Figure 1 bands** (M:116; figures.py, function fig1)
- Evidence: bands are 95% CIs of each grade's mean over 16 topic means, i.e. between-topic, whereas the slopes are inferred within topic. Adjacent-grade bands overlap for all six models, and the 3H and 8H bands overlap for GPT-6 Luna (half-width 0.065 to 0.078), while slope p-values are below 1.6e-5.
- Fix: a caption sentence, or topic-centred bands.

**m10. Topics are a fixed convenience set**
- Evidence: PREREG Q5 says "Topics are treated as random". design.json lists 32 topics and make_prompts.py takes the first 16. The six pilot topics are all among them. Limitations does not say so.
- Fix: one sentence in Limitations.

**m11. Records**
- PREREG.md lines 3-4 still read "not yet deposited". The AsPredicted record and the data-v1 tag are not in this checkout (section 1). I found no discrepancy where I could check (answers are under 2,900 characters; Q3 2,379, Q8 2,038).
- Fix: update the status line and add the AsPredicted PDF to the repository or Supplement.

**m12. Table S1 "Exact duplicates removed" equals the primary row** (S:36)
- No duplicates exist (M:110). Fix: delete the row or say it is empty by construction.

**m13. Measure validity wording** (M:90 "The measure passed two checks of validity")
- H1 is a manipulation check on the models, not a validity check of the instrument. The Vikidia and Wikipedia contrast (28 of 29 usable pairs) supports ordering of registers. It does not show that 0.01 to 0.04 Zipf corresponds to a year of reading level, which is a model-internal calibration (M:104, M:114).
- Fix: "one validity check and one manipulation check".

**m14. Scope of the number check**
- check_numbers.py verifies digits against the dictionary (S8 is its blind spot) but not written-out quantities. I checked these by hand against numbers.json: "about two years" (M:8), "a third of a year", "nine tenths" (M:123), "more than a third" (M:151), "more than five years" (M:185), "about 35 words". All are correct except "almost a year" (M:185; see S7).
- Fix: extend the checker to number words, or list them as claims in a table.

## 3. Analytic choices in the text that PREREG did not fix
- Equivalence margin: SESOI reused (S2).
- Interval type: percentile (m6).
- Dispersion metric for "consistent" (S5).
- Criterion for "followed poorly" and the tier grouping (S6).
- Pooling for the isotonic reading (m7).
- 3-year extrapolation cap (code only; PREREG says only "inverse lookup on an isotonic fit").
- L0 placement formula 9 + (L0 − mean ruler)/slope (code only).
- 1.5 to 2.5-year window in the probes (m5).
- Conversion of 0.04 Zipf to "one year" at the mean slope (-0.0394). Per model it is 0.8 (Sol) to 1.6 years (Luna).
- Topic selection: first 16 of 32 (m10).

## 4. Checked, no finding
- Holm step order and monotone adjustment; df = 15; two-sided tests; rounding of Table 2 and S1 to S6 (3 d.p. levels, 4 d.p. gradients).
- H1 eligibility rule (all six slopes <= -0.02; the smallest is -0.0246).
- Exclusions: none triggered. 8,400 calls launched, 8,396 ok, 4 failed and retried (logs/run_*.json). Five truncated, 11 flagged, 0 duplicates, mean 405 words (median 369), 330 (Luna) to 594 (Sonnet). Cost 41.0981 + 0.0186 = 41.12 USD; pilot 2.2554 = 2.26 USD.
- The hypothesis that out-of-lexicon tokens drive the L2 effect was tested (oov_check.py, oov_content.py) and rejected.
- Sample-size rule: .835 at T = 16 reproduces; the smallest T with power >= .80 is 16 under the registered assumptions.
- Pilot summary: reproduces, and the pilot topics are inside the confirmatory set.

## 5. Files (absolute paths)
Work directory: /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/p7/r2_work/
- Copy of the repo: .../r2_work/repo ; planted-fault copy: .../r2_work/plant
- Scripts: .../r2_work/indep.py, h1_check.py, boot_check.py, boot_mc.py, tables_check.py, probe_check.py, power_check.py, sim_repro.py, l0_check.py, oov_check.py, oov_content.py, lin_check.py, lin_check2.py, offset_check.py, disp_check.py, loo_model.py, pilot_check.py, l2l1_len.py, loto.py
- Outputs: .../r2_work/numbers_check.json, manuscript_numbers_recomputed.json, measures_pylexique.csv, numbers_pylexique.json, sim_repro_out.json, sim_repro_stdout.txt, exploratory_frozen.json, oov_content_by_text.csv, and the *_out.txt files (indep, h1_check, boot_check, boot_mc, loo_model, disp_check, l0_check, lin_check2, offset_check, pilot_check, probe_check, l2l1_len, loto).

Memory: nothing new learned about the user or their preferences in this task.

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Les scripts et sorties texte cités sont gardés dans records/reader_scripts/r2/ ; la copie du dépôt (repo), la copie avec faute plantée (plant) et les tableaux mesurés avec la copie pylexique du lexique ne sont pas gardés.)

## Réfutation des constats de R1 (claude-fable-5-1), consigne

Consigne donnée (fichier refute_r1_full.md : le texte ci-dessous, puis le rapport complet de R1 tel qu'il figure plus haut, entre les lignes -----BEGIN R1 REPORT----- et -----END R1 REPORT-----).

````text
You are a refutation reader. A separate AI session (R1, a substance reviewer) reviewed a research manuscript and raised the findings listed below. Your job is to try to REFUTE each finding, not to confirm it: check it against the manuscript, the code and the data, and answer "refuted", "stands" or "partly stands", with the evidence (file and line, or a command you ran and its output). Then, for each finding that stands at least in part, say whether the fix R1 proposes is needed as stated, or whether a smaller fix is enough, and why. Do not fix anything.

Begin your report with exactly: "Internal reading by a separate AI session. Not peer review."

Context. ART 5 is a preregistered audit: six language models (two each from Anthropic, OpenAI and Mistral AI) wrote 7,680 French reading texts for Swiss primary grades 3H to 8H, with the grade named in eight ways (labels L0 to L6, see Table 1 of the manuscript). The primary measure is the mean Zipf frequency of content lemmas (Lexique 3.83). The four preregistered primary tests compare the bare HarmoS label (L1, « de 5H ») and the bare P label (L1P, « de 5P ») with the age-only label (L5, « de 8 à 9 ans ») on level and gradient, at the topic level (16 topics). Age equivalents ("shift" in years and "tracking") read each model's labelled texts on that model's own age-only ruler. Target journal: British Journal of Educational Technology.

Files (read only; do not edit, create or delete anything in the repository; put any script you write in /tmp/refute_r1/):
- Rendered manuscript as reviewed: /home/claude/art5-harmos-audit/manuscript/build/manuscript.md ; Supporting Information: manuscript/build/supplement.md ; figures: results/figures/*.png
- Repository: /home/claude/art5-harmos-audit (PREREG.md is the deposited preregistration; design.json; analyze.py; compute.py; exploratory.py; manuscript_numbers.py; results/numbers.json, results/manuscript_numbers.json, results/measures.csv (one row per text), results/probes.csv, results/exploratory.json; raw outputs in data/raw/calls_20261101T*.jsonl, where each record keeps the provider's full response under "response", including any visible reasoning; CHANGELOG.md).
- The official Lexique file used by the study is not on this machine. A Latin-1 copy is at /usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt (or under site-packages); it differs from the official file for words written with « œ » (729 texts get other values), so treat any re-measurement with it as approximate and say so.
- You may run Python (python3 -B; pandas, numpy, scipy, statsmodels are installed), e.g. `python3 -B analyze.py results/measures.csv results/probes.csv /tmp/refute_r1/x.json`. Do not call any model provider API, do not run pipeline.py steps that call models, do not use the network except to read a cited source if you need it.

R1's full report, verbatim (the findings are M1 to M6, S1 to S9 and m1 to m15):

[rapport complet de R1, voir plus haut]

What to do:
1. For each of M1 to M6, S1 to S9 and m1 to m15, give one verdict line (refuted | stands | partly stands) with evidence tagged [run] (you executed it) or [read] (you read it in a file, with the location) or [inference]. Recompute the numbers R1 gives where you can (for example the per-model shifts and tracking, the between-model spread of the age-only texts at the same grade, the reasoning-trace figures for Mistral Large 4, the 74 of 177 probe answers, the observed per-grade offsets, the H3 power in sim_power_results.json, the length adjustment). Where R1 says it used the Latin-1 lexicon copy, say whether the conclusion could change with the official file.
2. For M1, M2 and M3, which are about interpretation, say precisely which sentences of the manuscript are wrong or unsupported as written, and which are defensible as written (quote at most 15 words of each).
3. For each standing finding, say whether R1's proposed fix is necessary, or whether a smaller fix suffices (for example a rewording, a label "exploratory", or a stated limitation instead of a new analysis), and why.
4. Flag anything in R1's report that rests on memory rather than on a source (R1 marked some items "from memory, check").

Keep the report under 1,600 words, one short paragraph per finding at most, minor findings one line each.

````

## Réfutation des constats de R1, rapport complet (lancée à 13:05, reçu à 13:23, 47 appels d'outils, claude-fable-5-1), texte intégral

Internal reading by a separate AI session. Not peer review.

**Set-up.** `python3 -B analyze.py` on results/measures.csv reproduces results/numbers.json with 0 differences [run]. Scripts and outputs: /tmp/refute_r1/ (spread.py, sd_pergrade.py, mistral_reasoning.py, probes_check.py, pergrade_offsets.py, length_check.py, reasoning_tokens.py, swiss_lemmas.py, heterogeneity.py, report.md). Lexicon copy: the 729 texts whose frozen value the pylexique copy fails to reproduce are exactly the texts containing « vrai » or « faux » (the copy holds them only as uppercase VRAI/FAUX rows, which compute.py never matches, so they score out of lexicon and the local value is 0.009–0.127 Zipf lower; the official file evidently resolves them [inference]); texts with « œ » and without these words match 2,408 of 2,408 [run]. The œ explanation in verification_report.md §2 and in the brief is therefore wrong, but the difference is balanced across labels (vrai 4–8%, faux about 3.5% of texts per label) and does not touch the Swiss-French lemmas, so R1's approximate re-measurements would not change with the official file, except that « vrai »/« faux » leave the out-of-lexicon list.

**M1 stands.** (a), (b) as Table S3 [read]. (c) Mistral Large 4 traces: an age stated in 91% of L1/L1P texts; among stated, wrong in 61% (L1) and 53% (L1P), 49%/44% with the preregistered ±0.5-year tolerance, mostly +2 years; L5 never wrong [run]. With grade and genre effects, L1−L5 falls 0.025 Zipf per year of stated error (cluster SE 0.007), L1P −0.011 (SE 0.012, p = .37) [run], as R1 says. Sharper than R1: L1 texts whose reasoning states the right age already sit 0.44 model-years older than L5; those stating at least 1.5 years too old sit at 0.82. The measure registers about a fifth of a stated misreading, and none for P [run]. (d) partly: for H2-H four secondary measures agree (harder) and none disagrees; only for H2-P do three uncorrected tests say "easier" [read Table S2]. Unsupported as written: Method "a model that understands the label should write the same kind of text"; Discussion "so we can say whether a label is read as its age"; heading "A local label is mostly understood, on average". Defensible: "Two lighter models misread the bare labels" for Haiku (probes and texts agree) and, through the probes, Mistral Small 4; "The difference is real but small" with "on the primary measure" added. Fix: the reframing is necessary; L1−L4 contrasts are not (Table S3 shows L4's departure, cite it); the trace analysis is cheap and worth adding as exploratory; discuss only the H2-P divergence.

**M2 stands for the H level and both trackings, not for the P level.** Per-model CIs as stated [read]. Wald tests on the preregistered secondary OLS: label × model terms differ for the L1 level (F(5,15) = 21.9, p < .001), L1 gradient (10.4, p < .001), L1P gradient (19.8, p < .001), but not the L1P level (1.7, p = .20), whose six per-model CIs all include 0 [run]. Wrong as written: Abstract and Results "neither label changed how texts followed the grade"; Results "at least as steeply as the age". Defensible: Table 2; "the evidence of under-tracking is weak". Fix: the heterogeneity test is one line (above); the necessary part is wording (non-rejection, spread in the abstract, |tracking − 1| symmetric).

**M3 stands.** L3 −0.46 [read]; between-model SD of per-grade means 0.058 (L3), 0.061 (L1), 0.063 (L1P), 0.064 (L5); L3−L1 CI [−0.008, 0.004], 2,000 topic resamples [run]; L5 model means at one grade span 0.14–0.23 Zipf, 3.6–5.8 years at the mean slope [run]. Caveat on (b): absolute between-model SD is dominated by baseline differences that no wording can remove, so it is the wrong criterion if "consistent" means each model's agreement with its own ruler; the paper must say which it means. Unsupported as written: Abstract "made the models more consistent" and "can keep local labels if they add the age"; Conclusion "the wording to recommend in teacher education"; Implications "label wordings, models and languages". Defensible: Discussion "in exploratory per-model estimates, brought the models closer together"; the tool-developer mapping. Fix: rewording suffices (state the sense, add the absolute spread, demote to a hedged note); no new study.

**M4 partly stands.** Method, Figure 3 and Discussion label the per-model, L2, L4 and probe results exploratory; Abstract, notes and Conclusion do not [read]. The equivalence reading is absent from PREREG Q5 [read]. TOST is unnecessary: the 95% CIs ([−0.018, −0.005], [−0.010, 0.009]) lie inside ±0.04, which already implies TOST at α = .05. Fix: add "exploratory" and "post hoc" where missing.

**M5 stands.** CHANGELOG line 18 (201.87 USD promotional), line 10 (readers claude-fable-5-1, claude-sonnet-5-5), line 6 (briefs outside the repository) [read]; manuscript names Opus only [read]. Fix is wording plus a summary of the briefs; the BJET requirement is unverified here.

**M6 stands** [read: title, "AUTHOR INPUT", PREREG Q3 URL, CHANGELOG "Pablo"]. make_anonymous_bundle.py already redacts the repository copy; the gap is the AsPredicted record, so the cover-letter note is the fix.

**S1 stands** (approximate, robust to the copy, see set-up). Counts 258/0, 159/0, 148/0, 120/6, 58/0; L2−L5 −0.0343 → −0.0242 without the narrow set (0.87 → 0.62 years); L1−L5 −0.0117 → −0.0108; without out-of-lexicon tokens H2-H −0.014 [run]. "tandis" is absent from the official file too: texts containing it match 491/491 [run]. A decomposition sentence and the Method statement suffice.

**S2 stands as a limitation**; 0.04 Zipf is 0.82–1.6 years across rulers [run]. Necessary: "model-internal years" in the abstract and the SESOI's range; Manulex optional.

**S3 stands on facts, partly refuted on tiers.** Reasoning tokens: Large 933–1,361, Small 0, Haiku 163/107/291 (L1/L1P/L2) against 0–1 (L5, L4) [run]; prices and "no dated id" in models.json; PREREG Q8 "provider and model size" has no row in S1 [read]. Tiers are defined within provider in the Method, which is defensible. Fix: one table, one term, correct S1.

**S4 stands.** 177 wrong, 74 also correct, 152 (86%) two years; 49/542 boundary cases, 52% of Mistral Small 4's; Sonnet's one P error parses "vers 4 ans"; at least 7 of 10 too-young errors are contextual; Haiku 11 errors of 6–9 years; one "1P à 6P" answer [run]. Among the 152, 28% mention France, 13% Belgium, 40% HarmoS tables starting at 6–7 years, so the counting-from-six reading fits more answers than R1's percentages suggest. Fix: "consistent with", note artefacts and boundary cases; hand-coding optional.

**S5 stands**: half-tracking power .902 at σ 0.15, slope −0.04, T 16 [read]; from the observed SEs the smallest detectable tracking departure at 80% is 0.16–0.18 [run]. One sentence.

**S6 stands**: observed Haiku 3H 4.30 [3.58, 5.05], 8H −0.13 [−1.15, 0.94]; Mistral Small 4 3H 1.75 [0.33, 3.24], 8H −0.76 [−1.85, 0.50], profile non-monotone (7H −2.11) [run]. Necessary: replace or label the fitted 0.9/−1.8.

**S7 partly stands.** Per-model slopes −0.016 to −0.172; within-cell slope −0.021 to −0.025 (cluster SE 0.02); implied bias +0.002; within-cell H2-H −0.014, H2-P −0.003 [run]. "Did not depend" is true of decisions, not estimates; one sentence on H2-P suffices.

**S8 partly stands**: Limitations list the conditions, the Conclusion does not; one clause.

**S9**: Imperial confirmed [read arXiv v2 pp. 2, 4–6: story completion, FKGL grade 2 none in range, CEFR A2 0.76–0.85]; Rooein confirmed [read: ChatGPT flat, GPT-3 moved]; Avry refuted as a defect, the population is already stated. Row "no earlier study": the repository log's P2 section holds 131 entries, not empty [read]; "other non-US labels" is the weak part.

**Minor.** m1 stands [read]. m2 stands [PREREG Q8]. m3 stands [PREREG controls]. m4 unverified, memory; design.json says "intercantonal documents", so widen the wording. m5 partly: 12% of L1 texts name an age, mostly a character's. m6 stands. m7 stands. m8 partly: Luna has the widest CIs; a limitation sentence suffices. m9 stands, with the cause corrected (vrai/faux, not œ). m10 stands [Figure 1, flat 5H–6H segments]. m11 refuted: the axis title gives the ages. m12 stands [CHANGELOG 08:52 and 08:54 Zurich, run 41286684728; first record 07:55:47Z]. m13 stands. m14 suggestion only. m15: 5,706 words without tables, 6,274 with [run].

**Memory-based in R1**: Geneva pre-HarmoS dates (S4, marked); H notation in Valais, Neuchâtel, Jura, Bernese Jura (m4, marked); "the BJET editorial asks for them" (M5, guidelines not opened); "AsPredicted shows dates only" (m12).

(No memory or project notes were used; the repository is unchanged; no provider API was called. Beyond the brief, one item worth recording: the local pylexique copy differs from the official Lexique file through « vrai »/« faux », not « œ », learned from /tmp/refute_r1/swiss_lemmas.py and the agreement test in this session.)

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Scripts gardés dans records/reader_scripts/refute_r1/.)

## Réfutation des constats de R2 et R3 (claude-opus-5-5), consigne

Consigne donnée (fichier refute_r2r3_full.md : le texte ci-dessous, avec les rapports complets de R2 et R3 tels qu'ils figurent plus haut à la place de {{R2}} et {{R3}}).

````text
You are a refutation reader. Two separate AI sessions reviewed the same research manuscript: R2 (methods and statistics) and R3 (a handling-editor reading for the target journal). Their full reports follow. Your job is to try to REFUTE each of their findings, not to confirm them: check each against the manuscript, the code and the data, and answer "refuted", "stands" or "partly stands", with the evidence (file and line, or a command you ran and its output). Then, for each finding that stands at least in part, say whether the fix the reviewer proposes is needed as stated, or whether a smaller fix is enough, and why. Do not fix anything.

Begin your report with exactly: "Internal reading by a separate AI session. Not peer review."

Context. ART 5 is a preregistered audit: six language models (two each from Anthropic, OpenAI and Mistral AI) wrote 7,680 French reading texts for Swiss primary grades 3H to 8H, with the grade named in eight ways (labels L0 to L6, Table 1 of the manuscript). The primary measure is the mean Zipf frequency of content lemmas (Lexique 3.83). The four preregistered primary tests compare the bare HarmoS label (L1, « de 5H ») and the bare P label (L1P, « de 5P ») with the age-only label (L5, « de 8 à 9 ans ») on level and gradient, at the topic level (16 topics). Age equivalents ("shift" in years and "tracking") read each model's labelled texts on that model's own age-only ruler. Target journal: British Journal of Educational Technology (BJET; double-anonymous review; about 6,000 words excluding references; Wiley's AI policy allows substantial AI use if described transparently; a 2025 BJET editorial asks LLM studies to name model, version and provider and to give prompt details).

Files (read only; do not edit, create or delete anything in the repository; put any script you write in /tmp/refute_r2r3/):
- Rendered manuscript as reviewed: /home/claude/art5-harmos-audit/manuscript/build/manuscript.md ; Supporting Information: manuscript/build/supplement.md ; figures: results/figures/*.png ; submission drafts: manuscript/submission/cover_letter.md and title_page.md ; manuscript/make_anonymous_bundle.py ; manuscript/verification_report.md
- Repository: /home/claude/art5-harmos-audit (PREREG.md is the deposited preregistration text; design.json; analyze.py; compute.py; exploratory.py; sim_power.py and sim_power_results.json; manuscript_numbers.py; results/numbers.json, results/manuscript_numbers.json, results/measures.csv (one row per text), results/probes.csv, results/exploratory.json; raw outputs in data/raw/calls_20261101T*.jsonl; CHANGELOG.md; README.md). Note: since the readings, the main session has added exploratory_p7.py and results/exploratory_p7.json (post hoc analyses written in response to the readings); you may use them, but check them rather than trust them.
- R2's own scripts and outputs are in /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/p7/r2_work/ (read only); you may rerun them in your own folder.
- The official Lexique file used by the study is not on this machine; a Latin-1 copy (pylexique) is under /usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/ or site-packages, and differs for words written with « œ ». Treat re-measurements with it as approximate.
- You may run Python (python3 -B; pandas, numpy, scipy, statsmodels installed). Do not call any model provider API, do not run pipeline.py steps that call models, and use the network only to read a source you need to check (for example a journal or publisher page).

What to do:
1. For each finding of R2 (M1, S1 to S8, m1 to m14) and of R3 (reasons 1, 2, 3a to 3e, 4, 5 with its four parts, 6 and 7), give one verdict line (refuted | stands | partly stands) with evidence tagged [run], [read] (with the location) or [inference]. Recompute the reviewers' numbers where you can (for example: H2-H without Claude Haiku 5.5; the seed dependence of the upper bound of the P tracking interval; L2 − L1 in Zipf and in years; the between-model SDs of shifts and tracking; the per-grade offsets; the power-simulation assumptions; the isotonic pooling).
2. For R2 M1 and R3 reasons 2 and 3, which concern compliance and disclosure, say exactly which sentences of the manuscript are false or incomplete as written.
3. For each standing finding, say whether the proposed fix is necessary, or whether a smaller fix suffices (a rewording, a label, a stated limitation instead of a new analysis), and why. Say also where R2 and R3 contradict each other, if they do.
4. Flag anything in the reports that rests on memory or on an unread source rather than on a checked one.

Keep the report under 1,800 words; minor findings one line each.

-----BEGIN R2 REPORT-----
{{R2}}
-----END R2 REPORT-----

-----BEGIN R3 REPORT-----
{{R3}}
-----END R3 REPORT-----

````

## Réfutation des constats de R2 et R3, rapport complet (lancée à 13:17, reçu à 13:39, 78 appels d'outils, claude-opus-5-5), texte intégral

Internal reading by a separate AI session. Not peer review.

Scope. "As reviewed" means manuscript/build/*.md at commit ea43d9d. These files are unchanged at HEAD dca44b4. Commit dca44b4, made after R3, changes only make_anonymous_bundle.py, and e7eb7f7 adds literature notes. My scripts and outputs are in /tmp/refute_r2r3/ (core.py, s1_loo.py, boot.py, s2_s3.py, s3_len.py, minor.py, bundle_sim.py, power_repro.py, wordcount.py, *_out.txt). I did not touch the repository: git status shows only the main session's three untracked p7 files. results/exploratory_p7.json agrees with my recomputations where they overlap (90% CIs, L2 − L1, tracking at large B, L0 intervals). I used no memory or project notes.

## A. R2

**M1: partly stands.** [read] PREREG.md:124–125 registers "provider and model size". No table, number or contrast reports it (Figures 1 and 3 only mark tier), and S1 (S:20) leaves it out.
- Refuted sub-point: "H against P" is not post hoc. analyze.py at tag prereg (same SHA-256 62324d6d… at HEAD) computes P_vs_H at line 502. Only the registration text leaves it out.
- The 1.5–2.5 window (exploratory.py) and the line-implied offsets (manuscript_numbers.py, "after the deposit") are post hoc, as R2 says.
- Fix: the itemised statement is needed. Marking the Table S5 rows "not registered" would be wrong; they are "in the registered code, not the registration text". A tier table is optional if the omission is stated.

**S1: stands.** [run s1_loo, boot]
- H2-H without Haiku: +0.0041, p = .297. Without any other single model: p ≤ .022.
- H3-P without Mistral Small: −0.0008, p = .672.
- Per-model H2-H SD 0.043. Shift SD 1.07 [0.88, 1.36]; tracking SD 0.50 [0.39, 0.67].
- Models treated as a sample: H2-H [−0.057, 0.034]. Shift pooled 0.30, mean 0.21, median −0.19.
- Fix: the leave-Haiku-out sentence and "for these six models" are needed. The SDs can go to the SI.

**S2: partly stands.**
- [read] PREREG has no equivalence test, and Q7 powers H2-H only.
- But the margin is the registered SESOI, named at M:100, and both level claims hold for these six models: TOST p = 1.1e-7 each, 90% CIs [−0.017, −0.006] and [−0.008, 0.007] [run].
- The gradient upper limits times 5 years are 0.038 and 0.042 Zipf [run]. So "Neither label changed how texts followed the grade" (M:8, M:123, M:173) is absence of evidence.
- H3-P leave-one-topic-out: p from .008 to .124; 12 of 16 topics positive [run].
- [read] sim_power_results.json gives H3-H power .90 against half tracking (σ = .15, T = 16). So M:193 needs the effect sizes named, not a restriction to H2-H.
- Fix: rewording plus "post hoc use of the SESOI". No new analysis.

**S3: mostly refuted.** M:167 already reports the length row, and no test decision changes (S:38: H2-H p < .001, the others p ≥ .077). H2-P at −0.008 stays well inside ±0.04, so "the P-label conclusion changes" is wrong. It stands only as wording: "did not depend" sits next to an H2-H estimate 42% larger. Fix: "no test decision changed". R2's key numbers here have no script or output behind them (see E).

**S4: stands.** [run boot]
- The registered seed reproduces [0.814, 0.9947].
- Seeds 1–200 at B = 2,000: upper limit 0.993–1.011, below 1 in 37% of seeds (R2: 43%).
- B = 200,000: [0.815, 1.001], P(≥ 1) = .026.
- Fix: delete "stops just below 1" and add one clause on Monte Carlo precision. Keeping the registered [0.81, 0.99] in Table 2, with the converged 1.00 in a note, is enough.
- Also: checks/check_numbers.py:48 exempts "just below 1" as if it were part of the tracking definition.

**S5: partly stands.** [run]
- The SDs reproduce: shift 1.07/0.28/0.87/0.28/0.42 and tracking 0.50/0.46/0.22/0.21/0.26 for L1/L1P/L2/L3/L4.
- "Holds against the bare H label only" is wrong. L3 is also tighter than L1P on tracking (−0.24 [−0.35, −0.10]) and than L2 on shift (−0.59 [−0.89, −0.30]).
- L3 ties L1P on shift and L2 on tracking, and cannot be separated from L4. So M:189 "most consistent" is unsupported (because of L4). The Abstract and practitioner notes, which compare with the bare label, hold.
- Fix: R2's wording, with the metric named.

**S6: partly stands.**
- R2's numbers are correct, and the manuscript gives no criterion and no tier analysis.
- But Luna's size in years comes from its shallow ruler (−0.025). In Zipf, its level (+0.019) is close to Sonnet's and Mistral Small's, and its gradient (−0.0104) to Sonnet's, Sol's and Mistral Large's (Table S4).
- The two named models are exactly those whose tracking CIs lie below 1 for both labels (Table S3).
- Fix: "two of the three lighter models", that criterion, and a note that Sol and Luna over-track. No new analysis.

**S7: partly stands.** [run]
- L2 − L1: −0.0224 [−0.0309, −0.0139], t(15) = −5.62; +0.57 years [0.37, 0.81]. Per model: Haiku +0.004, Sol −0.004.
- M:185 "harder by almost a year" gives the region the whole shift, and M:137 is ambiguous.
- Refuted for L3: M:137 states L3 against the age and gives L3 − L1.
- Fix as R2 proposes.

**S8: stands.** [run] 480 texts per topic, 80 per model and topic, 1,280 per model. Fix as R2 proposes.

Minor findings (verdict and fix):
- m1 stands [run power_repro]. .835 reproduces (σ 0.1223, planning slope −0.04, seed 793); .856 at R = 2,000. [inference, computed analytically from the sim_power.py assumptions] Simulated topic-level SDs are 0.040 and 0.017 against observed 0.013 and 0.009. L5 residual SD 0.104 [run]. The pilot p used HC3 with a normal reference (pipeline.py:129–131). One clause.
- m2 stands [run]. L0 intervals reproduce within 0.1. Mistral Large's L6 readings reach 16.8–17.3, not 16.3.
- m3 stands [run]. Fitted line +0.9/−1.8 against isotonic +1.1/−1.3 (7H −2.4). Rewording.
- m4 stands. 10 of 32 p-values below .05, and the caption is silent. Caption note.
- m5 partly stands. Table S7 already has the any-range column and the 77%; the window is post hoc. One clause.
- m6 mostly refuted. M:104 already says "percentile", and analyze.py at the tag fixes it (lines 42–43). Only the precision remark stands.
- m7 stands [run]. Unweighted linear readings 0.21/0.94 and −0.01/0.91. The caption's 198 cells = 6 × 33 cells, covering all labels.
- m8 stands [run]. Hotelling p .171/.563/.494/.444/.068/.217, an exact match. Rewording.
- m9 stands (figures.py, fig1). Caption sentence.
- m10 partly stands. The topics are the first 16 by a pre-specified rule (make_prompts.py:77), not hand-picked. One sentence.
- m11 stands. But note the status in the README rather than edit the frozen PREREG.md. A non-anonymous AsPredicted PDF cannot go to reviewers.
- m12 stands; trivial.
- m13 partly stands; M:90 itself calls H1 a manipulation check.
- m14 stands; add the "just below 1" exemption to it.

## B. R3

**1: stands.** Placeholders at M:2, 207 and 209; docx dc:title "TITLE TO WRITE LAST"; no keywords; placeholder tokens in title_page.md and cover_letter.md. All are listed for G2 in verification_report.md §6. Fix as stated.

**2: partly stands.**
- [read] CHANGELOG:18: credit before the run was 206.87 USD, of which 201.87 promotional. manuscript_numbers.json: Anthropic spend 25.44 of 41.12 USD.
- Which credit paid the calls is not recorded, so "checked, not inferred" overclaims. [inference] At least 20.44 USD (80%) was promotional even if the purchased credit was spent first.
- G2 items 2–3 do not mention the promotional credit.
- Fix needed as R3 proposes. But "Anthropic had no role" must not hide that Anthropic's assistant did the work.

**3a: partly stands.** The assistant is named, with its identifier and provider. Its protocol and prompts are outside the repository (CHANGELOG:6; "protocol rule 3" is only cited). Smaller fix: put the protocol and the session briefs in the repository and point to them. No SI section is needed.

**3b: stands.** But the sessions that checked the manuscript are not named anywhere (verification_report.md:40 and 42 read "RESULT PENDING"). CHANGELOG:10 names the design readers, so the names R3 proposes are an inference.

**3c: stands in substance.** [run git log] Every non-bot commit (24) is authored "Claude", none by the author; the G1 approval is one line (CHANGELOG:41). R3 overstates the "written by" lines: none exists for the design, PREREG or the core code. Wording fix; a CRediT statement is optional.

**3d: partly stands.** The logged, bounded search sentence is deliberate (verification_report.md §5). R3's "to our knowledge" would remove the bound. Keep the bound and move the tool names to the log.

**3e: stands**; trivial.

**4: partly stands.** Li et al. is cited in cover_letter.md but not in the manuscript. [read, Crossref] It is BJET 56(3), 1092–1117, online December 2024, so the APA year is 2025. The desk-reject risk is opinion. Fix: cite it, or drop it from the letter. The other additions are optional given the length.

**5a (preregistration text): stands.** PREREG.md:46 at the tag carries the GitHub user name. aspredicted.org/help says the anonymous PDF "will not list authors", and for identifying answers recommends to "download the .pdf, manually cover the information". verification_report.md:62 plans an anonymous link. Fix as R3 proposes.

**5b (bundle): stood at the reviewed commit; now fixed.** [run bundle_sim at ea43d9d] The script stops on itself, cover_letter.md and title_page.md, and the ORCID and UNIR appear in verification_report.md. At HEAD nothing is left except the French verb "unir" in the raw texts. The manuscript, SI, docx and PNG metadata carry no identifier [run].

**5c (stale headers): stands** (README.md:5, PREREG.md:3–4; see m11).

**5d (timing): stands as fact.** First call 07:55:47Z (08:55:47 CET); AsPredicted approval about 08:52; tag 07:29:40 CET. The optics are opinion; the fix is optional.

**6: stands.** [run wordcount] 6,248 / 5,826 / 5,506 / 5,084 words, as R3 counted.

**7: partly stands.** 244 words confirmed. "0.30 years needs the unit" is refuted: the unit is present (M:8). For the SESOI wording, see D.

## C. Exact sentences

- M1:
  - S:8 "All were run as registered" is false.
  - The S:20 row is incomplete.
  - M:104 "S1 lists where every preregistered analysis is reported" and M:203 "…there were no deviations" are false.
  - The M:179 offsets and M:181 "86% … 1.5 to 2.5 years" are post hoc but not labelled as such.
- R3 reason 2:
  - M:207 is incomplete: it does not mention the credit received from an audited provider.
  - M:209 "no specific funding" and "paid from API credits attached to the author's account" are literally true but incomplete.
  - The same applies to title_page.md and cover_letter.md ("I have no conflict of interest to declare").
- R3 reason 3:
  - M:211 "conceived and designed with the assistance of" understates the assistant's role. It also conflicts with M:193, "designed, run and written with an AI assistant". The CHANGELOG describes the session entering the deposit (lines 14–16) [inference].
  - "Reference and number checks were performed … by separate AI sessions, whose reports the author reviewed": still pending in the repository, and the models are not named.
  - "Reviewed and edited the full manuscript": not yet true; G2 is pending per both submission files.
  - "The prompts, parameters and outputs are archived": true only for the audited models.

## D. Contradictions between R2 and R3

- Length: R2's fixes add text, and R3 finds no room under the limit. Put R2's additions in the SI.
- R3 (reason 7) proposes "below the one-year difference set in advance". R2 shows that 0.04 Zipf is 0.8 (Sol) to 1.6 (Luna) years depending on the model, and that the equivalence use is not registered. Keep the Zipf wording and label it post hoc.
- Both want PREREG.md edited, yet R2 itself relies on the file being identical to the tag.
- R3 treats the per-model findings as the contribution. R2 (S1, S6) shows they are exploratory and that the attribution to model size is untested.

## E. Findings not backed by a script or a read source

- R2 S3: the within-cell slopes (+0.005 for L5; −0.038 for L1/L1P/L5) have no script or output in r2_work. L5 has one text per model × grade × genre × topic cell, so the first cannot be computed as described. For the second I get −0.032 (SE 0.007). The per-model slopes −0.016 to −0.172 reproduce.
- R2 m2: the 16.3-year reading does not reproduce.
- R3:
  - The AsPredicted behaviour was unsourced; I confirmed it on aspredicted.org/help.
  - The editorial's content and its "falling acceptance rate" come from common.md and a summary. Neither R3 nor I could read the body (Wiley blocked). Crossref confirms the title, "Reporting on AIED research and ethical considerations".
  - Yan et al. (2023) was not checked.
  - Shen, Nguyen and Murgia were read as abstracts only.
  - The keyword count and the BJET limits come from secondary copies.
  - The claim about which credit paid the calls is an inference (see reason 2).
  - The names proposed for the checking sessions are an inference (see 3b).

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Scripts et sorties gardés dans records/reader_scripts/refute_r2r3/.)

## Lecture de confirmation des corrections (claude-fable-5-1), consigne

(Consigne donnée telle quelle, lancée à 13:46 par la session principale, qui n'a pas pris part à la lecture.)

You are a separate reader confirming corrections to a research manuscript. You did not make them and must not assume they work. Begin your report with exactly: "Internal reading by a separate AI session. Not peer review."

Context. ART 5 is a preregistered audit: six language models (two each from Anthropic, OpenAI and Mistral AI) wrote 7,680 French reading texts for Swiss primary grades 3H to 8H, with the grade named in eight ways; the measure is the mean Zipf frequency of content lemmas; the four primary tests compare the bare HarmoS label (L1) and the bare P label (L1P) with the age-only label (L5). Target journal: British Journal of Educational Technology (double-anonymous; about 6,000 words excluding references). Three internal readings of the draft (R1 substance, R2 methods and statistics, R3 editor) and a check of 44 sentence-citation pairs produced findings; two refutation sessions tried to refute them. The main session then revised the manuscript. Your task is to confirm, finding by finding, that the corrections are real and correct, and to find any new error they introduced.

Files (read only; do not edit, create or delete anything in the repository; write scripts and any temporary file only under /tmp/confirm_p7/):
- Revised repository (a git worktree): /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/p7/wt at commit 49e8ae4 (branch p7-revision). The draft that was reviewed is its parent commit dca44b4: `git -C <worktree> diff dca44b4 49e8ae4 -- manuscript/manuscript.md` shows the text changes.
- Rendered revised manuscript: manuscript/build/manuscript.md and supplement.md (figures in results/figures/*.png); sources with placeholders: manuscript/manuscript.md, supplement.md; numbers: results/manuscript_numbers.json (built by manuscript_numbers.py), facts: manuscript/process_facts.json and source_facts.json; references: manuscript/references.json.
- Post hoc analyses added in response to the readings: exploratory_p7.py, output results/exploratory_p7.json and results/exploratory_p7_mistral_sample.txt.
- The full findings, refutations and verdicts are in manuscript/records/p7/p7_records.md (read the R1, R2 and R3 reports and the two refutations; the refutations say which findings stand and what fix suffices).
- Checks: checks/check_numbers.py, checks/check_claims.py (new), checks/check_citations.py, checks/recompute_primary.py, history/check_history.sh; the anonymisation script manuscript/make_anonymous_bundle.py.
- The official Lexique file is not on this machine; do not re-measure texts. You may run Python (python3 -B; pandas, numpy, scipy, statsmodels installed) on the repository's files from your own folder. Do not call any model provider API. You may use the web only to read the sources cited by the new sentences (see 3).

What to do:
1. For every finding that the refutations say stands at least in part (R1: M1 to M6, S1 to S9 and the minor ones; R2: M1, S1, S2, S4 to S8 and the minor ones; R3: reasons 1 to 7; the seven partial sentence-citation pairs C-n10, C-n18, C-n25, C-n30/31, C-n33, C-n40), say "confirmed", "partly" or "not fixed", with the location of the fix (section and sentence, table, file and line) and evidence. A finding may be answered by a stated limitation or a label rather than a new analysis when the refutation said that suffices.
2. Check the meaning of every new or changed number in the revised text: that each placeholder names the quantity the sentence says it does (the digit checks cannot see this), recomputing a sample of the new post hoc numbers from the data (for example the leave-one-model-out estimate without Claude Haiku 5.5, L2 − L1 in years, the between-model spread of the age-only texts, the observed per-grade offsets, the Mistral Large 4 comparison with grade and genre held constant). Read exploratory_p7.py for errors.
3. Check the sentences that cite sources added after the readings against the sources themselves: Javourey-Drevet et al. (2022, Applied Psycholinguistics, open access, doi 10.1017/S014271642100062X), Sclar et al. (2024, arXiv 2310.11324), Yan et al. (2024; read the arXiv version 2303.13379v2, pp. 12 and 16), État de Vaud (2012, the press release whose address is in references.json), and the ministry page on the école élémentaire (ages 6 to 11). Say for each whether the sentence is supported.
4. Look for new errors: contradictions between sections, claims stronger than the results, post hoc or exploratory results without a label, statements about the author's own actions that are not yet true, anything that would identify the author in the manuscript or the supporting information, and wording that reads as written by a machine.
5. Run the checks listed above and the anonymisation script on commit 49e8ae4 with an output file under /tmp/confirm_p7/ (python3 manuscript/make_anonymous_bundle.py /tmp/confirm_p7/bundle.zip --ref 49e8ae4, run from the worktree), and report the results.

Report under 1,400 words: first the verdict list (one line per finding), then new errors ranked by severity with a concrete fix each, then the check results. Tag what you ran [run], what you read [read], and inferences [inference].

## Lecture de confirmation, rapport complet (lancée à 13:46, reçu à 14:16, 73 appels d'outils, claude-fable-5-1), texte intégral

Internal reading by a separate AI session. Not peer review.

Scope: worktree at 49e8ae4, diff against dca44b4, rendered manuscript and SI, p7_records.md, exploratory_p7.py, checks. Scripts and outputs in /tmp/confirm_p7/ (recompute.py, recompute_out.txt, bundle_sim_confirm.py, checks/). Repository untouched (git status clean after all runs). No memory or project notes used.

## 1. Verdicts

R1
- M1 confirmed [read]: Method §Prompts ("a departure ... does not by itself show a misreading"), Discussion §"Lexical equivalence is not understanding", trace analysis Table S12 (reproduced [run]); H2-P secondary divergence stated in Results.
- M2 confirmed [read]: "both directions" (Abstract, Results §Behind the averages, RM-ANOVA F reproduced [run]); "no change ... was detected"; Sol/Luna over-tracking named; |tracking−1| in Table S11.
- M3 confirmed [read]: teacher-education sentence and "and languages" dropped; absolute spread 0.053 vs 0.051 [run] beside SD of shifts; Implications restated with "read the text".
- M4 partly [read]: "(all exploratory)" in Abstract, "post hoc equivalence reading" in Results; Conclusion and practitioner notes still carry per-model results unlabelled.
- M5 confirmed [read]: COI/Funding (206.87/201.87 match CHANGELOG), three model ids named, records folder exists.
- M6 partly: title, keywords, no "AUTHOR INPUT" in manuscript [run grep]; cover-letter note on the preregistration URL; but the anonymised bundle is broken (new error 1).
- S1 confirmed [read/run]: Method sentence on adult corpora and Swiss usage; romand 220, canton 54 of 1,152 L2 texts, 0 in L5 (reproduced); lemma decomposition replaced by word counts.
- S2 confirmed: "model-internal years" (Abstract); SESOI 0.8–1.6 years in Limitations (reproduced [run]).
- S3 confirmed: Table S9 (reproduced [run]); tiers by price, undated aliases, default reasoning in Method; S1 row → Table S11.
- S4 confirmed: 74/177, 49/542 (reproduced [run]); "consistent with"; Vaud numbering until 2013.
- S5 confirmed: power .90 (grid T=16, slope −0.04, σ=0.15, smallest σ ≥ 0.122 [read sim_power_results.json]).
- S6 confirmed: observed offsets with CI, Haiku 3H 4.3 [3.6, 5.1], Mistral Small 1.7 at 3H, −2.1 at 7H, negative from 5H on (reproduced [run]).
- S7 confirmed: both length-adjusted estimates given, "no test decision changed".
- S8 confirmed: Conclusion "with the prompt and settings tested"; Limitations list the conditions; Sclar cited.
- S9 confirmed [read]: story continuation and Flesch–Kincaid scope; Rooein "some models"/"slightly"; priority sentence narrowed to Swiss labels.
- Minor: m1, m2, m3, m4 (cantonal notations), m5, m6, m7, m9 (SHA in S1), m10, m12, m13 confirmed [read]; m8 partly (generic S1 note only); m11 done though refuted (Fig. 1 by age [read PNG]); m14 not done (optional per refutation); m15 see new error 3.

R2
- M1 confirmed: S1 "Departures", Statements, Table S5 rows "not in the registered list", Table S11.
- S1 confirmed: "rests on one model", +0.0041 (p = .297); Table S10 all 24 values reproduced [run]; "Pooled over the six models", "models audited here".
- S2 confirmed: post hoc equivalence reading, "not detected", H3 power; "powered for the pooled tests" removed [run grep].
- S4 confirmed: sentence deleted; [0.81, 1.00] at 100,000 resamples (reproduced [0.815, 1.001], P(≥1) = .026 [run]); check_numbers exemption removed.
- S5 partly: metric named, five SDs in Table S11, "most consistent" gone; the ties (L1P 0.28 shift, L2 0.22 tracking) visible in the table, not stated.
- S6 confirmed: criterion "tracking intervals below 1 for both labels"; "model size is at most a hypothesis".
- S7 partly: L2−L1 +0.57 [0.36, 0.84] (reproduced exactly [run]), Table S5 row, "half a model-internal year"; absence for Haiku/Sol not stated.
- S8 confirmed.
- m1 partly (assumptions in S1, realised SD not given); m2–m13 confirmed [read]; m14 confirmed (check_claims.py PASS, planted FAIL [run]).

R3
- 1 confirmed (AUTHOR INPUT only on title page/cover letter, by design). 2 confirmed. 3a–3e confirmed [read; grep: no "we"/"our"], but see error 2. 4 partly: Yan et al. cited and supported, Li dropped from the letter, educational paragraph added; general framing in Introduction only. 5a partly (depends on 5b). 5b NOT FIXED, regressed (error 1). 5c, 5d confirmed. 6 not addressed (error 3). 7 confirmed (251 words, SESOI phrase gone).

Citation pairs: C-n10, C-n18 (Rooein p. 9 read: "unlikely to translate without adaptation"), C-n25, C-n30/31, C-n33 confirmed [read]; C-n40 confirmed (sentence removed, replaced by État de Vaud 2012).

New sources [read]: Javourey-Drevet 2022 (165 grade-2 pupils in France, 10 narrative and 10 scientific texts, "substituting long and infrequent words by shorter and more frequent synonyms", fluency and comprehension better, poor readers benefited "to a greater extent"): supported. Yan 2024 arXiv v2 p. 16 ("should at least report the exact models, prompts, and model temperature ... as different models may differ"): supported; Crossref 55(1), 90–112 confirmed. Sclar 2024 v2 (formatting sensitivity up to 76 points, GPT-3.5 via API, open-ended generation in appendix): supported. État de Vaud 2012 (4 avril 2012: "en août 2013, la numérotation ... sera adaptée à HarmoS", "6e année actuelle déjà (8H)"): supported. Ministry page (6 à 11 ans, CP to CM2, no per-class age): supported, derivation stated. Cambridge page via alphaXiv; WebFetch blocked.

## 2. New errors, by severity

1. Must-fix, anonymity. make_anonymous_bundle.py on 49e8ae4 exits: "identifying strings left in manuscript/records/p7/reader_scripts/refute_r2r3/bundle_sim.py" [run] (that reader script holds the author's names in lowercase regexes; REPLACEMENTS are case-sensitive, FORBIDDEN is not). With the stop bypassed [run, in-memory simulation], the only remaining text hits are that file, but manuscript/build/title_page.docx and cover_letter.docx, new at this commit, are binary, skipped by the scan, and contain the author's name (2×), ORCID, AsPredicted number and affiliation [run: unzipped from git show]. The cover letter, title page, verification report §6.6 and the AI statement all assume this bundle. Fix: exclude manuscript/build/title_page.* and cover_letter.* (or render them under manuscript/submission/) and the bundle_sim.py file, make the name replacements case-insensitive, unzip and scan .docx (or refuse binaries outside data/ and results/figures/), rerun, record the run; correct p7_records.md line 177, which says the records folder is excluded from the anonymised copy.
2. Should-fix, statements not yet true. AI statement: "read the final manuscript", "decided the questions left open at submission"; CRediT "writing – review and editing"; "the corrections made in response are archived in the repository" (records/README.md says the per-finding log is the author's journal, outside the repository). Fix: list all four on the G2 sheet (§6.4 covers CRediT only); add the per-finding table to manuscript/records/p7/ or write "the main corrections are listed in CHANGELOG.md".
3. Should-fix, length [run]: all text except references 7,047 words (R3 counted 6,248); Introduction–Conclusion 6,050 with tables, 5,614 without, 5,133 by render.py's token rule. Over 6,000 if abstract, notes, tables or Statements (539 words) count. Fix: move the F statistics, the secondary-measure sentence and the trace numbers to the SI; shorten Statements.
4. Minor, contradiction. "more than any label wording moved them" (Discussion) vs the next sentence: « de 5e » moved texts 0.22 Zipf (Table S5), as much as the between-model range 0.14–0.23. Fix: "more than any Swiss or French wording of the grade".
5. Minor, labels (M4 residual): Conclusion "4.3 years at 3H", "two lighter models", practitioner notes. Fix: one "(exploratory)" in the Conclusion.
6. Minor, unsupported: "the grade where a text that is too hard does most harm". Fix: "the grade of beginning readers".
7. Minor: "The two that departed most" — Mistral Small's |shift| 0.49 is below Luna's 0.77 and Large's 0.79; it departs most on tracking. Fix: "the two whose texts followed the grade least".
8. Minor, references: Sclar et al. is an ICLR 2024 paper (v2 header), listed as a preprint; Javourey-Drevet lacks issue "(2)"; cover letter "this journal's call" overstates one article's recommendation.
9. Minor: "every model wrote within a year" rests on Mistral Small 4's point estimate −0.96 [−1.55, −0.38]; say "point estimates".
No machine-sounding wording stood out; the nine "post hoc" tags in Results read as checklist-driven and could be consolidated.

## 3. Check results [run]

check_numbers PASS; check_claims PASS and --plant FAIL as required; check_citations PASS (24 cited, farajidizaji2023 uncited); recompute_primary PASS (20 values); check_history PASS (v0.2 to v0.4.10); make_anonymous_bundle FAIL (error 1). exploratory_p7.py rerun in a copy outside the worktree reproduces results/exploratory_p7.json and the Mistral sample byte for byte, assertions pass; code read, no error found (the English age pattern and the 4–16 plausibility window are documented; 25 sampled traces extract correctly [read]). My independent recomputation without importing it matches every quoted post hoc number: LOO table, spread 0.144–0.227 and 0.123–0.244 Zipf, L2−L1 and L3−L1 shifts with CIs (exact with seed 20261101), SD of levels and its CI, offsets, F 29.42/15.17/9.47/1.60, TOST, tracking precision, L0 CIs, probes 542/177/74/49/77%, reasoning shares, trace shares 51/42/38/40%, −0.0428 (SE 0.0201) and −0.0116 (SE 0.0234), 52% of −0.083, Swiss words. Anthropic thinking blocks carry no text (0 of 1,877), so "only model whose reasoning is returned as text" holds; pylexique lists VRAI/FAUX in capitals only; figure and manuscript/supplement docx metadata clean. Not verifiable here: tag data-v1 (absent from this worktree), the AsPredicted record [inference: as R2 noted].

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Scripts et sorties gardés dans records/reader_scripts/confirm/ ; bundle_sim_confirm.py, qui contient les chaînes à chercher, est exclu de la copie anonymisée.)

## Deuxième lecture de confirmation, des corrections faites après la première (claude-sonnet-5-5), consigne

(Consigne donnée telle quelle, lancée à 14:37 sur le commit 34545cc par la session principale, qui n'a pas pris part à la lecture.)

You are a separate reader confirming a small set of corrections to a research manuscript. You did not make them and must not assume they work. Begin your report with exactly: "Internal reading by a separate AI session. Not peer review."

Context. ART 5 is a preregistered audit: six language models wrote 7,680 French reading texts for Swiss primary grades 3H to 8H, with the grade named in eight ways; the measure is the mean Zipf frequency of content lemmas. A first confirmation reading (claude-fable-5-1) checked the revision made after three internal readings and listed ten new findings (C1 to C10) plus partial fixes. The main session then made commit 34545cc. Your task is narrow: confirm, finding by finding, that these last corrections are real and correct, and find any new error they introduced.

Files (read only; do not edit, create or delete anything in the repository; write scripts and temporary files only under /tmp/confirm2_p7/):
- Repository (git worktree): /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/p7/wt at commit 34545cc (branch p7-revision). The commit before the corrections is 49e8ae4: `git -C <worktree> diff 49e8ae4 34545cc` shows every change (ignore the binary .docx files in manuscript/build/).
- The first confirmation report, with C1 to C10 and the partial verdicts, is the last section of manuscript/records/p7/p7_records.md ("Lecture de confirmation, rapport complet").
- Rendered text: manuscript/build/manuscript.md and supplement.md; sources with placeholders: manuscript/manuscript.md and supplement.md; numbers: results/manuscript_numbers.json (built by manuscript_numbers.py from results/exploratory_p7.json and other outputs).
- Checks: checks/check_numbers.py, checks/check_claims.py (and --plant, which must FAIL), checks/check_citations.py, checks/recompute_primary.py, history/check_history.sh, and the anonymisation script manuscript/make_anonymous_bundle.py.
- Do not call any model provider API. Do not re-measure texts (the official lexicon is not on this machine). No web access is needed.

What to do:
1. For each of C1 to C10 of the first confirmation report, and for the two partial findings R2 S5 (tie of the gloss with the bare P label) and R2 S7 (effect of the region by model), say "confirmed", "partly" or "not fixed", with the location of the fix and evidence. For C3 (length), report your own word counts of the rendered manuscript (main text Introduction to Conclusion with and without tables and captions, and everything except the references) and say whether the new verification report (manuscript/verification_report.md, section 6, item 10) states them correctly; the counting rule of the journal is unknown and is a decision for the author.
2. Check that every new or changed number placeholder names the quantity its sentence says (for example the per-model differences of the region wording, the count of contrasts in which the models differed, the tie of 0.28), from results/exploratory_p7.json and results/manuscript_numbers.json.
3. Check manuscript/make_anonymous_bundle.py as changed: run `python3 manuscript/make_anonymous_bundle.py /tmp/confirm2_p7/bundle.zip --ref 34545cc` from the worktree, then scan the zip yourself (text files and the members of any .docx) for the author's name in any case, the ORCID, the university, e-mail domains, the AsPredicted number and links to private documents. Report the exclusions and whether anything identifying is left. Do not print identifying strings in your report: name the file and the kind of string only.
4. Check manuscript/records/findings_log.csv against what manuscript/records/README.md and the manuscript's "Use of generative AI" statement say about it (rows, columns, coverage), without judging the findings themselves.
5. Look for new errors in the diff: contradictions between sections, claims stronger than the numbers, labels missing (exploratory, post hoc), wording that reads as written by a machine, references that do not match their sources as described in references.json.
6. Run the checks listed above on 34545cc and report the results.

Report under 700 words: first the verdict list (one line per item), then new errors ranked by severity with a concrete fix each, then the check results. Tag what you ran [run], what you read [read], and inferences [inference].

## Deuxième lecture de confirmation, rapport complet (lancée à 14:37, reçu à 15:11, 123 appels d'outils, claude-sonnet-5-5), texte intégral

Internal reading by a separate AI session. Not peer review.

Reader: claude-sonnet-5-5. Worktree unchanged [run]. No memory used.

VERDICTS (34545cc)
- C1 confirmed [run]: script exits 0; in a clone, a name planted in a .docx or binary stops it, lowercase names are replaced, a new bundle_sim*.py is excluded.
- C2 confirmed [read]: findings_log.csv added; the three statements true only after G2 are on the G2 list (report §6.4).
- C3 partly [run]: cuts (-87/-87/-119 words) are real. My counts (space-separated tokens, headings in): Introduction to Conclusion 5,219 without tables and captions, 5,803 with; all but references 6,772. Report §6.10 says 5,233 / 5,835 / 6,800: +14/+32/+28, the same offsets at 49e8ae4, so a counting-rule difference [inference]. The rule is the author's decision.
- C4 confirmed [read]: "more than any wording of the intended grade moved them".
- C5 partly [read]: "in exploratory analyses" (Conclusion) and "(exploratory)" (two notes) added; see error 3.
- C6 confirmed [read]: "meant for beginning readers".
- C7 confirmed [run]: bare-H tracking is lowest for Haiku (0.18) and Mistral Small (0.46), others 1.17 or more; now checked.
- C8 partly [read]: Sclar as ICLR 2024 paper, Javourey-Drevet 43(2), cover letter reworded; see error 4.
- C9 confirmed [run]: "point estimate" in four sentences; largest |L3 shift| 0.96; check_claims entry.
- C10 partly [run]: "post hoc" in Results 12 to 9, one umbrella clause.
- R2 S5 confirmed [run]: SDs 0.284 and 0.279 recomputed from measures.csv; "as low as" holds.
- R2 S7 partly [run]: Results sentence right; Discussion sentence wrong (error 1).

NEW ERRORS (by severity)
1. Discussion: "Naming the region made the texts of four models harder ... by about half a model-internal year on average." Half a year (0.57) is the six-model figure; the four models' own is about 0.9 [run]. check_claims ties the sentence to the pooled placeholder, so it misses this. Luna's interval [-0.032, 0.000] touches zero (p = .051). Fix: "about half a year across six models, about nine-tenths for the four that moved"; add a four-model placeholder; give per-model differences with intervals in an SI table.
2. Length: three counts disagree (title page 5,051; report 5,233; mine 5,219) and the §6.10 cut candidates total about 540 words, not 800. Fix: one rule in render.py and the report; recompute the cut list.
3. Unlabelled exploratory claims: Conclusion sentence 3 ("The model mattered more than the label"), the Implications point-estimate sentence, the cover letter's matching claim. Fix: "(exploratory)" or "in this sample".
4. Yan et al. was read only as arXiv v2, yet the cover letter says "published in this journal". Fix: G2 list, or "reported in a review".
5. References: render.py's sort keeps accents, so "État de Vaud" follows Yan; "[Conference paper]" is not an APA 7 descriptor [inference].
6. Machine-sounding [inference]: "A teacher does not meet an average; each tool runs on one model"; 55 semicolons in 5,374 words of main text.

CHECK RESULTS
Placeholders [run]: all new ones name their quantity (three of four heterogeneity contrasts; per-model L2-L1 levels, four models -0.016 to -0.042, Haiku +0.004, Sol -0.004; 0.28 = SD of shifts, bare P label).

Bundle [run]: 348 files, 339 members; 10 excluded (title pages, cover letters, verification_report.md, the script, two bundle_sim scripts). My scan of 331 text members, both .docx, 3 PDF and 3 PNG found no author name in any case, ORCID number, university, e-mail domain, AsPredicted number or private-document link; only the word "ORCID", generic aspredicted.org help links and three paths with a generic account name remain. Nothing identifying left.

Findings log [read, run]: 160 rows, 9 columns, matches the README; the correction column is full. README says each row has its refutation, but 44 do not (design-stage readings); 2 rows are not reader findings; C1 to C10 still read "to confirm". Log this reading and update the README count.

Scripts [run]: check_numbers PASS (also --docx on manuscript.docx; its 5 planted faults FAIL); check_claims PASS (--plant FAIL; my ten planted faults caught); check_citations PASS (24 cited; 3 plants FAIL); recompute_primary PASS (20 values; plant FAIL); check_history PASS; anonymisation exit 0; pandoc rebuild identical. Not run: GitHub Actions run_all, verify_refs.

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Scripts et sorties gardés dans records/reader_scripts/confirm2/ ; scan_bundle.py, qui contient les chaînes à chercher, est exclu de la copie anonymisée. Corrections faites ensuite par la session principale : voir CHANGELOG.md et findings_log.csv, lignes E1 à E6.)

## Troisième lecture de confirmation, étroite (claude-sonnet-5-5), consigne

(Consigne donnée telle quelle, lancée à 15:19 sur le commit 1ba5083 par la session principale, qui n'a pas pris part à la lecture.)

You are a separate reader confirming a last, small set of corrections to a research manuscript. You did not make them and must not assume they work. Begin your report with exactly: "Internal reading by a separate AI session. Not peer review."

Context. ART 5 is a preregistered audit of French reading texts written by six language models for Swiss grade labels. A second confirmation reading (claude-sonnet-5-5, report at the very end of manuscript/records/p7/p7_records.md, findings 1 to 6, logged as E1 to E6 in manuscript/records/findings_log.csv) found six points in commit 34545cc. The main session then made commit 1ba5083. Your task is narrow: confirm that these corrections are real and correct, and find any error they introduced. Do not re-review the whole study.

Files (read only; do not edit, create or delete anything in the repository; write any script or temporary file only under /tmp/confirm3_p7/):
- Repository (git worktree): /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/p7/wt at commit 1ba5083. `git -C <worktree> diff 34545cc 1ba5083 -- manuscript/manuscript.md manuscript/submission manuscript/render.py manuscript/references.json manuscript/make_anonymous_bundle.py checks/check_claims.py manuscript/verification_report.md manuscript/records/README.md` shows the changes that matter (ignore build/*.docx).
- Rendered text: manuscript/build/manuscript.md, cover_letter.md, title_page.md; numbers: results/manuscript_numbers.json.
- Do not call any model provider API and do not use the web.

What to do:
1. For each of the six findings, say "confirmed", "partly" or "not fixed", with the location and evidence. For finding 2, run the word counts yourself by the rule now written in manuscript/render.py (function words) and check that the title page and section 6, item 10 of manuscript/verification_report.md state them, and that the sizes given there for the cut list match the paragraphs they name.
2. Read every sentence whose semicolon was replaced (the diff shows them) and say whether any change of punctuation altered the meaning, broke the grammar or split a sentence badly. List only the problems.
3. Check that the reference list in manuscript/build/manuscript.md is in APA order (diacritics ignored) and that the Sclar et al. entry is well formed.
4. Run checks/check_numbers.py, checks/check_claims.py and its --plant option (which must FAIL), checks/check_citations.py, checks/recompute_primary.py and history/check_history.sh; run `python3 manuscript/make_anonymous_bundle.py /tmp/confirm3_p7/bundle.zip --ref 1ba5083` from the worktree and check that no file of the copy names the author (any case), the ORCID, the university or the AsPredicted number; do not print identifying strings, name the file and the kind of string only.

Report under 500 words: the verdict list, then any new error with a concrete fix, then the check results. Tag what you ran [run], what you read [read], and inferences [inference].

## Troisième lecture de confirmation, rapport complet (lancée à 15:19, reçu à 15:38, 79 appels d'outils, claude-sonnet-5-5), texte intégral

Internal reading by a separate AI session. Not peer review.

Reader claude-sonnet-5-5, commit 1ba5083. Worktree files hash-identical before and after [run]. No memory, web or provider API.

VERDICTS
1. E1 confirmed [run]. Discussion now says "about half a model-internal year across the six models though hardly for two of them". From results/measures.csv: pooled L2−L1 shift 0.569 (0.925 for the four that moved); Haiku +0.004, Sol −0.004, others −0.016 to −0.042. check_claims ties both facts.
2. E2 confirmed [run]. My implementation of the render.py rule gives 5,241 / 5,825 / 6,798, as on the title page and in §6.10 (docx: 5,827 / 6,791). Cut-list sizes match: sensitivity paragraph 115 + Table 3 159 = 274; background 230; Results paragraph 237; Discussion paragraph 133; equivalence paragraph 120; AI statement 212 (150 is 70%); total 799.
3. E3 confirmed [read]: "(both exploratory)" in Conclusion and Implications; letter "Exploratory analyses showed".
4. E4 confirmed [read]: G2 item 14 added; "published in this journal" now qualifies the review.
5. E5 confirmed [run]: 24 entries alphabetical, diacritics folded, État after Conférence. "[Paper presentation]" is an APA 7 descriptor [inference]. Sclar entry is well formed but has no conference date or city.
6. E6 confirmed [run]: phrase rewritten; semicolons outside brackets 38 to 2 (Table 2 caption); 23 remain in citation brackets. Log and CHANGELOG say 37 replaced; I count 36 (+2 in the letter).

SEMICOLON SENTENCES [read, run]. Grammar intact (regex scan clean). One meaning problem, Abstract: "(all exploratory)" now closes only the "At the same requested age…" sentence, so "Behind these averages, models departed… two years." lost its label. Fix: add "(exploratory)" after "about two years" and write "(also exploratory)" at the end of the next sentence.

NEW ERRORS (minor)
- Implications: "because the model that wrote it changes its vocabulary more than the wording does" is unlabelled. Add "(exploratory)".
- "abstract: 250 words" counts the Keywords line (paragraph: 236); "from the Abstract to the Statements" (report, render.py) runs through the Statements; CHANGELOG's earlier paragraph still quotes 5,233/5,835/6,800. Count the paragraph; say "through".
- Letter says "settings"; the manuscript and §6.14 say temperature [read]. Write "prompts and temperature".
- Letter-by-letter, "État de Vaud" (2012) should precede "État de Vaud, Direction générale…" (n.d.) [inference]; render.py's whole-string key puts "," before ".". Key on the author element's letters.

CHECKS [run]
check_numbers PASS (also --docx); check_claims PASS, --plant FAIL (four claims); check_citations PASS (24 cited); recompute_primary PASS (20 values); check_history PASS (v0.2 to v0.4.10); pandoc rebuild of three docx identical.
Bundle: exit 0, 360 files plus ANONYMISATION.md, 11 excluded (title pages, letters, verification report, the script, three reader scan scripts). My scanner (text, docx members, PDF streams, PNG chunks, paths; author name any case, ORCID, university and acronym, AsPredicted number, e-mail domains, residence, private links) found nothing; one number-pattern hit in results/measures.csv sits inside a longer decimal. It catches planted strings in text, docx, PNG and PDF. Files: /tmp/confirm3_p7/.

(Rapport copié tel quel depuis le message de remise de la session (SubagentHandback), sans retouche. Scripts et sorties gardés dans records/reader_scripts/confirm3/, sans les deux copies .docx de la page de titre et de la lettre que la session avait faites (elles nomment l'auteur) ; ses scripts scan_bundle_confirm3*.py sont exclus de la copie anonymisée. Les dernières corrections (F1 à F6 du journal des constats) ont été vérifiées par les contrôles scriptés et par la session principale, pas par une nouvelle lecture séparée.)
