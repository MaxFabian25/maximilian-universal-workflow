# Repository Instructions

This repository publishes the `maximilian-universal-workflow` Codex plugin as a Codex marketplace repository.

## Operating Model

- Treat git repository workspaces as the universal operating surface for this plugin.
- Prefer hard cutovers over compatibility aliases or legacy shims.
- Keep workflow authority in human-readable prose: `AGENTS.md`, `README.md`, `docs/workflow-contracts/`, skill `SKILL.md` files, and direct references.
- Use code only for deterministic mechanics such as validation, parsing, formatting, and reproducible checks.
- Do not trim capability, source-backed guidance, or subagent encouragement solely to reduce token cost.

## Plugin Layout

- Marketplace metadata lives at `.agents/plugins/marketplace.json`.
- The plugin root lives at `plugins/maximilian-universal-workflow/`.
- The required plugin manifest is `plugins/maximilian-universal-workflow/.codex-plugin/plugin.json`.
- Bundled skills live under `plugins/maximilian-universal-workflow/skills/`.

## Edit Rules

- Keep the plugin name `maximilian-universal-workflow` unless the user explicitly requests a breaking rename.
- Keep `multi-agent-v2` bundled as the canonical future copy.
- Keep `explorer` fanout encouraged for read-only investigation and review.
- Keep `worker` fanout encouraged for isolated execution ownership.
- Do not add non-git fallback parity language. If repo mechanics are missing, the workflow should establish a repo/worktree or stop.

## Validation

Before handoff, run the available deterministic checks:

- Validate `.agents/plugins/marketplace.json` and plugin JSON with `jq`.
- Run plugin validation against `plugins/maximilian-universal-workflow`.
- Run skill validation for every bundled skill when the local validator is available.
- Run Plugin Eval when available; budget warnings are acceptable if structural checks pass.
