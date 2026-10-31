#!/bin/bash
# Rebuilds every kept design version from the current code files by applying the diffs of history/
# in reverse, newest first, and compares each file with the SHA-256 recorded in history/hashes.txt.
# Prints PASS history or FAIL history. Written by the main session (claude-opus-5-5), 25.10.2026.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
CODE=${ART5_CODE:-$(dirname "$HERE")}
W=$(mktemp -d "${TMPDIR:-/tmp}/art5_history_XXXX")
FILES="PREREG.md README.md analyze.py compute.py design.json generate.py make_prompts.py pipeline.py requirements.txt run.yml sim_power.py sim_power_results.json validate_measure.py .gitignore"
mkdir -p "$W/v"
for f in $FILES; do
  src="$CODE/$f"; [ -f "$src" ] || src="$CODE/.github/workflows/$f"   # run.yml sits under .github/workflows in the repository
  [ -f "$src" ] && cp "$src" "$W/v/$f"
done
fail=0
check() {  # version: compare every file of the folder with hashes.txt, both ways
  python3 - "$1" "$W/v" "$HERE/hashes.txt" <<'PY' || fail=1
import hashlib, os, sys
ver, folder, table = sys.argv[1], sys.argv[2], sys.argv[3]
want = {}
for line in open(table, encoding="utf-8"):
    p = line.split()
    if len(p) == 3 and p[0] == ver:
        want[p[1]] = p[2]
have = {f: hashlib.sha256(open(os.path.join(folder, f), "rb").read()).hexdigest() for f in os.listdir(folder)}
bad = sorted(f for f in set(want) | set(have) if want.get(f) != have.get(f))
print(f"{ver}: {len(want)} files recorded, {'all identical' if not bad else 'differ: ' + ', '.join(bad)}")
sys.exit(1 if bad else 0)
PY
}
ORDER=$(python3 -c "
import glob, os, sys
key = lambda v: tuple(int(x) for x in v.lstrip('v').split('.'))
ds = sorted(glob.glob(os.path.join(sys.argv[1], '*_to_*.diff')), key=lambda d: key(os.path.basename(d).split('_to_')[0]), reverse=True)
print(' '.join(ds))" "$HERE")   # newest first, by numeric version
cur=$(basename "${ORDER%% *}" .diff | sed 's#.*_to_##')
check "$cur"
for d in $ORDER; do
  from=$(basename "$d" .diff | sed 's#_to_.*##')
  (cd "$W/v" && patch -R -p1 -E -s --no-backup-if-mismatch < "$d") || { echo "patch failed: $d"; fail=1; break; }
  check "$from"
done
rm -rf "$W"
[ $fail -eq 0 ] && echo "PASS history" || echo "FAIL history"
exit $fail
