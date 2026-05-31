# Maximilian Universal Workflow

Maximilian Universal Workflow is a prose-first plugin for universal, phase-oriented, repeatable Codex-native workflows in git repository workspaces.

The default lifecycle is:

```text
intake -> exploration -> ideation -> planning -> git-worktrees -> execution -> verification -> review -> handoff
```

## Skills

- `intake`
- `exploration`
- `ideation`
- `planning`
- `git-worktrees`
- `execution`
- `verification`
- `review`
- `receiving-review`
- `handoff`
- `repo-context-cleanup`
- `multi-agent-v2`

## Repository Assumption

Assume the active workspace is a git repository. Start by reading applicable `AGENTS.md` files and checking branch/status before mutation. If no git repo or worktree is present, establish one or stop; this plugin does not model a non-repo work surface.

## Runtime Config

The marketplace/source repository root includes `.codex/config.toml` and `.codex/agents/*.toml` as the required Codex runtime config for this plugin. In an installed marketplace checkout, those files live beside `.agents/plugins/marketplace.json`, not inside this plugin package directory. Merge those settings into `$CODEX_HOME/config.toml` and copy the role files into `$CODEX_HOME/agents/` when setting up a Codex environment. Keep machine-local paths, MCP servers, secrets, marketplaces, and unrelated policy in the operator's own config.

## Subagent Lanes

- Use `explorer` when read-only repository investigation, critique, review, or evidence fanout is independent enough to improve confidence or speed.
- Use `worker` when write/execution tasks have explicitly owned, non-overlapping mutable scope.
- Child agents never ask the user directly; they return `decision_needed` to the parent.
- Use `multi-agent-v2` when the native subagent coordination mechanics, task paths, collection, recovery, or debugging are themselves the work.

## Review Reception

Use `receiving-review` when review feedback, PR comments, reviewer findings, CI review notes, or user critique arrives and must be triaged before changes. Verify each item against repo evidence before fixing, pushing back, or escalating.

## Goal-Backed Planning

Use `planning` for repo plans and native goal-backed execution setup. Planning inspects active goal state, resolves active-goal conflicts and proceed choices with `request_user_input`, and creates the goal only when no current goal exists and proceed intent is clear.

## Worktree Isolation

Use `git-worktrees` before substantial write-owning execution when the current branch has not been approved for mutation. It creates an isolated branch workspace, runs setup and baseline verification, then hands off to `execution`.

## Artifacts

`./workflow-artifacts/YYYY-MM-DD-<slug>.html` is for supporting evidence, plans, ledgers, reports, handoffs, and standalone interactive HTML dashboards for substantial runs. Repo files, tests, branches, commits, and PRs are the primary work surface.

## Authority

Human-facing workflow authority lives in `docs/workflow-contracts/`. Skills are compact phase front doors into those contracts and their direct references. Use `phase-bundle.md` for shared handoff state, `phase-transition.md` for routing, `request-user-input.md` for decisions, and `html-artifact-template.md` for substantial support artifacts.
