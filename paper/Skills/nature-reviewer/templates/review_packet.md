# Immutable review packet (<run id>, <date>)

This packet is identical for every reviewer. It contains only supplied material and common criteria.
It contains no concerns, interpretations or other reviews.

## Supplied manuscript

- LaTeX source (authoritative text): `paper/main.tex` (<word count> words; SHA256 in `manuscript_hashes.txt`).
- Compiled PDF of the same manuscript: `<path to PDF>` (<pages> pages).
- Figures referenced by the manuscript: `paper/figs/*.pdf`.
- Bibliography: `paper/references.bib`.

Do NOT read anything else in the repository (no experiments/, docs/, .agent/, data/, code, response
letters). The review must be based on the manuscript as a reader would receive it.

## Input scope

<Full manuscript draft | selected sections>. Target journal: <journal>. <First submission | Resubmission;
previous reviews are not part of this packet and must not be guessed.>

## Assessment boundary

- Only the manuscript text, tables, figures and reference list are assessable.
- Supplementary files, code repositories and raw data are <not supplied | supplied at ...>.
- Data or code availability statements can be assessed only as reporting, not verified.

## Common journal criteria

Apply the five axes of `editorial criteria and processes.md` and `review-axes.md`: originality,
scientific importance, interdisciplinary readership, technical soundness, readability for
nonspecialists. Calibrate "interdisciplinary readership" to the readers of <journal> and say so.

## Common grounding rules

- Use `technical-concern-taxonomy.md` as the internal 12-axis coverage checklist.
- Use `report-structure.md` for the report skeleton and concern formats.
- Evidence pointers cite a section, table, figure or equation number verified in `paper/main.tex`.
  Line numbers are not supplied; do not invent them.
- Never invent experiments, prior work, datasets or figure contents not present in the input.
- Mark anything that cannot be assessed as `Not assessable from provided material`.
