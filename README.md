# Maximilian Universal Workflow

Maximilian Universal Workflow is a public Codex marketplace repository for the `maximilian-universal-workflow` plugin.

The plugin provides universal, phase-oriented, repeatable Codex-native workflows for git repository workspaces. Each phase consumes and updates a shared phase bundle with repo state, objective, acceptance criteria, side effects, evidence, decisions, goal state, artifact state, and next phase:

```text
intake -> exploration -> ideation -> planning -> git-worktrees -> execution -> verification -> review -> handoff
```

When the plugin is invoked generally, `intake` should start the loop and advance through later phases as far as the current request, repo evidence, approval, and permissions allow.

## Install

Add this repository as a Codex plugin marketplace, then install the plugin from that marketplace:

```bash
codex plugin marketplace add MaxFabian25/maximilian-universal-workflow --ref main
codex plugin add maximilian-universal-workflow@maximilian-universal-workflow
```

## Environment Assumptions

The user's Codex environment owns tool and feature availability.

The workflow assumes the relevant native Codex surfaces are available when a phase asks for them, including goal tools, skill/plugin mentions, and operator input tools.

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
- `maximilian-universal-workflow:git-worktrees`
- `maximilian-universal-workflow:execution`
- `maximilian-universal-workflow:verification`
- `maximilian-universal-workflow:review`
- `maximilian-universal-workflow:receiving-review`
- `maximilian-universal-workflow:handoff`
- `maximilian-universal-workflow:repo-context-cleanup`

## Repository Layout

```text
.agents/plugins/marketplace.json
.codex-plugin/plugin.json
docs/workflow-contracts/
skills/
```

## Workflow Contract

The plugin assumes the active workspace is a git repository. If repo mechanics are missing, establish a repository or worktree before using the phase workflows, or stop.

`git-worktrees` creates isolated branch workspaces before substantial write-owning execution when current-branch mutation is not approved. `workflow-artifacts/` is a supporting evidence surface for plans, ledgers, reports, handoffs, and standalone interactive HTML dashboards for substantial workflow runs. Repo files, tests, branches, commits, and pull requests are the primary work surface.

## Development

Validate the marketplace and plugin metadata:

```bash
jq empty .agents/plugins/marketplace.json
jq empty .codex-plugin/plugin.json
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Run skill validation and Plugin Eval when those local tools are available; Plugin Eval budget warnings are acceptable if structural checks pass:

```bash
for skill in skills/*; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done

plugin-eval analyze . --format markdown
```

Run the Plugin Eval Scenario Suite benchmark gate when changing workflow guidance that may affect token use or routing behavior:

```bash
scripts/run_benchmark_gate.sh
```

See `docs/benchmark-gate.md` for thresholds, observed-usage analysis, and expected benchmark artifacts. Benchmark gate files live beside the plugin source and are development support, not runtime workflow authority.
