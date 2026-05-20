---
name: planning
description: Use when repo planning is needed, including native goal-backed execution setup.
---

# Planning

Turn an approved direction into an executable, goal-backed repo plan.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/plan-structure.md`.

## Do

- If repo evidence is missing, follow `exploration` first; cite fresh evidence when present.
- Do not plan from assumptions when evidence is discoverable.
- State goal, acceptance criteria, scope, files/areas, tasks, ownership, verification, review, handoff, and phase-transition packet.
- Use native goal tools: call `get_goal`, compare the current objective to the planned execution objective, resolve conflicts with `request_user_input`, and call `create_goal` only when no current goal exists and proceed intent is clear.
- The goal objective describes the desired executed repo end state; keep it durable, repo-scoped, verifiable, concise, and under 4,000 characters.
- Put long execution detail in the execution prompt body or a repo file, not in the goal objective.
- Inspect repo conventions first.
- Use root-thread `request_user_input` liberally for major planning tradeoffs, scope, ownership, and verification choices.
- Worker-suitable tasks must have non-overlapping mutable ownership.
- Use `workflow-artifacts/` only for supporting plans, evidence, ledgers, or handoff notes.
- If the user asked the plugin to carry the workflow forward, continue to execution when approval and ownership are clear; otherwise provide the exact next prompt.

## Stop

Stop with a decision-ready payload when direction, ownership, active-goal conflict, proceed intent, or verification is unclear. Use native goal tools for goal setup.
