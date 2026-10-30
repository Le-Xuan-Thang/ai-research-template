# Running a mock peer review in this template

`SKILL.md` is the upstream protocol and stays authoritative. This file says how to run it here,
what it costs, and where results go. Mock reviews are internal evidence for the authors; never
paste them into the manuscript or present them as real peer review.

## When to run it

| Mode | Use | Measured cost on a 14k-word manuscript |
|---|---|---|
| Three blind reviewers (default of `SKILL.md`) | once per major revision, before submission | about 345k subagent tokens + about 70k orchestration, 8 min wall in parallel |
| One reviewer with one emphasis brief | intermediate drafts, a focused check (statistics, physics, claims) | about one third of the above |
| Forensic audit only (`references/forensic-consistency-audit.md`) | after any change to tables or headline numbers | about 15k tokens, no subagents |

Run it only when the user asks. The three-reviewer mode needs one isolated context per reviewer
(subagents, separate processes or separate sessions). If isolation is not available, say that mutual
blindness is not guaranteed, as `SKILL.md` requires.

## Procedure

1. Create a new run directory, never reuse one:
   `experiments/<exp>/<dataset>/review_<YYYYMMDD>_<nn>/` with `inputs/` and `reports/`.
2. Copy `templates/review_packet.md`, `templates/reviewer_instructions.md` and one
   `templates/brief_example_R*.md` per reviewer into `inputs/`, then fill every `<...>` field.
   Copy `SKILL.md`, `references/review-axes.md`, `references/technical-concern-taxonomy.md`,
   `references/report-structure.md` and `references/editorial criteria and processes.md` into
   `inputs/` so the run stays reproducible if the skill changes.
3. Record `sha256sum paper/main.tex` and the compiled PDF in `inputs/manuscript_hashes.txt`.
   Fix the emphasis briefs before launching any reviewer.
4. Launch each reviewer in its own context with only: "read `inputs/reviewer_instructions.md` and
   follow it". Reviewers read the whole manuscript and nothing else in the repository.
5. When all reports exist, freeze them: `sha256sum reports/*.md > reports/sha256_frozen.txt`.
   Do not edit them afterwards.
6. In the main session run `references/forensic-consistency-audit.md` on the Abstract, Conclusion and
   all tables, and write `forensic_audit.md`.
7. Write `synthesis.md` following `references/report-structure.md`: consensus only when at least two
   reports raise the same issue; keep audit findings separate; record pairwise overlap.
8. Spot-check at least ten evidence pointers against `paper/main.tex` and record the result. A pointer
   that does not exist in the manuscript invalidates that concern.
9. Write `REPORT.md` (what ran, cost from the harness, counts, groundedness check) and `metrics.md`.
   Link the run from the project's evidence records. Do not change `paper/main.tex` unless the user
   starts a revision.

## Calibration notes

- The skill's criteria are written for *Nature*. For a disciplinary journal, tell reviewers in the
  packet to calibrate "interdisciplinary readership" to the target journal's readers.
- Useful emphasis lenses for an applied-AI paper: physical or domain basis of the labels;
  machine-learning methodology and statistics; claims, novelty, reporting and readability.
- Expect the most valuable output to be the consensus blocking items and the forensic audit; the full
  reports are long (about 30k characters each) and are read through the synthesis.
