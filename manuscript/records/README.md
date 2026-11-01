# Records of the AI-assisted research process

This folder holds what the manuscript's statement "Use of generative AI" refers to: the written protocol
the study followed, and the briefs and full reports of every separate AI session that read the design,
the code or the manuscript. These sessions are internal readings by AI sessions, not peer review.

- `protocol_v1.1.md`: the protocol for an AI-assisted article (version 1.1 of 25.10.2026, in French),
  exported from the author's Google Doc on 1.11.2026 without edits. It sets the division of labour
  (the assistant does the work; the author decides at gate G1, design, and gate G2, submission), the
  checks, the rule that every source is read in full before it is cited, and the logging rules.
- `design_readings/`: the nine readings of the design before the preregistration (25.10.2026 and
  1.11.2026) and the research session on the journal ladder, each with its brief and full report
  (`readings_1_to_8.md`, `reading_9.md`, in French with the English briefs and reports quoted
  verbatim), and the scripts the readers wrote (`reader_scripts_bundle.txt`, unpack with
  `python checks/bundle.py unpack manuscript/records/design_readings/reader_scripts_bundle.txt OUTDIR`).
- `p7/`: the readings of the manuscript (phase P7, 1.11.2026) and the check of the citations (phase
  P6.2): `p7_records.md` keeps every brief and every full report verbatim, in order (R1 substance,
  claude-opus-5-5; R2 methods and statistics, claude-sonnet-5-5; R3 editor's reading, claude-fable-5-1;
  the sentence-citation check, claude-sonnet-5-5; the refutation of R1, claude-fable-5-1; the
  refutation of R2 and R3, claude-opus-5-5); `briefs/` holds the brief files as given, including the
  brief and the report of the literature reading session (phase P2) and the 44 sentence-citation pairs
  that were checked; `reader_scripts/` the scripts and text outputs the reading sessions wrote.

Every finding of these readings is one row of the "Relectures IA" tab of the project journal, with its
refutation where one was made (the design readings of 25.10.2026 sent only their blocking findings to a
refutation), whether it was applied, and who confirmed the correction. The journal is kept by the author
outside the repository; `findings_log.csv` is a copy of that tab, in French: 166 rows, from the design
readings of 25.10.2026 to the second confirmation reading of 1.11.2026, of which one row is a finding of the
main session and one a note of checks that found nothing. It was exported by the main session on 1.11.2026
after the first confirmation reading noted that the manuscript's AI statement refers to it. The two
confirmation readings of the P7 corrections (claude-fable-5-1, then claude-sonnet-5-5) are at the end of
`p7/p7_records.md`, with their scripts in `p7/reader_scripts/confirm/` and `confirm2/`. The main session that
ran the study is claude-opus-5-5.
