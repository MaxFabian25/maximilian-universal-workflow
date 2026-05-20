# Lifecycle Playbook

Repeatable git-repo lifecycle:

`intake -> exploration -> ideation -> planning -> execution/production -> verification -> review -> handoff`

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
| planning downstream of exploration evidence and `/goal` launch | `planning` |
| implementation, execution, creation, production | `execution` |
| fresh evidence and completion claims | `verification` |
| read-only review | `review` |
| triage received review feedback | `receiving-review` |
| status, branch/PR choices, operator handoff | `handoff` |
| stale context cleanup | `repo-context-cleanup` |
| subagent coordination mechanics and diagnostics | `multi-agent-v2` |

## Decisions

Use root-thread `request_user_input` liberally for material options, ambiguity, approvals, ownership, and closeout choices.

## Goal-Backed Planning

`planning` outputs the plan first, then a self-contained next prompt that starts with `/goal <execution objective>` and invokes `maximilian-universal-workflow:execution`. When native goal tools are available and user intent is clear, `planning` may create the goal after the plan is complete.

## Stop

Stop when repo target, branch safety, mutation permission, decision authority, verification, review scope, external permission, or closeout action is unclear.
