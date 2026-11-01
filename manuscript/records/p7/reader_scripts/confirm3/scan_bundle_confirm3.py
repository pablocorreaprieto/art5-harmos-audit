"""Independent scan of the anonymised bundle (third confirmation reading).

python3 -B scan_bundle_confirm3.py BUNDLE.zip

Looks for kinds of identifying strings in every member (text, then the members of containers such as .docx,
the decompressed streams of PDFs, the text chunks of PNGs, and raw bytes in several encodings). It prints the
member name and the KIND of string only, never the string. The patterns are assembled from fragments so that
this file does not spell them out in one piece.
"""
import io
import re
import sys
import zipfile
import zlib

J = "".join

KINDS = {
    "author name": [J(["pa", "blo"]), J(["cor", "rea"]), J(["pri", "eto"]), J(["pabcor", "pri"])],
    "orcid": [J(["0009", "-", "0009", "-", "1844", "-", "7453"]), J(["0009", "0009", "1844", "7453"]),
              J(["1844", "-", "7453"])],
    "university": [J(["universidad ", "internacional ", "de la ", "rioja"]), J(["unir", "ioja"]),
                   J(["comunidad", "unir"]), J(["unir", ".net"])],
    "aspredicted number": [J(["32", "14", "15"])],
    "e-mail domain": [J(["gmail", ".com"]), J(["hot", "mail", "."]), J(["edu", "-vd"]), J(["edu", "vaud"]),
                      J(["univ-", "tlse3"]), J(["mail", ".ch"])],
    "residence": [J(["joux", "tens"]), J(["mez", "ery"]), J(["mé", "zery"])],
    "private link": [J(["docs.google", ".com"]), J(["drive.google", ".com"])],
}
# the university's acronym, in capitals only (the lower-case form is a French verb)
UNIR_CAPS = re.compile(rb"(?<![A-Za-z])" + J(["UN", "IR"]).encode() + rb"(?![A-Za-z])")


def variants(p):
    """The pattern as bytes in the encodings a binary container may use (lower-case search)."""
    return [p.encode("utf-8"), p.encode("utf-16-le"), p.encode("utf-16-be")]


COMPILED = {k: [v for p in ps for v in variants(p)] for k, ps in KINDS.items()}


def kinds_in(data):
    found = set()
    low = data.lower()
    # also a text view in which non-letters between letters are kept as is; Latin-1 keeps byte values
    for kind, pats in COMPILED.items():
        if kind == "aspredicted number":
            # a stand-alone number: not inside a longer run of digits (a decimal in a data file is not the number)
            num = KINDS[kind][0].encode()
            if re.search(rb"(?<![0-9])" + re.escape(num) + rb"(?![0-9])", low) or \
               any(p in low for p in pats[1:]):
                found.add(kind)
            continue
        if any(p in low for p in pats):
            found.add(kind)
    if UNIR_CAPS.search(data):
        found.add("university (capitals)")
    return found


def pdf_streams(data):
    out = []
    for m in re.finditer(rb"stream\r?\n", data):
        start = m.end()
        end = data.find(b"endstream", start)
        if end < 0:
            continue
        raw = data[start:end]
        for wbits in (15, -15):
            try:
                out.append(zlib.decompress(raw, wbits))
                break
            except Exception:
                continue
    return out


def png_chunks(data):
    out = []
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return out
    i = 8
    while i + 8 <= len(data):
        ln = int.from_bytes(data[i:i + 4], "big")
        typ = data[i + 4:i + 8]
        body = data[i + 8:i + 8 + ln]
        if typ in (b"tEXt", b"iTXt", b"zTXt", b"eXIf", b"tIME", b"iCCP"):
            out.append(body)
            for wb in (15, -15):
                try:
                    out.append(zlib.decompress(body[body.index(b"\x00") + 2:], wb))
                    break
                except Exception:
                    pass
            # iTXt may hold a compressed text after the keyword fields
            for k in range(len(body)):
                try:
                    out.append(zlib.decompress(body[k:]))
                    break
                except Exception:
                    continue
        i += 12 + ln
    return out


def scan_bytes(name, data, depth=0):
    """Return the set of kinds found in data and, recursively, in its containers."""
    found = kinds_in(data)
    if depth < 3 and zipfile.is_zipfile(io.BytesIO(data)):
        with zipfile.ZipFile(io.BytesIO(data)) as zz:
            for info in zz.infolist():
                found |= {k + " (in member of container)" for k in kinds_in(info.filename.encode())}
                try:
                    found |= {k + " (in member of container)" for k in scan_bytes(name, zz.read(info), depth + 1)}
                except Exception:
                    pass
    if data[:5] == b"%PDF-":
        for s in pdf_streams(data):
            found |= {k + " (in PDF stream)" for k in kinds_in(s)}
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        for s in png_chunks(data):
            found |= {k + " (in PNG chunk)" for k in kinds_in(s)}
    return found


def main():
    path = sys.argv[1]
    n = nbin = 0
    hits = {}
    kinds_of_files = {}
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            n += 1
            data = z.read(info)
            ext = info.filename.rsplit(".", 1)[-1].lower() if "." in info.filename.rsplit("/", 1)[-1] else ""
            kinds_of_files[ext] = kinds_of_files.get(ext, 0) + 1
            f = scan_bytes(info.filename, data)
            fn = kinds_in(info.filename.encode())
            if fn:
                f |= {k + " (in the path)" for k in fn}
            if f:
                hits[info.filename] = sorted(f)
    print(f"members scanned: {n}")
    print("by extension:", ", ".join(f"{k or '(none)'}={v}" for k, v in sorted(kinds_of_files.items())))
    if not hits:
        print("no identifying string of any kind found")
        return 0
    for name, ks in sorted(hits.items()):
        shown = name if not any("path" in k for k in ks) else "[path withheld]"
        print(f"HIT {shown}: " + "; ".join(ks))
    return 1


if __name__ == "__main__":
    sys.exit(main())
