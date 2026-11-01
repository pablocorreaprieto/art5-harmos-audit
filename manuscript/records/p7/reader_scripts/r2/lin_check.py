import sys, numpy as np, pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
REPO=sys.argv[1]
df=pd.read_csv(f"{REPO}/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"])
AGE={"3H":6.5,"4H":7.5,"5H":8.5,"6H":9.5,"7H":10.5,"8H":11.5}
l5=df[df.label=="L5"].copy(); l5["a"]=(l5.grade.map(AGE)-9.0)/2.5
# orthogonal polynomial terms
P=np.polynomial.legendre
for k in range(2,6): l5[f"p{k}"]=P.Legendre.basis(k)(l5.a.values)
Y="mean_zipf_content"
for m,s in l5.groupby("model"):
    s=s.reset_index(drop=True); g=pd.factorize(s.topic)[0]
    # classical F test (the pipeline's)
    lin=smf.ols(f"{Y} ~ a + C(genre) + C(topic)",data=s).fit()
    full=smf.ols(f"{Y} ~ a + p2 + p3 + p4 + p5 + C(genre) + C(topic)",data=s).fit()
    F,pF,_=full.compare_f_test(lin)
    # cluster-robust Wald F for p2..p5 jointly = 0, reference F(4, G-1)
    rc=smf.ols(f"{Y} ~ a + p2 + p3 + p4 + p5 + C(genre) + C(topic)",data=s).fit(cov_type="cluster",cov_kwds={"groups":g,"use_correction":True})
    w=rc.wald_test("p2 = 0, p3 = 0, p4 = 0, p5 = 0",use_f=True,scalar=True)
    # note: with G=16 clusters the Wald covariance of 4 contrasts is rank-limited but < G-1, valid
    print(f"{m:20s} classical F(4,{int(full.df_resid)}) = {F:.3f} p = {pF:.3f} | cluster-robust Wald F = {float(w.statistic):.3f}, p(F(4,{15})) = {float(stats.f.sf(float(w.statistic),4,15)):.3f}; p(chi2 4) = {float(stats.chi2.sf(4*float(w.statistic),4)):.3f}")
