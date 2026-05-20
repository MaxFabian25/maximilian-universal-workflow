# Lifecycle Playbook

Repeatable git-repo lifecycle:

`intake -> exploration -> ideation -> planning -> execution -> verification -> review -> handoff`

`repo-context-cleanup` supports any phase blocked by stale context.

`receiving-review` supports review feedback received from the user, a PR, CI, a reviewer, or another agent before execution or handoff continues.

`multi-agent-v2` supports any phase that needs native subagent task-path coordination or debugging.

See `phase-runtime.md` for per-phase tool, evidence, exit, and next-phase rules.

## Routing

| Need | Skill |
| --- | --- |
| intake and repo state | `intake` |
| exploration and read-only fanout | `exploration` |
| ideation and branch selection | `ideation` |
| planning downstream of exploration evidence and native goal setup | `planning` |
| implementation, execution, creation, production | `execution` |
| fresh evidence and completion claims | `verification` |
| read-only review | `review` |
| triage received review feedback | `receiving-review` |
| status, branch/PR choices, operator handoff | `handoff` |
| stale context cleanup | `repo-context-cleanup` |
| subagent coordination mechanics and diagnostics | `multi-agent-v2` |

## Decisions

Use root-thread `request_user_input` liberally for material options, ambiguity, approvals, ownership, and closeout choices. Use `request-user-input.md` for the exact prompt shape.

## Goal-Backed Planning

`planning` outputs the plan first, then uses native goal tools. It compares active goal state to the planned objective with `get_goal`, resolves goal conflicts and proceed choices through `request_user_input`, and calls `create_goal` only when no current goal exists and proceed intent is clear.

## Phase Transitions

Use `phase-transition.md` for phase handoffs, stop payloads, and substantial workflow artifacts. Carry acceptance criteria from ideation and planning into execution, verification, review, and handoff.

## Stop

Stop when repo target, branch safety, mutation permission, decision authority, verification, review scope, external permission, or closeout action is unclear.
