# Relectures IA de l'ART 5, consignes et rapports complets

> Internal reading by separate AI sessions. Not peer review.

Ce document garde, pour chaque session IA séparée lancée pendant la conception de l'ART 5, la consigne donnée et le rapport final tels quels. Ce sont des lectures internes par des sessions IA séparées, pas des relectures par les pairs ni des relectures externes. Les lectures sont numérotées comme dans le dossier G1 et le journal (lecture 1 à 8). La session de recherche de l'échelle de revues n'est pas une lecture, elle figure ici parce que son rapport complet devait être gardé. Les constats, leur réfutation, leur application et leur confirmation sont suivis ligne par ligne dans l'onglet Relectures IA du journal de bord, chaque action dans l'onglet Historique, chaque version dans CHANGELOG.md. Les rapports sont copiés depuis l'appel de remise de chaque session (SubagentHandback), sans retouche. Les chemins /tmp/... qu'ils citent désignent l'espace de travail temporaire de la session, fermé depuis. Les scripts écrits par les lecteurs sont gardés dans le lot reader_scripts_bundle.txt du projet Claude.

Session principale, claude-opus-5-5, conversation du projet Claude ART 5, 25.10.2026. Heures de Zurich (UTC+1).

| Lecture | Heure | Rôle | Modèle | Version lue | Résultat en bref | Identifiant |
|---|---|---|---|---|---|---|
| Recherche | 15:04 à 15:44 | Recherche de l'échelle de revues | claude-opus-5-5 | aucune (recherche web, pas de lecture du code) | Échelle BJET, JCAL, Reading and Writing, JRR en remplaçante, exclusions motivées | acc8168e8d2b072a8 |
| Lecture 1 | 15:21 à 15:34 | Relecture adverse du dossier de conception | claude-fable-5-1 | v0.1 | 24 constats A1 à G24, dont sept bloquants | a7f03bbb7acb0aaa9 |
| Lecture 2 | 15:37 à 16:02 | Réfutation des constats principaux | claude-sonnet-5-5 | v0.1 | aucun constat réfuté, C11 et D15 maintenus en partie | a09782157132d378e |
| Lecture 3 | 16:34 à 16:49 | Vérification des corrections | claude-fable-5-1 | v0.2 | corrections statistiques confirmées, 13 défauts N1 à N13 dont quatre bloquants | a086027218acd0b04 |
| Lecture 4 | 16:51 à 17:08 | Réfutation de N1 à N13 | claude-sonnet-5-5 | v0.2 | aucun constat réfuté | afb95676e5f8883f3 |
| Lecture 5 | 17:16 à 17:44 | Confirmation des corrections | claude-sonnet-5-5 | v0.3 | 12 corrections confirmées, N9 en partie, nouveaux défauts D1 à D5, restes R1 et R2 | a626c2db760db0f98 |
| Lecture 6 | 17:46 à 18:02 | Réfutation de D1 à D5, R1 et R2 | claude-sonnet-5-5 | v0.3 | D1 à D5 maintenus au moins en partie, R1 réfuté pour l'exemple donné, R2 maintenu mais peu plausible | ac38a015650cb9bcc |
| Lecture 7 | 18:28 à 18:59 | Confirmation des corrections | claude-sonnet-5-5 | v0.4 | D1 à D4 et R1 confirmés, D5 tel que décrit, R2b en partie, nouveaux constats V1 à V5 (V1 moyen, sur la dépense) | aad05b1fca8b0d365 |
| Lecture 8 | 19:22 à 20:02 | Confirmation étroite des corrections | claude-sonnet-5-5 | v0.4.1 (generate.py mis à jour pendant la lecture, 81bc955a) | V1 confirmé après la mise à jour (0 dépassement sur 39 essais), V3 et V4 confirmés, V2 et V5 en partie, constats W1 à W5 dont un reste de V1 (réponses illisibles qui arrêtent l'exécution) et une régression du correctif V4 (demandes en tu sans « me ») | aa0068f00eed2165b |
| Lecture 8, tour 2 | 20:22 à 20:45 | Relecture des corrections v0.4.2 | claude-sonnet-5-5 | v0.4.2 (compute.py 1f5742c8c36b24a8, generate.py 4680bda30be1d520) | W1, W2 et W4 confirmés, constats X1 à X5 | aa0068f00eed2165b |
| Lecture 8, tour 3 | 20:51 à 21:06 | Relecture des corrections v0.4.3 | claude-sonnet-5-5 | v0.4.3 (compute.py a24472f501d4e52e, generate.py 7ce38baa5b8f397e) | X1 à X3 confirmés, effet Y1 sur « à quelle », « quels » et « quelles », notes Y2 et Y3 | aa0068f00eed2165b |
| Lecture 8, tour 4 | 21:07 à 21:09 | Relecture du correctif v0.4.4 | claude-sonnet-5-5 | v0.4.4 (compute.py 8ad7a56512616c64, generate.py inchangé) | correctif de Y1 confirmé, aucune régression | aa0068f00eed2165b |

## Recherche. Recherche de l'échelle de revues

- Identifiant, acc8168e8d2b072a8
- Modèle, claude-opus-5-5
- Heure, 25.10.2026, 15:04 à 15:44
- Version lue, aucune (recherche web, pas de lecture du code)
- Résultat en bref, Échelle BJET, JCAL, Reading and Writing, JRR en remplaçante, exclusions motivées
- Dossier de travail cité, aucun dossier de travail

### Consigne donnée (verbatim)

````text
You are helping build the journal ladder for a research article. Do web research only (WebSearch and WebFetch). Do not write any files or touch Google Drive. Return a structured report.

The article: an audit of large language models (Claude, GPT, Mistral, called through their APIs) that generate French reading texts for primary-school pupils in French-speaking Switzerland. The question is whether the Swiss HarmoS grade labels (3H to 8H, ages 6 to 12) are interpreted correctly compared with age labels and French grade labels (CP to 6e), measured with lexical frequency (Lexique 3) and sentence length. No human participants. Written in English. The manuscript is developed almost entirely with AI (design, code, analysis, drafting) under the author's supervision and responsibility, and that use is fully disclosed. The author wants three Q1 journals, from most ambitious realistic to safest, with NO publication fee on the subscription route (hybrid journals are fine if publishing non-OA is free).

Candidates to check (add one or two others if a clearly better fit turns up):
1. Journal of Computer Assisted Learning (Wiley)
2. British Journal of Educational Technology (Wiley)
3. International Journal of Artificial Intelligence in Education (Springer)
4. Reading and Writing (Springer)
5. Journal of Research in Reading (Wiley)
6. Computers & Education (Elsevier) — check its generative-AI policy carefully, it may rule out AI-developed manuscripts.
7. Education and Information Technologies (Springer) — note: the author already targets this journal with another article.

For each journal record:
- Publisher and quartile: SJR quartile in Education (or the best-fitting category) with the year and the source URL (scimagojr.com journal page if it loads). If it does not load, say so and give what you could find, labelled.
- Fee on the subscription route: is publishing non-open-access free? Give the source sentence or page.
- Word limit (or page limit) for an original research article, with source.
- Review model (single-blind, double-blind), and whether an anonymised manuscript is required.
- AI policy: the exact text (verbatim quote, keep it short, the key 1-3 sentences) of the journal's or publisher's policy on generative AI use by authors, with its URL. Say clearly whether a manuscript where AI did most of the drafting, analysis and code, fully disclosed and with the human author taking responsibility, is (a) explicitly allowed, (b) allowed only for language editing, or (c) unclear. Quote, do not paraphrase, for the decisive sentence.
- Two recent articles (2023-2026) in that journal close to this topic (LLM-generated educational texts, readability, AI content generation for school, text complexity), with authors, year, title and DOI. Say how far you read each (abstract only is fine).
- Scope fit in one sentence.

Integrity rules, they matter more than coverage:
- Label every fact with how you know it: read-directly (you read the page itself), abstract-only, search-summary (only a search result snippet), or not found.
- Never fill a gap from memory. If a page is blocked (403, paywall, robots, bot protection), list it under Blocked and try another official source (publisher policy hub, Wiley Author Services, Springer Nature editorial policies, Elsevier policy page). If nothing loads, write "not verified".
- Copy quotations, titles, years and DOIs exactly from the source.

Output format: one section per journal with the fields above, then a short ranking proposal (3 journals, most ambitious realistic first) with the reason for each rank and any journal you would exclude and why, then a list of every URL you opened and every URL that was blocked.
````

### Rapport final (verbatim)

````text
## Journal ladder report: LLM audit of HarmoS grade labels (researched 2026-10-25)

**Coverage gaps.** Wiley Online Library and ScienceDirect blocked every request. So the official author guidelines of JCAL, BJET, JRR, Computers & Education and the Elsevier-era IJAIED were never read. For those journals the word limit, the review model and any journal-specific AI wording are "not verified" unless another source is named.

**How facts are labelled**
- **[read-directly]** The page loaded and the passage was pulled out by the WebFetch reader, which I asked for verbatim text. "2 passes" means two separate fetches returned the same wording.
- **[metadata]** A Crossref, OpenAlex or DOAJ API record that I read.
- **[third-party]** An unofficial site.
- **[secondary]** An official text reproduced somewhere else.
- **[reasoning]** My inference.
- **[abstract-only]** Only the abstract was read.
- **[not verified]** The official source was blocked.

WebSearch returned only titles and URLs, never snippets. So nothing below rests on a search summary alone. Quartiles come from the SJR 2025 edition, with 2024 for comparison.

**Short answer (a view, reasons in the ranking section):** 1. BJET, 2. JCAL, 3. Reading and Writing. JRR is the swap for #3 if Springer's AI rules are the binding constraint.
- **Exclude Computers & Education:** its AI-policy wording is against you and its scope carries a desk-reject warning.
- **Exclude IJAIED:** it moved to Elsevier on 1 Jan 2026 and is probably gold OA now, so the fee criterion likely fails.
- **Keep EAIT only as a fallback.**

---

### 1. Journal of Computer Assisted Learning (JCAL), Wiley

**Quartile**
- Publisher: Wiley-Blackwell. SJR: Q1 in Education for 2024 and 2025, also Q1 in Computer Science Applications and E-learning.
- SJR 2025 = 2.155, H-index 129 [read-directly, 1 pass]. https://www.scimagojr.com/journalsearch.php?q=26183&tip=sid&clean=0

**Fee on the subscription route**
- Wiley publisher level: "If you are unwilling or unable to pay for open access, your article will be published on Wiley Online Library as a subscription article." [read-directly, 2 passes] https://authors.wiley.com/asset/Make-your-article-open-access-with-OnlineOpen.pdf
- Hybrid confirmed: 11 of 40 JCAL items from June 2026 onward carry a CC licence, the other 29 do not [metadata].
- So publishing without OA is free by default [reasoning]. Journal-level page or colour charges are not verified.

**Word limit:** not verified. A third-party SciSpace template page says "no single overall word limit is stated in the accessible guide" [third-party].

**Review model:** not verified. SciSpace says "blind model not specified" [third-party].

**AI policy (Wiley), https://authors.wiley.com/ethics-guidelines/index.html** [read-directly, 2 passes on the key sentences]
- "Authors may only use AI Technology as an additional tool in their writing process, not a replacement for their own expertise and judgement."
- "If an author has used AI Technology to substantially edit, develop, or translate any part of a manuscript, its use must be described transparently and integrated into the manuscript as described in our guidance on disclosure and declaration of AI use."
- "The final decision on whether using AI Technology is appropriate or permissible for a submitted manuscript or a published article belongs to the journal's editor or other party responsible for the publication's editorial policy."
- Secondary: a UKSG news item of 29 Oct 2025 says, in UKSG's own words rather than a Wiley quote, that Wiley's new guidance covers disclosure for "drafting and editing, study design, data collection, literature review, data analysis, and visuals" and "AI use should not result in automatic manuscript rejection." The Wiley guidelines page itself was blocked.
- **Verdict: (a) qualified.** Substantial AI development of a manuscript is explicitly provided for, with disclosure. Whether "most of the drafting" is acceptable stays with the editor, under the "not a replacement" clause. Journal-specific wording not verified.

**Two recent articles**
1. Patel, N., Nagpal, P., Shah, T., Sharma, A., Malvi, S., & Lomas, D. (2023). "Improving mathematics assessment readability: Do large language models help?" https://doi.org/10.1111/jcal.12776
   - Read: abstract-only, via OpenAlex.
   - GPT-3 simplified 250 math items for grades 3–5. Readability improved but the output was noisy.
2. Lohr, D., Berges, M., Chugh, A., Kohlhase, M., & Müller, D. (2024). "Leveraging Large Language Models to Generate Course‑Specific Semantically Annotated Learning Objects." https://doi.org/10.1111/jcal.13101
   - Read: abstract-only, via OpenAlex.

**Scope fit:** The SJR scope reads "covers the whole range of uses of information and communication technology to support learning and knowledge exchange" [read-directly]. Patel et al. is a learner-free LLM readability study at primary grades, so the fit is good [reasoning].

### 2. British Journal of Educational Technology (BJET), Wiley for BERA

**Quartile**
- SJR: Q1 in Education and E-learning for 2024 and 2025.
- SJR 2025 = 3.830, H-index 143 [read-directly]. https://www.scimagojr.com/journalsearch.php?q=23988&tip=sid&clean=0

**Fee on the subscription route**
- Same Wiley publisher-level sentence as JCAL.
- Hybrid confirmed: 18 of 40 items from March 2026 onward carry a CC licence, 22 do not [metadata].
- Journal-level charges not verified.

**Word limit**
- "Manuscripts should not normally exceed 6000 words, excluding references." [secondary, 2 passes]
- Source: a BJET special-issue call reposted by EdTech Hub on 10 Jan 2025. The call says contributions follow the BJET Author Guidelines. https://edtechhub.org/2025/01/10/call-for-papers-the-british-journal-of-education-technology/

**Review model**
- "All submissions will go through the usual process of double-anonymous peer review." [same secondary source, 2 passes]
- So an anonymised manuscript is required [reasoning].

**AI policy:** Wiley, as for JCAL. **Verdict: (a) qualified.**

**BJET Spring 2025 editorial** (doi 10.1111/bjet.13581) [abstract-only, OpenAlex index]
- It asks LLM studies to report "model name, version, provider, modifications or fine-tuning".
- It adds: "If using commercial Large Language Models, you might also consider providing prompt engineering details".
- On competition: "In 2024, we saw a huge uptick in submissions, with a 39% increase over the previous year" and "Notably, our acceptance rate for 2024 dropped to 11%". It also reports more desk rejections.
- The indexed text contained nothing on AI-assisted manuscript writing.

**Two recent articles**
1. Li, H., Xing, W., Li, C., Zhu, W., & Oh, H. (2024). "Are simpler math stories better? Automatic readability assessment of GAI‐generated multimodal mathematical stories validated by engagement." https://doi.org/10.1111/bjet.13554
   - Read: abstract-only. Readability of AI-generated stories for grades 3–5.
2. Malik, R., Abdi, D., Wang, R., & Demszky, D. (2025). "Scaffolding middle school mathematics curricula with large language models." https://doi.org/10.1111/bjet.13571
   - Read: abstract-only.

**Scope fit:** BJET wants research "that demonstrate whether and how applications of instructional/educational technology systems, networks, tools and resources lead to improvements in formal and non-formal education at all levels" [read-directly, SJR scope]. The topic fits well. But a study with no learners must argue its consequence for education, for example teachers using LLMs to make levelled texts [reasoning].

### 3. International Journal of Artificial Intelligence in Education (IJAIED)

**Publisher change**
- Springer's journal page: "The International Journal of Artificial Intelligence in Education (IJAIED) will be no longer be published by Springer." and "As of January 1st, 2026 this journal will be published by Elsevier." [read-directly] https://link.springer.com/journal/40593
- Crossref shows the 2026 items with 10.1016/j.ijaied.* DOIs and publisher "Elsevier BV" [metadata].

**Quartile**
- SJR: Q1 in Education 2024 and 2025. SJR 2025 = 3.207 [read-directly]. https://www.scimagojr.com/journalsearch.php?q=19600156811&tip=sid&clean=0
- These figures cover the Springer era.

**Fee: not verified, likely fails**
- All 14 Elsevier-era items dated 2026 carry CC licences: 5 CC BY and 9 CC BY-NC-ND [metadata].
- That points to full open access, which normally means an APC [reasoning].
- The ScienceDirect page was blocked by robots rules. The journal is not in DOAJ (0 results) [metadata].

**Word limit / review model:** not found. The Springer page gave neither, and the Elsevier guide was blocked.

**AI policy:** Elsevier's policy now applies (see Computers & Education below). **Verdict: (c), leaning restrictive.**

**Two recent articles**
1. Watanabe, M. (2025). "ChatGPT, Can You Make this Text Easier?: Investigating the Utility of LLMs in Easing Text Readability." https://doi.org/10.1007/s40593-025-00520-7
   - Read: abstract-only. Only the grade-targeted prompts eased readability.
2. Norberg, K. A., Almoubayyed, H., De Ley, L., Murphy, A., Weldon, K., & Ritter, S. (2024 online; vol. 35(2), 2025). "Rewriting Content with GPT-4 to Support Emerging Readers in Adaptive Mathematics Software." https://doi.org/10.1007/s40593-024-00420-2
   - Read: abstract-only.

**Scope fit:** The journal "publishes papers concerned with the application of AI to education" [read-directly, shop.elsevier.com]. This is the strongest topical fit of the list, but it fails on fee and policy.

### 4. Reading and Writing, Springer

**Quartile**
- SJR: Q1 in Education 2024 and 2025, also Q1 in Linguistics and Language.
- SJR 2025 = 1.206, H-index 101 [read-directly]. https://www.scimagojr.com/journalsearch.php?q=22281&tip=sid&clean=0

**Fee on the subscription route**
- "Authors can also choose to publish under the subscription publishing model (no APC charges apply)." [read-directly] https://link.springer.com/journal/11145/how-to-publish-with-us
- On colour: "Color art is free of charge for online publication." Print colour needs a contribution [read-directly].

**Word limit:** "The manuscript should be no longer than 9000 words or ca. 35 double spaced A-4 pages, including references, tables, etcetera." [read-directly, 2 passes] https://link.springer.com/journal/11145/submission-guidelines

**Review model**
- "This journal follows a double-blind reviewing procedure."
- "It is the responsibility of the author to anonymize the manuscript and any associated materials." [2 passes]
- A separate title page is required.
- Median time from submission to first decision: "3 days" [read-directly]. That suggests fast desk screening [reasoning].

**AI policy:** three current official layers.
1. Journal page:
   - "Use of an LLM should be properly documented in the Methods section (and if a Methods section is not available, in a suitable alternative part) of the manuscript."
   - The copy-editing exemption excludes "generative editorial work and autonomous content creation".
2. Springer brand policy, https://link.springer.com/brands/springer/journal-policies [read-directly; I read the first 100,000 of 120,153 characters]:
   - The amber tier, which covers "Extensive copy editing or writing support", is "Permitted with human oversight, verification, and transparency through disclosure."
   - Red tier: "Generating hypotheses, analyses or conclusions and presenting them as human-derived" and "Using an LLM to generate core research reasoning without disclosure".
3. Springer Nature, https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation [2 passes]:
   - Amber includes "drafting sections based on author input".
   - **Red (not permitted):** "Writing results or discussion independently; generating scientific claims or interpretations; producing data or figures as if empirical; listing AI as an author; creating content from text prompts or without verifiable source data or material".
   - Also: "AI can assist with expression, but the argument, interpretation, and conclusions must be author-led."

**Verdict: (c) unclear.** Use beyond language editing is allowed with disclosure. But results, discussion and interpretation written by AI fall in the red tier on the Springer Nature page.

**Two recent articles**
1. Liu, F., Lu, X., Jin, T., Kang, M., & Zhang, H. (2025). "Does ChatGPT simplify texts like expert teachers? Linguistic features of simplified texts." https://doi.org/10.1007/s11145-025-10676-2
   - Read: abstract, partly, on the Springer page. It compares 17 lexical, syntactic and cohesion features. I did not extract the findings.
2. Mesmer, H. A. E. (2024 online; 38(1), 2025). "Exploring the frequency contours in close reading texts." https://doi.org/10.1007/s11145-023-10493-5
   - Read: abstract-only. 249 texts for grades 2–8, analysed by word frequency.

**Scope fit:** The aims cover "the processes, acquisition, and loss of reading and writing skills" [read-directly]. Two recent text-only studies make your lexical-frequency and sentence-length design publishable here [reasoning].

### 5. Journal of Research in Reading (JRR), Wiley for UKLA

**Quartile**
- SJR: Q1 in Education 2024 and 2025.
- Developmental and Educational Psychology, and Psychology (miscellaneous): Q1 in 2024, Q2 in 2025.
- SJR 2025 = 0.817 [read-directly, 1 pass; the re-check fetch failed]. https://www.scimagojr.com/journalsearch.php?q=12834&tip=sid&clean=0

**Fee on the subscription route**
- Same Wiley publisher-level sentence.
- Hybrid: 16 of 40 items from June 2025 onward carry a CC licence, 24 do not [metadata].

**Word limit / review model:** not verified. The UKLA page says only "refereed" [read-directly].

**AI policy:** Wiley. **Verdict: (a) qualified.**

**Two recent articles**
- No LLM or AI article turned up in three Crossref title searches for 2023–2026 [metadata]. These are the closest:
1. Green, C., & Keogh, K. (2024). "Vocabulary exposure to children is enhanced by using both informational and narrative picture books for read‐alouds: A comparative modelling study using data science methods." https://doi.org/10.1111/1467-9817.12462
   - Read: abstract-only. A corpus of more than 2,000 picture books.
2. Cain, K., Currie, N. K., Francey, G., Davies, R. A. I., Gray, S. I., Bridges, M. S., Restrepo, M. A., Thompson, M. S., & Ciraolo, M. F. (2024). "The influence of reader and text characteristics on sixth graders' inference making." https://doi.org/10.1111/1467-9817.12474
   - Read: abstract-only.

**Scope fit:** JRR is "principally devoted to reports of original empirical research in reading and related fields" [read-directly, UKLA]. A corpus-style study is plausible, but with no LLM precedent the scope risk is higher [reasoning].

### 6. Computers & Education, Elsevier

**Quartile**
- SJR: Q1 in Education 2024 and 2025.
- SJR 2025 = 4.434, H-index 267 [read-directly]. https://www.scimagojr.com/journalsearch.php?q=17645&tip=sid&clean=0

**Fee on the subscription route**
- "Authors publishing in hybrid journals can publish under the subscription model at no cost" [read-directly, 2 passes] https://www.elsevier.com/researcher/author/open-access/choice
- Hybrid confirmed: 18 of 40 items carry a CC licence, 22 do not [metadata].

**Word limit:** not verified. Manusights says "sets no rigid body word cap for Articles" [third-party].

**Review model:** not verified. Manusights says "Double anonymized peer review" [third-party].

**AI policy:** Elsevier policy, "Policy updated June 2026." https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals [2 passes on the key sentences]
- "Authors preparing a manuscript for an Elsevier journal can use AI tools to support them in these tasks." The tasks named are literature synthesis, "content organization and improving language and readability".
- "However, these tools must never be used as a substitute for human critical thinking, expertise and evaluation."
- Listed as inappropriate: "Generating sections of a manuscript without genuine intellectual contribution from the author."
- Listed as appropriate: "Improving language, clarity, and readability of text written by the authors."
- On research use: "This policy does not prevent the use of AI tools in formal research design or research methods", provided the use is described reproducibly in the Methods.
- "Please note that the range of AI use varies depending on the journal."
- The journal's own guide was blocked, so C&E-specific wording is not verified.

**Verdict: (c), leaning (b).** I found no outright ban on AI-developed manuscripts at publisher level. But AI drafting is not among the listed allowed uses, and the journal guide may be stricter.

**Scope risk** [read-directly, shop.elsevier.com]
- "We do not publish small-scale evaluations of specific software/systems in specialist domains"
- "Papers that do not address the criteria outlined in the author guidelines will be returned without review."

**Two recent articles**
1. Lim, H., Lee, E., Kwoun, S. E., Bae, S.-H., Park, G.-M., Hwang, Y., & Lee, S.-M. (2026). "Diffusion-based AI system for second language reading: Development, text quality validation, and learner perception." https://doi.org/10.1016/j.compedu.2026.105653
   - Read: title and metadata only. No abstract was reachable.
2. Zaklas, N., & Gazit, T. (2026). "The experience of using AI-generated social stories as a behavioral intervention tool for children." https://doi.org/10.1016/j.compedu.2026.105723
   - Read: abstract-only.

**Scope fit:** The journal "aims to increase knowledge and understanding of ways in which digital technology can enhance education" [read-directly]. The topic fits, but the AI policy and the desk-reject warning make it a poor match for this manuscript [reasoning].

### 7. Education and Information Technologies (EAIT), Springer

**Quartile**
- SJR: Q1 in Education 2024 and 2025.
- SJR 2025 = 2.131 [read-directly]. https://www.scimagojr.com/journalsearch.php?q=144955&tip=sid&exact=no (the "&clean=0" form of the URL failed twice).

**Fee on the subscription route:** "Authors can also choose to publish under the subscription publishing model (no APC charges apply)" [read-directly] https://link.springer.com/journal/10639/how-to-publish-with-us

**Word limit / review model:** not found on the submission-guidelines or how-to-publish pages.

**AI policy:** Springer layers as for Reading and Writing; the journal page carries the same LLM paragraph. **Verdict: (c).**

**Two recent articles**
1. Shin, D., Kwon, S. K., & Lee, Y. (2025). "Examining the efficacy of generative artificial intelligence in item generation: comparative analysis of human-developed and AI-generated reading tests." https://doi.org/10.1007/s10639-025-13683-6
   - Read: abstract-only.
2. Luo, Z., Lin, D., & Liu, T. (2026). "Zero-shot prompting with GenAI for EFL cloze text generation: a mixed-methods evaluation for language assessment in China." https://doi.org/10.1007/s10639-026-14163-1
   - Read: abstract-only. In this study, 117 teachers rated GPT-4o texts slightly lower for difficulty appropriateness. That is the closest to your grade-calibration question.

**Scope fit:** The journal "covers the complex relationships between information and communication technologies and education" [read-directly]. Good fit, but you already target it.

### Other journals checked (none fit better)
- **Educational Technology & Society:** Q1, SJR 2025 2.109.
  - "There is no charge for publishing in the ET&S journal."
  - Limit under 8,000 words; double-blind review.
  - But: "Authors should only use AI and AI-assisted technologies to improve readability and language, and the listing of references of the manuscript." The journal also runs "an AI similarity index check" [read-directly].
  - Verdict (b). **Exclude.**
- **Journal of Educational Computing Research (SAGE):** Q1, SJR 2025 2.457.
  - SAGE's AI policy lists as inappropriate "Generation of data or submission using a series of prompts" [read-directly].
  - Verdict (c), leaning restrictive. Not proposed.
- **Computers and Education: Artificial Intelligence:** gold OA, APC up to 2940 USD per DOAJ [metadata]. **Excluded on fee.**
- **L1 Educational Studies in Language and Literature:** Q3 in Education 2025 [read-directly]. **Excluded.**
- **A related paper for your literature review:** Ripoll Y Schmitz & Sonnleitner (2025), Large-Scale Assessments in Education 13(1). They used GPT-4 to write German reading texts for Luxembourg's large-scale assessment [abstract-only, ORBilu; no DOI on the page].

---

### Ranking (my view)
1. **BJET (most ambitious, still realistic).**
   - Highest SJR among journals whose AI policy is compatible with your workflow, and Wiley's policy explicitly covers substantial AI development with disclosure.
   - Li et al. (2024) is a direct precedent.
   - Your API audit naturally provides the model, version and prompt detail the editorial asks for.
   - Risks: 11% acceptance in 2024, about 6,000 words, and you must spell out what the audit means for education when there are no learners in the study.
2. **JCAL.** Same Wiley policy. Its precedent is a learner-free LLM readability study at grades 3–5 (Patel et al. 2023), which is the closest match in design. Word limit not verified.
3. **Reading and Writing (safest on scope).** It has text-only precedents in both directions: ChatGPT text simplification and word-frequency analysis. The limit is 9,000 words including references, and the subscription route is explicitly free. The price is the Springer Nature rule that interpretation must be author-led.
   - **Swap to JRR** (Wiley policy, Q1 in Education) if you cannot honestly say that you led the results and discussion. JRR carries more scope risk.

**Excluded**
- **Computers & Education:** its policy names "Generating sections of a manuscript without genuine intellectual contribution from the author" as inappropriate, the journal guide could not be read, and the scope warns against "small-scale evaluations".
- **IJAIED:** now Elsevier and probably gold OA with an APC.
- **EAIT:** fallback only, because you already target it.

**Where your framing is the problem.** Across all three publishers the decisive test is not who typed the draft. It is who owns the interpretation and the conclusions. Your disclosure statement should name your role in those concretely. If AI also led the interpretation, every journal here is at risk, and the Springer journals most of all.

---

### URLs opened
**SciMago (SJR)**
- Search pages: q=Journal+of+Computer+Assisted+Learning; British+Journal+of+Educational+Technology; International+Journal+of+Artificial+Intelligence+in+Education; Reading+and+Writing; Journal+of+Research+in+Reading; Computers+and+Education; Education+and+Information+Technologies; Journal+of+Educational+Computing+Research; Educational+Technology+and+Society; L1+Educational+Studies+in+Language+and+Literature
- Journal pages (journalsearch.php, tip=sid&clean=0): q=26183 (loaded twice); q=23988 (twice); q=19600156811; q=22281 (first attempt); q=12834 (first attempt); q=17645; q=18874; q=18405; q=145569
- EAIT journal page: q=144955&tip=sid&exact=no

**Wiley and related**
- https://authors.wiley.com/ethics-guidelines/index.html (3 times)
- https://authors.wiley.com/asset/Make-your-article-open-access-with-OnlineOpen.pdf (2 times)
- https://authors.wiley.com/author-resources/Journal-Authors/open-access/hybrid-open-access/index.html
- https://authors.wiley.com/open-access/hybrid-open-access/index.html (loaded, no body text)
- https://newsroom.wiley.com/press-releases/press-release-details/2025/Wiley-Releases-AI-Guidelines-for-Authors/default.aspx
- https://www.uksg.org/?p=25636 (2 times)
- https://the-hospitalist.org/wp-content/uploads/2025/04/Wiley-AI-Guidelines.pdf (third-party copy)
- https://www.editage.com/insights/wiley-guidelines-for-responsible-ai
- https://www.editage.com/research-solutions/journal/journal-of-computer-assisted-learning/15751
- https://ukla.org/research-journals/journal-of-research-in-reading-jrir/
- https://www.bera.ac.uk/publications/british-journal-of-educational-technology (a 2016 page, not useful)
- https://edtechhub.org/2025/01/10/call-for-papers-the-british-journal-of-education-technology/ (2 times)
- https://www.eduhk.hk/ele/news/call-for-papers-informal-digital-learning-of-english-idle-as-innovative-pedagogy-mapping-current-and-future-trends
- https://www.myhuiban.com/journal/759.md
- https://scispace.com/templates/journal-of-computer-assisted-learning-template-xl0i8n0vbomlsr8
- https://researcher.life/ja/journal/journal-of-research-in-reading/16600
- https://oapublishing.mpdl.mpg.de/journals/Record/Wiley-BJET

**Springer / Springer Nature**
- https://link.springer.com/journal/11145/submission-guidelines (2 times)
- https://link.springer.com/journal/40593/submission-guidelines
- https://link.springer.com/journal/10639/submission-guidelines
- https://link.springer.com/journal/40593/how-to-publish-with-us
- https://link.springer.com/journal/10639/how-to-publish-with-us
- https://link.springer.com/journal/11145/how-to-publish-with-us
- https://link.springer.com/journal/40593
- https://link.springer.com/journal/10639 (the content served looked out of date)
- https://link.springer.com/journal/11145
- https://link.springer.com/journal/11145/aims-and-scope
- https://link.springer.com/brands/springer/journal-policies (2 times, partial)
- https://link.springer.com/article/10.1007/s11145-025-10676-2
- https://link.springer.com/article/10.1007/s11145-023-10493-5
- https://link.springer.com/article/10.1007/s10639-025-13683-6
- https://link.springer.com/article/10.1007/s10639-026-14163-1
- https://support.nature.com/en/support/solutions/articles/6000084580-costs-of-publishing-in-springer-nature-journal
- https://www.springernature.com/gp/policies/editorial-policies (2 times)
- https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation (2 times)
- https://www.springernature.com/gp/policies/editorial-policies/using-ai-in-research

**Elsevier**
- https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals (3 times)
- https://www.elsevier.com/authors/open-access/choice (2 times; canonical address /researcher/author/open-access/choice)
- https://www.elsevier.com/open-access
- https://www.elsevier.com/zh-cn/connect/everything-you-ever-wanted-to-know-about-open-access-but-were-afraid-to-ask
- https://www.elsevier.com/about/policies-and-standards/pricing
- https://legacyfileshare.elsevier.com/els_com_pricing/article-publishing-charge.xlsx (binary, could not be read)
- https://shop.elsevier.com/journals/computers-and-education/0360-1315 (3 times)
- https://shop.elsevier.com/journals/international-journal-of-artificial-intelligence-in-education/1560-4292
- https://manusights.com/blog/computers-and-education-submission-guide (third-party)

**Other publishers and sites**
- https://www.sagepub.com/journals/publication-ethics-policies/artificial-intelligence-policy (2 times)
- https://www.j-ets.net/author_guide (2 times)
- https://taylorandfrancis.com/our-policies/ai-policy/
- https://iaied.org/journal (no body text)
- https://techfak.uni-bielefeld.de/ags/wbski/gk-ev/verteiler/m17.html (a 1997 page, not useful)
- https://askbisht.com/journals/international-journal-of-artificial-intelligence-in-education (third-party, out of date)
- https://orbilu.uni.lu/handle/10993/65475
- https://api.figshare.com/v2/articles/32556423 (record had no files)
- DOAJ API: https://doaj.org/api/search/journals/issn%3A1560-4292
- DOAJ API: https://doaj.org/api/search/journals/bibjson.title%3A%22International%20Journal%20of%20Artificial%20Intelligence%20in%20Education%22
- DOAJ API: https://doaj.org/api/search/journals/issn%3A2666-920X

**Crossref API, topic searches (all filtered from 2023 or later)**
- api.crossref.org/journals/1365-2729/works: 2 topic queries
- api.crossref.org/journals/1467-8535/works: 2 topic queries
- api.crossref.org/journals/1573-0905/works: 1 topic query
- api.crossref.org/journals/1467-9817/works: 3 topic queries
- api.crossref.org/works?query.bibliographic=…&filter=issn:1467-9817: 2 queries
- api.crossref.org/journals/1560-4306/works: 1 query (0 results)
- api.crossref.org/journals/1560-4292/works: 3 topic queries
- api.crossref.org/journals/0360-1315/works: 3 topic queries
- api.crossref.org/journals/1573-7608/works: 1 topic query
- api.crossref.org/works?query.bibliographic=editorial…&filter=issn:1365-2729: 2 queries
- api.crossref.org/works?query.bibliographic=editorial…&filter=issn:1467-8535: 1 query
- https://api.crossref.org/works/10.1016/j.ijaied.2026.100015

**Crossref API, licence checks (select=DOI,license)**
- journals/1365-2729 from 2026-06-01
- journals/1467-8535 from 2026-03-01
- journals/1467-9817 from 2025-06-01
- journals/0360-1315 from 2026-06-01
- journals/1560-4292 from 2026-01-01

**OpenAlex API**
- Works by DOI: 10.1111/bjet.70039; 10.1111/bjet.13581 (2 times); 10.1111/bjet.13426; 10.1111/jcal.12776; 10.1111/jcal.13101; 10.1111/bjet.13554; 10.1111/bjet.13571
- Works by DOI: 10.1007/s40593-025-00520-7; 10.1007/s40593-024-00394-1; 10.1007/s40593-024-00420-2; 10.1007/s11145-025-10676-2; 10.1007/s11145-023-10493-5
- Works by DOI: 10.1111/1467-9817.12462; 10.1111/1467-9817.12474; 10.1016/j.compedu.2026.105653; 10.1016/j.compedu.2026.105723; 10.1007/s10639-025-13683-6; 10.1007/s10639-026-14163-1
- Source record: sources/issn:1560-4292

### URLs blocked
**Wiley Online Library and Wiley sites (failed at the site)**
- https://onlinelibrary.wiley.com/page/journal/13652729/homepage/forauthors.html
- https://onlinelibrary.wiley.com/page/journal/14679817/homepage/forauthors.html
- https://onlinelibrary.wiley.com/journal/13652729
- https://bera-journals.onlinelibrary.wiley.com/hub/journal/14678535/homepage/forauthors.html
- https://bera-journals.onlinelibrary.wiley.com/hub/journal/14678535/forauthors.html
- https://www.wiley.com/en-gb/publish/article/ai-guidelines/
- https://www.wiley.com/en-us/publish/article/ai-guidelines/
- https://www.wiley.com/publish/article/ai-guidelines/

**Refused by the site's robots rules**
- https://wiley.atyponrex.com/journal/JCAL
- https://www.sciencedirect.com/journal/computers-and-education/publish/guide-for-authors
- https://www.elsevier.com/journals/computers-and-education/0360-1315/guide-for-authors
- https://www.sciencedirect.com/journal/international-journal-of-artificial-intelligence-in-education
- https://www.ivysci.com/en/journals/0266-4909

**Site blocked by the fetch tool**
- web.archive.org
- archive.ph

**Other failures**
- https://figshare.com/articles/journal_contribution/BJET_editorial_2026_The_changing_landscape_of_EdTech_and_AI_scholarship/32556423
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.compedu.2026.105653?fields=title,abstract,authors,year,venue,publicationDate
- SJR: q=144955 with "&clean=0" (2 times) and without it (1 time); q=22281 on the second attempt; q=12834 on the second attempt and with "&exact=no"

**Redirect:** authorservices.wiley.com redirected with a 302 to authors.wiley.com, which I then fetched.

**Rate-limited, then loaded on retry:** link.springer.com 40593 and 10639 submission guidelines; journal/11145; 11145/aims-and-scope; article s10639-026-14163-1; two Crossref queries.

**Worth saving (for the main session's memory):** IJAIED moved from Springer to Elsevier on 1 Jan 2026, and all its 2026 articles are CC-licensed, so an APC is likely. Proposed ladder for the HarmoS LLM-audit article: BJET → JCAL → Reading and Writing, with JRR as the swap that is safer on AI policy.
````

## Lecture 1. Relecture adverse du dossier de conception (v0.1)

- Identifiant, a7f03bbb7acb0aaa9
- Modèle, claude-fable-5-1
- Heure, 25.10.2026, 15:21 à 15:34
- Version lue, v0.1
- Résultat en bref, 24 constats A1 à G24, dont sept bloquants
- Dossier de travail cité, scratchpad/referee/

### Consigne donnée (verbatim)

````text
You are a methods and statistics referee. You did not see how this study design was produced. Your job is to find what is wrong with it, not to praise it. Begin your report with: "Internal reading by a separate AI session. Not peer review."

Read these files (all local, read them fully):
- /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/dossier_g1.html (the design dossier, in French; sections 1 and 2 are the design, annex A is the draft preregistration in English; the placeholders {{LADDER_SHORT}} and {{LADDER_TABLE}} are a journal list still being filled, ignore them)
- /home/claude/art5/design.json and /home/claude/art5/make_prompts.py (the frozen factorial design and the call builder)
- /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/sim/sim_power.py and sim_power_results.json (power simulation)
- /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/sim/measures.py (prototype of the primary measure; it uses Lexique 3.83 at /usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt)

The study: an audit of six large language models asked to write French reading texts for Swiss primary pupils, where the grade is named in five ways (bare HarmoS label like "5H", HarmoS plus region, HarmoS plus age, French grade label like "CE2", age only). Primary outcome: mean Zipf frequency of content words. Main hypothesis H2: bare HarmoS labels yield rarer words than the matching age label.

Check at least:
1. Construct validity: is mean Zipf frequency of content words (adult subtitle frequencies) a defensible primary measure of text difficulty for 6 to 12 year olds? Is the age-only condition a valid internal "ruler"? Could length, genre or topic confound the label effect?
2. Design: are the five label conditions well chosen and correctly worded (look at the generated prompts by running make_prompts.py if useful)? Are the HarmoS/French/age equivalences right? Is there a condition missing that a referee would demand?
3. Statistics: is the OLS with model x grade cells, label x model effects, genre and topic, HC3 errors, and one-sided contrasts with Holm correct for H2 and H3? Are the texts independent units or is there clustering the analysis ignores? Is the conversion to "years of age" sound? Is the H1 ruler test well specified?
4. The power simulation: does sim_power.py simulate the analysis that the dossier says will be run? Are its failure controls able to fail for the right reason? Are the assumed sigma and slope plausible, and is the pilot (36 texts) big enough to update them?
5. Code: run measures.py and make_prompts.py (python3 -I file.py) and look for bugs in tokenisation, elision handling, proper-noun exclusion, content-word classification, syllable counting, out-of-lexicon handling.
6. The preregistration draft (annex A): anything ambiguous, missing or inconsistent with the dossier.
7. Threats to validity and claims: anything that overclaims.

For each finding give: location (section or file:line), the problem, why it matters, a severity (must-fix, should-fix or minor), and a concrete fix. Do not rewrite the dossier. Keep the report under 1,500 words. Label anything you could not check.
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review.

**Verdict.** The design is coherent and the arithmetic (5 760 + 360 calls, power table vs sim_power_results.json, HarmoS ages from the 31 July rule, French equivalences) checks out. But the primary measure as prototyped is dominated by tokenisation artefacts an order of magnitude larger than the hypothesised effect (0.04 Zipf/year), the text-level standard errors ignore prompt-level dependence, and the 36-text pilot cannot set k. Three must-fix clusters before the pilot runs.

## A. Measure code (measures.py) — all verified by running the file and probes against Lexique 3.83

1. **Typographic apostrophe not handled** (line 27, `'?` only). LLM French output uses U+2019. "c’est" → token "c" = NOM Zipf 5.06 counted as content; "n’a" → "n" = ADV 4.9; "j’ai" → "j" = NOM. With straight apostrophes, "ne" (7.13) and "pas" (7.26) are counted as content. **Must-fix:** normalise ’→', then exclude negation/clitic particles.

2. **Sentence-initial names count as rare content words** (line 54: proper = capitalised and not first). "Léa", "Chloé", "Hugo" → OOV → Zipf 1.0; "Pierre", "Marie", "Rose" → scored as pierre/marie/rose. Same test story with Léa / Pierre / Chloé gives 4.34 / 4.57 / 4.34: a 0.24 swing from the protagonist's name alone, i.e. six "years" at the assumed slope. **Must-fix:** NER or "capitalised mid-sentence anywhere → name everywhere"; exclude capitalised OOV tokens; report OOV share separately.

3. **Hyphenated inversion and fixed expressions** (line 27): "dit-elle", "explique-t-il", "demanda-t-il" → OOV 1.0; "aujourd'hui" → "aujourd" (1.0) + "hui" (3.37); "quelqu'un" → "quelqu" (1.0). Dialogue-heavy stories are penalised, and dialogue density plausibly varies with requested age. **Must-fix:** strip clitic suffixes (-t-il, -elle, …) or use a French tokeniser (spaCy fr).

4. **Form-level POS by most frequent reading** (lines 25, 39). "est/était/sont/été" count as content (Zipf 6–7.4) while "a/ai/ont" are excluded as AUX: 54 of 87 forms tagged AUX somewhere resolve to content. "très", "plus", "bien", "si", "oui/non", "or" (NOM) all count. These top-frequency tokens dominate a mean. **Must-fix:** contextual tagger, exclude AUX and a short stoplist of grammatical adverbs, or restrict the primary to NOM + ADJ + lexical VER lemmas.

5. **Subtitle form frequencies** (line 34, dossier 2.5). 23.8 % of Lexique content forms have film frequency 0 → Zipf 1.0, indistinguishable from OOV ("durablement": 1.0 films, 2.87 books). Passé simple forms score as rare ("regarda" 3.34 vs lemma 6.08; "répondit" 3.47 vs 5.40), so narrative tense for older readers is read as lexical rarity: a register confound aligned with age. **Must-fix:** lemma frequency (freqlemfilms2 and/or freqlemlivres) as primary, form-subtitle as secondary; Laplace smoothing rather than a floor.

6. **Title line** (requested by the prompt) is merged into the first sentence and counted; newlines are not boundaries (line 28). **Should-fix:** strip line 1 as title, pre-register it.

7. The planting self-test cannot fail for any text with mean > 2; it tests the sign of the mapping, not tokenisation. **Minor:** add a golden-file test on 3–5 realistic outputs with hand-marked content tokens.

## B. Construct

8. Title and fiche say "difficulté"/"difficulty of reading texts"; the measure is lexical sophistication under adult spoken-register frequency. For 3H–4H, decoding load (word length, graphemes) dominates and subtitle frequency does not index what a 6-year-old knows. **Should-fix:** claim "lexical sophistication"; add word length or Manulex as secondary; report median and share below Zipf 4 as robustness to the floor.

9. **Ruler.** Converting to years assumes the L5 response is linear in age; LLMs may respond in steps. **Should-fix:** pre-register a linearity check (categorical vs linear fit) and prefer inverse lookup on the six L5 cell means to dividing by a slope; call the unit "model-internal age-equivalent years".

10. Length is uncontrolled (a mediator, acceptable) but no length-adjusted sensitivity analysis is pre-registered. **Should-fix.**

## C. Design

11. **Missing L0 (no audience).** A flat L1 grade profile is compatible with "label ignored" and "label read as a constant wrong level"; only an L0 baseline separates them (section 2.1 claims the profile does). +1 152 texts at k = 2. **Should-fix.** Optional: "5e" at one grade as positive control of the collision.

12. Section 1 states Suisse romande uses 3H–8H. [Not verified against a source here] Vaud and Geneva write 5P, Neuchâtel/Jura "5e année", Fribourg/Valais 5H. The study tests only "H". **Should-fix:** add a "P" level or restrict the claim and say so.

13. Wording of the ten prompt variants is grammatical and parallel (ran make_prompts.py: 5 760/360, pilot 36/18). Probe parser unspecified: answers may list several systems or a range. **Minor:** pre-register the extraction rule and the correctness criterion.

14. generate.py:14 records sampling as the string "default"; defaults differ by provider and can change silently. No stop/finish reason field; "refusal" is not implemented anywhere though exclusions depend on it. **Should-fix:** set temperature explicitly or log the documented default; store finish reason; define refusal operationally.

## D. Statistics

15. **Prompt-level dependence.** HC3 at text level treats the k replicates of one prompt as independent; omitted interactions (topic×model, genre×grade…) make within-prompt residuals correlated. Check I ran with sim_power's design: a prompt-level SD of 0.1 (half the residual) raises the null H2 rejection rate from 3.5 % to 8 % at k = 2 and 10–16 % at k = 4. HC3 does not fix this. **Must-fix:** cluster SEs at the prompt (cell) level or analyse cell means; bootstrap by cell.

16. **Estimand under exclusions.** "Average over six models and six grades" holds only while cells stay balanced; analyze.py:45 raises on an empty cell with no fallback. **Should-fix:** equal-weight marginal means over model×grade cells, and a pre-registered fallback.

17. **Years conversion** (analyze.py:83–92) divides the pooled contrast by the mean of the *significant* slopes: selection inflates the slope, biases years downward, and contradicts dossier 2.6 (per-model ruler). Bootstrap interval promised, not implemented. **Should-fix:** per-model ratio with a non-significance-based minimum-slope rule, Fieller or bootstrap CI, then average.

18. Holm is implemented correctly, but under the null each hypothesis rejects at ~2.5–3 %, so the 12 % control bound (sim_power.py:159) is four times the expected rate and would not catch the 8 % above. **Minor:** bound from the binomial around the expected rate; add a control expected to fail (drop model×grade cells).

19. Fixed-effects inference is about these six models; the prereg should say so. H1 per-model with no correction is fine as a manipulation check, but no decision rule exists for 1–3 failures in the main study. **Minor.**

## E. Power and pilot

20. **Pilot cannot set k.** Per model, L5 slope from 6 texts (3 grades, 1 topic): SE ≈ σ/√25.3 ≈ 0.040 Zipf/yr at σ = 0.2, equal to the assumed slope; pooled ≈ 0.023. With k = 1 the pilot cannot separate within-prompt from between-prompt variance, which decides whether raising k helps at all. **Must-fix:** ~150 L5 texts (6 grades × 2 topics × 2 genres × k = 2 × 3 models, a few dollars) or fix k = 4 conservatively.

21. Stop rule "H1 flat for ≥ 4 of 6 models at pilot" is unevaluable: the pilot has 3 models. Sim grid has k ∈ {1, 2} while the prereg chooses in {2, 3, 4}; sim uses classical SE, no heteroscedasticity, skew, floor, missingness or H1 gate; its controls test contrast coding only. **Should-fix.**

22. σ = 0.15–0.25 is plausible for a clean measure (~0.12 from token sampling alone with ~100 content tokens); with the artefacts above, 0.25–0.4 is likelier. The slope is unknown for this corpus. [Estimation]

## F. Preregistration (annex A)

23. §3 names compute.py (files are measures.py, analyze.py); omits title handling, apostrophe normalisation, the actual proper-noun rule, that zero-frequency in-lexicon forms also score 1, duplicate texts (SHA already stored), truncation at 2 000 tokens, order_seed 20261025, collection window, clustering, the estimand under exclusions, the exact conversion formula, the probe parser. §6 "refusal" undefined; the 40-word floor may exclude legitimate 3H texts differentially by grade. **Should-fix.**

## G. Claims

24. "Aussi adapté", "années d'âge", "difficulty" overclaim relative to a lexical measure and a model-internal ruler; 2.10 already concedes this, so align section 1 and the title with it. Antériorité is properly hedged. **Should-fix.**

**Not checked:** model names/ids and prices; Vikidia/Wikipedia control (not yet run); Manulex licence; concordat text (ages verified by arithmetic from the stated rule); French-grade equivalences (standard, unsourced); canton label conventions; GitHub Actions runtime limits for a 6 120-call sequential run.

Scratch files: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/referee/ (diag1–3.py, clust_sim.py, mp/). Nothing in /home/claude/art5 was modified.
````

## Lecture 2. Réfutation des constats principaux (v0.1)

- Identifiant, a09782157132d378e
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 15:37 à 16:02
- Version lue, v0.1
- Résultat en bref, aucun constat réfuté, C11 et D15 maintenus en partie
- Dossier de travail cité, /tmp/refute/ (hors du dossier de session)

### Consigne donnée (verbatim)

````text
A referee report on a study design lists the findings below. Your job is to try to refute each one. For each, answer "refuted", "stands" or "partly stands", with the evidence (file and line, a command you ran and its output, or a source passage). If you cannot check one, say so. Begin your report with: "Internal reading by a separate AI session. Not peer review." Keep it under 900 words. Do not modify any file outside /tmp/refute/ (create it and work there).

Files (read them, run them with python3 -I):
- Measure prototype: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/sim/measures.py (Lexique 3.83 table at /usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt, tab-separated, latin-1, decimal commas)
- Power simulation: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/sim/sim_power.py
- Analysis: /home/claude/art5/analyze.py (run with --self-test)
- Design: /home/claude/art5/design.json and /home/claude/art5/make_prompts.py
- Dossier (French): /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/dossier_g1.html

The study: six language models write French reading texts for Swiss primary pupils; the grade is named five ways (bare HarmoS label "5H", HarmoS + region, HarmoS + age, French label "CE2", age only). Primary outcome: mean Zipf frequency of content words. H2: bare HarmoS label gives rarer words than the matching age.

Findings to test:
A1. measures.py does not handle the typographic apostrophe (U+2019), and with straight apostrophes the negation "ne"/"pas" count as content words.
A2. Sentence-initial first names (Léa, Pierre, Chloé) are not excluded as proper nouns and swing the mean Zipf of a story by about 0.24.
A3. Hyphenated inversions ("dit-elle", "demanda-t-il") and "aujourd'hui" are mis-tokenised into out-of-lexicon tokens.
A4. Content-word classification by the most frequent reading counts "est", "était", "très", "plus", "bien" as content words.
A5. Film-subtitle form frequencies score passé simple forms ("regarda", "répondit") as rare, a register confound that could align with requested age; lemma frequencies would not.
D15. Because each prompt is repeated k = 2 times, text-level HC3 errors ignore within-prompt dependence; with a prompt-level SD of half the residual SD, the null rejection rate of H2 rises from about 3.5 % to about 8 % at k = 2. (You may write a small simulation reusing build_design/contrasts from sim_power.py.)
D17. analyze.py converts to years by dividing the pooled contrast by the mean of only the significant per-model slopes, which differs from the per-model conversion the dossier describes.
E20. A pilot of 36 texts (3 models, grades 3H/5H/8H, labels L1 and L5, 2 genres, 1 topic, k = 1) cannot estimate the age slope precisely enough to choose k (per-model slope SE about as large as the assumed slope of -0.04 Zipf per year at sigma 0.2).
C11. A no-audience baseline condition (no grade at all) is needed to tell "label ignored" from "label read as a constant wrong level".
C12. In Vaud and Geneva, primary grades are usually written 1P to 8P rather than 1H to 8H, so a study testing only "H" labels misses the label Vaud teachers actually write. (Check with web search: official Vaud DGEO or Geneva DIP pages showing how grades are named, and quote them.)
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review.

Bottom line: none of the ten findings is refuted. Eight stand; D15 and C11 stand only in weaker form. [run] = I executed it, [inf] = my inference. Scripts and outputs: /tmp/refute/ (python3 -I -B).

A1 stands (measures.py). [run] WORD_RE (l.27) takes only the straight apostrophe: "L’eau n’est pas chaude." yields l, eau, n, est, pas, chaude, with "n" scored as content ADV (Zipf 4.90). With straight apostrophes, "ne" (ADV, 7.13) and "pas" (ADV, 7.26) are content. Effect of ’ on four texts I wrote: -0.03 to +0.01. compute.py v0.1 already normalised ’; ne/pas applies to it too.

A2 stands. [run] l.54 never flags a sentence-initial token. Template "{n} joue dans le jardin. Le chat de {n} saute sur une feuille. {n} rit.": Léa, Chloé, Hugo, Emma 3.70 (OOV, Zipf 1); Pierre 4.60; Marie 4.53; Rose 4.57. On an 80-content-word story, excluding names moves the mean +0.19; Léa to Pierre +0.09. The 0.24 is text-specific (swing is about m x (mean-1)/N).

A3 stands. [run] Lexique has 4,256 hyphenated forms but not dit-elle, dit-il, veux-tu or demanda-t-il: each becomes one OOV token (Zipf 1). "aujourd'hui" (in Lexique, Zipf 5.56) splits into aujourd (OOV, 1.0) plus hui (NOM, 3.37). One story: hyphens +0.13, aujourd'hui +0.07. With names added, +0.42 and +0.34 on my two stories (8 to 10 "years" at 0.04 per year); 0.00 on two documentary texts.

A4 stands, by design. [run] est: VER 19,418 vs AUX 3,319 per million; était: VER 2,357 vs AUX 351. So both count; très, plus, bien are ADV, and dossier l.87 lists adverbs. These five forms are 2.7 to 8.8% of content tokens in my texts; dropping them moves the mean by -0.05 to -0.23. One percentage point of density is 0.022 Zipf, so a 2-point difference equals the whole one-year effect.

A5 stands; link to requested age unchecked. [run] regarda 2.2 per million (Zipf 3.3) and répondit 2.9 (3.5) against regarde 613 (5.8); the lemma regarder is 6.1 for every form. Over the 298 commonest verbs: 3sg present 4.63, imparfait 3.41, passé simple 2.60. One story re-tensed to passé simple: form-based 5.02 to 4.52, lemma-based 5.41 to 5.44. No model outputs exist, so alignment with age cannot be checked. [inf] Part of the penalty is real difficulty, but grammatical, not rare words.

D15 partly stands. [run, 20,000 draws; my HC3 matches analyze.fit] Mechanism right: a prompt-cell SD of half the within SD (ICC 0.20) inflates the SE by 1.09 (theory sqrt(1+(k-1)rho)); cluster-robust SEs restore 2.9%. Size not reproduced. Holm-H2 null rate: 2.8% at baseline (authors' own run(), 8,000 draws, not 3.5%); 4.0 to 4.1% at ICC 0.20; 4.4% at ICC 0.25; 6.5% at k = 4. The unadjusted one-sided 5% test goes 5.0% to 6.6-7.1%. Even a prompt SD of 1.5 times the within SD gives 7.2%. Larger risk (extension, assumed SD 0.10): an effect shared by the six models (same prompt string) gives 14.4%.

D17 stands. analyze.py v0.1 l.83-84, 92 divide the six-model pooled contrast by the mean of significant slopes only; the dossier (l.100) and AsPredicted section 5 say per model. [run] Six rulers (-0.06 to -0.005), true shift 1.0 year each: analyze.py 0.76, per-model 0.99. No bootstrap exists (docstring l.13 only). The self-test (slope SD 0.01) cannot expose this.

E20 stands. [run] Six L5 texts per model: SE = 0.2/sqrt(25.3) = 0.040; through analyze.py's HC3 path, median 0.052, and per-model H1 rejects 9% at a true -0.04. pipeline.py sets k from the mean of three slopes (SD 0.024; 90% interval -0.079 to -0.002). With the authors' run() power grid: true -0.04 gives k=2 72%, k=4 24% (19% via the silent "choice or 4" fallback); true -0.02 (needs k=4) gives k=2 39%, power 0.68. The "H1 flat for 4 of 6 models" rule cannot be evaluated with three pilot models.

C11 partly stands. [inf] A flat L1 profile cannot separate "ignored" from "constant wrong level" without a baseline. But offset versus ignored is separable from L1 and L5 slopes (dossier l.48, l.159, exploratory), and the probe (l.22) covers knowledge. [arithmetic] With ages symmetric about 9, a flat L1 at the model's mid level gives pooled H2 = 0 despite +/-0.1 Zipf at the ends.

C12 stands. vd.ch (raw HTML, grep): "Premier cycle primaire (1P - 4P)", "Deuxième cycle primaire (5P - 8P)", "Degré secondaire (9S - 11S)"; no "HarmoS", no 1H to 8H. ge.ch (fetch tool; curl blocked): "le cycle élémentaire (1P à 4P) pour les élèves de 4 à 8 ans", "le cycle moyen (5P à 8P) pour les élèves de 8 à 12 ans". Contrast fr.ch: "les années de scolarité 1H à 11H". Dossier l.17 ("En Suisse romande ... 3H à 8H") overgeneralises. Official usage only; I did not check what teachers write.

Limits. The project moved while I worked. analyze.py (v0.1: 6,053 bytes, md5 2764d886, rewritten 16:00), design.json, make_prompts.py, calls*.jsonl and compute.py (rewritten 15:43-15:55) are now v0.2. My D15, D17 and E20 runs used analyze.py v0.1 and the design as the findings describe it; v0.2 is not audited. measures.py, sim_power.py and pipeline.py are unchanged. My texts are not model outputs. I opened the first 1.5 KB of review_report.md by accident (A1, A2 wording). My imports created /home/claude/art5/__pycache__; I deleted it.

Next action: when the pilot texts exist, re-score them with names, hyphens, aujourd'hui, ’ and lemma frequencies fixed, and cluster by prompt string, before fixing k.
````

## Lecture 3. Vérification des corrections (v0.2)

- Identifiant, a086027218acd0b04
- Modèle, claude-fable-5-1
- Heure, 25.10.2026, 16:34 à 16:49
- Version lue, v0.2
- Résultat en bref, corrections statistiques confirmées, 13 défauts N1 à N13 dont quatre bloquants
- Dossier de travail cité, scratchpad/probe/

### Consigne donnée (verbatim)

````text
You are checking whether a set of fixes really closes the findings of an earlier design review. You did not make the fixes. Begin your report with: "Internal reading by a separate AI session. Not peer review."

Context. ART 5 is a planned LLM audit (no data collected yet): six language models are asked to write French reading texts for Swiss primary pupils, with the grade named in different ways (bare HarmoS label "de 5H", P label "de 5P", label plus age, French grade, age only "de 8 à 9 ans", no level, and "de 3e/4e/5e" as a collision control). The outcome is the mean Zipf frequency of content lemmas (Lexique 3.83). An adversarial review found 24 problems in design v0.1 (the report is at /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/review_report.md). A refutation pass refuted none of them; D15 (prompt-level dependence) and C11 (no-level baseline) stood in weaker form, and the refuter added that a model which ignores the label and writes at its default level gives a pooled L1-L5 contrast near zero (texts too hard at 3H and too easy at 8H cancel).

What changed in v0.2 (the drafting session's claim; do not take it on trust): measure rewritten in compute.py (A1 to A7); one text per prompt with topics as the unit of inference and two-sided topic-level t-tests, Holm over four primary tests (level and gradient of L1-L5 and L1P-L5), D15/D16; age equivalents from each model's own linear L5 ruler with a size-based eligibility rule and a topic bootstrap, isotonic lookup kept only as sensitivity (B9, D17); new labels L1P, L0, L6 (C11, C12); finish reason, refusal definition and explicit temperature (C14); pilot of 72 age-only texts plus 18 blinded format-check texts and 36 probes, with a rule choosing 16, 24 or 32 topics by simulation (E20, E21); power simulation with controls including one that must fail (D18); preregistration draft (F23); construct renamed to lexical demand (B8, G24).

Files (read only, do not modify anything under /home/claude/art5): design.json, make_prompts.py, compute.py, analyze.py, sim_power.py, generate.py, pipeline.py, validate_measure.py, run.yml, PREREG.md, sim_power_results.json, all in /home/claude/art5. The lexicon is /usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt (latin-1 copy of Lexique 3.83). Copy the folder to your own temporary directory before running anything, and run Python there with plain python3 (the scripts import each other). Useful commands: python3 compute.py --self-test LEXICON; python3 analyze.py --self-test (about 15 s); python3 make_prompts.py and --pilot; python3 sim_power.py --pilot 0.3 -0.04 (quick). The full sim_power.py run takes about 10 minutes; you do not need to rerun it unless you doubt a number.

Your task.
1. For each finding A1 to G24 of the review, say fixed, partly fixed, not fixed, or no longer applicable, with the evidence (file and line, or the output of a command you ran). Check fixes against the code, not against comments or docstrings.
2. Try to break v0.2: write a few realistic French texts of your own (dialogue, names at sentence start, passé simple, elisions, hyphenated words) and check the measure behaves as the docstring of compute.py says; check that the analysis code computes what its docstring and PREREG.md say (the same statistic, the same sign, the same exclusions); check that PREREG.md matches the code; check that the pilot cannot leak the L1 or L1P measures (blinding) into any output.
3. List any new defect you find in v0.2, ranked by severity (must-fix, should-fix, minor), each with a concrete fix.
Keep the report under 1,200 words. Mark what you ran as [run] and what you inferred as [inf]. If you could not check something, say so in the first lines.
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review.

Not checked: anything needing the network (validate_measure.py against the wikis, model ids/prices, GitHub Action versions); the full sim_power.py grid was not rerun (one cell rechecked). Nothing under /home/claude/art5 was modified; work ran in a copy under the scratchpad.

**Verdict.** The statistics are fixed for real: topic-level tests, per-model rulers, bootstrap, must-fail control, and the code computes exactly what PREREG §5–7 says [run: brute-force recomputation of level(t) and gradient(t) with pandas on simulated data with missing pairs matches analyze.topic_stat to 1e-5; ttest matches scipy]. Blinding holds in code [run: fake pilot of 126 records; all 12 measure columns NaN for the 18 L1/L1P rows; pilot_summary.json carries only kept/reason/finish/truncated]. But the measure still has three artefacts of the size the review flagged in v0.1 (determiners, œ ligatures, "suis"), none caught by the golden tests, and the pilot cannot set T reliably. Fix the measure before the pilot, since the pilot's σ and slope decide T.

**1. Findings A1–G24**

- A1 fixed: compute.py:88 normalises ’ ‘; ELIDED:50 [run]. Caveat N7.
- A2 fixed with a hole: :130–139 [run: name control passes]; words after ":" or "«" become names (N4).
- A3 fixed: split_token:97–109 [run: dit-elle, demanda-t-il, s'écrièrent, va-t-il, Allons-y, Dis-le-moi, aujourd'hui, quelqu'un, c'est-à-dire, grands-parents all right].
- A4 partly: être/avoir by lemma (:48,177), ADV out [run: très/plus/bien/si not content]; but :75 `cgram.split(":")[0]` lets determiners in (N1) and "suis" → suivre (N3).
- A5 fixed: :80 mean of freqlemfilms2/freqlemlivres, smoothing 0.031 [run: tense control passes].
- A6 fixed: clean():90–93, sentences() per line.
- A7 fixed in form: GOLDEN:296–309 plus four controls [run: pass]; no golden text contains a determiner, œ or "suis", so N1–N3 pass unseen.
- B8 fixed: "lexical demand" in PREREG title, design.json, compute docstring; median/share<3/<4/word length secondary. README stale (G24).
- B9 fixed: linear per-model ruler analyze.py:292–309, linearity F :190–192, isotonic only as sensitivity :350.
- B10 fixed: length_residualised :410–417, used :483.
- C11 fixed: L0 design.json:52 [run: make_prompts 7,680 = 16×480 incl. 192 L0]; placed on ruler :308.
- C12 fixed: L1P primary, PRIMARY:68–69.
- C13 fixed: parse_probe/probe_correct :427–436, rule in PREREG §8 [run: 6 cases pass].
- C14 fixed with a gap: temperature 1.0 + fallback generate.py:172–181, finish_reason :182–186, refusal = finish reason (compute:59). Textual refusals (Mistral has no refusal finish reason) ≥20 words are kept (N9).
- D15 fixed: topic_stat/ttest :117–141; H1 and secondary OLS clustered by topic [run; sim C3 0.139 vs C4 0.048 from the json].
- D16 fixed: pairwise NaN, half-pairs/any-grade rule :127, counted; PREREG §6 [run: self-test 5].
- D17 fixed: ratio of sums over eligible models :334–338, size rule −0.02 :73, 2,000 topic resamples :340–349 [run: shift 1.15 for planted 1, CI 0.48–2.01].
- D18 fixed: binomial bound 0.0613 sim_power.py:41; C3 must-fail 0.139 > bound; C1 0.0435.
- D19 fixed: PREREG §5 "conditional on these six models"; H1 failures handled by eligibility and pilot stop rule.
- E20 partly: k=1 makes within/between moot and T is set from the pilot, but the pooled slope from 72 texts has SE σ/√210 = 0.021 at σ=0.3 [computed]: with a true slope of −0.04 the 80% range of the estimate is [−0.066, −0.014], so the chosen T swings 16↔32 on pilot noise and the flat-ruler stop rule (pipeline.py:84) fires falsely 17% of the time (23% at σ=0.4). See N5, N6.
- E21 fixed: stop rule evaluable; grid T∈{16,24,32} = PREREG; t(5) noise, 2% missing, prompt effects [run: --pilot 0.3 −0.04 → .46/.69/.85, grid says .452/.686/.866].
- E22 fixed: σ 0.15–0.4 in grid; pilot estimates σ with an upper 80% bound.
- F23 mostly fixed: PREREG §3/§6 state title rule, apostrophes, names, f=0, duplicates, truncation, seed, clustering, estimand, formula, parser, refusal, 20-word floor. Missing: collection window; "eligibility fixed on full data" (docstring only, :42); §3 says "adjective" while the code counts determiners (N1).
- G24 partly: README.md still describes v0.1 (5,760 texts, HC3, k, "harder texts").

**2. Attack results** are folded into the items above and below. Prompts [run: make_prompts main and --pilot] are grammatical for all eight labels and both probes; counts 7,680+720 and 72+18+36 as claimed.

**3. New defects**

Must-fix
- N1 Determiners counted as content. compute.py:75 truncates cgram, so ADJ:pos/dem/ind/int/num (mon, ma, ses, cette, ces, chaque, tous, deux, quelques, plusieurs: 198 forms, film mass 32k per million, three quarters of all true adjectives) enter at Zipf 5–6.5. [run] 8H informational text: 9 of 49 "content" tokens, mean 4.405 → 4.161 without them; 3H story 5.019 → 4.909. Genre- and grade-dependent. Fix: keep the full tag and require cat == "ADJ" exactly; add golden text with "ma sœur", "ces", "chaque".
- N2 œ/æ ligatures. Lexique spells coeur/soeur/oeil/oeuf; models write cœur/sœur/œil/œuf, which score OOV (1.49 instead of 5.2–5.9). One cœur per 100 content words = −0.04 = one "year". [run] 3H story with sœur ×2 and cœur: 5.019 → 5.445 after folding. Fix: fold œ→oe, æ→ae in the lookup key.
- N3 "suis" resolves to suivre (Lexique gives suivre 1,819/M for the form) and counts at Zipf 6.18 [run: 4 of 11 content tokens in a first-person 3H text]. Fix: exclude a form if any Lexique reading has lemma être/avoir.
- N5 design.json lists 24 topics; the T rule allows 32. make_prompts slices topics[:n_topics] and checks counts on the same slice, so n_topics=32 silently gives 24×480 = 11,520 texts and exit 0 [run]. Fix: add 8 topics or assert n_topics ≤ len(topics).

Should-fix
- N4 After ":" or "«" a capitalised word is non-initial, so it is a name, and it then poisons sentence-initial copies via noninitial_caps. [run] dialogue 3H text: Regarde, Attends, Venez, Donne, Mange, Joyeux dropped, −0.11 (≈2.7 "years"); dialogue density varies with grade. Fix: in analyse(), treat a token as initial when the gap before it contains : « " — – or a line start.
- N6 Pilot slope noise (E20). Fix: use the slope's conservative 80% bound in pilot_power as for σ, or 4–6 ruler topics (SE 0.015–0.012); make the stop rule a one-sided test.
- N7 validate_measure.py:94 calls measure() without clean(): the wikis' typographic apostrophes are not normalised, "c" (NOM 4.49) is counted [run]. The validated measure is not the deployed one. Fix: move ’ normalisation into analyse().
- N8 Blinding is code-only: run.yml:56 commits data/raw with the 18 L1/L1P texts and output_tokens, and uploads them. Fix: write format_check records to a file excluded from the commit until G1, or say in PREREG §1 that the raw texts were stored unopened.
- N9 Textual refusals (C14). Fix: pre-registered opening-phrase regex counted as refusal, applied before any measure.
- N10 design.json "analysis" still says three primary tests, Holm over three, L3 vs L1 primary; contradicts PREREG §5 and analyze.PRIMARY.

Minor
- N11 retry_list lists only ok records; transport failures and empty responses get no second request within the step, contrary to PREREG §6.
- N12 Title rule drops the first sentence of a titleless short-line 3H text [run]; a "Texte :" line is measured. Fix: strip only a first line without terminal punctuation; drop ^(titre|texte)\s*:$.
- N13 Stale text: README (v0.1), make_prompts docstring "L6 for 3H to 6H" (design says 3H–5H), PREREG missing a collection window. Form-level lemma ambiguity ("vit" → voir) remains an accepted, documented limit [inf].

Next action: fix N1–N3 and N5 in compute.py/design.json, extend GOLDEN with a text containing ma sœur, ces, je suis, cœur and a colon-quote, rerun --self-test and the pilot power once with the conservative slope.

Scratch: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/probe/ (p1–p3.py, fake_pilot.py, mp32/) and .../scratchpad/verify/ (copy with fake pilot outputs).
````

## Lecture 4. Réfutation de N1 à N13 (v0.2)

- Identifiant, afb95676e5f8883f3
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 16:51 à 17:08
- Version lue, v0.2
- Résultat en bref, aucun constat réfuté
- Dossier de travail cité, scratchpad/refute_work/

### Consigne donnée (verbatim)

````text
Begin your report with: "Internal reading by a separate AI session. Not peer review."

A separate AI session reviewed version v0.2 of a research pipeline and raised the findings below. Your job is to try to refute each one: check it against the code and data, and answer "refuted", "stands" or "partly stands", with the evidence (file and line, or the output of a command you ran). If you cannot check a finding, say so. Do not fix anything.

Context. ART 5 is a planned audit (no data yet) where six language models write French reading texts for Swiss primary pupils, with the grade named in different ways. The outcome is the mean Zipf frequency of content lemmas computed by compute.py from Lexique 3.83. Analysis is in analyze.py, simulation in sim_power.py, workflow glue in pipeline.py and run.yml, the plan in design.json and make_prompts.py, the preregistration draft in PREREG.md, a measure-validity check against Vikidia and Wikipedia in validate_measure.py.

Files (frozen copy, read only): /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/v02_frozen/ . Copy that folder to your own new temporary directory before running anything, and run Python there with plain python3 (the scripts import each other). Lexicon: /usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt (latin-1 copy of Lexique 3.83, read it with compute.load_lexicon or pandas). Useful: python3 compute.py --self-test LEXICON; python3 make_prompts.py; python3 analyze.py --self-test (about 15 s). The wikis are not reachable from this environment.

Findings to test:
N1. Determiners counted as content: compute.py keeps only the part of the Lexique tag before ":", so ADJ:pos, ADJ:dem, ADJ:ind, ADJ:int and ADJ:num forms (mon, ma, ses, cette, ces, chaque, tous, deux, quelques) count as content words at Zipf 5 to 6.5, moving a text's mean by about 0.1 to 0.25.
N2. Ligatures: Lexique spells coeur, soeur, oeil, oeuf; models write cœur, sœur, œil, œuf, which are scored as absent from the lexicon (Zipf about 1.49 instead of 5 to 6).
N3. The form "suis" resolves to the lemma suivre and is counted as a content word, because the single most frequent Lexique row for "suis" is suivre, although être's rows together are more frequent.
N4. A capitalised word right after ":" or "«" inside a sentence is treated as a name, and then its sentence-initial copies elsewhere also become names, so dialogue verbs like « Regarde ! » drop out of the measure.
N5. design.json lists 24 topics while the topic rule allows 32; make_prompts.py slices topics[:n_topics] and checks counts on the same slice, so n_topics = 32 silently yields 24 topics and exits 0.
N6. The pilot's pooled slope from 72 age-only texts has a standard error of about 0.021 at sigma 0.3, so the topic-count decision and the flat-ruler stop rule (slope above -0.02) are driven by noise (false stop about 17% when the true slope is -0.04).
N7. validate_measure.py calls compute.measure() without compute.clean(), so typographic apostrophes in wiki text are not normalised and the validated measure is not the deployed one.
N8. The pilot blinding is code-only: run.yml commits data/raw, including the 18 blinded L1/L1P texts, and uploads them as artifacts.
N9. Refusals are defined only by finish reason; a textual refusal or a request for clarification of 20 words or more would be kept and measured.
N10. design.json's "analysis" block still describes three primary tests with Holm over three and L3 vs L1 as primary, contradicting PREREG.md and analyze.PRIMARY.
N11. compute.retry_list only lists answered calls; calls that failed at transport level or returned empty text get no second request within the step, contrary to PREREG.md section 6.
N12. The title rule drops the first line of a text whenever it has 12 words or fewer, so the first sentence of a titleless text written one short sentence per line is lost.
N13. Stale text: make_prompts.py docstring says L6 exists for 3H to 6H while design.json says 3H to 5H; PREREG.md has no data-collection window.

Keep the report under 800 words, one line or two per finding, marking what you ran as [run] and what you inferred as [inf].
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review.

Result: all 13 findings stand; none refuted. N6's 17% is specific to sigma 0.3, and N7's impact could not be checked (wikis unreachable). Untagged = read in the code, [run] = executed in a copy, [inf] = inferred. Magnitudes come from 8 short French texts I wrote myself (not audit outputs), so they are illustrative.

N1 stands. [run] mon, ma, ses, cette, ces, chaque, tous, deux, quelques resolve to cat ADJ (compute.py:75) at Zipf 5.56-6.49 (152 forms in all). Excluding them moves my 8 texts' means by 0.00-0.26 (median 0.10; stories 0.09-0.26, informational 0.00-0.11). [inf] Genre- and topic-dependent, so it can leak into contrasts, not just add noise.

N2 stands. [run] Lexique has 0 forms with the ligature (195 with "oe"); cœur, sœur, œil, œuf(s), bœuf, œuvre, nœud, vœu score 1.49, against 4.2-5.9 for the oe spellings. Two samples lose 0.20 and 0.25; sentence-initial "Œufs"/"Cœur" are dropped as names. [inf] The latin-1 copy has no "?" or U+FFFD, so the official file very likely spells oe too (lexique.org unreachable).

N3 stands, small. [run] lex["suis"] = suivre (Zipf 6.18): row 2403.4 vs être 1832.8 + 678.5 = 2511.2. Among the 88 forms with an être/avoir row it is the only real misresolution. [inf] About +0.02 per occurrence at 60 content words.

N4 stands, mid-sentence openings only. [run] "Léa cria : « Regarde le ciel ! »" makes Regarde a name, and every sentence-initial "Regarde" with it; « at sentence start and dash dialogue are fine. Dialogue-heavy story: 5 of 52 content words lost, mean -0.054.

N5 stands. [run] n_topics = 32: exit 0, 11,520 text calls, 24 topics (32 would give 15,360); pipeline.py has no guard.

N6 stands, conditional on sigma. [run] The pipeline.py:77 formula on 72 texts from sim_power's generator (4,000 draws): SE 0.0205 (analytic 0.0207). False stop at true -0.04 is 16.5% at sigma 0.3, but 4.6% at 0.15, 9.6% at 0.20, 24.6% at 0.40. At sigma 0.3 the grid picks T = 16, 32 or none for slopes -0.06, -0.04, -0.02. [inf] Sampling alone gives sigma about 0.08-0.11; the real value is unknown until the pilot.

N7 stands as a code fact. validate_measure.py:94 skips clean() (deployed: compute.py:227). [run] With a typographic apostrophe, "aujourd'hui" becomes aujourd (absent) + hui and "c'est" gives c (counted): toy sentence 4.18 vs 4.49. Apostrophe rate in wiki HTML not checkable here.

N8 stands. run.yml:56 commits data/raw, :70 uploads it. [run] /home/claude/art5/.gitignore (outside the frozen copy) ignores only data/lexicon/ and caches; README says raw outputs are published. PREREG section 1 is literally true (measures blanked), but the texts are readable.

N9 stands. [run] A 36-token refusal and a 44-token clarification request with finish_reason "stop" are kept and measured; only under 20 tokens or over 50% non-French is excluded. PREREG section 6 uses the same finish-reason definition, so the gap is in the spec.

N10 stands. design.json:79-80 (three tests, L3 vs L1 primary) vs PREREG sections 5 and 8 and analyze.py:68 (four tests, L3 secondary). [run] No code reads design["analysis"]: documentation only.

N11 stands, partly mitigated. [run] On a synthetic raw file retry_list omits the status-500 and the 200/empty-text records. generate.http retries 6 times on 408/429/5xx/URLError, and a manual re-run re-requests ok=False calls (unbounded, logged as attempt 1). [run] An empty-text refusal (ok=False) is labelled "failed call" and never retried.

N12 stands, narrow. [run] A titleless one-sentence-per-line text loses its first line; a preface line ("Voici une histoire ... :") becomes the title and the real title is measured. Only outputs without a title are hit.

N13 stands, both parts. make_prompts.py:7 says 3H to 6H; design.json:53, PREREG.md:43, analyze.py:51 say 3H to 5H. [run] grep: PREREG.md has no collection window, only {PILOT_DATE}.

Not checked: wiki text, official Lexique file, real model outputs, GitHub Actions behaviour (YAML only read). compute.py and analyze.py self-tests pass. Nothing in the frozen folder or /home/claude/art5 was changed; scripts and sample texts are in /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/refute_work/.

Next action: fix N5, N1, N2 and N4 first (they silently change the sample or the outcome measure), add one golden case each to compute.py, then re-freeze before tagging prereg.
````

## Lecture 5. Confirmation des corrections (v0.3)

- Identifiant, a626c2db760db0f98
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 17:16 à 17:44
- Version lue, v0.3
- Résultat en bref, 12 corrections confirmées, N9 en partie, nouveaux défauts D1 à D5, restes R1 et R2
- Dossier de travail cité, scratchpad/v03_check/

### Consigne donnée (verbatim)

````text
Begin your report with: "Internal reading by a separate AI session. Not peer review."

You did not write these fixes. Your job is to confirm or reject each one by checking the code and running it, not by reading comments.

Context. ART 5 is a planned audit (no data yet) in which six language models write French reading texts for Swiss primary pupils. The outcome is the mean Zipf frequency of content lemmas computed by compute.py from Lexique 3.83. A review of version v0.2 raised 13 findings, all confirmed by a refutation pass. Version v0.3 claims to fix them. The v0.2 files are frozen in /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/v02_frozen/ ; the v0.3 files are in /home/claude/art5/ (read only; copy the folder to your own new temporary directory before running anything, run Python there with plain python3, and do not modify /home/claude/art5). Lexicon: /usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt. Earlier sessions left sample French texts and scripts you may reuse in /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/refute_work/ and .../scratchpad/probe/ (read only).

The findings and the claimed fix for each:
N1 determiners (ADJ:pos, ADJ:dem, ADJ:ind, ADJ:int, ADJ:num) counted as content. Claimed fix: full Lexique tag kept, only plain ADJ counts.
N2 ligatures œ, æ scored as absent (Lexique writes oe). Claimed fix: normalise() folds œ to oe and æ to ae before lookup.
N3 "suis" read as suivre. Claimed fix: each form is read as the lemma with the largest summed form frequency, then that lemma's most frequent row.
N4 capitalised words after ":" or "«" inside a sentence treated as names. Claimed fix: a token after a colon, an opening quote or a dash counts as initial.
N5 n_topics larger than the topic list silently truncated. Claimed fix: 32 topics listed and make_prompts.py fails if n_topics exceeds the list.
N6 pilot slope too noisy to set the number of topics and to trigger the flat-ruler stop. Claimed fix: pilot ruler of 216 texts (six topics), topic count chosen for a fixed 0.04 Zipf difference at the pilot's sigma upper 80% bound, stop rule = one-sided test of the pooled slope at p > .05 (pipeline.py pilot_summary).
N7 validate_measure.py skipped clean(). Claimed fix: it now calls compute.clean().
N8 blinding only in code. Claimed fix: the pilot no longer requests any L1 or L1P text; only age-only texts and 36 probes (answers stored, accuracy not computed).
N9 textual refusals kept. Claimed fix: compute.REFUSAL_RE, an anchored list of refusal and clarification phrases, excludes them.
N10 design.json analysis block stale. Claimed fix: rewritten to four primary tests.
N11 transport failures and empty answers not retried within a step. Claimed fix: pipeline.run_calls reruns the same call file once when the first pass had failures and was not stopped.
N12 first line of a titleless text dropped, and a preface line taken as the title. Claimed fix: title rule requires no final period, label lines are removed, leading lines ending with a colon are dropped.
N13 stale docstring and no collection window. Claimed fix: docstring corrected, PREREG.md section 4 states a window.

For each, answer "confirmed", "partly" or "not fixed", with evidence ([run] for commands you ran, file:line for code you read). Then list any new defect introduced by v0.3 (for example a refusal phrase that would exclude ordinary children's texts, a title rule that drops real text, a change that breaks the analysis self-test or make_prompts counts), ranked by severity with a concrete fix. Useful commands: python3 compute.py --self-test LEXICON; python3 analyze.py --self-test; python3 make_prompts.py and --pilot. Keep the report under 700 words.
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review.

Scope: v0.3 read and run in a copy under /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v03_check/ (scripts/), with pylexique's Latin-1 Lexique383.txt. Not tested: lexique.org's official tsv (host unreachable), the wikis, real model outputs, GitHub Actions. Texts are invented; magnitudes are illustrative. [run] = executed. Both self-tests exit 0; make_prompts gives 7,680+720 and 216+36 (shipped call files identical). compute's self-test catches 9 of 10 mutants (undo of N1-N4, N9, N12; smoothing constant); the miss is REFUSAL_RE match changed to search. One scratch `rm` was blocked by the safety check; not retried, fresh directories used; /home/claude/art5 untouched.

Verdicts
N1 confirmed. [run] 152 forms (num 106, ind 24, pos 15, int 4, dem 3) are now non-content (compute.py:94); means of 8 sample texts move -0.004 to -0.219. Residual: D4.
N2 confirmed. [run] œ texts score like their oe spellings (5.162=5.162; 4.972=4.972; v0.2 lost 0.20 and 0.25). Caveat D2.
N3 confirmed. [run] suis reads as être; 160 of 125,652 forms change lemma (suis the only high-frequency one); all readings equal an independent argmax.
N4 confirmed. [run] "Léa cria : « Regarde" no longer yields a name; a dialogue story equals its lower-cased control (5.416; v0.2 5.327). A spaced " - " dash is still missed.
N5 confirmed. [run] n_topics 32 gives 15,360 calls; 33 exits 1 (make_prompts.py:74-76).
N6 confirmed, caveat. [run] pilot_summary runs on 216 synthetic texts (flat or reversed ruler stops). Monte Carlo: false stop at true slope -0.04 is 0.1% (sigma .15), 0.3% (.20), 8% (.30), 21% (.40).
N7 confirmed. [run] validate_measure.main calls clean() 60 times (validate_measure.py:94); real wiki text untested.
N8 confirmed. [run] calls_pilot.jsonl: 216 L5 texts, 36 probes, no other label.
N9 partly. [run] REFUSAL_RE flagged only 5 of 18 invented refusals, all opening with a listed phrase; the earlier "Merci pour votre demande... pouvez-vous préciser" case is still kept and, in a mock pipeline, not retried. See D1.
N10 confirmed, documentation only. [run] constants match analyze.py and pipeline.py; nothing reads design["analysis"].
N11 confirmed. [run] mock API: of 5 failures the same-file rerun recovered 3; a refusal went through the retry list; a budget-stopped pass triggered no rerun. See D5.
N12 confirmed for the claimed cases. Residual: a first line ending ? or ! is still dropped; a preface without a final colon is still taken as the title or kept as text.
N13 confirmed (make_prompts.py:7; PREREG.md:52), but README.md:5,12,14 still say v0.2 and "pilot 72 + 18 + 36".

New defects, by severity
D1 (medium) REFUSAL_RE (compute.py:69-74, 242). Recall: misses prefaced or rephrased answers (Merci..., m'indiquer, me dire, Malheureusement). Precision: it tests the raw start including the title, so 6 of 6 constructed ordinary texts titled "Désolé, petit lapin", "Je ne peux pas dormir" and similar were excluded (real rate unknown, likely small). The pilot has no bare-label answers, so the list cannot be tuned before the freeze. A leaked clarification scores 4.91 against 5.0-5.3 for stories, so each leak biases little. Fix: test the first body sentence after title removal; allow a short preface; add the missing forms; add a vous/votre rule outside quotes with a preregistered manual screen blind to Zipf; self-test both directions.
D2 (medium if triggered, one-line fix) The fold applies to text, not lexicon keys. [run] A lexicon spelling œ passes the self-test (exit 0) while ligature texts lose 0.23-0.27; the official tsv's spelling is unverified. Fix: normalise() ortho and lemme on load; assert share_oov is 0 on a sœur/cœur golden text.
D3 (low) `marked` is read from raw[0] before label and preface removal (compute.py:118,128). [run] "**Texte**", "## Texte" or a bold preface before a titleless body drops its first body line; v0.2 kept it. Fix: carry markedness per line.
D4 (low) tous/toute/toutes (lemma tout, plain ADJ, Zipf 6.49), autre and mêmes still count; removing them moves 3 of 8 texts by -0.02 to -0.03. Fix: add tout, autre, même to EXCLUDED_LEMMAS and re-pin.
D5 (low) pipeline.py:65-72 gives each of up to three runs the full cap (cap_usd 1.0 in all three logs), so a step can spend 3x --max-cost. Fix: pass cap minus summed spent_usd.

Next action: fix D2 and D1, rerun both self-tests, then re-freeze.
````

## Lecture 6. Réfutation de D1 à D5, R1 et R2 (v0.3)

- Identifiant, ac38a015650cb9bcc
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 17:46 à 18:02
- Version lue, v0.3
- Résultat en bref, D1 à D5 maintenus au moins en partie, R1 réfuté pour l'exemple donné, R2 maintenu mais peu plausible
- Dossier de travail cité, scratchpad/v03_refute/

### Consigne donnée (verbatim)

````text
You are a refutation reader for a research-code audit. Your job is to try to REFUTE seven findings that another AI session reported on version 0.3 of a measurement pipeline. Do not fix anything. Start your report with the line "Internal reading by a separate AI session. Not peer review."

## Context (brief)
ART 5 is an audit of language models: models write French reading texts for pupils, and the primary measure is the mean Zipf frequency of content-word lemmas per text, using Lexique 3.83. compute.py does cleaning (clean), tokenisation and name rules (analyse, split_token), the measure (measure), exclusions (exclusion_reason with REFUSAL_RE) and has a self-test. pipeline.py runs model calls through generate.py with a budget cap. Read the module docstring of compute.py first; it states the intended rules.

## Files (your own copy, edit nothing outside your folder)
- Code: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v03_refute/art5/ (compute.py, pipeline.py, generate.py, make_prompts.py, design.json, calls_pilot.jsonl)
- Lexicon: /usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt (Latin-1, tab-separated; compute.load_lexicon reads it). If that path does not exist, search under /usr/local/lib for Lexique383.txt.
- Put your scripts in /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v03_refute/scripts/ . Do not delete files anywhere; create new files instead. No network access is available (lexique.org is unreachable).

## Findings to try to refute (as reported)
D1. REFUSAL_RE (compute.py, applied in exclusion_reason) (a) misses refusals or clarification requests that open with a preface or a rephrasing, e.g. "Merci pour votre demande ! Pouvez-vous préciser…", "Pourriez-vous m'indiquer…", "Pouvez-vous me dire…", "Malheureusement, je…"; (b) is tested on the raw start of the answer, title included, so ordinary texts whose title opens with a listed phrase ("Désolé, petit lapin", "Je ne peux pas dormir") are excluded as refusals; (c) the self-test does not fail if REFUSAL_RE.match is changed to REFUSAL_RE.search.
D2. normalise() folds œ/æ to oe/ae in texts, but load_lexicon does not fold the lexicon's ortho or lemme keys; so if a lexicon file spelled "cœur", ligature words in texts would become out-of-lexicon, and the self-test would still pass. (Say what spelling the available Lexique file uses for coeur/soeur/oeuvre, and whether the claim "self-test passes with a ligature-spelled lexicon" holds when you build such a lexicon copy.)
D3. In clean(), whether the first line is a marked title is decided from raw[0] before label lines and prefaces are removed, so an answer like "**Texte**" or "## Texte" or a bold preface line, followed by a body with no title, loses its first body line.
D4. tous/toute/toutes (lemma tout), autre(s) and même(s) are still counted as content words because their top reading is tagged plain ADJ, which raises the mean; removing them changes typical texts by about -0.02 to -0.03 Zipf.
D5. pipeline.run_calls passes the full --max-cost cap to each of up to three generate.py passes (first pass, transport rerun, retry list), so one step can spend up to three times the cap. Check generate.py too: does it count money already spent in earlier passes (for example from earlier log files) before applying the cap?
R1 (residual of an earlier fix). analyse() treats a capitalised word after a colon, an opening quote or a dash as sentence-initial, but a spaced hyphen-minus used as a dialogue dash (" - Regarde !") is not recognised, so the word after it is counted as a name.
R2 (residual). clean() drops a first line of at most 12 words that ends with "?" or "!" as a title, even when the text has no title; and a preface line that does not end with a colon ("Voici une histoire pour des élèves de 8 à 9 ans.") is kept as text or taken as the title.

## What to do
For each item, write and run the smallest script that could show the claim is false (and if it is not false, the run is your evidence). Judge also whether the scenario is plausible for real outputs of current chat models given the prompt "Écris {une histoire à lire | un texte documentaire à lire} pour des élèves {label}, sur le thème {topic}. Réponds seulement avec un titre et le texte." Mark plausibility as your inference, not as a fact. Where the reported magnitude is checkable, recompute it.

## Report format (keep it under 600 words)
For each of D1a, D1b, D1c, D2, D3, D4, D5, R1, R2, one line: verdict (holds | refuted | holds in part), evidence tagged [run] or [reasoning], and the magnitude you measured. Then at most three lines on any risk you see in the obvious fix (for example a fix for D1b that would let real refusals through). Do not propose a full redesign.
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review.

Folder has prompts only, no model outputs, no network: plausibility calls are inference. Baseline self-test OK. Scripts: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v03_refute/scripts/

D1a: holds. [run] 8 openers escape REFUSAL_RE: your four, plus "Je ne comprends pas", "Je ne suis pas sûr de comprendre" and tu forms ("Pourrais-tu préciser"; the prompt says "Écris"). Short ones (6-11 words) are still caught as "under 20 words" and retried, so only the label changes; a 39-word clarification is kept (mean Zipf 4.89). Rare, label-correlated (inference).

D1b: holds. [run] "# Désolé, petit lapin" and "**Je ne peux pas dormir**" are excluded as refusal; "Titre : Je suis désolé…" is not. A handful of 7,680 texts at most, each retried (inference).

D1c: holds in part. [run] Self-test exits 0 with .search, but that mutant is equivalent: the pattern starts with ^ (0 of 200,000 strings differ). Real gap: dropping ^ as well also passes, and would exclude 4 of 5 ordinary dialogue stories ("Je suis désolé" in speech). The "kept" control has no text key, so the regex never runs on a kept text.

D2: holds in part. [run] The available file spells coeur, soeur, oeuvre with "oe"; zero rows contain œ or æ. A ligature-spelled copy (156 rows) passes the self-test, because an unknown token is recorded as its own lowercase form, which equals the expected "soeur"/"coeur". Cost: -0.06 to -0.14 Zipf per ligature token. Latent: the workflow's UTF-8 .tsv can't be checked offline.

D3: holds in part. [run] Six no-title variants ("**Texte**", "## Texte", bold preface, …) lose the first paragraph: 74 to 49 words, Zipf 5.220 to 5.194. Needs a title-less answer, unlikely given "un titre et le texte" (inference).

D4: holds in part. [run] Counted: tous/toute/toutes (ADJ, lemma tout, Zipf 6.49), autre, mêmes. Not counted: tout (ADV), autres (PRO:ind), même (ADV), so "autre(s), même(s)" is mostly wrong. Removal: -0.029 on 16 proxy texts I wrote knowing the finding (0 to -0.061), but -0.010 to -0.014 at Lexique corpus rates (1.0-1.1% of content tokens): -0.02/-0.03 is the high end. An offset: it matters only if the rate differs by label or grade (not tested).

D5: holds. [run] generate.py starts spent at 0.0 on each call and reads only answered call_ids from data/raw, never cost_usd or logs (grep). Mock provider through the real run_calls, cap 1.05: three passes of 1.00 = 3.00 (2.86 times the cap). If pass 1 stops on the cap, pass 2 is skipped but the retry pass gets a fresh cap (1.82 times). Realistic overshoot is the cost of failed plus excluded calls (inference).

R1: refuted for the stated example. [run] A line- or sentence-initial " - Regarde !" is the first token, so initial. Holds only for a mid-sentence spaced hyphen before a capital ("Léa dit - Regarde !"), about 0.02 Zipf at 60 content words [reasoning].

R2: holds, low plausibility. [run] (a) Untitled text opening with a question or exclamation of 12 words or fewer loses it (-0.03 in a 74-word text). (b) Preface without colon is kept as text (+0.019) or taken as the title while the real title is measured (+0.007). Both need the model to ignore "Réponds seulement…".

Fix risks:
- D1b: testing the cleaned body lets 4 of 5 realistic two-line refusals through, since clean() drops a short refusal first line as a title [run].
- D1a: generic openers ("Malheureusement", "Merci") recreate D1b's false positives.
- D4: a lemma stoplist is a researcher degree of freedom, so fix it before the pilot.

Side effect: art5/__pycache__ (my first import); no source edited.
````

## Lecture 7. Confirmation des corrections (v0.4)

- Identifiant, aad05b1fca8b0d365
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 18:28 à 18:59
- Version lue, v0.4
- Résultat en bref, D1 à D4 et R1 confirmés, D5 tel que décrit, R2b en partie, nouveaux constats V1 à V5 (V1 moyen, sur la dépense)
- Dossier de travail cité, scratchpad/v04_check/

### Consigne donnée (verbatim)

````text
You are a separate reader confirming fixes in a research pipeline. You did not write the code and must not assume the fixes work. Start your report with the line "Internal reading by a separate AI session. Not peer review."

## Context
ART 5 audits language models: models write French reading texts for primary pupils ("Écris {une histoire à lire | un texte documentaire à lire} pour des élèves {label}, sur le thème {topic}. Réponds seulement avec un titre et le texte."). The primary measure is the mean Zipf frequency of content-word lemmas per text (Lexique 3.83). compute.py cleans answers (edge_lines, clean_info, clean), decides refusals (is_refusal_text, exclusion_reason), flags answers that address the user (flag_meta), and measures (analyse, measure). Its module docstring states the rules. pipeline.py runs generate.py passes under a budget. PREREG.md is the preregistration text that must describe the code.

Version 0.4 fixes these findings from an earlier reading of v0.3 (all were upheld by a refutation session):
- D1: refusal detection missed rephrased refusals ("Merci pour votre demande ! Pouvez-vous préciser…", "Malheureusement, je…", tu forms) and excluded ordinary texts whose title opened with a listed phrase ("Désolé, petit lapin", "Je ne peux pas dormir"). v0.4: specific phrases tested at the start of the first two lines, after an optional polite opener; a title-like first line is skipped only when at least 20 words follow.
- D2: ligatures were folded in texts but not in lexicon keys. v0.4: ortho and lemme are folded on load; control with a lexicon spelled "cœur".
- D3: the title mark was read from the raw first line before label lines were removed. v0.4: each line keeps its own mark.
- D4: tout, autre, même (tagged plain ADJ by Lexique) counted as content words. v0.4: excluded lemmas.
- D5: each of three generate.py passes got the full --max-cost. v0.4: --max-cost is the budget of the whole plan, counted from logs/run_*.json over passes and earlier runs.
- R1: a hyphen between spaces mid-sentence was not read as a dialogue dash. v0.4: INITIAL_GAP_RE also matches it.
- R2b: a preface without a final colon was kept as text. v0.4: preface and closing lines addressed to the user are removed (PREFACE_RE, VOICI_RE with AUDIENCE_RE, POSTFACE_RE), counted in n_meta_lines. (R2a, an untitled text whose first line ends with ? or !, is a declared limitation, not fixed.)

## Files (your own copy; do not edit anything outside your folder, do not delete files, no network)
- Code: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v04_check/art5/
- Lexicon: /usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt (Latin-1, tab-separated)
- Mock providers for pipeline tests: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/exp/mock_providers.py (run it on a free port and set ART5_ENDPOINT_OVERRIDE=http://127.0.0.1:PORT plus dummy API keys; see e2e_v04.sh in the same folder for the setup, but run in your own folder)
- Put your scripts in /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v04_check/scripts/

## What to do
1. For each of D1 to D5, R1 and R2b, check with a run that the reported failure no longer occurs, including at least two cases the self-test does not already contain.
2. Look for regressions introduced by the v0.4 rules. Write at least 15 realistic answers of the kind current chat models give to the prompt above (stories with dialogue in « » and with dashes, documentary texts that address pupils with "tu" or "vous", texts opening with "Voici", texts ending with a moral or a question to the reader, markdown titles, bullet lists), and report any genuine text line that is removed or any genuine text that is excluded or flagged. Say which of your answers are plausible and which are edge cases (inference).
3. Check that PREREG.md sections 3, 6 and 8 describe what the code does for the changed rules, and say where they differ.
4. Revert three of the fixes in a copy and confirm that compute.py --self-test fails each time.
5. Run pipeline.run_calls against the mock with a small plan budget, twice in a row, and confirm the total spent never exceeds the budget.

## Report (under 500 words)
One line per item D1 to D5, R1, R2b: confirmed, partly or not fixed, with [run] evidence. Then any new defects ranked by severity, each with a one-line magnitude and whether a realistic answer triggers it. Then the PREREG check and the revert check in two lines.
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review.

Scripts (tN_*.py) and answers.py: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v04_check/scripts/ ; mock runs: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v04_check/e2e/

D1 to D5, R1, R2b
- D1 confirmed. [t1] 13/13 new rephrasings excluded (incl. tu forms, Merci opener). Kept: title "Malheureusement, je suis petit", second line "Désolé, petit ours".
- D2 confirmed. [t2] UTF-8 Lexique copy spelled with œ: same measures; without folding OOV 0.30. (Supplied file lacks ligatures.)
- D3 confirmed. [t3] 12/12 label and mark layouts.
- D4 confirmed. [t4] tous, toutes, mêmes excluded.
- D5 confirmed as specified. [e2e] Provided mock, cap 0.6: retry pass got 0.4292 after 0.1708 spent; total 0.19 after two runs. Heavy-usage mock, cap 0.8: 0.7616 spent, reruns 0.0000. Runs stop ~0.4 USD below cap. Hole: N1.
- R1 confirmed. [t5] "dit - Viens vite": Viens counted, not a name.
- R2b partly. [t10] Listed wordings removed; kept as text: "Voici une histoire sur les lapins." (no audience word); "Dites-moi…" flagged only.

Answers: 49 written; plausible S01-S15, D01-D10, P01-P08 (33), edge E01-E15, S16 (16); my inference, no model sampled. Plausible: 0 genuine lines removed, excluded, flagged or mis-titled. Edge: 5 genuine lines removed, 2 texts excluded, 3 flagged, 2 mis-titled.

New defects (ranked)
N1 Medium. A crashed generate.py writes no run log, so its spend is uncounted. [e2e] Uncaught IncompleteRead (mid-body disconnect): two runs at --max-cost 0.8 spent 1.30 USD. Plausible over 8,400 calls (inference). Untested fix: sum cost_usd from data/raw; catch Exception in http().
N2 Medium-low. Clarifications with an unlisted opener ("Pour écrire…", "Que signifie", "Navré") stay as texts: 12/12 variants kept, 6 flagged; tu forms never flagged. One shifts a mean under 0.001 Zipf (inference), but a model clarifying systematically on bare labels would bias the contrast and the §8 rate. Possible, unobserved.
N3 Low. "---" after a preface becomes the title; after a closing line it blocks removal. These were the only failures in a 15,120-layout factorial of mainstream shapes (6,480 and 1,680); needs a preface or closing line. Fix verified in a copy: skip lines without letters in edge_lines (self-test OK, 15,120/15,120).
N4 Low. Rare genuine lines read as refusal: first body line "Qu'entends-tu…", "Peux-tu dire…", "Malheureusement, j'…" (6/17 constructs, 0/33 plausible). Also a refusal first line lacking final punctuation, followed by 20+ words not opening with a listed phrase, is kept as the "title".
N5 Low. Over-removal: opening "Voici Tom, un élève de CM1…" drops its paragraph; last line "Note :". Up to 0.11 Zipf on 40 to 60-word edge texts. Rare.

PREREG: sections 3, 6, 8 match the code on every changed rule. Gaps: §6 "reads as a title" is undefined (code also rejects ! ? :); §6 omits the dash-dialogue skip and vous-only META_RE; §3 says "addressed to the user" but any Note line goes; the budget rule is absent.
Reverts: [t7] 7/7 reverts (D1 twice, D2, D3, D4, R1, R2b) make --self-test exit 1; control exits 0. 7 of 10 finer mutants survive (incl. tu forms).
````

## Lecture 8. Confirmation étroite des corrections (v0.4.1 (generate.py mis à jour pendant la lecture, 81bc955a))

- Identifiant, aa0068f00eed2165b
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 19:22 à 20:02
- Version lue, v0.4.1 (generate.py mis à jour pendant la lecture, 81bc955a)
- Résultat en bref, V1 confirmé après la mise à jour (0 dépassement sur 39 essais), V3 et V4 confirmés, V2 et V5 en partie, constats W1 à W5 dont un reste de V1 (réponses illisibles qui arrêtent l'exécution) et une régression du correctif V4 (demandes en tu sans « me »)
- Dossier de travail cité, scratchpad/v041_check/

### Consigne donnée (verbatim)

````text
You are a separate reader confirming a small set of fixes in a research pipeline. You did not write the code. Start your report with "Internal reading by a separate AI session. Not peer review." Keep the scope narrow: confirm these fixes and look for regressions they cause, nothing else.

## Context
ART 5 audits language models that write French reading texts for primary pupils. compute.py cleans answers (edge_lines, clean_info), excludes refusals (is_refusal_text), flags answers that address the user (flag_meta) and measures them. generate.py calls the providers, and pipeline.py enforces a budget per plan. The module docstrings state the rules. Version 0.4.1 answers a reading of v0.4 that found:
- N1 (medium): a crashed generate.py wrote no run log, so its spend was not counted, and an uncaught IncompleteRead could crash it. Fix: http() catches every exception and counts attempts that may have been billed at the model's worst case (cost_usd_possibly_charged), one() never lets an error stop the run, and pipeline.spent_on counts money from the raw records (prefix of the call ids), not from the logs.
- N2: clarifications with unlisted openers stayed as texts. Fix: "navré" added to the refusal phrases; flag_meta also flags "peux-tu/pourrais-tu me préciser…", "dis-moi", "j'aurais besoin de savoir…", and a question line that names the grade label or the school system (LABEL_Q_RE).
- N3: a "---" line became the title or blocked the removal of closing lines. Fix: lines without letters are dropped in edge_lines.
- N4: rare genuine lines read as refusals ("Qu'entends-tu…", "Peux-tu dire…", "Malheureusement, j'ai…"). Fix: narrower patterns (tu forms need me or m', "qu'entends-tu par", malheureusement followed by je ne, j'ignore and similar).
- N5: over-removal of "Voici Tom, un élève de CM1…" and of any closing line starting with Note. Fix: a Voici line is a preface only if it opens "Voici une histoire/un texte…" or states the intended readers ("pour des élèves", "adapté", "destiné", "au niveau"); a Note line is removed only if it is about the text or its readers. Also new: "(Environ 80 mots)" and "Dites-moi…" closing lines are removed.

## Files (your own copy; do not edit or delete anything outside your folder; no network)
- Code: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v041_check/art5/
- Lexicon: /usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt
- A battery of 49 hand-written answers from the previous reader, with its harness: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v04_check/scripts/answers.py and t6_battery.py (run t6_battery.py with your code folder as argument, from your own working folder, since it writes battery_results.json in the current directory)
- Mock providers: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/exp/mock_providers.py and mock_bad.py (mock_bad cuts two 200 responses mid-body). Run them on a free port with ART5_ENDPOINT_OVERRIDE=http://127.0.0.1:PORT and dummy keys ANTHROPIC_API_KEY, OPENAI_API_KEY, MISTRAL_API_KEY.
- Your scripts go in /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v041_check/scripts/

## What to do
1. For N1 to N5, show with a run that the reported failure no longer occurs, with at least one case per item that the self-test does not contain.
2. Run the 49-answer battery and report its plausible and edge summaries.
3. Write 10 new realistic answers aimed at the new rules (documentary texts with "Note :" boxes about the subject, stories opening with "Voici", texts with "---" separators, texts addressing pupils with "tu" questions, texts mentioning "en 5H" inside the story) and report any genuine line removed, any genuine text excluded or flagged. Mark plausibility as your inference.
4. For N1, run pipeline.run_calls twice against mock_bad with a small plan budget and confirm that the money counted from the raw records never exceeds the budget, and that no run crashes.

## Report (under 350 words)
One line per item N1 to N5: confirmed, partly or not fixed, with [run] evidence. Battery summary in one line. New defects ranked by severity with a one-line magnitude and whether a realistic answer triggers it.
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review. Evidence: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v041_check/

N1, v0.4.1: partly. [mock_bad] v0.4 exits 1 (IncompleteRead), no log; two runs at budget 0.8 count 1.33. v0.4.1 exits 0 in 39/39 runs. [kill -9, budget 3.0] v0.4 believes 0.0 spent, ends 3.92; v0.4.1 believes 1.005, ends 2.96. But counted money exceeded the budget in 5/20 runs (up to +0.04): a cut attempt plus its retry costs two reservations; at 30/60/90% cuts 1.74/2.08/2.66 against 1.2.
N1, update (81bc955a): confirmed. 0/39 over (stress 1.17/1.18/1.14); no record above its reservation (v0.4.1: 6x); 39/39 crash-free.
N1 residual: HTTP-200 bodies with null token counts, non-string content (OpenAI/Mistral) or a lone surrogate still stop one() (3 of 9 shapes; exit 1, no log). In-flight calls at a kill (~0.4 USD) go uncounted.
N2: partly. Navré excluded (not "Navré de vous décevoir"); 10/12 other unlisted-opener clarifications flagged (v0.4: 3), none excluded.
N3: confirmed. 603 layouts, 11 separator kinds: v0.4 392 wrong, v0.4.1 0.
N4: confirmed for Qu'entends-tu, Peux-tu dire, Malheureusement j'ai.
N5: partly. "Voici Noah…" kept; "(Environ N mots)" and "Dis-moi…" removed, other word-count layouts stay; subject Notes survive only without a trigger word.

Battery: plausible 33: 0 removed, left in, mis-titled, excluded, flagged; edge 16: 3 removed, 3 flagged, 0 excluded (v0.4: 5, 3, 2). Ten new answers: genuine lines removed 4, excluded 0, flagged 3.

New defects by severity (realistic/rare is my inference):
1. N1 overshoot above (fixed by the update); a dropped connection near the cap triggers it: realistic.
2. N4 narrowing: 6 of 8 tu clarifications v0.4 excluded (no "me": "Pourrais-tu préciser…") now stay texts, 5 flagged. Realistic (prompt in tu).
3. N5 Note filter: niveau, histoire, mots, phrases, lecture or élèves anywhere removes a subject note (2/10 answers); text notes lacking them stay. Rare.
4. False flags (flag only): "degré", "8 h" or "5H" plus "?" (2/10); "Peux-tu me dire…", "Dis-moi…" (1/10, closing "Dis-moi…" line also removed); 0/33 earlier. Water, snow, train, school topics.
5. Rare: untitled "Voici…" paragraph with destinée/adaptée/au niveau dropped whole (-0.058 Zipf); "Malheureusement, il n'y a pas…" and "Navré, le…" first lines excluded.
````


## Lecture 8, deuxième tour. relecture des corrections v0.4.2

- Identifiant, aa0068f00eed2165b (même session, reprise par un message)
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 20:22 à 20:45
- Version lue, v0.4.2 (compute.py 1f5742c8c36b24a8, generate.py 4680bda30be1d520)
- Résultat en bref, W1, W2 et W4 confirmés, constats X1 à X5
- Dossier de travail cité, scratchpad/v041_check/work/

### Consigne donnée (verbatim)

````text
Narrow follow-up: please confirm or reject the v0.4.2 fixes of your findings W1, W2 and W4 (your numbers 1, 2 and 4), nothing else. Start your report with "Internal reading by a separate AI session. Not peer review." Keep it under 500 words, tag [run] for what you executed and [inf] for inference, and do not modify anything outside your own folder.

Code (read-only copy): /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v042_for_reader/art5 (compute.py 1f5742c8c36b24a8, generate.py 4680bda30be1d520). Changes: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v042_for_reader/v0.4.1_to_v0.4.2.diff. Copy what you need into your own folder.

What changed, and what to check:
1. W1 (generate.py). After parse(), a 200 answer whose token counts are missing or not numbers, or whose text is not a string, raises inside the try: the record is failed, the original body is kept under unreadable_response, and the attempt is counted at the worst case of its model. A lone surrogate is replaced in the text, and the raw line falls back to ASCII-escaped JSON if it cannot be encoded. finish_reason and model id that are not strings become null. Please rerun your malformed-body shapes on both routes, and one or two of your cut-response or stress budget runs, to see that the budget accounting did not regress. The uncounted in-flight calls at a kill -9 are out of scope (declared limitation).
2. W2 (compute.py, REFUSAL_RE). "(pourrais|peux)-tu (me |m')?(préciser|clarifier|indiquer|confirmer)" no longer needs "me"; "(pourrais|peux)-tu (me |m')(donner|expliquer|dire (ce que|ce qu'|à quel|quel|quelle|l'âge))" still needs it; added "dis-moi (ce que|ce qu'|à quel|quel|quelle|l'âge)", "tu veux dire (ce que|ce qu'|à quel|quel|quelle)", and "qu'entends-tu (exactement |vraiment )?par". Please rerun your N2/N4 cases, and write a few genuine opening lines that start with these new phrases, to see whether any genuine text is now excluded.
3. W4 (compute.py, flag_meta). The label question is now tested sentence by sentence (a sentence that ends with "?" and names a label), the grade pattern "\b\d+\s?[HP]\b" is case-sensitive, and "degré" matches only the singular. Please check that your false flags are gone and that real label questions ("Que signifie 5H ?", "Quel âge ont les élèves de 5P ?", a question naming HarmoS or the school system) are still flagged.
4. Rerun your 49-answer battery and your ten new answers for regressions.

Out of scope: W3, W5, and everything else (they are listed for the human gate G1).
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review. Hashes match the brief. Evidence: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v041_check/work/

W1, generate.py: confirmed, one gap.
- [run] 46 runs (22 malformed-200 shapes plus a clean control, 2 routes): 0 stops, 12/12 raw records each, no unreadable line. Earlier update: 9 stops, 2 silent early stops.
- [run] Null usage, null, string, negative, boolean or infinite counts, and non-string content now give a failed record at exactly 1.00x its reservation, JSON body kept (non-JSON: exception text only). Through pipeline.run_calls (cap 3.0): exit 0, the 3 failed calls re-asked in pass 2, 252/252 ok.
- [run] Budget not regressed: 32 run_calls runs (20 repetitions at caps 0.5 and 1.2, 12 cut, stress or mock_bad runs), all exit 0, none over the cap; closest 1.193 of 1.2 (update 0/39, v0.4.1 5/20 over). No raw record above its reservation (3,047 checked).
- [run] Gap, same as the earlier update: usage absent or {} is accepted at cost 0 (output count absent: input cost only), because parse() defaults to 0. [inf] Rare (providers send usage), but the undercount is unbounded.
- [run] A lone surrogate in the model id passes generate.py, then stops compute.py at the CSV write. [inf] Same for finish_reason; contrived.

W2, REFUSAL_RE: confirmed, at a cost.
- [run] tu clarifications excluded 10/10 (v0.4.1: 2/10). My 16 genuine N4 texts behave as in v0.4.1.
- [run] Cost: 18 genuine openings I wrote with the new phrases ("Peux-tu indiquer sur la carte...", "Dis-moi ce que tu vois...") are all excluded (v0.4.1: 1/18); I judge 8 plausible [inf]. 12/12 common hooks and dialogue lines are not excluded.
- [run] "quel" has no word boundary: "Dis-moi quelque chose" and "Tu veux dire quelque chose ?" are excluded (3/3). [inf] Add \b; applying these openers only to answers under about 60 words would remove most false exclusions.

W4, flag_meta: confirmed, with a trade-off.
- [run] False flags gone, 6/6 (zéro degré, 5H x2, "8 h" x2, "20 degrés"). Ten new answers: wrongly flagged 3 to 1 (N08, via META_RE).
- [run] Still flagged: "Que signifie 5H ?", "Quel âge ont les élèves de 5P ?", HarmoS, système scolaire (9/12 variants; v0.4.1: 11/12).
- [run] Newly missed: label and "?" in different sentences (0/6; v0.4.1: 6/6), e.g. "Pour la 5H, il me faut plus d'informations. Quel âge ont les élèves ?"; lower-case "5h". None of my 12 earlier clarifications lost its flag (META_RE alone 5, label rule alone 3, both 2, neither 2). [inf] Loss limited to clarifications with no other cue; frequency unknown.
- [run] Still falsely flagged when label, singular "degré", "8H" or HarmoS shares the question's sentence (5/5).

Regressions: [run] 49-answer battery identical to v0.4.1 (33 plausible clean; 16 edge: 3 removed, 3 flagged, 0 excluded). Ten new answers: 4 genuine lines removed (as in v0.4.1), 0 excluded. N3 and N5 tables identical. Author's self-test passes.
````

## Lecture 8, troisième tour. relecture des corrections v0.4.3

- Identifiant, aa0068f00eed2165b (même session, reprise par un message)
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 20:51 à 21:06
- Version lue, v0.4.3 (compute.py a24472f501d4e52e, generate.py 7ce38baa5b8f397e)
- Résultat en bref, X1 à X3 confirmés, effet Y1 sur « à quelle », « quels » et « quelles », notes Y2 et Y3
- Dossier de travail cité, scratchpad/v041_check/work/

### Consigne donnée (verbatim)

````text
Last narrow follow-up: please confirm or reject three small v0.4.3 fixes of the gaps you reported on v0.4.2, nothing else. Start with "Internal reading by a separate AI session. Not peer review." Keep it under 250 words, tag [run] and [inf], do not modify anything outside your own folder. This is the last round. Anything else you notice goes to the human gate G1 as a listed limitation, so please report it rather than propose redesigns.

Code (read-only copy): /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v043_for_reader/art5 (compute.py a24472f501d4e52e, generate.py 7ce38baa5b8f397e). Changes: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v043_for_reader/v0.4.2_to_v0.4.3.diff. The main session's extended copy of your mock (four shapes added: usage_missing, usage_empty, model_surrogate, finish_surrogate) is in the same folder as mock_weird.py if useful.

1. W1 gap, usage absent or {}: parse() now returns None for a token count the provider did not send, so the answer is a failed record counted at the worst case. Please rerun your usage-absent and usage-{} shapes on both routes, and one of your budget or cut runs for regressions.
2. Lone surrogate in the model id or the finish reason: both are now passed through the same replacement as the text. Please rerun your case that stopped compute.py at the CSV write.
3. "quel" boundary: a word boundary now follows the alternatives of "dis-moi (...)", "tu veux dire (...)" and "(pourrais|peux)-tu (me |m')(donner|expliquer|dire (...))". Please rerun "Dis-moi quelque chose", "Tu veux dire quelque chose ?" and your 10 tu clarifications.
4. Rerun the 49-answer battery and your ten new answers for regressions.
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review. Hashes match the brief. Evidence: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v041_check/work/

1. Usage absent or {}: confirmed.
[run] 50 runs (25 shapes, both routes; the main session's mock agrees): usage absent, {} and output count absent now give a failed record at 1.00x its reservation; 40 other rows unchanged. Through pipeline.run_calls: exit 0, 3 failed calls re-asked, 252/252 ok.
[run] 32 budget runs (20 repetitions, cuts, mock_bad): all exit 0, none over the cap; no record above its reservation (3,029 checked).

2. Surrogate in model id or finish reason: confirmed.
[run] Both become "?"; compute.py exits 0 (v0.4.2 raw files still stop it at the CSV write, finish reason too).

3. "quel" boundary: confirmed, with collateral.
[run] "Dis-moi quelque chose" and "Tu veux dire quelque chose ?" are kept; 10/10 tu clarifications still excluded.
Limitation [run]: "à quelle", "quelles", "quels" no longer match. 6/10 probe clarifications are now flagged, not excluded, e.g. "Peux-tu me dire à quelle classe correspond 5H ?" (excluded in v0.4.1 and v0.4.2).

4. Regressions: none. [run] Battery identical to v0.4.2 (33 clean; 16 edge: 3 removed, 3 flagged, 0 excluded); ten new answers identical; N3/N5 tables identical; self-test OK.

Other limitations for G1:
- [run] A provider that never sends usage fails every call: 69 calls, 0 ok, 2.965 of 3.0 spent, exit 0. [inf] Theoretical.
- [run] compute.py itself is not hardened: v0.4.2 raw files stop it.
````

## Lecture 8, quatrième tour. relecture du correctif v0.4.4

- Identifiant, aa0068f00eed2165b (même session, reprise par un message)
- Modèle, claude-sonnet-5-5
- Heure, 25.10.2026, 21:07 à 21:09
- Version lue, v0.4.4 (compute.py 8ad7a56512616c64, generate.py inchangé)
- Résultat en bref, correctif de Y1 confirmé, aucune régression
- Dossier de travail cité, scratchpad/v041_check/work/

### Consigne donnée (verbatim)

````text
One-item follow-up on your v0.4.3 collateral finding, and truly the last: please confirm or reject the v0.4.4 fix, nothing else. Start with "Internal reading by a separate AI session. Not peer review." Under 150 words, [run]/[inf] tags, nothing modified outside your folder.

Code (read-only): /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v044_for_reader/art5 (compute.py 8ad7a56512616c64; generate.py unchanged from v0.4.3). Diff: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v044_for_reader/v0.4.3_to_v0.4.4_compute.diff. The alternatives after "dis-moi", "tu veux dire" and "(pourrais|peux)-tu (me |m')dire" are now (ce que|ce qu'|à quel(le)?s?|quel(le)?s?|l'âge) followed by \b.

Please rerun: your 10 probe clarifications (the 6 with "à quelle", "quels", "quelles" should be excluded again); "Dis-moi quelque chose" and "Tu veux dire quelque chose ?" (should stay kept); your 10 tu clarifications; the 49-answer battery and your ten new answers for regressions.
````

### Rapport final (verbatim)

````text
Internal reading by a separate AI session. Not peer review. Hashes match the brief (compute.py 8ad7a565; generate.py unchanged). Evidence: /tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v041_check/work/w2_v044_out.txt

v0.4.4 fix: confirmed.
- [run] 10/10 probe clarifications are excluded again (v0.4.3: 4/10), including the six with "à quelle", "quelles", "quels"; 10/10 tu clarifications still excluded.
- [run] "Dis-moi quelque chose", "Tu veux dire quelque chose ?", "Peux-tu me dire quelques noms", "quelqu'un", "quelquefois" stay kept.
- [run] Cost, as in v0.4.2: my genuine hooks "Dis-moi à quelle heure...", "quelles couleurs...", "quels animaux..." are excluded again (3/3; v0.4.3: 0/3).
- [run] No regression: battery identical (33 clean; 16 edge: 3 removed, 3 flagged, 0 excluded); ten new answers and N3/N5 tables identical; self-test OK.
````
