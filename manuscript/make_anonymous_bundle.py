"""Anonymised copy of the repository for double-anonymous review (P8).

python manuscript/make_anonymous_bundle.py OUT.zip [--ref HEAD]

Takes the committed files at --ref (git archive, so nothing untracked and no .git history), replaces the
strings that identify the author (REPLACEMENTS), checks that none is left in any text file (it stops
otherwise), adds ANONYMISATION.md listing what was changed and why the SHA-256 of the changed files differ
from those recorded in history/hashes.txt, and writes a zip. The raw model outputs (data/raw) are kept.
Written by the main session (claude-opus-5-5) on 1.11.2026.
"""
import argparse
import io
import os
import re
import subprocess
import sys
import tarfile
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPLACEMENTS = [
    (r"https://github\.com/pablocorreaprieto/art5-harmos-audit", "https://github.com/ANONYMISED/art5-harmos-audit"),
    (r"pablocorreaprieto", "ANONYMISED"),
    (r"AsPredicted #\d+", "AsPredicted #[anonymised]"),
    (r"\"321415\"", "\"[anonymised]\""),
    (r"\bPablo's\b", "the author's"),
    (r"\bPablo\b", "the author"),
]
FORBIDDEN = re.compile(r"pablo|correa|pabcorpri|edu-vd|\b321415\b|jouxtens", re.IGNORECASE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--ref", default="HEAD")
    a = ap.parse_args()
    tar_bytes = subprocess.run(["git", "archive", "--format=tar", a.ref], cwd=REPO, check=True,
                               capture_output=True).stdout
    changed, left = [], []
    with tarfile.open(fileobj=io.BytesIO(tar_bytes)) as tar, zipfile.ZipFile(a.out, "w", zipfile.ZIP_DEFLATED) as z:
        for m in tar.getmembers():
            if not m.isfile():
                continue
            data = tar.extractfile(m).read()
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                z.writestr("art5-harmos-audit/" + m.name, data)
                continue
            new = text
            for pat, rep in REPLACEMENTS:
                new = re.sub(pat, rep, new)
            if new != text:
                changed.append(m.name)
            if FORBIDDEN.search(new):
                left.append(m.name)
            z.writestr("art5-harmos-audit/" + m.name, new)
        note = ("# Anonymised copy for review\n\nThis is the study repository at commit " +
                subprocess.run(["git", "rev-parse", "--short", a.ref], cwd=REPO, capture_output=True, text=True).stdout.strip() +
                ", without its git history. Strings that identify the author were replaced in these files, whose "
                "SHA-256 therefore differ from the values in history/hashes.txt:\n\n" +
                "\n".join(f"- {c}" for c in changed) + "\n\nNothing else was changed.\n")
        z.writestr("art5-harmos-audit/ANONYMISATION.md", note)
    if left:
        os.remove(a.out)
        sys.exit("identifying strings left in: " + ", ".join(left))
    print(f"wrote {a.out}; {len(changed)} files anonymised: {', '.join(changed)}")


if __name__ == "__main__":
    main()
