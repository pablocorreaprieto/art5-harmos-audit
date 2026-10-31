"""The call files built from design.json by make_prompts.py are the recorded ones, byte for byte:
8,400 calls for the main study and 252 for the pilot (SHA-256 below, unchanged since design v0.3).
Exits 1 otherwise. Written by the main session (claude-opus-5-5), 25.10.2026."""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import code_dir

EXPECTED = {"calls.jsonl": "149a34b0d3ebd578045559d07c4079302ffd600db5fa829c29316ac8089e92b7",
            "calls_pilot.jsonl": "729522e52638b021b12ed48c84cc5e0c999cb7fd3ac1544a0354bca0f028fecb"}
w = tempfile.mkdtemp(prefix="art5_plan_")
for f in ("make_prompts.py", "design.json"):
    shutil.copy(os.path.join(code_dir(), f), w)
ok = True
for args in ([], ["--pilot"]):
    r = subprocess.run([sys.executable, "-B", "make_prompts.py"] + args, cwd=w, capture_output=True, text=True)
    print(r.stdout.splitlines()[0] if r.stdout else r.stderr.strip()[-200:])
    ok &= r.returncode == 0
for f, h in EXPECTED.items():
    got = hashlib.sha256(open(os.path.join(w, f), "rb").read()).hexdigest() if os.path.exists(os.path.join(w, f)) else "missing"
    print(f"{f}: {got[:16]} {'= recorded' if got == h else '!= recorded ' + h[:16]}")
    ok &= got == h
shutil.rmtree(w)
print("PASS plan" if ok else "FAIL plan")
sys.exit(0 if ok else 1)
