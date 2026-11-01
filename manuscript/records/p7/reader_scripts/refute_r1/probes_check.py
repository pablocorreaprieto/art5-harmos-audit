import sys, json, re
import numpy as np, pandas as pd
sys.path.insert(0, '/home/claude/art5-harmos-audit')
import analyze
p = pd.read_csv('/home/claude/art5-harmos-audit/results/probes.csv', keep_default_na=False, na_values=['', 'nan', 'NaN'])
rows=[]
for r in p.itertuples():
    found = analyze.parse_probe(r.text) if str(r.ok).lower() in ('true','1') else []
    first = found[0] if found else None
    mid = (first[0]+first[1])/2 if first else np.nan
    truth_mid = (r.truth_age_from + r.truth_age_to)/2
    rows.append(dict(model=r.model, notation=r.notation, grade=r.grade, probe=r.probe, text=r.text, parsed=first is not None,
                     first=first, mid=mid, err=mid-truth_mid,
                     correct_first=bool(first and analyze.probe_correct(*first, r.truth_age_from, r.truth_age_to)),
                     correct_any=any(analyze.probe_correct(lo,hi,r.truth_age_from,r.truth_age_to) for lo,hi in found),
                     truth=(r.truth_age_from, r.truth_age_to)))
d = pd.DataFrame(rows)
print("n", len(d), "parsed", d.parsed.sum(), "correct_first", d.correct_first.sum(), "wrong (parsed & not correct)", (d.parsed & ~d.correct_first).sum())
wrong = d[d.parsed & ~d.correct_first]
print("wrong that also state a correct range:", wrong.correct_any.sum(), "of", len(wrong))
print("wrong with 1.5<=err<=2.5:", ((wrong.err>=1.5)&(wrong.err<=2.5)).sum(), "share", round(((wrong.err>=1.5)&(wrong.err<=2.5)).mean(),3))
correct = d[d.correct_first]
# boundary cases: |err| == 1.0 exactly (range one full year off, midpoint at the widened edge)
b = correct[correct.err.abs() >= 1.0]
print("correct first answers with |err|>=1.0:", len(b), "of", len(correct), "; by model:", b.groupby('model').size().to_dict())
print("share of Mistral Small 4 correct answers that are boundary:", round(len(b[b.model=='mistral_light'])/len(correct[correct.model=='mistral_light']),3))
# Sonnet P errors
s = d[(d.model=='anthropic_balanced')&(d.notation=='P')&d.parsed&~d.correct_first]
for r in s.itertuples(): print("SONNET P ERROR:", r.grade, r.first, r.truth, "|", r.text[:300].replace('\n',' '))
# too young errors
ty = wrong[wrong.err < 0]
print("too-young wrong answers:", len(ty), ty.groupby('model').size().to_dict())
for r in ty.itertuples(): print("  TOO YOUNG:", r.model, r.notation, r.grade, r.first, r.truth, "|", r.text[:160].replace('\n',' '))
# Haiku large errors
h = wrong[(wrong.model=='anthropic_light')]
print("Haiku wrong n:", len(h), "err>=6:", (h.err>=6).sum(), "err distribution:", h.err.round(1).value_counts().sort_index().to_dict())
for r in h[h.err>=6].itertuples(): print("  HAIKU BIG:", r.notation, r.grade, r.first, r.truth, "|", r.text[:200].replace('\n',' '))
# mention of France/Belgique among the 1.5-2.5 errors
two = wrong[(wrong.err>=1.5)&(wrong.err<=2.5)]
print("two-year errors:", len(two), "mention France:", two.text.str.contains('France|français', case=False).mean().round(3), "mention Belgi:", two.text.str.contains('Belgi', case=False).mean().round(3), "mention CM2:", two.text.str.contains('CM2').mean().round(3), "mention HarmoS:", two.text.str.contains('HarmoS|Harmos|harmos').mean().round(3))
# pre-HarmoS mentions
pre = d[d.text.str.contains('avant HarmoS|ancien système|ancienne numérotation|pré-HarmoS|avant l.harmonisation|ancienne', case=False)]
print("answers mentioning old/pre-HarmoS numbering:", len(pre), pre.groupby(['model']).size().to_dict())
for r in pre.head(6).itertuples(): print("  PRE:", r.model, r.notation, r.grade, r.first, r.truth, "|", re.sub(r'\s+',' ', r.text)[:400])
d.to_csv('/tmp/refute_r1/probes_parsed.csv', index=False)
