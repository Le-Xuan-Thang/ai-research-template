# AI Research Template

**English** | [Tiếng Việt](README.vi.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg)](pyproject.toml)

`ai-research-template` is a lightweight, AI-friendly project template for reproducible, multi-dataset AI and machine learning research. It gives researchers and AI agents clear conventions for organizing datasets, notebooks, reusable code, configurations, experimental evidence, documentation, and papers.

Unlike a standard software or production ML template, it treats exploration and scientific traceability as first-class concerns. It intentionally avoids deployment, MLOps, and enterprise infrastructure.

## Why this template?

- Keep several datasets independent while studying one research question.
- Preserve the exact configuration and evidence behind every important result.
- Use notebooks freely without trapping reusable logic inside them.
- Let researchers and AI agents resume work from concise, durable context.
- Move naturally from data exploration to experiments, analysis, and an Elsevier manuscript.

## Core principles

The two fundamental filesystem rules are:

```text
data/                              experiments/
├── dataset_a/                     └── exp001_baseline/
│   ├── raw/                           ├── config.yaml
│   ├── interim/                       ├── dataset_a/
│   └── processed/                     ├── dataset_b/
└── dataset_b/                         └── summary/

dataset -> processing stage        experiment -> dataset -> result
```

Raw data is immutable. Cross-dataset tables, plots, and conclusions belong in an experiment's `summary/`. Reusable research logic belongs in `src/`, while dataset exploration and cross-experiment analysis remain first-class notebook workflows.

## Repository structure

```text
data/<dataset>/                  Dataset files and provenance by processing stage
notebooks/exploration/<dataset>/ Dataset inspection, visualization, and hypotheses
notebooks/analysis/              Cross-dataset and cross-experiment analysis
src/project/                     Reusable placeholder Python package
configs/                         Dataset, model, and experiment configurations
experiments/<experiment>/        Configuration snapshots and dataset-specific results
docs/{en,vi}/                    Canonical English docs and Vietnamese translations
paper/                           Single-file Elsevier CAS manuscript and figures
website/                         Dependency-free project dashboard
.agent/                          Current context, handoff, and durable decisions
```

See the detailed [repository structure](docs/en/repository-structure.md).

## Quick start

1. On GitHub, select **Use this template**, create your research repository, and clone it.
2. If [`uv`](https://docs.astral.sh/uv/) is available, prepare the pinned Python environment and install the project:

   ```bash
   uv python install
   uv sync
   uv run python -c "import project"
   ```

   Without `uv`, use the standard fallback:

   ```bash
   python -m venv .venv
   # Activate .venv for your shell, then:
   python -m pip install -e .
   ```

3. Rename `src/project/` to your package name. Update `[project].name` in `pyproject.toml`; src-layout discovery is already configured.
4. Replace the template description in `README.md` and define the current objective in `.agent/state.md`.
5. Register each dataset under `data/<dataset_name>/` and add its runtime config under `configs/datasets/`.
6. Explore datasets in `notebooks/exploration/<dataset_name>/`, moving reusable logic to `src/<project_package>/`.
7. Define model and experiment configs, then save each actual run under `experiments/<experiment_id>/` with a resolved `config.yaml` snapshot.

The package is imported as `project`, never `src.project`, until you rename it.

## Multi-dataset research

Each dataset owns its source, version, license, splits, preprocessing stages, and caveats in `data/<dataset>/README.md`. One experiment may evaluate the same hypothesis across several datasets; its per-dataset metrics remain together beneath the experiment, and its `summary/` holds comparable aggregate evidence.

The included `example_a`, `example_b`, and `exp001_baseline` are instructional metadata only. They contain no fake data or claimed results.

## Experiment workflow

Start from reusable files in `configs/`, resolve all critical settings, and snapshot the configuration beside the run. Store small metrics, notes, summaries, and provenance in Git; keep large datasets, checkpoints, tensors, and logs out of Git. Do not overwrite completed experiments—create a new, descriptive identifier such as `exp004_ablation_no_augmentation`.

See the full [research workflow](docs/en/research-workflow.md).

## AI agent workflow

Agents read [AGENTS.md](AGENTS.md), [.agent/state.md](.agent/state.md), and any active [.agent/handoff.md](.agent/handoff.md) before modifying research artifacts. Durable scientific or structural decisions belong in `.agent/decisions/`, not chat transcripts. Manuscript work additionally follows the local [`write-ai-paper` skill](paper/Skills/write-ai-paper/SKILL.md).

## Documentation

English is canonical for technical and machine-facing content. Vietnamese translations are available for human-facing documentation at aligned paths under `docs/vi/`. Code, configs, experiment identifiers, `AGENTS.md`, and `.agent/` are not duplicated by language.

- [Repository structure](docs/en/repository-structure.md)
- [Research workflow](docs/en/research-workflow.md)
- [Vietnamese documentation](docs/vi/repository-structure.md)
- [Project dashboard](website/index.html)
- [Changelog](CHANGELOG.md)

## Contributing

Focused improvements are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing structural changes, and keep contributions lightweight and research-oriented.

## Citation

If this template supports your research workflow, citation metadata is available in [CITATION.cff](CITATION.cff). Replace its repository-level metadata when creating a new project from this template.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details. Third-party Elsevier template assets under `paper/` retain their own copyright notices and terms.

