import sys, json
sys.path.insert(0, "/home/claude/art5-harmos-audit")
import numpy as np
import sim_power as S
p = json.load(open("/home/claude/art5-harmos-audit/results/pilot_summary.json"))["ruler"]
sig, slope = p["sigma_upper80"], -0.04  # PLANNING_SLOPE of pipeline.py
r = S.rates(S.SCENARIOS["offset_1y"], sig, slope, 16, 1000, seed=777 + 16)
print("registered seed, R=1000:", r["h2_level_H"], "MC SE", round(np.sqrt(r["h2_level_H"] * (1 - r["h2_level_H"]) / 1000), 4))
r2 = S.rates(S.SCENARIOS["offset_1y"], sig, slope, 16, 2000, seed=11)
print("seed 11, R=2000:", r2["h2_level_H"])
