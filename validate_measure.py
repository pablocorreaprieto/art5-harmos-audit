"""Known-groups check of the primary measure for ART 5, run in GitHub Actions (the wikis are not
reachable from the drafting environment).

python validate_measure.py LEXIQUE OUT_JSON

For 30 subjects fixed before any data were seen, the article on Vikidia (a French encyclopedia
for readers aged 8 to 13) and the article on French Wikipedia are fetched through the MediaWiki
API (current revision, revision id recorded). The first 300 words of running paragraphs of each
article are cleaned and measured with compute.py exactly as the study texts. The measure passes if the mean Zipf frequency of content
lemmas is higher on Vikidia (easier words) in at least 21 of the usable pairs out of 30, i.e. a
one-sided sign test at about .02, and fails otherwise; the script then exits non-zero. Texts are
not stored, only titles, revision ids and measures (both wikis are CC BY-SA).
"""
import html.parser
import json
import os
import sys
import time
import urllib.parse
import urllib.request

from scipy import stats

import compute

SUBJECTS = ["Abeille", "Volcan", "Lune", "Dinosaure", "Pompier", "Chat", "Chien", "Soleil", "Eau", "Neige",
            "Train", "Pain", "Cheval", "Lion", "Baleine", "Forêt", "Montagne", "Arbre", "Fleur", "Papillon",
            "Grenouille", "Château fort", "Chocolat", "Pomme", "Hiver", "Vélo", "Ferme", "Étoile", "Pluie", "Oiseau"]
WIKIS = {"vikidia": "https://fr.vikidia.org/w/api.php", "wikipedia": "https://fr.wikipedia.org/w/api.php"}
N_WORDS = 300
MIN_WINS = 21


class Paragraphs(html.parser.HTMLParser):
    """Collect the text of <p> elements outside tables; footnote markers, styles and scripts dropped."""
    SKIP = {"table", "sup", "style", "script"}

    def __init__(self):
        super().__init__()
        self.skip, self.in_p, self.buf, self.paras = 0, False, [], []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag == "p" and self.skip == 0:
            self.in_p, self.buf = True, []

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        elif tag == "p" and self.in_p:
            text = " ".join("".join(self.buf).split())
            if text:
                self.paras.append(text)
            self.in_p = False

    def handle_data(self, data):
        if self.in_p and self.skip == 0:
            self.buf.append(data)


def fetch(api, title):
    q = urllib.parse.urlencode({"action": "parse", "page": title, "prop": "text|revid", "format": "json",
                                "redirects": 1, "formatversion": 2})
    ua = f"art5-measure-check/0.2 ({os.environ.get('CONTACT_EMAIL', 'no contact set')})"
    req = urllib.request.Request(f"{api}?{q}", headers={"User-Agent": ua})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = json.loads(r.read().decode())
    if "error" in body:
        return None, None
    p = Paragraphs()
    p.feed(body["parse"]["text"])
    words, kept = 0, []
    for para in p.paras:
        kept.append(para)
        words += len(para.split())
        if words >= N_WORDS:
            break
    text = " ".join(" ".join(kept).split()[:N_WORDS])
    return text, body["parse"].get("revid")


def main(lex_path, out_json):
    lex, sha = compute.load_lexicon(lex_path)
    rows = []
    for subject in SUBJECTS:
        row = {"subject": subject}
        for wiki, api in WIKIS.items():
            text, rev = fetch(api, subject)
            time.sleep(1)
            if not text:
                row[wiki] = None
                continue
            m, _ = compute.measure(compute.clean(text)[1], lex)  # same cleaning as the study texts
            row[wiki] = {"revid": rev, "n_words": m["n_words"], "mean_zipf_content": m["mean_zipf_content"],
                         "mean_word_length": m["mean_word_length"], "words_per_sentence": m["words_per_sentence"]}
        rows.append(row)
    usable = [r for r in rows if r.get("vikidia") and r.get("wikipedia") and r["vikidia"]["n_words"] >= 100
              and r["wikipedia"]["n_words"] >= 100]
    wins = sum(r["vikidia"]["mean_zipf_content"] > r["wikipedia"]["mean_zipf_content"] for r in usable)
    p = float(stats.binomtest(wins, len(usable), 0.5, alternative="greater").pvalue) if usable else float("nan")
    diff = [r["vikidia"]["mean_zipf_content"] - r["wikipedia"]["mean_zipf_content"] for r in usable]
    passed = len(usable) >= 25 and wins >= MIN_WINS
    out = {"lexicon_sha256": sha, "n_pairs_usable": len(usable), "vikidia_higher": wins, "sign_test_p_one_sided": p,
           "mean_difference_zipf": sum(diff) / len(diff) if diff else None, "criterion": f"at least {MIN_WINS} pairs and 25 usable",
           "passed": passed, "pairs": rows}
    json.dump(out, open(out_json, "w"), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in out.items() if k != "pairs"}, indent=1))
    return passed


if __name__ == "__main__":
    sys.exit(0 if main(sys.argv[1], sys.argv[2]) else 1)
