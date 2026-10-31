"""Mutation testing of compute.py v0.4.1: each mutation is applied to a copy, the self-test must fail."""
import os, shutil, subprocess, sys, tempfile
SRC = sys.argv[1]
LEX = next(p for p in ["/usr/local/lib/python3.13/site-packages/pylexique/Lexique383/Lexique383.txt",
                       "/usr/local/lib/python3.13/dist-packages/pylexique/Lexique383/Lexique383.txt"] if os.path.exists(p))
MUT = [
 # carried over from v0.3
 ("apostrophe not normalised", '.replace("’", "\'")', ''),
 ("ligature not folded", '.replace("œ", "oe")', ''),
 ("excluded lemmas emptied", 'EXCLUDED_LEMMAS = {"être", "avoir", "tout", "autre", "même"}', 'EXCLUDED_LEMMAS = set()'),
 ("adverbs counted", 'CONTENT = {"NOM", "ADJ", "VER"}', 'CONTENT = {"NOM", "ADJ", "VER", "ADV"}'),
 ("determiners counted", 'df["cat"] = df["cgram"].fillna("")  # full tag', 'df["cat"] = df["cgram"].fillna("").str.split(":").str[0]  # full tag'),
 ("most frequent row instead of lemma", 'df = df[df["lemme"] == df["top_lemme"]]', 'df = df'),
 ("form frequency instead of lemma", 'content.append(zipf(lemfreq))', 'content.append(zipf(formfilms))'),
 ("sentence-initial names kept", 'name = is_cap and (not initial or low not in lex or t in noninitial_caps)', 'name = is_cap and not initial'),
 ("no initial after quote or colon", 'initial = i == 0 or INITIAL_GAP_RE.search(s[prev_end:m.start()]) is not None', 'initial = i == 0'),
 ("elided particles not handled", 'if low in ELIDED:\n                rows.append((t, low, False))', 'if False:\n                rows.append((t, low, False))'),
 ("title kept when short", 'if marked or labelled or short:', 'if False:'),
 ("title rule ignores the final period", 'short = len(first.split()) <= 12 and not first.rstrip().endswith((".", "…"))', 'short = len(first.split()) <= 12'),
 ("preface lines kept", 'while len(items) > 1 and head < 2 and is_preface(items[0][0]):', 'while False and is_preface(items[0][0]):'),
 ("label lines kept", ' and not LABEL_LINE_RE.match(plain):', ':'),
 ("no clitic stripping", '        for c in CLITICS:\n            if low.endswith(c) and low[: -len(c)] in lex:\n                return [tok[: -len(c)]]\n', ''),
 ("hyphen split disabled", 'return [p for part in tok.split("-") if part for p in split_token(part, lex)]', 'return [tok]'),
 ("smoothing replaced by a floor", 'return math.log10(freq + SMOOTH) + 3', 'return math.log10(max(freq, 0.1)) + 3'),
 ("OOV threshold inverted", 'if m.get("share_oov", 0) > MAX_OOV:', 'if m.get("share_oov", 0) < MAX_OOV:'),
 ("refusal finish not detected", 'if rec.get("finish_reason") in REFUSAL_FINISH or is_refusal_text', 'if False or is_refusal_text'),
 ("textual refusal not detected", ' or is_refusal_text(rec.get("text", "")):', ':'),
 ("minimum length 40", 'MIN_WORDS = 20', 'MIN_WORDS = 40'),
 ("least frequent reading", 'df = df.sort_values(["formfreq", "cat"], ascending=[False, True], kind="mergesort")', 'df = df.sort_values(["formfreq", "cat"], ascending=[True, True], kind="mergesort")'),
 # new in v0.4
 ("tout, autre and même counted (D4)", 'EXCLUDED_LEMMAS = {"être", "avoir", "tout", "autre", "même"}', 'EXCLUDED_LEMMAS = {"être", "avoir"}'),
 ("lexicon keys not folded (D2)", 'df[c] = df[c].map(lambda v: normalise(v) if isinstance(v, str) else v)', 'df[c] = df[c]'),
 ("every line marked as a title (D3)", 'marked = l.startswith("#") or re.fullmatch(r"(\\*\\*|__).+(\\*\\*|__)", l) is not None', 'marked = True'),
 ("spaced hyphen not a dash (R1)", 'INITIAL_GAP_RE = re.compile(r"[:«\\"“—–]|(?:^|\\s)-(?:\\s|$)")', 'INITIAL_GAP_RE = re.compile("[:«\\"“—–]")'),
 ("closing lines kept (R2)", 'while len(items) > 1 and tail < 3 and POSTFACE_RE.match(items[-1][0]):', 'while False and POSTFACE_RE.match(items[-1][0]):'),
 ("preface needs a colon (R2)", 'return line.endswith(":") or PREFACE_RE.match(line) is not None or VOICI_META_RE.match(line) is not None or \\', 'return line.endswith(":") or False and \\'),
 ("refusal searched anywhere (D1)", 'if REFUSAL_RE.match(line):', 'if REFUSAL_RE.search(line):'),
 ("title-like first line tested (D1)", 'if i == 0 and title_like(line) and rest_words >= MIN_WORDS:\n            continue', 'if False:\n            continue'),
 ("title-like line skipped before a short body (D1)", 'if i == 0 and title_like(line) and rest_words >= MIN_WORDS:', 'if i == 0 and title_like(line):'),
 ("polite opener not stripped (D1)", 'm = OPENER_RE.match(line)', 'm = None'),
 ("only the first line tested (D1)", 'for i, (line, _) in enumerate(items[:2]):', 'for i, (line, _) in enumerate(items[:1]):'),
 ("meta flag ignores quotes", 'unquoted = QUOTED_RE.sub(" ", line)', 'unquoted = line'),
 ("meta flag never raised", 'LABEL_Q_RE.search(unquoted)):\n            return True', 'LABEL_Q_RE.search(unquoted)):\n            return False'),
 ("dialogue lines flagged", 'if line.startswith(DIALOGUE_START):\n            continue', 'if False:\n            continue'),
 # new in v0.4.1
 ("lines without letters kept (N3)", 'if plain and re.search(f"[{LETTERS}]", plain) and not LABEL_LINE_RE.match(plain):', 'if plain and not LABEL_LINE_RE.match(plain):'),
 ("Voici with a grade mention is a preface (N5)", 'AUDIENCE_RE = re.compile(r"\\b(pour (des|les|vos|tes|nos|de jeunes) (élèves|enfants|lecteurs)|adaptée?s?|destinée?s?|"\n                         r"au niveau|du niveau|de niveau)\\b", re.IGNORECASE)', 'AUDIENCE_RE = re.compile(r"\\b(élèves|degré|niveau|\\d+\\s*[HP]\\b|\\d+\\s*(à|-)\\s*\\d+\\s*ans|CE[12]\\b|CM[12]\\b|CP\\b|6e\\b)", re.IGNORECASE)'),
 ("Voici une histoire not a preface (v0.4.1)", ' or VOICI_META_RE.match(line) is not None or', ' or'),
 ("any note line removed (N5)", "\\(?\\s*(note|remarque|nb|n\\.b\\.).*\\b(texte|", "\\(?\\s*(note|remarque|nb|n\\.b\\.)\\b|(texte|"),
 ("word count kept (v0.4.1)", 'r"\\(?\\s*(environ |à peu près )?\\d+\\s*mots\\s*\\)?$|"', 'r""'),
 ("dites-moi kept (v0.4.1)", "dites-moi|dis-moi|si vous", "si vous"),
 ("malheureusement j\' excluded (N4)", "malheureusement[\\s,]*(je ne\\b|je n'|j'ignore|je suis dans l'impossibilité|il n'existe|il n'y a pas)", "malheureusement[\\s,]*(je\\b|j')"),
 ("tu form without me (N4)", "(pourrais|peux)-tu (me |m')(préciser|clarifier|indiquer|expliquer|confirmer|dire (ce que|ce qu'|à quel|quel|quelle))", "(pourrais|peux)-tu (me |m')?(préciser|clarifier|indiquer|expliquer|confirmer|dire)"),
 ("qu'entends-tu without par (N4)", "qu'entends-tu par", "qu'entends-tu"),
 ("navré not a refusal (N2)", "|je suis navrée?|navrée?", ""),
 ("tu requests not flagged (N2)", 'r"|\\b(pourrais|peux)-tu (me |m\')(préciser|clarifier|indiquer|expliquer|dire)\\b|\\bdis-moi\\b"', 'r""'),
 ("label question not flagged (N2)", ' or ("?" in unquoted and LABEL_Q_RE.search(unquoted))', ''),
 ("need-to-know not flagged (N2)", 'r"|\\bj\'(aurais|ai) besoin (de savoir|de connaître|d\'une précision|de précisions)\\b"', 'r""'),
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
    print(f"{n:40s} {r}")
print(sum(r.startswith("caught") for _, r in res), "of", len(res), "caught;",
      sum("not run" in r for _, r in res), "not run")
