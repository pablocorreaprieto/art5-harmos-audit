# Changelog

Design versions of ART 5 before the preregistration, on 25.10.2026 (v0.1 to v0.4.4), 31.10.2026 (v0.4.5 to v0.4.7) and 1.11.2026 (v0.4.8 and v0.4.9), times in Zurich time (UTC+1). Nothing here is a result of the study; the pilot of 31.10.2026 is reported in v0.4.7 only for the values the design takes from it.

- A "reading" is an internal reading by a separate AI session. It is not peer review and not an outside review.
- Readings are numbered 1 to 9 as in the design dossier and the journal. The briefs and full reports of the nine readings, and of one research session on the journal ladder, are kept verbatim in the review record: `claude/art5/records/relectures_ia.md` in the Claude project, and the Drive document "RELECTURES IA" in folder 04.
- Every finding is one row of the Relectures IA tab of the project journal, with its refutation, its fix and the confirmation of the fix. Every action is one row of the Historique tab.
- Hashes are the first 16 hex digits of SHA-256. `history/hashes.txt` has the full values for every kept version.
- `history/` holds a unified diff from each version to the next, so any kept version can be rebuilt from the current files.
- The main session is claude-opus-5-5. Readers are claude-fable-5-1 or claude-sonnet-5-5, as named below.

## Repository prepared for publication (11.11.2026, about 07:30)

Two scripts written by AI reading sessions held the author's phone numbers, date of birth and street name as search patterns. Before the repository was made public they were edited in every commit that contained them (session claude-fable-5-2, at the author's request). The commits up to 34545cc and the tags `prereg` and `data-v1` are unchanged. Later commits have new identifiers; `history/commit_map_2026-11-11.md` maps the identifiers cited in the records to the present ones. The API keys of 31.10.2026 that remain in the history (commit 9e03e53) were revoked before the main run.

## Submitted to Education and Information Technologies (11.11.2026, 07:12)

Manuscript number EAIT-D-26-14286, acknowledged by the journal on 11.11.2026 at 07:12 (Zurich time). Files submitted from commit c56541d: title page, anonymised manuscript, Supporting Information (filed under the item type "Table" as Online Resource 1). The cover letter was pasted into the Comments field. Author entry and Editorial Manager profile: Independent researcher, Jouxtens-Mézery, Vaud, Switzerland. The session (claude-fable-5-2) read the text of the PDF built by the journal's system (32 pages) before approval: affiliation as above, no author name outside the cover page and the title page. The author asked the session to open the built PDF and approve the submission on his behalf. The repository is made public at submission, as the preregistration and the title page say.

## Anonymised copy offered on request (10.11.2026, about 12:20)

The journal's upload form has no item type for supplementary material, and the anonymised copy of the repository (19 MB) is too large to attach through the browser. At the author's choice, the Supporting Information is uploaded under the "Table" item type and the anonymised copy is not uploaded. The Data availability statement, the title page and the cover letter now say that the anonymised copy is available to the reviewers on request, and the letter says why the Supporting Information is filed as a table. Session claude-opus-5-5.

**Checks.** Locally: render.py, check_numbers, check_claims, check_citations and recompute_primary.

## AI-use paragraph of the Method reworded and moved (10.11.2026, about 08:25)

At the author's request (keep the disclosure, present it better), the same session (claude-fable-5-2) moved the paragraph on the use of an AI assistant from "Design and preregistration" to its own subsection at the end of the Method and reordered it: the author's part first, then the assistant's tasks, then what lets a reader check the assistant's work (preregistration, numbers filled in by script, archived prompts, outputs and code), with the note that the AI reviews are not an independent review. No fact was removed. The statement on the use of generative AI now names this session and what it reworded (`reader_id_fable52` in `manuscript/process_facts.json`). The cover letter has one added sentence on how the assistant's work can be checked.

**Checks.** Locally: render.py, check_numbers, check_claims, check_citations and recompute_primary PASS. Not rerun: the GitHub Actions suite and the anonymised copy.

## Competing interests: paid Claude subscription disclosed (10.11.2026, about 08:15)

A new session (claude-fable-5-2) read the rendered manuscript before submission, re-read the journal's submission guidelines (unchanged for the points checked on 2.11.2026) and recomputed the main figures by hand from the numbers in the text. At the author's decision, one sentence of the Competing interests statement now says that the author holds a personal paid subscription to Anthropic's Claude service. No other text changed. The title page carries the same sentence and its whole-manuscript word count moved from 7,660 to 7,671.

**Checks.** Locally: render.py, check_numbers, check_claims, check_citations and recompute_primary PASS. The GitHub Actions suite has not been rerun on this commit.

## Shorter statement on the use of AI and two added sources (2.11.2026, 08:45 to about 09:30)

**Statement.** At the author's request (08:43), the statement on the use of generative AI was shortened without removing any fact. It now has 154 words instead of 347: the assistant's tasks, the review sessions (one of whose models is also audited), the author's part and responsibility, and a pointer to the records in the repository. The Methods paragraph says the statement sums up who did what. The cover letter's paragraph on the protocol is shorter in the same way.

**Sources.** Two sources suggested by referee 2 of the pre-submission audit, read by the main session (abstracts and, for the first, the introduction and method): Kuzu, Irion and Bay (2025, in Education and Information Technologies) on prospective primary teachers prompting ChatGPT, cited in the Introduction, and Myung et al. (2024, BLEnD) on everyday knowledge of cultures less represented online, cited in the Discussion of the probe errors. References, litnotes (part A1) and verify-refs updated. Two more suggested reviewers were looked for, but no institutional e-mail could be confirmed on an official page, so none was added.

**Files for the submission (saved at 10:55).** The files prepared for Education and Information Technologies are the builds at a48a3fb: `manuscript/build/manuscript.docx`, `title_page.docx`, `cover_letter.docx`, and `manuscript/build/supplement.pdf` (ESM 1, converted from `supplement.docx` with LibreOffice and now kept in the repository). ESM 2, the anonymised copy, is rebuilt with `python3 manuscript/make_anonymous_bundle.py ESM_2_anonymised_repository.zip --ref 1424109`. Not yet submitted: the author still reads the changed passages and submits himself.

## Author's advice to teachers and AsPredicted link (2.11.2026, 08:20 to about 08:50)

**AsPredicted.** At the author's request, the main session made the public PDF of registration #321415 in his browser session, in its anonymous form, which AsPredicted recommends while a paper is under review (author names appear once the author deanonymises it after acceptance): https://aspredicted.org/zv58ce.pdf. The link is on the title page for the editor (process fact `aspredicted_url`) and replaced in the anonymised copy, since the registered text gives the repository address.

**Implications.** The author wrote the advice to teachers (four paragraphs) that now opens the Implications section, in place of the assistant's sentences on teachers. The main session checked it against the results (per-model shifts with the bare H label and with the label and the age, the post hoc comparison of models) and kept, after it, the sentences for developers and for research, with one sentence naming the analyses the advice rests on. The Methods paragraph on the assistant, the use-of-AI statement, CRediT (writing – original draft for that part) and the cover letter say so. `check_claims`: the two claims of the replaced sentences removed, two added for the author's wording.

## Pre-submission audit (2.11.2026, 06:30 to about 08:00)

**Protocol.** The author asked for a protocol to audit an article before each submission. The main session wrote it (`manuscript/records/audit/protocole_audit_v1.0.md`, also in the author's Drive) and applied it to this manuscript for Education and Information Technologies.

**Independent reviews.** Three separate sessions (claude-opus-5-5), with no access to the drafting conversation, earlier readings or the audit: a methods and statistics referee, a reading-education referee and an editor's assessment before review. Briefs and reports verbatim in `manuscript/records/audit/` (left out of the anonymised copy, like the G2 records, because they discuss the choice of journal; their recommendations are in `manuscript/verification_report.md`, section 8); each finding is a row of `manuscript/records/findings_log.csv` (AU1 to AU16, and AU17 from the read-back of the portal sheet, whose short funding answer contradicted the manuscript and was corrected). Referee 1 recomputed the measure from the raw outputs and found it identical to the archived results.

**Author's choices (07:00).** New general title; affiliation given as independent researcher with city and country of residence, which the journal publishes for unaffiliated authors; the AI statement keeps the full list of the assistant's tasks without the summary phrase "did most of the research work". The author did not rewrite any section, so the statement still says that he read and approved the manuscript.

**Changes.** b9f19ef: protocol, Crossref "updated-by" notices in verify_refs, audit records left out of the anonymised copy. 8a6abf6 and 1a708d5: `exploratory_audit.py` (post hoc) run on the official lexicon in GitHub Actions (run 41397357903): leaving out the 0.53% of content words absent from Lexique changes no test decision (H level −0.014, p < .001; P level −0.003, p = .433). 8d5166a: abstract, Implications and Conclusion reworded (the pooled H result rests on one model; adding the age is a precaution, not a finding; read each text), measure description corrected (absent words count as content words of frequency zero, as preregistered), reason for Lexique rather than Manulex, scope of the Vikidia check, reasoning analysis of Mistral Large 4 with all specifications and a t-based interval, d_z in Table 2, ruler t and linearity tests in Table 3, post hoc row in Table S1, figures 2 and 3 renumbered in citation order, the journal's style (bold "Fig. N" captions, numbered headings, page numbers, declarations repeated on the title page), CRediT limited to the author, consent statement, sampling parameters, software, limits (validity scope, « à lire », bootstrap over 16 topics, no reviewer independent of Anthropic's models). 0b0d80d: four sources verified in full text by a separate session (Valentini et al., 2023; the Dutch, Belgian and Québec school starts) and a paragraph on the three questions the design keeps apart.

**Checks.** Locally after each change: render.py, check_numbers, check_claims (planted error fails), check_citations, recompute_primary. GitHub Actions: verify-refs 41396681921 on b9f19ef (PASS, planted FAIL), run-all 41399373406 on 8d5166a (ALL CHECKS PASSED), verify-refs 41401062224 (PASS, planted FAIL) and run-all 41401065069 (ALL CHECKS PASSED, 17 checks) on 0b0d80d, outputs 2d3fe66 and 898b04f (see `manuscript/verification_report.md`, section 8). Anonymised copy at 0b0d80d: 462 files, no identifying string, audit records excluded.

## Gate G2 and preparation for submission (1.11.2026, 18:58 to about 21:30)

**Decisions.** The author read the final manuscript and answered the open questions of `manuscript/verification_report.md` (section 6) in five rounds of multiple-choice questions, 18:58 to 19:52. Section 7 of that report lists each answer. In short: conflicts of interest as written; the AI use stays disclosed in full and the statement now also states the author's part (topic, the main rules of the protocol, infrastructure, design decisions); affiliation and e-mail for the title page; the repository goes public at submission; no preprint; a separate check reading of these changes before submission. The origin of the promotional credit was first given as the author's Claude Max plan, from an Anthropic e-mail of 17.10.2026 that the main session's question quoted; the check reading found that this grant expired on 31.10.2026, and the console shows the pilot and the main run paid from a promotional grant of 100 USD of 28.10.2026 (source in `manuscript/process_facts.json`).

**Journal ladder.** BJET and JCAL were judged too selective for a first publication, L1-ESLL was set aside after its own page showed a 95% rejection rate in 2025, and the Swiss Journal of Educational Research is kept for another article. Three research sessions (claude-sonnet-5-5: hybrid journals, diamond open-access journals, other routes) and the main session's own checks gave a ladder of five journals, to be tried one at a time: Education and Information Technologies (Springer), Education in the Knowledge Society, Computers in the Schools, Reading Psychology, Research in Learning Technology. Acceptance rates are those the journals publish; where none is published, the estimate is marked as an inference.

**Changes.** f303b58: statements (Competing interests, Funding, Limitations, Use of generative AI, CRediT with methodology and resources), title page and letter, `manuscript/process_facts.json` (sources of the credit origin and of the author's roles). f710101: format for Education and Information Technologies (practitioner notes removed, the AI use also documented in the Method as Springer asks, heading "Statements and Declarations", "Competing interests"; `render.py` counts to the new heading; the claim that only matched the practitioner notes removed from `checks/check_claims.py`; letter addressed to the journal). Then the letter addressed to the editor-in-chief.

**Checks.** render.py, check_numbers, check_claims (with the planted error failing as required), check_citations, recompute_primary and history/check_history.sh PASS on f710101. Anonymised copy at f710101: 396 files, nothing identifying. GitHub Actions on the branch `g2-submission`: run-all 41342321846 (outputs 07824a6) and verify-refs 41342324280 on f710101, and run-all 41344501275 on 14a3165 after the fixes (outputs 31fe104), all successful ("ALL CHECKS PASSED").

**Check reading (about 20:40 to 21:00).** A separate session (claude-sonnet-5-5) read the G2 changes: two blocking findings (the AsPredicted link, given by the author at submission, and the credit, corrected as above), five to fix (the author's part overclaimed in "conceived the study", "designed the written protocol" and "deposited the preregistration"; the assistant's part understated after "did most of the work" and the agent of the citation check were dropped; the author to read the changed passages; the title page's financial-relationship clause) and five minor (CRediT note on the assistant's roles, literature search in the Method, process facts, how reviewers get the anonymised copy, the letter's salutation). All applied except the AsPredicted link. Briefs and reports of the three research sessions and of the check reading: `manuscript/records/g2/g2_check_reading.md` (left out of the anonymised copy). Findings: rows G1 to G12 of `manuscript/records/findings_log.csv`.

**Literature.** Yan et al. (2024) is open access; its published version contains the recommendation the manuscript cites (Discussion, section Implications). Li et al. (2025) and Mesmer (2024) can be reached only through the author's UNIR login and stay uncited.

## Manuscript revision after the internal readings (P7, 1.11.2026, 12:32 to about 14:00)

**Readings.** Three separate sessions read the rendered draft (R1 substance, claude-opus-5-5; R2 methods and statistics, claude-sonnet-5-5; R3 editor's reading for BJET, claude-fable-5-1), a fourth checked 44 sentence-citation pairs against the full texts (claude-sonnet-5-5), and two more tried to refute the findings (R1 by claude-fable-5-1; R2 and R3 by claude-opus-5-5). Briefs and full reports: `manuscript/records/p7/`. No confirmatory number changed.

**Main changes.** Claims reframed as lexical equivalence with each model's own age-only texts, in model-internal years; heterogeneity between models reported where pooled results are stated (H2-H rests on Claude Haiku 5.5); the region and age wordings compared with the bare label; post hoc analyses added and labelled (`exploratory_p7.py`: spread between models, equivalence reading, tests of differences between models, reasoning tokens, leave-one-model-out, observed offsets per grade, ages stated in the reasoning of Mistral Large 4, precision of the P tracking interval, intervals of the default reader age, counts of two Swiss words); recommendations limited to what was shown; the "480 texts per topic" error corrected; the two departures from the registration stated; statements completed (Anthropic promotional credit, every model used in the research process, protocol and records in the repository, CRediT); title and keywords; four references added after reading them (Javourey-Drevet et al., 2022; Sclar et al., 2024; Yan et al., 2024; État de Vaud, 2012); `checks/check_claims.py` added; the explanation of the lexicon-copy difference corrected (*vrai* and *faux* in capitals, not « œ »).

**Documentation version v0.4.10.** `README.md` only: status after the deposit and the data freeze, new files. `PREREG.md` is unchanged, as deposited. `history/v0.4.9_to_v0.4.10.diff`, hashes added, `history/check_history.sh`: PASS.

| File | Hash |
|---|---|
| README.md | 75650296b6d57bb0 |
| other files | as in v0.4.9 |

**Confirmation of the corrections (13:46 to 14:16) and fixes (14:16 to 14:36).** A separate session that had made no correction (claude-fable-5-1) checked every finding that the refutations kept, recomputed the new post hoc numbers without importing `exploratory_p7.py`, read the four sources added after the readings and ran the checks on commit 49e8ae4 (report at the end of `manuscript/records/p7/p7_records.md`, scripts in `manuscript/records/p7/reader_scripts/confirm/`). Most corrections were confirmed; the numbers reproduced. It found one regression: `make_anonymous_bundle.py` stopped on that commit, because a reading session's script holds the author's names in lower case and the rendered title page and cover letter (.docx, not scanned) name the author. Fixed: those files are left out, the name replacements ignore case and binary files are scanned. Other fixes: wordings it found wrong or too strong ("every model's point estimate", "the two whose texts followed the grade least", "any wording of the intended grade", "meant for beginning readers"), exploratory labels in the Conclusion and practitioner notes, the effect of the region given model by model (four models; near zero for Claude Haiku 5.5 and GPT-6.1 Sol), the tie of the gloss with the bare P label stated, the F statistics and the probe-rule checks moved to Supporting Information S1, a few sentences shortened (word counts given at this step by an earlier rule; see the next paragraph for the counts by one rule), Sclar et al. listed as an ICLR 2024 paper and the issue of Javourey-Drevet et al. added, the cover letter's "this journal's call" toned down, and the per-finding log of the journal exported to `manuscript/records/findings_log.csv`. New entries in `checks/check_claims.py`. A second, narrower confirmation reads these fixes.

**Second confirmation (14:37 to 15:11) and fixes (15:11 to 15:17).** A separate session (claude-sonnet-5-5) confirmed the anonymisation fix (it planted a name in a .docx and in a binary file, and the script stopped), the findings log and most wordings, and found six more points: the Discussion tied "half a model-internal year" to four models although it is the six-model value; three word counts disagreed; three exploratory claims lacked a label; Yan et al. was read as a preprint while the letter says "published in this journal"; the reference list sorted "État" after "Yan" and used a non-APA descriptor; and the prose had many semicolons and one phrase that sounded machine-written. Fixed: the region sentence, one word-count rule in `manuscript/render.py` used by the title page and the verification report (5,241 words from the Introduction to the Conclusion, 5,825 with tables and captions, 6,798 without the references only) with a recomputed cut list for G2, the labels, the letter's wording and a G2 item on Yan et al., the sort and the descriptor, 36 semicolons of the running prose and 2 of the letter, and the README of the records. The anonymisation script also leaves out reader scripts named `scan_bundle*.py`. A third, narrow reading checks these fixes.

**Third confirmation (15:19 to 15:38) and last fixes.** A separate session (claude-sonnet-5-5) confirmed the six fixes, recomputed the word counts and the sizes of the cut list, found the grammar of the sentences whose semicolon was replaced intact and the anonymised copy clean (it planted strings in text, .docx, PNG and PDF files and its scanner caught them), and listed small points: after the semicolon was replaced, the abstract's "(all exploratory)" covered only its last sentence; one exploratory clause of the Implications had no label; the abstract count included the keywords line; the letter said "settings" where the manuscript says temperature; "État de Vaud" (2012) should precede "État de Vaud, Direction générale" (n.d.); and 36 semicolons were replaced, not 37. All fixed (labels, abstract paragraph counted alone, 237 words; sort on the author element; letter; counts: 5,242 words from the Introduction to the Conclusion, 5,826 with tables and captions, 6,800 through the Statements). These last fixes were checked by the scripts and by the main session, not by a further separate reading.

**Merge, checks and delivery (15:40 to 16:05).** Branch `p7-revision` fast-forwarded into `main` and pushed (2029f0f), then the cover letter's signature put on three lines (90ae120). GitHub Actions on 2029f0f: run-all (run 41317370806) 17 of 17 PASS on the official lexicon; verify-refs (run 41317380753) PASS, every reference with a DOI or an arXiv id matched. Anonymised copy built on f5c82c2: exit 0, 396 files, nothing identifying. Reading copies of the manuscript, the Supporting Information, the cover letter and the title page in the author's Drive (02 RÉDACTION); the .docx files are in `manuscript/build/`. Gate G2 is next.

## Deposit (1.11.2026, 08:50 to 08:55)

- **AsPredicted #321415**, approved by its only author on 1.11.2026 at about 08:52 (Zurich time), private until made public. The deposited text is `PREREG.md` at tag `prereg` (commit 6a0a061, design v0.4.9), entered field by field; the SHA-256 of each of the ten text fields, read back from the form before the preview, matched the file.
- Tag `prereg` was created by publishing a GitHub release on commit 6a0a061, at Pablo's request ("aprove"), because the session's own tag push was refused (HTTP 403).
- A first click on APPROVE, on the preview opened at 07:31, returned an empty form and created nothing (the account listed no pre-registration). The preview had probably expired [inference]. The form was filled again with the same ten hashes, previewed and approved.
- Main data collection: workflow step `generate`, run 41286684728 on commit 6a0a061, plan budget 50 USD, started at about 08:54.
- Keys. During the run Pablo put new OpenAI and Mistral keys in the two secrets (the running job kept the old ones), and at 11:29, after the run, he revoked the old keys. Checked in both consoles: the old OpenAI key shows as revoked and the old Mistral key is no longer listed. Commit 9e03e53 now holds only revoked values, which clears the item listed for G2 in v0.4.6 and v0.4.8. The new keys expire about 1 December 2026. Provider credit before the run: Anthropic 206.87 USD (5.00 purchased, 201.87 promotional), OpenAI 19.45 USD, Mistral 10.00 USD.

## v0.4.9 (1.11.2026, about 07:30 to 07:45)

**Why.** The name field of the AsPredicted form (question 9) holds at most 80 characters (maxlength of the field), and the v0.4.8 name had 152.

**Changes.** `PREREG.md`, question 9: "Swiss grade labels and the lexical demand of LLM-generated French reading texts" (79 characters), the study name of `design.json` without "ART 5,". Status line of `PREREG.md` and `README.md`, version line of `design.json`.

**Checks.** `history/check_history.sh`: PASS, v0.4.9 down to v0.2. No code file changed.

**Reading.** None. The change only fits a form limit.

**Hashes.**

| File | Hash |
|---|---|
| PREREG.md | f94164b6faddb549 |
| README.md | 3f157bf29193245e |
| design.json | d0d2672284783290 |
| other files | as in v0.4.8 |

## v0.4.8 (1.11.2026, about 06:50 to 07:27)

**Why.** Pablo passed gate G1 at 06:48 ("i read everything you can check and fix mistakes then go, dont send too much on apis if possible"). Reading 9 (claude-sonnet-5-5, 06:50 to 07:13, read-only, no model call) checked `PREREG.md` against the code and `design.json`, the AsPredicted Google Doc against `PREREG.md`, and the pilot and validation figures. It found no figure in `PREREG.md` that contradicts the code or the results, and ten points to fix. The main session checked each point in the files before acting. The AsPredicted form itself (questions version 2.00), opened before the deposit, has radio buttons for question 1, numbers the title 9 and the type of study 10, adds 11 data source, and its help page limits each answer to 2,900 characters.

**Changes to `PREREG.md`.**

- Layout. The questions follow the form: 1 data collection, 2 to 8 as before, 9 name (the former title), 10 type of study, 11 data source.
- Q1. Option ticked: "It's complicated", with the explanation in question 8, as the form asks. The form does not accept "Yes", and "No" would contradict the pilot. The pilot paragraph moves to the start of Q8. It now says "No data for the confirmatory study have been collected" and adds why the pilot leaves the main hypotheses open: no text was requested with any label other than the age, so the pilot says nothing about H2 and H3, and its texts bear on H1 for three models.
- Q3. The "Voici" preface rule names every form that `compute.VOICI_META_RE` removes (histoire, texte, récit, conte, lecture, poème, with an optional petite, courte, belle or nouvelle); the old text named two. The repository URL replaces `{REPO}`, and the lexicon is named with its source and hash.
- Q4. The French prompt template is written out, and `design.json` and `make_prompts.py` at tag `prereg` are cited for the topics, label wordings and call plan. Reasoning stays at each provider's default and counts toward the 4,000-token limit. In the pilot raw records, thinking or reasoning tokens were present in 61 of 72 texts of Claude Sonnet 5.5 (mean 331 tokens in those texts), 68 of 72 of GPT-6.1 Sol (79) and 72 of 72 of Mistral Large 4.0 (1,104, 67% of its output tokens). Collection dates 1 to 15 November 2026.
- Q6. "No exclusion uses the value of the dependent variable or of any other frequency measure". The old wording, "a lexical measure", read as if length and the share of words absent from Lexique were never used. New rule: if the spending cap stops collection, it resumes only after the author raises the cap, and calls without an answer by 15 November 2026 are missing.
- Q8. The validity criterion includes the 25 usable pairs that `validate_measure.py` requires, and the result of 31.10.2026 (28 of 29).
- Length. The longest answer is Q3, 2,379 characters, or 2,689 if every quotation mark and accented letter counted as an HTML entity.

**Other changes.** `design.json`: version line, and "exact dated id" becomes "exact id ... in models.json", since no provider lists a dated id for these six models. `README.md`: version line and the same wording.

**Checks.** `checks/plan.py`: PASS. `history/check_history.sh`: PASS, v0.4.8 down to v0.2. No code file changed since v0.4.6, so the full run of v0.4.6 (12 of 12) stands for the code, on the lexicon copy named below.

**Verified, not changed.**

- The counted pilot spend matches the provider consoles: Anthropic 1.42 USD and OpenAI 0.55 USD for 84 requests, against 1.4185 and 0.5513 counted from the raw records. Mistral's billing page could not be read from the browser (0.2857 counted).
- With the lexicon copy of the `pylexique` package (fe2cb931f774d4c4), which the local checks use, 36 of the 216 pilot measures differ from those computed in GitHub Actions with the lexique.org file (637ba37a767a6667), by at most 0.064 Zipf (mean 0.022 among the 36). The study uses the lexique.org file. The pilot step runs `compute.py --self-test` on that file before any call and stops if it fails; it went on. The sandbox cannot reach lexique.org, so a full check run on that file is listed for P6, in GitHub Actions.
- The docstring of `sim_power.py` gives the control bound as 0.0627; the code and `sim_power_results.json` use 0.0613, as the dossier says. Comment only, left unchanged.

**Reading 9.** Its ten findings are rows of the Relectures IA tab; its brief and report are in the review record. Five concern the design dossier, not the repository: the journal ladder after G1, topics written as still open, steps written as future, a rule "H1 fails for at least four models of six" that neither `PREREG.md` nor the code has, and the budget assumptions. They are fixed in the dossier.

**Hashes.**

| File | Hash |
|---|---|
| PREREG.md | ca124e2132a25c53 |
| README.md | 2e4d2203762ba9d3 |
| design.json | 52ef93b9b4989f23 |
| generate.py | 10085215000e27f6 (unchanged) |
| compute.py | 8ad7a56512616c64 (unchanged) |
| analyze.py | 62324d6d5c6293c2 (unchanged) |
| pipeline.py | bc409da02b73fa9f (unchanged) |
| make_prompts.py | 739ea744914f9237 (unchanged) |
| run.yml | 497409fc94c1df59 (unchanged) |

**Listed for G2.** Commit 9e03e53 still holds the OpenAI and Mistral keys in the history of the private repository; rotate them, or rewrite that commit, before the repository is made public. Rerun `checks/run_all.sh` on the lexique.org file (P6). Fix the `sim_power.py` docstring at the next code change.

## v0.4.7 (31.10.2026, about 19:30 to 19:40)

**Why.** The model listing (run 41225923569) and the pilot (run 41229061481, 19:22 to 19:28) gave the values that `PREREG.md` left in braces, as planned.

**Pilot, as recorded in `results/pilot_summary.json` and `logs/run_*.json`.**

- 252 calls launched, 251 answered on the first pass. One Mistral probe used its 4,000 output tokens on reasoning and returned no text; it was asked again in the second pass and answered. Counted spend 2.2554 USD for a plan budget of 3 USD (Anthropic 1.4185, OpenAI 0.5513, Mistral 0.2857), nothing counted as possibly charged.
- 216 of 216 age-only texts kept, no exclusion, no answer flagged as addressing the user, no line removed, a title in every text. One Mistral text stopped at the token limit (kept and flagged as truncated). Median length 596 words (Claude Sonnet 5.5), 419 (GPT-6.1 Sol), 351 (Mistral Large 4.0).
- Ruler: residual SD 0.117 (upper 80% bound 0.122), pooled slope -0.0449 Zipf per year (SE 0.0049, one-sided p 2e-20), per model -0.044 (Anthropic), -0.036 (OpenAI), -0.055 (Mistral). The flat-ruler stop rule does not apply.
- Simulated power of the H2-H level test at 0.04 Zipf (1,000 data sets per option, planning slope -0.04): .835 with 16 topics, .974 with 24, .994 with 32. The rule gives 16 topics, as already set in `design.json`.
- Probes: 36 of 36 parsed; 31 of 36 state more than one age range, and the rule takes the first. Accuracy not computed before the deposit.

**Changes.**

- `PREREG.md`. Pilot date, 16 topics, 7,680 texts and the six model ids filled in; the pilot values added at the end of question 7; the status line says which fields remain for the deposit (`{REPO}`, `{START_DATE}`, `{END_DATE}`).
- `design.json`, `README.md`. Version line; README says where the pilot outputs are.

**Checks.** `checks/plan.py`: PASS (the call files are unchanged). `history/check_history.sh`: PASS, v0.4.7 down to v0.2. No code file changed since v0.4.6, so the full run of v0.4.6 (12 of 12) stands for the code.

**Reading.** None. Only fields that the design said the pilot would fill were filled.

**Hashes.**

| File | Hash |
|---|---|
| PREREG.md | 411fbce4113b7d20 |
| README.md | bd7c45ebd5def95f |
| design.json | 06dc537dc8c6ba9c |
| generate.py | 10085215000e27f6 (unchanged) |
| compute.py | 8ad7a56512616c64 (unchanged) |
| analyze.py | 62324d6d5c6293c2 (unchanged) |
| pipeline.py | bc409da02b73fa9f (unchanged) |
| make_prompts.py | 739ea744914f9237 (unchanged) |
| run.yml | 497409fc94c1df59 (unchanged) |

**Listed for gate G1.** As in v0.4.4, plus: the number of topics (16) and the spending cap set from the pilot; the probe rule when an answer gives several age ranges (31 of 36 in the pilot); Claude Sonnet 5.5 writes texts about 1.5 times longer than the two other models (length is measured and residualised in a sensitivity analysis); Mistral Large 4.0 reasons by default, and 2 of its 85 calls stopped at the 4,000-token limit, one of them (a probe) with all its tokens spent on reasoning and no text.

## v0.4.6 (31.10.2026, about 18:06 to 18:37)

**Why.**

- The second workflow run (step list-models, run 41222817007 on 65e9bb3, committed at 18:05:57) found the secret `ANTHROPIC_API_KEY` holding three values on separate lines: an Anthropic key identifier, the OpenAI key and the Mistral key. Python refused the header before sending it (ValueError, invalid header value), and `generate.py` stored `repr()` of the error, which quotes the header. The workflow committed that text in `logs/models_2026-10-31.json` (commit 9e03e53) and kept it in the run's artifact. Nothing was sent to a provider with that header and nothing was billed. The OpenAI and Mistral lists (status 200) were recorded normally.
- The same path would have written the keys into every raw line of a pilot run, each call failing the same way and being counted at the worst case of its model.

**Done before this version.**

- Commit 9805078 (18:10) replaced the error text in `logs/models_2026-10-31.json` by the error type and a note. The rest of the file is as the run wrote it. Commit 9e03e53 still holds the text in the history of the private repository, and the run's artifact holds it until deleted.
- Pablo was asked at 18:09 to revoke the exposed OpenAI and Mistral keys, to put exactly one key in each secret, and to delete the artifact. The session does not delete data.

**Changes.**

- `generate.py`. `key_problem` checks each key secret before any request: empty, line breaks, spaces or tabs, or characters that are not printable ASCII. `list-models` records the problem for that provider, without the value, and asks the others. `run` stops before its first call and before opening a raw file. `scrub` removes every key value, whole or split on white space (parts of 8 characters or more), from error texts, from the model list and from every raw line. Docstring updated.
- `checks/e2e_secrets.py`, a new check in three parts, with fake keys and local servers only. `checks/run_all.sh` runs it. The history check now always runs and fails when its script is missing, as listed in v0.4.5. `checks/README.md` updated.
- `design.json`, `PREREG.md`. Version line. `README.md`. Version line, the `generate.py` row, and one key per secret, on one line.

**Checks.**

- `checks/e2e_secrets.py`: PASS on v0.4.6. Failure control: the v0.4.5 code fails all three parts, with the fake keys in the model list, in 6 raw lines and in the 401 records (`checks/outputs/failure_controls/e2e_secrets_on_v0.4.5.txt`).
- `run_all.sh` on an empty code folder: all 12 checks fail, the history check included (`checks/outputs/failure_controls/run_all_on_empty_code_v0.4.6.txt`).
- `history/check_history.sh`: PASS, v0.4.6 down to v0.2.
- Full `checks/run_all.sh` run on v0.4.6, in `checks/outputs/`: 12 checks of 12 passed (ALL CHECKS PASSED), 18:14:51 to 18:34:52 (20 min 1 s), Python 3.13.18, lexicon fe2cb931f774d4c4 (pylexique copy). 59 of 59 mutations of `compute.py` and 22 of 22 of `analyze.py` caught. The battery and clarifications outputs are identical to those of the v0.4.5 run. e2e_crash counted 0.7204 then 0.7775 USD for a budget of 0.8. The v0.4.5 outputs are kept in `checks/history/run_20261031T161744Z/`.

**Reading.** None. The fix answers a failure seen in a run, and the new check has its failure control.

**Hashes.**

| File | Hash |
|---|---|
| generate.py | 10085215000e27f6 |
| design.json | 142c1dca51b5747a |
| PREREG.md | 710b106df167e4d4 |
| README.md | 50fbf891d6c9da53 |
| compute.py | 8ad7a56512616c64 (unchanged) |
| analyze.py | 62324d6d5c6293c2 (unchanged) |
| pipeline.py | bc409da02b73fa9f (unchanged) |
| make_prompts.py | 739ea744914f9237 (unchanged) |
| sim_power.py | dd9eb28c54889fde (unchanged) |
| sim_power_results.json | 11fb624153b742b4 (unchanged) |
| validate_measure.py | 7253e08b8dc1cd02 (unchanged) |
| run.yml | 497409fc94c1df59 (unchanged) |

**Listed for gate G1.** As in v0.4.4.

## v0.4.5 (31.10.2026, about 17:17 to 17:40)

**Why.**

- Mistral's model list marks Mistral Medium 3.5 (v26.04) as deprecated on 31.10.2026, with retirement on 30.04.2027, and names Mistral Large 4 as its replacement. The model is still callable, but the study would audit a model retired before the article appears. Pablo decided in the chat of 31.10.2026 to switch to Mistral Large 4 before the pilot. No model had been called.
- The first workflow run (step lexicon, run 41219166928, 31.10.2026) succeeded but committed nothing. `git add -A data/raw results logs calls*.jsonl` stops on the first path that does not exist, and the error was hidden by `2>/dev/null || true`. So the steps that write only `logs/` (lexicon, list-models, validate) would never have saved their outputs to the repository, only to the run's artifact.

**Changes.**

- `design.json`. `mistral_balanced` is now "Mistral Large 4 (exact dated id read at pilot; replaces Mistral Medium 3.5, deprecated on 31.10.2026)", and the version line says v0.4.5. The model keys, labels, prompts, topics, pilot blocks and analysis are unchanged.
- `run.yml`. The save step adds each output path only if it exists. Tested in a scratch repository with `logs/` only: the old line stages 0 files, the new one stages the log.
- `README.md`, `PREREG.md`. Version line.
- `history/check_history.sh` is executable again (git mode 100755, content unchanged). The repository rebuilt on 31.10.2026 from the project copies had it as 100644, and `run_all.sh` runs the history check only when the script is executable, so it would have been skipped without a message. The outputs of 25.10.2026 include `history.txt`, so the bit was set then (inferred from those outputs). Found and fixed while the v0.4.5 run was at `mutate_compute`, before it reached the history check.
- `checks/README.md`. History row and gate wording updated to v0.4.5; the skip above added under Limits.

**Checks.**

- `checks/plan.py`: PASS. The call files are byte-identical to the recorded ones, since they name model keys, not models.
- `history/check_history.sh`: PASS. It rebuilds v0.4.5 down to v0.2 from the current files.
- `compute.py`, `analyze.py`, `generate.py`, `pipeline.py` and the other code files are unchanged.
- Full `checks/run_all.sh` run on v0.4.5, in `checks/outputs/`: 11 checks of 11 passed (ALL CHECKS PASSED), 17:17:44 to 17:39:12 (21 min 28 s), Python 3.13.18, lexicon fe2cb931f774d4c4 (pylexique copy). 59 of 59 mutations of `compute.py` and 22 of 22 of `analyze.py` caught. The battery and clarifications outputs are identical to those of 25.10.2026. e2e_crash counted 0.6898 then 0.7470 USD for a budget of 0.8 (0.7203 and 0.7774 on 25.10.2026; where the connections drop depends on timing). The history check rebuilds v0.4.5 down to v0.2 with every file identical. The previous outputs (25.10.2026, 20:07 UTC) are kept in `checks/history/run_20261025T200733Z/`.
- The checks do not exercise `run.yml`; its fix is tested by the next workflow run.

**Reading.** None. The model change was decided by the author, and the workflow fix answers a failure seen in the first run.

**Hashes.**

| File | Hash |
|---|---|
| design.json | 26eb3c7b0f523661 |
| PREREG.md | 860ea592dfc1ec55 |
| README.md | 9198a840d0c9bb32 |
| compute.py | 8ad7a56512616c64 (unchanged) |
| generate.py | 7ce38baa5b8f397e (unchanged) |
| analyze.py | 62324d6d5c6293c2 (unchanged) |
| pipeline.py | bc409da02b73fa9f (unchanged) |
| make_prompts.py | 739ea744914f9237 (unchanged) |
| sim_power.py | dd9eb28c54889fde (unchanged) |
| sim_power_results.json | 11fb624153b742b4 (unchanged) |
| validate_measure.py | 7253e08b8dc1cd02 (unchanged) |
| run.yml | 497409fc94c1df59 |

**Listed for gate G1.** As in v0.4.4.

**Listed for the next version.** `run_all.sh` should fail, not skip, when `history/check_history.sh` is missing or not executable. Not changed now because `run_all.sh` was running.

## v0.4.4 (21:06 to 21:10, reading of the fix 21:07 to 21:09)

**Why.** Reading 8 found a side effect of the v0.4.3 word boundary: "à quelle", "quels" and "quelles" no longer matched. 6 of its 10 probe clarifications, such as "Peux-tu me dire à quelle classe correspond 5H ?", were flagged instead of excluded.

**Changes.**

- `compute.py`.
  - The alternatives after "dis-moi", "tu veux dire" and "(pourrais|peux)-tu (me |m')dire" are now (ce que|ce qu'|à quel(le)?s?|quel(le)?s?|l'âge), followed by a word boundary.
  - The self-test has 2 more refusals ("Peux-tu me dire à quelle classe correspond 5H ?", "Dis-moi quels âges ont les élèves de 5P..."). Both are missed by v0.4.3.
- `design.json`, `README.md`, `PREREG.md`. Version line.
- `checks/mutate_compute.py`. 4 patterns follow the new formula, and 2 new mutations restore the cut alternatives (59 in all).
- `checks/run_all.sh`, after the run below. It now copies the previous run to `checks/history/run_<UTC date>/` before writing new outputs, because the command that started this run (removing the old outputs, then `run_all.sh`) had erased the outputs of the v0.4.2 run on the repository code, and `run_all.sh` alone overwrites them too (Décisions tab, row 43). Tested at 21:29 on an empty code folder: the previous run was kept and all 10 checks failed (`checks/outputs/failure_controls/run_all_on_empty_code.txt`).
- `checks/history/v0.4.2_run/`. The full run on a work copy of v0.4.2 (20:12 to 20:26, same code files except README.md), kept in place of the erased one.

**Checks.** All 11 checks pass on the repository code (`bash checks/run_all.sh`, 21:07:33 to 21:22:17, outputs and tested hashes in `checks/outputs/`).

- The self-test has 21 reference texts, 20 refusals excluded and 14 texts with a refusal phrase kept. 59 of 59 mutations are caught. The 2 new ones each miss the refusal they restore ("Dis-moi quels âges ont les élèves de 5P...", "Peux-tu me dire à quelle classe correspond 5H ?").
- The battery and the clarification cases give the same counts as v0.4.2 and v0.4.3: nothing wrong on the 33 plausible answers, 14 of 21 requests excluded, 8 of 16 genuine texts excluded.
- End to end: the pilot completes under its budget (0.4267 USD counted for 5, 216 texts), cut responses are counted (0.7774 USD for 0.8 after two runs), and 28 of 28 malformed runs finish. `history` rebuilds v0.2 to v0.4.4.
- The v0.4.3 work copy had passed every check from 20:51 to 21:05. Its outputs are kept in `checks/history/v0.4.3_run/`.

**Reading.** Reading 8, fourth round (claude-sonnet-5-5, 21:07 to 21:09), confirmed the fix.

- 10 of its 10 probe clarifications are excluded again, and its 10 tu clarifications stay excluded.
- "Dis-moi quelque chose", "Tu veux dire quelque chose ?", "Peux-tu me dire quelques noms", "quelqu'un" and "quelquefois" stay kept.
- Its battery, ten answers and N3/N5 tables are unchanged, and the self-test passes.
- Cost, as in v0.4.2: its genuine hooks "Dis-moi à quelle heure...", "quelles couleurs..." and "quels animaux..." are excluded again (3 of 3). This is listed under X4 below.

The review cycles end here.

**Hashes.**

| File | Hash |
|---|---|
| compute.py | 8ad7a56512616c64 |
| design.json | e78f95b14cb18ca2 |
| PREREG.md | 985d1f5d34b7408b |
| README.md | 48abc30cfd94e776 |
| generate.py | 7ce38baa5b8f397e (unchanged since v0.4.3) |
| analyze.py | 62324d6d5c6293c2 (unchanged) |
| pipeline.py | bc409da02b73fa9f (unchanged) |
| make_prompts.py | 739ea744914f9237 (unchanged) |
| sim_power.py | dd9eb28c54889fde (unchanged) |
| sim_power_results.json | 11fb624153b742b4 (unchanged) |
| validate_measure.py | 7253e08b8dc1cd02 (unchanged) |
| run.yml | ad4f416889e61311 (unchanged) |

**Listed for gate G1.** These are declared limitations. No further review cycle is opened (Décisions tab). Proposal for each: keep it.

- **R2a.** In an untitled text, a first line ending with ? or ! is taken for a title. This is unlikely, because the prompt asks for a title.
- **Free-opener requests (V2, rest).** A request for clarification that starts otherwise ("Pour écrire ce texte, pourriez-vous préciser...", "Excusez-moi...") is kept, not excluded.
  - In reading 8's cases, 7 of 21 requests are kept and 5 of those are flagged.
  - Flagged answers leave in the sensitivity analysis, and their rate by label is reported.
- **Openings close to a refusal (W5 and reading 8's cases).** Genuine openings are excluded as refusals in 8 of the 16 constructed cases, for example "Malheureusement, il n'y a pas...", "Navré, le renard...", "Je ne suis pas sûre..." and "Pouvez-vous expliquer pourquoi...".
  - An untitled "Voici..." paragraph that names the intended readers is removed whole.
  - These cases are rare and as likely under every label (inference). Each text is requested once more and costs a pair only if the second answer is excluded too. The exclusion rate by label is reported.
- **Lines addressed to the pupil (W3, W4 rest).**
  - A closing "Dis-moi, quel est ton animal préféré ?" is removed and flagged.
  - A closing note about the subject is removed when it contains niveau, histoire, mots, phrases, lecture or élèves.
  - The cost is one line at most.
- **Refusal without punctuation (V4, rest).** A refusal on a first line without punctuation, followed by at least 20 words, is kept as a title. This is rare.
- **Openings in tu close to a request (X4).**
  - A genuine opening written with the new tu phrases is excluded as a refusal, for example "Peux-tu indiquer sur la carte..." or "Dis-moi ce que tu vois...". This happened in 18 of 18 of reading 8's constructed openings, 8 of them plausible by its judgement.
  - With v0.4.4, genuine hooks with "à quelle", "quelles" or "quels" ("Dis-moi à quelle heure...") are excluded too, 3 of 3 in reading 8's fourth round, as in v0.4.2.
  - An excluded text is requested once more, so the cost is mostly one more call.
  - The reader's option, not applied: use these phrases only for answers under about 60 words.
- **Label and question in different sentences (X5).**
  - A clarification whose label and question mark sit in different sentences is no longer flagged (0 of 6 of reading 8's cases), nor is a lower-case "5h".
  - A label, a singular "degré", "8H" or "HarmoS" in the question's own sentence is still flagged.
  - None of reading 8's 12 clarifications lost its flag. The flag only feeds the sensitivity analysis.
- **Provider without usage (reading 8).** A provider that never sent token counts would make every call a failed record counted at its worst case, so the plan budget would be spent without data. This would show at the first pilot run.
- **Outside stop (W1, rest).** Calls in flight when the job is cancelled from outside are not counted: at most the reservations in flight, about 0.4 USD at the test prices. The provider console caps remain a second barrier.

## v0.4.3 (20:47 to 20:53, reading of the fixes 20:51 to 21:06)

**Why.** Reading 8 checked v0.4.2 and found X1 to X3, listed under v0.4.2. Two are gaps in the generate.py fix. The third is a regex defect that v0.4.2 introduced.

**Changes.**

- `generate.py`.
  - `parse()` returns None for a token count the provider did not send. An answer without usage, or with an empty one, is then a failed record counted at the worst case of its model.
  - A lone surrogate in the model id or the finish reason is replaced, as in the text (helper `utf8()`).
- `compute.py`.
  - A word boundary follows the alternatives of "dis-moi (...)", "tu veux dire (...)" and "(pourrais|peux)-tu (me |m')(donner|expliquer|dire (...))".
  - The self-test has 2 more kept texts ("Dis-moi quelque chose...", "Peux-tu me dire quelque chose..."). Both fail on v0.4.2.
- `design.json`, `README.md`, `PREREG.md`. Version line.
- `checks/`.
  - `mock_weird.py` has four more shapes: usage missing, usage empty, a surrogate in the model id, a surrogate in the finish reason.
  - `e2e_malformed.py` checks the worst-case count and runs compute.py after the surrogate shapes.
  - Two more mutations.

**Checks.** Run on a copy of v0.4.3. The outputs are in `checks/history/v0.4.3_run/`.

- All 10 checks passed.
- Mutations: 57 of 57 caught.
- Battery and clarification cases: as in v0.4.2.
- Malformed answers: 28 of 28 runs pass. On v0.4.2, 8 of 28 fail: missing usage counted at 0, a surrogate stops compute.py. That output is `checks/outputs/failure_controls/e2e_malformed_on_v0.4.2.txt`.
- Cut responses: 0.7584 USD counted for a budget of 0.8.
- The two new kept texts fail on v0.4.2.

**Reading.** Reading 8 confirmed the three fixes:

- **X1.** An answer without usage, with an empty usage or without an output count becomes a failed record at exactly its reservation (50 runs, 25 shapes, both routes). 32 budget runs without overshoot, and no record above its reservation among 3,029.
- **X2.** A surrogate in the model id or the finish reason becomes "?", and compute.py runs.
- **X3.** "Dis-moi quelque chose" and "Tu veux dire quelque chose ?" are kept, and the 10 tu clarifications are still excluded.
- The battery, the ten answers and its other tables are unchanged.

It found one side effect. The word boundary cut "à quelle", "quels" and "quelles", so 6 of its 10 probe clarifications were only flagged. This is fixed in v0.4.4.

It left two notes for G1:

- A provider that never sends usage would fail every call and spend the budget (2.965 of 3.0 USD in its test). This is theoretical.
- compute.py still stops on raw files written by v0.4.2 or earlier. No such file exists, since no call has been made.

**Hashes.**

| File | Hash |
|---|---|
| compute.py | a24472f501d4e52e |
| generate.py | 7ce38baa5b8f397e |
| design.json | 3efc96516de9c847 |
| PREREG.md | 9cd0b149f4a2b95a |
| README.md | 392ebf141c3b720f |
| analyze.py | 62324d6d5c6293c2 (unchanged) |
| pipeline.py | bc409da02b73fa9f (unchanged) |
| make_prompts.py | 739ea744914f9237 (unchanged) |
| sim_power.py | dd9eb28c54889fde (unchanged) |
| sim_power_results.json | 11fb624153b742b4 (unchanged) |
| validate_measure.py | 7253e08b8dc1cd02 (unchanged) |
| run.yml | ad4f416889e61311 (unchanged) |

**Listed for gate G1.** See v0.4.4.

## v0.4.2 (20:07 to 20:26, reading of the fixes 20:22 to 20:45)

**Why.** Reading 8 read v0.4.1. Its findings W1 to W5 are listed under v0.4.1. Two of them were fixed before the pilot:

- **W1.** It contradicted the v0.4.1 note that no call error stops a run, and could block a run.
- **W2.** It was a regression of the V4 fix.

A request for clarification kept as a text enters the measure, and is more likely under a bare label. A genuine text excluded by mistake is requested once more and loses one pair only if the second answer is excluded too, in the same way under every label (inference).

**Changes.**

- `generate.py`.
  - A 200 answer whose token counts are missing or not numbers, or whose text is not a string, is recorded as failed. Its body is kept under `unreadable_response`, and the attempt is counted at the worst case of its model.
  - A lone surrogate is replaced in the text. A raw line that cannot be encoded is written with ASCII escapes.
  - A finish reason or a model id that is not a string is recorded as null.
- `compute.py`, refusals.
  - "(pourrais|peux)-tu préciser, clarifier, indiquer, confirmer" no longer needs "me". "donner", "expliquer" and "dire (ce que, quel, l'âge...)" still do.
  - "dis-moi quel...", "tu veux dire quel..." and "qu'entends-tu exactement par" are added.
- `compute.py`, flag.
  - A label question is tested sentence by sentence.
  - The grade pattern (5H, 5P) is case-sensitive, so "8 h" is read as a time.
  - "degré" matches only the singular, so "20 degrés" is read as a temperature.
- `compute.py`, self-test. 3 refusals, 2 kept texts and 4 flag cases added.
- `design.json`, `README.md`, `PREREG.md`. Version line, flag wording in the preregistration, new files listed in the README.
- New files: `checks/` (every check, portable, with `run_all.sh` and the failure controls), `history/` and this changelog.

**Checks.** Outputs are in `checks/outputs/`, with the hashes of the files tested in `tested_versions.txt`.

- Self-tests: `OK`.
- Mutations: 55 of 55 caught in compute.py, the 6 new ones each failing on the case they target; 22 of 22 in analyze.py.
- Battery:
  - 33 plausible answers without a problem;
  - 16 edge answers with 3 genuine lines removed and 3 flags;
  - the 10 answers of reading 8 with 4 genuine lines removed and 1 flag, against 3 flags in v0.4.1.
- Clarification cases:
  - 14 of 21 requests are excluded, against 6 in v0.4.1 and 10 in v0.4;
  - 8 of 16 genuine texts are excluded, the same cases as in v0.4.1.
- Malformed answers: 20 of 20 runs complete, against 5 stopped in v0.4.1.
- Cut responses, the full offline pilot and the call files all pass.
- `history/` rebuilds every kept version.

Every failure control was run and failed as expected. The outputs are in `checks/outputs/failure_controls/`.

**Reading.** v0.4.2 was sent back to reading 8 for W1, W2 and W4 only, as a read-only copy without the main session's results. Reading 8 confirmed the three fixes:

- **W1.** 46 runs over 22 malformed shapes without a stop. 32 budget runs without overshoot, the closest at 1.193 USD of 1.2. No raw record above its reservation among 3,047.
- **W2.** 10 of 10 tu requests excluded, against 2 of 10 in v0.4.1. Its 16 genuine texts unchanged.
- **W4.** The 6 false flags gone. 1 of its 10 answers wrongly flagged instead of 3.

It also found five problems:

- **X1.** An answer without usage, or with an empty one, is counted at 0 USD.
- **X2.** A lone surrogate in the model id or the finish reason stops compute.py at the CSV write.
- **X3.** No word boundary after "quel", so "Dis-moi quelque chose" is excluded.
- **X4.** 18 genuine openings written with the new phrases are excluded, 8 of them plausible by its judgement.
- **X5.** A clarification with the label and the question mark in different sentences is no longer flagged.

X1 to X3 are fixed in v0.4.3. X4 and X5 are listed for G1.

**Hashes.**

| File | Hash |
|---|---|
| compute.py | 1f5742c8c36b24a8 |
| generate.py | 4680bda30be1d520 |
| design.json | 81164e40c216979a |
| PREREG.md | 05aa7cc9ba3567ff |
| README.md | 4f69be7594094ca2 |
| analyze.py | 62324d6d5c6293c2 (unchanged) |
| pipeline.py | bc409da02b73fa9f (unchanged) |
| make_prompts.py | 739ea744914f9237 (unchanged) |
| sim_power.py | dd9eb28c54889fde (unchanged) |
| sim_power_results.json | 11fb624153b742b4 (unchanged) |
| validate_measure.py | 7253e08b8dc1cd02 (unchanged) |
| run.yml | ad4f416889e61311 (unchanged) |

**Listed for gate G1.** See v0.4.3.

## v0.4.1 (19:01 to 19:40)

**Why.** Reading 7 (claude-sonnet-5-5, 18:28 to 18:59) read v0.4. It confirmed D1 to D4 and R1, D5 as described, and R2b in part. It found five new problems, not put to a refutation round:

- **V1 (medium).** A run that crashes writes no log, so its spend is not counted. A response cut in the middle of its body (IncompleteRead) crashes generate.py. On the mock API, two runs with a 0.8 USD budget spent 1.30 USD.
- **V2.** Requests for clarification with an unlisted opener are kept as texts. Forms in tu are never flagged.
- **V3.** A "---" line after a preface becomes the title and blocks the removal of closing lines.
- **V4.** Rare genuine lines are read as refusals ("Qu'entends-tu...", "Peux-tu dire...", "Malheureusement, j'ai...").
- **V5.** "Voici Tom, un élève de CM1..." is removed, and so is any closing line that starts with "Note".

**Changes.**

- `pipeline.py`. The spend of a plan is counted from the raw records by call_id prefix (pilot-, main-), so a run killed before it writes its log is still counted.
- `generate.py`. Every call error is caught. An attempt that may have been billed (sent, then cut, timed out or unreadable) is counted at the worst case of its model and is not retried within the call; the next pass asks again.
  - A first version retried within the call. In one test it counted 0.8269 USD against a 0.8 USD budget. It was replaced before the reading ended (81bc955a4b877bf0).
- `compute.py`, cleaning.
  - Lines without letters are removed.
  - "Voici" is removed only before "une histoire", "un texte" or the intended readers.
  - A closing note is removed only when it is about the text.
  - A word count and "Dites-moi" are removed.
- `compute.py`, refusals.
  - "Navré" is added.
  - Forms in tu need "me" or "m'", and "qu'entends-tu" needs "par".
  - "Malheureusement" counts only when followed by "je ne" or "j'ignore".
- `compute.py`, flag. It now also covers requests in tu, need-to-know sentences, and questions that name the grade label or the school system.

**Checks.**

- `compute.py --self-test`: 29 checks.
- Mutations: 49 of 49 caught in `compute.py`, 22 of 22 in `analyze.py`.
- Battery of 49 answers written by reading 7: 33 plausible answers with no problem; 16 edge answers with 3 genuine lines removed and 3 flags.
- Cut responses: 6 runs under the 0.8 USD budget, at most 0.7760 USD counted.
- The full offline pilot runs.
- Call files are identical to v0.3.

**Decision.** The fixes were applied without a separate refutation round, which departs from the rule "reading, then refutation". The departure is recorded in the Décisions tab.

**Reading.** Reading 8 (claude-sonnet-5-5, 19:22 to 20:02). The final budget fix holds: 0 overshoots in 39 runs, 39 of 39 runs without a crash, no record above its reservation. V3 and V4 are confirmed, V2 and V5 in part. Reading 8 found:

- **W1 (medium).** Three malformed 200 answers still stop the run with no log (null token counts, a number as content, a lone surrogate). Calls in flight when a run is killed (about 0.4 USD) are not counted.
- **W2.** Since the V4 fix, requests for clarification in tu without "me" are kept as texts.
- **W3.** The Note filter removes a subject note that contains a trigger word.
- **W4.** False flags: "degré", "8 h" or "5H" next to a question mark, and "Peux-tu me dire" or "Dis-moi" in a text.
- **W5 (rare).** An untitled "Voici..." paragraph is dropped. Doc lines starting with "Malheureusement, il n'y a pas..." or "Navré, le..." are excluded.

**Hashes.**

| File | Hash |
|---|---|
| compute.py | 1412a470efc44b92 |
| generate.py | 81bc955a4b877bf0 |
| pipeline.py | bc409da02b73fa9f |
| design.json | 26b8c5f8b45c1de5 |
| PREREG.md | 1229bde13d47e9c2 |
| README.md | 97301c5cc2dca008 |
| analyze.py | 62324d6d5c6293c2 (unchanged) |
| make_prompts.py | 739ea744914f9237 (unchanged) |
| sim_power.py | dd9eb28c54889fde (unchanged) |
| run.yml | ad4f416889e61311 (unchanged) |

## v0.4 (17:47 to 18:25)

**Why.** Reading 5 (claude-sonnet-5-5, 17:16 to 17:44) read v0.3. It confirmed 12 fixes and N9 in part, and found:

- **D1.** REFUSAL_RE misses reworded refusals ("Merci...", "Malheureusement"). It tests the raw start of the answer, title included, so titles such as "Je ne peux pas dormir" are excluded.
- **D2.** Ligatures are folded in the texts but not in the lexicon keys.
- **D3.** The title mark is read before label lines are removed.
- **D4.** "tout", "autre" and "même" are counted as content words.
- **D5.** Each pass of a step gets the whole budget, so a step can spend up to three times `--max-cost`.
- **R1.** A spaced hyphen does not open a reply.
- **R2a.** A first line ending with ? or ! is taken for a title.
- **R2b.** A preface without a colon is kept.

Reading 6 (claude-sonnet-5-5, 17:46 to 18:02) tried to refute them. D1 to D5 stand at least in part. R1 was refuted for the example given and stands mid-sentence. R2 stands but is unlikely.

**Changes.**

- `compute.py`, measure. "tout", "autre" and "même" are excluded, and lexicon keys are folded like the texts.
- `compute.py`, cleaning.
  - Up to two preface lines and three closing lines addressed to the user are removed and counted.
  - A spaced hyphen counts as a dialogue dash.
  - The title mark is kept line by line.
- `compute.py`, refusals. Precise phrases are matched at the start of the first two lines, after an optional polite opener. A title-like first line is skipped only when at least 20 words follow it.
- `compute.py`, flag. Answers addressing the user are kept, flagged (flag_meta) and removed in a sensitivity analysis.
- `pipeline.py`. `--max-cost` becomes the budget of the whole plan, earlier runs included.
- `analyze.py`. Sensitivity analysis without the flagged answers, and counts by label.
- R2a is kept as a declared limitation.

**Checks.**

- `compute.py --self-test`: 24 checks; 36 of 36 mutations caught.
- `analyze.py --self-test`: 36 checks; 22 of 22 mutations caught.
- Offline run with the plan budget passes.
- Call files are identical to v0.3.

**Decision.** End of the review cycles of the design. After the reading of v0.4, remaining minor findings are listed for gate G1 instead of opening a new cycle.

**Hashes.**

| File | Hash |
|---|---|
| compute.py | e1e954d16b3ee183 |
| analyze.py | 62324d6d5c6293c2 |
| pipeline.py | 617ca1b71f23d98e |
| generate.py | c5fdb28bd5ee8642 (unchanged since v0.2) |
| design.json | 728781d1921b7172 |
| make_prompts.py | 739ea744914f9237 |
| sim_power.py | dd9eb28c54889fde (docstring only) |
| PREREG.md | c52786735a774c46 |
| run.yml | ad4f416889e61311 |

## v0.3 (16:50 to 17:15)

**Why.** Reading 3 (claude-fable-5-1, 16:34 to 16:49) read v0.2. It confirmed the statistical fixes and found 13 problems, four of them blocking:

- **N1.** Determiners and numerals are counted as content words. The main session's mutation test found this independently.
- **N2.** The ligatures œ and æ fall outside the lexicon.
- **N3.** "suis" is read as suivre.
- **N4.** A capitalised word after a colon or a quote is counted as a name.
- **N5.** 24 topics are listed for a rule that allows 32, and the plan truncates silently.
- **N6.** The pilot slope is too imprecise to set the number of topics.
- **N7.** validate_measure.py does not call clean().
- **N8.** The pilot is blinded only in the code.
- **N9.** Textual refusals are kept.
- **N10.** The analysis block of design.json is stale.
- **N11.** Transport failures are not asked again within the step.
- **N12.** The first sentence of an untitled text is removed, and a preface is taken for the title.
- **N13.** The docstring is stale and there is no collection window.

Reading 4 (claude-sonnet-5-5, 16:51 to 17:08) refuted none of them.

**Changes.**

- `compute.py`, measure.
  - The full Lexique tag is used, so determiners and numerals are excluded.
  - Ligatures are written oe and ae.
  - Each form is read by its most frequent lemma.
  - Initial position applies after a colon, a quote or a dash.
- `compute.py`, cleaning. A title has no final period. Preface and label lines are removed.
- `compute.py`, refusals. Refusals are matched by a list of phrases.
- `design.json` and `make_prompts.py`. 32 topics are listed, and make_prompts.py stops when the plan asks for more.
- Pilot. 216 age-only texts and 36 probes, with no L1 or L1P text before the preregistration is deposited.
- Sample size. The smallest effect of interest is 0.04 Zipf. The number of topics is set from the pilot σ taken at its 80 % bound.
- `pipeline.py`. A second pass asks again for failed calls.

**Checks.**

- `compute.py --self-test`: 11 golden texts; 21 of 22 mutations caught. The surviving clitic mutation is equivalent for the primary measure.
- `analyze.py`: 22 of 22 mutations caught.
- Plan counts and duplicate check pass. The full offline run passes.
- Simulation: C1 0.0435 and C2 0.0375 under the bound 0.0613; C3, the text-level analysis that must fail, 0.139.

**Hashes.**

| File | Hash |
|---|---|
| compute.py | 3784219d79611dfa |
| analyze.py | 6856342ef25b72ad |
| design.json | 45c2d282b0d7e759 |
| make_prompts.py | 123e1693dea22dbe |
| pipeline.py | 230bf9ed977f7a59 |
| generate.py | c5fdb28bd5ee8642 |
| sim_power.py | a437fa94609e2541 |
| run.yml | 0bbc724fba52ea80 |
| PREREG.md | d35f613a749ff8c2 |
| validate_measure.py | 7253e08b8dc1cd02 |

## v0.2 (about 16:00 to 16:30)

**Why.** Reading 1 (claude-fable-5-1, 15:21 to 15:34) read the design dossier v0.1 and found 24 problems, A1 to G24. Seven were blocking:

- the measure: apostrophes, names, inversions, word class, form frequencies;
- the dependence between texts of one prompt;
- a pilot too small to set the sample.

Reading 2 (claude-sonnet-5-5, 15:37 to 16:02) refuted none of them; C11 and D15 stand only in part. Its reading of C11 led to the H3 test of grade tracking.

**Changes.**

- Design: one text per prompt, with topics as the unit of inference.
- Tests: level and gradient tests, with Holm over four tests.
- Labels: L0, L1P and L6 added.
- Sampling: temperature fixed at 1.0.
- Answers: the probe parser and the refusal rule are defined.
- Measure: computed on lemmas.
- Age readings: specific to each model.
- Simulation: includes a control that must fail.

**Hashes.**

| File | Hash |
|---|---|
| compute.py | d52ba4de15177c65 |
| analyze.py | 6856342ef25b72ad |
| sim_power.py | a437fa94609e2541 |
| sim_power_results.json | 11fb624153b742b4 (unchanged since) |
| generate.py | c5fdb28bd5ee8642 |
| pipeline.py | c35ca266baab8014 |
| make_prompts.py | de5649da860e0910 |
| design.json | 31d5ce9ebdc900f5 |
| PREREG.md | dd58d209f986d52a |
| validate_measure.py | 975a8d558b9887b0 |
| run.yml | 0bbc724fba52ea80 |

README.md and requirements.txt of v0.2 were not kept.

## v0.1 (about 15:10)

First design:

- six models from three providers and several grade labels;
- mean Zipf frequency of content words, prototype `measures.py`;
- a power simulation and two texts per cell.

Only `measures.py` (d94368ea49681d3c) was kept. The other v0.1 files were overwritten by v0.2. Their hashes are in the Contrôles tab of the journal:

| File | Hash |
|---|---|
| sim_power.py | c1650f9a1e34bd11 |
| analyze.py | 375b53ec9e33e901 |
| make_prompts.py | d4c56457dfa3538d |
| design.json | a5405b05ff710259 |
| generate.py | 125c5e14e9b86441 |

## Records

**Check scripts.** In `checks/`. `bash checks/run_all.sh` reruns them all on any version.

**Outputs.** The last run's outputs are in `checks/outputs/`, with the hashes of the files tested. The outputs of the earlier runs quoted in the journal are in `checks/history/`.

**Earlier code versions.** Kept as diffs in `history/`.

**Readers' working folders.** The scripts the readers wrote, and the text outputs at the top of reading 8's work folder, are bundled in `claude/art5/records/reader_scripts_bundle.txt` of the Claude project. Until the repository exists, `checks/` and `history/` themselves, with all their outputs, are bundled in `claude/art5/records/repo_additions_bundle.txt`. Unpack either with `python checks/bundle.py unpack BUNDLE DEST`, which checks each file's SHA-256. The readers' run folders and copies of the code were not kept.

**Power simulation.** `sim_power_results.json` was produced at 16:32 by sim_power.py a437fa94609e2541 with analyze.py 6856342ef25b72ad. It was rerun from 20:00 to 20:03 on v0.4.1 and gave a byte-identical file (11fb624153b742b4). analyze.py and sim_power.py are unchanged since that rerun, through v0.4.4. The changes since 16:32 do not touch the functions the simulation calls.
