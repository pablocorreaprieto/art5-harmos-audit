import sys, numpy as np, pandas as pd
from scipy import stats
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
AGE={"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}; G=list(AGE); Y="mean_zipf_content"
ages=np.array(list(AGE.values())); c=ages-ages.mean()
def tv(a,b,kind,models):
    x=df[df.label==a].set_index(["model","grade","genre","topic"])[Y]; y=df[df.label==b].set_index(["model","grade","genre","topic"])[Y]
    d=(x-y).dropna().rename("d").reset_index(); d=d[d.model.isin(models)]
    g=d.groupby(["topic","grade"]).d.mean().unstack("grade")[G]
    return g.mean(axis=1).values if kind=="level" else g.values@(c/(c**2).sum())
allm=sorted(df.model.unique())
print("leave-one-model-out, uncorrected two-sided p (5 models, 16 topics)")
for drop in [None]+allm:
    ms=[m for m in allm if m!=drop]; out=[]
    for nm,a,kind in (("H2-H","L1","level"),("H2-P","L1P","level"),("H3-H","L1","gradient"),("H3-P","L1P","gradient")):
        x=tv(a,"L5",kind,ms); t=stats.ttest_1samp(x,0); out.append(f"{nm} {x.mean():+.4f} (p={t.pvalue:.3f})")
    print(f"drop {str(drop):20s}"," | ".join(out))
# models as random: one-sample t over six per-model estimates (level, exploratory)
for nm,a,kind in (("H2-H","L1","level"),("H2-P","L1P","level"),("H3-H","L1","gradient"),("H3-P","L1P","gradient")):
    v=np.array([tv(a,"L5",kind,[m]).mean() for m in allm]); t=stats.ttest_1samp(v,0); q=stats.t.ppf(.975,5); se=v.std(ddof=1)/np.sqrt(6)
    print(f"models as random effects, {nm}: mean {v.mean():+.4f}, SD across models {v.std(ddof=1):.4f}, 95% CI [{v.mean()-q*se:+.4f}, {v.mean()+q*se:+.4f}] (t5), p = {t.pvalue:.3f}")
# the same on the years scale for the L1 shift: per-model shifts mean/SD
sh=np.array([-0.254,2.124,0.786,-0.487,-0.131,-0.768]); q=stats.t.ppf(.975,5); se=sh.std(ddof=1)/np.sqrt(6)
print("per-model L1 shifts: mean %.2f, SD %.2f, t5 95%% CI [%.2f, %.2f]; median %.2f"%(sh.mean(),sh.std(ddof=1),sh.mean()-q*se,sh.mean()+q*se,np.median(sh)))
