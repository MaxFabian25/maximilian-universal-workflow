# Lifecycle Playbook

Repeatable git-repo lifecycle:

`intake -> exploration -> ideation -> planning -> git-worktrees -> execution -> verification -> review -> handoff`

`repo-context-cleanup` supports any phase blocked by stale context.

`receiving-review` supports review feedback received from the user, a PR, CI, a reviewer, or another agent before execution or handoff continues.

`git-worktrees` owns the planning-to-execution branch-safety boundary, whether execution stays on the current branch or moves into an isolated worktree.

`multi-agent-v2` supports any phase that needs native subagent task-path coordination or debugging.

See `phase-runtime.md` for per-phase tool, evidence, exit, and next-phase rules.

## Routing

| Need | Skill |
| --- | --- |
| intake and repo state | `intake` |
| exploration and read-only fanout | `exploration` |
| ideation and implementation-path selection | `ideation` |
| planning downstream of exploration evidence and native goal setup | `planning` |
| isolated branch workspace before execution | `git-worktrees` |
| implementation, execution, creation, production | `execution` |
| fresh evidence and completion claims | `verification` |
| read-only review | `review` |
| triage received review feedback | `receiving-review` |
| status, branch/PR choices, operator handoff | `handoff` |
| stale context cleanup | `repo-context-cleanup` |
| subagent coordination mechanics and diagnostics | `multi-agent-v2` |

## Decisions

Use `request-user-input.md` for material decision gates, prompt shape, and stable decision ids.

## Goal-Backed Planning

`planning` outputs the plan first, then uses native goal tools. It compares active goal state to the planned objective with `get_goal`, resolves goal conflicts and proceed choices through `request_user_input`, and calls `create_goal` only when no current goal exists and proceed intent is clear.

## Phase Transitions

Use `phase-bundle.md` for shared handoff state and `phase-transition.md` for routing. Carry acceptance criteria from ideation and planning into execution, verification, review, and handoff.

## Worktree Isolation

Use `git-worktrees` after planning and before execution. It records explicit current-branch approval as `worktree_state.mode: current-branch`, or it owns worktree path selection, branch creation, setup, baseline verification, and the execution handoff bundle.

## Stop

Stop when repo target, branch safety, mutation permission, decision authority, verification, review scope, external permission, or closeout action is unclear.
