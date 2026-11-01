"""Simulate manuscript/make_anonymous_bundle.py in memory at a given ref, with the script's own
REPLACEMENTS/FORBIDDEN/EXCLUDE as they stood at that ref. Writes nothing to the repository."""
import io, re, subprocess, sys, tarfile, types

REPO = "/home/claude/art5-harmos-audit"
ref = sys.argv[1]
src = subprocess.run(["git", "show", f"{ref}:manuscript/make_anonymous_bundle.py"], cwd=REPO, capture_output=True, text=True, check=True).stdout
mod = types.ModuleType("bundle_at_ref"); mod.__dict__["__file__"] = "/nonexistent/manuscript/make_anonymous_bundle.py"
exec(compile(src.split("\ndef main")[0], "bundle", "exec"), mod.__dict__)
EXCL = getattr(mod, "EXCLUDE_PREFIXES", ())
tar_bytes = subprocess.run(["git", "archive", "--format=tar", ref], cwd=REPO, check=True, capture_output=True).stdout
EXTRA = re.compile(r"0009-0009-1844-7453|\bUNIR\b|Universidad Internacional|Rioja|pabcorpri|gmail|hotmail|edu-vd|"
                   r"correa|prieto|pablo|jouxtens|claude\.ai/(?:code|chat|project)|drive\.google", re.IGNORECASE)
left, extra = [], {}
with tarfile.open(fileobj=io.BytesIO(tar_bytes)) as tar:
    for m in tar.getmembers():
        if not m.isfile() or (EXCL and m.name.startswith(EXCL)):
            continue
        data = tar.extractfile(m).read()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        new = text
        for pat, rep in mod.REPLACEMENTS:
            new = re.sub(pat, rep, new)
        if mod.FORBIDDEN.search(new):
            left.append(m.name)
        hits = sorted(set(h.group(0) for h in EXTRA.finditer(new)))
        if hits:
            extra[m.name] = hits
print(f"ref {ref}: excluded prefixes {EXCL}")
print("script would stop on:", left)
print("broader scan after replacement (file: strings):")
for k, v in extra.items():
    print("  ", k, v[:8])
