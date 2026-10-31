#!/bin/bash
# End-to-end offline test of the ART 5 pipeline v0.4 against the mock providers. Not data.
# Checks the plan budget over passes and runs (D5), the new columns, and the pilot summary.
set -u
EXP=/tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/art5/exp
SRC=${SRC:-/tmp/claude-0/-home-claude/d28672eb-31f4-533e-85fc-00a96d822022/scratchpad/v04_work/art5}
W=$(mktemp -d $EXP/e2e_v04_XXXX)
mkdir -p $W/data/lexicon
cp $SRC/*.py $SRC/design.json $W/
LEX=/usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt
cp $LEX $W/data/lexicon/Lexique383.tsv
cat > $W/models.json <<'EOF'
{"anthropic_balanced": {"provider": "anthropic", "id": "claude-sonnet-test", "usd_per_mtok_in": 3.0, "usd_per_mtok_out": 15.0},
 "openai_balanced": {"provider": "openai", "id": "gpt-test", "usd_per_mtok_in": 2.0, "usd_per_mtok_out": 10.0},
 "mistral_balanced": {"provider": "mistral", "id": "mistral-test", "usd_per_mtok_in": 0.5, "usd_per_mtok_out": 2.0}}
EOF
python3 $EXP/mock_providers.py 18778 & MOCK=$!
sleep 1
export ART5_ENDPOINT_OVERRIDE=http://127.0.0.1:18778 ANTHROPIC_API_KEY=x OPENAI_API_KEY=x MISTRAL_API_KEY=x
cd $W
spent() { python3 -c "
import json, glob
runs = [json.load(open(f)) for f in sorted(glob.glob('logs/run_*.json'))]
print('runs', len(runs), 'caps', [r['cap_usd'] for r in runs], 'spent total', round(sum(r['spent_usd'] for r in runs), 4))"; }
echo "== 1. pilot step with a plan budget of 0.2 USD"
python3 pipeline.py --step pilot --max-cost 0.2 > $W/log1.txt 2>&1; echo "exit $?"
grep -E "plan budget|not run|spent_usd_total" $W/log1.txt | tail -3
spent
echo "== 2. same step again with the same budget: nothing more may be spent"
python3 pipeline.py --step pilot --max-cost 0.2 > $W/log2.txt 2>&1; echo "exit $?"
grep -E "not run|spent_usd_total" $W/log2.txt | tail -3
spent
echo "== 3. same step with a budget of 5 USD: completes"
python3 pipeline.py --step pilot --max-cost 5 > $W/log3.txt 2>&1; echo "exit $?"
grep -E "spent_usd_total|retry_file" $W/log3.txt | tail -3
spent
python3 - <<'EOF'
import json, pandas as pd
df = pd.read_csv("results/pilot_measures.csv")
print("rows", len(df), "kept", int(df["kept"].sum()), "columns present", all(c in df for c in ("n_meta_lines", "flag_meta")))
print("labels", sorted(df["label"].unique()), "exclusions", df.loc[~df["kept"], "exclusion_reason"].value_counts().to_dict())
s = json.load(open("results/pilot_summary.json"))
print("summary keys", sorted(s)[:8], "n_topics_rule", s["n_topics_rule"], "stop_flat_ruler", s["stop_flat_ruler"])
EOF
kill $MOCK
echo "workdir $W"
