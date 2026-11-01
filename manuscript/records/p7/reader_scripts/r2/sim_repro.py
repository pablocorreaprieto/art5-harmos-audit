"""Re-run sim_power.controls() and sim_power.grid() from the copy and compare with the stored sim_power_results.json."""
import sys, json
import numpy as np
sys.path.insert(0, sys.argv[1])
import sim_power as S

stored = json.load(open(sys.argv[1] + "/sim_power_results.json"))
c = S.controls()
print("controls:", json.dumps(c, default=float))
print("stored controls == recomputed:", json.loads(json.dumps(c, default=float)) == stored["controls"])
g = S.grid()
gj = json.loads(json.dumps(g, default=float))
print("grid rows", len(gj), "stored rows", len(stored["grid"]), "identical:", gj == stored["grid"])
json.dump({"controls": c, "grid": g}, open(sys.argv[2], "w"), indent=1, default=float)
