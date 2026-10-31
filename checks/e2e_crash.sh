#!/bin/bash
# Offline run of the pilot calls against mock_bad.py, which cuts two 200 responses in the middle of
# the body (fake answers, not data). Checks of the budget fix V1: the run does not stop on a cut
# response; the spend counted from the raw records stays under the plan budget (0.8 USD) after one
# run and after a second run; the raw lines of a run killed before writing its log are counted, and
# only for their own plan. Prints PASS e2e_crash or FAIL.
# Written by the main session (claude-opus-5-5), 25.10.2026; mock_bad.py by the v0.4 confirmation session.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
CODE=${ART5_CODE:-$(dirname "$HERE")}
LEX=${LEXIQUE:-$(python3 "$HERE/_paths.py" lexicon)} || exit 1
W=$(mktemp -d "${TMPDIR:-/tmp}/art5_e2e_crash_XXXX")
mkdir -p "$W/data/lexicon"
cp "$CODE"/*.py "$CODE/design.json" "$W/"
cp "$LEX" "$W/data/lexicon/Lexique383.tsv"
cat > "$W/models.json" <<'JSON'
{"anthropic_balanced": {"provider": "anthropic", "id": "claude-sonnet-test", "usd_per_mtok_in": 3.0, "usd_per_mtok_out": 15.0},
 "openai_balanced": {"provider": "openai", "id": "gpt-test", "usd_per_mtok_in": 2.0, "usd_per_mtok_out": 10.0},
 "mistral_balanced": {"provider": "mistral", "id": "mistral-test", "usd_per_mtok_in": 0.5, "usd_per_mtok_out": 2.0}}
JSON
PORT=$(python3 -c "import socket; s=socket.socket(); s.bind(('127.0.0.1',0)); print(s.getsockname()[1]); s.close()")
python3 -B "$HERE/mock_bad.py" "$PORT" > "$W/mock.log" 2>&1 & MOCK=$!
trap 'kill $MOCK 2>/dev/null' EXIT
sleep 1
export ART5_ENDPOINT_OVERRIDE=http://127.0.0.1:$PORT ANTHROPIC_API_KEY=x OPENAI_API_KEY=x MISTRAL_API_KEY=x
cd "$W"
python3 -B make_prompts.py --pilot > /dev/null || { echo "FAIL e2e_crash: make_prompts"; exit 1; }
fail=0
count() {  # counted spend from the raw records; fails if above 0.8
  python3 - <<'PY'
import glob, json, sys
cost = poss = 0.0; n = 0
for f in glob.glob("data/raw/*.jsonl"):
    for l in open(f, encoding="utf-8"):
        r = json.loads(l); n += 1; cost += r.get("cost_usd", 0.0); poss += r.get("cost_usd_possibly_charged", 0.0)
logs = [json.load(open(f)) for f in glob.glob("logs/run_*.json")]
print(f"records {n}, reported cost {cost:.4f}, possibly charged {poss:.4f}, counted total {cost + poss:.4f}, "
      f"run logs {len(logs)}, logged {sum(r['spent_usd'] for r in logs):.4f}")
sys.exit(0 if cost + poss <= 0.8 + 1e-9 else 1)
PY
}
for i in 1 2; do
  echo "== $i. pilot plan with a budget of 0.8 USD, connections dropped in the middle of two bodies"
  python3 -B -c "
import sys; sys.path.insert(0, '.')
import pipeline; pipeline.run_calls('calls_pilot.jsonl', 0.8, 10.0)" > "log$i.txt" 2>&1; e=$?
  echo "exit $e"; [ $e -eq 0 ] || { grep -E "Traceback|Error" "log$i.txt" | tail -2; fail=1; }
  count || { echo "FAIL: counted spend above the budget"; fail=1; }
done
echo "== 3. the raw lines of a run killed before writing its log are counted, for their own plan only"
python3 - <<'PY' || fail=1
import json, os, sys
sys.path.insert(0, ".")
import pipeline
before = pipeline.spent_on("pilot-")
with open("data/raw/calls_pilot_20991231T000000000000Z.jsonl", "x", encoding="utf-8") as f:
    f.write(json.dumps({"call_id": "pilot-99990", "ok": False, "cost_usd": 0.0, "cost_usd_possibly_charged": 0.0615}) + "\n")
    f.write(json.dumps({"call_id": "main-00001", "ok": True, "cost_usd": 5.0}) + "\n")
after, main = pipeline.spent_on("pilot-"), pipeline.spent_on("main-")
print(f"pilot spend before {before:.4f}, after the planted lines {after:.4f} (+0.0615 expected), main plan {main:.4f} (5.0 expected)")
sys.exit(0 if abs(after - before - 0.0615) < 1e-9 and abs(main - 5.0) < 1e-9 else 1)
PY
[ $fail -eq 0 ] && echo "PASS e2e_crash" || echo "FAIL e2e_crash"
rm -rf "$W"
exit $fail
