---
name: planning
description: Use when repo planning is needed, including default goal-backed execution launch prompts.
---

# Planning

Turn an approved direction into an executable, goal-backed repo plan.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/plan-structure.md`.

## Do

- If repo evidence is missing, follow `exploration` first; cite fresh evidence when present.
- Do not plan from assumptions when evidence is discoverable.
- State goal, scope, files/areas, tasks, ownership, verification, handoff.
- Output the plan first, then a single next prompt that starts with `/goal <execution objective>` and invokes `maximilian-universal-workflow:execution`.
- The `/goal` objective describes the desired executed repo end state; keep it durable, repo-scoped, verifiable, concise, and under 4,000 characters.
- Put long execution detail in the execution prompt body or a repo file, not in the `/goal` objective.
- Use `get_goal` when current goal state matters. When the plan is complete and no replacement choice is unresolved, call `create_goal` if the native tool is available and the user intent is to proceed.
- Inspect repo conventions first.
- Use root-thread `request_user_input` liberally for major planning tradeoffs, scope, ownership, and verification choices.
- Worker-suitable tasks must have non-overlapping mutable ownership.
- Use `workflow-artifacts/` only for supporting plans, evidence, ledgers, or handoff notes.
- If the user asked the plugin to carry the workflow forward, continue to execution when approval and ownership are clear; otherwise provide the exact next prompt.

## Stop

Stop when direction, ownership, goal replacement, or verification is unclear.
