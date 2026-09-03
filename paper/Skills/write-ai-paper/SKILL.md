---
name: write-ai-paper
description: Write, rewrite, and review AI and computer-vision research papers in academic English, including abstracts, introductions and literature synthesis, experimental setup, equations, results and discussion, LaTeX tables, citations, and BibTeX integrity. Use for evidence-grounded manuscript work; do not use to invent experiments, results, sources, or bibliographic metadata.
---

# Write AI Paper

Produce publication-ready scientific prose that is faithful to the supplied research evidence, internally consistent across manuscript sections, and compatible with LaTeX workflows.

## Core workflow

1. Identify the requested deliverable, target venue or style, available manuscript context, and evidence supplied by the user.
2. Read [General.md](General.md) for every writing, rewriting, or manuscript-review task.
3. Read only the task-specific guidance listed below. When a task spans multiple sections, read each applicable file and reconcile cross-section terminology, claims, numbers, notation, and citations.
4. Inspect the user's source material before drafting. Preserve verified technical facts and explicit stylistic constraints.
5. Draft or revise the requested content, then audit it for non-fabrication, claim strength, numerical consistency, terminology, acronym use, LaTeX correctness, and citation support.

## Task routing

- Abstract: read [Abstract.md](Abstract.md).
- Introduction, related-work synthesis, research gaps, or contribution statements: read [Introduction.md](Introduction.md).
- Experimental setup, datasets, implementation details, metrics, reproducibility, fairness, leakage, or statistical protocol: read [Experimental_Setup.md](Experimental_Setup.md).
- Results, discussion, ablations, comparisons, qualitative analysis, efficiency, or limitations: read [Results_and_discussion.md](Results_and_discussion.md).
- Equations, mathematical notation, symbols, or equation references: read [Equations.md](Equations.md).
- Literature verification, citation integrity, or BibTeX creation and cleanup: read [References.md](References.md).
- Formatting `tabular*` with `latexindent` or the documented TeXstudio table workaround: read [Tables.md](Tables.md).

## Evidence and missing information

Never invent scientific facts, experiments, datasets, methods, numerical values, statistical outcomes, citations, DOIs, or bibliographic fields. Distinguish clearly between supplied evidence, verified external evidence, interpretation, and proposed wording.

When essential information is missing, continue only where a useful and honest draft is possible. Use precise, conspicuous placeholders defined by the applicable guidance, or ask a focused question when the missing choice would materially change the scientific meaning. Do not silently convert assumptions into facts.

For literature-dependent work, verify newly introduced sources before citing them and keep citation claims aligned with what the source actually supports. Treat unverified bibliography entries as candidates, not evidence.

## Precedence and delivery

Follow the user's requested journal, template, language, word limit, and section structure. These explicit requirements override defaults in the reference files. Section-specific guidance overrides general guidance where they conflict.

Return only the requested deliverable unless the user asks for commentary, an audit, or alternatives. Preserve LaTeX commands, labels, citation keys, and mathematical notation unless changing them is part of the task. Briefly flag unresolved placeholders or evidence gaps after the deliverable.
