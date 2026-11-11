# Pre-submission audit, editor forecast (2.11.2026)

Separate session (model claude-opus-5-5), launched by the main session (claude-opus-5-5) with no access to the drafting conversation, earlier reviews or the audit in progress. Brief and report verbatim.

## Brief

You are an experienced journal editor and publication strategist in educational technology and literacy research. Give an independent, candid forecast.

Situation. A sole author will submit the manuscript /home/claude/art5-harmos-audit/manuscript/build/manuscript.md (anonymised version; Supporting Information in manuscript/build/supplement.md) to five journals one at a time, in the order below, moving to the next after a rejection, until one accepts. The editor will also see a title page: the author is an independent researcher with no institutional affiliation, a primary-school teacher in Switzerland, and this is his first journal submission. The manuscript declares that an AI assistant did most of the research work under a written protocol, with the author choosing the topic, setting the protocol's rules, building the infrastructure, taking design decisions and approving the design and the manuscript (see the end of "Design and preregistration" in the Method and "Use of generative AI" under Statements and Declarations). Read the manuscript in full before estimating.

Read-only rules. Do not open anything under /home/claude/art5-harmos-audit/manuscript/records/, manuscript/verification_report.md, CHANGELOG.md, history/, or any journal-ladder document: form your own view. Do not create, modify or delete any file in that repository; use /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/forecast/ for scratch work.

Journal facts as read on the journals' own pages on 1 November 2026 (verify anything you rely on that seems doubtful; aims and scope pages are worth reading for fit):
1. Education and Information Technologies (Springer), https://link.springer.com/journal/10639 . Scopus and SSCI. Acceptance rate not published on its page. Median 29 days from submission to first decision. Springer AI policy: LLMs cannot be authors, and use of an LLM must be documented in the Methods section. Abstract 150 to 250 words, 4 to 6 keywords, no word limit stated.
2. Education in the Knowledge Society (Universidad de Salamanca), https://revistas.usal.es/tres/index.php/eks/index . ESCI, with a JCR Q1 badge (2024) on its site. Free to publish. Review in at most 3 months. No AI policy found on its pages. English or Spanish. Guidelines say 7,500 words including references (its checklist says 10,000).
3. Computers in the Schools (Taylor & Francis), https://www.tandfonline.com/journals/wcis20 . Scopus and ESCI. Acceptance rate 25% (journal page). 29 days to first decision on average. Taylor & Francis AI policy: "Authors should not submit manuscripts where Generative AI tools have been used in ways that replace core researcher and author responsibilities, for example: Text or code generation without rigorous revision" (policy page https://taylorandfrancis.com/our-policies/ai-policy/). 8,000 words all inclusive, unstructured 150-word abstract, single-anonymous review with one reviewer.
4. Reading Psychology (Taylor & Francis), https://www.tandfonline.com/journals/urpy20 . Scopus. Acceptance rate 42% (journal page). 103 days to first decision on average. Same Taylor & Francis AI policy.
5. Research in Learning Technology (Association for Learning Technology), https://journal.alt.ac.uk/index.php/rlt . Scopus and ESCI. Acceptance rate not published. 6,000 words including tables, captions and references, longer submissions rejected without review. Double-anonymous review. AI use to be declared in the acknowledgements.
Manuscript length as rendered: main text 5,377 words (5,961 with tables and captions), abstract 237 words, everything except references 6,885 words, 25 references.

Deliver:
A. For each journal: P(sent out for review), P(eventually accepted | sent out for review, revisions included), and their product, each as a range and a point value; the main reasons (fit with scope and readership, how the journal's AI policy and editors are likely to treat the declared AI use, length and format, the manuscript's strengths and weaknesses as that journal's reviewers would see them); and the expected time to a decision.
B. The probability that at least one of the five accepts. Explain how you treat correlation between the journals' decisions (shared weaknesses, the same AI disclosure), and give both the independence figure and your realistic figure.
C. Whether you would change the order, and why.
D. The five changes to the manuscript, title, abstract or cover letter that can be done today without new data and would most raise the odds, ranked by expected gain, each with the exact passage concerned.
E. Optional: if you know a clearly better journal for this goal (legitimate, indexed in Scopus or Web of Science, no fee, reasonably fast, AI policy compatible with this disclosure, not the Swiss Journal of Educational Research), name it only after verifying on its own pages, with URLs.

Mark every estimate as an estimate. Do not invent facts about journals; say "not found" when you could not verify something. Keep it under 1,500 words. Your final message must be the forecast itself.

## Report

**Forecast for the ART 5 journal ladder.** Every probability and time below is my estimate unless I attribute it to a journal page. I read the manuscript, Supporting Information, title page, cover letter and figures in full. I opened nothing under records/ or history/, and no verification report, changelog or ladder document.

**What I checked on the journals' pages (two points differ from the brief)**
- **Springer:** its current policy page (link.springer.com/brands/springer/journal-policies) sorts AI uses into Green, Amber and Red. It says "AI may support, but must not replace, scholarly judgement". It does not permit "Assigning authorship or accountability to AI systems or tools". The page does not say the disclosure goes in the Methods section, so I could not confirm that rule from the brief.
- **EKS does have an AI clause** (About page): authors must declare generative-AI use, and reviewers and editors may not use it.
  - Its 7,500-word cap counts the title, abstract and keywords in both languages plus the references. A bilingual version would be about 7,850 words, so it is over. The checklist says 10,000.
  - First decision within 30 days, 7 days allowed for revisions, free to publish (diamond open access).
- **RLT:** "if the paper is over the 6000 word limit on submission it will be desk rejected". AI use is declared in the acknowledgements. Indexed in Scopus and ESCI, no fees.
- **Taylor & Francis journals:** the tandfonline.com pages were blocked, so I read the same "About this journal" pages mirrored on informahealthcare.com.
  - Computers in the Schools: "primarily focused on the use of technology in K-12 education", 25% acceptance, 29 days to first decision.
  - Reading Psychology: "literacy, reading, and related psychology disciplines", 42% acceptance, 103 days to first decision, and no mention of technology.
  - I could not verify the word limits or review model of either.

**A. Per journal** (assuming the manuscript is formatted to each journal's rules)

| Journal | P(sent for review) | P(accepted, given review) | P(accepted) | Time to decision |
|---|---|---|---|---|
| 1 EAIT | 0.35 (0.25–0.50) | 0.50 (0.35–0.65) | **0.17** (0.09–0.30) | desk decision ~2–4 wk; if reviewed, final ~5–9 mo |
| 2 EKS | 0.33 (0.20–0.50) | 0.48 (0.35–0.60) | **0.16** (0.07–0.28) | desk ≤1 mo; final ~2–4 mo |
| 3 Computers in the Schools | 0.27 (0.15–0.40) | 0.48 (0.35–0.65) | **0.13** (0.05–0.25) | first ~1 mo; final ~4–6 mo |
| 4 Reading Psychology | 0.20 (0.10–0.30) | 0.45 (0.30–0.60) | **0.09** (0.03–0.18) | first ~3.5 mo; final ~6–10 mo |
| 5 RLT, at current length | ~0.02 | n/a | **~0.01** | rejected at the desk on length |
| 5 RLT, cut to ≤6,000 words | 0.32 (0.20–0.50) | 0.45 (0.30–0.60) | **0.14** (0.06–0.27) | not published; desk ~1–2 mo, final ~4–8 mo |

**What reviewers at every journal will see**
- **Strengths:**
  - preregistration;
  - 7,680 texts from six models;
  - the Vikidia validity check and the collision control;
  - results reported model by model;
  - a public pipeline whose scripts fill in and check every number.
- **Weaknesses:**
  - the measure covers one lexical dimension, taken from adult corpora;
  - nothing ties the results to real pupils (they are in "model-internal years");
  - the confirmatory effect (−0.012 Zipf) "rests on one model";
  - the practical rule comes from exploratory analyses;
  - the models are already ageing;
  - the paper uses dense coined terms.

**EAIT.** The topic fits.
- Its scope page asks for "strong conceptual frameworks". The 500-word Background has none, and a Swiss case can read as local.
- Two passages create the AI risk: the CRediT line that gives formal analysis, software and the original draft to the AI, and the phrase "did most of the research work". Under Springer's wording, together they read as AI replacing the author's judgement.
- I expect 30–40% of editors to reject it at the desk for that reason alone.

**EKS.** The topic fits, and being free and ranked Q1 it is competitive.
- No clause I found restricts AI use that has been declared. But a journal that bars its own reviewers from generative AI may be cool to research run by AI.
- It needs a Spanish title, abstract and keywords and about 450 words cut. Otherwise it may be returned at the technical check, which takes 5–7 days.

**Computers in the Schools.** This is the best topical fit.
- The Taylor & Francis clause "Text or code generation without rigorous revision" matches the disclosure ("drafted the manuscript", and the author "read the final manuscript"). That holds unless the author shows his own revision. I put the risk of a desk rejection on that ground alone at about 50%.
- The abstract must go from 237 to 150 words.
- The brief says there is one reviewer (I could not verify this), which makes the outcome highly variable.

**Reading Psychology.** This is the weakest fit: the study has no readers, and technology is not in the scope.
- Reviewers will ask why the measure uses Lexique rather than Manulex, which the paper itself cites, and about decodability and syntax.
- It has the same Taylor & Francis clause and the slowest clock.

**RLT.** At its current length the paper is about 6,660 words with tables, captions and references, before the abstract and statements. That means automatic rejection at the desk.
- Once cut: the AI policy only asks for a declaration, review is double-anonymous, and the scope includes primary education.
- Against it: the readership is mostly in higher education and sceptical of research led by AI.

**B. Probability that at least one journal accepts**
- If the five decisions were independent: 0.52, or 0.45 if RLT gets the current length.
- Realistic estimate: **0.37 (0.20–0.58)**.
- How I treated correlation:
  - I used a one-factor model with a latent correlation of 0.4–0.5. The shared causes are the identical AI disclosure (the main one), the same weaknesses and the same author profile.
  - The two Taylor & Francis journals are linked more tightly still: a rejection by Computers in the Schools on AI grounds nearly settles Reading Psychology.
  - I discounted journals 3–5 by 10–20% because the models, sampled on 1 November 2026, age with each rejection. Reviews from earlier rounds partly offset that.
- My inference: if EAIT and EKS both reject at the desk citing AI use, the other three together are worth about 0.15.

**C. Order:** EAIT → EKS → RLT (6,000-word version) → Computers in the Schools → Reading Psychology, or replace Reading Psychology. The overall probability moves by less than a point, but the expected time to acceptance falls.
- The two Taylor & Francis journals, whose clause fits the disclosure most directly, go last, so they receive the most-revised statement.
- Reading Psychology, the slowest and worst-fitting, goes last of all.
- RLT's different AI policy makes it a more independent chance.
- If a fast final decision matters more than being in SSCI, put EKS first.

**D. Five changes, ranked by expected gain**
1. **Rewrite the AI disclosure and the CRediT line.** This brings the largest gain because it affects every journal.
   - Passages:
     - Method: "Under it the assistant (Claude Opus 5.5, claude-opus-5-5) did most of the research work".
     - Statements: "read the final manuscript and takes full responsibility for its content".
     - CRediT: "The detailed study design, data curation, formal analysis, investigation, software, validation, visualization and writing – original draft were carried out by the AI assistant".
   - Keep every fact. Take the AI out of CRediT, which lists human contributors, and describe its tasks only in the AI statement.
   - Replace "most of the research work" with the list of tasks, plus what the author decided and checked himself.
   - Then do a recorded revision pass of the Discussion and Conclusion, so the statement can say "revised" rather than "read". Never claim a revision that did not happen.
   - Estimated gain: +5–10 points on P(sent for review), more at the Taylor & Francis journals.
2. **Make one master version of at most 6,000 words in total.** This makes RLT possible, keeps EKS under 7,500 words with both abstracts, and tightens the paper.
   - Move the paragraph beginning "Mistral Large 4, the only audited model whose reasoning is returned as text…" and the "Sensitivity analyses" section to the Supporting Information.
   - Shorten Funding ("Before the main run that account held 206.87 USD of credit…").
   - Merge "Lexical equivalence is not understanding" into Limitations.
   - Renumber the figures, since Figure 3 is cited before Figure 2.
3. **Write a cover letter for each journal.**
   - Passage: "I chose the topic and set the main rules of the protocol for AI-assisted research under which an AI assistant did most of the research work."
   - Open with his position as a primary teacher inside the HarmoS system, where the question came from.
   - Explain the process against that journal's AI clause.
   - Give reviewers an anonymised repository link instead of saying a copy "can be sent to reviewers through the editorial office".
   - Check "As Springer's policy asks, this use is documented in the Methods" against EAIT's own guidelines, and check the "Dr Keane" salutation.
4. **Rework the title and abstract.**
   - "Swiss grade labels and the lexical demand…" signals a local study. A suggestion: "Local grade labels in prompts to large language models: A preregistered audit of French reading texts for Swiss primary grades".
   - In the abstract, "0.30 model-internal years older (95% CI [0.13, 0.46])" is hard to follow for an editor deciding at the desk. Lead with how far the models differ and with the advice to state the age, keeping the exploratory labels.
   - Prepare a 150-word version for Computers in the Schools and a 200-word version for RLT.
5. **Justify the measure and add a framework.**
   - Passage: "Grade-level norms from French school readers exist (Lété et al., 2004), and adult-based norms are a weaker guide…". It concedes the obvious objection without saying why Lexique was chosen.
   - State the real reason in the Measure section. If feasible, add a post hoc check with Manulex on the archived texts, which needs no new data.
   - Add a short paragraph placing lexical demand within text complexity, to meet EAIT's request for "conceptual frameworks".

**E.** I name none: I could not verify any journal as clearly better on all six criteria. The deciding criterion is an AI policy that only asks for a declaration, so check that first in any replacement for Reading Psychology.

**Next action:** rewrite the AI statement and the CRediT line (change 1) before the EAIT submission. That one passage moves the odds at every journal on the list.
