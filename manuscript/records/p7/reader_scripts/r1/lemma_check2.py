import sys
sys.argv = ['x']
exec(open('/tmp/r1_review/lemma_check.py').read().split("# lemma counts per label")[0])
narrow = {'romand', 'suisse', 'grand-papa', 'grand-maman', 'vaudois', 'genevois', 'valaisan', 'fribourgeois',
          'neuchâtelois', 'jurassien', 'helvétique', 'romandie', 'natel', 'tresse', 'septante', 'nonante', 'huitante',
          'cantonal', 'canton', 'chalet', 'alpage', 'fondue', 'raclette'}
for lab in ('L2', 'L1', 'L1P'):
    print(lab, 'level vs L5: all lemmas', round(contrast_without(lab, set()), 4), '| without narrow Swiss-French set', round(contrast_without(lab, narrow), 4))
cnt = {}
for r in meas.itertuples():
    c = cnt.setdefault(r.label, {})
    for l in lem[r.call_id]:
        if l in narrow:
            c[l] = c.get(l, 0) + 1
for lab in ('L1', 'L1P', 'L2', 'L5'):
    print(lab, sorted(cnt.get(lab, {}).items(), key=lambda x: -x[1])[:12])
