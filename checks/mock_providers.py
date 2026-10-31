"""Offline stand-in for the three provider APIs, for the end-to-end test of the ART 5 pipeline only.
Texts are generated from a small word list; easier words for younger requested ages. Not data.
Written by the main session (claude-opus-5-5), 25.10.2026.
"""
import json, random, re, sys, threading
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

EASY = "chat chien maison jardin soleil pain eau arbre fleur école ami jouer manger courir voir petit grand beau content".split()
HARD = "insecte pollen colonie nectar ruche éruption magma cratère migration altitude hémisphère photosynthèse écosystème".split()
COUNT = {"n": 0}
SEEN = set()
LOCK = threading.Lock()

def age_of(prompt):
    m = re.search(r"de (\d+) à (\d+) ans", prompt)
    if m:
        return (int(m.group(1)) + int(m.group(2))) / 2
    m = re.search(r"de (\d)[HP]\b", prompt)
    if m:
        return int(m.group(1)) + 3.5
    return 9.0

def make_text(prompt, rng):
    if prompt.startswith("À quel âge") or "quel âge" in prompt:
        g = re.search(r"(\d)[HP]", prompt)
        n = int(g.group(1)) if g else 5
        return f"Les élèves de {n}H ont en général entre {n + 3} et {n + 4} ans.", "stop"
    a = age_of(prompt)
    p_hard = min(max((a - 5) / 12, 0.05), 0.6)
    n = rng.randint(60, 160)
    words = [rng.choice(HARD) if rng.random() < p_hard else rng.choice(EASY) for _ in range(n)]
    sents, i = [], 0
    while i < len(words):
        k = rng.randint(6, 12)
        s = " ".join(words[i:i + k])
        sents.append("Le " + s + ".")
        i += k
    return "Le jardin des abeilles\n\n" + " ".join(sents), "stop"

class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])).decode())
        prompt = body["messages"][0]["content"]
        if self.path.strip("/") == "openai" and "temperature" in body:  # this mock model refuses the parameter
            msg = b'{"error": {"message": "Unsupported parameter: temperature is not supported with this model."}}'
            self.send_response(400); self.send_header("Content-Length", str(len(msg))); self.end_headers(); self.wfile.write(msg); return
        rng = random.Random(prompt + body["model"])
        with LOCK:
            COUNT["n"] += 1
            n = COUNT["n"]
        if n == 3:  # one transient rate-limit error
            self.send_response(429); self.end_headers(); self.wfile.write(b'{"error":"rate"}'); return
        text, finish = make_text(prompt, rng)
        key = prompt + body["model"]
        with LOCK:
            first = key not in SEEN
            SEEN.add(key)
        if first and rng.random() < 0.06:
            text, finish = "Voici un texte court.", "stop"  # too short on the first request only
        if first and rng.random() < 0.04:  # a transport failure on the first request only
            msg = b'{"error": "bad gateway at the mock"}'
            self.send_response(400); self.send_header("Content-Length", str(len(msg))); self.end_headers(); self.wfile.write(msg); return
        if rng.random() < 0.02:
            finish = "length"
        provider = self.path.strip("/")
        if provider == "anthropic":
            out = {"model": body["model"] + "-20261001", "content": [{"type": "text", "text": text}],
                   "stop_reason": "end_turn" if finish == "stop" else "max_tokens",
                   "usage": {"input_tokens": 40, "output_tokens": len(text) // 4}}
        else:
            out = {"model": body["model"], "choices": [{"message": {"content": text}, "finish_reason": finish}],
                   "usage": {"prompt_tokens": 40, "completion_tokens": len(text) // 4}}
        data = json.dumps(out).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
    def do_GET(self):
        data = b'{"data": []}'
        self.send_response(200); self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)

if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1])), H).serve_forever()
