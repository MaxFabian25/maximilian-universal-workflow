# Harness Boundary

Maximilian Universal Workflow is a universal git-repository phase harness, not a global session router.

## Owns

Intake, repo state checks, exploration, ideation, goal-backed planning, git worktree isolation, execution, worker dispatch, verification, read-only review, review feedback reception, handoff, branch/PR/merge/keep choices, evidence summaries, and stale context cleanup.

## Does Not Own

Domain execution owned by a narrower skill/tool/process, work without an established repo/worktree, or hidden code-policy authority.

## Narrower Skills

When a narrower skill, tool, or repo-local process applies, use it for domain procedure, data handling, external-system rules, and artifact-specific validation. This workflow still owns repository lifecycle mechanics: repo state, phase routing, decision gates, worktree and goal coordination, evidence capture, verification routing, review arbitration, and handoff.

If a narrower skill requires stricter safety, evidence, approval, or verification than this harness, follow the stricter requirement and record it in `allowed_side_effects`, `evidence`, or `decision_gate`. If the narrower skill conflicts with repo instructions or an explicit user decision, use `request_user_input` when available; return `decision_needed` only when the tool is unavailable, the parent owns the choice, or sibling synthesis must happen first.

## Human Decisions

The running agent that has `request_user_input` available owns operator-facing decisions for its assigned task. Spawned children return unresolved choices to the parent as `decision_needed` only when the tool is unavailable, the packet explicitly assigns the choice to the parent, or sibling synthesis must happen first.

## Subagent Roles

The fanout parent owns bounded `wait_agent`, `list_agents`, `followup_task`, `close_agent`, synthesis, and arbitration. Stuck leaves are closed and reported as partial evidence. Spawned explorers/workers are leaves unless explicitly assigned descendants.
