import copy, os, sys, importlib.util
W = sys.argv[1]
sys.path.insert(0, os.path.join(W, "manuscript"))
sys.path.insert(0, os.path.join(W, "checks"))
import render
spec = importlib.util.spec_from_file_location("check_claims", os.path.join(W, "checks", "check_claims.py"))
cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
nums, _ = render.load(W)
md = open(os.path.join(W, "manuscript/build/manuscript.md"), encoding="utf-8").read()
base = cc.problems(md, nums)
print("baseline problems:", base)
def plant(name, edits):
    n = copy.deepcopy(nums)
    for k, v in edits.items():
        n[k]["value"] = v
    p = cc.problems(md, n)
    print(f"{name:55s} -> {'FAIL (detected)' if p else 'PASS (NOT detected)'}", [x[:80] for x in p][:2])
plant("L3 sd shift raised to 0.40 (tie 'as low as P')", {"ph_disp_L3_shift": 0.40})
plant("L1P sd shift raised to 0.60", {"ph_disp_L1P_shift": 0.60})
plant("ph_het_n_sig 3 -> 4", {"ph_het_n_sig": 4})
plant("ph_het_L1P_level_p -> 0.01", {"ph_het_L1P_level_p": 0.01})
plant("Haiku L2-L1 level -> -0.03 (not near zero)", {"ph_L2mL1_level_anthropic_light": -0.03})
plant("others_max -> -0.005 (a 'four model' not harder)", {"ph_L2mL1_level_others_max": -0.005})
plant("Sol L2-L1 level -> 0.02", {"ph_L2mL1_level_openai_balanced": 0.02})
plant("Haiku track raised above Luna (two least)", {"ae_L1_anthropic_light_track": 1.5})
plant("L2-L1 pooled shift -> 0.9 ('half a year')", {"ph_L2mL1_shift": 0.9})
plant("Small L3 shift -> -1.2 ('within a year')", {"ae_L3_mistral_light_shift": -1.2})
