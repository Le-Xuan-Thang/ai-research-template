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

## Before the session ends: hand off

A session can end without warning — quota exhaustion, context compaction, a timeout, or the user
closing it. **Nothing that lives only in the conversation survives.** The `.agent/` directory is the
only channel through which the next agent inherits your work.

**Write the handoff before you need it, not when you notice you are running out.** By the time
context or quota is nearly exhausted there may not be enough budget left to write a good one. Treat
the handoff as due whenever any of these is true:

- you are past roughly two thirds of your context or quota;
- you started something long-running (a training run, a background job) that will outlive you;
- you are about to begin a step that could consume a large amount of budget;
- the user has been idle and the session may be closed at any moment.
- the user asks you to hand off, switch agents, pause, stop, or end the session.

If the user requests a handoff or asks another agent to continue, update
`.agent/handoff.md` before ending your response, unless there is no unfinished work.

Update `.agent/handoff.md` so that an agent with **no memory of this conversation** can resume
without re-deriving anything. It must answer:

1. **Objective** — what is being attempted, in one or two sentences.
2. **Completed** — what is actually done, each item with the evidence that proves it (a test result,
   a file path, a recorded metric). Never write "done" for something you did not verify.
3. **In flight** — anything running right now: the command, the PID, the log path, where its outputs
   land, how to tell whether it is still alive, and how to check its progress. A background run
   nobody knows how to find is a lost run.
4. **Blockers and open questions** — including decisions you deliberately left to the user.
5. **Modified files** — what changed and why, so the next agent does not undo it.
6. **Verification already performed** — the exact commands and their results, so they are not
   repeated needlessly or wrongly assumed.
7. **Next safe command** — the single concrete thing to run next, copy-pasteable.

Also record what you did **not** do and why. An unstated gap is read as completed work, and that is
how a wrong number reaches a paper.

Durable facts belong in `state.md` (current state of the research) or `decisions/` (choices that
stay true regardless of who is working). `handoff.md` holds only the continuation of unfinished
work; clear it once the work is resolved.

If a long-running job is still executing when you hand off, `state.md` must also say so, so the next
agent does not launch a duplicate.
