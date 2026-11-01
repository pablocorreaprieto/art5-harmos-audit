"""Is the AsPredicted-number hit of scan_bundle_confirm3.py a stand-alone number or a run inside a longer number?
Prints counts only (never the digits)."""
import re
import sys
import zipfile

NUM = "".join(["32", "14", "15"])
z = zipfile.ZipFile(sys.argv[1])
name = sys.argv[2]
text = z.read(name).decode("utf-8", "ignore")
total = len(re.findall(NUM, text))
standalone = len(re.findall(r"(?<![0-9.])" + NUM + r"(?![0-9])", text))
embedded_decimal = len(re.findall(r"[0-9]\." + r"[0-9]*" + NUM, text)) + len(re.findall(NUM + r"[0-9]", text))
print(f"{name}: occurrences {total}, stand-alone (no digit or dot before, no digit after) {standalone}, "
      f"inside a longer decimal or digit run {total - standalone}")
