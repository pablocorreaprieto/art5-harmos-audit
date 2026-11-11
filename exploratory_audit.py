"""Post hoc analysis added at the pre-submission audit of 2.11.2026, after the data freeze; reporting only.

Tokens absent from Lexique. As preregistered, a token absent from Lexique that is not a name counts as a
content word of frequency 0 (Zipf 1.49). A referee simulated at the audit found that some of these tokens are
artefacts of the lexicon rather than rare words (for example "tandis", which Lexique lists only inside
"tandis que", units such as "kg", onomatopoeia). This script
1. recomputes the preregistered measure of every kept text of the main run and checks that it equals
   results/measures.csv (so that the lexicon and the code are those of the archived results);
2. recomputes the measure without the absent tokens (mean Zipf of the content lemmas found in Lexique);
3. reports the share of absent tokens among content tokens, overall and by model and label, and the most
   frequent absent forms;
4. reruns the four primary tests (analyze.primary_from_cubes, Holm over the four) on the measure without the
   absent tokens.

python exploratory_audit.py [--lexicon data/lexicon/Lexique383.tsv] [--out results/exploratory_audit.json]

Needs the official Lexique 3.83 file (python pipeline.py --step lexicon), so it runs in GitHub Actions
(.github/workflows/checks.yml, task exploratory-audit). Deterministic: rerunning gives the same file.
Written by the main session (claude-opus-5-5) on 2.11.2026.
"""
import argparse
import collections
import json
import math
import os

import pandas as pd

import analyze as A
import compute as C

EXPECTED_LEXICON_SHA16 = "637ba37a767a6667"


def in_lexicon_measure(lines, lex):
    """Mean Zipf of the content lemmas found in Lexique, number of content tokens and of absent tokens."""
    _, rows = C.analyse(lines, lex)
    found, absent_forms = [], []
    for _t, low, name in rows:
        if low in C.ELIDED or name:
            continue
        entry = lex.get(low)
        if entry is None:
            absent_forms.append(low)
            continue
        cat, lemma, lemfreq, _formfilms, _ = entry
        if cat in C.CONTENT and lemma not in C.EXCLUDED_LEMMAS:
            found.append(C.zipf(lemfreq))
    mean = sum(found) / len(found) if found else float("nan")
    return mean, len(found) + len(absent_forms), absent_forms


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lexicon", default=os.environ.get("LEXIQUE", "data/lexicon/Lexique383.tsv"))
    ap.add_argument("--out", default="results/exploratory_audit.json")
    a = ap.parse_args()
    lex, sha = C.load_lexicon(a.lexicon)
    if not sha.startswith(EXPECTED_LEXICON_SHA16):
        raise SystemExit(f"not the registered lexicon: {sha[:16]}")
    df = pd.read_csv("results/measures.csv")
    df["kept"] = A.as_bool(df["kept"])
    kept = df[df["kept"]]
    raw = {}
    for f in sorted(set(kept["raw_file"])):
        for line in open(f, encoding="utf-8"):
            r = json.loads(line)
            raw[r["call_id"]] = r
    alt, n_content, n_absent, max_diff = {}, {}, {}, 0.0
    absent_counts = collections.Counter()
    for row in kept.itertuples():
        r = raw[row.call_id]
        lines = C.clean_info(r.get("text", ""))["lines"]
        m, _ = C.measure(lines, lex)
        max_diff = max(max_diff, abs(m["mean_zipf_content"] - row.mean_zipf_content))
        mean_in, n_c, forms = in_lexicon_measure(lines, lex)
        if n_c != row.n_content:
            raise SystemExit(f"content count differs for {row.call_id}: {n_c} vs {row.n_content}")
        alt[row.call_id], n_content[row.call_id], n_absent[row.call_id] = mean_in, n_c, len(forms)
        absent_counts.update(forms)
    if max_diff > 1e-9:
        raise SystemExit(f"the recomputed measure differs from results/measures.csv by up to {max_diff}")
    df2 = df.copy()
    df2.loc[df2["kept"], A.Y] = df2.loc[df2["kept"], "call_id"].map(alt)
    df2["n_absent_content"] = df2["call_id"].map(n_absent)
    df2["n_content_check"] = df2["call_id"].map(n_content)
    ax = A.axes(df2[df2["label"].isin(A.GRADED_LABELS)])
    primary = A.primary_from_cubes(A.to_cubes(df2, A.Y, ax))
    k = df2[df2["kept"]]
    by_cell = (k.groupby(["model", "label"])[["n_absent_content", "n_content_check"]].sum()
               .assign(share=lambda t: t["n_absent_content"] / t["n_content_check"]))
    out = {
        "note": "post hoc (pre-submission audit, 2.11.2026); preregistered measure unchanged, see the docstring",
        "lexicon_sha256": sha,
        "n_texts": int(len(k)),
        "max_abs_diff_recomputed_vs_archived": max_diff,
        "absent_content_tokens": int(k["n_absent_content"].sum()),
        "content_tokens": int(k["n_content_check"].sum()),
        "share_absent_among_content": float(k["n_absent_content"].sum() / k["n_content_check"].sum()),
        "share_absent_by_model_label": {f"{m} | {lab}": float(v) for (m, lab), v in by_cell["share"].items()},
        "share_absent_by_model": {m: float(g["n_absent_content"].sum() / g["n_content_check"].sum())
                                  for m, g in k.groupby("model")},
        "most_frequent_absent_forms": absent_counts.most_common(25),
        "primary_without_absent_tokens": primary,
    }
    json.dump(out, open(a.out, "w"), indent=1, ensure_ascii=False, default=float)
    print(json.dumps({key: out[key] for key in ("n_texts", "max_abs_diff_recomputed_vs_archived",
                                                "share_absent_among_content")}))
    for name, v in primary.items():
        print(name, round(v["estimate"], 5), "p =", round(v["p_two_sided"], 4), "Holm p =", round(v["p_holm"], 4))
    print("PASS exploratory_audit")


if __name__ == "__main__":
    main()
