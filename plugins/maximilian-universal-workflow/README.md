# Maximilian Universal Workflow

Maximilian Universal Workflow is a prose-first plugin for universal, phase-oriented, repeatable Codex-native workflows in git repository workspaces.

The default lifecycle is:

```text
intake -> exploration -> ideation -> planning or goal-planning -> execution/production -> verification -> review -> handoff
```

## Skills

- `intake`
- `exploration`
- `ideation`
- `planning`
- `goal-planning`
- `execution`
- `verification`
- `review`
- `handoff`
- `repo-context-cleanup`
- `multi-agent-v2`

## Repository Assumption

Assume the active workspace is a git repository. Start by reading applicable `AGENTS.md` files and checking branch/status before mutation. If no git repo or worktree is available, establish one or stop; this plugin does not model a non-repo work surface.

## Subagent Lanes

- Use `explorer` freely for read-only repository investigation, critique, review, and evidence fanout.
- Use `worker` freely for explicitly owned, isolated write/execution tasks.
- Child agents never ask the user directly; they return `decision_needed` to the parent.
- Use `multi-agent-v2` when the native subagent coordination mechanics, task paths, collection, recovery, or debugging are themselves the work.

## Goal Planning

Use `goal-planning` when the planning phase should produce a plan plus the next goal-backed execution prompt. The launch prompt starts with `/goal <execution objective>` and invokes `maximilian-universal-workflow:execution`; the goal describes the executed repo end state, not the planning task. Keep the `/goal` objective concise and put long instructions in the execution prompt body or a repo file.

## Artifacts

`./workflow-artifacts/YYYY-MM-DD-<slug>.html` is for supporting evidence, plans, ledgers, reports, and handoffs. Repo files, tests, branches, commits, and PRs are the primary work surface.

## Authority

Human-facing workflow authority lives in `docs/workflow-contracts/`. Skills are compact phase front doors into those contracts and their direct references.
