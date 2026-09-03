# Repository structure

[English](repository-structure.md) | [Tiếng Việt](../vi/repository-structure.md)

English is canonical if translations differ.

`ai-research-template` uses two intentionally different organizing axes for research inputs and outputs.

## The two organizing axes

Inputs are dataset-first:

```text
data/<dataset>/{raw,interim,processed}
```

Outputs are experiment-first:

```text
experiments/<experiment>/<dataset>/
```

This makes a dataset's provenance easy to inspect while keeping all evidence for one research question together. Cross-dataset results belong in `experiments/<experiment>/summary/`.

## Directory responsibilities

### `data/`

Each dataset is an independent research entity with its own README. `raw/` is immutable, `interim/` holds incomplete transformations, and `processed/` holds experiment-ready data. Payloads are ignored by Git; documentation and placeholders are tracked. This root contains actual data, unlike `src/project/data/`, which contains code.

### `notebooks/`

`exploration/<dataset>/` is for dataset-oriented inspection and hypotheses. `analysis/` is for cross-dataset or cross-experiment analysis, statistics, error analysis, and paper figures. Notebooks may be exploratory, but important reusable or result-critical logic must graduate to `src/`.

### `src/project/`

This is the importable Python package. Begin with small modules; split them only when real complexity warrants it. `project` is a placeholder package name and should be renamed for a real project.

### `configs/` and `experiments/`

`configs/` holds editable, reusable starting configurations grouped by dataset, model, and experiment. An experiment directory holds the immutable record of an actual run. Its `config.yaml` is a fully resolved snapshot, not merely a pointer to mutable shared configs. Dataset-specific results live below the experiment; comparisons live in `summary/`.

### `docs/`, `paper/`, `website/`, and `.agent/`

`docs/en/` is canonical human documentation and `docs/vi/` contains aligned translations. `paper/` is an Elsevier CAS LaTeX workspace: the complete article stays in one `main.tex`, figures live in `figs/`, and the local writing skill guides AI-assisted manuscript work. `website/` is a dependency-free project dashboard that summarizes canonical evidence without replacing it. `.agent/` contains current operational context and durable decisions, not transcripts or a second experiment history. `CHANGELOG.md` records notable project versions and updates.

## What belongs in Git

Track source, notebooks worth preserving, configs, dataset metadata, small metrics, tables, figures, experiment notes, and decisions. Normally exclude dataset payloads, checkpoints, generated tensors, very large logs, caches, environments, and temporary outputs. If a large artifact is essential, document its storage location and integrity checksum.
