# Repository Instructions

This repository publishes the `maximilian-universal-workflow` Codex plugin as a Codex marketplace repository.

## Operating Model

- Treat git repository workspaces as the universal operating surface for this plugin.
- Prefer hard cutovers over compatibility aliases or legacy shims.
- Keep workflow authority in human-readable prose: `AGENTS.md`, `README.md`, `docs/workflow-contracts/`, skill `SKILL.md` files, and direct references.
- Use code only for deterministic mechanics such as validation, parsing, formatting, and reproducible checks.
- Do not trim capability or source-backed guidance solely to reduce token cost.

## Plugin Layout

- Marketplace metadata lives at `.agents/plugins/marketplace.json`.
- The repository root is the plugin root.
- The required plugin manifest is `.codex-plugin/plugin.json`.
- Bundled skills live under `skills/`.

## Edit Rules

- Keep the plugin name `maximilian-universal-workflow` unless the user explicitly requests a breaking rename.
- Do not bundle plugin-owned delegation skills, role files, runtime hint blocks, or packet templates; rely on Codex CLI's built-in model instructions.
- Do not add non-git fallback parity language. If repo mechanics are missing, the workflow should establish a repo/worktree or stop.

## Validation

Before handoff, run the available deterministic checks:

- Validate `.agents/plugins/marketplace.json` and plugin JSON with `jq`.
- Run plugin validation against the repository root.
- Run skill validation for every bundled skill when the local validator is available.
- Run Plugin Eval when available; budget warnings are acceptable if structural checks pass.
