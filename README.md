# Maximilian Universal Workflow

Maximilian Universal Workflow is a public Codex marketplace repository for the `maximilian-universal-workflow` plugin.

The plugin provides universal, phase-oriented, repeatable Codex-native workflows for git repository workspaces:

```text
intake -> exploration -> ideation -> planning -> execution -> verification -> review -> handoff
```

When the plugin is invoked generally, `intake` should start the loop and advance through later phases as far as the current request, repo evidence, approval, and permissions allow.

It also bundles `multi-agent-v2` as the canonical future copy for Codex native subagent coordination.

## Install

Add this repository as a Codex plugin marketplace, then install the plugin from that marketplace:

```bash
codex plugin marketplace add MaxFabian25/maximilian-universal-workflow --ref main
codex plugin add maximilian-universal-workflow@maximilian-universal-workflow
```

## Required Codex Config

This repository includes the runtime config the plugin expects at `.codex/config.toml`, plus the referenced agent role files under `.codex/agents/`.

Merge those settings into `$CODEX_HOME/config.toml` and copy the role files into `$CODEX_HOME/agents/` when setting up a Codex environment for this plugin. Do not replace personal machine paths, MCP servers, secrets, marketplace state, or unrelated local policy with the repository file.

The config enables the plugin's required native surfaces:

- `request_user_input` in Default mode
- `/goal`
- remote plugin installation
- skill/plugin mentions
- MultiAgentV2 with explicit root/subagent role boundaries
- `default`, `explorer`, and `worker` agent roles

To refresh after updates:

```bash
codex plugin marketplace upgrade maximilian-universal-workflow
codex plugin add maximilian-universal-workflow@maximilian-universal-workflow
```

## Skills

- `maximilian-universal-workflow:intake`
- `maximilian-universal-workflow:exploration`
- `maximilian-universal-workflow:ideation`
- `maximilian-universal-workflow:planning`
- `maximilian-universal-workflow:execution`
- `maximilian-universal-workflow:verification`
- `maximilian-universal-workflow:review`
- `maximilian-universal-workflow:receiving-review`
- `maximilian-universal-workflow:handoff`
- `maximilian-universal-workflow:repo-context-cleanup`
- `maximilian-universal-workflow:multi-agent-v2`

## Repository Layout

```text
.codex/config.toml
.codex/agents/
.agents/plugins/marketplace.json
plugins/maximilian-universal-workflow/
  .codex-plugin/plugin.json
  docs/workflow-contracts/
  skills/
```

## Workflow Contract

The plugin assumes the active workspace is a git repository. If repo mechanics are missing, establish a repository or worktree before using the phase workflows.

Subagents are encouraged:

- Use `explorer` for read-only repository investigation, critique, review, and evidence fanout.
- Use `worker` for explicitly owned, isolated write/execution tasks.
- Parent threads own user decisions, synthesis, integration, verification, review arbitration, and handoff.

`workflow-artifacts/` is a supporting evidence surface for plans, ledgers, reports, and handoffs, including optional interactive HTML for large workflow runs. Repo files, tests, branches, commits, and pull requests are the primary work surface.

## Development

Validate the marketplace and plugin metadata:

```bash
jq empty .agents/plugins/marketplace.json
jq empty plugins/maximilian-universal-workflow/.codex-plugin/plugin.json
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/maximilian-universal-workflow
```

When available, also run skill validation and Plugin Eval:

```bash
for skill in plugins/maximilian-universal-workflow/skills/*; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done

plugin-eval analyze plugins/maximilian-universal-workflow --format markdown
```
