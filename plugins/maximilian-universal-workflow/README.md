# Maximilian Universal Workflow

Maximilian Universal Workflow is a prose-first plugin for universal, phase-oriented, repeatable Codex-native workflows in git repository workspaces.

The default lifecycle is:

```text
intake -> exploration -> ideation -> planning -> execution/production -> verification -> review -> handoff
```

## Skills

- `intake`
- `exploration`
- `ideation`
- `planning`
- `execution`
- `verification`
- `review`
- `receiving-review`
- `handoff`
- `repo-context-cleanup`
- `multi-agent-v2`

## Repository Assumption

Assume the active workspace is a git repository. Start by reading applicable `AGENTS.md` files and checking branch/status before mutation. If no git repo or worktree is available, establish one or stop; this plugin does not model a non-repo work surface.

## Runtime Config

The public repository includes `.codex/config.toml` and `.codex/agents/*.toml` as the required Codex runtime config for this plugin. Merge those settings into `$CODEX_HOME/config.toml` and copy the role files into `$CODEX_HOME/agents/` when setting up a Codex environment. Keep machine-local paths, MCP servers, secrets, marketplaces, and unrelated policy in the operator's own config.

## Subagent Lanes

- Use `explorer` freely for read-only repository investigation, critique, review, and evidence fanout.
- Use `worker` freely for explicitly owned, isolated write/execution tasks.
- Child agents never ask the user directly; they return `decision_needed` to the parent.
- Use `multi-agent-v2` when the native subagent coordination mechanics, task paths, collection, recovery, or debugging are themselves the work.

## Review Reception

Use `receiving-review` when review feedback, PR comments, reviewer findings, CI review notes, or user critique arrives and must be triaged before changes. Verify each item against repo evidence before fixing, pushing back, or escalating.

## Goal-Backed Planning

Use `planning` for repo plans and the default goal-backed execution launch. The launch prompt starts with `/goal <execution objective>` and invokes `maximilian-universal-workflow:execution`; the goal describes the executed repo end state. Keep the `/goal` objective concise and put long instructions in the execution prompt body or a repo file. When native goal tools are available and the plan is complete, planning may create the goal directly.

## Artifacts

`./workflow-artifacts/YYYY-MM-DD-<slug>.html` is for supporting evidence, plans, ledgers, reports, and handoffs. Repo files, tests, branches, commits, and PRs are the primary work surface.

## Authority

Human-facing workflow authority lives in `docs/workflow-contracts/`. Skills are compact phase front doors into those contracts and their direct references.
