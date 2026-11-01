import sys, json, re
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import analyze
t = pd.read_csv('/tmp/refute_r1/mistral_reasoning.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
Y='y'
l5 = t[t.label=='L5'].set_index(['grade','genre','topic'])['y']
print("outliers:", t[(t.err.abs()>10)][['call_id','label','grade','stated']].to_dict('records'))
slope_ruler = json.load(open('/home/claude/art5-harmos-audit/results/numbers.json'))['h1']['mistral_balanced']['slope']
for lab in ['L1','L1P']:
    s = t[t.label==lab].copy()
    s['d'] = s.y.values - l5.reindex(list(zip(s.grade, s.genre, s.topic))).values
    s2 = s[s.err.notna() & (s.err.abs() < 10)].copy()
    r = smf.ols('d ~ err', data=s2).fit()
    rc = smf.ols('d ~ err', data=s2).fit(cov_type='cluster', cov_kwds={'groups': pd.factorize(s2.topic)[0]})
    print(f"{lab}: slope {r.params['err']:.4f} (OLS SE {r.bse['err']:.4f}, p={r.pvalues['err']:.3f}; cluster SE {rc.bse['err']:.4f}, p={rc.pvalues['err']:.3f}), n={len(s2)}, ruler {slope_ruler:.4f}")
    # with grade and genre fixed effects
    r2 = smf.ols('d ~ err + C(grade) + C(genre)', data=s2).fit(cov_type='cluster', cov_kwds={'groups': pd.factorize(s2.topic)[0]})
    print(f"   with grade+genre FE: slope {r2.params['err']:.4f} (cluster SE {r2.bse['err']:.4f}, p={r2.pvalues['err']:.3f})")
    s2['wrong'] = s2.err != 0
    print("   share err!=0 among stated:", round(s2.wrong.mean(),3), " among all:", round(s2.wrong.sum()/len(s),3))
    print("   mean d: err==0:", round(s2[s2.err==0].d.mean(),4), " err==2:", round(s2[s2.err==2].d.mean(),4), " err>=1.5:", round(s2[s2.err>=1.5].d.mean(),4), " n", (s2.err>=1.5).sum())
    # implied shift years in each group
    print("   implied years: err==0:", round(s2[s2.err==0].d.mean()/slope_ruler,2), " err>=1.5:", round(s2[s2.err>=1.5].d.mean()/slope_ruler,2))
