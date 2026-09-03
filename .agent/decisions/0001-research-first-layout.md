# Decision 0001: Use a research-first, multi-dataset layout

- **Status:** Accepted
- **Date:** 2026-09-03

## Context

The template must support one research question evaluated across two or more datasets while remaining usable without deployment or experiment-tracking infrastructure.

## Decision

Organize input data as `data/<dataset>/<stage>` and research outputs as `experiments/<experiment>/<dataset>`. Keep cross-dataset synthesis in each experiment's `summary/`, reusable code in a src-layout package, exploration in notebooks, and exact run configuration snapshots beside results.

## Consequences

Dataset provenance and experiment evidence have distinct, obvious homes. Historical results remain interpretable when shared configs change. The repository favors transparent filesystem conventions over production abstractions or external platforms.

