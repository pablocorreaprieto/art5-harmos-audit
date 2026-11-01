# Preregistration draft (AsPredicted), ART 5

Status: text for the deposit (design v0.4.9, gate G1 passed on 1 November 2026), not yet
deposited. Text to paste into the AsPredicted form (questions version 2.00), question by question.
Each answer is under the form's limit of 2,900 characters.

**1) Data collection.** Option ticked: "It's complicated. We have already collected some data but
explain in Question 8 why readers may consider this a valid pre-registration nevertheless." The
explanation is the first paragraph of question 8.

**2) Hypotheses.** We ask whether naming the grade with a Swiss label gives texts whose lexical
demand matches the texts the same model writes when given the pupils' age.
H1 (manipulation check, per model): with the age only, the mean Zipf frequency of content
lemmas decreases as the requested age increases.
H2 (level): averaged over the six grades, texts requested with the bare HarmoS label ("de 5H")
differ in mean Zipf frequency from texts requested with the matching age ("de 8 à 9 ans"); and
the same for the bare P label used in Vaud and Geneva ("de 5P"). We expect lower values (rarer
words), but test two-sided because reading the digit as an age would give the opposite.
H3 (tracking): the change of mean Zipf frequency across grades differs between bare-label texts
and age-only texts (H and P labels separately). A model that ignores the label gives a positive
gradient of the difference.

**3) Dependent variable.** Mean Zipf frequency of content lemmas in each text. Each word form is
read as the Lexique 3.83 lemma with the largest summed form frequency, then that lemma's most
frequent row. Content words are forms whose reading is tagged noun, qualifying adjective (tag ADJ
without a subtype, so determiners, numerals and indefinites are excluded) or verb, excluding the
lemmas être, avoir, tout, autre and même (indefinites that Lexique tags as plain adjectives) and
excluding names. Frequency is the mean of the Lexique lemma frequencies in films and in books (per
million). Zipf = log10(f + 0.031) + 3. Tokens absent from Lexique that are not names count as
frequency 0. Typographic apostrophes are normalised and the ligatures œ and æ written oe and ae,
in the texts and in the lexicon alike; elisions are split, verb-subject clitics removed, and
Lexique forms with a hyphen or apostrophe kept whole. Markdown marks, lines without letters and
label lines ("Titre :", "Texte :") are removed, as are up to two leading preface lines (a line
ending with a colon, a line opening with a polite formula such as "Bien sûr", a line opening with
"Voici un" or "Voici une" followed, after an optional "petite", "courte", "belle" or "nouvelle", by
"histoire", "texte", "récit", "conte", "lecture" or "poème", or a line opening with "Voici" that
states the intended readers, such as "pour des élèves" or "adapté") and up to three closing lines addressed to the
user ("N'hésitez pas ...", "Dites-moi ...", "Si vous souhaitez ...", "Bonne lecture", a word count,
a note about the text or its readers, "Ce texte est adapté ..."); the number of lines removed is
recorded. The first remaining line is a title, not measured, when it was a
markdown heading or bold line, starts with "Titre", or has at most 12 words and does not end with
a period or an ellipsis. A capitalised token is a name when it is not in initial position (first
token of a sentence or line, or after a colon, an opening quote, a dash or a hyphen standing
between spaces), or when it is in initial position and is absent from Lexique in lower case or
capitalised elsewhere in non-initial position. Code: compute.py at tag prereg of
https://github.com/pablocorreaprieto/art5-harmos-audit (made public at submission). The lexicon is
the Lexique 3.83 file downloaded from lexique.org by the workflow (SHA-256 637ba37a767a6667...,
logged).

**4) Conditions.** Labels crossed with six grades (3H to 8H, ages 6-7 to 11-12): L1 bare H label,
L1P bare P label, L2 H label plus "en Suisse romande", L3 H label plus the age, L4 French grade
label (CP to 6e), L5 age only (reference). Also L0, no level (one text per model, genre and
topic), and L6, the same digit with the French collège suffix ("de 3e", "de 4e", "de 5e") at 3H
to 5H. Crossed with two genres (story, informational text), 16 fixed topics and six models
(claude-sonnet-5-5, claude-haiku-5-5, gpt-6.1-sol, gpt-6-luna, mistral-large-4-0,
mistral-small-2603, as listed by the providers on 31 October 2026), that is 480 texts per topic
and 7,680 texts, plus 720 knowledge probes. Prompt (French): "Écris {une histoire à lire | un
texte documentaire à lire} pour des élèves{label}, sur le thème {topic}. Réponds seulement avec un
titre et le texte." The topics, the label wordings and the call plan are in design.json and
make_prompts.py at tag prereg. One text per prompt, independent calls in random order (seed
20261025), temperature 1.0 (omitted and recorded for a model that rejects it), at most 4,000
output tokens. Reasoning settings stay at each provider's default; in the pilot, most answers of
all three models included reasoning tokens, which count toward the 4,000-token limit. Data are
collected within 14 days after this deposit, between 1 November 2026 and 15 November 2026.

**5) Analyses.** Pairs are matched on model, grade, genre and topic. For topic t and grade g,
d(g,t) is the mean over models and genres of (label minus L5). Level(t) is the mean of d over
the six grades, and gradient(t) is the least-squares slope of d on the grade's age midpoint.
Primary tests: two-sided one-sample t-tests over topics (df = T minus 1) of the level of L1
minus L5 (H2-H) and of L1P minus L5 (H2-P), and of the gradient of L1 minus L5 (H3-H) and of
L1P minus L5 (H3-P). Holm correction over these four tests, alpha .05. H1: per model, OLS of the
dependent variable on the age midpoint within L5 with genre and topic effects, standard errors
clustered by topic, one-sided t with T minus 1 df, no correction. Effects are reported in Zipf
units with 95% intervals, and as model-internal age equivalents for models whose L5 slope is at
most -0.02 Zipf per year: shift = sum of model levels / sum of slopes, tracking = 1 + sum of
gradients / sum of slopes, with 95% intervals from 2,000 bootstrap resamples of topics, the set of
eligible models being fixed on the full data. Topics are treated as random, and inference is
conditional on these six models and this prompt wording. Code: analyze.py at tag prereg.

**6) Exclusions.** A call that fails or returns nothing is requested once more. A text that is
refused or asks for clarification (finish reason content_filter or refusal, or one of the first
two lines of the answer opening with a phrase listed in compute.REFUSAL_RE, directly or after a
polite opener such as "Merci" or "Bien sûr"; a first line of at most 12 words that does not end
with a period, an ellipsis, a question mark, an exclamation mark or a colon is not tested when at
least 20 words follow it), has fewer than 20 words, or has more than half of its word tokens
absent from Lexique (not French) is requested once more. If the second answer fails the same
rules, the text is excluded and counted by label, model and grade. Truncated texts and exact
duplicates are kept and flagged, and sensitivity analyses remove them. Answers that address the
user in their first two or last three lines, outside quotation marks and dialogue lines
(compute.META_RE, for example "Souhaitez-vous ...", "Peux-tu me préciser ...", or a sentence ending
with a question mark that names the grade label, such as 5H or 5P, or the school system), are kept and flagged, and a sensitivity analysis
removes them.
No exclusion uses the value of the dependent variable or of any other frequency measure. If the
spending cap stops data collection, it resumes only after the author raises the cap, and calls
without an answer by 15 November 2026 are missing. Missing pairs are dropped. A topic with fewer
than half of its pairs, or with a grade without any pair, is dropped from that test and counted.

**7) Sample size.** 16 topics, 7,680 texts. The smallest effect of interest is a level difference
of 0.04 Zipf, one year of age on the planning ruler of -0.04 Zipf per year (the pilot slope is
reported). T is the smallest of 16, 24 or 32 that gives a simulated power of at least .80 for the
H2-H level test at that difference, with the pilot's residual standard deviation taken at its
upper 80% confidence bound (sim_power.py at tag prereg, 1,000 simulated data sets per option). If
no option reaches .80, or if the pilot ruler is not significantly decreasing (one-sided p above
.05), the author decides before data collection and the decision is recorded. Pilot: residual
standard deviation 0.117 (upper 80% bound 0.122), pooled slope -0.045 Zipf per year (one-sided
p < .001), simulated power .835 with 16 topics, hence 16 topics.

**8) Other.** Data collected before this pre-registration (question 1). No data for the
confirmatory study have been collected. A pilot was run on 31 October 2026 with 252 calls to three
of the six models: 216 texts requested with the pupils' age only (six grades, two genres, six
topics), used to estimate the residual standard deviation and the age slope, and 36 knowledge
probes, used only to check the answer parser. No text was requested with any other label before
this deposit, so the pilot says nothing about H2 and H3; its age-only texts bear on H1 for three
models. The probe answers are stored in the repository and their accuracy was not computed. Pilot
outputs are excluded from every confirmatory analysis.

Secondary: L3 against L5 and against L1 (level and gradient); the primary
contrasts by OLS with model x grade cells and label x model level and gradient terms, standard
errors clustered by topic; the primary contrasts on median Zipf, share of content lemmas below
Zipf 3 and below Zipf 4, mean word length, words per sentence, number of words, Kandel-Moles
readability and mean Zipf of word forms in films; sensitivity analyses (length residualised
within model, truncated texts removed, duplicates removed, flagged answers removed, age
equivalents by inverse lookup on an isotonic fit); linearity of each L5 ruler (F test). Controls:
L6 minus L5 at 3H to 5H; L0 placed on each model's ruler. Exploratory: per-model and per-grade
contrasts, L2 and L4, provider and model size, explicit mention of an age or a grade in the
outputs, refusal and clarification rates, flagged answers and removed preface or closing lines by
label, and the knowledge probes (the first age range stated counts; correct if its
midpoint lies within the true range plus or minus half a year). Measure validity: known-groups
check run before the pilot (Vikidia against French Wikipedia, 30 subjects; passes if at least 25
pairs are usable and Vikidia scores higher in at least 21), run on 31 October 2026 and passed
(Vikidia higher in 28 of 29 usable pairs).

**9) Name.** Swiss grade labels and the lexical demand of LLM-generated French reading texts

**10) Type of study.** Other: audit experiment on large language models, no human participants.

**11) Data source.** Other: API calls to six large language models (Anthropic, OpenAI, Mistral).
