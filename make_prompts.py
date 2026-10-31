"""Build every generation and probe call of ART 5 from design.json (design v0.4).

python make_prompts.py            -> calls.jsonl        (main study, n_topics from design.json)
python make_prompts.py --pilot    -> calls_pilot.jsonl  (pilot blocks of design.json)

One text per prompt (no replicates). L0 has no grade (grade field "nograde") and is written
once per model, genre and topic; L6 exists only for 3H to 5H. Calls are shuffled with order_seed.
The script prints the counts and exits non-zero when they differ from the design arithmetic, when
the design asks for more topics than it lists, or when a text prompt repeats for one model.
"""
import itertools
import json
import random
import sys

design = json.load(open("design.json", encoding="utf-8"))
GRADES = list(design["grades"])


def label_grades(lab, grades):
    spec = design["labels"][lab]["grades"]
    if spec == "none":
        return ["nograde"]
    allowed = GRADES if spec == "all" else spec
    return [g for g in grades if g in allowed]


def label_text(lab, grade):
    if grade == "nograde":
        return design["labels"][lab]["text"]
    return design["labels"][lab]["text"].format(**design["grades"][grade])


def text_calls(models, labels, grades, genres, topics, block):
    out = []
    for m, lab, ge, t in itertools.product(models, labels, genres, topics):
        for g in label_grades(lab, grades):
            prompt = design["prompt_template"].format(genre=design["genres"][ge], label=label_text(lab, g), topic=t)
            out.append({"kind": "text", "block": block, "model": m, "grade": g, "label": lab, "genre": ge,
                        "topic": t, "prompt": prompt})
    return out


def probe_calls(models, templates, notations, reps):
    out = []
    for m, g, nota, pk, r in itertools.product(models, GRADES, notations, templates, range(reps)):
        info = design["grades"][g]
        grade_label = f"{info['n']}{nota}"
        out.append({"kind": "probe", "block": "probe", "model": m, "grade": g, "notation": nota, "probe": pk,
                    "rep": r, "truth_age_from": info["age_from"], "truth_age_to": info["age_to"],
                    "prompt": design["probe_templates"][pk].format(grade=grade_label)})
    return out


def expected_texts(models, labels, grades, genres, topics):
    return len(models) * len(genres) * len(topics) * sum(len(label_grades(l, grades)) for l in labels)


def main():
    pilot = "--pilot" in sys.argv
    calls, expected = [], {}
    if pilot:
        p = design["pilot"]
        for block in [b for b in p if b != "probe"]:
            b = p[block]
            grades = GRADES if b["grades"] == "all" else b["grades"]
            calls += text_calls(b["models"], b["labels"], grades, b["genres"], b["topics"], block)
            expected[block] = expected_texts(b["models"], b["labels"], grades, b["genres"], b["topics"])
        pr = p["probe"]
        calls += probe_calls(pr["models"], pr["templates"], pr["notations"], pr["repetitions"])
        expected["probe"] = len(pr["models"]) * len(GRADES) * len(pr["notations"]) * len(pr["templates"]) * pr["repetitions"]
        prefix, path = "pilot", "calls_pilot.jsonl"
    else:
        if design["n_topics"] > len(design["topics"]):
            print(f"FAIL: n_topics = {design['n_topics']} but only {len(design['topics'])} topics are listed")
            sys.exit(1)
        topics = design["topics"][: design["n_topics"]]
        models, labels, genres = list(design["models"]), list(design["labels"]), list(design["genres"])
        calls += text_calls(models, labels, GRADES, genres, topics, "main")
        expected["main"] = expected_texts(models, labels, GRADES, genres, topics)
        calls += probe_calls(models, list(design["probe_templates"]), design["probe_notations"], design["probe_repetitions"])
        expected["probe"] = len(models) * len(GRADES) * len(design["probe_notations"]) * len(design["probe_templates"]) * design["probe_repetitions"]
        prefix, path = "main", "calls.jsonl"

    random.Random(design["order_seed"]).shuffle(calls)
    for i, c in enumerate(calls):
        c["call_id"] = f"{prefix}-{i:05d}"
    got = {}
    for c in calls:
        got[c["block"]] = got.get(c["block"], 0) + 1
    text_keys = [c["prompt"] + "|" + c["model"] for c in calls if c["kind"] == "text"]
    print(json.dumps({"file": path, "counts": got, "expected": expected, "total": len(calls)}, ensure_ascii=False))
    with open(path, "w", encoding="utf-8") as f:
        for c in calls:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    if got != expected:
        print("FAIL: call counts differ from the design")
        sys.exit(1)
    if len(set(text_keys)) != len(text_keys):
        print("FAIL: the same text prompt appears twice for one model")
        sys.exit(1)
    for lab in sorted({c["label"] for c in calls if c["kind"] == "text"}):
        print(lab, next(c["prompt"] for c in calls if c.get("label") == lab))
    print(next(c["prompt"] for c in calls if c["kind"] == "probe"))


if __name__ == "__main__":
    main()
