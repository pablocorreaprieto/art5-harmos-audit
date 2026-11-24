"""Post hoc analysis added after the data freeze (revision of 24.11.2026); reporting only.

Child-based norms. The preregistered measure reads lemma frequencies from Lexique 3.83, whose corpora are
written for adults (film subtitles and novels). Manulex (Lété, Sprenger-Charolles & Colé, 2004) gives lemma
frequencies from 54 French primary-school readers, separately for CP, CE1 and CE2 to CM2 and for the whole
CP to CM2 corpus. This script uses it in three ways.

1. Reader benchmarks on the preregistered scale. For each Manulex level, the token-weighted mean Zipf
   frequency, in Lexique, of the content lemmas of the readers of that level (nouns, qualifying adjectives
   and verbs, without the excluded lemmas, with the category matched in Lexique). Lexique is independent of
   Manulex, so the texts of the study and the school readers are placed on the same external scale.
2. Child-norm rescoring. Every kept text is scored again with the same content tokens, each lemma taking its
   Manulex CP to CM2 frequency (U, per million; a lemma absent from Manulex counts as frequency 0, as the
   preregistration does for Lexique). The four primary tests, the age rulers and the shifts and tracking by
   label and model are recomputed on this measure.
3. Coverage. The share of a text's content tokens attested in the readers of the level that matches the
   requested grade (3H with CP, 4H with CE1, 5H to 7H with CE2 to CM2; Manulex has no level for 8H).

python exploratory_manulex.py --manulex data/lexicon/Manulex-Lemmes.rds
    [--lexicon data/lexicon/Lexique383.tsv] [--out results/exploratory_manulex.json]

Needs the official Lexique 3.83 file (python pipeline.py --step lexicon) and the Manulex lemma table
distributed by Open Lexicon (Manulex-Lemmes.rds, md5 checked), so it runs in GitHub Actions
(.github/workflows/checks.yml, task manulex). With another lexicon file it runs for development only and
says so. Deterministic: rerunning gives the same file.
"""
import argparse
import hashlib
import json
import math
import os

import numpy as np
import pandas as pd

import analyze as A
import compute as C

EXPECTED_LEXICON_SHA16 = "637ba37a767a6667"
EXPECTED_MANULEX_MD5 = "12c1aeafd96d38baa1093934c4164ca9"
LEX_TO_MANULEX = {"NOM": "NC", "VER": "VER", "ADJ": "ADJ"}
MANULEX_TO_LEX = {v: k for k, v in LEX_TO_MANULEX.items()}
LEVELS = {"CP": "CP", "CE1": "CE1", "CE2-CM2": "CE2-CM2"}
GRADE_LEVEL = {"3H": "CP", "4H": "CE1", "5H": "CE2-CM2", "6H": "CE2-CM2", "7H": "CE2-CM2"}
REPORTED_LABELS = ["L1", "L1P", "L3", "L5"]


def num(v):
    """Manulex numbers are strings with spaces as thousands separators ('14 660.67'); missing means 0."""
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return 0.0
    s = str(v).replace(" ", "").replace(" ", "").replace(" ", "")
    if "," in s and "." not in s:
        s = s.replace(",", ".")
    return float(s) if s else 0.0


def load_manulex(path):
    raw = open(path, "rb").read()
    md5 = hashlib.md5(raw).hexdigest()
    if path.endswith(".rds"):
        import pyreadr
        df = list(pyreadr.read_r(path).values())[0]
    else:
        df = pd.read_csv(path, sep="\t", dtype=str, encoding="utf-8")
    df = df.copy()
    df["word"] = df["Word"].map(lambda w: C.normalise(str(w)).lower())
    for lev in list(LEVELS.values()) + ["CP-CM2"]:
        df[f"F_{lev}"] = df[f"{lev}_F"].map(num)
    df["U_all"] = df["CP-CM2_U"].map(num)
    by_key, by_word = {}, {}
    for r in df[df["SYNT"].isin(MANULEX_TO_LEX)].to_dict("records"):
        e = {"U": r["U_all"], "F": {lev: r[f"F_{lev}"] for lev in LEVELS.values()}}
        by_key[(r["word"], r["SYNT"])] = e
        best = by_word.get(r["word"])
        if best is None or e["U"] > best["U"]:
            by_word[r["word"]] = e
    return df, by_key, by_word, md5


def lexique_lemma_freqs(path):
    """(lemma, cgram) -> lemma frequency per million, as in compute.load_lexicon, for every row of Lexique."""
    try:
        lx = pd.read_csv(path, sep="\t", dtype=str, encoding="utf-8")
    except UnicodeDecodeError:
        lx = pd.read_csv(path, sep="\t", dtype=str, encoding="latin-1")
    lx.columns = [c.split("_", 1)[1] if c.split("_", 1)[0].isdigit() else c for c in lx.columns]
    lx["lemme"] = lx["lemme"].map(lambda v: C.normalise(v) if isinstance(v, str) else v)
    for c in ["freqlemfilms2", "freqlemlivres"]:
        lx[c] = lx[c].fillna("0").str.replace(",", ".").astype(float)
    lx["cat"] = lx["cgram"].fillna("")
    lx["lemfreq"] = (lx["freqlemfilms2"] + lx["freqlemlivres"]) / 2
    pairs = lx.groupby(["lemme", "cat"])["lemfreq"].max().to_dict()
    lemmas = set(lx["lemme"].dropna())
    return pairs, lemmas


def content_tokens(lines, lex):
    """The preregistered content tokens: (lemma or form, Lexique category or None, Lexique lemma frequency)."""
    _, rows = C.analyse(lines, lex)
    out = []
    for _t, low, name in rows:
        if low in C.ELIDED or name:
            continue
        entry = lex.get(low)
        if entry is None:
            out.append((low, None, 0.0))
            continue
        cat, lemma, lemfreq, _formfilms, _ = entry
        if cat in C.CONTENT and lemma not in C.EXCLUDED_LEMMAS:
            out.append((lemma, cat, lemfreq))
    return out


def manulex_entry(lemma, cat, by_key, by_word):
    if cat is not None:
        e = by_key.get((lemma, LEX_TO_MANULEX[cat]))
        if e is not None:
            return e, "exact"
    e = by_word.get(lemma)
    return (e, "lemma") if e is not None else (None, "absent")


def reader_benchmarks(mdf, pairs, lemmas):
    """Token-weighted mean Lexique Zipf of the content lemmas of each Manulex level."""
    rows = mdf[mdf["SYNT"].isin(MANULEX_TO_LEX) & ~mdf["word"].isin(C.EXCLUDED_LEMMAS)]
    out, kept_types, dropped_types = {}, 0, 0
    zs, keep = [], []
    for r in rows.to_dict("records"):
        cat = MANULEX_TO_LEX[r["SYNT"]]
        f = pairs.get((r["word"], cat))
        if f is not None:
            zs.append(C.zipf(f))
            keep.append(True)
        elif r["word"] in lemmas:  # in Lexique, but not as a content word of that category (ADJ:num and the like)
            zs.append(float("nan"))
            keep.append(False)
        else:  # absent from Lexique: frequency 0, as the preregistered rule
            zs.append(C.zipf(0.0))
            keep.append(True)
    rows = rows.assign(z_lexique=zs, keep=keep)
    kept_types, dropped_types = int(rows["keep"].sum()), int((~rows["keep"]).sum())
    k = rows[rows["keep"]]
    for lev in list(LEVELS.values()) + ["CP-CM2"]:
        w = k[f"F_{lev}"].to_numpy(float)
        z = k["z_lexique"].to_numpy(float)
        out[lev] = {"mean_zipf_lexique": float(np.sum(w * z) / np.sum(w)), "content_tokens": int(w.sum()),
                    "content_types": int((w > 0).sum())}
    return out, kept_types, dropped_types


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lexicon", default=os.environ.get("LEXIQUE", "data/lexicon/Lexique383.tsv"))
    ap.add_argument("--manulex", default="data/lexicon/Manulex-Lemmes.rds")
    ap.add_argument("--out", default="results/exploratory_manulex.json")
    a = ap.parse_args()
    lex, sha = C.load_lexicon(a.lexicon)
    official = sha.startswith(EXPECTED_LEXICON_SHA16)
    if not official:
        print(f"DEVELOPMENT RUN: lexicon {sha[:16]} is not the registered file; numbers are not reportable")
    mdf, by_key, by_word, md5 = load_manulex(a.manulex)
    if md5 != EXPECTED_MANULEX_MD5:
        raise SystemExit(f"unexpected Manulex file: md5 {md5}")
    pairs, lemmas = lexique_lemma_freqs(a.lexicon)

    df = pd.read_csv("results/measures.csv")
    df["kept"] = A.as_bool(df["kept"])
    kept = df[df["kept"]]
    raw = {}
    for f in sorted(set(kept["raw_file"])):
        for line in open(f, encoding="utf-8"):
            r = json.loads(line)
            raw[r["call_id"]] = r

    z_child, z_child_found, share_absent, cov, max_diff, n_mismatch = {}, {}, {}, {}, 0.0, 0
    match_counts = {"exact": 0, "lemma": 0, "absent": 0}
    for row in kept.itertuples():
        lines = C.clean_info(raw[row.call_id].get("text", ""))["lines"]
        toks = content_tokens(lines, lex)
        if len(toks) != row.n_content:
            n_mismatch += 1
            if official:
                raise SystemExit(f"content count differs for {row.call_id}: {len(toks)} vs {row.n_content}")
        if toks:
            m = sum(C.zipf(f) for _l, _c, f in toks) / len(toks)
            max_diff = max(max_diff, abs(m - row.mean_zipf_content))
        zs, zf, absent, att = [], [], 0, {lev: 0 for lev in LEVELS.values()}
        for lemma, cat, _f in toks:
            e, how = manulex_entry(lemma, cat, by_key, by_word)
            match_counts[how] += 1
            if e is None:
                zs.append(C.zipf(0.0))
                absent += 1
                continue
            zs.append(C.zipf(e["U"]))
            zf.append(C.zipf(e["U"]))
            for lev in LEVELS.values():
                att[lev] += e["F"][lev] > 0
        n = len(toks)
        z_child[row.call_id] = sum(zs) / n if n else float("nan")
        z_child_found[row.call_id] = sum(zf) / len(zf) if zf else float("nan")
        share_absent[row.call_id] = absent / n if n else float("nan")
        cov[row.call_id] = {lev: (att[lev] / n if n else float("nan")) for lev in LEVELS.values()}
    if official and max_diff > 1e-9:
        raise SystemExit(f"the recomputed measure differs from results/measures.csv by up to {max_diff}")

    d = df.copy()
    d["z_child"] = d["call_id"].map(z_child)
    d["z_child_found"] = d["call_id"].map(z_child_found)
    d["share_absent_manulex"] = d["call_id"].map(share_absent)
    for lev in LEVELS.values():
        d[f"cov_{lev}"] = d["call_id"].map(lambda c, lev=lev: cov[c][lev] if c in cov else float("nan"))
    k = d[d["kept"]]

    # 1. reader benchmarks on the preregistered (Lexique) scale, and the study's texts at the matching grades
    bench, kept_types, dropped_types = reader_benchmarks(mdf, pairs, lemmas)
    graded = k[k["grade"].isin(GRADE_LEVEL) & k["label"].isin(REPORTED_LABELS)].copy()
    graded["level"] = graded["grade"].map(GRADE_LEVEL)
    vs_readers = {}
    for (lev, lab), g in graded.groupby(["level", "label"]):
        ref = bench[lev]["mean_zipf_lexique"]
        by_model = g.groupby("model")[A.Y].mean()
        vs_readers.setdefault(lev, {})[lab] = {
            "grades": sorted(g["grade"].unique()), "mean_zipf_texts": float(g[A.Y].mean()),
            "minus_readers": float(g[A.Y].mean() - ref),
            "by_model_minus_readers": {m: float(v - ref) for m, v in by_model.items()},
            "models_below_readers": int((by_model < ref).sum())}

    # 2. child-norm rescoring: primary tests, rulers, shifts and tracking
    d2 = d.copy()
    d2.loc[d2["kept"], A.Y] = d2.loc[d2["kept"], "z_child"]
    ax = A.axes(d2[d2["label"].isin(A.GRADED_LABELS)])
    primary = A.primary_from_cubes(A.to_cubes(d2, A.Y, ax))
    h1 = A.h1_slopes(d2)
    aeb = A.age_equivalent_block(d2, h1, ax)
    d3 = d.copy()
    d3.loc[d3["kept"], A.Y] = d3.loc[d3["kept"], "z_child_found"]
    primary_found = A.primary_from_cubes(A.to_cubes(d3, A.Y, A.axes(d3[d3["label"].isin(A.GRADED_LABELS)])))
    corr = float(k[["z_child", A.Y]].corr().iloc[0, 1])

    # 3. coverage by the readers of the matching level
    coverage = {}
    for g_, lev in GRADE_LEVEL.items():
        sub = k[(k["grade"] == g_) & k["label"].isin(REPORTED_LABELS)]
        coverage[g_] = {"level": lev, "by_label": {lab: float(s[f"cov_{lev}"].mean()) for lab, s in sub.groupby("label")},
                        "by_model_label": {f"{m} | {lab}": float(s[f"cov_{lev}"].mean())
                                           for (m, lab), s in sub.groupby(["model", "label"])}}

    tok = sum(match_counts.values())
    out = {
        "note": "post hoc (revision of 24.11.2026); preregistered measure and analyses unchanged, see the docstring",
        "official_lexicon": official,
        "lexicon_sha256": sha,
        "manulex_md5": md5,
        "manulex_source": "Open Lexicon, datasets-info/Lete_2004_Manulex/Manulex-Lemmes.rds",
        "n_texts": int(len(k)),
        "content_count_mismatches": n_mismatch,
        "max_abs_diff_recomputed_vs_archived": max_diff,
        "content_tokens": tok,
        "manulex_match": {key: {"tokens": v, "share": v / tok} for key, v in match_counts.items()},
        "share_absent_by_model": {m: float(np.average(g["share_absent_manulex"], weights=g["n_content"]))
                                  for m, g in k.groupby("model")},
        "reader_benchmarks_lexique_scale": bench,
        "reader_benchmark_lemma_types": {"kept": kept_types, "dropped_not_content_in_lexique": dropped_types},
        "texts_vs_readers": vs_readers,
        "correlation_child_norm_vs_preregistered": corr,
        "child_norm_h1": h1,
        "child_norm_primary": primary,
        "child_norm_primary_found_only": primary_found,
        "child_norm_age_equivalents": aeb,
        "coverage_matching_level": coverage,
    }
    json.dump(out, open(a.out, "w"), indent=1, ensure_ascii=False, default=float)
    print(json.dumps({key: out[key] for key in ("official_lexicon", "n_texts", "content_count_mismatches",
                                                "max_abs_diff_recomputed_vs_archived")}))
    print("readers", {lev: round(v["mean_zipf_lexique"], 3) for lev, v in bench.items()})
    for name, v in primary.items():
        print("child norm", name, round(v["estimate"], 5), "p =", round(v["p_two_sided"], 4),
              "Holm p =", round(v["p_holm"], 4))
    print("PASS exploratory_manulex" if official else "DEVELOPMENT RUN ONLY")


if __name__ == "__main__":
    main()
