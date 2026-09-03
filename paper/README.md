# Elsevier manuscript

This directory is the publication workspace for an Elsevier journal manuscript using the CAS LaTeX template already stored here.

## Layout

- `main.tex`: the complete manuscript in one file, using `cas-sc.cls`.
- `figs/`: publication figures. Prefer stable, descriptive filenames and document the generating analysis.
- `references.bib`: project bibliography; verify every entry and citation claim.
- `cas-*.cls`, `cas-common.sty`, and `cas-model2-names.bst`: Elsevier CAS template assets.
- `doc/`: upstream template documentation.
- `Skills/write-ai-paper/`: evidence-grounded manuscript-writing instructions for AI agents.

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

Keep all manuscript sections in `main.tex`. Do not split the article into separate `sections/*.tex` files.
