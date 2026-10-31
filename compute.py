"""Measures for ART 5 (measure v0.4.4 of 25.10.2026, after the internal design review, the check of
its fixes and five confirmations of those fixes; the file also writes the retry list and the probe
table).

python compute.py LEXIQUE RAW_GLOB OUT_CSV [PREFIX]   measures for every text call in RAW_GLOB
python compute.py --self-test LEXIQUE                golden tests and failure controls, exits
                                                     non-zero on any mismatch

Construct: lexical demand of the text (not overall difficulty).
Primary measure: mean Zipf frequency of content-word lemmas.
  reading      = for each form, the lemma with the largest summed form frequency over its Lexique
                 rows, then that lemma's most frequent row (so "suis" is read as être, not suivre)
  content word = token whose reading is tagged exactly NOM, ADJ or VER (qualifying adjectives only,
                 so determiners, numerals and indefinites tagged ADJ:pos, ADJ:dem, ADJ:num, ADJ:ind
                 or ADJ:int are not content words), with a lemma other than être, avoir, tout,
                 autre and même (the last three are determiner-like words that Lexique tags plain
                 ADJ, as in "tous les enfants", "une autre balle", "les mêmes"), and which is not
                 a name
  frequency    = mean of the Lexique 3.83 lemma frequencies in films and books (freqlemfilms2,
                 freqlemlivres, per million), so inflection and tense (passé simple) do not count
  Zipf         = log10(frequency + 0.031) + 3, i.e. about one occurrence added to the corpus
  a token absent from Lexique that is not a name counts as a content word with frequency 0
Names: a capitalised token is a name if it is not in initial position, or if it is in initial
  position and either its lower-case form is absent from Lexique or the same capitalised form occurs
  elsewhere in the text in non-initial position. Initial position = first token of a sentence or of
  a line, or first token after a colon, an opening quote or a dash (an em or en dash, or a hyphen
  standing alone between spaces). Names are excluded from lexical measures.
Tokenisation: typographic apostrophes are normalised and the ligatures œ and æ are written oe and ae,
  in the texts and in the lexicon's forms and lemmas alike; forms Lexique lists with an apostrophe
  or a hyphen (aujourd'hui, quelqu'un, grand-mère) stay whole; other elisions are split after the
  apostrophe (l'école -> l' + école); verb-subject inversions lose their clitic (dit-elle -> dit,
  demanda-t-il -> demanda).
Cleaning: markdown marks removed, each line remembering whether it was a markdown heading or a bold
  line; lines without letters ("---") and label lines ("Titre :", "Texte :") removed; up to two
  leading lines of preface removed (a line ending with a colon, a line opening with Bien sûr,
  D'accord, Avec plaisir, Absolument, Certainement or Volontiers, a line opening with "Voici une
  histoire" or "Voici un texte", or a line opening with Voici that states the intended readers,
  such as "pour des élèves", "adapté", "destiné", "au niveau"); up to three closing lines addressed
  to the user removed (POSTFACE_RE, for example "N'hésitez pas ...", "Dites-moi ...", "Si vous
  souhaitez ...", "Bonne lecture", "(Environ 80 mots)", a note about the text or its readers such
  as "Note : le vocabulaire a été simplifié ...", "Ce texte est adapté ..."); then the first
  remaining line is a title, and is not measured, when it was a markdown
  heading or bold line, when it starts with "Titre", or when it has at most 12 words and does not
  end with a period or an ellipsis. The number of preface and closing lines removed is recorded.
Exclusions (counted, after one retry): failed call or empty answer, refusal or request for
  clarification (finish reason content_filter or refusal, or one of the first two lines of the
  answer opening with a phrase of REFUSAL_RE, directly or after a polite opener such as Merci or
  Bien sûr; a first line that reads as a title, at most 12 words not ending with a period, an
  ellipsis, a question or exclamation mark or a colon, is not tested when at least 20 words follow
  it), fewer than 20 words, more than half of the word tokens absent from Lexique (not French).
  Truncated texts (finish reason length, max_tokens or model_length) are kept and flagged. Exact
  duplicate texts are kept and flagged. Answers that address the user in their first two or last
  three lines, outside quotation marks and dialogue lines (META_RE, for example "Souhaitez-vous
  ...", "N'hésitez pas", "Peux-tu me préciser", "J'aurais besoin de savoir", or a sentence ending
  with a question mark that names the grade label, such as 5H or 5P, or the school system), are kept
  and flagged (flag_meta), and a sensitivity
  analysis removes them. No exclusion uses the value of a lexical measure.
Secondary: median Zipf and share of content lemmas below Zipf 3 and below Zipf 4, mean word
  length in letters (names excluded), words per sentence, number of words, Kandel-Moles
  readability, mean Zipf of word forms in films (sensitivity), share of tokens absent from Lexique.
Blinding (optional, blind_labels): every measure of the listed labels is blanked before anything is
  written or printed, length included; the pilot of design v0.4 has no such texts.
Probes: python compute.py --probes RAW_GLOB OUT_CSV [PREFIX] writes the knowledge-probe answers.
"""
import glob
import hashlib
import json
import math
import os
import re
import statistics
import sys
import tempfile

import pandas as pd

CONTENT = {"NOM", "ADJ", "VER"}
EXCLUDED_LEMMAS = {"être", "avoir", "tout", "autre", "même"}
# elided function particles, several of them absent from Lexique as forms
ELIDED = {"c'", "d'", "j'", "l'", "m'", "n'", "s'", "t'", "qu'", "jusqu'", "lorsqu'", "puisqu'", "quoiqu'"}
CLITICS = ["-t-ils", "-t-elles", "-t-il", "-t-elle", "-t-on", "-ils", "-elles", "-il", "-elle", "-on",
           "-je", "-tu", "-nous", "-vous", "-le", "-la", "-les", "-lui", "-leur", "-moi", "-toi", "-y", "-en", "-ce"]
LETTERS = "A-Za-zÀ-ÖØ-öø-ÿŒœÆæ"
TOKEN_RE = re.compile(f"[{LETTERS}]+(?:['-][{LETTERS}]+)*'?")
VOWELS = "aeiouyàâäéèêëîïôöùûüÿœæ"
MIN_WORDS = 20
MAX_OOV = 0.5
SMOOTH = 0.031
REFUSAL_FINISH = {"content_filter", "refusal"}
# Refusals and requests for clarification, matched at the start of one of the first two lines of an
# answer (after markdown marks and label lines are removed), directly or after OPENER_RE. Each
# phrase states the refusal or the question itself, so that a story opening with "Désolé, petit
# lapin" or "Je ne peux pas dormir" does not match.
REFUSAL_RE = re.compile(
    r"(je suis désolée?|désolée?|je suis navrée?|navrée?|toutes mes excuses)\b[\s,!.]*(mais\s+)?(je\b|j'|il\b|"
    r"cette\b|ce\b|cela\b|ça\b|le\b|la\b|les\b|sans\b)"
    r"|malheureusement[\s,]*(je ne\b|je n'|j'ignore|je suis dans l'impossibilité|il n'existe|il n'y a pas)"
    r"|je ne (peux|pourrai|pourrais) pas (écrire|rédiger|produire|créer|générer|répondre|savoir|deviner|"
    r"déterminer|identifier|vous aider|t'aider|aider)"
    r"|je ne suis pas (en mesure|sûre?|certaine?)"
    r"|je n'ai pas (bien |très bien )?compris"
    r"|je ne comprends pas (bien |très bien )?(ce que|ce qu'|votre|ta|la demande|le terme|le sigle|l'abréviation|"
    r"cette|ce sigle|ce terme)"
    r"|je ne sais pas (exactement |bien )?(ce que (signifie|veut dire|désigne|représente)|à quel (âge|niveau|degré)|"
    r"quel (âge|niveau|degré))"
    r"|je ne (connais|reconnais) pas (bien )?(le |la |l'|les |ce |cette )?(degré|niveau|classe|système|notation|"
    r"sigle|abréviation|désignation|terme)"
    r"|(pourriez|pouvez|voudriez|voulez)-vous (me |m')?(préciser|clarifier|indiquer|dire|expliquer|donner|confirmer)"
    r"|(pourrais|peux)-tu (me |m')?(préciser|clarifier|indiquer|confirmer)\b"
    r"|(pourrais|peux)-tu (me |m')(donner|expliquer|dire (ce que|ce qu'|à quel(le)?s?|quel(le)?s?|l'âge))\b"
    r"|dis-moi (ce que|ce qu'|à quel(le)?s?|quel(le)?s?|l'âge)\b|tu veux dire (ce que|ce qu'|à quel(le)?s?|quel(le)?s?)\b"
    r"|qu'entendez-vous|que voulez-vous dire|qu'entends-tu (exactement |vraiment )?par"
    r"|merci (pour|de) (votre|ta) (demande|message|question|requête)"
    r"|(i'm|i am) sorry|sorry\b|i (can't|cannot)|could you (please )?(clarify|specify)|can you clarify",
    re.IGNORECASE)
OPENER_RE = re.compile(r"^(merci( beaucoup)?( pour [^.!?]*)?|bien sûr|bien sur|d'accord|avec plaisir|absolument|"
                       r"certainement|volontiers)\s*[,!.:]*\s*", re.IGNORECASE)
TITLE_LABEL_RE = re.compile(r"^(titre|title)\s*:?\s*", re.IGNORECASE)
LABEL_LINE_RE = re.compile(r"^(titre|title|texte|text|histoire|récit)\s*:?\s*$", re.IGNORECASE)
PREFACE_RE = re.compile(r"^(bien sûr|bien sur|d'accord|avec plaisir|absolument|certainement|volontiers)\b", re.IGNORECASE)
VOICI_RE = re.compile(r"^voici\b", re.IGNORECASE)
VOICI_META_RE = re.compile(r"^voici (une|un) (petite |courte |belle |nouvelle )?(histoire|texte|récit|conte|lecture|poème)\b",
                           re.IGNORECASE)
AUDIENCE_RE = re.compile(r"\b(pour (des|les|vos|tes|nos|de jeunes) (élèves|enfants|lecteurs)|adaptée?s?|destinée?s?|"
                         r"au niveau|du niveau|de niveau)\b", re.IGNORECASE)
POSTFACE_RE = re.compile(
    r"^(n'hésitez|n'hésite pas|dites-moi|dis-moi|si vous (souhaitez|voulez|avez besoin|le souhaitez|désirez)|"
    r"\(?\s*(environ |à peu près )?\d+\s*mots\s*\)?$|"
    r"(souhaitez|voulez|aimeriez|voudriez|préférez)-vous|j'espère que (ce|cette|cela|ça|l'histoire|le texte|vos|tes|les élèves)\b|"
    r"je (peux|pourrais) (aussi |également )?(adapter|modifier|proposer|raccourcir|allonger|simplifier|écrire une autre)|"
    r"bonne lecture|\(?\s*(note|remarque|nb|n\.b\.).*\b(texte|histoire|récit|vocabulaire|niveau|élèves|enseignante?s?|"
    r"lecture|mots|phrases|adaptée?s?|simplifiée?s?)\b|"
    r"(ce|cet|cette) (texte|histoire|récit|article) (est|a été) "
    r"(adapté|adaptée|écrit|écrite|conçu|conçue|pensé|pensée|rédigé|rédigée))", re.IGNORECASE)
META_RE = re.compile(
    r"\b(pourriez|pouvez|voulez|souhaitez|préférez|aimeriez|voudriez|souhaiteriez|préféreriez)-vous\b"
    r"|\bn'hésitez pas\b|\bsi vous (souhaitez|voulez|avez besoin|le souhaitez|désirez)\b|\bdites-moi\b"
    r"|\bfaites-moi savoir\b|\bj'espère que (ce|cette|cela|ça|l'histoire|le texte)\b"
    r"|\bje (peux|pourrais) (aussi |également )?(adapter|modifier|proposer|raccourcir|allonger|simplifier)\b"
    r"|\b(pourrais|peux)-tu (me |m')(préciser|clarifier|indiquer|expliquer|dire)\b|\bdis-moi\b"
    r"|\bj'(aurais|ai) besoin (de savoir|de connaître|d'une précision|de précisions)\b",
    re.IGNORECASE)
# A grade label (5H, 5P: capital letter, so "8 h" is a time) or the school system, tested on each
# sentence that ends with a question mark; "degré" in the singular, so "20 degrés" is a temperature
LABEL_Q_RE = re.compile(r"\b\d+\s?[HP]\b|(?i:harmos|\bdegré\b|niveau scolaire|système scolaire)")
SENTENCE_END_RE = re.compile(r"(?<=[.!?…])\s+")
QUOTED_RE = re.compile("«[^»]*»|“[^”]*”|\"[^\"]*\"")
DIALOGUE_START = ("–", "—", "-", "«", "\"", "“")
INITIAL_GAP_RE = re.compile(r"[:«\"“—–]|(?:^|\s)-(?:\s|$)")
TRUNCATED_FINISH = {"length", "max_tokens", "model_length"}
LEXICAL = ["n_content", "mean_zipf_content", "median_zipf_content", "share_rare_content", "share_below4_content",
           "mean_word_length", "kandel_moles", "mean_zipf_form_films"]
BLINDED = LEXICAL + ["n_words", "n_sentences", "words_per_sentence", "share_oov"]


def load_lexicon(path):
    try:
        df = pd.read_csv(path, sep="\t", dtype=str, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(path, sep="\t", dtype=str, encoding="latin-1")
    df.columns = [re.sub(r"^\d+_", "", c) for c in df.columns]
    for c in ["ortho", "lemme"]:  # same spelling as the texts (ligatures, apostrophes)
        df[c] = df[c].map(lambda v: normalise(v) if isinstance(v, str) else v)
    for c in ["freqfilms2", "freqlivres", "freqlemfilms2", "freqlemlivres"]:
        df[c] = df[c].fillna("0").str.replace(",", ".").astype(float)
    df["nbsyll"] = pd.to_numeric(df["nbsyll"], errors="coerce")
    df["cat"] = df["cgram"].fillna("")  # full tag: ADJ:pos, ADJ:num and the like are not content words
    df["formfreq"] = df["freqfilms2"] + df["freqlivres"]
    # reading of a form: the lemma with the largest summed form frequency, then its most frequent row
    by_lemma = df.groupby(["ortho", "lemme"], as_index=False)["formfreq"].sum()
    by_lemma = by_lemma.sort_values(["formfreq", "lemme"], ascending=[False, True], kind="mergesort")
    top = by_lemma.groupby("ortho").first()["lemme"].rename("top_lemme")
    df = df.join(top, on="ortho")
    df = df[df["lemme"] == df["top_lemme"]]
    df = df.sort_values(["formfreq", "cat"], ascending=[False, True], kind="mergesort")
    best = df.groupby("ortho").first()
    lex = {
        o: (r["cat"], r["lemme"], (r["freqlemfilms2"] + r["freqlemlivres"]) / 2, r["freqfilms2"], r["nbsyll"])
        for o, r in best.iterrows()
    }
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    return lex, sha


def normalise(text):
    return (text or "").replace("’", "'").replace("‘", "'").replace("œ", "oe").replace("Œ", "Oe") \
        .replace("æ", "ae").replace("Æ", "Ae")


def edge_lines(text):
    """Non-empty lines without markdown marks or label lines, each with its own title mark."""
    out = []
    for l in normalise(text).splitlines():
        l = l.strip()
        if not l:
            continue
        marked = l.startswith("#") or re.fullmatch(r"(\*\*|__).+(\*\*|__)", l) is not None
        plain = " ".join(re.sub(r"[#*_]+", " ", l).split())
        if plain and re.search(f"[{LETTERS}]", plain) and not LABEL_LINE_RE.match(plain):
            out.append((plain, marked))
    return out


def is_preface(line):
    return line.endswith(":") or PREFACE_RE.match(line) is not None or VOICI_META_RE.match(line) is not None or \
        (VOICI_RE.match(line) is not None and AUDIENCE_RE.search(line) is not None)


def clean_info(text):
    items = edge_lines(text)
    head = tail = 0
    while len(items) > 1 and head < 2 and is_preface(items[0][0]):
        items, head = items[1:], head + 1
    while len(items) > 1 and tail < 3 and POSTFACE_RE.match(items[-1][0]):
        items, tail = items[:-1], tail + 1
    title = ""
    if len(items) > 1:
        first, marked = items[0]
        labelled = TITLE_LABEL_RE.match(first) is not None
        short = len(first.split()) <= 12 and not first.rstrip().endswith((".", "…"))
        if marked or labelled or short:
            title, items = TITLE_LABEL_RE.sub("", first), items[1:]
    lines = [re.sub(r"^(texte|text)\s*:\s*", "", l, flags=re.IGNORECASE) for l, _ in items]
    return {"title": title, "lines": [l for l in lines if l], "n_meta_lines": head + tail}


def clean(text):
    info = clean_info(text)
    return info["title"], info["lines"]


def title_like(line):
    return len(line.split()) <= 12 and not line.rstrip().endswith((".", "…", "!", "?", ":"))


def is_refusal_text(text):
    """REFUSAL_RE at the start of one of the first two lines, directly or after a polite opener; a
    first line that reads as a title is not tested when at least 20 words follow it."""
    items = edge_lines(text)
    rest_words = sum(len(TOKEN_RE.findall(l)) for l, _ in items[1:])
    for i, (line, _) in enumerate(items[:2]):
        if i == 0 and title_like(line) and rest_words >= MIN_WORDS:
            continue
        if REFUSAL_RE.match(line):
            return True
        m = OPENER_RE.match(line)
        if m and m.end() > 0 and REFUSAL_RE.match(line[m.end():]):
            return True
    return False


def flag_meta(text):
    """An answer that addresses the user in its first two or last three lines, outside quotation
    marks and dialogue lines. Kept, flagged, removed in a sensitivity analysis."""
    items = edge_lines(text)
    edge = items if len(items) <= 5 else items[:2] + items[-3:]
    for line, _ in edge:
        if line.startswith(DIALOGUE_START):
            continue
        unquoted = QUOTED_RE.sub(" ", line)
        if META_RE.search(unquoted) or any("?" in s and LABEL_Q_RE.search(s) for s in SENTENCE_END_RE.split(unquoted)):
            return True
    return False


def split_token(tok, lex):
    low = tok.lower()
    if low in lex:
        return [tok]
    if "'" in tok and not tok.endswith("'"):
        i = tok.index("'")
        return [tok[: i + 1]] + split_token(tok[i + 1:], lex)
    if "-" in tok:
        for c in CLITICS:
            if low.endswith(c) and low[: -len(c)] in lex:
                return [tok[: -len(c)]]
        return [p for part in tok.split("-") if part for p in split_token(part, lex)]
    return [tok]


def sentences(lines):
    out = []
    for line in lines:
        for s in re.split(r"(?<=[.!?…])\s+", line):
            if re.search(f"[{LETTERS}]", s):
                out.append(s)
    return out


def analyse(lines, lex):
    sents = []
    for s in sentences([normalise(l) for l in lines]):
        toks, prev_end = [], 0
        for i, m in enumerate(TOKEN_RE.finditer(s)):
            initial = i == 0 or INITIAL_GAP_RE.search(s[prev_end:m.start()]) is not None
            prev_end = m.end()
            for j, t in enumerate(split_token(m.group(0), lex)):
                toks.append((t, initial and j == 0))
        if toks:
            sents.append(toks)
    noninitial_caps = {t for s in sents for (t, ini) in s if not ini and t[:1].isupper()}
    rows = []
    for s in sents:
        for t, initial in s:
            low = t.lower()
            if low in ELIDED:
                rows.append((t, low, False))
                continue
            is_cap = t[:1].isupper()
            name = is_cap and (not initial or low not in lex or t in noninitial_caps)
            rows.append((t, low, name))
    return sents, rows


def zipf(freq):
    return math.log10(freq + SMOOTH) + 3


def measure(lines, lex):
    sents, rows = analyse(lines, lex)
    n = len(rows)
    if n == 0:
        return {"n_words": 0, "share_oov": float("nan")}, []
    content, content_lemmas, form_z, lengths, syl = [], [], [], [], 0
    oov = 0
    for t, low, name in rows:
        if low in ELIDED:
            syl += 1
            lengths.append(len(low) - 1)
            continue
        entry = lex.get(low)
        if entry is None:
            oov += 1
        nb = entry[4] if entry is not None and not math.isnan(entry[4]) else None
        if nb is None:
            g = len(re.findall(f"[{VOWELS}]+", low))
            nb = max(g - (1 if low.endswith("e") and g > 1 else 0), 1)
        syl += nb
        if name:
            continue
        lengths.append(len(low.replace("'", "").replace("-", "")))
        if entry is None:
            content.append(zipf(0.0))
            content_lemmas.append(low)
            form_z.append(zipf(0.0))
            continue
        cat, lemma, lemfreq, formfilms, _ = entry
        if cat in CONTENT and lemma not in EXCLUDED_LEMMAS:
            content.append(zipf(lemfreq))
            content_lemmas.append(lemma)
            form_z.append(zipf(formfilms))
    wps = n / len(sents)
    nan = float("nan")
    m = {
        "n_words": n,
        "n_sentences": len(sents),
        "n_content": len(content),
        "share_oov": oov / n,
        "mean_zipf_content": sum(content) / len(content) if content else nan,
        "median_zipf_content": statistics.median(content) if content else nan,
        "share_rare_content": sum(z < 3 for z in content) / len(content) if content else nan,
        "share_below4_content": sum(z < 4 for z in content) / len(content) if content else nan,
        "mean_word_length": sum(lengths) / len(lengths) if lengths else nan,
        "words_per_sentence": wps,
        "kandel_moles": 207 - 1.015 * wps - 73.6 * syl / n,
        "mean_zipf_form_films": sum(form_z) / len(form_z) if form_z else nan,
    }
    return m, content_lemmas


def exclusion_reason(rec, m):
    if not rec.get("ok"):
        return "failed call"
    if rec.get("finish_reason") in REFUSAL_FINISH or is_refusal_text(rec.get("text", "")):
        return "refusal"
    if m.get("n_words", 0) < MIN_WORDS:
        return "under 20 words"
    if m.get("share_oov", 0) > MAX_OOV:
        return "not French"
    return ""


def raw_records(raw_glob, prefix=""):
    for f in sorted(glob.glob(raw_glob)):
        for line in open(f, encoding="utf-8"):
            r = json.loads(line)
            if r["call_id"].startswith(prefix):
                yield f, r


def compute(lex_path, raw_glob, out_csv, prefix="", blind_labels=()):
    lex, lex_sha = load_lexicon(lex_path)
    rows = {}
    for f, r in raw_records(raw_glob, prefix):
        if r.get("kind") != "text":
            continue
        base = r["call_id"].split("-r")[0]
        info = clean_info(r.get("text", ""))
        title, body = info["title"], info["lines"]
        m, _ = measure(body, lex) if r.get("ok") else ({"n_words": 0, "share_oov": float("nan")}, [])
        reason = exclusion_reason(r, m)
        if r.get("label") in blind_labels:
            m = {k: (float("nan") if k in BLINDED else v) for k, v in m.items()}
            title = ""
        row = {k: r.get(k) for k in ["call_id", "block", "model", "grade", "label", "genre", "topic", "model_returned", "finish_reason"]}
        row.update(base_call=base, attempt=2 if r["call_id"] != base else 1, raw_file=f,
                   text_sha256=r.get("text_sha256"), title=title, kept=not reason, exclusion_reason=reason,
                   truncated=r.get("finish_reason") in TRUNCATED_FINISH,
                   n_meta_lines=info["n_meta_lines"], flag_meta=flag_meta(r.get("text", "")), **m)
        prev = rows.get(base)
        if prev is None or (not prev["kept"] and not reason) or (not prev["kept"] and row["attempt"] > prev["attempt"]):
            rows[base] = row
    df = pd.DataFrame(rows.values())
    if len(df):
        df["duplicate_text"] = df.duplicated("text_sha256", keep=False) & df["kept"]
        for c in LEXICAL:
            if c not in df:
                df[c] = float("nan")
    df.to_csv(out_csv, index=False)
    summary = {"rows": len(df), "excluded": int((~df["kept"]).sum()) if len(df) else 0,
               "lexicon_sha256": lex_sha, "blinded_labels": sorted(blind_labels)}
    print(json.dumps(summary))
    return df


def probes(raw_glob, out_csv, prefix=""):
    rows = {}
    for f, r in raw_records(raw_glob, prefix):
        if r.get("kind") != "probe":
            continue
        row = {k: r.get(k) for k in ["call_id", "model", "grade", "notation", "probe", "rep", "truth_age_from",
                                     "truth_age_to", "ok", "finish_reason", "model_returned", "text"]}
        prev = rows.get(r["call_id"])
        if prev is None or (not prev["ok"] and r.get("ok")):
            rows[r["call_id"]] = row
    df = pd.DataFrame(rows.values())
    df.to_csv(out_csv, index=False)
    print(json.dumps({"probes": len(df), "ok": int(df["ok"].sum()) if len(df) else 0}))
    return df


def retry_list(lex_path, raw_glob, calls_path, out_path):
    """Write the calls to re-request once: text calls whose first attempt returned an answer that
    is a refusal, under 20 words or not French, and that have no retry yet. Calls that failed at
    the transport level are not listed here; a rerun of the same call file resumes them."""
    lex, _ = load_lexicon(lex_path)
    calls = {json.loads(l)["call_id"]: json.loads(l) for l in open(calls_path, encoding="utf-8")}
    first, retried = {}, set()
    for _, r in raw_records(raw_glob):
        cid = r["call_id"]
        if cid.endswith("-r1"):
            retried.add(cid[:-3])
        elif cid in calls and r.get("ok"):
            first[cid] = r
    out = []
    for cid, r in first.items():
        if cid in retried or r.get("kind") != "text":
            continue
        m, _ = measure(clean(r.get("text", ""))[1], lex)
        if exclusion_reason(r, m):
            out.append(dict(calls[cid], call_id=cid + "-r1", retry_of=cid))
    with open(out_path, "w", encoding="utf-8") as f:
        for c in out:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(json.dumps({"retry_file": out_path, "n": len(out)}))
    return len(out)


GOLDEN = [
    # Short texts written for this test only. Expected content lemmas follow the rules in the
    # docstring, checked by hand against the Lexique readings.
    ("Le ciel\nLéa regarda le ciel. « C'est beau », dit-elle. Aujourd’hui, Pierre n’a pas peur.",
     ["regarder", "ciel", "beau", "dire", "peur"], 2),
    ("Rose cueille une rose dans le jardin. Le soir, Rose montre la fleur à Tom.",
     ["cueillir", "rose", "jardin", "soir", "montrer", "fleur"], 3),
    ("Les volcans se forment lorsque le magma remonte. Aujourd'hui, quelqu'un les observe, demanda-t-il.",
     ["volcan", "former", "magma", "remonter", "observer", "demander"], 0),
    ("Il est très content. Il a été au marché, puis il est rentré.",
     ["content", "marché", "rentrer"], 0),
    ("Je m'appelle Tom et j'aime le pain qu'il fait jusqu'à midi.",
     ["appeler", "aimer", "pain", "faire", "midi"], 1),
    ("Sa maman lui donne deux pommes. Cette forêt est grande, et chaque arbre a ses feuilles.",
     ["maman", "donner", "pomme", "forêt", "grand", "arbre", "feuille"], 0),
    ("Le robot-jardinier arrose les fleurs.",
     ["robot", "jardinier", "arroser", "fleur"], 0),
    ("Léa dit : « Regarde ! Ma sœur arrive. » Alors Tom répond : « Je suis content. »",
     ["dire", "regarder", "soeur", "arriver", "répondre", "content"], 2),
    ("Le chat dort.\nLe chien joue.\nLa lune brille.",
     ["chat", "dormir", "chien", "jouer", "lune", "briller"], 0),
    ("Titre : La ruche\nHistoire :\nTexte : Les abeilles vivent dans la ruche. Mon cœur bat.",
     ["abeille", "vivre", "ruche", "coeur", "battre"], 0),
    ("Voici une histoire pour des élèves de 8 à 9 ans :\nLe hérisson\nLe hérisson dort sous les feuilles.",
     ["hérisson", "dormir", "feuille"], 0),
    # v0.4: a bold label line before a body without title keeps the body's first line
    ("**Texte**\nLe chat dort sur le tapis.\nIl attend la souris.",
     ["chat", "dormir", "tapis", "attendre", "souris"], 0),
    # v0.4: a preface without a colon and a closing line addressed to the user are removed
    ("Voici une histoire pour des élèves de 8 à 9 ans.\nLe hérisson\nLe hérisson dort sous les feuilles.\n"
     "N'hésitez pas à me demander une version plus courte pour vos élèves !",
     ["hérisson", "dormir", "feuille"], 0),
    ("Bien sûr ! Voici un texte sur le thème des abeilles.\n## Les abeilles\nLes abeilles butinent les fleurs.\n"
     "Bonne lecture !", ["abeille", "butiner", "fleur"], 0),
    # v0.4: tout, autre and même are not content words
    ("Tous les enfants jouent avec une autre balle, toujours la même.",
     ["enfant", "jouer", "balle"], 0),
    # v0.4: a hyphen standing alone between spaces opens a reply like a dash
    ("Le soir, Léa cria - Regarde la lune ! - Elle brille, répondit Tom.",
     ["soir", "crier", "regarder", "lune", "briller", "répondre"], 2),
    # v0.4.1: a story opening with Voici and a grade label is not a preface
    ("Voici Léa, une élève de 5H.\nLéa aime les volcans.",
     ["élève", "aimer", "volcan"], 3),
    # v0.4.1: rules ("---") neither become the title nor block the removal of a closing line
    ("Voici une histoire pour des élèves de 8 à 9 ans.\n---\n## Le hérisson\nLe hérisson dort sous les feuilles.\n"
     "---\nBonne lecture !", ["hérisson", "dormir", "feuille"], 0),
    # v0.4.1: "Voici une histoire" is a preface, a word count is a closing line, a note about the
    # subject is kept while a note about the text is removed
    ("Voici une histoire sur les volcans.\nLe volcan qui tousse\nLe volcan tousse et crache de la fumée.\n"
     "N.B. : le vocabulaire a été simplifié pour des élèves de 5H.\n(Environ 80 mots)\nDites-moi si vous voulez une suite !",
     ["volcan", "tousser", "cracher", "fumée"], 0),
    ("Les volcans\nUn volcan crache des cendres.\nNote : le magma refroidit et devient une roche.",
     ["volcan", "cracher", "cendre", "note", "magma", "refroidir", "devenir", "roche"], 0),
    # v0.4.1: a closing line that only starts with the word note is kept
    ("Le carnet\nLéo ouvre son carnet.\nNote bien ce que tu vois, dit maman.",
     ["ouvrir", "carnet", "note", "voir", "dire", "maman"], 1),
]
# v0.4: answers that must be excluded as refusals or requests for clarification, and texts that
# must be kept although they contain one of the phrases (a title, a story opening, a reply in the
# middle of the text).
STORY = "Le loup regarde la forêt. Il cherche un abri pour la nuit. La pluie tombe sur les arbres. " * 2
REFUSALS = [
    "Je suis désolé, mais je ne connais pas le degré 5H. Pourriez-vous préciser l'âge des élèves ?",
    "Désolé, je ne peux pas écrire ce texte sans savoir ce que signifie 5H.",
    "Merci pour votre demande ! Pouvez-vous préciser ce que vous entendez par 5P ?",
    "Bien sûr ! Pourriez-vous m'indiquer l'âge des élèves de 5H ?",
    "Malheureusement, je ne connais pas le système 5H.",
    "Pourriez-vous préciser le niveau ?\nS'agit-il du système HarmoS ou d'un autre système scolaire ?",
    "**Désolé !**\nJe ne peux pas répondre sans plus d'informations sur le degré 5P, " + STORY,
    "Je ne suis pas sûr de comprendre ce que signifie 5H. " + STORY,
    "Je ne comprends pas ce que signifie 5H. Pourrais-tu préciser l'âge des élèves ?",
    "Je suis désolé\nJe ne sais pas ce que veut dire 5H.",
    "Désolé, je ne peux pas écrire ce texte\nMerci de votre compréhension.",
    "Pourrais-tu me préciser l'âge des élèves de 5H ?",
    "Navré, je ne connais pas la notation 5P.",
    "Qu'entends-tu par 5H exactement ?",
    # v0.4.2: requests in tu without "me", as the prompt itself uses tu
    "Peux-tu préciser l'âge des élèves de 5H ? Je pourrai alors écrire une histoire sur les volcans.",
    "Qu'entends-tu exactement par 5H ?",
    "Dis-moi quel âge ont les élèves de 5H et j'écrirai l'histoire.",
    # v0.4.4: quelle, quels and quelles, which the word boundary of v0.4.3 had cut off
    "Peux-tu me dire à quelle classe correspond 5H ?",
    "Dis-moi quels âges ont les élèves de 5P et j'écrirai l'histoire.",
    "I'm sorry, I can't help with that.",
]
KEPT_DESPITE_PHRASE = [
    "Désolé, je ne peux pas venir\n" + STORY,
    "Désolé, petit lapin\n" + STORY,
    "Je ne peux pas dormir\n" + STORY,
    "**Je suis désolé**\n" + STORY,
    "Malheureusement, il pleuvait ce jour-là. " + STORY,
    "Le loup et le lapin\nLe lapin court dans le pré. « Je ne peux pas t'aider », dit le loup. " + STORY,
    "Le loup et le lapin\n" + STORY + "\nJe ne peux pas t'aider, pensa le loup.",
    "Le doudou perdu\nMalheureusement, j'ai perdu mon doudou ce matin. " + STORY,
    "Les araignées\nPeux-tu dire combien de pattes a une araignée ? " + STORY,
    "Le hibou\nQu'entends-tu, petit hibou, dans la nuit ? " + STORY,
    "Les araignées\nPeux-tu me dire combien de pattes a une araignée ? " + STORY,
    "Les oiseaux\nPeux-tu donner le nom de trois oiseaux qui migrent ? " + STORY,
    # v0.4.3: "quel" must end a word, so "quelque" does not open a request
    "Le secret\nDis-moi quelque chose de gentil, demanda Léa.\n" + STORY,
    "Les volcans\nPeux-tu me dire quelque chose sur les volcans ?\n" + STORY,
]
# Values written out by hand from Lexique 3.83 lemma frequencies (mean of films and books, per
# million): content 132.715, marché 68.395, rentrer 406.22. Zipf = log10(f + 0.031) + 3.
GOLDEN_MEAN_TEXT4 = 5.1890
ZIPF_OF_ZERO = 1.4914


def self_test(lex_path):
    lex, _ = load_lexicon(lex_path)
    ok = True
    for text, expected, n_names in GOLDEN:
        _, lines = clean(text)
        _, rows = analyse(lines, lex)
        names = sum(1 for _, _, nm in rows if nm)
        _, got = measure(lines, lex)
        if sorted(got) != sorted(expected) or names != n_names:
            print("FAIL", repr(text[:40]), "got", got, "names", names, "expected", expected, n_names)
            ok = False
        else:
            print("ok", repr(text[:40]), got)
    # numeric pins: the smoothing and the lemma frequencies, against values written out by hand, and
    # the word count of the first golden text (14 words once the title is removed and dit-elle
    # loses its clitic: Léa regarda le ciel C' est beau dit Aujourd'hui Pierre n' a pas peur)
    m4 = measure(clean(GOLDEN[3][0])[1], lex)[0]["mean_zipf_content"]
    n1 = measure(clean(GOLDEN[0][0])[1], lex)[0]["n_words"]
    if abs(zipf(0.0) - ZIPF_OF_ZERO) > 1e-4 or abs(m4 - GOLDEN_MEAN_TEXT4) > 1e-3 or n1 != 14:
        print("FAIL: numeric pins", round(zipf(0.0), 4), round(m4, 4), n1)
        ok = False
    else:
        print("ok numeric pins", round(zipf(0.0), 4), round(m4, 4), n1)
    # failure control: the same story with three different first names must give the same mean
    base = "{n} joue dans le jardin. Le chat de {n} saute sur une feuille. {n} rit."
    vals = []
    for name in ["Léa", "Pierre", "Chloé"]:
        m, _ = measure(clean(base.format(n=name))[1], lex)
        vals.append(m["mean_zipf_content"])
    if max(vals) - min(vals) > 1e-9:
        print("FAIL: the protagonist's name changes the measure", vals)
        ok = False
    else:
        print("ok names do not move the measure", round(vals[0], 3))
    # failure control: passé simple and présent of the same story give the same lemma measure
    m1, _ = measure(clean("Le loup regarda la forêt et répondit au renard.")[1], lex)
    m2, _ = measure(clean("Le loup regarde la forêt et répond au renard.")[1], lex)
    if abs(m1["mean_zipf_content"] - m2["mean_zipf_content"]) > 1e-9:
        print("FAIL: tense changes the lemma measure", m1["mean_zipf_content"], m2["mean_zipf_content"])
        ok = False
    else:
        print("ok tense does not move the measure", round(m1["mean_zipf_content"], 3))
    # failure control: planted rare words must lower the mean, planted frequent words must raise it
    story = "Le loup regarde la forêt. Il cherche un abri pour la nuit. La pluie tombe sur les arbres."
    m0 = measure(clean(story)[1], lex)[0]["mean_zipf_content"]
    rare = measure(clean(story + " L'ornithorynque contemple la saponaire flétrie.")[1], lex)[0]["mean_zipf_content"]
    freq = measure(clean(story + " Le petit homme veut voir la maison.")[1], lex)[0]["mean_zipf_content"]
    if not (rare < m0 < freq):
        print("FAIL: planted words do not move the mean as they should", rare, m0, freq)
        ok = False
    else:
        print("ok planted rare and frequent words move the mean", round(rare, 3), round(m0, 3), round(freq, 3))
    # failure control: exclusion rules decide on length, language and refusal only
    probe = {"ok": True, "finish_reason": "stop"}
    short = exclusion_reason(probe, measure(clean("Le chat dort.")[1], lex)[0])
    english = exclusion_reason(probe, measure(clean(" ".join(["The quick brown fox jumps over the lazy dog."] * 4))[1], lex)[0])
    refusal = exclusion_reason({"ok": True, "finish_reason": "content_filter"}, measure(clean(story * 3)[1], lex)[0])
    asked = "Pourriez-vous préciser ce que signifie 5H ? " + story * 2
    textual = exclusion_reason({"ok": True, "finish_reason": "stop", "text": asked}, measure(clean(asked)[1], lex)[0])
    if textual != "refusal":
        print("FAIL: a request for clarification is not excluded", textual)
        ok = False
    kept = exclusion_reason(probe, measure(clean(story * 3)[1], lex)[0])
    if (short, english, refusal, kept) != ("under 20 words", "not French", "refusal", ""):
        print("FAIL: exclusion rules", short, english, refusal, kept)
        ok = False
    else:
        print("ok exclusion rules", short, "|", english, "|", refusal, "| kept")
    # failure control, both directions: refusals and requests for clarification are excluded, and
    # texts that only contain a refusal phrase as a title, a story opening or a reply are kept
    def reason(text):
        return exclusion_reason({"ok": True, "finish_reason": "stop", "text": text}, measure(clean(text)[1], lex)[0])
    missed = [t[:50] for t in REFUSALS if reason(t) != "refusal"]
    wrong = [t[:50] for t in KEPT_DESPITE_PHRASE if reason(t) != ""]
    if missed or wrong:
        print("FAIL: refusal rule, missed", missed, "wrongly excluded", wrong)
        ok = False
    else:
        print(f"ok refusal rule, {len(REFUSALS)} refusals excluded, {len(KEPT_DESPITE_PHRASE)} texts with a phrase kept")
    # failure control: ligatures are found in the lexicon, also when the lexicon file spells them
    lig = measure(clean("Ma sœur arrive. Mon cœur bat.")[1], lex)[0]
    tmp = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False, encoding="utf-8")
    tmp.write("ortho\tlemme\tcgram\tfreqfilms2\tfreqlivres\tfreqlemfilms2\tfreqlemlivres\tnbsyll\n"
              "cœur\tcœur\tNOM\t200\t250\t320\t320\t1\nbat\tbattre\tVER\t10\t10\t50\t50\t1\n"
              "mon\tmon\tADJ:pos\t500\t500\t900\t900\t1\n")
    tmp.close()
    small, _ = load_lexicon(tmp.name)
    os.unlink(tmp.name)
    lig_small = measure(clean("Mon cœur bat.")[1], small)[0]
    if lig["share_oov"] != 0 or lig_small["share_oov"] != 0 or lig_small["n_content"] != 2:
        print("FAIL: ligatures not found in the lexicon", lig["share_oov"], lig_small)
        ok = False
    else:
        print("ok ligatures found in the lexicon, also when the file spells them")
    # failure control: meta lines are counted and flagged, dialogue is not
    meta_text = GOLDEN[12][0]
    offer = "Le hérisson\n" + story + "\nSouhaitez-vous une version plus longue de ce texte ?"
    dialogue = "Le lapin\nLe lapin demanda : « Voulez-vous jouer avec moi ? » " + story + "\n– Voulez-vous venir ? dit Tom."
    label_q = "Le hérisson\n" + story + "\nQue signifie 5H exactement ?"
    tu_req = "Pour écrire ce texte, peux-tu me préciser l'âge des élèves ?\n" + story
    need = "J'aurais besoin de savoir l'âge des élèves.\n" + story
    sais_tu = "Les abeilles\nSais-tu pourquoi les abeilles dansent ? " + story
    # v0.4.2: a time, a temperature and a label outside the question are not label questions
    time_q = "Le train\nÀ 8 h, où va le train de Léa ? " + story
    degrees = "L'hiver\nSais-tu qu'il peut faire moins 20 degrés en hiver ? " + story
    label_apart = "La ferme\nLes élèves de 5H visitent la ferme. Que vont-ils voir ? " + story
    label_q2 = "Quel âge ont les élèves de 5P ? Je voudrais adapter le vocabulaire.\n" + story
    n_meta = clean_info(meta_text)["n_meta_lines"]
    flags = tuple(flag_meta(t) for t in (meta_text, offer, dialogue, label_q, tu_req, need, sais_tu,
                                          time_q, degrees, label_apart, label_q2))
    if n_meta != 2 or flags != (True, True, False, True, True, True, False, False, False, False, True):
        print("FAIL: meta lines", n_meta, flags)
        ok = False
    else:
        print("ok meta lines removed and flagged, dialogue not flagged")
    print("OK" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    if sys.argv[1] == "--self-test":
        sys.exit(0 if self_test(sys.argv[2]) else 1)
    if sys.argv[1] == "--probes":
        probes(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
        sys.exit(0)
    compute(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
