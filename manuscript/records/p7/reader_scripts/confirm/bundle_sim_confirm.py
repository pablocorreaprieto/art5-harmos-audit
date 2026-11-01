"""Simulate manuscript/make_anonymous_bundle.py at a ref, in memory, with the stop bypassed, and scan the
result with the script's own FORBIDDEN regex plus the broader list the refutation reader used (both are in
the repository), plus generic patterns (e-mail, ORCID, claude.ai links, google links). Writes nothing."""
import io, re, subprocess, sys, tarfile, types, collections

REPO = sys.argv[1]
ref = sys.argv[2]
src = subprocess.run(["git", "show", f"{ref}:manuscript/make_anonymous_bundle.py"], cwd=REPO,
                     capture_output=True, text=True, check=True).stdout
mod = types.ModuleType("bundle_at_ref")
mod.__dict__["__file__"] = "/nonexistent/manuscript/make_anonymous_bundle.py"
exec(compile(src.split("\ndef main")[0], "bundle", "exec"), mod.__dict__)
EXCL = getattr(mod, "EXCLUDE_PREFIXES", ())
tar_bytes = subprocess.run(["git", "archive", "--format=tar", ref], cwd=REPO, check=True, capture_output=True).stdout
# broader list: the refutation reader's EXTRA (records/p7/reader_scripts/refute_r2r3/bundle_sim.py) plus generic patterns
EXTRA = re.compile(r"0009-0009-1844-7453|\bUNIR\b|Universidad Internacional|Rioja|pabcorpri|gmail|hotmail|edu-vd|"
                   r"correa|prieto|pablo|jouxtens|claude\.ai/(?:code|chat|project)|drive\.google|docs\.google|"
                   r"[\w.+-]+@[\w-]+\.[\w.]+|orcid\.org/\S+|github\.com/[\w-]+", re.IGNORECASE)
left, extra, n_files, changed = [], {}, 0, []
with tarfile.open(fileobj=io.BytesIO(tar_bytes)) as tar:
    for m in tar.getmembers():
        if not m.isfile() or (EXCL and m.name.startswith(EXCL)):
            continue
        n_files += 1
        data = tar.extractfile(m).read()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        new = text
        for pat, rep in mod.REPLACEMENTS:
            new = re.sub(pat, rep, new)
        if new != text:
            changed.append(m.name)
        if mod.FORBIDDEN.search(new):
            left.append(m.name)
        hits = collections.Counter(h.group(0).lower() for h in EXTRA.finditer(new))
        if hits:
            extra[m.name] = dict(hits)
print(f"ref {ref}: {n_files} files in the bundle; excluded prefixes {EXCL}")
print(f"files changed by REPLACEMENTS: {len(changed)}")
print("script would stop on:", left)
print("broader scan after replacement (file: strings and counts):")
for k, v in sorted(extra.items()):
    print("  ", k, v)
