"""Between-model spread of the age-only texts, between-model SD by label, L3-L1 SD difference CI."""
import sys, json
import numpy as np, pandas as pd
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import analyze
df = pd.read_csv('/home/claude/art5-harmos-audit/results/measures.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
df['kept'] = analyze.as_bool(df['kept'])
Y = 'mean_zipf_content'
d = df[df['kept'] & df['label'].isin(analyze.GRADED_LABELS)]
# (a) model means of L5 per grade
l5 = d[d.label=='L5'].groupby(['grade','model'])[Y].mean().unstack()
print("L5 model means by grade:\n", l5.round(3))
rng_ = l5.max(1) - l5.min(1)
print("range across models per grade (Zipf):", rng_.round(3).to_dict())
slopes = json.load(open('/home/claude/art5-harmos-audit/results/numbers.json'))['h1']
mean_slope = np.mean([v['slope'] for v in slopes.values()])
print("mean ruler slope:", round(mean_slope,4), "-> range in years:", (rng_/abs(mean_slope)).round(2).to_dict())
print("SD across models per grade:", l5.std(1, ddof=1).round(3).to_dict())
# (b) between-model SD of label grand means (over grades, genres, topics)
gm = d.groupby(['label','model'])[Y].mean().unstack()
print("\nlabel grand means by model:\n", gm.round(3))
print("between-model SD by label:", gm.std(1, ddof=1).round(4).to_dict())
# also SD of per-grade model means averaged over grades
pg = d.groupby(['label','grade','model'])[Y].mean().unstack()
print("between-model SD by label, mean over grades of per-grade SD:", pg.std(1, ddof=1).groupby(level=0).mean().round(4).to_dict())
# bootstrap over topics: L3 SD - L1 SD
topics = sorted(d.topic.unique()); T = len(topics)
cube = {}
for lab in ['L1','L1P','L3','L5']:
    s = d[d.label==lab].groupby(['model','topic'])[Y].mean().unstack()  # model x topic
    cube[lab] = s.reindex(columns=topics).to_numpy()
rng = np.random.default_rng(20261025)
diffs = []; sds = {lab: [] for lab in cube}
for _ in range(2000):
    w = np.bincount(rng.integers(0, T, T), minlength=T).astype(float)
    m = {lab: (cube[lab] @ w) / w.sum() for lab in cube}
    sd = {lab: np.std(m[lab], ddof=1) for lab in cube}
    for lab in cube: sds[lab].append(sd[lab])
    diffs.append(sd['L3'] - sd['L1'])
diffs = np.array(diffs)
print("\nbootstrap (2000, topics) SD(L3)-SD(L1): point", round(np.std(cube['L3'].mean(1), ddof=1)-np.std(cube['L1'].mean(1), ddof=1),4),
      "CI", np.percentile(diffs,[2.5,97.5]).round(4))
for lab in cube: print(lab, "SD CI", np.percentile(sds[lab],[2.5,97.5]).round(4))
d2 = np.array(sds['L3']) - np.array(sds['L5'])
print("SD(L3)-SD(L5) CI", np.percentile(d2,[2.5,97.5]).round(4))
