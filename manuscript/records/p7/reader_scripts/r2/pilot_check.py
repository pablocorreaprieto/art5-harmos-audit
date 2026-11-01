import sys, json, numpy as np, pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/pilot_measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
df=df[df.block=="ruler"].copy(); df["age"]=df.grade.map({"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5})
r=smf.ols("mean_zipf_content ~ C(model):C(grade) + C(genre) + C(topic)",data=df).fit()
s=float(np.sqrt(r.scale)); d=float(r.df_resid); up=s*np.sqrt(d/stats.chi2.ppf(.2,d))
print("pilot sigma %.5f df %.0f upper80 %.5f"%(s,d,up))
ps=json.load(open(f"{REPO}/results/pilot_summary.json"))["ruler"]; print("stored", ps["sigma"], ps["sigma_df"], ps["sigma_upper80"])
pooled=smf.ols("mean_zipf_content ~ age + C(model) + C(genre) + C(topic)",data=df).fit(cov_type="HC3")
print("pooled slope %.5f HC3 se %.5f z p(one-sided, normal) %.2e"%(pooled.params["age"],pooled.bse["age"],stats.norm.cdf(pooled.params["age"]/pooled.bse["age"])))
g=pd.factorize(df.topic)[0]
pc=smf.ols("mean_zipf_content ~ age + C(model) + C(genre) + C(topic)",data=df).fit(cov_type="cluster",cov_kwds={"groups":g,"use_correction":True})
t=pc.params["age"]/pc.bse["age"]; print("topic-clustered (6 clusters): se %.5f t %.2f one-sided p (t5) %.2e"%(pc.bse["age"],t,stats.t.cdf(t,5)))
# per-model with clusters
for m,s_ in df.groupby("model"):
    gg=pd.factorize(s_.topic)[0]; rr=smf.ols("mean_zipf_content ~ age + C(genre) + C(topic)",data=s_).fit(cov_type="cluster",cov_kwds={"groups":gg,"use_correction":True})
    tt=rr.params["age"]/rr.bse["age"]; print("  ",m,"slope %.4f t %.2f p(t5) %.1e"%(rr.params["age"],tt,stats.t.cdf(tt,5)))
