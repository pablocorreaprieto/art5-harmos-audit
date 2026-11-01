# ART 5, verification report (phase P6) and exception list for gate G2

Main session (claude-opus-5-5), 1 November 2026. Every check below can fail and was seen to fail on a planted
fault; each line names the program, the commit and the output kept in the repository.

## 1. Numbers of the manuscript (P6.3)

- `checks/check_numbers.py`: every digit of `manuscript/manuscript.md` and `supplement.md` is a placeholder of
  `results/manuscript_numbers.json` (from `results/numbers.json` and the other archived outputs), of
  `manuscript/source_facts.json` (numbers taken from cited sources, with page) or of `manuscript/process_facts.json`,
  or one of the structural tokens listed with their reason in the script; quoted French wordings occur in the
  prompts sent; the rendered text and the .docx carry the same numbers as the render of the source.
  PASS on the final text (see section 8). Planted faults, each FAIL: a number typed in the source, a digit changed in
  the rendered copy, a value changed in `manuscript_numbers.json`, « de 8 à 10 ans », a digit changed in the .docx.
- `checks/recompute_primary.py`: the four primary tests recomputed without `analyze.py` from `results/measures.csv`,
  20 values within 1e-9 of `numbers.json`. PASS; planted +0.05 Zipf on one text: FAIL.

## 2. Reproducibility (P6.4)

- GitHub Actions, commit 87b16d3 (code identical to tag `prereg`, data of tag `data-v1`): step compute (run
  41298958403) and step analyze (run 41299102557) produced no commit, so `measures.csv`, `probes.csv` and
  `numbers.json` were recomputed byte for byte from the raw outputs and the official lexicon.
- Failure control, outside GitHub (Python 3.13, numpy 2.5.3): `numbers.json` differs in six numbers of
  `secondary_ols_clustered` at the 16th significant digit; with the Latin-1 copy of Lexique shipped in pylexique,
  729 texts get other values (words with « œ » are lost). The comparison can fail, and the official lexicon matters.
- Figures: `figures.py` writes byte-identical PDFs on a rerun (no creation date).

## 3. Full check suite (P1 checks rerun on the official lexicon)

- `checks/run_all.sh` in GitHub Actions (workflow `checks`, task run-all, run 41300583934 on 8573ef5, outputs at
  b710cd3): 14 of 14 PASS, including 59 of 59 and 22 of 22 code mutations caught, the answer battery, the
  clarification cases, the offline pipeline runs, the secrets check, the version history, `recompute_primary` and
  `check_numbers`.

## 4. References (P6.1)

- `checks/check_citations.py`: every in-text citation is the citation string of a reference, every cited reference
  was read in full or is listed below as an exception, no marker left. PASS; planted orphan parenthetical citation,
  orphan narrative citation and abstract-only reference: each FAIL.
- `checks/verify_refs.py` in GitHub Actions (Crossref, OpenAlex, arXiv): RESULT PENDING.
- Sentence-citation pairs (44 pairs, 21 references and 2 secondary citations), checked against the full texts by a
  separate session: RESULT PENDING.

## 5. Novelty (P6.5)

- The only priority sentence is bounded by the searches logged in `manuscript/literature/search_log.md`
  ("Searches of Consensus, alphaXiv and the web, in English and French, found no earlier study ...; Scite and Elicit
  could not be searched"). No phrase of the list to avoid (protocol, annex E) occurs in the text: CHECK PENDING.

## 6. Exceptions for gate G2 (to read and decide)

1. New et al. (2004) is cited only as the reference of the Lexique database, which its manual (read) asks users to
   cite; its full text could not be opened (HAL bot wall).
2. Conflicts of interest: the draft says "no conflict of interest", to confirm.
3. Funding and API costs: the draft says the OpenAI and Mistral calls were paid by the author and the Anthropic calls
   from API credits attached to the author's account; Anthropic is also the maker of the assistant that ran the
   study. To confirm or reword.
4. Title page: affiliation to choose (independent researcher and primary teacher in Vaud, or the master's programme
   at UNIR), ORCID 0009-0009-1844-7453.
5. The preregistration says the repository is "made public at submission": making it public is your action (or
   mine with your explicit OK). Reviewers get the anonymised copy (`manuscript/make_anonymous_bundle.py`).
6. AsPredicted: an anonymous link to the preregistration for reviewers, created in your account (or by me with your OK).
7. Mesmer (2024), the closest study of mean word frequency in primary reading texts, could only be read as an
   abstract and is not cited; reading it through a library before submission would strengthen the measure section.
8. BJET's own author guidelines could not be opened (Wiley pages blocked); the word limit (6,000 excluding
   references) and the practitioner notes come from secondary sources. To check on the submission portal.
9. Lexique 4 appeared in 2026; the study uses Lexique 3.83, fixed in the preregistration. A reviewer may ask.
