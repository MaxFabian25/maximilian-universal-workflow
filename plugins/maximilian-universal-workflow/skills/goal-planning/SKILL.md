---
name: goal-planning
description: Use when /goal launch planning is needed.
---

# Goal Planning

Planning variant for goal-backed repo execution.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/goal-plan-structure.md`.

## Do

- Cite exploration; run `exploration` first if evidence is missing.
- Output `/goal ...`, execution prompt, ownership, verification, review, and handoff.
- Keep the objective durable, repo-scoped, verifiable, concise, and under 4,000 characters.
- Expect `goals = true`; if `/goal` is unavailable, output the same objective and execution prompt as a manual launch bundle.
- Say submit `/goal ...` first unless execution is explicitly asked to set the goal.
- Use `request_user_input` for replacement, budget, ownership, or execution choices.
- Do not call `create_goal` during planning; produce command and prompt text.

## Stop

Stop when evidence, approval, replacement, ownership, or verification is unresolved.
