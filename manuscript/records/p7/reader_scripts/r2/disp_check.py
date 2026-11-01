import sys, numpy as np, pandas as pd
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
Y="mean_zipf_content"; AGE={"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}; G=list(AGE); ages=np.array(list(AGE.values()))
models=sorted(df.model.unique()); topics=sorted(df.topic.unique()); T=len(topics)
labs=["L1","L1P","L2","L3","L4","L5"]
A=np.full((6,6,6,T),np.nan)
for i,l in enumerate(labs):
    for (m,g,t),v in df[df.label==l].groupby(["model","grade","topic"])[Y].mean().items(): A[i,models.index(m),G.index(g),topics.index(t)]=v
c=ages-ages.mean(); wg=c/(c**2).sum()
def per_model(w):
    w=w/w.sum(); mean=np.einsum("lmgt,t->lmg",A,w); r=mean[labs.index("L5")]; b=np.array([np.polyfit(ages,r[m],1)[0] for m in range(6)])
    out={}
    for l in ("L1","L1P","L2","L3","L4"):
        x=mean[labs.index(l)]-r; out[l]=(x.mean(1)/b, 1+(x@wg)/b)
    return out
p=per_model(np.ones(T)); rng=np.random.default_rng(5)
bs=[per_model(np.bincount(rng.integers(0,T,T),minlength=T).astype(float)) for _ in range(5000)]
def sd(x): return x.std(ddof=1)
print("between-model SD of per-model estimates (point; 95% boot):")
for l in ("L1","L1P","L2","L3","L4"):
    for k,nm in ((0,"shift"),(1,"tracking")):
        pt=sd(p[l][k]); b=np.array([sd(x[l][k]) for x in bs]); print(f"  {l:4s} {nm:9s} SD {pt:.2f}  [{np.percentile(b,2.5):.2f}, {np.percentile(b,97.5):.2f}]")
for k,nm in ((0,"shift"),(1,"tracking")):
    d=np.array([sd(x["L1"][k])-sd(x["L3"][k]) for x in bs]); r=np.array([sd(x["L3"][k])/sd(x["L1"][k]) for x in bs])
    print(f"SD(L1)-SD(L3) {nm}: point {sd(p['L1'][k])-sd(p['L3'][k]):.2f}, 95% boot [{np.percentile(d,2.5):.2f},{np.percentile(d,97.5):.2f}], share of resamples with SD(L3) < SD(L1): {(d>0).mean():.3f}; ratio SD(L3)/SD(L1) point {sd(p['L3'][k])/sd(p['L1'][k]):.2f} [{np.percentile(r,2.5):.2f},{np.percentile(r,97.5):.2f}]")
# but excluding Haiku (the main source of dispersion in L1)
keep=[i for i,m in enumerate(models) if m!="anthropic_light"]
print("excluding Claude Haiku 5.5: SD(L1 shift) %.2f vs SD(L3 shift) %.2f ; SD(L1 tracking) %.2f vs SD(L3 tracking) %.2f"%(sd(p['L1'][0][keep]),sd(p['L3'][0][keep]),sd(p['L1'][1][keep]),sd(p['L3'][1][keep])))
print("L1 shifts",np.round(p['L1'][0],2),"L3 shifts",np.round(p['L3'][0],2))
print("L1 tracking",np.round(p['L1'][1],2),"L3 tracking",np.round(p['L3'][1],2))
