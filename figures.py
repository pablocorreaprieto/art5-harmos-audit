"""Figures of the ART 5 manuscript, drawn from the frozen data (tag data-v1).

Reads results/measures.csv and results/numbers.json, writes results/figures/:
  fig1_rulers   each model's age-only ruler (mean Zipf of content lemmas by grade, 95% CI over topics)
  fig2_labels   model-internal age equivalents by label wording (shift and tracking, 95% bootstrap CI)
  fig3_models   shift and tracking of the bare H and P labels, model by model
as PDF (vector, for the journal) and PNG (300 dpi, for reading).
No number is computed here that the manuscript quotes; quoted numbers come from results/numbers.json
through manuscript_numbers.py. Requires matplotlib (requirements-figures.txt).
Written by the main session (claude-opus-5-5) on 1.11.2026, after the deposit; presentation only.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

OUT = "results/figures"
GRADES = ["3H", "4H", "5H", "6H", "7H", "8H"]
AGE_MID = dict(zip(GRADES, [6.5, 7.5, 8.5, 9.5, 10.5, 11.5]))
PROVIDERS = [("anthropic", "Anthropic"), ("openai", "OpenAI"), ("mistral", "Mistral")]
# Categorical slots 1 and 2 of the validated reference palette (light mode, ALL CHECKS PASS):
# identity of the model tier, with marker shape as the secondary encoding for print and CVD.
TIER = {"balanced": ("#2a78d6", "o"), "light": ("#eb6834", "s")}
INK, INK2, GRID = "#0b0b0b", "#52514e", "#d9d8d4"
LABEL_TEXT = {"L1": "de 5H (bare H label)", "L1P": "de 5P (bare P label)",
              "L2": "de 5H en Suisse romande", "L3": "de 5H (8 à 9 ans)", "L4": "de CE2 (French grade)"}


def style(ax):
    ax.spines[["top", "right"]].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK2)
        ax.spines[s].set_linewidth(0.8)
    ax.tick_params(colors=INK2, labelsize=8, width=0.8)
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def names():
    design = json.load(open("design.json"))
    return {k: v.split(" (")[0] for k, v in design["models"].items()}


def save(fig, stem):
    os.makedirs(OUT, exist_ok=True)
    # no creation date in the PDF, so that a rerun gives the same bytes (checked in P6)
    fig.savefig(f"{OUT}/{stem}.pdf", bbox_inches="tight", metadata={"CreationDate": None})
    fig.savefig(f"{OUT}/{stem}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def fig1(m, nm):
    l5 = m[(m["label"] == "L5")]
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.6), sharey=True)
    for ax, (prov, title) in zip(axes, PROVIDERS):
        for tier in ("balanced", "light"):
            key = f"{prov}_{tier}"
            sub = l5[l5["model"] == key]
            topic_means = sub.groupby(["grade", "topic"])["mean_zipf_content"].mean().reset_index()
            xs, ys, lo, hi = [], [], [], []
            for g in GRADES:
                v = topic_means.loc[topic_means["grade"] == g, "mean_zipf_content"].to_numpy(float)
                mean, se = v.mean(), v.std(ddof=1) / np.sqrt(len(v))
                q = stats.t.ppf(0.975, len(v) - 1)
                xs.append(AGE_MID[g]); ys.append(mean); lo.append(mean - q * se); hi.append(mean + q * se)
            color, marker = TIER[tier]
            ax.fill_between(xs, lo, hi, color=color, alpha=0.15, linewidth=0)
            ax.plot(xs, ys, color=color, linewidth=2, marker=marker, markersize=4, label=nm[key])
        ax.set_title(title, fontsize=9, color=INK, loc="left")
        ax.set_xticks([AGE_MID[g] for g in GRADES])
        ax.set_xticklabels([f"{int(AGE_MID[g] - 0.5)}–{int(AGE_MID[g] + 0.5)}" for g in GRADES], fontsize=7.5)
        style(ax)
        ax.legend(fontsize=7, frameon=False, loc="lower left")
    axes[0].set_ylabel("Mean Zipf of content lemmas\n(age-only texts)", fontsize=8, color=INK)
    fig.supxlabel("Age requested (years), the ages of grades 3H to 8H", fontsize=8, color=INK, y=-0.07)
    save(fig, "fig1_rulers")


def fig2(n):
    by = n["age_equivalent"]["by_label"]
    labs = ["L1", "L1P", "L2", "L3", "L4"]
    y = np.arange(len(labs))[::-1]
    color = TIER["balanced"][0]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.4), sharey=True)
    for ax, (field, ci, ref, xlabel) in zip(axes, [
            ("shift_years", "shift_ci95", [0], "Shift (years older than asked)"),
            ("tracking", "tracking_ci95", [0, 1], "Tracking (1 = follows the grade like the age)")]):
        for yi, lab in zip(y, labs):
            est, (a, b) = by[lab][field], by[lab][ci]
            ax.plot([a, b], [yi, yi], color=color, linewidth=2, solid_capstyle="round")
            ax.plot(est, yi, marker="o", color=color, markersize=6, markeredgecolor="white", markeredgewidth=1)
        for r in ref:
            ax.axvline(r, color=INK2, linewidth=0.8, linestyle="--" if r else "-")
        ax.set_xlabel(xlabel, fontsize=8, color=INK)
        style(ax)
        ax.grid(axis="x", color=GRID, linewidth=0.6)
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(y)
    axes[0].set_yticklabels([LABEL_TEXT[lab] for lab in labs], fontsize=8)
    save(fig, "fig2_labels")


def fig3(n, nm):
    by = n["age_equivalent"]["by_label"]
    order = ["anthropic_balanced", "anthropic_light", "openai_balanced", "openai_light",
             "mistral_balanced", "mistral_light"]
    y = np.arange(len(order))[::-1]
    series = [("L1", "de 5H", TIER["balanced"]), ("L1P", "de 5P", TIER["light"])]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), sharey=True)
    for ax, (field, ci, ref, xlabel) in zip(axes, [
            ("shift_years", "shift_ci95", [0], "Shift (years older than asked)"),
            ("tracking", "tracking_ci95", [0, 1], "Tracking (1 = follows the grade like the age)")]):
        for k, (lab, text, (color, marker)) in enumerate(series):
            off = 0.14 if k == 0 else -0.14
            for yi, model in zip(y, order):
                v = by[lab]["by_model"][model]
                a, b = v[ci]
                ax.plot([a, b], [yi + off, yi + off], color=color, linewidth=2, solid_capstyle="round")
                ax.plot(v[field], yi + off, marker=marker, color=color, markersize=5,
                        markeredgecolor="white", markeredgewidth=0.8, label=text if yi == y[0] else None)
        for r in ref:
            ax.axvline(r, color=INK2, linewidth=0.8, linestyle="--" if r else "-")
        ax.set_xlabel(xlabel, fontsize=8, color=INK)
        style(ax)
        ax.grid(axis="x", color=GRID, linewidth=0.6)
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(y)
    axes[0].set_yticklabels([nm[m] for m in order], fontsize=8)
    axes[1].legend(fontsize=7, frameon=False, loc="lower right")
    save(fig, "fig3_models")


def main():
    m = pd.read_csv("results/measures.csv", keep_default_na=False)
    m = m[m["kept"].astype(str).str.lower().isin(["true", "1"])].copy()
    m["mean_zipf_content"] = pd.to_numeric(m["mean_zipf_content"])
    n = json.load(open("results/numbers.json"))
    nm = names()
    fig1(m, nm)
    fig2(n)
    fig3(n, nm)
    print("wrote", sorted(os.listdir(OUT)))


if __name__ == "__main__":
    main()
