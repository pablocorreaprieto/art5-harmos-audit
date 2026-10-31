#!/bin/bash
# Offline run of the pilot step against mock_providers.py (fake answers, not data): the plan budget
# holds over runs (0.2 USD twice), then a 5 USD budget completes the pilot, 216 texts are measured,
# the new columns are present and the pilot summary is written. Prints PASS e2e_pilot or FAIL.
# Written by the main session (claude-opus-5-5), 25.10.2026.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
CODE=${ART5_CODE:-$(dirname "$HERE")}
LEX=${LEXIQUE:-$(python3 "$HERE/_paths.py" lexicon)} || exit 1
W=$(mktemp -d "${TMPDIR:-/tmp}/art5_e2e_pilot_XXXX")
mkdir -p "$W/data/lexicon"
cp "$CODE"/*.py "$CODE/design.json" "$W/"
cp "$LEX" "$W/data/lexicon/Lexique383.tsv"
cat > "$W/models.json" <<'JSON'
{"anthropic_balanced": {"provider": "anthropic", "id": "claude-sonnet-test", "usd_per_mtok_in": 3.0, "usd_per_mtok_out": 15.0},
 "openai_balanced": {"provider": "openai", "id": "gpt-test", "usd_per_mtok_in": 2.0, "usd_per_mtok_out": 10.0},
 "mistral_balanced": {"provider": "mistral", "id": "mistral-test", "usd_per_mtok_in": 0.5, "usd_per_mtok_out": 2.0}}
JSON
PORT=$(python3 -c "import socket; s=socket.socket(); s.bind(('127.0.0.1',0)); print(s.getsockname()[1]); s.close()")
python3 -B "$HERE/mock_providers.py" "$PORT" > "$W/mock.log" 2>&1 & MOCK=$!
trap 'kill $MOCK 2>/dev/null' EXIT
sleep 1
export ART5_ENDPOINT_OVERRIDE=http://127.0.0.1:$PORT ANTHROPIC_API_KEY=x OPENAI_API_KEY=x MISTRAL_API_KEY=x
cd "$W"
fail=0
spent() {  # counted spend of the pilot plan, from the raw records; fails if above the cap given
  python3 - "$1" <<'PY'
import glob, json, sys
cap = float(sys.argv[1]); total = 0.0
for f in glob.glob("data/raw/*.jsonl"):
    for l in open(f, encoding="utf-8"):
        r = json.loads(l)
        if r["call_id"].startswith("pilot-"):
            total += r.get("cost_usd", 0.0) + r.get("cost_usd_possibly_charged", 0.0)
runs = len(glob.glob("logs/run_*.json"))
print(f"runs {runs}, counted spend {total:.4f} USD, cap {cap}")
sys.exit(0 if total <= cap + 1e-9 else 1)
PY
}
step() {  # budget
  python3 -B pipeline.py --step pilot --max-cost "$1" > "log_$1_$RANDOM.txt" 2>&1; e=$?
  echo "exit $e"; [ $e -eq 0 ] || fail=1
  spent "$1" || { echo "FAIL: spend above the plan budget"; fail=1; }
}
echo "== 1. pilot step with a plan budget of 0.2 USD"; step 0.2
echo "== 2. same step again with the same budget: the total stays under 0.2"; step 0.2
echo "== 3. same step with a budget of 5 USD: completes"; step 5
python3 - <<'PY' || fail=1
import json, sys
import pandas as pd
df = pd.read_csv("results/pilot_measures.csv")
cols = all(c in df for c in ("n_meta_lines", "flag_meta"))
print("rows", len(df), "kept", int(df["kept"].sum()), "columns present", cols)
print("labels", sorted(df["label"].unique()), "exclusions", df.loc[~df["kept"], "exclusion_reason"].value_counts().to_dict())
s = json.load(open("results/pilot_summary.json"))
print("summary keys", sorted(s), "n_topics_rule", s.get("n_topics_rule"), "stop_flat_ruler", s.get("stop_flat_ruler"))
sys.exit(0 if len(df) == 216 and int(df["kept"].sum()) == 216 and cols and "n_topics_rule" in s else 1)
PY
[ $fail -eq 0 ] && echo "PASS e2e_pilot" || echo "FAIL e2e_pilot"
rm -rf "$W"
exit $fail
