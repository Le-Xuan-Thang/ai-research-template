---
name: nature-figure
description: Create, revise and audit publication figures in Python (matplotlib) for the manuscript in paper/main.tex. Use for any figure added to or changed in paper/figs/, and before delivering a figure. Trimmed copy of the upstream nature-figure skill (Python only, no R, no AI image generation, no bundled example figures).
---

# Figure making and QA (template copy of nature-figure)

Upstream: https://github.com/Yuan1z0825/nature-skills, `skills/nature-figure`, Apache-2.0
(see `LICENSE`, `NOTICE.md`, `UPSTREAM_COMMIT.txt`). This copy keeps the Python track and the
QA scripts. `../write-ai-paper/SKILL.md` remains the authority for manuscript text and captions.

## Changes relative to upstream

- Backend fixed to Python/matplotlib. No backend question, no R fragment.
- AI graphical-abstract and OpenRouter image routes removed. Do not generate figures with image models.
- Flagship-Nature and Nature Machine Intelligence layout rules removed. The manuscript uses the
  Elsevier CAS template; use the widths below and verify the target journal's guide for authors.
- The upstream `assets/` directory (34 MB of example figures, partly third-party material without a
  clear licence) is not included. Learn layout from the references; do not reuse upstream images.

## Requirements

Plotting needs `matplotlib`; the collision audit needs `pymupdf`. Add them when the project starts
making figures: `uv add matplotlib pymupdf`. The other audit scripts are dependency-free.

## Export contract

| Item | Default |
|---|---|
| Column widths | single 90 mm, 1.5 column 140 mm, double 190 mm (Elsevier artwork guide; verify) |
| Text at final size | 7 to 8 pt for body, ticks and legends; no glyph below 5 pt, including math sub/superscripts |
| Font | sans-serif (Arial/Helvetica/DejaVu Sans fallback), `pdf.fonttype 42` |
| Panel labels | lowercase bold `a`, `b`, ... near top-left, consistent across the paper |
| Export | vector PDF into `paper/figs/`; manifest with input and output SHA256 in the experiment record |
| Colour | one restrained palette per figure; no rainbow maps; legible in greyscale |
| Legends | outside the data area or as direct labels; never over data points or error bars |

## Workflow

1. Read `static/core/contract.md` and `static/core/stance.md` (about 2.7k tokens). Write the figure
   contract first: one-sentence core conclusion, panel roles, archetype.
2. For a multi-panel figure also read `references/multipanel-evidence-architecture.md`.
3. Put plotting code in `src/project/` (for example `src/project/analysis/paper_figures.py`), not only
   in a notebook. Figures must be generated from recorded experiment artifacts, never from numbers
   typed by hand. `static/fragments/backend/python.md` gives rcParams and an export helper.
4. Run QA from the repository root:

```bash
S=paper/Skills/nature-figure/scripts
uv run python -I $S/validate_figure.py src/project/analysis/paper_figures.py
uv run python -I $S/audit_pdf_text.py paper/figs/<fig>.pdf --min-pt 5
uv run python -I $S/audit_figure_collisions.py paper/figs/<fig>.pdf \
    --json-out <record>/<fig>.collision.json --overlay-pdf <record>/<fig>.collision-overlay.pdf
```

   For multi-panel figures call `require_matplotlib_panel_alignment(fig, ...)` from
   `scripts/audit_panel_alignment.py` after the final layout draw (tolerance 1.5 pt), with the
   scripts directory on `sys.path`.
5. Exit code 1 (`FIX BEFORE DELIVERY`) blocks delivery. `REVIEW REQUIRED` means inspect every WARN at
   final size and record why it is acceptable. Exit code 2 means the check could not run; do not claim
   it passed. Engineering drawings exported from CAD usually fail the collision audit by design
   (dimension lines cross dimension text); record them as accepted rather than editing them.
6. `validate_figure.py` also flags Nature conventions (SVG/TIFF export, `svg.fonttype`). For a PDF-only
   Elsevier submission record those as accepted deviations.
7. Render every page at final size and look at every panel; scripts do not replace inspection.
8. Record QA outputs under `experiments/<exp>/<dataset>/figure_qa_<date>_<nn>/`. Never overwrite an
   earlier QA record.

## References (load on demand, approximate token cost)

| File | Open when |
|---|---|
| `references/qa-contract.md` (6k) | before final delivery or a revision package |
| `references/design-theory.md` (4.5k) | typography, colour theory, export rationale |
| `references/api.md` (5k) | palette constants, helper signatures, alignment integration |
| `references/multipanel-evidence-architecture.md` (3k) | planning or auditing a multi-panel figure |
| `references/figure-contract.md` (1.4k) | turning a request into conclusion, evidence chain, panel map |
| `references/figure-legend-conventions.md` (1.3k) | writing or auditing captions |
| `references/common-patterns.md`, `references/chart-types.md`, `references/tutorials.md` | layout and chart recipes |
| `references/template-catalog.md` + `scripts/plot_templates.py` | CSV-driven ROC, paired, dot-plot templates |
| `references/asset-adaptation.md` | adapting existing plotting code to new data |

Upstream references may mention `nature-shared` journal files or R; those are not included and do
not apply. Each audit script supports `--self-test`.
