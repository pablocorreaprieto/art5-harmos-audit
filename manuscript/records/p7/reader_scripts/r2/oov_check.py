import sys, numpy as np, pandas as pd
from scipy import stats
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
AGE={"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}; G=list(AGE)
def tv(a,b,kind,Y):
    x=df[df.label==a].set_index(["model","grade","genre","topic"])[Y]; y=df[df.label==b].set_index(["model","grade","genre","topic"])[Y]
    d=(x-y).dropna().rename("d").reset_index(); g=d.groupby(["topic","grade"]).d.mean().unstack("grade")[G]
    ag=np.array(list(AGE.values())); c=ag-ag.mean()
    return g.mean(axis=1).values if kind=="level" else g.values@(c/(c**2).sum())
print("share_oov (token share absent from Lexique), mean by label:", df.groupby("label").share_oov.mean().round(4).to_dict())
print("share_oov by model:", df.groupby("model").share_oov.mean().round(4).to_dict())
for lab in ("L1","L1P"):
    for kind in ("level","gradient"):
        x=tv(lab,"L5",kind,"share_oov"); t=stats.ttest_1samp(x,0)
        print(f"share_oov {lab}-L5 {kind}: mean {x.mean()*100:.3f} pp, t {t.statistic:.2f}, p {t.pvalue:.3f}")
# how much of the H2-H effect could OOV carry? regress text-level Y on share_oov within model
import statsmodels.formula.api as smf
r=smf.ols("mean_zipf_content ~ share_oov + C(model) + C(grade) + C(genre) + C(topic)",data=df[df.label.isin(["L1","L1P","L5"])]).fit()
print("within-condition slope of mean Zipf on share_oov:", round(r.params["share_oov"],3), "(Zipf per 1.0 share; i.e., per 1 pp:", round(r.params["share_oov"]/100,4),")")
