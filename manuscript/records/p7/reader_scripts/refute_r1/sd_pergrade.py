import sys, json
import numpy as np, pandas as pd
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import analyze
df = pd.read_csv('/home/claude/art5-harmos-audit/results/measures.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
df['kept'] = analyze.as_bool(df['kept']); Y='mean_zipf_content'
d = df[df['kept'] & df['label'].isin(['L1','L1P','L3','L5'])]
topics = sorted(d.topic.unique()); T=len(topics); grades = analyze.GRADES
cube = {}
for lab in ['L1','L1P','L3','L5']:
    s = d[d.label==lab].groupby(['model','grade','topic'])[Y].mean()
    arr = np.full((6, 6, T), np.nan)
    models = sorted(d.model.unique())
    for (m,g,t),v in s.items(): arr[models.index(m), grades.index(g), topics.index(t)] = v
    cube[lab] = arr
def stat(w):
    out = {}
    for lab, arr in cube.items():
        m = (arr @ w) / w.sum()   # model x grade
        out[lab] = np.std(m, axis=0, ddof=1).mean()
    return out
w0 = np.ones(T); p = stat(w0); print("point per-grade-SD mean:", {k: round(v,4) for k,v in p.items()})
rng = np.random.default_rng(20261025); res=[]
for _ in range(2000):
    w = np.bincount(rng.integers(0,T,T), minlength=T).astype(float); s = stat(w); res.append([s['L3']-s['L1'], s['L3']-s['L5'], s['L3']-s['L1P']])
res = np.array(res)
print("L3-L1 point", round(p['L3']-p['L1'],4), "CI", np.percentile(res[:,0],[2.5,97.5]).round(4))
print("L3-L5 point", round(p['L3']-p['L5'],4), "CI", np.percentile(res[:,1],[2.5,97.5]).round(4))
print("L3-L1P point", round(p['L3']-p['L1P'],4), "CI", np.percentile(res[:,2],[2.5,97.5]).round(4))
