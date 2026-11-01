"""(1) L2 minus L1 (effect of adding 'en Suisse romande' to the H label), topic-level t-test and pooled shift difference
with the same topic bootstrap; (2) text-length descriptives quoted in the Data paragraph. Reads a COPY of the repo."""
import sys, numpy as np, pandas as pd
from scipy import stats
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
Y="mean_zipf_content"; AGE={"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}; G=list(AGE); ages=np.array(list(AGE.values()))
models=sorted(df.model.unique()); topics=sorted(df.topic.unique()); T=len(topics)
labs=["L1","L1P","L2","L3","L4","L5"]
A=np.full((6,6,6,T),np.nan)
for i,l in enumerate(labs):
    for (m,g,t),v in df[df.label==l].groupby(["model","grade","topic"])[Y].mean().items(): A[i,models.index(m),G.index(g),topics.index(t)]=v
c=ages-ages.mean(); wg=c/(c**2).sum()
# topic-level t-test of L2 - L1 level and gradient
d=A[labs.index("L2")]-A[labs.index("L1")]            # model, grade, topic
lev=d.mean(axis=(0,1)); grd=np.einsum("mgt,g->t",d,wg)/6
for nm,x in (("level",lev),("gradient",grd)):
    t=stats.ttest_1samp(x,0); q=stats.t.ppf(.975,T-1); se=x.std(ddof=1)/np.sqrt(T)
    print(f"L2 - L1 {nm}: {x.mean():+.4f} [{x.mean()-q*se:+.4f}, {x.mean()+q*se:+.4f}] t({T-1})={t.statistic:.2f} p={t.pvalue:.4f}")
def shifts(w):
    w=w/w.sum(); mean=np.einsum("lmgt,t->lmg",A,w); r=mean[labs.index("L5")]
    b=np.array([np.polyfit(ages,r[m],1)[0] for m in range(6)])
    out={}
    for l in ("L1","L2","L3"):
        x=mean[labs.index(l)]-r; out[l]=x.mean(1).sum()/b.sum()
    return out
p=shifts(np.ones(T)); rng=np.random.default_rng(20261025)
bs=[shifts(np.bincount(rng.integers(0,T,T),minlength=T).astype(float)) for _ in range(2000)]
for a,b in (("L2","L1"),("L3","L1"),("L3","L2")):
    dd=np.array([x[a]-x[b] for x in bs]); print(f"pooled shift {a} - {b}: {p[a]-p[b]:+.2f} years, 95% percentile [{np.percentile(dd,2.5):+.2f}, {np.percentile(dd,97.5):+.2f}]")
print("point shifts:", {k:round(v,3) for k,v in p.items()})
# per-model L2-L1 level
for i,m in enumerate(models):
    x=d[i].mean(axis=0); print(f"  {m:20s} L2-L1 level {x.mean():+.4f} (SD over topics {x.std(ddof=1):.4f})")
# lengths
nw=df.n_words.astype(float); print("n_words: mean %.1f median %.1f"%(nw.mean(),nw.median()))
print(df.groupby("model").n_words.mean().round(0).to_dict())
print("truncated", int(df.truncated.astype(str).str.lower().isin(["true","1"]).sum()), "flag_meta", int(df.flag_meta.astype(str).str.lower().isin(["true","1"]).sum()), "dup", int(df.duplicate_text.astype(str).str.lower().isin(["true","1"]).sum()))
