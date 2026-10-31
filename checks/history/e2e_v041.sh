#!/bin/bash
# Offline test of v0.4.1 budget accounting (N1): connections dropped mid-body, and a run killed
# before it writes its log. Uses the mock that cuts two 200 responses. Not data.
set -u
EXP=/tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/exp
SRC=${SRC:-/tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v041_work/art5}
W=$(mktemp -d $EXP/e2e_v041_XXXX)
mkdir -p $W/data/lexicon
cp $SRC/*.py $SRC/design.json $W/
cp /usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt $W/data/lexicon/Lexique383.tsv
cat > $W/models.json <<'EOF'
{"anthropic_balanced": {"provider": "anthropic", "id": "claude-sonnet-test", "usd_per_mtok_in": 3.0, "usd_per_mtok_out": 15.0},
 "openai_balanced": {"provider": "openai", "id": "gpt-test", "usd_per_mtok_in": 2.0, "usd_per_mtok_out": 10.0},
 "mistral_balanced": {"provider": "mistral", "id": "mistral-test", "usd_per_mtok_in": 0.5, "usd_per_mtok_out": 2.0}}
EOF
PORT=$(python3 -c "import socket; s=socket.socket(); s.bind(('127.0.0.1',0)); print(s.getsockname()[1]); s.close()")
python3 $EXP/mock_bad.py $PORT > $W/mock.log 2>&1 & MOCK=$!
sleep 1
export ART5_ENDPOINT_OVERRIDE=http://127.0.0.1:$PORT ANTHROPIC_API_KEY=x OPENAI_API_KEY=x MISTRAL_API_KEY=x
cd $W
python3 make_prompts.py --pilot > /dev/null
count() { python3 -c "
import json, glob
cost = poss = 0.0; n = 0
for f in glob.glob('data/raw/*.jsonl'):
    for l in open(f, encoding='utf-8'):
        r = json.loads(l); n += 1; cost += r.get('cost_usd', 0.0); poss += r.get('cost_usd_possibly_charged', 0.0)
logs = [json.load(open(f)) for f in glob.glob('logs/run_*.json')]
print(f'records {n}, reported cost {cost:.4f}, possibly charged {poss:.4f}, counted total {cost + poss:.4f}, run logs {len(logs)}, logged {sum(r[\"spent_usd\"] for r in logs):.4f}')"; }
echo "== 1. pilot plan with budget 0.8 USD, two connections dropped mid-body"
python3 -c "
import sys; sys.path.insert(0, '.')
import pipeline; pipeline.run_calls('calls_pilot.jsonl', 0.8, 10.0)" > log1.txt 2>&1; echo "exit $?"
grep -E "Traceback|Error|spent_usd_total|possibly_charged_usd" log1.txt | head -8
count
echo "== 2. same plan again, budget 0.8: the total must stay under 0.8"
python3 -c "
import sys; sys.path.insert(0, '.')
import pipeline; pipeline.run_calls('calls_pilot.jsonl', 0.8, 10.0)" > log2.txt 2>&1; echo "exit $?"
grep -E "Traceback|spent_usd_total|not run" log2.txt | head -4
count
echo "== 3. a run killed before writing its log is still counted"
python3 - <<'EOF'
import json, os, sys
sys.path.insert(0, ".")
import pipeline
os.makedirs("data/raw", exist_ok=True)
with open("data/raw/calls_pilot_20991231T000000000000Z.jsonl", "x", encoding="utf-8") as f:   # a crashed run: raw lines, no log
    f.write(json.dumps({"call_id": "pilot-99990", "ok": False, "cost_usd": 0.0, "cost_usd_possibly_charged": 0.0615}) + "\n")
    f.write(json.dumps({"call_id": "main-00001", "ok": True, "cost_usd": 5.0}) + "\n")   # another plan, not counted
before = pipeline.spent_on("pilot-")
print("pilot spent counted from raw records:", round(before, 4), "| main plan:", round(pipeline.spent_on("main-"), 4))
EOF
kill $MOCK
echo "workdir $W"
