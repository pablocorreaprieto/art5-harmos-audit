"""Mutation testing of analyze.py: each mutation is applied to a copy, the self-test must fail."""
import os, shutil, subprocess, sys, json, tempfile
SRC = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/art5/analyze.py"
MUT = [
 ("sign of the paired difference", 'd = (a - b)[:, grades]', 'd = (b - a)[:, grades]'),
 ("one-sided p reported as two-sided", '"t": float(t), "df": T - 1, "p_two_sided": float(2 * stats.t.sf(abs(t), T - 1))', '"t": float(t), "df": T - 1, "p_two_sided": float(stats.t.sf(t, T - 1))'),
 ("Holm replaced by no correction", 'if not stop and pvals[k] <= alpha / (m - i):', 'if not stop and pvals[k] <= alpha:'),
 ("Holm adjusted p not monotone", 'running = max(running, min(1.0, (m - i) * pvals[k]))', 'running = min(1.0, (m - i) * pvals[k])'),
 ("SD with ddof 0", 'np.std(x, ddof=1)', 'np.std(x, ddof=0)'),
 ("gradient weights not scaled", 'return c / np.sum(c ** 2)', 'return c'),
 ("H1 tested in the wrong direction", 'p = float(stats.t.cdf(t, T - 1))', 'p = float(stats.t.sf(t, T - 1))'),
 ("eligibility threshold sign", 'MIN_SLOPE = -0.02', 'MIN_SLOPE = 0.02'),
 ("shift sign in the pooled reading", 'return float(v[:, 0].sum() / v[:, 2].sum()), float(1 + v[:, 1].sum() / v[:, 2].sum())', 'return float(-v[:, 0].sum() / v[:, 2].sum()), float(1 + v[:, 1].sum() / v[:, 2].sum())'),
 ("excluded texts used", 'd = df[(df["kept"]) & (df["label"].isin(GRADED_LABELS)) & df[y].notna()]', 'd = df[(df["label"].isin(GRADED_LABELS)) & df[y].notna()]'),
 ("completeness rule removed", 'keep = (n >= 0.5 * full) & np.isfinite(s)', 'keep = np.isfinite(s)'),
 ("mean over the wrong axes", 'dg = np.nanmean(d, axis=(0, 2))', 'dg = np.nanmean(d, axis=(0, 1))'),
 ("probe regex without et", '(?:à|-|–|—|ou|et)', '(?:à|-|–|—|ou)'),
 ("probe tolerance widened", 'truth_from - 0.5 <= (lo + hi) / 2 <= truth_to + 0.5', 'truth_from - 1.5 <= (lo + hi) / 2 <= truth_to + 1.5'),
 ("L0 placement sign", 'l0_age[m] = 9.0 + (l0[m] - float(np.mean(ruler))) / b', 'l0_age[m] = 9.0 - (l0[m] - float(np.mean(ruler))) / b'),
 ("gloss compared with the wrong label", '("gloss_level_vs_bare", "L3", "L1", "level")', '("gloss_level_vs_bare", "L3", "L5", "level")'),
 ("OLS gradient term not multiplied by age", 'd[grd] = d[lev] * d["age_c"]', 'd[grd] = d[lev]'),
 ("P test reads the H label", '("h2_level_P", "L1P", "L5", "level")', '("h2_level_P", "L1", "L5", "level")'),
 ("genres collapsed in the cube", 'ei = d["genre"].map({e: i for i, e in enumerate(ax["genres"])}).to_numpy()', 'ei = np.zeros(len(d), dtype=int)'),
 ("L6 read over all grades", 'grades = [GRADES.index(g) for g in ("3H", "4H", "5H")] if lab == "L6" else None', 'grades = None'),
 ("tracking without the 1", 'float(1 + v[:, 1].sum() / v[:, 2].sum())', 'float(v[:, 1].sum() / v[:, 2].sum())'),
 ("level weights not equal", 'return np.full(len(grades), 1 / len(grades))', 'return np.linspace(0.5, 1.5, len(grades)) / len(grades)'),
]
src = open(SRC, encoding="utf-8").read()
results = []
for name, old, new in MUT:
    n = src.count(old)
    if n != 1:
        results.append((name, f"pattern found {n} times, not run")); continue
    d = tempfile.mkdtemp()
    open(os.path.join(d, "analyze.py"), "w", encoding="utf-8").write(src.replace(old, new))
    p = subprocess.run([sys.executable, "analyze.py", "--self-test"], cwd=d, capture_output=True, text=True, timeout=600)
    caught = p.returncode != 0
    first_fail = next((l for l in (p.stdout + p.stderr).splitlines() if l.startswith("FAIL") or "Error" in l), "")
    results.append((name, ("caught: " + first_fail[:110]) if caught else "NOT caught"))
    shutil.rmtree(d)
for name, r in results:
    print(f"{name:42s} {r}")
print(sum(r.startswith("caught") for _, r in results), "of", len(results), "caught")
