# -*- coding: utf-8 -*-
"""Clarification requests and genuine texts near a refusal phrase (cases in clarification_cases.py):
each case goes through clean_info, measure, exclusion_reason and flag_meta of compute.py, and gets
EXCL (excluded as a refusal), kept+FLAG or kept.
Gate (recorded for v0.4.2, see checks/README.md): at least MIN_CLARIF_EXCLUDED of the 21 requests
are excluded and at most MAX_GENUINE_EXCLUDED of the 16 genuine texts are excluded. Exits 1
otherwise. Harness adapted by the main session (claude-opus-5-5) from n2_n4_cases.py of the v0.4.1
confirmation session (claude-sonnet-5-5)."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import code_dir, lexicon
from clarification_cases import CLARIF, GENUINE

MIN_CLARIF_EXCLUDED = int(os.environ.get("MIN_CLARIF_EXCLUDED", "14"))  # v0.4.2: 14 (v0.4.1: 6, v0.4: 10)
MAX_GENUINE_EXCLUDED = int(os.environ.get("MAX_GENUINE_EXCLUDED", "8"))  # v0.4.2: 8 (v0.4.1: 8, v0.4: 10)

spec = importlib.util.spec_from_file_location("compute_under_test", os.path.join(code_dir(), "compute.py"))
compute = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compute)
lex, _ = compute.load_lexicon(lexicon())


def verdict(text):
    info = compute.clean_info(text)
    m, _ = compute.measure(info["lines"], lex)
    reason = compute.exclusion_reason({"ok": True, "finish_reason": "stop", "text": text}, m)
    if reason == "refusal":
        return "EXCL"
    if reason:
        return reason
    return "kept+FLAG" if compute.flag_meta(text) else "kept"


counts = {}
for title, cases in (("clarifications (expected EXCL)", CLARIF), ("genuine texts (expected kept)", GENUINE)):
    print(title)
    for lab, t in cases:
        v = verdict(t)
        counts.setdefault(title, []).append(v)
        print(f"  {lab:46s} {v}")
cl = counts["clarifications (expected EXCL)"]
ge = counts["genuine texts (expected kept)"]
n_ex, n_flag = sum(v == "EXCL" for v in cl), sum(v == "kept+FLAG" for v in cl)
g_ex, g_flag = sum(v == "EXCL" for v in ge), sum(v == "kept+FLAG" for v in ge)
print(f"clarifications: excluded {n_ex}/{len(cl)}, flagged only {n_flag}, neither {len(cl) - n_ex - n_flag}")
print(f"genuine: wrongly excluded {g_ex}/{len(ge)}, flagged {g_flag}")
ok = n_ex >= MIN_CLARIF_EXCLUDED and g_ex <= MAX_GENUINE_EXCLUDED
print("PASS clarifications" if ok else f"FAIL clarifications (need excluded >= {MIN_CLARIF_EXCLUDED} and wrongly excluded <= {MAX_GENUINE_EXCLUDED})")
sys.exit(0 if ok else 1)
