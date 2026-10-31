# -*- coding: utf-8 -*-
"""No key value is ever written or printed by generate.py (check added in v0.4.6, after run 41222817007
committed the value of a secret that held several keys on separate lines, quoted by an error message).

1. list-models with ANTHROPIC_API_KEY holding three fake keys on separate lines and no other key:
   exit 0, the Anthropic entry names the secret and its line breaks, and no part of the value is in
   the model list or in the printed output.
2. A pilot run with that secret, against the local mock: no call is made, the run stops with a message
   that names the secret, and no part of the value is in any file or in the printed output.
3. A run against a local mock that answers 401 and quotes the key it received, with a valid one-line
   fake key: the run ends, records its calls, and no raw line holds the key.

Passes when all three hold. Exits 1 otherwise. Failure control: generate.py v0.4.5, which writes the
value in 1 and 2 and the quoted key in 3. Fake keys and local servers only: nothing reaches a provider.
Written by the main session (claude-opus-5-5), 31.10.2026."""
import glob
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _paths import code_dir

CODE = code_dir()
PARTS = ["fakeKeyAAA_7f3c91d2e8b4", "fakeKeyBBB_2a6d0c5f9e17", "fakeKeyCCC_9b8e4a1d3c60"]
MULTI = "\n\n".join(PARTS)
ONE = "fakeKeyDDD_5c2e7b9a0f43"
MODELS = {"anthropic_balanced": {"provider": "anthropic", "id": "claude-test", "usd_per_mtok_in": 3.0, "usd_per_mtok_out": 15.0}}
root = tempfile.mkdtemp(prefix="art5_secrets_")


def pilot_calls(n):
    calls_file = os.path.join(CODE, "calls_pilot.jsonl")
    if not os.path.exists(calls_file):  # a fresh checkout has no call files: build the pilot calls
        shutil.copy(os.path.join(CODE, "design.json"), root)
        subprocess.run([sys.executable, "-B", os.path.join(CODE, "make_prompts.py"), "--pilot"], cwd=root,
                       check=True, capture_output=True)
        calls_file = os.path.join(root, "calls_pilot.jsonl")
    calls = [json.loads(l) for l in open(calls_file, encoding="utf-8")]
    return [c for c in calls if c["model"] == "anthropic_balanced" and c["kind"] == "text"][:n]


def workdir(name, with_calls):
    w = os.path.join(root, name)
    os.makedirs(w)
    shutil.copy(os.path.join(CODE, "generate.py"), w)
    if with_calls:
        json.dump(MODELS, open(os.path.join(w, "models.json"), "w"))
        with open(os.path.join(w, "calls.jsonl"), "w", encoding="utf-8") as f:
            for c in pilot_calls(6):
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
    return w


def written(w):
    """Every file the run wrote (logs, raw records), as text."""
    out = []
    for p in glob.glob(os.path.join(w, "logs", "*")) + glob.glob(os.path.join(w, "data", "raw", "*")):
        out.append(open(p, encoding="utf-8", errors="replace").read())
    return "\n".join(out)


def leaks(text, parts):
    return [p[:11] + "..." for p in parts if p in text]


def free_port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
    return port


def env_with(**keys):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONPATH=os.path.join(HERE, "fast"))
    env.pop("ART5_ENDPOINT_OVERRIDE", None)
    env.update(keys)
    return env


fails = 0

# 1. list-models: only the Anthropic secret is set, and it holds three keys
w = workdir("list_models", False)
r = subprocess.run([sys.executable, "-B", "generate.py", "list-models"], cwd=w, capture_output=True, text=True,
                   timeout=120, env=env_with(ANTHROPIC_API_KEY=MULTI, OPENAI_API_KEY="", MISTRAL_API_KEY=""))
files = written(w)
found = leaks(files + r.stdout + r.stderr, PARTS)
try:
    entry = json.load(open(glob.glob(os.path.join(w, "logs", "models_*.json"))[0]))["anthropic"]
    named = "ANTHROPIC_API_KEY" in json.dumps(entry) and "line breaks" in json.dumps(entry)
except Exception as e:
    entry, named = repr(e)[:200], False
ok = r.returncode == 0 and not found and named
fails += not ok
print(f"1. list-models, secret with three keys: exit {r.returncode}, parts found in outputs {found or 'none'}, "
      f"problem named {named} -> {'ok' if ok else 'FAIL'}")

# 2. a pilot run with the same secret, against the offline mock of the providers
port = free_port()
mock = subprocess.Popen([sys.executable, "-B", os.path.join(HERE, "mock_providers.py"), str(port)],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(0.7)
w = workdir("run_multi", True)
r = subprocess.run([sys.executable, "-B", "generate.py", "run", "calls.jsonl", "models.json", "1.0", "--workers", "2"],
                   cwd=w, capture_output=True, text=True, timeout=300,
                   env=env_with(ANTHROPIC_API_KEY=MULTI, OPENAI_API_KEY="x", MISTRAL_API_KEY="x",
                                ART5_ENDPOINT_OVERRIDE=f"http://127.0.0.1:{port}"))
mock.terminate(); mock.wait()
files = written(w)
found = leaks(files + r.stdout + r.stderr, PARTS)
raw_lines = sum(1 for p in glob.glob(os.path.join(w, "data", "raw", "*.jsonl")) for _ in open(p, encoding="utf-8"))
named = "ANTHROPIC_API_KEY" in (r.stdout + r.stderr)
ok = r.returncode != 0 and raw_lines == 0 and not found and named
fails += not ok
print(f"2. pilot run, secret with three keys: exit {r.returncode}, raw lines {raw_lines}, parts found in outputs "
      f"{found or 'none'}, secret named in the message {named} -> {'ok' if ok else 'FAIL'}")


# 3. a provider that answers 401 and quotes the key it received
class Echo(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        self.rfile.read(int(self.headers.get("Content-Length", 0)))
        got = self.headers.get("x-api-key") or self.headers.get("Authorization", "")
        msg = json.dumps({"type": "error", "error": {"type": "authentication_error",
                                                     "message": f"invalid x-api-key: {got}"}}).encode()
        self.send_response(401); self.send_header("Content-Length", str(len(msg))); self.end_headers()
        self.wfile.write(msg)


server = ThreadingHTTPServer(("127.0.0.1", 0), Echo)
threading.Thread(target=server.serve_forever, daemon=True).start()
w = workdir("run_echo", True)
r = subprocess.run([sys.executable, "-B", "generate.py", "run", "calls.jsonl", "models.json", "1.0", "--workers", "2"],
                   cwd=w, capture_output=True, text=True, timeout=300,
                   env=env_with(ANTHROPIC_API_KEY=ONE, OPENAI_API_KEY="x", MISTRAL_API_KEY="x",
                                ART5_ENDPOINT_OVERRIDE=f"http://127.0.0.1:{server.server_address[1]}"))
server.shutdown()
files = written(w)
found = leaks(files + r.stdout + r.stderr, [ONE])
raw_lines = sum(1 for p in glob.glob(os.path.join(w, "data", "raw", "*.jsonl")) for _ in open(p, encoding="utf-8"))
ok = r.returncode == 0 and raw_lines == 6 and not found
fails += not ok
print(f"3. run against a provider that quotes the key in a 401: exit {r.returncode}, raw lines {raw_lines}, "
      f"key found in outputs {found or 'none'} -> {'ok' if ok else 'FAIL'}")

shutil.rmtree(root, ignore_errors=True)
print("PASS e2e_secrets" if fails == 0 else "FAIL e2e_secrets")
sys.exit(1 if fails else 0)
