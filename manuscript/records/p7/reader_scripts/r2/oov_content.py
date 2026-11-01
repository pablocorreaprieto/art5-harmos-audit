"""Out-of-lexicon content tokens (frequency 0 by the preregistered rule) by label, using compute.py's own tokeniser with
the pylexique copy of Lexique 3.83 (Latin-1; words with oe/ae ligatures are unreliable there and are set aside).
Runs from a COPY of the repository. Purpose: does the preregistered 'absent from Lexique = frequency 0' rule drive the L2 contrast?"""
import sys, json, glob, math, re, collections
import numpy as np, pandas as pd
from scipy import stats
sys.path.insert(0, sys.argv[1])
import compute as C
lex, sha = C.load_lexicon(sys.argv[2])
raw = {}
for f in sorted(glob.glob(sys.argv[1] + "/data/raw/calls_2026*.jsonl")):
    for l in open(f):
        r = json.loads(l)
        if r.get("kind") != "probe" and r.get("text"): raw[r["call_id"]] = r["text"]
meas = pd.read_csv(sys.argv[1] + "/results/measures.csv", keep_default_na=False, na_values=["", "nan", "NaN"])
rows = []; oov_words = collections.defaultdict(collections.Counter)
for r in meas.itertuples():
    title, lines = C.clean(raw[r.call_id])
    sents, toks = C.analyse(lines, lex)
    inlex, oov, skipped = [], 0, 0
    for t, low, name in toks:
        if low in C.ELIDED or name: continue
        e = lex.get(low)
        if e is None:
            if "oe" in low or "ae" in low: skipped += 1; continue
            oov += 1; oov_words[r.label][low] += 1; continue
        cat, lemma, lemfreq, _, _ = e
        if cat in C.CONTENT and lemma not in C.EXCLUDED_LEMMAS: inlex.append(C.zipf(lemfreq))
    n_c = len(inlex) + oov
    rows.append(dict(call_id=r.call_id, model=r.model, grade=r.grade, label=r.label, genre=r.genre, topic=r.topic, n_content_adj=n_c, oov=oov,
                     oov_share_content=oov / n_c if n_c else np.nan, z_inlex=np.mean(inlex) if inlex else np.nan,
                     z_all=(sum(inlex) + oov * C.zipf(0.0)) / n_c if n_c else np.nan))
d = pd.DataFrame(rows)
AGE = {"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}; G = list(AGE); ages = np.array(list(AGE.values())); c = ages - ages.mean()
def tv(a, b, col, kind="level"):
    x = d[d.label == a].set_index(["model","grade","genre","topic"])[col]; y = d[d.label == b].set_index(["model","grade","genre","topic"])[col]
    z = (x - y).dropna().rename("d").reset_index(); g = z.groupby(["topic","grade"]).d.mean().unstack("grade")[G]
    return g.mean(axis=1).values if kind == "level" else g.values @ (c / (c**2).sum())
print("mean share of content tokens that are OOV (non-name, frequency 0 by rule):", d.groupby("label").oov_share_content.mean().round(4).to_dict())
for a in ("L1","L1P","L2","L3","L4"):
    out = []
    for col in ("oov_share_content", "z_all", "z_inlex"):
        x = tv(a, "L5", col); t = stats.ttest_1samp(x, 0); out.append(f"{col} {x.mean():+.4f} (p={t.pvalue:.3f})")
    print(f"{a}-L5 level:", " | ".join(out))
print("most frequent OOV (non-name) words, L2 vs L5 (per 1000 texts):")
for lab in ("L2", "L5"):
    n = (d.label == lab).sum(); print(" ", lab, [(w, round(1000 * k / n, 1)) for w, k in oov_words[lab].most_common(14)])
d.to_csv(sys.argv[3], index=False)
