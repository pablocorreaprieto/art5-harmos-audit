"""Re-measure texts with the local (pylexique) Lexique copy, collecting tokens absent from Lexique,
and recompute the content-lemma mean Zipf with and without those tokens. Read-only on the repo."""
import sys, json, re, math, collections
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import pandas as pd, numpy as np
import compute
LEX = '/usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt'
lex, sha = compute.load_lexicon(LEX)
REPO = '/home/claude/art5-harmos-audit'
meas = pd.read_csv(f'{REPO}/results/measures.csv')
keep_ids = set(meas.call_id)
texts = {}
for f in [f'{REPO}/data/raw/calls_20261101T075547530698Z.jsonl', f'{REPO}/data/raw/calls_20261101T101404154113Z.jsonl']:
    for line in open(f, encoding='utf-8'):
        r = json.loads(line)
        if r.get('kind') == 'text' and r['call_id'] in keep_ids:
            texts[r['call_id']] = r['text']
rows = []
oov_by_label = collections.defaultdict(collections.Counter)
for r in meas.itertuples():
    title, lines = compute.clean(texts[r.call_id])
    sents, toks = compute.analyse(lines, lex)
    z_all, z_in, n_oov = [], [], 0
    for t, low, name in toks:
        if low in compute.ELIDED or name:
            continue
        e = lex.get(low)
        if e is None:
            z_all.append(compute.zipf(0.0)); n_oov += 1
            oov_by_label[r.label][low] += 1
            continue
        cat, lemma, lemfreq, ff, _ = e
        if cat in compute.CONTENT and lemma not in compute.EXCLUDED_LEMMAS:
            z = compute.zipf(lemfreq); z_all.append(z); z_in.append(z)
    rows.append(dict(call_id=r.call_id, model=r.model, label=r.label, grade=r.grade, genre=r.genre, topic=r.topic,
                     z_orig=r.mean_zipf_content, z_local=np.mean(z_all) if z_all else np.nan,
                     z_no_oov=np.mean(z_in) if z_in else np.nan, n_content=len(z_all), n_oov_content=n_oov))
d = pd.DataFrame(rows)
d.to_csv('/tmp/r1_review/remeasured.csv', index=False)
print('lexicon sha', sha[:16])
print('agreement local vs frozen measure: share identical (|diff|<1e-9):', round((abs(d.z_local - d.z_orig) < 1e-9).mean(), 3),
      'max abs diff', round(abs(d.z_local - d.z_orig).max(), 4))
for lab in ['L2', 'L1', 'L1P', 'L5']:
    c = oov_by_label[lab]
    print(lab, 'total OOV content tokens', sum(c.values()), '| top:', c.most_common(25))
