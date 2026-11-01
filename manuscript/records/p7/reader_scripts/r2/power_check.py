"""Checks on the power simulation: (1) the topic-level SD of the primary statistics implied by the simulation assumptions
against the SD observed in the confirmatory data; (2) power at T=16 for different seeds / R and for the observed variance;
(3) power for the observed SE. Runs from a COPY of the repository (argument 1); writes nothing into the original."""
import sys, os, json
import numpy as np
sys.path.insert(0, sys.argv[1])
import analyze as A
import sim_power as S

SIG = 0.12228291408794054
rng = np.random.default_rng(2024)
lev, grd = [], []
for _ in range(1000):
    cubes = S.draw({}, rng, SIG, -0.04, 16)
    x_l, _ = A.topic_stat(cubes["L1"], cubes["L5"], "level")
    x_g, _ = A.topic_stat(cubes["L1"], cubes["L5"], "gradient")
    lev.append(np.std(x_l, ddof=1)); grd.append(np.std(x_g, ddof=1))
print("simulated null: SD across 16 topics of H2-H level  mean %.4f  (observed 0.0126);  of H3-H gradient mean %.5f (observed 0.00927)" % (np.mean(lev), np.mean(grd)))
for nm, kw in [("assumed", {}), ("tau_lt=0,tau_ps=0", dict(tau_lt=0.0, tau_ps=0.0)), ("tau_ps=0", dict(tau_ps=0.0)), ("tau_lt=0", dict(tau_lt=0.0))]:
    lev = []
    r = np.random.default_rng(5)
    for _ in range(300):
        cubes = S.draw({}, r, SIG, -0.04, 16, **kw)
        x_l, _ = A.topic_stat(cubes["L1"], cubes["L5"], "level")
        lev.append(np.std(x_l, ddof=1))
    print(f"  SD of level across topics, {nm}: {np.mean(lev):.4f}")

# power at T=16 with other seeds and R=4000 (the preregistered estimate: .835 with R=1000, seed 793)
for seed in (11, 12, 13):
    r = S.rates(S.SCENARIOS["offset_1y"], SIG, -0.04, 16, 4000, seed=seed)
    print("power H2-H, T=16, sigma_upper80, slope -0.04, R=4000, seed", seed, "->", r["h2_level_H"], "(familywise any rejection", r["familywise"], ")")
# power at the pilot point estimates (sigma 0.117, slope -0.0449) and at the confirmatory residual SD 0.104
for sg, sl in ((0.1169, -0.0449), (0.104, -0.0394)):
    r = S.rates(S.SCENARIOS["offset_1y"], sg, sl, 16, 2000, seed=21)
    print("power H2-H, T=16, sigma", sg, "slope", sl, "->", r["h2_level_H"])
# Monte Carlo SE of the preregistered estimate
p = .835; print("MC SE of .835 at R=1000: %.4f, 95%% MC interval [%.3f, %.3f]" % (np.sqrt(p * (1 - p) / 1000), p - 1.96 * np.sqrt(p * (1 - p) / 1000), p + 1.96 * np.sqrt(p * (1 - p) / 1000)))
