# Lifecycle Playbook

Repeatable git-repo lifecycle:

`intake -> exploration -> ideation -> planning or goal-planning -> execution/production -> verification -> review -> handoff`

`repo-context-cleanup` supports any phase blocked by stale context.

`multi-agent-v2` supports any phase that needs native subagent task-path coordination or debugging.

See `phase-runtime.md` for per-phase tool, evidence, exit, and next-phase rules.

## Routing

| Need | Skill |
| --- | --- |
| intake and repo state | `intake` |
| exploration and read-only fanout | `exploration` |
| ideation and branch selection | `ideation` |
| planning downstream of exploration evidence | `planning` |
| planning that should launch `/goal` before execution | `goal-planning` |
| implementation, execution, creation, production | `execution` |
| fresh evidence and completion claims | `verification` |
| read-only review | `review` |
| status, branch/PR choices, operator handoff | `handoff` |
| stale context cleanup | `repo-context-cleanup` |
| subagent coordination mechanics and diagnostics | `multi-agent-v2` |

## Decisions

Use root-thread `request_user_input` for two or three material options. Otherwise ask one concise question.

## Goal Planning

`goal-planning` outputs `/goal ...` first, then a self-contained `execution` invocation carrying the same objective.

## Stop

Stop when repo target, branch safety, mutation permission, decision authority, verification, review scope, external permission, or closeout action is unclear.
