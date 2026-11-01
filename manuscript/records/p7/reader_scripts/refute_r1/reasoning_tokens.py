import json, numpy as np, pandas as pd
rows=[]
for f in ['/home/claude/art5-harmos-audit/data/raw/calls_20261101T075547530698Z.jsonl','/home/claude/art5-harmos-audit/data/raw/calls_20261101T101404154113Z.jsonl']:
    for line in open(f):
        r = json.loads(line)
        u = r['response'].get('usage', {}) if isinstance(r.get('response'), dict) else {}
        rt = None
        if r['provider']=='anthropic': rt = (u.get('output_tokens_details') or {}).get('thinking_tokens')
        elif r['provider']=='openai': rt = (u.get('completion_tokens_details') or {}).get('reasoning_tokens')
        elif r['provider']=='mistral': rt = (u.get('completion_tokens_details') or {}).get('reasoning_tokens')
        rows.append(dict(kind=r.get('kind'), model=r['model'], label=r.get('label'), grade=r.get('grade'), rt=rt, out=r.get('output_tokens'), cost=r.get('cost_usd'), fin=r.get('finish_reason')))
d = pd.DataFrame(rows)
print("missing reasoning field:", d.rt.isna().sum())
t = d[d.kind=='text']
print(t.pivot_table(index='model', columns='label', values='rt', aggfunc='mean').round(0))
print("share of texts with reasoning>0:\n", t.assign(any=t.rt>0).pivot_table(index='model', columns='label', values='any', aggfunc='mean').round(2))
print("probes mean reasoning:", d[d.kind=='probe'].groupby('model').rt.mean().round(0).to_dict())
print("total cost:", round(d.cost.sum(),2), "by provider-model:", d.groupby('model').cost.sum().round(2).to_dict())
print("finish reasons:", d.fin.value_counts().to_dict())
