#!/bin/bash
# Reruns the power simulation (about 4 minutes) in a temporary copy and compares its output byte for
# byte with the recorded sim_power_results.json. sim_power.py exits 1 itself when a control fails
# (C1 or C2 above 0.0613, or C3 not above it). Prints PASS sim or FAIL sim.
# Written by the main session (claude-opus-5-5), 25.10.2026.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
CODE=${ART5_CODE:-$(dirname "$HERE")}
W=$(mktemp -d "${TMPDIR:-/tmp}/art5_sim_XXXX")
cp "$CODE/sim_power.py" "$CODE/analyze.py" "$W/"
cd "$W"
python3 -B sim_power.py > stdout.txt 2> stderr.txt; e=$?
tail -1 stdout.txt
echo "exit $e"
if [ $e -eq 0 ] && cmp -s sim_power_results.json "$CODE/sim_power_results.json"; then
  echo "output identical to the recorded sim_power_results.json ($(sha256sum sim_power_results.json | cut -c1-16))"
  echo "PASS sim"; r=0
else
  echo "output differs from the recorded file or the run failed"; tail -3 stderr.txt
  echo "FAIL sim"; r=1
fi
rm -rf "$W"
exit $r
