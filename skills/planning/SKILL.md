---
name: planning
description: Use when turning repo evidence into an executable plan with goal and worktree decisions.
---

# Planning

Turn an approved direction into an executable, goal-backed repo plan.

## Read

Read `../../docs/workflow-contracts/phase-core.md` and `references/plan-structure.md`. Use other workflow-contract files only when the core or local reference requires deeper authority.

## Do

- If repo evidence is missing, follow `exploration` first; cite fresh evidence when present.
- Do not plan from assumptions when evidence is discoverable.
- Update the phase bundle with goal, acceptance criteria, scope, files/areas, tasks, ownership, worktree decision, proof surface, verification, review, handoff, and next phase.
- Follow `references/plan-structure.md` for required payload and Goal Tool Gates.
- Use this workflow's explicit default goal-backed planning unless the user asks for planning-only, no-goal, or stop-with-evidence. Keep the goal objective durable, repo-scoped, verifiable, concise, and under 4,000 characters.
- Inspect repo conventions and use root-thread `request_user_input` for material tradeoffs, scope, ownership, active-goal, proof-surface, and verification choices when 2-3 concrete options remain.
- Use Codex-native subagents to check substantial task decomposition, ownership conflicts, or proof-surface adequacy when that improves plan quality.
- Worker-suitable tasks must have non-overlapping mutable ownership.
- Decide current-branch approval versus isolated worktree, route to `git-worktrees`, and apply `../../docs/workflow-contracts/artifact-floor.md` for support artifacts.
- Set `continue_now: yes` only when approval, goal state, worktree state, and ownership are clear; otherwise give the exact next prompt.

## Stop

Stop with a decision-ready payload when direction, ownership, active-goal conflict, planning mode, or verification is unclear.
