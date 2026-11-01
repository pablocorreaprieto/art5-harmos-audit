"""Lemma-level contributions to the L2 - L5 and L1 - L5 differences (local Lexique copy; approximate)."""
import sys, json, collections
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import pandas as pd, numpy as np
import compute, analyze
LEX = '/usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt'
lex, _ = compute.load_lexicon(LEX)
REPO = '/home/claude/art5-harmos-audit'
meas = pd.read_csv(f'{REPO}/results/measures.csv')
texts = {}
for line in open(f'{REPO}/data/raw/calls_20261101T075547530698Z.jsonl', encoding='utf-8'):
    r = json.loads(line)
    if r.get('kind') == 'text':
        texts[r['call_id']] = r['text']
lem = {}
for r in meas.itertuples():
    if r.label not in ('L1', 'L1P', 'L2', 'L5'):
        continue
    title, lines = compute.clean(texts[r.call_id])
    m, lemmas = compute.measure(lines, lex)
    lem[r.call_id] = lemmas
zipf_of = {}
for o, (cat, lemma, lf, ff, nb) in lex.items():
    zipf_of[lemma] = compute.zipf(lf)
def z(l):
    return zipf_of.get(l, compute.zipf(0.0))
meas = meas[meas.call_id.isin(lem)]
def contrast_without(lab, drop):
    rows = []
    for r in meas.itertuples():
        ls = [l for l in lem[r.call_id] if l not in drop]
        rows.append((r.call_id, np.mean([z(l) for l in ls]) if ls else np.nan))
    d = meas.merge(pd.DataFrame(rows, columns=['call_id', 'zz']), on='call_id')
    d['kept'] = True
    ax = analyze.axes(d)
    cubes = analyze.to_cubes(d, 'zz', ax)
    x, _ = analyze.topic_stat(cubes[lab], cubes['L5'], 'level')
    return analyze.ttest(x)['estimate']
# lemma counts per label
cnt = {lab: collections.Counter() for lab in ('L1', 'L1P', 'L2', 'L5')}
ntok = {lab: 0 for lab in cnt}
for r in meas.itertuples():
    cnt[r.label].update(lem[r.call_id]); ntok[r.label] += len(lem[r.call_id])
rows = []
for l in set(cnt['L2']) | set(cnt['L5']):
    a, b = cnt['L2'][l] / ntok['L2'], cnt['L5'][l] / ntok['L5']
    rows.append((l, cnt['L2'][l], cnt['L5'][l], round(z(l), 2), (a - b) * 1e4))
df = pd.DataFrame(rows, columns=['lemma', 'n_L2', 'n_L5', 'zipf', 'diff_per10k'])
print('lemmas most over-represented in L2 vs L5 (per 10k content tokens):')
print(df.sort_values('diff_per10k', ascending=False).head(30).to_string(index=False))
swiss = {'romand', 'suisse', 'vaudois', 'genevois', 'valaisan', 'fribourgeois', 'neuchâtelois', 'jurassien',
         'helvétique', 'alpage', 'chalet', 'fondue', 'raclette', 'alpin', 'cantonal', 'canton', 'natel', 'léman',
         'bernois', 'romandie', 'vaudoise', 'lac', 'montagne', 'sapin', 'vache', 'fromage', 'marmotte', 'edelweiss',
         'skier', 'ski', 'sommet', 'vallée', 'glacier'}
base = contrast_without('L2', set())
print('L2-L5 level (local lexicon):', round(base, 4))
print('without Swiss/Alpine lemmas:', round(contrast_without('L2', swiss), 4))
top = set(df.sort_values('diff_per10k', ascending=False).head(30).lemma)
print('without the 30 lemmas most over-represented in L2:', round(contrast_without('L2', top), 4))
print('L1-L5 without the same 30:', round(contrast_without('L1', top), 4), ' (with all:', round(contrast_without('L1', set()), 4), ')')
