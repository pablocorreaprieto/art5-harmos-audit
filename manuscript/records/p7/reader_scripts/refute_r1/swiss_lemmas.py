"""Approximate re-measurement with the pylexique Latin-1 copy: Swiss-French lemmas in L2 vs L5, and sensitivity of L2-L5 and L1-L5."""
import sys, json, collections
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import pandas as pd, numpy as np
import compute, analyze
LEX = '/usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt'
lex, sha = compute.load_lexicon(LEX)
print("local lexicon sha16", sha[:16])
for w in ['tandis', 'romand', 'suisse', 'grand-papa', 'tresse', 'canton', 'grand-maman', 'septante', 'tchou', 'h']:
    print(w, '->', lex.get(w))
REPO = '/home/claude/art5-harmos-audit'
meas = pd.read_csv(f'{REPO}/results/measures.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
texts = {}
for f in [f'{REPO}/data/raw/calls_20261101T075547530698Z.jsonl', f'{REPO}/data/raw/calls_20261101T101404154113Z.jsonl']:
    for line in open(f, encoding='utf-8'):
        r = json.loads(line)
        if r.get('kind') == 'text': texts[r['call_id']] = r['text']
lem, zloc = {}, {}
for r in meas.itertuples():
    title, lines = compute.clean(texts[r.call_id])
    m, lemmas = compute.measure(lines, lex)
    lem[r.call_id] = lemmas; zloc[r.call_id] = m['mean_zipf_content']
meas['z_local'] = meas.call_id.map(zloc)
print("share of texts where local == frozen:", round((abs(meas.z_local - meas.mean_zipf_content) < 1e-9).mean(), 3), "max abs diff", round(abs(meas.z_local - meas.mean_zipf_content).max(), 3), "n differing:", int((abs(meas.z_local - meas.mean_zipf_content) >= 1e-9).sum()))
zipf_of = {}
for o, (cat, lemma, lf, ff, nb) in lex.items(): zipf_of[lemma] = compute.zipf(lf)
def z(l): return zipf_of.get(l, compute.zipf(0.0))
def level(lab, drop, col=None):
    rows = []
    for r in meas.itertuples():
        ls = [l for l in lem[r.call_id] if l not in drop]
        rows.append((r.call_id, np.mean([z(l) for l in ls]) if ls else np.nan))
    d = meas.merge(pd.DataFrame(rows, columns=['call_id','zz']), on='call_id'); d['kept'] = True
    ax = analyze.axes(d); cubes = analyze.to_cubes(d, 'zz', ax)
    x,_ = analyze.topic_stat(cubes[lab], cubes['L5'], 'level'); t = analyze.ttest(x)
    return t['estimate'], t['p_two_sided']
cnt = {lab: collections.Counter() for lab in ['L1','L1P','L2','L3','L5']}
for r in meas.itertuples():
    if r.label in cnt: cnt[r.label].update(lem[r.call_id])
for w in ['romand','grand-papa','suisse','tresse','canton','grand-maman','chalet','alpage','vaudois','genevois']:
    print(f"{w}: L2 {cnt['L2'][w]}, L5 {cnt['L5'][w]}, L1 {cnt['L1'][w]}, zipf {z(w):.2f}")
narrow = {'romand','suisse','grand-papa','grand-maman','vaudois','genevois','valaisan','fribourgeois','neuchâtelois','jurassien','helvétique','romandie','natel','tresse','septante','nonante','huitante','cantonal','canton','chalet','alpage','fondue','raclette'}
n = json.load(open(f'{REPO}/results/numbers.json'))
print("frozen L2-L5 level:", round(n['exploratory']['other_labels']['L2_level']['estimate'],4), " frozen L1-L5:", round(n['primary']['h2_level_H']['estimate'],4))
for lab in ['L2','L1','L1P']:
    a = level(lab, set()); b = level(lab, narrow)
    print(f"{lab}-L5 local: all lemmas {a[0]:.4f} (p={a[1]:.3g}) | without narrow Swiss set {b[0]:.4f} (p={b[1]:.3g})")
slope_sum = np.mean([v['slope'] for v in n['h1'].values()])
print("in years at mean slope: L2 all", round(level('L2', set())[0]/slope_sum,2), "without", round(level('L2', narrow)[0]/slope_sum,2))
# OOV content tokens
oov = collections.Counter()
for r in meas.itertuples():
    for l in lem[r.call_id]:
        if l not in zipf_of: oov[l] += 1
print("OOV content tokens total:", sum(oov.values()), "top 30:", oov.most_common(30))
def level_no_oov(lab):
    rows = []
    for r in meas.itertuples():
        ls = [l for l in lem[r.call_id] if l in zipf_of]
        rows.append((r.call_id, np.mean([z(l) for l in ls]) if ls else np.nan))
    d = meas.merge(pd.DataFrame(rows, columns=['call_id','zz']), on='call_id'); d['kept'] = True
    ax = analyze.axes(d); cubes = analyze.to_cubes(d, 'zz', ax)
    x,_ = analyze.topic_stat(cubes[lab], cubes['L5'], 'level'); return analyze.ttest(x)['estimate']
print("without OOV tokens: L1-L5", round(level_no_oov('L1'),4), "L1P-L5", round(level_no_oov('L1P'),4), "L2-L5", round(level_no_oov('L2'),4))
