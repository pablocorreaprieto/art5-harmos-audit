import sys, numpy as np, pandas as pd
from scipy import stats
W = sys.argv[1]
m = pd.read_csv(f"{W}/results/measures.csv"); m = m[m["kept"] == True]
Y = "mean_zipf_content"
keys = ["model", "grade", "genre", "topic"]
a = m[m.label == "L2"].set_index(keys)[Y]; b = m[m.label == "L1"].set_index(keys)[Y]
d = (a - b).dropna().rename("d").reset_index()
NAMES = {"anthropic_balanced": "Sonnet 5.5", "anthropic_light": "Haiku 5.5", "openai_balanced": "GPT-6.1 Sol", "openai_light": "GPT-6 Luna", "mistral_balanced": "Mistral Large 4", "mistral_light": "Mistral Small 4"}
for mo, g in d.groupby("model"):
    pt = g.groupby("topic")["d"].mean()          # per-topic mean over grades and genres
    n = len(pt); mean = pt.mean(); se = pt.std(ddof=1) / np.sqrt(n)
    tcrit = stats.t.ppf(0.975, n - 1)
    p = 2 * stats.t.sf(abs(mean / se), n - 1)
    print(f"{NAMES[mo]:16s} L2-L1 level {mean:+.4f}  95% CI over {n} topics [{mean - tcrit * se:+.4f}, {mean + tcrit * se:+.4f}]  p={p:.4f}")
