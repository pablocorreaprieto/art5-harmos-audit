import sys, numpy as np, pandas as pd
import statsmodels.formula.api as smf
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import analyze
df = pd.read_csv('/home/claude/art5-harmos-audit/results/measures.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
df['kept'] = analyze.as_bool(df['kept']); Y='mean_zipf_content'
d = df[df.kept & df.label.isin(['L1','L1P','L5'])].copy()
d['mg'] = d.model + '_' + d.grade; d['age_c'] = d.grade.map(analyze.AGE_MID) - analyze.AGES.mean()
models = sorted(d.model.unique()); code = {m: f"m{i}" for i,m in enumerate(models)}; terms=[]
for m in models:
    for lab in ['L1','L1P']:
        lev, grd = f"lev_{lab}_{code[m]}", f"grd_{lab}_{code[m]}"
        d[lev] = ((d.label==lab)&(d.model==m)).astype(float); d[grd] = d[lev]*d.age_c; terms += [lev, grd]
groups = pd.factorize(d.topic)[0]
res = smf.ols(f"{Y} ~ C(mg) + " + " + ".join(terms) + " + C(genre) + C(topic) - 1", data=d).fit(cov_type='cluster', cov_kwds={'groups': groups, 'use_correction': True})
for lab in ['L1','L1P']:
    for kind in ['lev','grd']:
        names = [f"{kind}_{lab}_{code[m]}" for m in models]
        # equality constraints: term_i - term_0 = 0 for i>0
        cons = ", ".join(f"{n} - {names[0]} = 0" for n in names[1:])
        w = res.wald_test(cons, use_f=True, scalar=True)
        print(f"{lab} {kind}: equality across the six models, F = {float(w.statistic):.2f}, df = {w.df_num}, {w.df_denom}, p = {float(w.pvalue):.2g}")
