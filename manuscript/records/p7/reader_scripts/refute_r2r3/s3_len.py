import numpy as np, pandas as pd
import statsmodels.formula.api as smf
REPO = "/home/claude/art5-harmos-audit"
df = pd.read_csv(f"{REPO}/results/measures.csv")
df["log_n"] = np.log(df["n_words"].astype(float))
Y = "mean_zipf_content"
# (a) the registered residualisation model (analyze.length_residualised): Y ~ C(model) + C(model):log_n, all kept texts
fit = smf.ols(f"{Y} ~ C(model) + C(model):log_n", data=df).fit()
print("(a) per-model slopes on log words, registered model, all labels:")
print({k.split('[')[1].split(']')[0].replace('T.', ''): round(v, 4) for k, v in fit.params.items() if ":log_n" in k})


def within(d, keys, label):
    d = d.copy()
    d["cell"] = d[keys].astype(str).agg("|".join, axis=1)
    n = d.groupby("cell")[Y].transform("size")
    d = d[n > 1]
    for col in [Y, "log_n"]:
        d[col + "_c"] = d[col] - d.groupby("cell")[col].transform("mean")
    f = smf.ols(f"{Y}_c ~ log_n_c - 1", data=d).fit()
    fc = smf.ols(f"{Y}_c ~ log_n_c - 1", data=d).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d["topic"])[0]})
    print(f"{label}: slope {f.params['log_n_c']:+.4f} naive SE {f.bse['log_n_c']:.4f} topic-clustered SE {fc.bse['log_n_c']:.4f} (n={len(d)})")


three = df[df["label"].isin(["L1", "L1P", "L5"])]
within(three, ["model", "grade", "genre", "topic"], "(b) L1, L1P, L5 within model x grade x genre x topic")
l5 = df[df["label"] == "L5"]
for keys in (["model", "grade", "genre"], ["model", "grade", "topic"], ["model", "genre", "topic"], ["model", "grade"]):
    within(l5, keys, "(c) L5 only within " + " x ".join(keys))
