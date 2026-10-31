# Changelog

Design versions of ART 5 before the pilot, on 25.10.2026 (v0.1 to v0.4.4) and 31.10.2026 (v0.4.5), times in Zurich time (UTC+1). Nothing here is a result.

- A "reading" is an internal reading by a separate AI session. It is not peer review and not an outside review.
- Readings are numbered 1 to 8 as in the design dossier and the journal. The briefs and full reports of the eight readings, and of one research session on the journal ladder, are kept verbatim in the review record: `claude/art5/records/relectures_ia.md` in the Claude project, and the Drive document "RELECTURES IA" in folder 04.
- Every finding is one row of the Relectures IA tab of the project journal, with its refutation, its fix and the confirmation of the fix. Every action is one row of the Historique tab.
- Hashes are the first 16 hex digits of SHA-256. `history/hashes.txt` has the full values for every kept version.
- `history/` holds a unified diff from each version to the next, so any kept version can be rebuilt from the current files.
- The main session is claude-opus-5-5. Readers are claude-fable-5-1 or claude-sonnet-5-5, as named below.

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
