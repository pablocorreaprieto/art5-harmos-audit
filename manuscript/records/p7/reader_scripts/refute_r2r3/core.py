"""Independent core for the refutation reading (does not import analyze.py).
Builds arrays Y[label][model, grade, genre, topic] from results/measures.csv (read only)."""
import numpy as np
import pandas as pd
from scipy import stats

REPO = "/home/claude/art5-harmos-audit"
AGE_MID = {"3H": 6.5, "4H": 7.5, "5H": 8.5, "6H": 9.5, "7H": 10.5, "8H": 11.5}
GRADES = list(AGE_MID)
AGES = np.array(list(AGE_MID.values()))
LABELS = ["L1", "L1P", "L2", "L3", "L4", "L5", "L6"]
NAMES = {"anthropic_balanced": "Sonnet", "anthropic_light": "Haiku", "openai_balanced": "Sol",
         "openai_light": "Luna", "mistral_balanced": "MLarge", "mistral_light": "MSmall"}


def load(y="mean_zipf_content", df=None):
    if df is None:
        df = pd.read_csv(f"{REPO}/results/measures.csv")
    df = df[df["kept"].astype(str).str.lower().isin(["true", "1"])]
    models = sorted(df["model"].unique())
    genres = sorted(df["genre"].unique())
    topics = sorted(df["topic"].unique())
    shape = (len(models), len(GRADES), len(genres), len(topics))
    Y = {lab: np.full(shape, np.nan) for lab in LABELS}
    d = df[df["label"].isin(LABELS)]
    for r in d.itertuples():
        Y[r.label][models.index(r.model), GRADES.index(r.grade), genres.index(r.genre), topics.index(r.topic)] = getattr(r, y)
    L0 = np.full((len(models), len(genres), len(topics)), np.nan)
    for r in df[df["label"] == "L0"].itertuples():
        L0[models.index(r.model), genres.index(r.genre), topics.index(r.topic)] = getattr(r, y)
    return Y, L0, models, genres, topics


def wlev(grades):
    return np.full(len(grades), 1 / len(grades))


def wgrad(grades):
    a = AGES[grades]
    c = a - a.mean()
    return c / np.sum(c ** 2)


def topic_stats(Y, a, b, kind, models=None, grades=None):
    grades = list(range(6)) if grades is None else grades
    d = (Y[a] - Y[b])[:, grades]
    if models is not None:
        d = d[models]
    dg = np.nanmean(d, axis=(0, 2))  # grades x topics
    w = wlev(grades) if kind == "level" else wgrad(grades)
    return w @ dg


def ttest(x, conf=0.95):
    x = np.asarray(x, float)
    T = len(x)
    m, se = x.mean(), x.std(ddof=1) / np.sqrt(T)
    t = m / se
    q = stats.t.ppf(0.5 + conf / 2, T - 1)
    return dict(est=m, se=se, t=t, p=2 * stats.t.sf(abs(t), T - 1), lo=m - q * se, hi=m + q * se, T=T)


def cell_means_w(Y, w=None):
    """label -> (models, grades) means over genres and topics, topics weighted by w (bootstrap)."""
    out = {}
    for lab, A in Y.items():
        if w is None:
            out[lab] = np.nanmean(A, axis=(2, 3))
        else:
            ok = np.isfinite(A)
            s = np.where(ok, A, 0.0).sum(axis=2) @ w
            c = ok.sum(axis=2) @ w
            out[lab] = s / c
    return out


def per_model_profile(means, lab, grades=None):
    """per model (level, gradient, slope b) of lab - L5 from cell means"""
    grades = list(range(6)) if grades is None else grades
    res = []
    for m in range(means["L5"].shape[0]):
        ruler = means["L5"][m]
        b = np.polyfit(AGES, ruler, 1)[0]
        d = means[lab][m, grades] - means["L5"][m, grades]
        lev = wlev(grades) @ d
        grd = wgrad(grades) @ d if len(grades) >= 3 else np.nan
        res.append((lev, grd, b))
    return np.array(res)


def pooled(prof, models=None):
    p = prof if models is None else prof[models]
    return p[:, 0].sum() / p[:, 2].sum(), 1 + p[:, 1].sum() / p[:, 2].sum()


def per_model_shift_track(prof):
    return prof[:, 0] / prof[:, 2], 1 + prof[:, 1] / prof[:, 2]
