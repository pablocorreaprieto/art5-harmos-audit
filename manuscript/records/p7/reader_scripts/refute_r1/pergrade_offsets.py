import sys, json
import numpy as np, pandas as pd
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import analyze
df = pd.read_csv('/home/claude/art5-harmos-audit/results/measures.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
df['kept'] = analyze.as_bool(df['kept']); Y='mean_zipf_content'
n = json.load(open('/home/claude/art5-harmos-audit/results/numbers.json'))
topics = sorted(df.topic.unique()); T = len(topics); grades = analyze.GRADES; AGES = analyze.AGES
def cube(model, lab):
    s = df[df.kept & (df.model==model) & (df.label==lab)].groupby(['grade','topic'])[Y].mean()
    a = np.full((6, T), np.nan)
    for (g,t),v in s.items(): a[grades.index(g), topics.index(t)] = v
    return a
rng = np.random.default_rng(20261025)
out = {}
for model in ['anthropic_light','mistral_light','anthropic_balanced','openai_balanced','openai_light','mistral_balanced']:
    for lab in ['L1','L1P']:
        a, b5 = cube(model, lab), cube(model, 'L5')
        def est(w):
            ma = (a @ w)/w.sum(); m5 = (b5 @ w)/w.sum()
            slope = np.polyfit(AGES, m5, 1)[0]
            return (ma - m5)/slope          # years, per grade; positive = older
        p = est(np.ones(T))
        boots = np.array([est(np.bincount(rng.integers(0,T,T), minlength=T).astype(float)) for _ in range(2000)])
        lo, hi = np.percentile(boots, [2.5, 97.5], axis=0)
        fitted = {g: n['age_equivalent']['by_label'][lab]['by_model'][model]['shift_years'] + (n['age_equivalent']['by_label'][lab]['by_model'][model]['tracking']-1)*(AGES[grades.index(g)]-AGES.mean()) for g in grades}
        print(f"{model} {lab}: observed 3H {p[0]:.2f} [{lo[0]:.2f}, {hi[0]:.2f}] (fitted {fitted['3H']:.2f}); 8H {p[5]:.2f} [{lo[5]:.2f}, {hi[5]:.2f}] (fitted {fitted['8H']:.2f}); all grades observed: {np.round(p,2).tolist()}")
        out[(model,lab)] = (p, lo, hi, fitted)
# conclusion check: how many models stay within one model-year at both 3H and 8H on fitted lines, and observed
for lab in ['L1','L1P']:
    fit_ok = [m for (m,l),(p,lo,hi,f) in out.items() if l==lab and abs(f['3H'])<=1 and abs(f['8H'])<=1]
    obs_ok = [m for (m,l),(p,lo,hi,f) in out.items() if l==lab and abs(p[0])<=1 and abs(p[5])<=1]
    avg_ok = [m for (m,l),(p,lo,hi,f) in out.items() if l==lab and abs(n['age_equivalent']['by_label'][lab]['by_model'][m]['shift_years'])<=1]
    print(lab, "fitted within 1 year at both ends:", fit_ok, "| observed:", obs_ok, "| averaged shift within 1 year:", avg_ok)
