"""Leave-one-topic-out for the four primary tests, and the topic that moves H3-P most. Reads a COPY of the repo."""
import sys, numpy as np, pandas as pd
from scipy import stats
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
Y="mean_zipf_content"; AGE={"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}; G=list(AGE); ages=np.array(list(AGE.values()))
c=ages-ages.mean(); wg=c/(c**2).sum()
def tv(a,kind):
    x=df[df.label==a].set_index(["model","grade","genre","topic"])[Y]; y=df[df.label=="L5"].set_index(["model","grade","genre","topic"])[Y]
    d=(x-y).dropna().rename("d").reset_index()
    g=d.groupby(["topic","grade"]).d.mean().unstack("grade")[G]
    return (g.mean(axis=1) if kind=="level" else pd.Series(g.values@wg,index=g.index))
for nm,a,kind in (("H2-H","L1","level"),("H2-P","L1P","level"),("H3-H","L1","gradient"),("H3-P","L1P","gradient")):
    v=tv(a,kind); full=stats.ttest_1samp(v.values,0).pvalue
    ps={t:stats.ttest_1samp(v.drop(t).values,0).pvalue for t in v.index}
    lo=min(ps,key=ps.get); hi=max(ps,key=ps.get)
    print(f"{nm}: full p={full:.4f}; leave-one-topic-out p range [{ps[lo]:.4f} (drop '{lo}'), {ps[hi]:.4f} (drop '{hi}')]; topic values range {v.min():+.4f}..{v.max():+.4f}; SD {v.std(ddof=1):.4f}")
    if nm=="H3-P": print("   values by topic:", {k:round(float(x),4) for k,x in v.sort_values().items()})
