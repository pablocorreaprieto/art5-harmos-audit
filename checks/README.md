# Checks

Every check here can fail. Each has a failure control: a planted fault or an earlier version of the code that the check was seen to reject, for the reason it tests.

**Running them.**

- `bash checks/run_all.sh` runs all checks on the code in `ART5_CODE` (default: the repository root).
- It writes each output to `checks/outputs/` (or `CHECKS_OUT`), together with `tested_versions.txt` (date, Python, lexicon and the SHA-256 of every file tested).
- A check passes only when it exits 0 and prints its exact success line. `run_all.sh` exits 1 if any check fails.
- Before writing new outputs, `run_all.sh` copies the previous run to `checks/history/run_<UTC date>/` (to `OUT/previous_<date>/` when `CHECKS_OUT` is set), so no earlier output is lost.
- `--with-sim` also reruns the power simulation (about 4 minutes).

**Needs.**

- The packages of `requirements.txt`.
- Lexique 3.83, found through `LEXIQUE`, else `data/lexicon/Lexique383.tsv` (from `python pipeline.py --step lexicon`), else the copy in the `pylexique` package.
- The offline tests start mock servers on local ports. Nothing reaches a provider and nothing is billed. Their answers are fake and are not data.

| Check | Program | What it claims | Passes when | Failure control (observed) |
|---|---|---|---|---|
| selftest_compute | `compute.py --self-test` | Golden texts and their lemmas, refusals excluded and texts with a refusal phrase kept, ligatures in the lexicon, invariance to names and tense, planted rare words, flags | last line `OK` | the 59 mutations below |
| selftest_analyze | `analyze.py --self-test` | Planted effects found (one-year offset, ignored label, digit read as an age), nothing rejected under the null | last line `OK` | the 22 mutations below |
| plan | `checks/plan.py` | The call files built from `design.json` are byte-identical to the recorded ones (8,400 and 252 calls) | `PASS plan` | any change that alters a call changes a hash |
| mutate_compute | `checks/mutate_compute.py` | Each of 59 mutations of `compute.py` makes its self-test fail | `59 of 59 caught; 0 not run` | a surviving mutation prints `NOT caught`; in v0.3 the clitic mutation survived |
| mutate_analyze | `checks/mutate_analyze.py` | Each of 22 mutations of `analyze.py` makes its self-test fail | `22 of 22 caught` | as above |
| battery | `checks/battery.py` | 59 hand-written answers (two sets written by readings 7 and 8): no problem on the 33 plausible ones; on the others no count above the value recorded for v0.4.2 | `PASS battery` | `compute.py` v0.4 fails it (5 genuine lines lost, 3 lines addressed to the user left in, 2 wrong titles, 2 exclusions) |
| clarifications | `checks/clarifications.py` | Of 21 requests for clarification at least 14 are excluded; of 16 genuine texts near a refusal phrase at most 8 are excluded (values recorded for v0.4.2, unchanged in v0.4.3 to v0.4.5) | `PASS clarifications` | `compute.py` v0.4.1 fails it (6 of 21 excluded) |
| e2e_pilot | `checks/e2e_pilot.sh` | The pilot step keeps the counted spend under the plan budget over successive runs, then completes: 216 texts measured, summary written | `PASS e2e_pilot` | the v0.3 pipeline gave each pass the whole budget (3 × 1.00 USD for 1.05, reading 6) |
| e2e_crash | `checks/e2e_crash.sh` | A response cut mid-body does not stop the run; the spend counted from the raw records stays under the budget; a run killed before its log is still counted | `PASS e2e_crash` | the v0.4 code stops on the cut response (exit 1) and the counted spend goes over the budget |
| e2e_malformed | `checks/e2e_malformed.py` | Fourteen malformed or normal 200 answers on two routes: every run exits 0, writes its log and records all 12 calls; an answer without usable token counts is counted at the worst case; compute.py then measures the raw file of a surrogate shape | `PASS e2e_malformed` | the v0.4.2 code fails 8 of 28 runs (missing usage counted at 0, surrogate in the model id or finish reason stops compute.py); the v0.4.1 code also stopped on three shapes (None times a price, int without strip, lone surrogate) |
| e2e_secrets | `checks/e2e_secrets.py` | No key value is written or printed: a secret holding three fake keys on separate lines is not sent by list-models (the problem is recorded without the value) and stops a run before its first call; a provider answer that quotes the key (401) is stored without it | `PASS e2e_secrets` | `generate.py` v0.4.5 fails all three parts (the fake keys are in the model list, in 6 raw lines and in the 401 records), as run 41222817007 did with real keys |
| history | `history/check_history.sh` | The current version (v0.4.6) and each earlier kept version (v0.2 to v0.4.5), rebuilt from the current files, match the recorded SHA-256 of every file | `PASS history` | one wrong hex digit in `history/hashes.txt` fails it (v0.3 compute.py); a wrong diff order failed it during development |
| sim (with `--with-sim`) | `checks/sim.sh` | Rerunning `sim_power.py` gives `sim_power_results.json` byte for byte, with its controls passing | `PASS sim` | control C3 inside `sim_power.py` must exceed its bound, or the script exits 1 |

The outputs of the failure controls are in `checks/outputs/failure_controls/`. `run_all_on_empty_code.txt` shows every check failing when the code folder is empty (10 checks, v0.4.4), and `run_all_on_empty_code_v0.4.6.txt` the same with v0.4.6 (12 checks, the history check included). `e2e_secrets_on_v0.4.5.txt` shows the v0.4.5 code failing the secrets check. The two mutations added in v0.4.4 restore the v0.4.3 formula, so `mutate_compute.txt` also records v0.4.3 failing the new refusals.

**Limits.**

- The gates of `battery.py` and `clarifications.py` are regression limits recorded for v0.4.2 and unchanged in v0.4.3 to v0.4.5, not targets. The remaining cases are listed for gate G1 in `CHANGELOG.md`.
- Up to v0.4.5, `run_all.sh` ran the history check only when `history/check_history.sh` was executable, and otherwise skipped it without a message (the rebuilt repository of 31.10.2026 had lost that bit). From v0.4.6 the check always runs and fails when the script is missing.
- The answer sets were written by AI readings of the design. They are not model outputs, and their "plausible" or "edge" tags are those readings' own judgement.

**Other files.**

- Shared by the checks: `_paths.py` (code folder and lexicon), `bundle.py` (packs and unpacks text bundles with SHA-256 checks), `fast/sitecustomize.py` (shortens retry sleeps in `e2e_malformed.py` only).
- Mock servers: `mock_providers.py`, `mock_bad.py`, `mock_weird.py`.
- Answer sets and cases: `battery_answers.py`, `battery_answers41.py`, `clarification_cases.py`.

**Provenance.** Written by the main session (claude-opus-5-5) on 25.10.2026. These files were written by the reading sessions named in their docstrings, and adapted only in paths and pass/fail gates:

- `mock_bad.py`, `mock_weird.py`;
- `battery_answers.py`, `battery_answers41.py`, `clarification_cases.py`;
- the harnesses of `battery.py`, `clarifications.py` and `e2e_malformed.py`.

**Earlier outputs.** `checks/history/` keeps the scripts and outputs of the earlier runs quoted in the Contrôles tab of the project journal. Their paths point to the session's temporary folders. `checks/history/v0.4.2_run/` and `checks/history/v0.4.3_run/` hold the full runs on work copies of those versions.
