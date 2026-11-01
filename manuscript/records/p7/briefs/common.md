Context for every reviewer (same text for R1, R2 and R3)

- Manuscript to review (rendered, every number filled in): /home/claude/art5-harmos-audit/manuscript/build/manuscript.md
  Supporting Information: /home/claude/art5-harmos-audit/manuscript/build/supplement.md
  Figures: /home/claude/art5-harmos-audit/results/figures/*.png (open them with the Read tool to see them)
- Repository (local clone, read only for you): /home/claude/art5-harmos-audit
  Preregistration text as deposited: PREREG.md. Design: design.json. Analysis: analyze.py. Measure: compute.py.
  Frozen results: results/numbers.json (every confirmatory number), results/manuscript_numbers.json (the
  number as printed in the text, by name), results/measures.csv (one row per text), results/probes.csv.
  The manuscript source with its placeholders is manuscript/manuscript.md; the rendered file is what a
  journal would receive.
- Target journal: British Journal of Educational Technology (BJET, Wiley, for the British Educational
  Research Association). Recorded constraints: manuscripts "should not normally exceed 6000 words,
  excluding references"; double-anonymous review; BJET articles carry Practitioner Notes; Wiley's policy
  allows AI to "substantially edit, develop, or translate any part of a manuscript" if its use is
  "described transparently". A BJET editorial of 2025 asks authors to name the model, its version and
  provider and to give prompt details.
- Rules for you: do not edit, create or delete any file in the repository; write nothing except your
  report, which you return as your final message. Do not call any model provider API and do not run
  pipeline.py steps that call models (generate, pilot, list-models, validate). You may run Python
  locally on the repository files (python3, pandas, numpy, scipy, statsmodels are installed), for
  example `python3 analyze.py results/measures.csv results/probes.csv /tmp/x.json` to recompute.
- Do not praise. Every finding needs a location (section and sentence, table or file and line), the
  problem, why it matters, a severity (must-fix, should-fix or minor) and a concrete fix. Distinguish
  what you checked (say how) from what you infer.
- Begin your report with exactly: "Internal reading by a separate AI session. Not peer review."
