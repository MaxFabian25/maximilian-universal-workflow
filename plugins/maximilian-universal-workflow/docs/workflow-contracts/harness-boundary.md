# Harness Boundary

Maximilian Universal Workflow is a universal git-repository phase harness, not a global session router.

## Owns

Intake, repo state checks, exploration, ideation, goal-backed planning, execution, worker dispatch, verification, read-only review, review feedback reception, handoff, branch/PR/merge/keep choices, evidence summaries, and stale context cleanup.

## Does Not Own

Domain execution owned by a narrower skill/tool/process, work without an established repo/worktree, child-agent user decisions, or hidden code-policy authority.

## Human Decisions

The root thread owns user-facing decisions. Child agents and drafting passes return unresolved choices to the parent as `decision_needed`.

## Subagent Roles

The fanout parent owns bounded `wait_agent`, `list_agents`, `followup_task`, `close_agent`, synthesis, and arbitration. Stuck leaves are closed and reported as partial evidence. Spawned explorers/workers are leaves unless explicitly assigned descendants.
