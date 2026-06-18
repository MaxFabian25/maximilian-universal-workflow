# Harness Boundary

Maximilian Universal Workflow is a universal git-repository phase harness, not a global session router or a software-only workflow pack.

## Owns

Intake, repo state checks, exploration, ideation, goal-backed planning, git worktree isolation, execution, verification, read-only review, review feedback reception, handoff, branch/PR/merge/keep choices, evidence summaries, proof-surface discipline, diagnosis loops, proof-first change, information structure, decision interrogation, vocabulary and decision capture, question-first scratch-work disposition, work-item shaping, Codex-native subagent coordination, and stale context cleanup.

## Does Not Own

Domain execution owned by a narrower skill/tool/process, strict software-only TDD, issue-tracker state machines, visual architecture scanners, skill-authoring doctrine, teaching workflows, work without an established repo/worktree, or hidden code-policy authority.

## Narrower Skills

When a narrower skill, tool, or repo-local process applies, use it for domain procedure, data handling, external-system rules, and specialized validation. This workflow still owns repository lifecycle mechanics: repo state, phase routing, decision gates, worktree and goal coordination, information-structure placement, evidence capture, verification routing, review arbitration, and handoff.

If a narrower skill requires stricter safety, evidence, approval, or verification than this harness, follow the stricter requirement and record it in `allowed_side_effects`, `evidence`, or `decision_gate`. If the narrower skill conflicts with repo instructions or an explicit user decision, use `request_user_input` when available; return `decision_needed` only when the tool is unavailable or the active workflow phase cannot own the choice.

## Human Decisions

The running agent that has `request_user_input` available owns operator-facing decisions for its assigned task. Return unresolved choices as `decision_needed` only when the tool is unavailable or the active workflow phase cannot own the choice.
