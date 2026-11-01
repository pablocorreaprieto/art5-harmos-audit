"""H1 and the clustered OLS: replicate, then check with topic-level slopes and a wild cluster bootstrap (Rademacher and
Webb weights), 9,999 draws, restricted (null-imposed) residuals. Nothing written to the repository."""
import sys
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

REPO = sys.argv[1]
df = pd.read_csv(f"{REPO}/results/measures.csv", keep_default_na=False, na_values=["", "nan", "NaN"])
Y = "mean_zipf_content"
AGE = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
rng = np.random.default_rng(12345)

l5 = df[df.label == "L5"].copy()
l5["age"] = l5.grade.map(AGE)
out = {}
for m, sub in l5.groupby("model"):
    sub = sub.reset_index(drop=True)
    groups = pd.factorize(sub.topic)[0]
    G = groups.max() + 1
    # (a) the preregistered model
    r = smf.ols(f"{Y} ~ age + C(genre) + C(topic)", data=sub).fit(cov_type="cluster", cov_kwds={"groups": groups, "use_correction": True})
    b, se = r.params["age"], r.bse["age"]
    p_prereg = stats.t.cdf(b / se, G - 1)
    # (b) classical OLS SE (no clustering) for comparison
    r0 = smf.ols(f"{Y} ~ age + C(genre) + C(topic)", data=sub).fit()
    # (c) topic-level slopes: slope of Y on age within each topic (genre FE), one-sample t over topics
    sl = []
    for t_, g in sub.groupby("topic"):
        rr = smf.ols(f"{Y} ~ age + C(genre)", data=g).fit()
        sl.append(rr.params["age"])
    sl = np.array(sl)
    t_top = sl.mean() / (sl.std(ddof=1) / np.sqrt(len(sl)))
    p_top = stats.t.cdf(t_top, len(sl) - 1)
    # (d) wild cluster bootstrap-t, null imposed (slope = 0), weights Rademacher and Webb
    X = sm.add_constant(pd.get_dummies(sub[["genre", "topic"]], drop_first=True).astype(float))
    X["age"] = sub["age"].values
    Xr = X.drop(columns="age")
    yv = sub[Y].values
    fit_r = sm.OLS(yv, Xr).fit()
    yhat_r, u_r = fit_r.fittedvalues.values, fit_r.resid.values
    def cr1_t(yy):
        f = sm.OLS(yy, X).fit(cov_type="cluster", cov_kwds={"groups": groups, "use_correction": True})
        return f.params["age"] / f.bse["age"]
    t_obs = cr1_t(yv)
    webb = np.array([-np.sqrt(1.5), -1, -np.sqrt(.5), np.sqrt(.5), 1, np.sqrt(1.5)])
    res = {}
    for kind in ("rademacher", "webb"):
        B = 4999
        ts = np.empty(B)
        for i in range(B):
            w = rng.choice([-1.0, 1.0], G) if kind == "rademacher" else rng.choice(webb, G)
            ystar = yhat_r + u_r * w[groups]
            ts[i] = cr1_t(ystar)
        res[kind] = float((np.sum(ts <= t_obs) + 1) / (B + 1))  # one-sided: slope < 0
    out[m] = dict(slope=b, se_cluster=se, t=b / se, p_t15=p_prereg, se_classic=r0.bse["age"], t_classic=r0.params["age"] / r0.bse["age"],
                  slope_topic_mean=sl.mean(), t_topic=t_top, p_topic=p_top, p_wild_rad=res["rademacher"], p_wild_webb=res["webb"])
    print(m, {k: (float(f"{v:.6g}")) for k, v in out[m].items()})
