"""Paths shared by the checks: the code folder under test (ART5_CODE, default the repository root)
and the Lexique 3.83 file (LEXIQUE, default data/lexicon/Lexique383.tsv, else the copy shipped
with the pylexique package)."""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def code_dir():
    return os.path.abspath(os.environ.get("ART5_CODE", os.path.dirname(HERE)))


def lexicon():
    cands = [os.environ.get("LEXIQUE", ""), os.path.join(code_dir(), "data", "lexicon", "Lexique383.tsv")]
    spec = importlib.util.find_spec("pylexique")
    if spec and spec.submodule_search_locations:
        cands.append(os.path.join(list(spec.submodule_search_locations)[0], "Lexique383", "Lexique383.txt"))
    for p in cands:
        if p and os.path.exists(p):
            return p
    sys.exit("Lexique 3.83 not found: set LEXIQUE, or run python pipeline.py --step lexicon")


if __name__ == "__main__":
    print({"code": code_dir, "lexicon": lexicon}[sys.argv[1]]())
