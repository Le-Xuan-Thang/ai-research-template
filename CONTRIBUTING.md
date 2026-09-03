# Contributing

Contributions that make `ai-research-template` clearer, more reproducible, or easier to reuse are welcome.

Before proposing a change:

1. Open an issue for substantial structural changes so the research workflow can be discussed first.
2. Keep changes research-first and lightweight. Avoid production, deployment, MLOps, and enterprise infrastructure unless it directly supports the template's stated scope.
3. Preserve the core conventions: data is organized as dataset then processing stage; outputs are organized as experiment then dataset then result.
4. Keep reusable research logic in `src/`, exploratory work in notebooks, and historical experiment configurations/results intact.
5. Write code, configs, identifiers, `AGENTS.md`, and `.agent/` files in English.
6. Treat English human documentation as canonical and update the aligned Vietnamese translation when practical.
7. Add notable user-facing changes to `CHANGELOG.md` under `Unreleased`.

Keep pull requests focused. Explain the research use case, list the affected conventions, and include proportionate validation such as link checks, package imports, or deterministic utility tests.

