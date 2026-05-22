---
name: planning
description: Use when turning repo evidence into an executable plan with goal and worktree decisions.
---

# Planning

Turn an approved direction into an executable, goal-backed repo plan.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/request-user-input.md`, `../../docs/workflow-contracts/native-tool-map.md`, and `references/plan-structure.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- If repo evidence is missing, follow `exploration` first; cite fresh evidence when present.
- Do not plan from assumptions when evidence is discoverable.
- Update the shared phase bundle with goal, acceptance criteria, scope, files/areas, tasks, ownership, verification, review, handoff, and next phase.
- Use native goal tools under `references/plan-structure.md` Goal Tool Gates: call `get_goal`, compare the current objective to the planned execution objective, resolve conflicts with `request_user_input`, and call `create_goal` only when no current goal exists and the plan is decision-complete. Normal workflow invocation is goal setup intent unless the user asks for planning-only, no-goal, or stop-with-evidence.
- The goal objective describes the desired executed repo end state; keep it durable, repo-scoped, verifiable, concise, and under 4,000 characters.
- Put long execution detail in the execution prompt body or a repo file, not in the goal objective.
- Inspect repo conventions first.
- Use root-thread `request_user_input` for major planning tradeoffs, scope, ownership, and verification choices when there are 2-3 concrete options; otherwise proceed from approved evidence and plan constraints.
- Worker-suitable tasks must have non-overlapping mutable ownership.
- Decide whether execution is approved on the current branch or needs an isolated worktree, then route to `git-worktrees` either way so the branch-safety handoff is explicit.
- Apply `../../docs/workflow-contracts/artifact-floor.md` for supporting plans, evidence, ledgers, or handoff notes.
- If the user asked the plugin to carry the workflow forward, set `continue_now: yes` when approval, goal state, worktree state, and ownership are clear; otherwise provide the exact next prompt.

## Stop

Stop with a decision-ready payload when direction, ownership, active-goal conflict, proceed intent, or verification is unclear. Use native goal tools for goal setup.
