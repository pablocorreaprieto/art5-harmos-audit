"""Recompute, without importing the repository's code, the numbers behind the corrected region sentence.

Run from the worktree root:  python3 -I -B /tmp/confirm3_p7/recompute_confirm3.py
Reads results/measures.csv and results/manuscript_numbers.json only.
"""
import json
import numpy as np
import pandas as pd

m = pd.read_csv("results/measures.csv", keep_default_na=False)
m = m[m["kept"].astype(str).str.lower().isin(["true", "1"])].copy()
m["y"] = pd.to_numeric(m["mean_zipf_content"])
AGE = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
MODELS = ["anthropic_balanced", "anthropic_light", "openai_balanced", "openai_light", "mistral_balanced",
          "mistral_light"]
nums = json.load(open("results/manuscript_numbers.json"))
v = lambda k: float(nums[k]["value"])

keys = ["model", "grade", "genre", "topic"]
cell = {lab: m[m["label"] == lab].set_index(keys)["y"] for lab in ("L1", "L2", "L5")}

# slope of each model's age-only ruler: least squares through its six L5 grade means
slope = {}
for mod in MODELS:
    g = m[(m["model"] == mod) & (m["label"] == "L5")].groupby("grade")["y"].mean()
    x = np.array([AGE[k] for k in g.index]); y = g.to_numpy()
    slope[mod] = float(np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2))

# level difference L2 - L1 by model: mean over matched pairs
lev = {}
for mod in MODELS:
    a = cell["L2"].xs(mod, level="model"); b = cell["L1"].xs(mod, level="model")
    lev[mod] = float((a - b).dropna().mean())
names = {"anthropic_balanced": "Claude Sonnet 5.5", "anthropic_light": "Claude Haiku 5.5",
         "openai_balanced": "GPT-6.1 Sol", "openai_light": "GPT-6 Luna", "mistral_balanced": "Mistral Large 4",
         "mistral_light": "Mistral Small 4"}
print("L2 - L1 level by model (mine | manuscript_numbers.json)")
for mod in MODELS:
    print(f"  {names[mod]:18s} {lev[mod]:+.4f} | {v('ph_L2mL1_level_' + mod):+.4f}   ruler slope {slope[mod]:+.4f}")

six = sum(lev.values()) / sum(slope.values())
four = [mod for mod in MODELS if mod not in ("anthropic_light", "openai_balanced")]
fourv = sum(lev[k] for k in four) / sum(slope[k] for k in four)
print(f"pooled shift difference L2 - L1, six models : {six:.3f} (json {v('ph_L2mL1_shift'):.3f})")
print(f"same over the four models that moved       : {fourv:.3f}")
print(f"others_min / others_max in json: {v('ph_L2mL1_level_others_min'):+.4f} / {v('ph_L2mL1_level_others_max'):+.4f}; "
      f"mine over the four: {min(lev[k] for k in four):+.4f} / {max(lev[k] for k in four):+.4f}")
