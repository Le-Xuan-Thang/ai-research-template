# Decision 0002: Use uv, a single-file Elsevier manuscript, and a static dashboard

- **Status:** Accepted
- **Date:** 2026-09-03

## Context

The project needs reproducible Python environments, an Elsevier-ready publication workspace, and a visible overview of research progress without turning the repository into an application or deployment project.

## Decision

Prefer `uv` for Python installation, virtual environments, dependency resolution, and command execution, with standard Python tooling as a fallback. Pin Python through `.python-version` and commit `uv.lock` when real dependencies exist.

Use the existing Elsevier CAS assets in `paper/`. Keep the entire manuscript in one `paper/main.tex`, store publication figures in `paper/figs/`, and require AI agents to follow the local `write-ai-paper` skill for manuscript tasks.

Maintain a dependency-free static dashboard in `website/`. It summarizes canonical research evidence but does not own results. Track notable repository evolution in `CHANGELOG.md`.

## Consequences

Researchers get a fast, reproducible default environment, a journal-oriented writing path, and an accessible project overview. The repository remains usable without Node, a web framework, a hosted dashboard, or production infrastructure.
