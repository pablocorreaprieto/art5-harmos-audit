# -*- coding: utf-8 -*-
"""Answer battery: hand-written answers of the kind chat models give to the study prompt, run through
the cleaning, exclusion and flag rules of compute.py. Two sets: the 49 answers of the v0.4
confirmation session (battery_answers.py, 33 plausible and 16 edge) and the 10 answers of the v0.4.1
confirmation session (battery_answers41.py). For each answer the check counts genuine lines removed,
lines addressed to the user left in the text, a wrong title, an exclusion, and a flag on an answer
that has no line addressed to the user.
Gate: every count is 0 on the plausible answers of the first set; on the edge answers of the first
set and on the second set, no count exceeds the value recorded for v0.4.2 (LIMITS). Exits 1 otherwise.
Harness written by the v0.4 confirmation session (claude-sonnet-5-5, t6_battery.py), adapted by the
main session (claude-opus-5-5): paths, second answer set, gate."""
import importlib.util
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import code_dir, lexicon
import battery_answers
import battery_answers41

# recorded for v0.4.2 (see checks/README.md); a count above its limit fails the gate
LIMITS = {"edge": {"lost": 3, "leaked": 0, "title": 0, "excluded": 0, "flagged": 3},
          "set41": {"lost": 4, "leaked": 0, "title": 0, "excluded": 0, "flagged": 1}}

spec = importlib.util.spec_from_file_location("compute_under_test", os.path.join(code_dir(), "compute.py"))
compute = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compute)
lex, _ = compute.load_lexicon(lexicon())

LIST_RE = re.compile(r"^(- |\d+\. )")


def render(pieces):
    out, prev = [], None
    for kind, txt in pieces:
        if kind == "title" and txt == "x":
            continue
        if out and prev is not None and LIST_RE.match(txt) and LIST_RE.match(prev):
            out[-1] += "\n" + txt
        else:
            out.append(txt)
        prev = txt
    return "\n\n".join(out)


def canon(s):
    s = compute.normalise(s)
    s = re.sub(r"^(titre|title)\s*:\s*", "", re.sub(r"[#*_]+", " ", s).strip(), flags=re.I)
    return re.sub(r"[\W_]+", "", s.lower())


def run(answers, tag):
    rows = []
    for a in answers:
        text = render(a["pieces"])
        info = compute.clean_info(text)
        out_lines = [canon(l) for l in info["lines"]]
        out_title = canon(info["title"])
        exp_title = next((canon(t) for k, t in a["pieces"] if k == "title" and t != "x"), "")
        bodies = [(canon(t), t) for k, t in a["pieces"] if k == "body"]
        metas = [(canon(t), t) for k, t in a["pieces"] if k == "meta"]
        lost = [t for c, t in bodies if c not in out_lines and c != out_title]
        leaked = [t for c, t in metas if c in out_lines]
        m, _ = compute.measure(info["lines"], lex)
        reason = compute.exclusion_reason({"ok": True, "finish_reason": "stop", "text": text}, m)
        fm = compute.flag_meta(text)
        r = dict(id=a["id"], plaus=a["plaus"], lost=lost, leaked=leaked, title_ok=out_title == exp_title,
                 excluded=reason, flagged=bool(fm and not metas))
        rows.append(r)
        issue = lost or leaked or not r["title_ok"] or reason or r["flagged"]
        print(f"{tag} {a['id']} {a['plaus'][:4]} words={m['n_words']:3d} meta {info['n_meta_lines']}/{len(metas)} "
              f"title_ok={str(r['title_ok']):5s} excl={reason or '-':8s} {'FLAG' if fm else '    '} {'<<< ISSUE' if issue else ''}")
        if lost: print("      genuine lines REMOVED:", [x[:70] for x in lost])
        if leaked: print("      meta lines LEFT IN TEXT:", [x[:70] for x in leaked])
        if not r["title_ok"]: print("      title found:", repr(info["title"]), "expected:", exp_title[:50])
        if reason: print("      EXCLUDED as", reason)
        if r["flagged"]: print("      genuine text FLAGGED by flag_meta")
    return rows


def summ(rs):
    return {"n": len(rs), "lost": sum(bool(r["lost"]) for r in rs), "leaked": sum(bool(r["leaked"]) for r in rs),
            "title": sum(not r["title_ok"] for r in rs), "excluded": sum(bool(r["excluded"]) for r in rs),
            "flagged": sum(r["flagged"] for r in rs)}


r49 = run(battery_answers.A, "B49")
r10 = run(battery_answers41.A, "B10")
res = {"plausible": summ([r for r in r49 if r["plaus"] == "plausible"]),
       "edge": summ([r for r in r49 if r["plaus"] == "edge"]), "set41": summ(r10)}
for k, s in res.items():
    print(f"{k.upper()}: n={s['n']} | genuine line removed in {s['lost']} | meta left in {s['leaked']} | "
          f"title wrong in {s['title']} | excluded {s['excluded']} | genuine flagged {s['flagged']}")
bad = [f"plausible {k}={v}" for k, v in res["plausible"].items() if k != "n" and v != 0]
for part in ("edge", "set41"):
    bad += [f"{part} {k}={res[part][k]} > {lim}" for k, lim in LIMITS[part].items() if res[part][k] > lim]
print(json.dumps(res))
print("PASS battery" if not bad else "FAIL battery: " + "; ".join(bad))
sys.exit(0 if not bad else 1)
