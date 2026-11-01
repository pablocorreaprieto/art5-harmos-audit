# Gate G2 (1.11.2026, evening): journal-ladder research and check reading

Kept verbatim, as the protocol asks (rule 11). Four separate sessions launched by the main session
(claude-opus-5-5): three research sessions on the journal ladder (19:55 to about 20:25) and one check reading
of the G2 changes (about 20:40 to 21:00). All four ran on claude-sonnet-5-5, read only, with no provider API
call. Their findings were checked by the main session before use (see the journal's Historique tab and
`../findings_log.csv`, rows G1 to G12). In the anonymised copy this folder is left out, because the briefs
describe the author.

## 1. Research session A, hybrid journals

### Brief (verbatim)

You are researching journals for a first publication. Web research only (WebSearch, WebFetch). Do not write files, do not use any browser, do not touch Google Drive or email.

THE ARTICLE (ART 5): a preregistered audit (AsPredicted, 1 Nov 2026) of six large language models (Anthropic, OpenAI, Mistral, via their APIs) that wrote 7,680 French reading texts for primary-school pupils. Prompts named a Swiss grade label ("de 5H", "de 5P") or the matching age; the outcome is lexical demand (mean lemma frequency, Zipf scale, Lexique 3.83). Main result: labels gave texts close to the age's lexical demand on average, with model-specific departures. English manuscript, ~5,800 words plus tables, open data and code. Single author: an independent researcher (primary teacher in the canton of Vaud, Switzerland), no institution, no funding. The study was largely carried out by an AI assistant (Claude) under the author's written protocol: the AI worked out the design details, wrote the code, ran the analyses and drafted the text; this is fully disclosed; the author conceived the topic and the protocol, built the infrastructure, made design decisions and takes full responsibility.

GOAL: the author wants a FIRST publication, FAST, with the HIGHEST REALISTIC chance of acceptance, in a LEGITIMATE journal (indexed in Scopus or Web of Science incl. ESCI; real peer review; not predatory). He will submit down a ladder of 5. No publication fee is strongly preferred (subscription route of a hybrid journal is fine; note any charge). English submissions.

ALREADY EXCLUDED: BJET, Journal of Computer Assisted Learning, L1-Educational Studies in Language and Literature (95% rejection), Swiss Journal of Educational Research, Computers & Education, IJAIED, any Elsevier journal (Elsevier's AI policy limits AI to readability).

YOUR CLUSTER (hybrid journals of Taylor & Francis, Springer, SAGE, Emerald): Computers in the Schools; Journal of Research on Technology in Education; Interactive Learning Environments; Educational Media International; Technology, Pedagogy and Education; Journal of Digital Learning in Teacher Education; Reading Psychology; Literacy Research and Instruction; Reading & Writing Quarterly; Journal of Research in Childhood Education; TechTrends; Education and Information Technologies; Technology, Knowledge and Learning; Journal of Computers in Education; Journal of Educational Computing Research; Interactive Technology and Smart Education; Australian Journal of Language and Literacy. Add up to 3 others you find that fit better.
Taylor & Francis "about this journal" pages (tandfonline.com/journals/<code>/about-this-journal) list "% acceptance rate" and "days avg. from submission to first decision"; use them. Springer pages may list acceptance rate or median days to first decision.

ALSO VERIFY the AI policies of Taylor & Francis, Springer Nature, SAGE and Emerald: does each allow substantial AI use in design, analysis and drafting if disclosed and the author is accountable, or does it restrict AI to language editing? Quote the key sentence with URL.

RULES: Take acceptance rates only from the journal's or publisher's own pages or official reports; give the exact quote, the year and the URL. Never estimate silently; write "not published" when absent, and "blocked" for pages you could not open. Mark your own judgments [inference].

OUTPUT (under 1,000 words): (1) a table, one row per journal: name, publisher, indexing (Scopus/WoS, with source), fee, acceptance rate (value, year, URL), days to first decision, review model, word limit, scope fit 1-5 with a short reason; (2) the four AI policies with quotes and URLs; (3) your top 3 for this author's goal, with reasons; (4) what you could not verify.

### Report (verbatim)

Read 1 Nov 2026. tandfonline.com refuses automated fetches, so T&F figures come from the same pages on the publisher mirror informahealthcare.com/journals/<code>/about-this-journal; none states a year (JRCE's says "the last full calendar year" [inference: 2025]). All journals read are hybrid; no mandatory fee found. "–" = not stated on the page read; blocked = page unopenable. Fit scores are my judgment [inference].

**(1) Journals**

| Journal (publisher, code) | Indexing | Acceptance | Days to 1st decision | Review; words | Fit |
|---|---|---|---|---|---|
| Computers in the Schools (T&F wcis20) | Scopus, WoS ESCI | "25% acceptance rate" | "29 days avg." | – | 4 K-12 technology, teacher-author |
| J Research on Technology in Education (ISTE/T&F ujrt20) | – | "approximately 10%" (ISTE page) | "two to four months" (review target) | "between 4,000 and 8,000 words" | 3 ed-tech |
| Interactive Learning Environments (T&F nile20) | blocked | blocked | blocked | 2 anonymous referees | 3 ed-tech |
| Educational Media International (T&F remi20) | blocked | blocked | blocked | 2 anonymous referees | 2 media focus |
| Technology, Pedagogy and Education (T&F rtpe20) | blocked | blocked | blocked | 2 anonymous referees | 3 ed-tech |
| J Digital Learning in Teacher Education (ISTE/T&F) | – | – | – | blind; "4,000-6,000 words" excl. references | 2 teacher education |
| Reading Psychology (T&F urpy20) | Scopus | "42% acceptance rate" | "103 days avg." | 2 anonymous referees | 3 reading |
| Literacy Research and Instruction (T&F ulri20) | blocked | blocked | blocked | anonymous referees | 3 literacy |
| Reading & Writing Quarterly (T&F urwl20) | blocked | blocked | blocked | – | 3 literacy |
| J Research in Childhood Education (T&F ujrc20) | Scopus, WoS ESCI | "26% acceptance rate" | "21 days avg." | double-anonymized | 3 primary education |
| TechTrends (Springer 11528) | blocked | blocked | blocked | peer-reviewed | 3 practitioner ed-tech |
| Education and Information Technologies (Springer 10639) | Scopus, SSCI; JIF 7.2 (2025) | not published | median 29 | – | 4 LLMs in education are core [inference] |
| Technology, Knowledge and Learning (Springer 10758) | Scopus, ESCI; JIF 4.2 (2025) | not published | median 24 | "blind"; 4,500-8,000 words incl. references, tables | 3 ed-tech |
| J Computers in Education (Springer 40692) | blocked | blocked | blocked | – | 3 ed-tech |
| J Educational Computing Research (SAGE) | Scopus, SSCI; JIF 8.5 (year not shown) | not on page | not on page | double-anonymized; "no more than 10,000 total words, including references"; "no fees payable to submit or publish" | 3 ed-tech |
| Interactive Technology and Smart Education (Emerald) | JIF 8.8 (2025) | "6.9%" (year not shown) | "49.3 days" | double anonymous | 2 AI policy bars ART 5 |
| Australian J of Language and Literacy (Springer 44020) | Scopus, ESCI; JIF 1.1 (2024) | not published | median 9 | – | 3 literacy |
| Other: Reading and Writing (Springer 11145) | Scopus, SSCI; JIF 2.3 (2025) | not published | median 3 | – | 2 human reading processes |

Page URLs: link.springer.com/journal/<id>; uk.sagepub.com/en-gb/afr/journal/journal-educational-computing-research; journals.sagepub.com/author-instructions/jec; emerald.com/ITSE; iste-ascd.org/journal-of-research-on-technology-in-education; iste-ascd.org/journal-of-digital-learning-in-teacher-education; link.springer.com/journal/10758/updates/17231096.

**(2) AI policies** (all undated, read 1 Nov 2026)
- **T&F**, https://taylorandfrancis.com/our-policies/ai-policy/: conditional. Supports "Idea generation and idea exploration" and "Coding assistance", but "does not permit the use of Generative AI in the creation or manipulation of outputs of research or clinical testing, for example, research results". Bars "Text or code generation without rigorous revision". Also "some journals may not allow use of Generative AI tools beyond language improvement", so read each journal's Instructions for authors. [inference] AI-run analysis could be read as AI-created results; ask the editor first.
- **Springer Nature**, https://www.springer.com/us/editorial-policies/artificial-intelligence--ai-/25428500 (redirects to a cookie page; same text read at https://link.springer.com/journal/13036/updates/27838868): permissive. "Use of an LLM should be properly documented in the Methods section"; "there must be human accountability for the final version of the text". Barred: AI authorship, AI-generated images.
- **SAGE**, https://www.sagepub.com/journals/publication-ethics-policies/artificial-intelligence-policy: permissive with disclosure. AI content affecting "methodology, analysis, results and/or conclusions must be disclosed upon submission"; "submissions will not be rejected solely because of the disclosed use of GenAI tools". Caution: inappropriate use includes "Generation of data or submission using a series of prompts" [inference: state that the LLM outputs are the object of study].
- **Emerald**, https://www.emerald.com/publish-with-us/pages/publication-ethics: effectively language editing only (plus translation, visualisation). Not permitted: "Copywriting (creating, drafting, or writing) any part of a submission", "Generating, manipulating, or reporting research data and results", "Generating code for the research through author-inputted prompts". ART 5 would breach it.

**(3) Top 3**
1. **Computers in the Schools**: published 25% and 29 days, Scopus plus ESCI, K-12 scope suits a primary-teacher author. Email the editor about the T&F AI clause first.
2. **Education and Information Technologies**: Springer's policy is among the friendliest, median 29 days, Scopus plus SSCI, broad scope where LLM-in-education studies are routine [inference]. No rate published and JIF 7.2, so odds unknown.
3. **Journal of Research in Childhood Education**: fastest published figures (26%, 21 days), double-anonymized (anonymize repository links), weaker fit, same T&F clause.
Safety rung: Reading Psychology (42% but 103 days). JECR is fee-free and policy-friendly, but JIF 8.5 hints at selectivity [inference]. Skip ITSE (policy, 6.9%) and JRTE (about 10%). Nothing I found fits better than rows 1 and 2.

**(4) Not verified**
Blocked: T&F pages for ILE, EMI, TPE, LRI, RWQ, and the T&F-side JRTE and JDLTE pages; Springer home pages for TechTrends and JCE. Not published: Springer acceptance rates; JECR rate and speed. Unchecked: "–" cells, Clarivate and Scopus lists, T&F word limits. First fetches of tandfonline.com and link.springer.com were refused by the permission layer; Springer pages opened only after their URLs surfaced in search results.

## 2. Research session B, diamond open-access journals

### Brief (verbatim)

You are researching journals for a first publication. Web research only (WebSearch, WebFetch). Do not write files, do not use any browser, do not touch Google Drive or email.

THE ARTICLE (ART 5): [as in brief 1, same paragraph]

GOAL: the author wants a FIRST publication, FAST, with the HIGHEST REALISTIC chance of acceptance, in a LEGITIMATE journal (indexed in Scopus or Web of Science incl. ESCI; real peer review; not predatory). He will submit down a ladder of 5. No publication fee strongly preferred. English submissions (French or Spanish journals are acceptable only if they take English manuscripts).

ALREADY EXCLUDED: BJET, Journal of Computer Assisted Learning, L1-Educational Studies in Language and Literature (95% rejection), Swiss Journal of Educational Research, Computers & Education, IJAIED, Contemporary Educational Technology (13% acceptance in 2025), Australasian Journal of Educational Technology and Educational Technology & Society (very selective), any Elsevier journal.

YOUR CLUSTER (diamond or society open-access journals): Canadian Journal of Learning and Technology; Research in Learning Technology (ALT); Journal of Applied Learning and Teaching (JALT); Journal of Interactive Media in Education; Electronic Journal of e-Learning; Digital Education Review; Education in the Knowledge Society; Open Praxis; Language and Literacy (Canada); Formation et profession; Médiations et médiatisations; Revista Interuniversitaria de Investigación en Tecnología Educativa (RIITE); Edutec; Contemporary Issues in Technology and Teacher Education (CITE Journal); Journal of Information Technology Education: Research; Journal of Learning Analytics. Add up to 3 others that fit better (for example journals on AI in education, literacy or primary education with published acceptance rates).
Many Spanish and Latin American journals publish acceptance or rejection rates (FECYT/Latindex requirement), often on "estadísticas", "indicadores" or "about" pages, or in annual editorials; OJS journals sometimes publish statistics pages. Look for them.

RULES: Take acceptance rates only from the journal's own pages or official reports (editorials, annual reports); give the exact quote, the year and the URL. Never estimate silently; write "not published" when absent, and "blocked" for pages you could not open. Check each journal's own policy on generative AI if it has one (quote + URL). Mark your own judgments [inference].

OUTPUT (under 1,000 words): (1) a table, one row per journal: name, publisher, indexing (Scopus/WoS, with source), fee, acceptance rate (value, year, URL), time to first decision, review model, word limit, scope fit 1-5 with a short reason, AI policy (if any); (2) your top 3 for this author's goal, with reasons; (3) what you could not verify.

### Report (verbatim)

**Legend.** S = Scopus, E = WoS ESCI, NP = not published on the pages I opened, BL = blocked, [i] = my inference. Indexing, fees and policies are the journal's own statements unless noted. Checked 1 Nov 2026.

**(1) Table** (URLs are paths under the base URL in the first cell)

| Journal (publisher), base URL | Indexing | Fee | Acceptance rate | 1st decision | Review, words | Fit | AI policy |
|---|---|---|---|---|---|---|---|
| **EKS** (U. Salamanca) revistas.usal.es/tres/index.php/eks | E ("indexada en el … ESCI"); S not stated | none (DDH listing: "No fees") | NP | review "no será superior a 3 meses" | ≥2 Scientific Committee members, anonymous; 7,500 incl. refs (checklist says 10,000); ES/EN | 4 tech-mediated education | none found |
| **RLT** (ALT) journal.alt.ac.uk/index.php/rlt | S+E, CiteScore 6.5 (/indexing) | free (/apc) | NP. ALT-J 2005 data: "total acceptance rate of about 40%" (/article/download/968/1219) | NP | double-blind; 6,000 incl. tables, captions, refs, over = desk reject | 4 primary to HE | "should set this out clearly in the acknowledgement section" (/guidelines) |
| **DER** (U. Barcelona) revistes.ub.edu/index.php/der | S+E | free | NP | "within six months of submission"; calls "restricted to January and June" | double-blind, 2 external; words NP; EN/ES | 4 | none found |
| **EJEL** (ACPI) academic-publishing.org/index.php/ejel | S+E | GBP 600 + 20% VAT, after acceptance | NP (2025 stats image unreadable) | "approximately 6 weeks, with a maximum of three months" | double-blind ≥2; 8,000 incl. refs | 3 | "it must be declared within the paper" (/about/submissions) |
| **CJLT** (CNIE/U. Alberta) cjlt.ca/index.php/cjlt | S+E | free | NP. 2005 editorial: "approximate acceptance rate of 34%" (/article/download/26470/19652) | "within 20 days of receipt" to decline/send out; final "within nine months" (/en/peer_review) | ≥2 reviewers; 5,000–6,500 incl. refs; EN/FR | 4 | bans "Generation of substantial conceptual or scientific text (including abstracts, methods, results, or discussions)"; "rejection or retraction" (/libraryFiles/downloadPublic/35) |
| **Open Praxis** (ICDE) icde.org/open-praxis | S+E, CiteScore 4.7 | "diamond"; DDH "No fees" | NP | BL | BL | 3 open/distance ed. | BL |
| **JITE:R** (Informing Science Inst.) informingscience.org/Journals/JITEResearch | S+E (/IndexedIn) | "one-time publication fee of USD 75" for non-members, after acceptance | NP | NP | desk + double-blind; words NP | 3 | none found |
| **CITE** (AACE/SITE) citejournal.org | S/WoS not stated (lists ERIC, EBSCO) | free | "the current acceptance rate for CITE Journal is 29%" (/?p=1821, undated, site ©2026) | NP | peer review; words NP | 3 teacher-ed tech | none found |
| **JALT** (Kaplan) journals.sfu.ca/jalt | S (Kaplan page) | free | NP | avg "15 weeks" to pre-publication | double-blind ≥2; 10,000 excl. tables/refs | 2 higher-ed focus | "Authors should be transparent when chatbots and other artificial intelligence (AI) are used" |
| **JLA** (SoLAR) learning-analytics.info/index.php/JLA | S+WoS (/faq) | free | NP | "first review round complete within six weeks" | blind; 9,000 (8,000 in /about/editorialPolicies) | 2 | none found |
| **JIME** (OU) jime.open.ac.uk | – | optional £555 + VAT | NP | NP | closed to general submissions; higher-ed scope | 1 | "refer to the publisher's guidelines" |
| **RIITE** (U. Murcia) revistas.um.es/riite | none shown (Latindex, MIAR logos): ineligible [i] | free | /estadisticas: "65%" 2024, "47%" 2023 (counts 18/34, 20/43 don't reproduce them) | 63 days 2024, 71 days 2023 | blind; 5,000–6,000 excl. refs; ES/EN | 4 | declare tasks, but "no la creación autónoma de contenido" (/politica-IA) |

Also checked. L&L (Canada): ProQuest/EBSCO only, so ineligible. F&P: French only ("textes soumis en français"). M&M (Téluq): FR/EN/ES, double-blind per a third-party directory, no S/E evidence. Edutec: own site unreachable.

Extra (outside cluster): **JETOL** (DergiPark). Fee: "No fee is charged from the author or institution under any name". Own stats, accepted share: 57% (2022), 60% (2023), 55% (2024), 65% (2025). Scope: "particular focus on artificial intelligence". S/E unconfirmed, AI policy unread. Its sister **JOLTIDA** (ESCI) is out: 100 EUR/USD submission fee and "The author may not use generative AI … to create datasets, analyze and evaluate data" (dergipark.org.tr/en/pub/joltida/price-policy, /page/16820).

**(2) Top 3**
1. **EKS**: shortest stated review deadline among free, in-scope journals (3 months), English accepted, no AI rule, 7,500 words fits. Caveats: ESCI only, committee-style review.
2. **RLT**: strongest metrics among free, in-scope journals, double-blind, disclosure-only AI rule. Must cut to 6,000 words including tables and references. Probably the most selective [i].
3. **DER**: free, S+E, English, AI-silent, but calendar-bound and up to six months, so not fast [i]. If speed outranks cost, swap in EJEL (about 6 weeks, fee only after acceptance, disclosure-only AI rule).

[i] Only CITE (undated) and RIITE (ineligible) publish a rate, so "highest chance" is judgment. ART 5's AI-drafted text collides with CJLT and JOLTIDA, and arguably RIITE. Disclosure-only policies (RLT, EJEL, JALT) are safest. Drop CJLT, JIME, JLA, JALT.

**(3) Not verified**
- BL: openpraxis.org/about/submissions (Open Praxis timing, length, AI policy); jalt.journals.publicknowledgeproject.org; erudit.org/en/journals/media (bot check); DOAJ pages for RLT and Open Praxis.
- EJEL's academic-publishing.org/public/site/images/suenugus/ejel-2025-submission-statistics.jpg (may hold its rate) could not be read or fetched.
- Scopus status of EKS and CITE; WoS for JALT; word limits for DER, CITE and JITE:R.
- Edutec, M&M and F&P facts come from third parties or partial pages.

Memory-worthy (source: journals' own pages, 1 Nov 2026): ART 5 candidate rungs are EKS, RLT, DER (EJEL as paid fast fallback). CJLT and JOLTIDA AI policies bar AI-drafted text.

## 3. Research session C, other routes

### Brief (verbatim)

You are researching publication venues. Web research only (WebSearch, WebFetch). Do not write files, do not use any browser, do not touch Google Drive or email.

THE ARTICLE (ART 5): [as in brief 1, with "primary teacher in Switzerland"]

GOAL: a FIRST peer-reviewed publication, FAST, with the HIGHEST REALISTIC chance of acceptance, in a LEGITIMATE venue (indexed in Scopus or Web of Science incl. ESCI, or the ACL Anthology; real peer review; not predatory). He will submit down a ladder of 5. Costs matter: he is unfunded.

YOUR CLUSTER (routes other than classic education journals):
A. Soundness-based open-access journals: PLOS ONE, Frontiers in Education, SAGE Open, Cogent Education, Discover Education (Springer Nature), Royal Society Open Science, PeerJ Computer Science. For each: acceptance rate if the publisher states one (quote, year, URL), time to first decision, the fee, and the fee-waiver or assistance rules for an unfunded independent researcher in Switzerland (a high-income country), AI policy (quote + URL), and whether an education/LLM-audit paper is in scope.
B. NLP and education-technology venues with proceedings: the BEA workshop (Innovative Use of NLP for Building Educational Applications), the TSAR workshop (Text Simplification, Accessibility and Readability), the Northern European Journal of Language Technology, the journal TAL (Traitement Automatique des Langues), AIED late-breaking results, EC-TEL, CSEDU. For each: acceptance rates from official proceedings prefaces or reports (quote, year, URL), next deadline after November 2026 if announced, cost (registration, presentation requirement, virtual option), indexing, AI-writing policy (for ACL venues, the ACL policy on AI writing assistance: quote + URL), and whether a journal-length paper must be shortened.

RULES: Take acceptance rates only from official pages or proceedings prefaces; give the exact quote, the year and the URL. Never estimate silently; write "not published" when absent, and "blocked" for pages you could not open. Mark your own judgments [inference].

OUTPUT (under 1,000 words): (1) a table for A and a table for B with the fields above; (2) your top 3 options for this author's goal (first publication, fast, high chance, low cost), with reasons; (3) what you could not verify.

### Report (verbatim)

n.p. = not published on pages I opened; blocked = would not open; [inference] = my judgment; URLs omit https://.

**A. Soundness-based OA journals**

| Journal | Acceptance; 1st decision | Fee | Waiver (unfunded, CH) | AI policy |
|---|---|---|---|---|
| PLOS ONE | 30.74% (Jan–Jun 2023 cohort; 48.2% in 2020); median 45 d, publication 204 d. journals.plos.org/plosone/s/journal-information.assessment (main page blocked) | $2,477 plos.org/publish/fees | Fee Assistance for "financial need", requested at submission; no income rule stated | "AI tools may be used to support development or revision"; disclose in Methods. journals.plos.org/plosone/s/ethical-publishing-practice |
| Frontiers in Education | n.p.; n.p. | CHF 2,195 frontiersin.org/journals/education/for-authors/publishing-fees | "open to anyone, regardless of institutional affiliation", but "partial", "not guaranteed". frontiersin.org/for-authors/submitting-research/what-fee-support-is-available | "must be clearly disclosed in the acknowledgments". frontiersin.org/about/policies-and-publication-ethics |
| SAGE Open | n.p.; n.p. | $2,400 (undated) sagepub.com/docs/default-source/msg/SGO | "case-by-case". solutions.sagepub.com/support/solutions/articles/7000064837 | Disclose in "methods or acknowledgements"; mainly AI-generated work "must be disclosed upon submission". journalssolutions.sagepub.com/support/solutions/articles/7000090479 |
| Cogent Education | blocked | blocked | Low/lower-middle-income waivers only; others may request a "discretionary discount". authorservices.taylorandfrancis.com/choose-open/publishing-open-access/requesting-an-apc-waiver/ | "Authors must clearly acknowledge… any use of Generative AI tools". taylorandfrancis.com/our-policies/ai-policy/ |
| Discover Education | blocked | blocked | Waivers for "researchers in lower-income countries". springernature.com/gp/researchers/the-researchers-source/open-science-blogpost/oa-funding-options-discover-journals/27819946 | "Use of an LLM should be properly documented in the Methods section". nature.com/npjqi/editorial-policies/ai (group policy) |
| Royal Society Open Science | n.p.; median 19 d, publication 184 d (2025). royalsociety.org/journals/authors/benefits/publishing-times/ | £1,400 royalsociety.org/journals/open-access/ | "discretionary waivers for those who lack funds"; waiver page blocked | Not found |
| PeerJ Computer Science | n.p.; median 35, undated. peerj.com/computer-science/faq-cs | $2,155 | Low-income countries and undergraduate co-authors only. peerj.com/about/policies-and-procedures/ | "AI models may not be listed as an author" |

Scope [inference]: PLOS ONE, Frontiers, SAGE Open, Cogent, Discover take empirical education or NLP work. Frontiers has a Digital Education section and is in Scopus and ESCI (frontiersin.org/journals/education/about). PeerJ judges "scientific and methodological soundness" (peerj.com/about/aims-and-scope/cs), requires code and data, and is in Scopus and WoS. RSOS covers the "entire range of science", so education fit is weak.

**B. NLP and edtech venues**

| Venue | Acceptance (official) | Next deadline | Cost; format |
|---|---|---|---|
| BEA | 2026: "132 submissions… overall acceptance rate of 48 percent" aclanthology.org/2026.bea-1.0.pdf. 2025: "169 submissions… 75 papers (44% acceptance rate)" aclweb.org/adminwiki/index.php/2025Q3_Reports:_SIGEDU | 2027 not announced; ACL 2027 Kyoto, workshops 18–19 Aug (2027.aclweb.org); 2026 deadline was 5 Mar [inference: spring 2027] | "one hybrid day and one fully virtual day"; ACL 2025 workshop-only virtual $200–250 academic, $250–300 non-academic, in-person $450–650 (2025.aclweb.org/registration); 8 pp long, 4 short plus references, so cut needed [inference]; ACL Anthology |
| TSAR / READI | READIxTSAR 2026 (LREC): "acceptance rate of 70.83%" (24 submitted) aclanthology.org/2026.readi-1.0.pdf; TSAR 2025 n.p. | None announced | n.p.; 4–8 pp; TSAR 2025 allowed online attendance; ACL Anthology |
| NEJLT | n.p. | Any time | "Free to submit, free to publish, free to read" (2023 call: list.lrec-conf.org/mailman3/hyperkitty/list/corpora@list.elra.info/thread/QIC5NUQPMLPTUFSNCCXU7Z6X42CZLTEK); ACL Anthology, 3–10 papers a year (aclanthology.org/venues/nejlt); no page cap; type "Computationally-aided linguistic analysis" |
| TAL | "Le taux de sélection est de fait très variable, allant de 25 à 75 %"; Varia 2024: "Sept articles ont été soumis… Deux articles ont été retenus" atala.org/sites/default/files/TAL_66_1_0.pdf | Varia continuous | No fee stated; English accepted since 2024; ACL Anthology (older issues seen); Scopus not stated |
| AIED LBR; EC-TEL | AIED 2026 (CCIS, all tracks): "selected from 627 submissions" link.springer.com/978-3-032-29794-5. EC-TEL (LNCS) 2025: 195 submissions, 43 full papers; 2026: "295 submissions", 45 research papers of 194 (≈23% computed) | 2027 not announced for either | AIED LBR 2024: 6–8 pp, on-site presenter; EC-TEL "fully in-person" |
| CSEDU 2027 | 2024: "received 202 paper submissions from 46 countries, of which 28% were accepted and published as full papers" iris.unitn.it/retrieve/be00ad98-57c0-4b25-aed8-ae54d1bc8677/Agostini_CSEDU_2024_-_Volume_2_-_Proceedings.pdf | 17 Nov or 21 Dec 2026; decision 15 Feb 2027; Rome 16–18 Apr. csedu.scitevents.org/CallforPapers.aspx | Speaker fee €650 early, €760 late (csedu.scitevents.org/RegistrationFees.aspx, undated); remote only "exceptionally"; Scopus, WoS "will be submitted for evaluation"; 12 pp, 10,000–50,000 characters (csedu.scitevents.org/Guidelines.aspx), probably fits [inference] |

AI-writing policy. ACL (BEA, TSAR/READI), on new ideas plus new text: "we would discourage such use in ACL submissions" (2023.aclweb.org/blog/ACL-2023-policy/). AI cannot be a co-author (aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics). CSEDU: AI-generated text "should be disclosed in the acknowledgements section" (csedu.scitevents.org/Guidelines.aspx). NEJLT, TAL: not found.

**Top 3 (first, fast, likely, cheap)**
1. **NEJLT.** Free, open any time, ACL Anthology, no page cap, and "Computationally-aided linguistic analysis" fits. Acceptance rate, review time and AI policy are unknown: ask the editor about AI-led work first. [inference] Only 3–10 papers a year, so possibly selective.
2. **CSEDU 2027.** The only open deadline (21 Dec 2026), decision 15 Feb 2027, 28% full-paper acceptance (2024), €650, indexing not guaranteed.
3. **BEA 2027.** Best documented odds (44–48%), ACL Anthology, virtual option (about $250–300, 2025 rates [inference]). But no call yet, a cut to 8 pages, and ACL's stance on AI-drafted text is the main risk.

Paid fallback: PLOS ONE (Fee Assistance) or RSOS (£1,400, discretionary waiver). Frontiers, SAGE Open and PeerJ list $2,155–2,400 or CHF 2,195 with no waiver stated for him.

**Could not verify.** Blocked: PLOS ONE journal-information page; BEA 2025 PDF; Cogent Education and SAGE Open journal pages (client error); Discover Education (Springer cookie wall); RSOS waiver page; NEJLT policy, review and author pages (nejlt.org); AIED 2026 CFP; EC-TEL site. Not found: acceptance rates for Frontiers, SAGE Open, Cogent, Discover, RSOS, PeerJ, NEJLT, AIED LBR; RSOS and NEJLT AI policies; NEJLT and TAL Scopus status; 2027 dates for BEA, TSAR, AIED, EC-TEL. Weak sources: PLOS figures end at the 2023 cohort; EC-TEL 2026 counts come from a bookseller; CSEDU fee page undated; Springer policy read on nature.com; ACL fees are 2025.

## 4. Check reading of the G2 changes

### Brief (verbatim)

You are a separate AI session doing an internal check reading (not peer review) of the last changes to a research manuscript before submission. Read-only: do not edit, commit or push anything in the repository, do not use a browser, Google Drive, e-mail or any provider API. You may copy files to /tmp/check_g2/ and run scripts there.

Repository: /home/claude/art5-harmos-audit (git). The previous checked state is main = 981a3a2. The changes to check are on branch g2-submission: f303b58 (gate G2 decisions) and f710101 (formatting for the journal Education and Information Technologies, EAIT), plus any later commits named "checks <run id>" written by GitHub Actions. See them with: git -C /home/claude/art5-harmos-audit diff 981a3a2 f710101 -- manuscript checks (ignore manuscript/build/*.docx binaries; read manuscript/build/manuscript.md, title_page.md and cover_letter.md, which are rendered from the sources in manuscript/ and manuscript/submission/).

Facts you cannot check yourself (take them as given, but say if the text goes beyond them):
1. The author's answers at gate G2 (1.11.2026, multiple-choice): conflicts of interest statement confirmed as true; the Anthropic promotional credit came from his paid Claude Max plan; he ticked all four of: came up with the topic, designed the protocol (its rules: two gates, everything logged, journals without fees, keys never in the chat), built the infrastructure (GitHub repositories, API accounts and capped keys, AsPredicted account and deposit, key rotation and revocation), made design decisions (keep three providers, switch to Mistral Large 4, the spending limits, the changes asked for at G1). He read the final manuscript and said everything sounds fine, and asked that the AI use stay disclosed while crediting his part.
2. An Anthropic e-mail of 17.10.2026 to him says: "Pablo's Individual Org, the API organization linked to your Max plan, received $200 USD in API credits. ... These credits expire on October 31, 2026."
3. EAIT's submission guidelines (Springer, read 1.11.2026): abstract of 150 to 250 words; 4 to 6 keywords; statements under the heading "Statements and Declarations" (competing interests, funding; submissions without them are returned); every original research article needs a data availability statement; "Use of an LLM should be properly documented in the Methods section"; LLMs cannot be authors; APA 7 references with DOIs as links.
The records you can read: CHANGELOG.md (sections Deposit and the P7 sections), manuscript/process_facts.json (with sources), manuscript/records/ (protocol_v1.1.md, findings_log.csv, p7/p7_records.md), README.md.

CHECK AND REPORT:
A. Truth of every changed sentence about who did what (Method paragraph, "Use of generative AI", CRediT line, Competing interests, Funding, Limitations, cover letter, title page). For each: supported by the facts and records above, overclaimed for the author, or understated for the AI (an earlier internal reading found that the manuscript once understated the AI's role; check that the new text does not repeat that). Quote the exact words at issue.
B. EAIT compliance of the rendered manuscript: abstract length, keywords count, the heading, LLM use in the Methods, data availability statement, nothing left that only made sense for the earlier target journal (BJET), and anonymity of the main manuscript (no author name, e-mail, ORCID or identifying link in manuscript/build/manuscript.md).
C. Consistency between manuscript, cover letter and title page (e.g. the letter's claim that the AI use is documented in the Methods and in the Statements and Declarations).
D. Run, in a copy if you prefer: python3 manuscript/render.py; python3 checks/check_numbers.py; python3 checks/check_claims.py; python3 checks/check_claims.py --plant (must FAIL); python3 checks/check_citations.py; python3 checks/recompute_primary.py; bash history/check_history.sh. Report each result. Also build the anonymised copy: python3 manuscript/make_anonymous_bundle.py /tmp/check_g2/anon.zip --ref f710101 and confirm it exits 0; scan its text files and the members of any .docx inside for the author's name in any case, "pabcorpri", "gmail", "edu-vd", "jouxtens", the ORCID 0009-0009-1844-7453 and "321415" (a hit inside a longer decimal number in results/measures.csv is a known false positive).
E. Any new error (grammar, a broken sentence, a number, a dangling reference to a removed section such as the practitioner notes).

OUTPUT (under 700 words): verdict per area A to E (confirmed / problem), then a numbered list of problems ranked by severity (blocking for submission / should fix / minor), each with the file, a quote of at most 15 words, what is wrong and the fix. Label what you ran [run] and what you only read [read]. Begin the report with: "Internal check reading by a separate AI session. Not peer review."

### Report (verbatim)

Internal check reading by a separate AI session. Not peer review.

Scope: f303b58 and f710101 (no "checks" commit exists). Commit abeaf1e landed mid-check; D gave identical results on it. Runs used clean archives in /tmp/check_g2. Unlabelled statements are [read]. No fact here comes from memory.

VERDICTS
A. Problem. Method paragraph: 3. Use of generative AI: overclaimed (3, 4), understated (5), not yet read by the author (6). CRediT: 8. Competing interests, Funding, Limitations, letter, title page: credit clause (2). Supported: topic, infrastructure, G1 and G2 decisions, Mistral switch, spend figures.
B. Confirmed [run]. Abstract 237 words, 6 keywords, heading "Statements and Declarations", LLM paragraph in Method, data availability, practitioner notes gone (BJET survives only as the Yan et al. reference). manuscript.md and docx metadata hold no name, e-mail, ORCID or identifying link.
C. Problem (1, 7, 12). The letter's claim holds: Method paragraph and heading exist.
D. Confirmed [run]. render.py reproduces the committed build; check_numbers, check_claims, check_citations, recompute_primary (20 values) and history check PASS; --plant FAILs (exit 1). Anonymised copy: exit 0, 396 files; my scan (text files, both .docx, six binaries) found only "321415" inside 4.963214151529284 in results/measures.csv (known false positive).
E. Confirmed. No broken sentence, wrong number or dangling reference.

PROBLEMS

Blocking
1. title_page.md: "AUTHOR INPUT: link to the AsPredicted record (or its PDF)". Still in md and docx; the letter promises that link. Insert it once the registration is public.
2. Blocking until verified. Manuscript (Competing interests, Funding, Limitations), cover_letter.md, title_page.md: "API credits included in the author's paid Claude Max subscription". The e-mail describes a $200 grant "added" on 17 October, expiring 31 October; the main run began 1 November, about 08:54 CET; the repository holds 201.87 USD ("which credit Anthropic drew first is not recorded"). "Included", and dropping "promotional" in Competing interests, go beyond the e-mail. Check the console (expiry, 1 November usage). Then write "promotional API credits, 200 USD of them announced on 17 October 2026 for the organisation linked to the author's Claude Max plan". If expired, delete "most of the Anthropic calls were paid with".
3. manuscript.md, Method ("designed by the author") and Use of generative AI: "The author conceived the study and designed the written protocol". His answer was "came up with the topic"; process_facts.json says "conceived the study (topic)". Protocol P0 has Claude formulate the questions; the text is the assistant's [inference]. "scripted checks that must be able to fail" is not among the four rules he named. Same in cover_letter.md: "I conceived the study". Write "chose the topic and decided the main rules of a protocol drafted with the assistant".
4. Same paragraph: "deposited the preregistration". CHANGELOG Deposit shows the session filling, hashing and approving the form after his "aprove" [inference]. Write "approved the deposit, which the assistant entered", unless he confirms he typed it.
5. Understated for the AI. Dropped from the old text: "an AI assistant did most of the work". "Separate sessions ... checked each citation" became "each citation was checked against the full text of its source", no agent (the protocol says the author did not). Limitations still says "written with an AI assistant". Commit f303b58 claims every fact was kept. Restore both; add that the assistant launched the data collection [inference].
6. "read the final manuscript"; Method "approved ... the manuscript before submission". He read the version before f303b58 [inference]; these sentences came after. He should read the final file before upload.
7. title_page.md: "no financial relationship with the providers". The manuscript says "no employment, consulting, shareholding or other"; he is a paying customer and credit recipient. Restore the qualifier.

Minor
8. CRediT: "funding acquisition" beside "no specific grant"; "methodology" beside the assistant having "designed the study in detail". Author's call; add that unlisted roles were the assistant's.
9. Method paragraph omits the literature search, which only the Statement lists.
10. "Every number in the text is filled in by script from the archived results": credit balances come from hand-copied process_facts.json.
11. Manuscript promises a "link anonymised for review"; the letter offers a copy. Say how reviewers get it.
12. f710101 title page said "section Statements" (fixed in abeaf1e). abeaf1e's "Dear Dr Keane" is unverified.
