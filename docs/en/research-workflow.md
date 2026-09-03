# Research workflow

[English](research-workflow.md) | [Tiếng Việt](../vi/research-workflow.md)

English is canonical if translations differ.

This workflow is the default path for research projects created from `ai-research-template`.

## 1. Frame the question and register datasets

Write a concrete research question. For every dataset, create `data/<dataset>/README.md` with source, citation, license, version, acquisition steps, layout, split policy, preprocessing, and caveats. Never modify raw data in place.

## 2. Explore, then consolidate

Use `notebooks/exploration/<dataset>/` for inspection and fast hypotheses. Keep notebooks readable and record the inputs they used. When loading, preprocessing, models, metrics, or plotting logic is reused—or affects scientific validity—move it into `src/project/` and import it from notebooks.

## 3. Configure the experiment

Keep reusable fragments under `configs/datasets/`, `configs/models/`, and `configs/experiments/`. Critical settings should be recoverable: seed, datasets and versions, splits, model, optimizer, learning rate, batch size, epochs, augmentation, and evaluation protocol.

Before execution, create `experiments/expNNN_name/` and save the fully resolved settings to its `config.yaml`. A later edit to shared configs must not change the meaning of an old result.

Use `uv` when available: `.python-version` pins the intended Python line, `pyproject.toml` declares dependencies, and `uv.lock` should be committed once real dependencies exist. Run research commands with `uv run` so they use the resolved environment.

## 4. Run across datasets

Write outputs to `experiments/<experiment>/<dataset>/`. Save small structured metrics and useful metadata in Git. Keep large checkpoints and logs out of Git, but state how to locate or regenerate them. Record failed or partial runs honestly rather than silently replacing them.

Use deterministic seeds where meaningful, record software/hardware details that materially affect the result, and define metric aggregation and uncertainty. Do not compare datasets using incompatible protocols without labeling the difference.

## 5. Synthesize and publish

Put cross-dataset tables, plots, and conclusions in `experiments/<experiment>/summary/`. Use `notebooks/analysis/` for comparisons, ablations, error analysis, statistics, and figure generation. Publication-ready material can then flow into `paper/figs/` and the single `paper/main.tex` while retaining links to its experiment and configuration. AI agents must follow `paper/Skills/write-ai-paper/SKILL.md` for manuscript tasks.

Update `website/` with verified highlights, results, and milestones. It is a presentation layer: canonical values remain in experiment records and analysis outputs. Record notable repository changes in `CHANGELOG.md`.

## 6. Preserve continuity

Update `.agent/state.md` after meaningful work. Use `.agent/handoff.md` only when another session needs concrete continuation instructions. Record durable choices—such as a split protocol or metric definition—in `.agent/decisions/`. Experiment notes and Git remain the historical record.
