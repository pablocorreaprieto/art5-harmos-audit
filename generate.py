"""Model calls for ART 5 (design v0.4.6), run inside GitHub Actions only (keys come from repository secrets).

Secrets (v0.4.6): before any request, each key must be one line of printable characters. A
secret that is empty or holds line breaks, spaces or other characters is never sent: list-models
records the problem for that provider and asks the others, run stops before its first call. Every
line written or printed (raw records, model lists, error texts) has the key values removed, whole
or in parts of 8 characters or more, so an error message that quotes a header cannot leak a key.

python generate.py list-models
    -> logs/models_<date>.json, the model lists returned by each provider
python generate.py run CALLS MODELS CAP [--max-minutes M] [--workers W]
    -> data/raw/<calls>_<timestamp>.jsonl, resumable

CALLS   calls_pilot.jsonl, calls.jsonl or a retry file (from make_prompts.py or compute.py)
MODELS  models.json, e.g. {"anthropic_balanced": {"provider": "anthropic", "id": "...",
        "usd_per_mtok_in": 3.0, "usd_per_mtok_out": 15.0}, ...}
CAP     budget cap in USD for this run; a call starts only if the money already spent plus the
        worst case of every call in flight stays under the cap. An attempt that fails after the
        request was sent (time-out, dropped connection, a body cut short or not JSON) may have been
        billed without usage being reported, so it is counted at the worst case of its model,
        recorded as cost_usd_possibly_charged and not retried within the call (the next pass asks
        again), so that no call costs more than its reservation. An answer that cannot be read
        (token counts missing or not numbers, a content that is not text) and a call that raises
        an unexpected error are recorded as failed, counted at the worst case of their model, and
        never stop the run; a lone surrogate in the text, the model id or the finish reason is
        replaced, and escaped in the raw line.

Calls run concurrently, W workers per provider (default 4), and the run stops launching calls
after M minutes (default 330) so that the workflow can still save what was collected. Each raw
line keeps the prompt, the full response body, the usage, the finish reason, the model id
returned by the provider, timestamps and the SHA-256 of the text. Nothing is ever overwritten:
a rerun writes a new file and skips the call_ids already answered in earlier raw files.
Sampling: temperature 1.0 is sent to every model, other parameters stay at the provider
defaults, at most 4,000 output tokens. If a model rejects the temperature parameter (HTTP 400
naming it), the call is sent again without it, later calls to that model omit it, and the record
says so. Each record carries the sampling settings actually sent.
"""
import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import socket
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ENDPOINTS = {
    "anthropic": "https://api.anthropic.com/v1/messages",
    "openai": "https://api.openai.com/v1/chat/completions",
    "mistral": "https://api.mistral.ai/v1/chat/completions",
}
MODEL_LISTS = {
    "anthropic": "https://api.anthropic.com/v1/models",
    "openai": "https://api.openai.com/v1/models",
    "mistral": "https://api.mistral.ai/v1/models",
}
KEYS = {"anthropic": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY", "mistral": "MISTRAL_API_KEY"}
MAX_OUTPUT_TOKENS = 4000
WORST_INPUT_TOKENS = 500
TEMPERATURE = 1.0
ENDPOINT_OVERRIDE = os.environ.get("ART5_ENDPOINT_OVERRIDE")  # used only by the offline test harness


def key_problem(value):
    """Why a secret cannot be sent as a key, or None. The value itself is never returned or printed."""
    if not value:
        return "is empty"
    breaks = value.count("\n") + value.count("\r")
    if breaks:
        return f"holds {breaks} line breaks: put exactly one key in it, on one line"
    if any(ch.isspace() for ch in value):
        return "holds spaces or tabs: put exactly one key in it"
    if not all(33 <= ord(ch) <= 126 for ch in value):
        return "holds characters that are not printable ASCII"
    return None


def secret_parts():
    """The values of the three key secrets, whole and split on white space, 8 characters or longer."""
    parts = set()
    for name in KEYS.values():
        value = os.environ.get(name) or ""
        parts.update(p for p in [value] + value.split() if len(p) >= 8)
    return sorted(parts, key=len, reverse=True)


def scrub(text):
    """The text with every key value removed (added in v0.4.6 after a key was written by an error message)."""
    for p in secret_parts():
        text = text.replace(p, "[secret removed]")
    return text


def headers(provider):
    key = os.environ.get(KEYS[provider])
    if not key:
        raise SystemExit(f"missing secret {KEYS[provider]}")
    problem = key_problem(key)
    if problem:
        raise SystemExit(f"secret {KEYS[provider]} {problem}")
    if provider == "anthropic":
        return {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"}
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def not_sent(e):
    """True for errors raised before the request reached the provider (refused, name not found)."""
    reason = e.reason if isinstance(e, urllib.error.URLError) else e
    return isinstance(reason, (ConnectionRefusedError, socket.gaierror))


def http(method, url, hdrs, body=None, tries=6):
    """Return the status, the body and the number of failed attempts that may have been billed."""
    data = json.dumps(body).encode() if body is not None else None
    charged = 0
    for attempt in range(tries):
        req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.status, json.loads(r.read().decode()), charged
        except urllib.error.HTTPError as e:
            status = e.code
            payload = e.read().decode(errors="replace")
            if status in (408, 429, 500, 502, 503, 504, 529) and attempt < tries - 1:
                time.sleep(min(2 ** attempt * 5, 160))
                continue
            return status, {"error": scrub(payload)}, charged
        except Exception as e:  # time-out, dropped connection, IncompleteRead, a body that is not JSON
            if not not_sent(e):  # may have been billed: no retry here, so a call never costs more than
                return 0, {"error": scrub(repr(e))}, charged + 1  # its reservation; the next pass asks again
            if attempt < tries - 1:
                time.sleep(min(2 ** attempt * 5, 160))
                continue
            return 0, {"error": scrub(repr(e))}, charged


def list_models():
    out = {}
    for provider, url in MODEL_LISTS.items():
        if not os.environ.get(KEYS[provider]):
            out[provider] = {"error": "no key"}
            continue
        problem = key_problem(os.environ[KEYS[provider]])
        if problem:  # never sent: the provider is not asked, and the value is not written
            out[provider] = {"error": f"secret {KEYS[provider]} {problem}; not requested"}
            print(f"{provider}: secret {KEYS[provider]} {problem}; not requested")
            continue
        status, body, _ = http("GET", url, headers(provider))
        out[provider] = {"status": status, "body": body}
    os.makedirs("logs", exist_ok=True)
    path = f"logs/models_{dt.date.today().isoformat()}.json"
    with open(path, "w") as f:
        f.write(scrub(json.dumps(out, indent=1)))
    print("wrote", path)


def request_body(provider, model_id, prompt, temperature=TEMPERATURE):
    msgs = [{"role": "user", "content": prompt}]
    if provider == "anthropic":
        body = {"model": model_id, "max_tokens": MAX_OUTPUT_TOKENS, "messages": msgs}
    elif provider == "openai":
        body = {"model": model_id, "messages": msgs, "max_completion_tokens": MAX_OUTPUT_TOKENS}
    else:
        body = {"model": model_id, "messages": msgs, "max_tokens": MAX_OUTPUT_TOKENS}
    if temperature is not None:
        body["temperature"] = temperature
    return body


def rejects_temperature(status, body):
    return status == 400 and "temperature" in json.dumps(body).lower()


def parse(provider, body):
    """Return text, input tokens, output tokens, model id returned, finish reason; a token count the
    provider did not send is None, so that the call is counted at its worst case."""
    if provider == "anthropic":
        text = "".join(b.get("text", "") for b in body.get("content", []) if b.get("type") == "text")
        u = body.get("usage") or {}
        return text, u.get("input_tokens"), u.get("output_tokens"), body.get("model"), body.get("stop_reason")
    choice = (body.get("choices") or [{}])[0]
    content = (choice.get("message") or {}).get("content") or ""
    if isinstance(content, list):  # some APIs return content parts
        content = "".join(p.get("text", "") for p in content if isinstance(p, dict))
    u = body.get("usage") or {}
    return content, u.get("prompt_tokens"), u.get("completion_tokens"), body.get("model"), choice.get("finish_reason")


def utf8(s):
    """The string with any lone surrogate replaced, so that it can be written as UTF-8 here and by compute.py."""
    return s.encode("utf-8", "replace").decode("utf-8")


def as_count(x):
    """A token count reported by the provider, or None when it is missing or not a number."""
    return int(x) if isinstance(x, (int, float)) and not isinstance(x, bool) and x >= 0 else None


def done_ids():
    ids = set()
    for f in glob.glob("data/raw/*.jsonl"):
        for line in open(f, encoding="utf-8"):
            rec = json.loads(line)
            if rec.get("ok"):
                ids.add(rec["call_id"])
    return ids


def run(calls_path, models_path, cap_usd, max_minutes=330.0, workers=4):
    models = json.load(open(models_path))
    calls = [json.loads(l) for l in open(calls_path, encoding="utf-8")]
    used = sorted({models[c["model"]]["provider"] for c in calls})
    problems = [f"secret {KEYS[p]} {key_problem(os.environ.get(KEYS[p]) or '')}" for p in used
                if key_problem(os.environ.get(KEYS[p]) or "")]
    if problems:  # checked before the first call and before any raw file is opened (v0.4.6)
        raise SystemExit("no call made: " + "; ".join(problems))
    skip = done_ids()
    todo = [c for c in calls if c["call_id"] not in skip]
    os.makedirs("data/raw", exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    out_path = f"data/raw/{os.path.basename(calls_path).replace('.jsonl', '')}_{stamp}.jsonl"
    worst = {name: (m["usd_per_mtok_in"] * WORST_INPUT_TOKENS + m["usd_per_mtok_out"] * MAX_OUTPUT_TOKENS) / 1e6
             for name, m in models.items()}
    lock = threading.Lock()
    state = {"committed": 0.0, "spent": 0.0, "possibly": 0.0, "ok": 0, "failed": 0, "stopped": None, "launched": 0}
    no_temperature = set()  # models that rejected the temperature parameter during this run
    deadline = time.time() + max_minutes * 60
    out = open(out_path, "x", encoding="utf-8")  # mode x: never overwrite a raw file

    def one(c):
        w = worst[c["model"]]
        with lock:
            if state["stopped"]:
                return
            if time.time() > deadline:
                state["stopped"] = f"time limit of {max_minutes} minutes"
                return
            if state["committed"] + w > cap_usd:
                state["stopped"] = f"budget cap of {cap_usd} USD"
                return
            state["committed"] += w
            state["launched"] += 1
        m = models[c["model"]]
        provider = m["provider"]
        url = ENDPOINT_OVERRIDE + "/" + provider if ENDPOINT_OVERRIDE else ENDPOINTS[provider]
        t0 = time.time()
        utc_start = dt.datetime.now(dt.timezone.utc).isoformat()
        temp = None if c["model"] in no_temperature else TEMPERATURE
        charged, status, body = 0, 0, None
        try:
            status, body, ch = http("POST", url, headers(provider), request_body(provider, m["id"], c["prompt"], temp))
            charged += ch
            if temp is not None and rejects_temperature(status, body):
                with lock:
                    no_temperature.add(c["model"])
                temp = None
                status, body, ch = http("POST", url, headers(provider), request_body(provider, m["id"], c["prompt"], None))
                charged += ch
            text, tin, tout, returned, finish = parse(provider, body) if status == 200 else ("", 0, 0, None, None)
            tin, tout = as_count(tin), as_count(tout)
            if not isinstance(text, str) or tin is None or tout is None:
                raise ValueError("answer without text or token counts")
            text = utf8(text)  # a lone surrogate would stop the write, here or in compute.py
            returned = utf8(returned) if isinstance(returned, str) else None
            finish = utf8(finish) if isinstance(finish, str) else None
        except Exception as e:  # an unexpected or unreadable answer never stops the run; worst case
            body, charged = {"error": repr(e), "unreadable_response": body}, charged + 1
            text, tin, tout, returned, finish = "", 0, 0, None, None
        latency = time.time() - t0
        sampling = {"temperature": temp if temp is not None else "provider default (temperature rejected by the model)",
                    "top_p": "provider default", "max_output_tokens": MAX_OUTPUT_TOKENS}
        cost = (tin * m["usd_per_mtok_in"] + tout * m["usd_per_mtok_out"]) / 1e6
        possibly = charged * w
        ok = status == 200 and bool(text.strip())
        rec = dict(c, provider=provider, model_requested=m["id"], model_returned=returned, sampling=sampling,
                   status=status, ok=ok, finish_reason=finish, text=text, input_tokens=tin, output_tokens=tout,
                   cost_usd=cost, cost_usd_possibly_charged=possibly, latency_s=round(latency, 2), utc_start=utc_start,
                   utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                   text_sha256=hashlib.sha256(text.encode()).hexdigest(), response=body)
        line = scrub(json.dumps(rec, ensure_ascii=False))  # no key value in a raw line (v0.4.6)
        try:
            line.encode("utf-8")
        except UnicodeEncodeError:  # a lone surrogate in the raw body: escaped, the line stays valid UTF-8
            line = scrub(json.dumps(rec))
        with lock:
            state["committed"] += cost + possibly - w
            state["spent"] += cost + possibly
            state["possibly"] += possibly
            state["ok" if ok else "failed"] += 1
            out.write(line + "\n")
            out.flush()

    by_provider = {}
    for c in todo:
        by_provider.setdefault(models[c["model"]]["provider"], []).append(c)
    pools = [ThreadPoolExecutor(max_workers=workers) for _ in by_provider]
    futures = [pool.submit(one, c) for pool, cs in zip(pools, by_provider.values()) for c in cs]
    for f in futures:
        f.result()
    for pool in pools:
        pool.shutdown()
    out.close()
    summary = {"raw_file": out_path, "calls_file": calls_path, "to_do": len(todo), "launched": state["launched"],
               "ok": state["ok"], "failed": state["failed"], "spent_usd": round(state["spent"], 4),
               "possibly_charged_usd": round(state["possibly"], 4), "cap_usd": cap_usd,
               "stopped": state["stopped"], "raw_sha256": hashlib.sha256(open(out_path, "rb").read()).hexdigest()}
    os.makedirs("logs", exist_ok=True)
    json.dump(summary, open(f"logs/run_{stamp}.json", "w"), indent=1)
    print(json.dumps(summary, indent=1))
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["list-models", "run"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--max-minutes", type=float, default=330.0)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    if a.cmd == "list-models":
        list_models()
    else:
        run(a.args[0], a.args[1], float(a.args[2]), a.max_minutes, a.workers)
