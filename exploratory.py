"""Exploratory analyses listed in the preregistration (question 8) but not computed by analyze.py.

1. Knowledge probes: direction of the errors. For each model and notation, the mean signed error of
   the first age range stated (midpoint minus the true midpoint, in years), with the probe parser of
   analyze.py (analyze.parse_probe), and the share of parsed answers whose first range has its
   midpoint above (too old) or below (too young) the true range widened by half a year, the
   preregistered rule for a correct answer.
2. Explicit mention of an age or a grade in the outputs: share of kept texts, by label, whose
   measured text (compute.clean, title excluded) names an age ("8 ans", "huit ans") or a school grade
   ("5H", "5P", "5e", "CE2", "CM1", "6e année"...).

Reads results/probes.csv and results/measures.csv plus the raw files (texts), writes
results/exploratory.json. Labelled exploratory in the manuscript; no test is corrected or added to
the confirmatory family. Written by the main session (claude-opus-5-5) on 1.11.2026, after the deposit.
"""
import glob
import json
import re

import numpy as np
import pandas as pd

import analyze
import compute

NUM_WORDS = "un|une|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|treize|quatorze|quinze"
AGE_MENTION = re.compile(rf"\b(\d{{1,2}}|{NUM_WORDS})\s*(?:ans|an)\b", re.IGNORECASE)
GRADE_MENTION = re.compile(r"\b(\d{1,2}\s?[HP]|\d{1,2}\s?(?:e|ème|eme|ᵉ)(?:\s+année)?|CP|CE1|CE2|CM1|CM2)\b")


def probe_errors(p):
    out = {}
    for (m, notation), g in p.groupby(["model", "notation"]):
        errs, old, young = [], [], []
        for r in g.itertuples():
            ranges = analyze.parse_probe(r.text)
            if ranges:
                lo, hi = ranges[0]
                mid = (lo + hi) / 2
                errs.append(mid - (r.truth_age_from + r.truth_age_to) / 2)
                # outside the true range plus or minus half a year: the preregistered rule for "correct"
                old.append(mid > r.truth_age_to + 0.5)
                young.append(mid < r.truth_age_from - 0.5)
        e = np.array(errs, float)
        out[f"{m} | {notation}"] = {"n_parsed": int(len(e)), "mean_signed_error_years": float(e.mean()),
                                    "share_too_old": float(np.mean(old)), "share_too_young": float(np.mean(young))}
    return out


def mentions(meas):
    texts = {}
    for f in sorted(glob.glob("data/raw/calls_2026*.jsonl")):
        for line in open(f):
            r = json.loads(line)
            if r.get("kind") != "probe" and r.get("text"):
                texts[r["call_id"]] = r["text"]
    kept = meas[meas["kept"].astype(str).str.lower().isin(["true", "1"])]
    rows = []
    for r in kept.itertuples():
        title, lines = compute.clean(texts[r.call_id])
        body = "\n".join(lines)
        rows.append({"label": r.label, "model": r.model, "age": bool(AGE_MENTION.search(body)),
                     "grade": bool(GRADE_MENTION.search(body))})
    d = pd.DataFrame(rows)
    by_label = d.groupby("label")[["age", "grade"]].mean().to_dict(orient="index")
    by_label_model = d.groupby(["label", "model"])[["age", "grade"]].mean()
    return {"n_texts": int(len(d)),
            "by_label": {k: {"share_age": float(v["age"]), "share_grade": float(v["grade"])} for k, v in by_label.items()},
            "by_label_model": {f"{lab} | {m}": {"share_age": float(v["age"]), "share_grade": float(v["grade"])}
                               for (lab, m), v in by_label_model.iterrows()}}


def main():
    p = pd.read_csv("results/probes.csv", keep_default_na=False)
    meas = pd.read_csv("results/measures.csv", keep_default_na=False)
    out = {"note": "exploratory analyses of the preregistration (question 8), computed after the deposit",
           "probe_errors": probe_errors(p), "mentions": mentions(meas)}
    json.dump(out, open("results/exploratory.json", "w"), indent=1)
    print(json.dumps(out["probe_errors"], indent=1))
    print(json.dumps(out["mentions"]["by_label"], indent=1))


if __name__ == "__main__":
    main()
