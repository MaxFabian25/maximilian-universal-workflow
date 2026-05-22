# Maximilian Universal Workflow

Maximilian Universal Workflow is an outcome-first, prose-first plugin for repeatable Codex-native workflows in git repository workspaces.

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
- Default to no subagents for narrow single-thread work and 1-3 subagents for ordinary fanout. Exceed 3 only when the task naturally partitions and the parent can synthesize bounded summaries.
- Before spawning, name the reason for fanout, expected output, ownership boundary, and collection point.
- Child agents never ask the user directly; they return `decision_needed` to the parent.
- Use `multi-agent-v2` when the native subagent coordination mechanics, task paths, collection, recovery, or debugging are themselves the work.

## Review Reception

Use `receiving-review` when review feedback, PR comments, reviewer findings, CI review notes, or user critique arrives and must be triaged before changes. Verify each item against repo evidence before fixing, pushing back, or escalating.

## Goal-Backed Planning

Use `planning` for repo plans and default native goal-backed execution setup. Planning inspects active goal state, resolves active-goal conflicts with `request_user_input`, and creates the goal when no current goal exists after the plan is decision-complete. A normal workflow invocation is enough goal setup intent unless the user explicitly asks for planning-only, no-goal, or stop-with-evidence behavior.

## Worktree Isolation

Use `git-worktrees` after planning and before write-owning execution. It records explicit current-branch approval or creates an isolated branch workspace, runs setup and baseline verification, then hands off to `execution`.

## Artifacts

`artifact-floor.md` owns `workflow-artifacts/` policy and exceptions. Default durable support artifacts use `./workflow-artifacts/YYYY-MM-DD-<slug>.html`; source files, tests, docs, branches, commits, and PRs remain primary.

Prefer HTML over Markdown for durable workflow support artifacts unless repo instructions or the user explicitly require another format.

## Authority

Human-facing workflow authority lives in `docs/workflow-contracts/`. Skills are compact phase front doors into those contracts and their direct references. Use `phase-bundle.md` for shared handoff state, `phase-transition.md` for routing, `request-user-input.md` for decisions, `artifact-floor.md` for artifact policy, and `html-artifact-template.md` for HTML artifact shape.
