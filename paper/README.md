# Elsevier manuscript

This directory is the publication workspace for an Elsevier journal manuscript using the CAS LaTeX template already stored here.

## Layout

- `main.tex`: the complete manuscript in one file, using `cas-sc.cls`.
- `figs/`: publication figures. Prefer stable, descriptive filenames and document the generating analysis.
- `references.bib`: project bibliography; verify every entry and citation claim.
- `cas-*.cls`, `cas-common.sty`, and `cas-model2-names.bst`: Elsevier CAS template assets.
- `doc/`: upstream template documentation.
- `Skills/write-ai-paper/`: evidence-grounded manuscript-writing instructions for AI agents.
- `Skills/nature-figure/`: figure contract and QA scripts (text collisions, 5 pt glyph floor, panel alignment), Python only; adapted from nature-skills (Apache-2.0).
- `Skills/nature-reviewer/`: mock peer review with three blind reviewers, forensic numerical audit and synthesis; `RUN.md` and `templates/` explain how to run it here. Adapted from nature-skills (Apache-2.0).
- `Skills/nature-shared/`: one shared file used by `nature-reviewer`.

Use `cas-dc` instead of `cas-sc` only when the target journal requires the double-column layout. Confirm the current author guidelines of the selected journal before submission.

## Compile

From this directory, a typical local build is:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

LaTeX build products are ignored by Git. Keep manuscript sources, bibliography, and publication figures tracked.

## Evidence flow

Figures and tables should originate from `experiments/<experiment>/summary/` or `notebooks/analysis/`, with the source experiment and configuration recorded. Do not manually copy untraceable numbers into the paper.

Before any AI-assisted manuscript task, read `Skills/write-ai-paper/SKILL.md`, then `General.md`, followed by only the section-specific files routed by the skill. Never invent results, citations, or bibliographic metadata.

Before adding or changing a figure, read `Skills/nature-figure/SKILL.md` and run its audits (`uv add matplotlib pymupdf` once per project). Run a mock review with `Skills/nature-reviewer/RUN.md` only when requested; it costs several hundred thousand tokens in three-reviewer mode.

Keep all manuscript sections in `main.tex`. Do not split the article into separate `sections/*.tex` files.
