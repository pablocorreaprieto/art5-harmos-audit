# -*- coding: utf-8 -*-
"""Malformed answers with HTTP status 200 (fake answers from mock_weird.py, not data): for each of two
routes (Anthropic, OpenAI-style) and each shape (none, list, empty_choices, usage_null, usage_missing,
usage_empty, tokens_null, content_number, surrogate, model_surrogate, finish_surrogate, non_utf8,
empty_body, content_parts_bad), generate.py runs 12 pilot calls while the 2nd request of the route
gets the malformed body. Passes when every run exits 0, writes its run log and records all 12 calls,
when an answer without usable token counts is counted at the worst case of its model, and when
compute.py then measures the raw file of a surrogate shape without stopping. Exits 1 otherwise.
Written by the v0.4.1 confirmation session (claude-sonnet-5-5, n1_weird.py), adapted by the main
session (claude-opus-5-5): paths, temporary folders, gate."""
import glob
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _paths import code_dir, lexicon

CODE = code_dir()
MODELS = {"anthropic_balanced": {"provider": "anthropic", "id": "claude-sonnet-test", "usd_per_mtok_in": 3.0, "usd_per_mtok_out": 15.0},
          "openai_balanced": {"provider": "openai", "id": "gpt-test", "usd_per_mtok_in": 2.0, "usd_per_mtok_out": 10.0}}
SHAPES = ["none", "list", "empty_choices", "usage_null", "usage_missing", "usage_empty", "tokens_null", "content_number",
          "surrogate", "model_surrogate", "finish_surrogate", "non_utf8", "empty_body", "content_parts_bad"]
NO_USAGE = {"usage_null", "usage_missing", "usage_empty", "tokens_null"}   # must be counted at the worst case
SURROGATE = {"surrogate", "model_surrogate", "finish_surrogate"}           # compute.py must then run
LEX = lexicon()
calls_file = os.path.join(CODE, "calls_pilot.jsonl")
tmp_root = tempfile.mkdtemp(prefix="art5_malformed_")
if not os.path.exists(calls_file):  # a fresh checkout has no call files: build the pilot calls
    shutil.copy(os.path.join(CODE, "design.json"), tmp_root)
    subprocess.run([sys.executable, "-B", os.path.join(CODE, "make_prompts.py"), "--pilot"], cwd=tmp_root,
                   check=True, capture_output=True)
    calls_file = os.path.join(tmp_root, "calls_pilot.jsonl")
all_calls = [json.loads(l) for l in open(calls_file, encoding="utf-8")]
bad = 0
for model in MODELS:
    for shape in SHAPES:
        w = os.path.join(tmp_root, f"{model}_{shape}")
        os.makedirs(w)
        shutil.copy(os.path.join(CODE, "generate.py"), w)
        json.dump(MODELS, open(os.path.join(w, "models.json"), "w"))
        calls = [c for c in all_calls if c["model"] == model and c["kind"] == "text"][:12]
        with open(os.path.join(w, "calls.jsonl"), "w", encoding="utf-8") as f:
            for c in calls:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
        mock = subprocess.Popen([sys.executable, "-B", os.path.join(HERE, "mock_weird.py"), str(port)],
                                env=dict(os.environ, WEIRD=shape, WEIRD_K="2"), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.7)
        env = dict(os.environ, ART5_ENDPOINT_OVERRIDE=f"http://127.0.0.1:{port}", ANTHROPIC_API_KEY="x", OPENAI_API_KEY="x",
                   MISTRAL_API_KEY="x", PYTHONDONTWRITEBYTECODE="1", PYTHONPATH=os.path.join(HERE, "fast"))
        r = subprocess.run([sys.executable, "-B", "generate.py", "run", "calls.jsonl", "models.json", "5.0", "--workers", "2"],
                           cwd=w, env=env, capture_output=True, text=True, timeout=300)
        mock.terminate(); mock.wait()
        recs = []
        for f in glob.glob(os.path.join(w, "data", "raw", "*.jsonl")):
            recs += [json.loads(l) for l in open(f, encoding="utf-8")]
        logs = len(glob.glob(os.path.join(w, "logs", "run_*.json")))
        failed = [x for x in recs if not x["ok"]]
        poss = sum(x.get("cost_usd_possibly_charged", 0.0) for x in recs)
        good = r.returncode == 0 and logs == 1 and len(recs) == 12
        extra = ""
        if shape in NO_USAGE and good:
            counted = poss > 0
            good &= counted
            extra += " | unknown usage counted at the worst case" if counted else " | unknown usage NOT counted"
        if shape in SURROGATE and good:
            shutil.copy(os.path.join(CODE, "compute.py"), w)
            c = subprocess.run([sys.executable, "-B", "compute.py", LEX, "data/raw/*.jsonl", "measures.csv"],
                               cwd=w, capture_output=True, text=True, timeout=300)
            good &= c.returncode == 0
            extra += " | compute.py exit %d" % c.returncode + ("" if c.returncode == 0 else ": " + (c.stderr.strip().splitlines() or ["?"])[-1][:90])
        bad += not good
        tail = "" if r.returncode == 0 else " | " + (r.stderr.strip().splitlines() or ["?"])[-1][:110]
        print(f"{'ok  ' if good else 'FAIL'} {model[:9]:9s} {shape:18s} exit {r.returncode} | raw records {len(recs):2d}/12, "
              f"failed {len(failed)}, possibly charged {poss:.3f}, run log {logs}{tail}{extra}")
shutil.rmtree(tmp_root)
print("PASS e2e_malformed" if bad == 0 else f"FAIL e2e_malformed ({bad} of {2 * len(SHAPES)} runs)")
sys.exit(0 if bad == 0 else 1)
