"""Entry point of the GitHub Actions workflow of ART 5 (design v0.4.1).

python pipeline.py --step STEP --max-cost USD [--max-minutes M]
STEP: lexicon | list-models | validate | pilot | generate | compute | analyze
--max-cost is the budget of a whole plan (the pilot, or the main study), counted over every pass
and every earlier run: money already spent on that plan, summed over the raw records of its calls
(cost reported by the provider plus the worst case of attempts that may have been billed), is
subtracted before each pass, and a pass is skipped once the budget is used. Raw lines are written
as each call ends, so a run that crashed is counted too.

validate  known-groups check of the measure (Vikidia against Wikipedia, validate_measure.py)
pilot     252 pilot calls (216 age-only texts, 36 probes), then results/pilot_summary.json with the
          residual SD and the ruler slope of the 216 texts, the flat-ruler stop rule, the number of
          topics chosen by simulation, format and exclusion counts, and the probe parse rate (probe
          accuracy is not computed before the deposit).
generate  builds the main plan from design.json (n_topics as set at G1) and runs it.
compute   results/measures.csv and results/probes.csv from every raw file of the main study.
analyze   results/numbers.json (analyze.py).
Every call that fails or returns nothing is requested again once in the same step, then every text
that is refused, too short or not French once more (compute.retry_list). Every step writes its logs in
logs/, and nothing in data/raw is ever edited.
"""
import argparse
import glob
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.request

LEXIQUE_URL = "http://www.lexique.org/databases/Lexique383/Lexique383.tsv"
LEXIQUE_PATH = "data/lexicon/Lexique383.tsv"
POWER_TARGET = 0.80  # protocol v1.0, phase P1
TOPIC_OPTIONS = (16, 24, 32)
PLANNING_SLOPE = -0.04  # one year on the planning ruler = 0.04 Zipf, the smallest effect of interest
START = time.time()


def sh(*args):
    print("+", " ".join(args), flush=True)
    subprocess.run([sys.executable, *args], check=True)


def lexicon():
    os.makedirs("data/lexicon", exist_ok=True)
    if not os.path.exists(LEXIQUE_PATH):
        urllib.request.urlretrieve(LEXIQUE_URL, LEXIQUE_PATH)
    sha = hashlib.sha256(open(LEXIQUE_PATH, "rb").read()).hexdigest()
    os.makedirs("logs", exist_ok=True)
    json.dump({"url": LEXIQUE_URL, "sha256": sha, "licence": "CC BY-SA 4.0"}, open("logs/lexicon.json", "w"), indent=1)
    print("lexicon", sha)


def need_models():
    if not os.path.exists("models.json"):
        raise SystemExit("models.json is missing: run list-models, then commit models.json with the exact dated ids and prices")


def minutes_left(budget):
    return max(budget - (time.time() - START) / 60, 0.0)


def last_run():
    logs = sorted(f for f in os.listdir("logs") if f.startswith("run_"))
    return json.load(open(os.path.join("logs", logs[-1]))) if logs else {}


def plan_prefix(calls):
    """Call ids of a plan share a prefix (pilot- or main-); retries add -r1."""
    with open(calls, encoding="utf-8") as f:
        return json.loads(f.readline())["call_id"].split("-")[0] + "-"


def spent_on(prefix):
    """Money already spent on a plan, summed over every raw record of its calls."""
    total = 0.0
    for f in glob.glob("data/raw/*.jsonl"):
        for line in open(f, encoding="utf-8"):
            r = json.loads(line)
            if str(r.get("call_id", "")).startswith(prefix):
                total += float(r.get("cost_usd", 0.0)) + float(r.get("cost_usd_possibly_charged", 0.0))
    return total


def run_calls(calls, cap, minutes):
    retry = calls.replace(".jsonl", "_retry.jsonl")
    prefix = plan_prefix(calls)

    def one_pass(path):
        left = cap - spent_on(prefix)
        if left <= 0:
            print(f"budget of {cap} USD for this plan used, {path} not run", flush=True)
            return {"stopped": f"plan budget of {cap} USD used"}
        try:
            sh("generate.py", "run", path, "models.json", f"{left:.4f}", "--max-minutes", str(minutes_left(minutes)))
        except subprocess.CalledProcessError as e:  # counted from the raw records, then stop the step
            print(f"generate.py stopped with an error ({e.returncode}), spent so far {spent_on(prefix):.4f} USD", flush=True)
            raise
        return last_run()

    first = one_pass(calls)
    if first.get("failed") and not first.get("stopped"):  # transport failures and empty answers, once
        one_pass(calls)
    import compute
    if compute.retry_list(LEXIQUE_PATH, "data/raw/*.jsonl", calls, retry):
        one_pass(retry)
    print(json.dumps({"plan": prefix, "cap_usd": cap, "spent_usd_total": round(spent_on(prefix), 4)}), flush=True)


def pilot_summary():
    import numpy as np
    import pandas as pd
    import statsmodels.formula.api as smf
    from scipy import stats

    import analyze
    import sim_power

    df = pd.read_csv("results/pilot_measures.csv", keep_default_na=False, na_values=["", "nan", "NaN"])
    df["kept"] = analyze.as_bool(df["kept"])
    out = {"note": "pilot only, excluded from every confirmatory analysis"}
    ruler = df[(df["block"] == "ruler") & df["kept"]].copy()
    ruler["age"] = ruler["grade"].map(analyze.AGE_MID)
    cells = smf.ols("mean_zipf_content ~ C(model):C(grade) + C(genre) + C(topic)", data=ruler).fit()
    sigma, dfr = float(np.sqrt(cells.scale)), float(cells.df_resid)
    sigma_upper80 = sigma * float(np.sqrt(dfr / stats.chi2.ppf(0.20, dfr)))
    pooled = smf.ols("mean_zipf_content ~ age + C(model) + C(genre) + C(topic)", data=ruler).fit(cov_type="HC3")
    slope, slope_se = float(pooled.params["age"]), float(pooled.bse["age"])
    p_slope = float(stats.norm.cdf(slope / slope_se))  # one-sided, slope below zero
    per_model = {m: float(smf.ols("mean_zipf_content ~ age + C(genre) + C(topic)", data=g).fit().params["age"])
                 for m, g in ruler.groupby("model")}
    out["ruler"] = {"n_kept": int(len(ruler)), "n_planned": int((df["block"] == "ruler").sum()), "sigma": sigma,
                    "sigma_df": dfr, "sigma_upper80": sigma_upper80, "pooled_slope": slope, "pooled_slope_se": slope_se,
                    "pooled_slope_p_one_sided": p_slope, "per_model_slope": per_model,
                    "one_year_in_zipf_at_pilot_slope": -slope}
    out["stop_flat_ruler"] = bool(p_slope > 0.05)
    power = sim_power.pilot_power(sigma_upper80, PLANNING_SLOPE)
    out["power_level_test_0_04_zipf"] = {str(k): v for k, v in power.items()}
    chosen = next((T for T in TOPIC_OPTIONS if power[T] >= POWER_TARGET), None)
    out["n_topics_rule"] = chosen if chosen else f"no option reaches {POWER_TARGET}, decision at G1"
    out["texts"] = {"n": int(len(df)), "kept": int(df["kept"].sum()),
                    "exclusion_reasons": df.loc[~df["kept"], "exclusion_reason"].value_counts().to_dict(),
                    "finish_reasons": df["finish_reason"].value_counts(dropna=False).to_dict(),
                    "truncated": int(analyze.as_bool(df["truncated"]).sum())}
    allp = pd.read_csv("results/pilot_probes.csv", keep_default_na=False)
    parsed = [analyze.parse_probe(t) for t in allp["text"]]
    out["probes"] = {"n": int(len(allp)), "ok": int(analyze.as_bool(allp["ok"]).sum()),
                     "share_parsed": float(np.mean([bool(p) for p in parsed])) if len(parsed) else None,
                     "share_multiple": float(np.mean([len(set(p)) > 1 for p in parsed])) if len(parsed) else None,
                     "accuracy": "not computed before the deposit"}
    json.dump(out, open("results/pilot_summary.json", "w"), indent=1, default=float)
    print(json.dumps(out, indent=1, default=float))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", required=True)
    ap.add_argument("--max-cost", type=float, default=10.0)
    ap.add_argument("--max-minutes", type=float, default=320.0)
    a = ap.parse_args()
    os.makedirs("results", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    if a.step == "lexicon":
        lexicon()
    elif a.step == "list-models":
        sh("generate.py", "list-models")
    elif a.step == "validate":
        lexicon()
        sh("validate_measure.py", LEXIQUE_PATH, "results/validation_vikidia.json")
    elif a.step == "pilot":
        need_models()
        lexicon()
        sh("compute.py", "--self-test", LEXIQUE_PATH)
        sh("make_prompts.py", "--pilot")
        run_calls("calls_pilot.jsonl", a.max_cost, a.max_minutes)
        import compute
        compute.compute(LEXIQUE_PATH, "data/raw/*.jsonl", "results/pilot_measures.csv", prefix="pilot-")
        compute.probes("data/raw/*.jsonl", "results/pilot_probes.csv", prefix="pilot-")
        pilot_summary()
    elif a.step == "generate":
        need_models()
        lexicon()
        sh("make_prompts.py")
        run_calls("calls.jsonl", a.max_cost, a.max_minutes)
    elif a.step == "compute":
        lexicon()
        sh("compute.py", "--self-test", LEXIQUE_PATH)
        import compute
        compute.compute(LEXIQUE_PATH, "data/raw/*.jsonl", "results/measures.csv", prefix="main-")
        compute.probes("data/raw/*.jsonl", "results/probes.csv", prefix="main-")
    elif a.step == "analyze":
        sh("analyze.py", "--self-test")
        sh("analyze.py", "results/measures.csv", "results/probes.csv", "results/numbers.json")
    else:
        raise SystemExit(f"unknown step {a.step}")


if __name__ == "__main__":
    main()
