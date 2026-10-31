"""Text measures for ART 5, prototype (design stage P1).

Primary measure: mean Zipf frequency of content-word tokens, from Lexique 3.83
film-subtitle form frequencies (column 9_freqfilms2, per million words).
Zipf = log10(frequency per million) + 3. Lower = rarer words = harder.
Out-of-lexicon tokens get frequency 0.01 per million (Zipf 1.0).
Proper nouns (capitalised tokens not at sentence start) are excluded.

Secondary: words per sentence, share of content tokens with Zipf < 3, number of
words, Kandel-Moles readability (207 - 1.015 x words/sentence - 73.6 x syllables/word).

Self-test (python measures.py) runs two failure controls and exits non-zero if
either fails: rare-word planting must lower the mean Zipf of every test text, and
the simpler of two test texts must get the higher mean Zipf.
"""
import math
import random
import re
import sys
from functools import lru_cache

import pandas as pd

LEXIQUE_PATH = "/usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt"
CONTENT_CGRAMS = {"NOM", "VER", "ADJ", "ADV"}
ELISIONS = {"l": "le", "d": "de", "j": "je", "qu": "que", "n": "ne", "s": "se", "c": "ce", "m": "me", "t": "te", "jusqu": "jusque", "lorsqu": "lorsque", "puisqu": "puisque"}
WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿŒœÆæ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿŒœÆæ]+)*'?")
SENT_RE = re.compile(r"[^.!?…]+[.!?…]+|[^.!?…]+$")
VOWELS = "aeiouyàâäéèêëîïôöùûüÿœæ"


@lru_cache(maxsize=1)
def lexicon():
    df = pd.read_csv(LEXIQUE_PATH, sep="\t", encoding="latin-1", usecols=["1_ortho", "4_cgram", "9_freqfilms2", "24_nbsyll"], dtype=str)
    df["freq"] = df["9_freqfilms2"].str.replace(",", ".").astype(float)
    df["nbsyll"] = pd.to_numeric(df["24_nbsyll"], errors="coerce")
    # one row per form: total frequency over homographs, cgram of the most frequent reading
    df = df.sort_values("freq", ascending=False)
    agg = df.groupby("1_ortho").agg(freq=("freq", "sum"), cgram=("4_cgram", "first"), nbsyll=("nbsyll", "first"))
    return agg


def zipf(freq_pm):
    return math.log10(max(freq_pm, 0.01)) + 3


def tokenize(text):
    sentences = [s.strip() for s in SENT_RE.findall(text) if s.strip()]
    out = []
    for s in sentences:
        toks = []
        for i, m in enumerate(WORD_RE.finditer(s)):
            w = m.group(0)
            proper = i > 0 and w[0].isupper()
            low = w.lower()
            if low.endswith("'"):
                low = ELISIONS.get(low[:-1], low[:-1])
            toks.append((low, proper))
        if toks:
            out.append(toks)
    return out


def syllables(word, lex):
    if word in lex.index and not math.isnan(lex.at[word, "nbsyll"]):
        return int(lex.at[word, "nbsyll"])
    groups = re.findall(f"[{VOWELS}]+", word)
    n = len(groups)
    if word.endswith("e") and n > 1:
        n -= 1
    return max(n, 1)


def measures(text):
    lex = lexicon()
    sents = tokenize(text)
    words = [w for s in sents for (w, p) in s]
    content = []
    for s in sents:
        for w, proper in s:
            if proper:
                continue
            if w in lex.index:
                if lex.at[w, "cgram"] in CONTENT_CGRAMS:
                    content.append(zipf(lex.at[w, "freq"]))
            else:
                content.append(zipf(0.0))  # out of lexicon counts as rare content
    n_words = len(words)
    n_sents = len(sents)
    syl = sum(syllables(w, lex) for w in words)
    wps = n_words / n_sents if n_sents else float("nan")
    spw = syl / n_words if n_words else float("nan")
    return {
        "n_words": n_words,
        "n_sentences": n_sents,
        "mean_zipf_content": sum(content) / len(content) if content else float("nan"),
        "share_rare_content": sum(z < 3 for z in content) / len(content) if content else float("nan"),
        "words_per_sentence": wps,
        "kandel_moles": 207 - 1.015 * wps - 73.6 * spw,
    }


def plant_rare_words(text, share=0.2, seed=1):
    """Failure control: replace a share of content words by rare words (Zipf < 2)."""
    lex = lexicon()
    rare = lex[(lex["freq"] < 0.1) & (lex["cgram"] == "NOM")].index.tolist()
    rng = random.Random(seed)
    tokens = text.split(" ")
    idx = [i for i, t in enumerate(tokens) if t.strip(".,!?;:").lower() in lex.index and lex.at[t.strip(".,!?;:").lower(), "cgram"] in CONTENT_CGRAMS]
    for i in rng.sample(idx, max(1, int(len(idx) * share))):
        punct = tokens[i][len(tokens[i].rstrip(".,!?;:")):]
        tokens[i] = rng.choice(rare) + punct
    return " ".join(tokens)


SELF_TEST_TEXTS = [
    # Two short texts written for this code test only (not data).
    "Le petit chat joue dans le jardin. Il saute sur une feuille. Sa maman le regarde et sourit.",
    "Les volcans se forment lorsque le magma remonte des profondeurs de la croûte terrestre. Leurs éruptions modifient durablement les paysages environnants.",
]


def self_test():
    ok = True
    for t in SELF_TEST_TEXTS:
        base = measures(t)
        planted = measures(plant_rare_words(t))
        print("base", {k: round(v, 3) for k, v in base.items()})
        print("planted", {k: round(v, 3) for k, v in planted.items()})
        if not planted["mean_zipf_content"] < base["mean_zipf_content"]:
            print("FAIL: planting rare words did not lower the mean Zipf")
            ok = False
    easy, hard = (measures(t)["mean_zipf_content"] for t in SELF_TEST_TEXTS)
    if not easy > hard:
        print("FAIL: the simpler test text is not rated easier")
        ok = False
    print("OK" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    sys.exit(0 if self_test() else 1)
