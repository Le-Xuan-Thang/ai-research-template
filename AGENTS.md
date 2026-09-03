# Agent operating guide

Before working:

1. Read `README.md`.
2. Read `.agent/state.md`.
3. Read `.agent/handoff.md` if it contains unfinished work.
4. Inspect relevant configs, experiments, dataset READMEs, and docs before changing code.

Repository rules:

- Put reusable research code in `src/project/`; keep exploratory work in `notebooks/`.
- Root `data/` stores data; `src/project/data/` stores data-loading and processing code.
- Treat `data/*/raw/` as immutable. Preserve dataset source, version, split, and preprocessing provenance.
- Do not leave reusable or result-critical logic exclusively in notebooks.
- Make important runs reproducible with configuration snapshots in experiment directories.
- Organize inputs as dataset then stage; organize outputs as experiment then dataset.
- Never overwrite historical experiment results by default. Create a new experiment or run record.
- Keep small metadata and conclusions in Git; keep large data, weights, logs, and generated artifacts out.
- Use English for code, configs, identifiers, comments, and agent files. Keep human docs aligned under `docs/en/` and `docs/vi/`.
- Prefer simple files and functions over speculative abstractions or production infrastructure.
- Prefer `uv` for Python version, environment, and dependency management when available. Keep `.python-version`, `pyproject.toml`, and `uv.lock` consistent; use standard `venv`/`pip` only as a fallback.
- Keep the complete Elsevier manuscript in `paper/main.tex`; do not split it into section files. Put publication figures in `paper/figs/`.
- Before writing or reviewing manuscript content, read `paper/Skills/write-ai-paper/SKILL.md`, its required `General.md`, and the routed task-specific guidance.
- Treat `website/` as a static evidence dashboard. Update it from canonical dataset, experiment, analysis, paper, and changelog records; do not maintain independent results there.
- Record notable project-level changes in `CHANGELOG.md` under `Unreleased`.

After meaningful work:

- Update `.agent/state.md` with the current objective, known facts, active work, and next action.
- Use `.agent/handoff.md` only for concrete unfinished continuation work; clear it when resolved.
- Record durable scientific or architectural decisions under `.agent/decisions/`.
- Note exact commands, seeds, inputs, and outputs in experiment notes when they affect reproducibility.
