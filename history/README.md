# History of the design before the pilot

These are the earlier design versions of ART 5, from 25.10.2026 (v0.1 to v0.4.4), 31.10.2026 (v0.4.5 to v0.4.7) and 1.11.2026 (v0.4.8 and v0.4.9), kept as differences from one version to the next. Why each version changed is in `../CHANGELOG.md`.

**Rebuilding a version.**

1. Copy the current code files into an empty folder: `PREREG.md`, `README.md`, the `.py` files, `design.json`, `requirements.txt`, `run.yml` (`.github/workflows/run.yml` in the repository), `sim_power_results.json` and `.gitignore`.
2. Apply the diffs in reverse, newest first. For example, `patch -R -p1 -E < v0.4.3_to_v0.4.4.diff` gives v0.4.3, then `v0.4.2_to_v0.4.3.diff` gives v0.4.2, and so on down to v0.2.

**Checking.**

- `hashes.txt` lists the SHA-256 of every file of every kept version.
- `bash history/check_history.sh` rebuilds each version from the current files and compares every file with `hashes.txt`. It prints `PASS history` or `FAIL history`.
- It failed when one hex digit of a recorded hash was changed. During development it also failed on a wrong diff order.

**v0.1.** Only `measures.py`, the prototype of the measure, was kept (`v0.1_measures.py`). The other v0.1 files were overwritten by v0.2. Their hashes are in the Contrôles tab of the project journal and in `CHANGELOG.md`.

**v0.2.** README.md, requirements.txt and .gitignore of v0.2 were not kept, so the rebuilt v0.2 has no such files.
