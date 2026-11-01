"""Independent scan of the anonymised bundle (zip). Prints file names and KINDS of strings only, never the strings.
python3 -I scan_bundle.py BUNDLE.zip
"""
import io
import re
import sys
import zipfile
from collections import Counter, defaultdict

KINDS = {
    "name": re.compile(r"(?i)pablo|corr[eé]a|prieto|pabcorpri|p\.\s*correa|correaprieto"),
    "orcid": re.compile(r"(?i)0009[-\s]?0009[-\s]?1844[-\s]?7453|orcid\.org/|\borcid\b"),
    "university": re.compile(r"\bUNIR\b|(?i:unir\.net|comunidadunir|la rioja|universidad internacional|univ-tlse3|toulouse|tlse\b|universidad de la laguna|\bull\.es)"),
    "email_domain": re.compile(r"(?i)@(?:gmail|hotmail|mail\.ch|edu-vd|eduvaud|univ-tlse3|comunidadunir|unir)\b"),
    "email_any": re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    "aspredicted_number": re.compile(r"(?<!\d)321415(?!\d)"),
    "aspredicted_link": re.compile(r"(?i)aspredicted\.org/\S+"),
    "private_doc_link": re.compile(r"(?i)docs\.google\.com|drive\.google\.com|notion\.so|dropbox\.com|1drv\.ms|sharepoint\.com|onedrive\.live"),
    "claude_session_link": re.compile(r"(?i)claude\.ai/(?:chat|code|artifact|project)\S*|session_01[A-Za-z0-9]+"),
    "github_user_link": re.compile(r"(?i)github\.com/(?!ANONYMISED)[\w.-]+"),
    "residence": re.compile(r"(?i)jouxtens|m[eé]zery"),  # street and postcode patterns removed before publication (11.11.2026)
    "phone_or_dob": re.compile(r"(?!x)x"),  # the author's phone numbers and date of birth were removed before publication (11.11.2026)
    "placeholder_anonymised": re.compile(r"ANONYMISED|\[anonymised\]|\[author\]|\[university\]|\[e-mail removed\]|\[ORCID removed\]|the author"),
}
# kinds that must be zero for an anonymous bundle
MUST_BE_ZERO = ["name", "orcid", "university", "email_domain", "aspredicted_number", "private_doc_link", "residence", "phone_or_dob"]


def texts_of(name, data):
    """Yield (member label, text) for a zip member: plain text, or each member of a nested zip (.docx), else latin-1."""
    try:
        yield name, data.decode("utf-8")
        return
    except UnicodeDecodeError:
        pass
    if zipfile.is_zipfile(io.BytesIO(data)):
        with zipfile.ZipFile(io.BytesIO(data)) as zz:
            for info in zz.infolist():
                yield f"{name}!{info.filename}", zz.read(info).decode("utf-8", "ignore")
    else:
        yield name + " (raw bytes)", data.decode("latin-1")


def main(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    print(f"members: {len(names)}")
    per_kind_files = defaultdict(Counter)
    n_text = n_bin = 0
    bin_files = []
    for name in names:
        data = z.read(name)
        try:
            data.decode("utf-8")
            n_text += 1
        except UnicodeDecodeError:
            n_bin += 1
            bin_files.append(name)
        for label, t in texts_of(name, data):
            for kind, rx in KINDS.items():
                c = len(rx.findall(t))
                if c:
                    per_kind_files[kind][label] += c
    print(f"text members: {n_text}, binary members: {n_bin}")
    print("binary members:", ", ".join(sorted(bin_files)))
    for kind in KINDS:
        tot = sum(per_kind_files[kind].values())
        print(f"\n[{kind}] total hits {tot} in {len(per_kind_files[kind])} members")
        if kind in ("email_any", "placeholder_anonymised"):
            for lab, c in per_kind_files[kind].most_common(8):
                print(f"   {c:5d}  {lab}")
        else:
            for lab, c in per_kind_files[kind].most_common(30):
                print(f"   {c:5d}  {lab}")
    bad = {k: sum(per_kind_files[k].values()) for k in MUST_BE_ZERO if per_kind_files[k]}
    print("\nSUMMARY must-be-zero kinds with hits:", bad if bad else "none")


if __name__ == "__main__":
    main(sys.argv[1])
