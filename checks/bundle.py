"""Pack several text files into one bundle, or unpack a bundle, checking each file's SHA-256.
Used to keep archival material (earlier check outputs, the readers' scripts) as one text file in
the Claude project until the repository exists.
  python checks/bundle.py pack OUT.txt FILE...      (paths are stored as given)
  python checks/bundle.py unpack BUNDLE.txt DEST    (fails on any hash mismatch)
Written by the main session (claude-opus-5-5), 25.10.2026."""
import hashlib
import os
import re
import sys

HEAD = "===== FILE {path} | {size} bytes | sha256 {sha} =====\n"
HEAD_RE = re.compile(r"^===== FILE (.+) \| (\d+) bytes \| sha256 ([0-9a-f]{64}) =====\n", re.M)


def pack(out, files):
    with open(out, "w", encoding="utf-8", newline="") as o:
        o.write(f"Bundle of {len(files)} text files. Unpack with: python checks/bundle.py unpack {os.path.basename(out)} DEST\n")
        for f in files:
            data = open(f, "rb").read()
            o.write(HEAD.format(path=f, size=len(data), sha=hashlib.sha256(data).hexdigest()))
            o.write(data.decode("utf-8"))
            o.write("\n")
    print("packed", len(files), "files into", out)


def unpack(bundle, dest):
    text = open(bundle, encoding="utf-8", newline="").read()
    heads = list(HEAD_RE.finditer(text))
    bad = 0
    for h in heads:
        path, size, sha = h.group(1), int(h.group(2)), h.group(3)
        data = text[h.end():].encode("utf-8")[:size]
        ok = hashlib.sha256(data).hexdigest() == sha
        bad += not ok
        target = os.path.join(dest, path)
        os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
        open(target, "wb").write(data)
        print("ok  " if ok else "BAD ", path)
    print(len(heads), "files,", bad, "hash mismatches")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    {"pack": lambda: pack(sys.argv[2], sys.argv[3:]), "unpack": lambda: unpack(sys.argv[2], sys.argv[3])}[sys.argv[1]]()
