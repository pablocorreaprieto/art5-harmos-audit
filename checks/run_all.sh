#!/bin/bash
# Runs every check of ART 5 on the code in ART5_CODE (default: the repository root) and writes each
# output to checks/outputs/ (or CHECKS_OUT). A check passes only when it exits 0 and prints its exact
# success line. Exits 1 if any check fails. With --with-sim, also reruns the power simulation.
# Written by the main session (claude-opus-5-5), 25.10.2026; results and manuscript checks added 1.11.2026.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
export ART5_CODE=${ART5_CODE:-$(dirname "$HERE")}
export LEXIQUE=${LEXIQUE:-$(python3 "$HERE/_paths.py" lexicon)} || exit 1
OUT=${CHECKS_OUT:-$HERE/outputs}
mkdir -p "$OUT"
# keep the previous run before overwriting it: checks/history/run_<UTC date of that run>, or
# OUT/previous_<date> when CHECKS_OUT is set (added 25.10.2026 after a run was overwritten)
if [ -f "$OUT/tested_versions.txt" ]; then
  stamp=$(sed -n 's/^date (UTC): //p' "$OUT/tested_versions.txt" | tr -d ':-')
  if [ -z "${CHECKS_OUT:-}" ]; then keep="$HERE/history/run_${stamp:-unknown}"; else keep="$OUT/previous_${stamp:-unknown}"; fi
  mkdir -p "$keep" && cp -p "$OUT"/*.txt "$keep"/ && echo "previous run kept in $keep" || { echo "could not keep the previous run"; exit 1; }
fi
fail=0
run() {  # name, exact success line, command...
  local name=$1 ok=$2; shift 2
  "$@" > "$OUT/$name.txt" 2>&1; local code=$?
  if [ $code -eq 0 ] && grep -qxF "$ok" "$OUT/$name.txt"; then echo "PASS $name"; else echo "FAIL $name (exit $code)"; fail=1; fi
}
{
  echo "date (UTC): $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "python: $(python3 --version 2>&1)"
  echo "lexicon: $LEXIQUE $(sha256sum "$LEXIQUE" | cut -c1-16)"
  echo "code under test: $ART5_CODE"
  (cd "$ART5_CODE" && for f in design.json make_prompts.py compute.py analyze.py sim_power.py sim_power_results.json \
     generate.py pipeline.py validate_measure.py PREREG.md README.md requirements.txt \
     manuscript_numbers.py exploratory.py exploratory_p7.py results/numbers.json results/exploratory.json \
     results/exploratory_p7.json results/manuscript_numbers.json manuscript/manuscript.md manuscript/supplement.md; do
     [ -f "$f" ] && printf "%-24s %s\n" "$f" "$(sha256sum "$f" | cut -c1-16)"; done)
} > "$OUT/tested_versions.txt"
run selftest_compute "OK" python3 -B "$ART5_CODE/compute.py" --self-test "$LEXIQUE"
run selftest_analyze "OK" python3 -B "$ART5_CODE/analyze.py" --self-test
run plan "PASS plan" python3 -B "$HERE/plan.py"
run mutate_compute "PASS mutate_compute" python3 -B "$HERE/mutate_compute.py"
run mutate_analyze "PASS mutate_analyze" python3 -B "$HERE/mutate_analyze.py"
run battery "PASS battery" python3 -B "$HERE/battery.py"
run clarifications "PASS clarifications" python3 -B "$HERE/clarifications.py"
run e2e_pilot "PASS e2e_pilot" bash "$HERE/e2e_pilot.sh"
run e2e_crash "PASS e2e_crash" bash "$HERE/e2e_crash.sh"
run e2e_malformed "PASS e2e_malformed" python3 -B "$HERE/e2e_malformed.py"
run e2e_secrets "PASS e2e_secrets" python3 -B "$HERE/e2e_secrets.py"
# the history check fails when its script is missing (v0.4.6; before, a script without the executable bit was skipped silently)
run history "PASS history" bash "$ART5_CODE/history/check_history.sh"
# results and manuscript (added 1.11.2026, after the deposit): always on the repository's own results/,
# whatever ART5_CODE is
REPO=$(dirname "$HERE")
run recompute_primary "PASS recompute_primary" bash -c "cd '$REPO' && python3 -B checks/recompute_primary.py"
run check_numbers "PASS check_numbers" bash -c "cd '$REPO' && python3 -B checks/check_numbers.py"
# added after the internal readings of the draft (P7, 1.11.2026): quantities written in words, and citations
run check_claims "PASS check_claims" bash -c "cd '$REPO' && python3 -B checks/check_claims.py"
run check_claims_planted "FAIL check_claims" bash -c "cd '$REPO' && python3 -B checks/check_claims.py --plant; test \$? -eq 1"
run check_citations "PASS check_citations" bash -c "cd '$REPO' && python3 -B checks/check_citations.py"
if [ "${1:-}" = "--with-sim" ]; then run sim "PASS sim" bash "$HERE/sim.sh"; fi
[ $fail -eq 0 ] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
exit $fail
