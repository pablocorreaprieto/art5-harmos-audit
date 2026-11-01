import sys, numpy as np, pandas as pd
from scipy import stats
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
AGE={"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}; G=list(AGE)
a=(np.array(list(AGE.values()))-9.0)/2.5
V=np.vander(a,6,increasing=True)           # 1, a, a^2 ... a^5
Q,_=np.linalg.qr(V)                         # orthonormal columns: const, linear, then 4 nonlinear contrasts
B=Q[:,2:]                                   # 6 x 4, orthogonal to const and linear
assert np.allclose(B.T@np.ones(6),0) and np.allclose(B.T@a,0)
Y="mean_zipf_content"; l5=df[df.label=="L5"]
for m,s in l5.groupby("model"):
    tm=s.groupby(["topic","grade"])[Y].mean().unstack("grade")[G]    # 16 x 6 (mean over genres)
    Z=tm.values@B; n,p=Z.shape; mu=Z.mean(0); S=np.cov(Z.T)
    T2=n*mu@np.linalg.solve(S,mu); F=(n-p)/(p*(n-1))*T2; pv=stats.f.sf(F,p,n-p)
    rng=np.random.default_rng(1); cnt=0; N=20000
    for _ in range(N):
        sg=rng.choice([-1,1],n)[:,None]; Zs=Z*sg; ms=Zs.mean(0); Ss=np.cov(Zs.T); t2=n*ms@np.linalg.solve(Ss,ms); cnt+=(t2>=T2-1e-12)
    print(f"{m:20s} topic-level Hotelling T2 = {T2:6.2f}, F(4,12) = {F:.3f}, p = {pv:.3f}; sign-flip permutation p = {(cnt+1)/(N+1):.3f}")
