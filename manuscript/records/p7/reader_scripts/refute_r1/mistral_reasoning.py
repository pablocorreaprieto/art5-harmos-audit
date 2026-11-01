"""Mistral Large 4 visible reasoning: stated age in L1/L1P/L5 texts, and the relation with the paired lexical difference."""
import sys, json, re
import numpy as np, pandas as pd
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import analyze
AGE_MID = analyze.AGE_MID
raw = {}
for f in ['/home/claude/art5-harmos-audit/data/raw/calls_20261101T075547530698Z.jsonl', '/home/claude/art5-harmos-audit/data/raw/calls_20261101T101404154113Z.jsonl']:
    for line in open(f):
        r = json.loads(line)
        if r.get('kind') == 'text' and r['model'] == 'mistral_balanced':
            raw[r['call_id']] = r
def thinking_text(r):
    msg = r['response']['choices'][0]['message']
    c = msg.get('content')
    out = []
    if isinstance(c, list):
        for part in c:
            if part.get('type') == 'thinking':
                th = part.get('thinking')
                if isinstance(th, list):
                    out += [p.get('text','') for p in th if isinstance(p, dict)]
                elif isinstance(th, str): out.append(th)
    return "\n".join(out)
NUM = {"quatre":4,"cinq":5,"six":6,"sept":7,"huit":8,"neuf":9,"dix":10,"onze":11,"douze":12,"treize":13,"quatorze":14,"quinze":15,"seize":16}
AGE_RE = re.compile(r"(\d{1,2})\s*(?:(?:à|-|–|—|ou|et|/)\s*(\d{1,2})\s*)?ans\b")
def first_age(t):
    t = t.lower().replace(" "," ").replace("\xa0"," ")
    for w,n in NUM.items(): t = re.sub(rf"\b{w}\b", str(n), t)
    m = AGE_RE.search(t)
    if not m: return None
    lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
    if hi < lo: hi = lo
    return (lo+hi)/2
meas = pd.read_csv('/home/claude/art5-harmos-audit/results/measures.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
meas = meas[meas.model=='mistral_balanced']
Y='mean_zipf_content'
rows=[]
for r in meas.itertuples():
    rr = raw[r.call_id]
    th = thinking_text(rr)
    rows.append({'call_id': r.call_id, 'label': r.label, 'grade': r.grade, 'genre': r.genre, 'topic': r.topic, 'y': getattr(r, Y),
                 'has_thinking': len(th) > 0, 'stated': first_age(th), 'thinking_len': len(th)})
t = pd.DataFrame(rows)
t['true_mid'] = t.grade.map(AGE_MID)
t['err'] = t.stated - t.true_mid
for lab in ['L1','L1P','L5','L3','L4','L2']:
    s = t[t.label==lab]
    stated = s.stated.notna()
    wrong = (s.err.abs() > 1.0)  # outside true range +- 0.5: true range is mid+-0.5, so |err|>1.0 means midpoint outside widened range
    print(f"{lab}: n={len(s)}, has_thinking={s.has_thinking.mean():.2%}, states age={stated.mean():.2%}, wrong (|err|>1.0) among all={wrong.mean():.2%}, among stated={wrong[stated].mean():.2%}, mean err among stated={s.err[stated].mean():.2f}, share err>=1.5 & <=2.5 among stated={((s.err>=1.5)&(s.err<=2.5))[stated].mean():.2%}")
# paired difference L1-L5 per (grade, genre, topic) vs stated error in L1
l5 = t[t.label=='L5'].set_index(['grade','genre','topic'])['y']
slope_ruler = json.load(open('/home/claude/art5-harmos-audit/results/numbers.json'))['h1']['mistral_balanced']['slope']
import statsmodels.formula.api as smf
for lab in ['L1','L1P']:
    s = t[t.label==lab].copy()
    s['d'] = s.y.values - l5.reindex(list(zip(s.grade, s.genre, s.topic))).values
    s2 = s[s.err.notna()]
    r = smf.ols('d ~ err', data=s2).fit(cov_type='cluster', cov_kwds={'groups': pd.factorize(s2.topic)[0]})
    r0 = smf.ols('d ~ err', data=s2).fit()
    print(f"{lab}: d ~ stated error: slope {r.params['err']:.4f} (cluster SE {r.bse['err']:.4f}, p={r.pvalues['err']:.3f}; OLS SE {r0.bse['err']:.4f}, p={r0.pvalues['err']:.3f}); n={len(s2)}; ruler slope {slope_ruler:.4f}")
    # mean d when wrong vs right
    s2['wrong'] = s2.err.abs() > 1.0
    print("   mean d by wrong:", s2.groupby('wrong')['d'].agg(['mean','count']).round(4).to_dict())
    print("   err distribution:", s2.err.round(1).value_counts().sort_index().to_dict())
t.to_csv('/tmp/refute_r1/mistral_reasoning.csv', index=False)
# examples
ex = t[(t.label=='L1')&(t.err>=1.5)].head(3)
for cid in ex.call_id:
    th = thinking_text(raw[cid]); print('---', cid, raw[cid]['prompt']); print(th[:400].replace('\n',' '))
