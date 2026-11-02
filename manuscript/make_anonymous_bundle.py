"""Anonymised copy of the repository for double-anonymous review (P8).

python manuscript/make_anonymous_bundle.py OUT.zip [--ref HEAD]

Takes the committed files at --ref (git archive, so nothing untracked and no .git history), replaces the
strings that identify the author (REPLACEMENTS), checks that none is left in any text file (it stops
otherwise), adds ANONYMISATION.md listing what was changed and why the SHA-256 of the changed files differ
from those recorded in history/hashes.txt, and writes a zip. The raw model outputs (data/raw) are kept; the files
listed in EXCLUDE_PREFIXES, which name the author by design, are left out.
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
    (r"\b321415\b", "[anonymised]"),
    # names in any case (made case-insensitive after the confirmation reading of 1.11.2026)
    (r"(?i)\bPablo Correa Prieto\b", "the author"),
    (r"(?i)\bCorrea Prieto\b", "[author]"),
    (r"(?i)\bCorrea\b", "[author]"),
    (r"(?i)\bPrieto\b", "[author]"),
    (r"(?i)\bPablo's\b", "the author's"),
    (r"(?i)\bPablo\b", "the author"),
    (r"0009-0009-1844-7453", "[ORCID removed]"),
    (r"Universidad Internacional de La Rioja", "[university]"),
    (r"\bUNIR\b", "[university]"),
    (r"[\w.+-]+@(?:gmail\.com|hotmail\.\w+|edu-vd\.ch|eduvaud\.ch)", "[e-mail removed]"),
    (r"https://(?:docs|drive)\.google\.com/\S*?(?=[)\s\]>\"']|$)", "[link to a private document removed for review]"),
]
FORBIDDEN = re.compile(r"(?i:pablo|correa|prieto|pabcorpri|edu-vd|\b321415\b|jouxtens|0009-0009-1844-7453|"
                       r"Universidad Internacional de La Rioja|gmail\.com|hotmail)|\bUNIR\b")  # UNIR in capitals only: "unir" is a French verb
# files that name the author by design and are not part of what reviewers need (added after reading R3, 1.11.2026):
# the submission letters and title page, the G2 exception list, and this script (its patterns name the author)
EXCLUDE_PREFIXES = ("manuscript/submission/", "manuscript/verification_report.md", "manuscript/make_anonymous_bundle.py",
                    # the rendered title page and cover letter (added after the confirmation reading, 1.11.2026)
                    "manuscript/build/title_page.", "manuscript/build/cover_letter.",
                    # the G2 research and check-reading records, whose briefs describe the author (1.11.2026, evening)
                    "manuscript/records/g2/",
                    # the pre-submission audit records (journal strategy, simulated reviews), 2.11.2026
                    "manuscript/records/audit/")
# scripts of the reading sessions that search for the author's identifying strings (their patterns name the author)
EXCLUDE_PATTERNS = (re.compile(r"^manuscript/records/.*/(?:bundle_sim|scan_bundle)[^/]*\.py$"),)


def excluded(name):
    return name.startswith(EXCLUDE_PREFIXES) or any(p.search(name) for p in EXCLUDE_PATTERNS)


def binary_hits(data):
    """Identifying strings in a binary file: inside each member of a zip container (.docx), else in the raw bytes
    read as Latin-1 (catches PDF and PNG metadata). Added after the confirmation reading of 1.11.2026, which found
    the author's name in a .docx that the text scan skipped."""
    texts = []
    if zipfile.is_zipfile(io.BytesIO(data)):
        with zipfile.ZipFile(io.BytesIO(data)) as zz:
            for info in zz.infolist():
                texts.append(zz.read(info).decode("utf-8", "ignore"))
    else:
        texts.append(data.decode("latin-1"))
    return any(FORBIDDEN.search(t) for t in texts)
# manuscript/records/ (protocol, review briefs and reports) is kept, with the replacements above, because the
# manuscript's AI statement points reviewers to it (decided after the readings R1 and R3, 1.11.2026)


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
            if not m.isfile() or excluded(m.name):
                continue
            data = tar.extractfile(m).read()
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                if binary_hits(data):
                    left.append(m.name + " (binary)")
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
                "\n".join(f"- {c}" for c in changed) + "\n\nLeft out because they name the author by design: " +
                ", ".join(EXCLUDE_PREFIXES) + ", and the reading sessions' scripts matching " +
                ", ".join(p.pattern for p in EXCLUDE_PATTERNS) + " (they search for the author's identifying strings)."
                " Nothing else was changed.\n")
        z.writestr("art5-harmos-audit/ANONYMISATION.md", note)
    if left:
        os.remove(a.out)
        sys.exit("identifying strings left in: " + ", ".join(left))
    print(f"wrote {a.out}; {len(changed)} files anonymised: {', '.join(changed)}")


if __name__ == "__main__":
    main()
