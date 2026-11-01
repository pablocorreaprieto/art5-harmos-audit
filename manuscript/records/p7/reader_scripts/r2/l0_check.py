import sys, numpy as np, pandas as pd
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
Y="mean_zipf_content"; AGE={"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}; G=list(AGE); ages=np.array(list(AGE.values()))
models=sorted(df.model.unique()); topics=sorted(df.topic.unique()); T=len(topics)
L5=np.full((6,6,T),np.nan); L0=np.full((6,T),np.nan)
for (m,g,t),v in df[df.label=="L5"].groupby(["model","grade","topic"])[Y].mean().items(): L5[models.index(m),G.index(g),topics.index(t)]=v
for (m,t),v in df[df.label=="L0"].groupby(["model","topic"])[Y].mean().items(): L0[models.index(m),topics.index(t)]=v
def est(w):
    w=w/w.sum(); r=L5@w; l0=L0@w
    b=np.array([np.polyfit(ages,r[i],1)[0] for i in range(6)])
    return 9+(l0-r.mean(axis=1))/b
rng=np.random.default_rng(3)
bs=np.array([est(np.bincount(rng.integers(0,T,T),minlength=T).astype(float)) for _ in range(5000)])
p=est(np.ones(T))
for i,m in enumerate(models):
    print(f"{m:20s} L0 age {p[i]:.2f}  95% boot [{np.percentile(bs[:,i],2.5):.2f}, {np.percentile(bs[:,i],97.5):.2f}]  beyond the oldest ruler point (11.5): {p[i]>11.5}")
