"""Independent recomputation of the supplement tables S1, S2, S4, S5, S6 and Table 2 from results/measures.csv, written
without importing analyze.py, then string-compared with the rendered tables of manuscript/build/supplement.md and
manuscript.md. Prints mismatches only (and a count of cells compared)."""
import re, sys
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

REPO = sys.argv[1]
df = pd.read_csv(f"{REPO}/results/measures.csv", keep_default_na=False, na_values=["", "nan", "NaN"])
AGE = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
GR = list(AGE)
MINUS = "−"

def fmt(x, d):
    s = f"{x:.{d}f}"
    if s.startswith("-") and float(s) == 0:
        s = s[1:]
    return s.replace("-", MINUS)

def pfmt(p, eq=True):
    if p < 0.001:
        return "< .001"
    s = f"{p:.3f}"
    s = s[1:] if s.startswith("0") else s
    return ("= " + s) if eq else s

def wide(d, label, Y):
    x = d[d.label == label].set_index(["model", "grade", "genre", "topic"])[Y]
    return x

def topic_vec(d, a, b, kind, Y="mean_zipf_content", grades=None, models=None):
    xa, xb = wide(d, a, Y), wide(d, b, Y)
    diff = (xa - xb).dropna().rename("d").reset_index()
    if grades is not None:
        diff = diff[diff.grade.isin(grades)]
    if models is not None:
        diff = diff[diff.model.isin(models)]
    g = diff.groupby(["topic", "grade"]).d.mean().unstack("grade")
    gs = [x for x in GR if x in g.columns]
    g = g[gs]
    ages = np.array([AGE[x] for x in gs])
    if kind == "level":
        return g.mean(axis=1).values
    c = ages - ages.mean()
    return g.values @ (c / (c ** 2).sum())

def tt(x):
    x = np.asarray(x, float); n = len(x)
    m, s = x.mean(), x.std(ddof=1); se = s / np.sqrt(n); t = m / se
    p = 2 * stats.t.sf(abs(t), n - 1); q = stats.t.ppf(.975, n - 1)
    return m, se, t, p, m - q * se, m + q * se

def holm(ps):
    ks = sorted(ps, key=lambda k: ps[k]); m = len(ks); adj = {}; run = 0
    for i, k in enumerate(ks):
        run = max(run, min(1, (m - i) * ps[k])); adj[k] = run
    return adj

sup = open(f"{REPO}/manuscript/build/supplement.md", encoding="utf-8").read()
man = open(f"{REPO}/manuscript/build/manuscript.md", encoding="utf-8").read()
bad = []; n_ok = 0

def need(text, s, where):
    global n_ok
    if s in text:
        n_ok += 1
    else:
        bad.append(f"{where}: expected '{s}' not found")

PRIM = [("h2H", "L1", "level", 3), ("h2P", "L1P", "level", 3), ("h3H", "L1", "gradient", 4), ("h3P", "L1P", "gradient", 4)]

# ---- Table 2 and its text
res = {k: tt(topic_vec(df, a, "L5", kind)) for k, a, kind, _ in PRIM}
adj = holm({k: v[3] for k, v in res.items()})
for k, a, kind, d in PRIM:
    m, se, t, p, lo, hi = res[k]
    need(man, f"{fmt(m, d)} [{fmt(lo, d)}, {fmt(hi, d)}]", f"Table 2 {k} estimate/CI")
    need(man, f"{fmt(t, 2)} | {pfmt(p, False)} | {pfmt(adj[k], False)}", f"Table 2 {k} t/p/Holm")

# ---- Table S1
def prim_p(d):
    r = {k: tt(topic_vec(d, a, "L5", kind)) for k, a, kind, _ in PRIM}
    return r
def row_str(r):
    return " | ".join(f"{fmt(r[k][0], dd)} (*p* {pfmt(r[k][3])})" for k, a, kind, dd in PRIM)
variants = {
    "Primary, topic-level": df,
    "Truncated texts removed": df[~df.truncated.astype(str).str.lower().isin(["true", "1"])],
    "Exact duplicates removed": df[~df.duplicate_text.astype(str).str.lower().isin(["true", "1"])],
    "Texts addressing the user removed": df[~df.flag_meta.astype(str).str.lower().isin(["true", "1"])],
}
for nm, d in variants.items():
    need(sup, row_str(prim_p(d)), f"S1 {nm}")
# length residualised within model (all kept texts)
d2 = df.copy(); d2["log_n"] = np.log(d2.n_words.astype(float))
fit = smf.ols("mean_zipf_content ~ C(model) + C(model):log_n", data=d2).fit()
d2["mean_zipf_content"] = fit.resid + d2["mean_zipf_content"].mean()
need(sup, row_str(prim_p(d2)), "S1 length residualised")

# ---- Table S2 secondary measures
SEC = [("Median Zipf, content lemmas", "median_zipf_content", (3, 1)), ("Content lemmas below Zipf 3 (percentage points)", "share_rare_content", (2, 100)),
       ("Content lemmas below Zipf 4 (percentage points)", "share_below4_content", (2, 100)), ("Mean word length (letters)", "mean_word_length", (3, 1)),
       ("Words per sentence", "words_per_sentence", (2, 1)), ("Number of words", "n_words", (1, 1)), ("Kandel–Moles readability", "kandel_moles", (2, 1)),
       ("Mean Zipf, word forms in films", "mean_zipf_form_films", (3, 1))]
for nm, col, (dd, sc) in SEC:
    cells = []
    for k, a, kind, _ in PRIM:
        m, se, t, p, lo, hi = tt(topic_vec(df, a, "L5", kind, Y=col))
        d_ = dd if kind == "level" else dd + 1
        cells.append(f"{fmt(sc * m, d_)} (*p* {pfmt(p)})")
    need(sup, f"| {nm} | " + " | ".join(cells) + " |", f"S2 {nm}")

# ---- Table S4 per model
names = {"anthropic_balanced": "Claude Sonnet 5.5", "anthropic_light": "Claude Haiku 5.5", "openai_balanced": "GPT-6.1 Sol",
         "openai_light": "GPT-6 Luna", "mistral_balanced": "Mistral Large 4", "mistral_light": "Mistral Small 4"}
for m_, nm in names.items():
    cells = []
    for k, a, kind, dd in PRIM:
        m, se, t, p, lo, hi = tt(topic_vec(df, a, "L5", kind, models=[m_]))
        cells.append(f"{fmt(m, dd)} [{fmt(lo, dd)}, {fmt(hi, dd)}]")
    need(sup, f"| {nm} | " + " | ".join(cells) + " |", f"S4 {nm}")

# ---- Table S5
def s5(a, b, kind, grades=None):
    m, se, t, p, lo, hi = tt(topic_vec(df, a, b, kind, grades=grades))
    dd = 3 if kind == "level" else 4
    return f"{fmt(m, dd)} [{fmt(lo, dd)}, {fmt(hi, dd)}] | {pfmt(p, False)}"
S5 = [("L3", "L5", "level"), ("L3", "L5", "gradient"), ("L3", "L1", "level"), ("L3", "L1", "gradient"), ("L2", "L5", "level"), ("L2", "L5", "gradient"),
      ("L4", "L5", "level"), ("L4", "L5", "gradient"), ("L1P", "L1", "level"), ("L1P", "L1", "gradient")]
for a, b, kind in S5:
    need(sup, s5(a, b, kind), f"S5 {a}-{b} {kind}")
need(sup, s5("L6", "L5", "level", grades=["3H", "4H", "5H"]), "S5 L6-L5 level 3H-5H")

# ---- Table S6
for g in GR:
    cells = []
    for a in ("L1", "L1P", "L3"):
        m, se, t, p, lo, hi = tt(topic_vec(df, a, "L5", "level", grades=[g]))
        cells.append(f"{fmt(m, 3)} [{fmt(lo, 3)}, {fmt(hi, 3)}]")
    need(sup, f"| {g} | " + " | ".join(cells) + " |", f"S6 {g}")

# ---- Table S1 OLS row (clustered), own implementation
d = df[df.label.isin(["L1", "L1P", "L5"])].copy()
d["mg"] = d.model + "_" + d.grade
d["age_c"] = d.grade.map(AGE) - np.mean(list(AGE.values()))
models = sorted(d.model.unique()); terms = []
for i, m in enumerate(models):
    for lab in ("L1", "L1P"):
        d[f"lev_{lab}_{i}"] = ((d.label == lab) & (d.model == m)).astype(float)
        d[f"grd_{lab}_{i}"] = d[f"lev_{lab}_{i}"] * d.age_c
        terms += [f"lev_{lab}_{i}", f"grd_{lab}_{i}"]
groups = pd.factorize(d.topic)[0]
r = smf.ols("mean_zipf_content ~ C(mg) + " + " + ".join(terms) + " + C(genre) + C(topic) - 1", data=d).fit(
    cov_type="cluster", cov_kwds={"groups": groups, "use_correction": True})
names_ = r.params.index.tolist(); cov = r.cov_params().to_numpy(); cells = []
for k, a, kind, dd in PRIM:
    c = np.zeros(len(names_))
    for i in range(len(models)):
        c[names_.index(f"{'lev' if kind == 'level' else 'grd'}_{a}_{i}")] = 1 / len(models)
    est = float(c @ r.params.to_numpy()); se = float(np.sqrt(c @ cov @ c)); t = est / se
    p = 2 * stats.t.sf(abs(t), 15)
    cells.append(f"{fmt(est, dd)} (*p* {pfmt(p)})")
need(sup, " | ".join(cells), "S1 OLS clustered row")
print("cells/rows matched:", n_ok, "mismatches:", len(bad))
for b in bad:
    print("  MISMATCH", b)
