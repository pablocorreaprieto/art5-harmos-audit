# ART 5, verification report (phase P6) and exception list for gate G2

Main session (claude-opus-5-5), 1 November 2026, updated after the internal readings of the draft (phase P7).
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
  On its first run the check caught a quantity left uncovered after a rewording of the practitioner notes.
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
  `check_citations`; RERUN PENDING on the revised commit.

## 4. References (P6.1, P6.2)

- `checks/check_citations.py`: every in-text citation is the citation string of a reference, every cited reference
  was read in full or is listed below as an exception, no marker left. PASS (24 references cited); planted orphan
  parenthetical citation, orphan narrative citation and abstract-only reference: each FAIL.
- `checks/verify_refs.py` in GitHub Actions (Crossref, OpenAlex, arXiv), run 41302064405 on 46b2152: the
  references with a DOI or an arXiv id matched, except the year of Brysbaert et al. (online 2017, issue 2018), now
  marked online first. RERUN PENDING with the four references added after P7 (Javourey-Drevet et al., 2022;
  Sclar et al., 2024; Yan et al., 2024; État de Vaud, 2012).
- Sentence-citation pairs: 44 pairs (21 references and 2 secondary citations) checked against the full texts by a
  separate session (claude-sonnet-5-5): 37 support, 7 support in part, 0 do not support, none rests on an abstract.
  The seven partial pairs were reworded (ages of CE2 and CM2 derived, not stated by the ministry page; New et al.,
  2004, describes Lexique 2; "3.83" is not in the manual; the mean of the two frequencies is the study's
  definition; Rooein et al.'s caveat concerns Flesch–Kincaid). The same session read New et al. (2004) in full,
  which removes that exception. The sentences added after P7 cite four sources read by the main session in full
  text (Yan et al. in its arXiv version); they were not part of the 44 pairs and are covered by the confirmation
  reading.

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
   preregistration, decided the open questions at G2, read the final manuscript and take responsibility, and the
   CRediT line lists conceptualization, funding acquisition, project administration, supervision, and writing –
   review and editing. Remove any item that is not exactly what you did (for example "writing – review and
   editing" if you only read the text).
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
    references), double-anonymous review and practitioner notes come from secondary copies. Main text after
    revision: about 5,100 words without tables and captions, abstract about 250 words. Check the counting rule on
    the portal.
11. Lexique 4 appeared in 2026; the study uses Lexique 3.83, fixed in the preregistration. A reviewer may ask.
12. Analyses added after the readings are labelled post hoc in the text and listed in Supporting Information S1;
    none changes a preregistered result.
