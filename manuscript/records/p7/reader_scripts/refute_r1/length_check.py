import sys, json
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import analyze
df = pd.read_csv('/home/claude/art5-harmos-audit/results/measures.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
df['kept'] = analyze.as_bool(df['kept']); Y='mean_zipf_content'
d = df[df.kept & (df.n_words>0)].copy(); d['log_n'] = np.log(d.n_words.astype(float))
# preregistered: Y ~ C(model) + C(model):log_n across everything
fit = smf.ols(f"{Y} ~ C(model) + C(model):log_n", data=d).fit()
print("preregistered per-model log-length slopes:", {k.split('[')[1].split(']')[0]: round(v,4) for k,v in fit.params.items() if 'log_n' in k})
# within-cell: model x label x grade x genre cells, topic effects
d['cell'] = d.model + '_' + d.label + '_' + d.grade + '_' + d.genre
g = d[d.label.isin(['L1','L1P','L5'])]
fit2 = smf.ols(f"{Y} ~ C(cell) + C(topic) + log_n", data=g).fit(cov_type='cluster', cov_kwds={'groups': pd.factorize(g.topic)[0]})
print("within-cell log-length slope (L1,L1P,L5):", round(fit2.params['log_n'],4), "SE", round(fit2.bse['log_n'],4))
fit3 = smf.ols(f"{Y} ~ C(cell) + C(topic) + log_n", data=d).fit(cov_type='cluster', cov_kwds={'groups': pd.factorize(d.topic)[0]})
print("within-cell log-length slope (all labels):", round(fit3.params['log_n'],4), "SE", round(fit3.bse['log_n'],4))
# per-model within-cell slopes
for m, sub in g.groupby('model'):
    f = smf.ols(f"{Y} ~ C(cell) + C(topic) + log_n", data=sub).fit()
    print("  ", m, round(f.params['log_n'],4))
# implied bias: mean log-length difference L1-L5 (paired) times slope
l5 = g[g.label=='L5'].set_index(['model','grade','genre','topic'])['log_n']
for lab in ['L1','L1P']:
    s = g[g.label==lab]
    dl = s.log_n.values - l5.reindex(list(zip(s.model, s.grade, s.genre, s.topic))).values
    print(lab, "mean paired log-length difference:", round(np.nanmean(dl),4), "-> implied H2 bias at within-cell slope:", round(np.nanmean(dl)*fit2.params['log_n'],4))
# recompute H2 with within-cell length adjustment: subtract slope*(log_n - mean) and rerun primary tests
d2 = df.copy(); d2['kept']=analyze.as_bool(d2['kept'])
ok = d2.kept & (d2.n_words>0)
d2.loc[ok, Y] = d2.loc[ok, Y] - fit2.params['log_n'] * (np.log(d2.loc[ok,'n_words'].astype(float)) - np.log(d2.loc[ok,'n_words'].astype(float)).mean())
ax = analyze.axes(d2[d2.label.isin(analyze.GRADED_LABELS)])
res = analyze.primary_from_cubes(analyze.to_cubes(d2, Y, ax))
for k,v in res.items(): print("within-cell adjusted", k, round(v['estimate'],4), "p", round(v['p_two_sided'],3))
n = json.load(open('/home/claude/art5-harmos-audit/results/numbers.json'))
for k,v in n['sensitivity']['length_residualised'].items():
    if isinstance(v, dict): print("prereg residualised", k, round(v['estimate'],4), "p", round(v['p_two_sided'],3), "| primary", round(n['primary'][k]['estimate'],4))
