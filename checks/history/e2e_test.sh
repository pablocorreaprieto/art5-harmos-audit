#!/bin/bash
# End-to-end offline test of the ART 5 pipeline against the mock providers. Not data.
set -u
EXP=/tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/exp
W=$EXP/e2e/work
rm -rf $W && mkdir -p $W/data/lexicon
cp ${SRC:-/home/claude/art5}/*.py ${SRC:-/home/claude/art5}/design.json $W/
cp /usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt $W/data/lexicon/Lexique383.tsv
cat > $W/models.json <<'EOF'
{"anthropic_balanced": {"provider": "anthropic", "id": "claude-sonnet-test", "usd_per_mtok_in": 3.0, "usd_per_mtok_out": 15.0},
 "openai_balanced": {"provider": "openai", "id": "gpt-test", "usd_per_mtok_in": 2.0, "usd_per_mtok_out": 10.0},
 "mistral_balanced": {"provider": "mistral", "id": "mistral-test", "usd_per_mtok_in": 0.5, "usd_per_mtok_out": 2.0}}
EOF
python3 $EXP/mock_providers.py 18777 & MOCK=$!
sleep 1
export ART5_ENDPOINT_OVERRIDE=http://127.0.0.1:18777 ANTHROPIC_API_KEY=x OPENAI_API_KEY=x MISTRAL_API_KEY=x
cd $W
python3 make_prompts.py --pilot > /dev/null
echo "== 1. budget cap stops the run"
python3 generate.py run calls_pilot.jsonl models.json 0.2 | python3 -c "import json,sys; d=json.load(sys.stdin); print({k:d[k] for k in ('launched','ok','failed','spent_usd','stopped')})"
echo "== 2. time limit stops the run"
python3 generate.py run calls_pilot.jsonl models.json 5 --max-minutes 0 | python3 -c "import json,sys; d=json.load(sys.stdin); print({k:d[k] for k in ('to_do','launched','stopped')})"
ls data/raw | wc -l
echo "== 3. full pilot step through the pipeline (resumes, retries, measures, blinding, summary)"
python3 pipeline.py --step pilot --max-cost 5 > $EXP/e2e/pilot_log.txt 2>&1; echo "pipeline exit $?"
grep -E '"raw_file"|"to_do"|"launched"|"stopped"|retry_file|"n":|rows' $EXP/e2e/pilot_log.txt | head -20
kill $MOCK
