# art5-harmos-audit

Audit of large language models asked to write French reading texts for primary pupils in French-speaking Switzerland. The grade is named in several ways: the bare HarmoS label ("de 5H"), the P label used in Vaud and Geneva ("de 5P"), the label with the region or with the age, the French grade ("de CE2"), the age only ("de 8 à 9 ans"), no level at all, and the same digit with the French collège suffix ("de 5e"). The question is whether a bare Swiss label gives texts of the same lexical demand as the matching age, and whether those texts follow the grade as the age-only texts do. No human participants.

Status: design v0.4.9, after the pilot (31.10.2026) and gate G1 (1.11.2026), before the deposit of the preregistration. The pilot outputs are in `data/raw/` and `results/pilot_*`; they are excluded from every confirmatory analysis. Nothing here is a result of the study.

## Files

| File | Role |
|---|---|
| `design.json` | Frozen factorial design: grades, label wordings, genres, topics, models, sampling, pilot blocks |
| `make_prompts.py` | Builds every call (480 texts per topic, 720 knowledge probes; pilot 216 age-only texts and 36 probes), fails if the counts differ from the design, if a text prompt repeats for one model, or if the design asks for more topics than it lists |
| `generate.py` | Concurrent model calls with a budget cap and a time limit, resumable, never overwrites a raw file, temperature 1.0 with a recorded fallback; checks each key secret before any request and removes key values from everything it writes or prints; runs only in GitHub Actions |
| `compute.py` | Cleaning, exclusions and measures (mean Zipf frequency of content lemmas from Lexique 3.83 and secondary measures), one retry list, flags for answers that address the user and counts of removed preface or closing lines, an optional blinding switch (unused by the pilot, which requests age-only texts), probe export; `--self-test` runs golden texts and failure controls |
| `analyze.py` | Topic-level primary tests (level and gradient of L1 and L1P against L5, Holm over four), H1 rulers, model-internal age equivalents with a topic bootstrap, secondary and sensitivity analyses, probes; `--self-test` must find planted effects and reject nothing under the null |
| `sim_power.py` | Power and error-rate simulation through the same test function as the analysis, with controls including one that must fail; `sim_power_results.json` holds the last run |
| `validate_measure.py` | Known-groups check of the measure (Vikidia against French Wikipedia, 30 subjects) |
| `pipeline.py` | Entry point of the workflow (`--step lexicon | list-models | validate | pilot | generate | compute | analyze`); `--max-cost` is the budget of the whole plan (pilot or main study), earlier runs included |
| `PREREG.md` | Text of the AsPredicted preregistration (draft until deposited) |
| `.github/workflows/run.yml` | Manual workflow; API keys come from repository secrets only |
| `CHANGELOG.md` | Every design version before the pilot: why it changed (findings of each internal AI reading), what changed, the checks and the file hashes |
| `checks/` | Every check with its failure control; `bash checks/run_all.sh` reruns them all and writes `checks/outputs/` (see `checks/README.md`) |
| `history/` | Earlier design versions as diffs, their file hashes, and `check_history.sh`, which rebuilds each version and compares the hashes |

## Reproduce

1. Fork, add the secrets `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `MISTRAL_API_KEY` (each holds one key, on one line) and the variable `CONTACT_EMAIL`.
2. Actions, run, step `list-models`; write `models.json` with the exact model ids (and their dates when the provider lists them) and the prices.
3. Steps `validate`, `pilot`, then `generate`, `compute`, `analyze`.
4. Raw outputs are in `data/raw/` with their SHA-256; the numbers quoted in the paper are the named fields of `results/numbers.json`.

Model outputs change over time; the archived raw files at the tagged release are the data of the study.

## Licences

Code: MIT. Generated texts and derived tables: CC BY 4.0. Lexique 3.83 (New, Pallier, Brysbaert & Ferrand, 2004; http://www.lexique.org) is used under CC BY-SA 4.0 and is downloaded by the workflow, not redistributed here. Vikidia and Wikipedia pages used by the measure check are not stored, only their titles, revision ids and measures.
