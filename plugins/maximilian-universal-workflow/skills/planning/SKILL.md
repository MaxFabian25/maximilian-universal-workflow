---
name: planning
description: Use when repo planning is needed.
---

# Planning

Turn an approved direction into an executable repo plan.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/plan-structure.md`.

## Do

- If repo evidence is missing, follow `exploration` first; cite fresh evidence when present.
- Do not plan from assumptions when evidence is discoverable.
- Route to `goal-planning` when planning should output a goal-prefixed execution prompt.
- State goal, scope, files/areas, tasks, ownership, verification, handoff.
- Inspect repo conventions first.
- Use `request_user_input` for two or three major planning tradeoffs.
- Worker-suitable tasks must have non-overlapping mutable ownership.
- Use `workflow-artifacts/` only for supporting plans, evidence, ledgers, or handoff notes.
- If the user asked the plugin to carry the workflow forward, continue to execution when approval and ownership are clear; otherwise provide the exact next prompt.

## Stop

Stop when direction, ownership, or verification is unclear.
