"""Mutation testing of compute.py: each mutation is applied to a copy, the self-test must fail."""
import os, shutil, subprocess, sys, tempfile
SRC = "/home/claude/art5/compute.py"
LEX = "/usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt"
MUT = [
 ("typographic apostrophe not normalised", 'text = (text or "").replace("’", "\'").replace("‘", "\'")', 'text = (text or "")'),
 ("être and avoir counted", 'EXCLUDED_LEMMAS = {"être", "avoir"}', 'EXCLUDED_LEMMAS = set()'),
 ("adverbs counted as content", 'CONTENT = {"NOM", "ADJ", "VER"}', 'CONTENT = {"NOM", "ADJ", "VER", "ADV"}'),
 ("form frequency instead of lemma", 'content.append(zipf(lemfreq))', 'content.append(zipf(formfilms))'),
 ("sentence-initial names kept", 'name = is_cap and (not initial or low not in lex or t in noninitial_caps)', 'name = is_cap and not initial'),
 ("elided particles not handled", 'if low in ELIDED:\n                rows.append((t, low, False))', 'if False:\n                rows.append((t, low, False))'),
 ("no title removal", 'if len(lines) > 1 and len(lines[0].split()) <= 12:', 'if False:'),
 ("no clitic stripping", '        for c in CLITICS:\n            if low.endswith(c) and low[: -len(c)] in lex:\n                return [tok[: -len(c)]]\n', ''),
 ("hyphen split disabled", 'return [p for part in tok.split("-") if part for p in split_token(part, lex)]', 'return [tok]'),
 ("smoothing removed (floor)", 'return math.log10(freq + SMOOTH) + 3', 'return math.log10(max(freq, 0.1)) + 3'),
 ("OOV threshold inverted", 'if m.get("share_oov", 0) > MAX_OOV:', 'if m.get("share_oov", 0) < MAX_OOV:'),
 ("refusal not detected", 'if rec.get("finish_reason") in REFUSAL_FINISH:', 'if False:'),
 ("minimum length 40", 'MIN_WORDS = 20', 'MIN_WORDS = 40'),
 ("most frequent reading not chosen", 'df = df.sort_values("formfreq", ascending=False)', 'df = df.sort_values("formfreq", ascending=True)'),
]
src = open(SRC, encoding="utf-8").read()
res = []
for name, old, new in MUT:
    n = src.count(old)
    if n != 1:
        res.append((name, f"pattern found {n} times, not run")); continue
    d = tempfile.mkdtemp()
    open(os.path.join(d, "compute.py"), "w", encoding="utf-8").write(src.replace(old, new))
    p = subprocess.run([sys.executable, "compute.py", "--self-test", LEX], cwd=d, capture_output=True, text=True, timeout=600)
    first = next((l for l in (p.stdout + p.stderr).splitlines() if l.startswith("FAIL") or "Error" in l), "")
    res.append((name, ("caught: " + first[:120]) if p.returncode != 0 else "NOT caught"))
    shutil.rmtree(d)
for n, r in res:
    print(f"{n:38s} {r}")
print(sum(r.startswith("caught") for _, r in res), "of", len(res), "caught")
