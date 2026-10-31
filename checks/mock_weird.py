"""Offline stand-in for the provider APIs that answers the K-th request of a route with a malformed-but-HTTP-200 body (WEIRD shape),
and every other request normally. For the v0.4.1 check of 'one() never lets an error stop the run'. Not data.
env: WEIRD shape name, WEIRD_K (default 2): index (1-based) of the request that gets the weird body.
Written by the v0.4.1 confirmation session (claude-sonnet-5-5, 25.10.2026). Shapes usage_missing,
usage_empty, model_surrogate and finish_surrogate added by the main session for v0.4.3.
"""
import json, os, sys, threading
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
SHAPE = os.environ.get("WEIRD", "none"); K = int(os.environ.get("WEIRD_K", "2"))
N = {}; LOCK = threading.Lock()
TEXT = "Le jardin des abeilles\n\n" + " ".join(["Le chat joue dans le jardin avec un petit chien."] * 6)

def normal(route, model):
    if route == "anthropic":
        return {"model": model, "content": [{"type": "text", "text": TEXT}], "stop_reason": "end_turn", "usage": {"input_tokens": 40, "output_tokens": 300}}
    return {"model": model, "choices": [{"message": {"content": TEXT}, "finish_reason": "stop"}], "usage": {"prompt_tokens": 40, "completion_tokens": 300}}

def weird(route, model, shape):
    b = normal(route, model)
    if shape == "list": return json.dumps([1, 2, 3]).encode()
    if shape == "empty_choices":
        return json.dumps({"content": [], "usage": {"input_tokens": 40, "output_tokens": 0}} if route == "anthropic" else {"choices": [], "usage": {"prompt_tokens": 40, "completion_tokens": 0}}).encode()
    if shape == "usage_null": b["usage"] = None
    if shape == "usage_missing": b.pop("usage", None)
    if shape == "usage_empty": b["usage"] = {}
    if shape == "model_surrogate":
        b["model"] = "MODEL_SURROGATE"
        return json.dumps(b).replace('"MODEL_SURROGATE"', '"\\ud800x"').encode()
    if shape == "finish_surrogate":
        if route == "anthropic": b["stop_reason"] = "FINISH_SURROGATE"
        else: b["choices"][0]["finish_reason"] = "FINISH_SURROGATE"
        return json.dumps(b).replace('"FINISH_SURROGATE"', '"\\ud800stop"').encode()
    if shape == "tokens_null": b["usage"] = {"input_tokens": None, "output_tokens": None} if route == "anthropic" else {"prompt_tokens": None, "completion_tokens": None}
    if shape == "content_number":
        if route == "anthropic": b["content"][0]["text"] = 5
        else: b["choices"][0]["message"]["content"] = 5
    if shape == "surrogate":
        s = json.dumps(b).replace("Le jardin", "\\ud800 Le jardin", 1)
        return s.encode()
    if shape == "non_utf8": return b'{"model": "x", "content": "\xff\xfe\xfa"}'
    if shape == "empty_body": return b""
    if shape == "content_parts_bad": b["choices"] = [{"message": {"content": [1, 2]}, "finish_reason": "stop"}] if route != "anthropic" else b["choices"] if "choices" in b else None
    return json.dumps(b).encode()

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])).decode())
        route = self.path.strip("/"); model = body["model"]
        if route == "openai" and "temperature" in body:
            msg = b'{"error": {"message": "Unsupported parameter: temperature is not supported with this model."}}'
            self.send_response(400); self.send_header("Content-Length", str(len(msg))); self.end_headers(); self.wfile.write(msg); return
        with LOCK:
            N[route] = N.get(route, 0) + 1; k = N[route]
        data = weird(route, model, SHAPE) if (k == K and SHAPE != "none") else json.dumps(normal(route, model)).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
    def do_GET(self):
        data = b'{"data": []}'; self.send_response(200); self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)

if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1])), H).serve_forever()
