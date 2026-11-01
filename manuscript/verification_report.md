# ART 5, verification report (phase P6) and exception list for gate G2

Main session (claude-opus-5-5), 1 November 2026, updated after the internal readings of the draft (phase P7) and
after the readings that confirmed their corrections (claude-fable-5-1, 13:46 to 14:16; claude-sonnet-5-5, 14:37 to 15:11
and 15:19 to 15:38).
Every check below can fail and was seen to fail on a planted fault; each line names the program and the
output kept in the repository. The readings, their refutations and the corrections are recorded in
`manuscript/records/p7/` and in the "Relectures IA" tab of the project journal.

## 1. Numbers of the manuscript (P6.3)

- `checks/check_numbers.py`: every digit of `manuscript/manuscript.md` and `supplement.md` is a placeholder of
  `results/manuscript_numbers.json` (from `results/numbers.json`, `results/exploratory.json`,
  `results/exploratory_p7.json`, `sim_power_results.json` and the other archived outputs), of
  `manuscript/source_facts.json` (numbers taken from cited sources, with the passage) or of
  `manuscript/process_facts.json`, or one of the structural tokens listed with their reason in the script; quoted
  French wordings occur in the prompts sent; the rendered text and the .docx carry the same numbers as the render
  of the source. PASS on the revised text. Planted faults, each FAIL: a number typed in the source, a digit
  changed in the rendered copy, a value changed in `manuscript_numbers.json`, « de 8 à 10 ans », a digit changed
  in the .docx. The exemption "just below 1" was removed with the sentence it covered (finding S4 of R2).
- `checks/check_claims.py` (new, finding m14 of R2): every quantity written in words ("about two years", "within a
  year", "about half") lies inside a listed claim whose condition holds on the numbers; an unlisted quantity or a
  listed claim no longer in the text fails. PASS; planted fault (Claude Haiku 5.5's shift set to 3.1 years): FAIL.
  On its first run the check caught a quantity left uncovered after a rewording of the practitioner notes. After the
  confirmation reading, entries were added for the wordings it corrected ("every model's point estimate", "the two
  whose texts followed the grade least", the effect of the region by model, "as low as with the bare P label"); after
  the second confirmation reading, the region's effect is tied to the pooled value over the six models, with the two
  models near zero named.
- `checks/recompute_primary.py`: the four primary tests recomputed without `analyze.py` from `results/measures.csv`,
  20 values within 1e-9 of `numbers.json`. PASS; planted +0.05 Zipf on one text: FAIL.
- `exploratory_p7.py` (post hoc analyses) stops if its vectorised readings, its leave-one-model-out function at
  six models, its L3 − L1 contrast or its offsets do not reproduce the frozen values of `numbers.json`.

## 2. Reproducibility (P6.4)

- GitHub Actions, commit 87b16d3 (code identical to tag `prereg`, data of tag `data-v1`): step compute (run
  41298958403) and step analyze (run 41299102557) produced no commit, so `measures.csv`, `probes.csv` and
  `numbers.json` were recomputed byte for byte from the raw outputs and the official lexicon.
- Failure control, outside GitHub (Python 3.13, numpy 2.5.3): `numbers.json` differs in six numbers of
  `secondary_ols_clustered` at the 16th significant digit; with the Latin-1 copy of Lexique 3.83 shipped in the
  pylexique package, 729 texts get other values. They are exactly the texts that contain *vrai* or *faux*, which
  that copy lists only in capitals (VRAI, FAUX); the earlier statement here that words with « œ » were lost was
  wrong (found by the refutation of R1 and checked by the main session: 729 of 729 differing texts contain one of
  the two words, 2 of 731 such texts do not differ). The comparison can fail, and the official lexicon matters.
- Figures: `figures.py` writes byte-identical PDFs on a rerun (no creation date).

## 3. Full check suite (P1 checks rerun on the official lexicon)

- `checks/run_all.sh` in GitHub Actions (workflow `checks`, task run-all, run 41300583934 on 8573ef5, outputs at
  b710cd3): 14 of 14 PASS. The suite now also runs `check_claims` (with its planted fault) and
  `check_citations`. Rerun on the revised commit 2029f0f (run 41317370806, outputs at d5585dd,
  `checks/outputs/run_all_stdout.txt`): 17 of 17 PASS, ALL CHECKS PASSED, on the official lexicon (SHA-256
  637ba37a767a6667).

## 3b. Anonymised copy for review (P8)

- `manuscript/make_anonymous_bundle.py` stopped on commit 49e8ae4 (found by the confirmation reading): a script written
  by a reading session (`manuscript/records/p7/reader_scripts/refute_r2r3/bundle_sim.py`) holds the author's names in
  lower case, which the case-sensitive replacements missed, and the rendered title page and cover letter
  (`manuscript/build/*.docx`), binary files that the text scan skipped, name the author. Fixed: the reading sessions'
  scripts that search for identifying strings and the rendered title page and cover letter are left out, the name
  replacements ignore case, and binary files (inside .docx containers, else as raw bytes) are scanned too. The earlier
  dry run that found the copy clean had been made before these files were committed. Run on the corrected tree:
  exit 0, 338 files, nothing left by the script's own list or by a broader list (names, ORCID, university, e-mail
  domains, place of residence, AsPredicted number, links to private documents). The second confirmation reading ran it
  on 34545cc (exit 0), scanned the 331 text files, both .docx, the PDFs and the PNGs itself and found nothing
  identifying, and checked that a name planted in a .docx or a binary file stops the script. Its own scan script is
  left out like the others (pattern widened to `scan_bundle*.py`). Run on the merged and pushed commit f5c82c2
  (the commit after it changes only this report, which the copy leaves out, and the changelog): exit 0, 396 files,
  nothing left by the script's own list or by the broader list.

## 4. References (P6.1, P6.2)

- `checks/check_citations.py`: every in-text citation is the citation string of a reference, every cited reference
  was read in full or is listed below as an exception, no marker left. PASS (24 references cited); planted orphan
  parenthetical citation, orphan narrative citation and abstract-only reference: each FAIL.
- `checks/verify_refs.py` in GitHub Actions (Crossref, OpenAlex, arXiv), run 41302064405 on 46b2152: the
  references with a DOI or an arXiv id matched, except the year of Brysbaert et al. (online 2017, issue 2018), now
  marked online first. Rerun with the references added after P7 (run 41317380753, outputs at f5c82c2,
  `checks/outputs/verify_refs.txt`): PASS, the 14 references with a DOI or an arXiv id match their registry
  (title, year, first author, no notice; Crossref gives Applied Psycholinguistics 43(2), 485-512 for
  Javourey-Drevet et al. and BJET 55(1), 90-112 for Yan et al.), and the 11 web pages are marked as opened by the
  session.
- Sentence-citation pairs: 44 pairs (21 references and 2 secondary citations) checked against the full texts by a
  separate session (claude-sonnet-5-5): 37 support, 7 support in part, 0 do not support, none rests on an abstract.
  The seven partial pairs were reworded (ages of CE2 and CM2 derived, not stated by the ministry page; New et al.,
  2004, describes Lexique 2; "3.83" is not in the manual; the mean of the two frequencies is the study's
  definition; Rooein et al.'s caveat concerns Flesch–Kincaid). The same session read New et al. (2004) in full,
  which removes that exception. The sentences added after P7 cite four sources read by the main session in full
  text (Yan et al. in its arXiv version); they were not part of the 44 pairs. The confirmation reading read them and found each sentence supported
  (Javourey-Drevet et al. through the journal page and PDF, Sclar et al. v2, Yan et al. arXiv v2 p. 16, the État de
  Vaud press release of 4 April 2012, the ministry page). It also noted that Sclar et al. is an ICLR 2024 conference
  paper and that Javourey-Drevet et al. appeared in issue 2; both entries were corrected.

## 5. Novelty (P6.5)

- The only priority sentence is bounded by the searches logged in `manuscript/literature/search_log.md`: "The
  searches logged for this study, in English and French, found no earlier study of how language models read Swiss
  school grade labels". It was narrowed from "Swiss or other non-US labels" after R1 (Ripoll y Schmitz &
  Sonnleitner prompted for a Luxembourg grade), and the names of the search tools moved to the AI statement and the
  log (R3). No phrase of the list to avoid (protocol, annex E: first study, no prior work, verified, independently
  reviewed) occurs in the text.

## 6. Exceptions and decisions for gate G2

1. Title and keywords are proposals (title: "Swiss grade labels and the lexical demand of French reading texts
   written by large language models: A preregistered audit"); change them if you wish.
2. Conflicts of interest: the text says you have no employment, consulting, shareholding or other financial
   relationship with Anthropic, OpenAI or Mistral AI. Only you can confirm this.
3. Funding: the Anthropic calls (25.44 USD of 41.12) were paid from your Anthropic API credit, which before the run
   was 206.87 USD, of which 201.87 promotional (CHANGELOG, Deposit). Which credit Anthropic drew first is not
   recorded; at least 20.44 USD of the 25.44 were promotional whatever the order. Confirm the wording, and say
   where the promotional credit came from if you know.
4. Use of generative AI and CRediT: the statement says you set the aims of the study, approved the design and the
   preregistration, decided the questions left open at submission, read the final manuscript and take full
   responsibility, and the CRediT line lists conceptualization, funding acquisition, project administration,
   supervision, and writing – review and editing. Two of these ("decided the questions left open at submission",
   "read the final manuscript") become true only when you do them at G2, so the manuscript must not be submitted
   before; "writing – review and editing" is true only if you review or edit the text. Remove any item that is not
   exactly what you did. The statement's "log of each finding" is `manuscript/records/findings_log.csv`, a copy of
   the "Relectures IA" tab made on 1.11.2026.
5. Title page: affiliation and e-mail to fill in (AUTHOR INPUT); ORCID 0009-0009-1844-7453.
6. The repository is to be made public at submission, as the preregistration says (your action, or mine with your
   explicit OK). Reviewers get the anonymised copy (`manuscript/make_anonymous_bundle.py`), which now includes the
   protocol and the review records, with names, ORCID, e-mail addresses and links to private documents replaced.
7. AsPredicted: the deposited text contains the repository address with your GitHub user name, which the anonymous
   AsPredicted PDF would show. Give the editor the AsPredicted link (title page); reviewers read the preregistration
   in the anonymised repository copy. Download the AsPredicted PDF into the repository if you want it archived.
8. Li et al. (2024), the journal's closest precedent, is closed access and was read as an abstract only; it is not
   cited, and the cover letter now refers to Yan et al. (2024) instead. Reading it through a library would allow
   citing it.
9. Mesmer (2024), the closest study of mean word frequency in primary reading texts, was read as an abstract only and
   is not cited.
10. BJET's own author guidelines could not be opened (Wiley pages blocked); the word limit (6,000 words excluding
    references), double-anonymous review and practitioner notes come from secondary copies. Counts by one rule, the
    one `manuscript/render.py` prints and the title page uses (runs of non-space characters, as a word processor
    counts, headings included): main text from the Introduction to the Conclusion 5,242 words, 5,826 with tables and
    captions; abstract 237 (the paragraph, without the keywords); everything from the Abstract through the Statements,
    the references excluded, 6,800. Check the
    counting rule on the portal. If it counts everything except the references, about 800 words must go: move the
    sensitivity paragraph and Table 3 to the Supporting Information (274 words), shorten the background on lexical
    demand by half (about 115 of 230), keep only the key sentences of the per-model paragraph of the Results (about
    120 of 237), merge the per-model paragraph of the Discussion into the next one (about 80 of 133), shorten the
    paragraph on lexical equivalence (about 60 of 120) and move part of the AI statement to the records README
    (about 150). That is about 800 words; I can do it in one pass if you choose it.
11. Lexique 4 appeared in 2026; the study uses Lexique 3.83, fixed in the preregistration. A reviewer may ask.
12. Analyses added after the readings are labelled post hoc in the text and listed in Supporting Information S1;
    none changes a preregistered result.
13. API keys in the repository history: commit 9e03e53 (31.10.2026, the log of a list-models run) wrote the
    OpenAI and Mistral keys of that day into `logs/models_2026-10-31.json`; commit 9805078 removed them, and the
    current files hold no key (checked 1.11.2026 with a pattern search that prints file names only). You revoked
    those keys after the run, and both consoles showed them as revoked or removed (CHANGELOG, Deposit), so the
    history holds only dead values; for information before the repository is made public. Rewriting the history
    would change commits cited in the preregistration and the records, so I recommend leaving it.
14. Yan et al. (2024) was read in its arXiv version 2 of 22 July 2023, because the published PDF in BJET could not be
    opened (Wiley blocked); the manuscript and the cover letter cite the published article. If you can open it,
    check that the recommendation cited (p. 16 of the preprint: report at least the exact models, prompts and
    temperature) is in the published version.

## 7. Decisions taken at gate G2 (1.11.2026, 18:58 to 19:52)

The author read the final manuscript and answered the items of section 6 in five rounds of multiple-choice
questions. Item by item:

1. Title and keywords kept.
2. Conflicts of interest confirmed as written.
3. Funding: the author first answered that the promotional credit came from his Claude Max plan, to a question
   of the main session that quoted an Anthropic e-mail of 17.10.2026 (a 200 USD grant for the organisation linked
   to the Max plan). The check reading of the evening found that this grant expired on 31.10.2026, before the
   main run. The console (Billing, read at about 21:00) shows two promotional grants, 100 USD of 28.10.2026 and
   103.29 USD of 29.10.2026, and the 26.86 USD drawn from the first equals the pilot plus the main run; it does
   not say where these grants come from. Competing interests, Funding and Limitations therefore say "promotional
   credits that Anthropic granted to the author's API account", with the source in
   `manuscript/process_facts.json`; the author is asked whether he knows the origin of the two grants.
4. Use of generative AI: disclosed in full. The statement now also states the author's part, as he gave it and
   as the records show (topic, the main rules of the protocol, infrastructure, design decisions, approval of the
   design, the preregistration and its deposit, final read), says that the assistant did most of the research
   work, and how its work was checked. CRediT: methodology and resources added, writing – review and editing
   kept (critical read of the final manuscript), and a sentence gives the other roles to the assistant. The
   author reads the passages changed after his read before submitting.
5. Title page: "Independent researcher, canton of Vaud, Switzerland"; pabcorpri@gmail.com.
6. Repository: made public at submission by the main session, on the author's go given at G2.
7. AsPredicted: made public by the author at submission; its link goes on the title page for the editor.
8.–9. Li et al. (BJET 56(3), 2025) and Mesmer (2024): reachable only through the author's UNIR login; not cited.
10. Word count: no longer binding, the target journal changed (below).
11.–13. As listed (Lexique 3.83 fixed by the preregistration; post hoc analyses labelled; revoked keys left in
    the history).
14. Yan et al. (2024): the published version is open access; the recommendation cited ("at least report the exact
    models, prompts, and model temperature") is in its Discussion, section Implications. Closed.

Journal. BJET and JCAL were judged too selective for the author's goal (a first publication, fast). L1-ESLL was
set aside after its own page showed a 95% rejection rate in 2025, and the Swiss Journal of Educational Research is
kept for another article. Three separate research sessions (claude-sonnet-5-5) and the main session then built a
ladder of five journals, submitted one at a time (records in `manuscript/records/g2/`): Education and Information Technologies (Springer), Education in
the Knowledge Society, Computers in the Schools, Reading Psychology, Research in Learning Technology (Drive
document "📮 Échelle de revues ART 5"). The manuscript is formatted for the first (commit f710101): practitioner
notes removed, the AI use also documented in the Methods, heading "Statements and Declarations", abstract 237 words
(limit 150 to 250), six keywords (limit 4 to 6). No preprint. Submission planned on 2.11.2026.

Check reading of the G2 changes (claude-sonnet-5-5, about 20:40 to 21:00, report in
`manuscript/records/g2/g2_check_reading.md`): two blocking findings (the AsPredicted link, which the author
gives at submission, and the credit, corrected as in item 3), five to fix and five minor, all applied except
the AsPredicted link. Checks after the fixes: render.py, check_numbers, check_claims (plant FAIL),
check_citations, recompute_primary and history/check_history.sh PASS.
