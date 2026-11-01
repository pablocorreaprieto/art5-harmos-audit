Citation verification for the ART 5 manuscript (protocol phase P6.2). You did not write the manuscript.

Input: /tmp/claude-0/-home-claude/0d0dd4bc-423f-5ede-b3ba-98197293b71f/scratchpad/p6_pairs.json, a list of 44
sentence-citation pairs taken from the rendered manuscript (/home/claude/art5-harmos-audit/manuscript/build/manuscript.md).
Each pair gives the sentence, the reference key, the in-text citation, where the source is (DOI, arXiv or URL) and the
access level the author recorded. The full reference entries are in /home/claude/art5-harmos-audit/manuscript/references.json.

Task. For each sentence and the source cited for it, find the passage in the full text that supports the sentence.
Report, for every pair: n, the source key, the access level you obtained yourself (read-directly, abstract-only or not
accessible), the location of the passage (section, page or heading), a short quote of at most 15 words from the passage,
and a verdict: supports, partly supports, does not support, or cannot check. Never mark a pair as supported from an
abstract, a search snippet or a summary; read the passage itself. When a sentence cites several sources, judge the part of
the sentence each source is cited for. When a verdict is "partly supports" or "does not support", say what the sentence
should say instead, in one line. For the two secondary citations ("as cited in"), check that the secondary source
attributes the point to the primary one.

Also check, from the same readings, every number the sentences take from a source (for example ages, years, shares).

How to read. arXiv papers: the alphaXiv tools (get_paper_content, answer_pdf_queries). Web pages and PDFs on the web:
WebFetch, asking for verbatim sentences; alphaXiv's answer_pdf_queries also reads web PDFs. Scite is not available
(subscription expired). Crossref, OpenAlex and publisher pages may be blocked; say so when they are. Do not use the
reading notes of the earlier session (files under scratchpad/p2_literature) as evidence: open the sources yourself.
Do not edit any file. Return the whole report as your final message, as a table followed by a list of the pairs that
need a change. Begin your report with: "Internal reading by a separate AI session. Not peer review."
