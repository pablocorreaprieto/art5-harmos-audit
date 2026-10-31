"""Mutation testing of compute.py v0.3: each mutation is applied to a copy, the self-test must fail."""
import os, shutil, subprocess, sys, tempfile
SRC = sys.argv[1]
LEX = "/usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt"
MUT = [
 ("apostrophe not normalised", '.replace("’", "\'")', ''),
 ("ligature not folded", '.replace("œ", "oe")', ''),
 ("être and avoir counted", 'EXCLUDED_LEMMAS = {"être", "avoir"}', 'EXCLUDED_LEMMAS = set()'),
 ("adverbs counted", 'CONTENT = {"NOM", "ADJ", "VER"}', 'CONTENT = {"NOM", "ADJ", "VER", "ADV"}'),
 ("determiners counted", 'df["cat"] = df["cgram"].fillna("")  # full tag', 'df["cat"] = df["cgram"].fillna("").str.split(":").str[0]  # full tag'),
 ("most frequent row instead of lemma", 'df = df[df["lemme"] == df["top_lemme"]]', 'df = df'),
 ("form frequency instead of lemma", 'content.append(zipf(lemfreq))', 'content.append(zipf(formfilms))'),
 ("sentence-initial names kept", 'name = is_cap and (not initial or low not in lex or t in noninitial_caps)', 'name = is_cap and not initial'),
 ("no initial after quote or colon", 'initial = i == 0 or INITIAL_GAP_RE.search(s[prev_end:m.start()]) is not None', 'initial = i == 0'),
 ("elided particles not handled", 'if low in ELIDED:\n                rows.append((t, low, False))', 'if False:\n                rows.append((t, low, False))'),
 ("title kept when short", 'if marked or labelled or short:', 'if False:'),
 ("title rule ignores the final period", 'short = len(first.split()) <= 12 and not first.rstrip().endswith((".", "…"))', 'short = len(first.split()) <= 12'),
 ("preface line kept", '    while len(lines) > 1 and lines[0].endswith(":"):  # preface', '    while False and lines[0].endswith(":"):  # preface'),
 ("label lines kept", 'lines = [l for l in lines if l and not LABEL_LINE_RE.match(l)]', 'lines = [l for l in lines if l]'),
 ("no clitic stripping", '        for c in CLITICS:\n            if low.endswith(c) and low[: -len(c)] in lex:\n                return [tok[: -len(c)]]\n', ''),
 ("hyphen split disabled", 'return [p for part in tok.split("-") if part for p in split_token(part, lex)]', 'return [tok]'),
 ("smoothing replaced by a floor", 'return math.log10(freq + SMOOTH) + 3', 'return math.log10(max(freq, 0.1)) + 3'),
 ("OOV threshold inverted", 'if m.get("share_oov", 0) > MAX_OOV:', 'if m.get("share_oov", 0) < MAX_OOV:'),
 ("refusal finish not detected", 'if rec.get("finish_reason") in REFUSAL_FINISH or REFUSAL_RE', 'if False or REFUSAL_RE'),
 ("clarification not detected", ' or REFUSAL_RE.match(re.sub(r"[#*_]+", " ", normalise(rec.get("text", ""))).strip()):', ':'),
 ("minimum length 40", 'MIN_WORDS = 20', 'MIN_WORDS = 40'),
 ("least frequent reading", 'df = df.sort_values(["formfreq", "cat"], ascending=[False, True], kind="mergesort")', 'df = df.sort_values(["formfreq", "cat"], ascending=[True, True], kind="mergesort")'),
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
    res.append((name, ("caught: " + first[:110]) if p.returncode != 0 else "NOT caught"))
    shutil.rmtree(d)
for n, r in res:
    print(f"{n:38s} {r}")
print(sum(r.startswith("caught") for _, r in res), "of", len(res), "caught")
