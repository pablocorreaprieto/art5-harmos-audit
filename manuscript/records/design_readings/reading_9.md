# Relectures IA de l'ART 5, lecture 9 (suite de relectures_ia.md)

> Internal reading by a separate AI session. Not peer review.

Ce document continue `claude/art5/records/relectures_ia.md`, qui garde les lectures 1 à 8 et la recherche de l'échelle de revues. Même règle : la consigne donnée et le rapport final sont copiés tels quels, le rapport depuis l'appel de remise de la session (SubagentHandback), sans retouche. Les constats sont suivis ligne par ligne dans l'onglet Relectures IA du journal (lignes 66 à 76), les actions dans l'onglet Historique, les versions dans CHANGELOG.md (v0.4.8 et v0.4.9).

Session principale, claude-opus-5-5, conversation du projet Claude ART 5, 1.11.2026. Heures de Zurich (UTC+1).

| Lecture | Heure | Rôle | Modèle | Version lue | Résultat en bref | Identifiant |
|---|---|---|---|---|---|---|
| Lecture 9 | 06:50 à 07:13 | Relecture avant dépôt (cohérence du préenregistrement, du code, du texte AsPredicted et du dossier) | claude-sonnet-5-5 | v0.4.7, dossier G1 v0.4.7, texte AsPredicted v0.4.7 | aucun chiffre du préenregistrement contredit par le code ou les résultats, dix points à corriger (quatre dans le préenregistrement, cinq dans le dossier, un sur la copie du lexique), contrôles 2 et 5 sans problème | a64a1b97d6a3fda03 |

## Lecture 9. Relecture avant dépôt (v0.4.7)

- Identifiant, a64a1b97d6a3fda03
- Modèle, claude-sonnet-5-5 (type general-purpose, lancé en arrière-plan, lecture seule)
- Heure, 1.11.2026, 06:50 à 07:13
- Version lue, PREREG.md, design.json, code et résultats du dépôt au commit 2ab397e (v0.4.7), dossier G1 et texte AsPredicted tels qu'au 1.11.2026 à 06:50
- Résultat en bref, dix points, appliqués dans la v0.4.8 du préenregistrement et dans le dossier G1 du 1.11.2026, sauf l'essai des modèles légers (non fait, pour ne pas dépenser), la relance des contrôles sur le fichier de lexique.org (prévue en P6) et la docstring de sim_power.py (laissée, listée)

### Consigne donnée (verbatim)

````text
You are an independent reviewer for a preregistered study ("ART 5": an audit of whether language models write French reading texts of matching lexical difficulty when the Swiss school grade label, e.g. "de 5H", is used instead of the pupils' age). The preregistration will be deposited on AsPredicted today and cannot be changed afterwards, so your job is to find mistakes before that. Read only; do not edit any file, do not run any GitHub workflow, do not call any model API, and do not make network calls other than reading the two Google Docs below.

Materials:
- Local git repository (read-only): /home/claude/art5-harmos-audit. Key files: PREREG.md (the preregistration text), design.json (frozen design), README.md, CHANGELOG.md (read the entries v0.4.5, v0.4.6, v0.4.7 at the top), compute.py (text cleaning, exclusions, REFUSAL_RE, META_RE, the lexical measure), analyze.py (primary tests, H1 rulers, age equivalents, bootstrap), make_prompts.py (builds the calls), pipeline.py (pilot summary and topic-count rule), sim_power.py (pilot_power), models.json (model ids and prices), results/pilot_summary.json, results/validation_vikidia.json, logs/run_*.json, data/raw/*.jsonl (pilot raw records; do not quote texts).
- Google Doc "Dossier de conception G1" (French), file id 17uBpBRChMQIo8vmA4k0bXEcJbyT3HJrAOP0ynTFVPwU.
- Google Doc "Préenregistrement AsPredicted" (English text with a French status line), file id 1PAdZDGcDzlxegtPg53qIbtY1g3mtWUypOICV8mAozFo.
Read both Docs with the Google Drive read_file_content tool (includeComments true); you may need ToolSearch to load it.

Check, in this order:
1. Every factual statement in PREREG.md against the code and design.json: counts (texts per topic, total texts, probes), labels and their wording, grades and ages, genres, topics, seed, temperature and its fallback, max output tokens, refusal/clarification and exclusion rules, flags, the measure definition, the four primary tests and Holm, H1, the age-equivalent formulas and eligibility threshold, bootstrap count, the sample-size rule and power simulation settings.
2. The AsPredicted Google Doc against PREREG.md: the English answers should match word for word (only the French status line differs). List every difference.
3. Every number in the dossier and in PREREG.md that comes from the pilot or the validation against results/pilot_summary.json, results/validation_vikidia.json, logs/run_*.json and models.json. Also recompute: main-study cost per model from the pilot's mean cost per text and per probe (16 topics = 1,280 texts and 120 probes per model), and check the dossier's estimate (about 39 USD for the three balanced models, about 3 for the light ones, 43 to 45 with retries).
4. Stale or contradictory statements in the dossier: things written as future that are already done (keys, model listing, pilot, validation), and anything that contradicts these decisions taken on 31.10 and 1.11.2026: Pablo will not write the interpretation, so Reading and Writing leaves the journal ladder (BJET, then JCAL, then JRR); 16 topics; proposed cap 60 USD. Placeholders {REPO}, {START_DATE}, {END_DATE} are expected to remain until the deposit; do not report them.
5. Arithmetic or internal inconsistencies anywhere (e.g. 480 x 16, 720 probes, 252 pilot calls = 216 + 36).

Output (under 700 words): a numbered list. For each item give: severity (blocking for the deposit / should fix / cosmetic), location (file or dossier section, with a quote of at most 15 words), what is wrong, the evidence (file and line or the value), and the fix you suggest. For any of the five checks with no problem, write "check N: none found". Mark clearly which findings you verified in the files and which are your inference.
````

### Rapport final (verbatim)

````text
Scope: five checks, both Docs; scratch-copy re-runs only. [V] verified in files, [I] inference. Nothing blocks the deposit in the strict sense (no PREREG.md figure contradicts code or results), but items 1-4 cannot be fixed afterwards.

1. Should fix. PREREG Q1 "No data for this study have been collected." contradicts the next sentences (252 pilot calls, pilot_summary.json). Fix: "No confirmatory data...", and tick the form option for existing data. [V]

2. Should fix. Q4/Q5 "this prompt wording": prompt frame, genre phrases and the 16 topics are absent; design.json and make_prompts.py are never cited. Fix: paste them (design.json l.4-44) or cite both at tag prereg. [V]

3. Should fix. Q4 "at most 4,000 output tokens": reasoning is on by default and counts in the cap. Pilot texts with thinking: Claude 61/72 (mean 280 tokens), GPT 68/72 (75), Mistral 72/72 (1,104, 67% of output); Sonnet 5.5 cannot disable it; one Mistral text and one probe hit 4,000 (probe empty). [V] It may vary with the label [I]. Fix: declare it (dossier §3 says only Mistral reasons).

4. Should fix. Dossier §2.8 table "H1 échoue pour au moins quatre modèles sur six" (no conversion) is in neither PREREG nor code: analyze.py l.41-42, 196 converts every model with slope <= -0.02 ("size, not significance"). The cap-stop row is also missing from PREREG (what is analysed if 60 USD stops collection?). Fix: register both or delete. [V]

5. Should fix (check 4). Ladder: "C'est la condition pour garder Reading and Writing dans l'échelle"; §1 "BJET, puis JCAL, puis Reading and Writing"; "Ta part reste ... conclusions à G2"; §2.9 rank 3, "Remplaçante", "les trois éditeurs". Fix: BJET, JCAL, JRR; Reading and Writing to "Exclues"; drop item 3 of "Ce que je te demande". [V]

6. Should fix. Topics decided but written open: §2.2 "16, 24 ou 32 thèmes ... nombre fixé par le pilote"; §2.8 "σ, inconnu avant le pilote", "tu décides à G1"; Annexe A "si le pilote retient 16 thèmes". Fix: 16, σ 0,117, power ,835. The 60 USD cap is consistent. [V]

7. Should fix. Done but written as future: §2.5 "À lancer dans GitHub Actions avant le pilote" (validation done, 28/29); §2.3 "identifiants datés exacts sont lus ... au pilote" (done; models.json: 5 of 6 ids undated, so §2.10 "d'où les identifiants datés" is wrong); §1 "Rien ne change dans le pilote" and "d'un à trois dollars" (2.26 USD); §4 item 4 and "mise en place le 27.10" (done 31.10). "Clés ... restent à remplacer" is consistent: commit 9e03e53 (logs/models_2026-10-31.json, on origin/main) still holds an sk-type token; rotate it before the repo goes public. [V]

8. Should fix (check 3). Pilot and validation figures match the JSON files and logs. Budget recomputed from raw tokens and models.json: Sonnet 24.73, Sol 9.69, Mistral Large 4.81 (39.23); Haiku 1.24, Luna 0.48, Small 1.37 (3.09); total 42.32, so "39" and "3" hold. "43 à 45" implies +1.6% to +6.3% retries, unstated; "plus 30 %" gives 58.5, not 60. [V] The estimate rests on age-only prompts and never-called light models; +1,000 thinking tokens per Sonnet text adds 12.8 USD [I]. Fix: state assumptions, compare console spend of 31.10 with 2.2554 USD, smoke-test the light models.

9. Should fix, low. Per tested_versions.txt the checks ran on the pylexique copy (sha fe2cb931); the study uses lexique.org (637ba37a). With the copy, 36 of 216 pilot measures change (up to 0,064 Zipf; σ 0,1173), so I could not reproduce stored values. Fix: run checks/run_all.sh on the study's file. [V]

10. Cosmetic. Q8 omits "at least 25 usable pairs" (validate_measure.py l.103); Q3 "Voici une histoire" is narrower than VOICI_META_RE (compute.py l.122: also récit, conte, poème); Q6 "No exclusion uses the value of a lexical measure" though n_words and share_oov exclude; sim_power.py l.16 bound 0.0627 vs 0.0613; design.json l.70-75, README l.28 "exact dated id"; Mistral deprecation tagged [constat], stored listing shows none. [V]

check 2: none found (identical after removing markdown and escapes; only status line and title differ).
check 5: none found in PREREG or dossier (480x16, 720, 252=216+36, 1,280/120 per model, matrix 96/79/63/60, power tables, 35+15+10).
Check 1 otherwise: all other statements match code and design.json. Not checked: SJR, policies, bibliography, prices.
````
