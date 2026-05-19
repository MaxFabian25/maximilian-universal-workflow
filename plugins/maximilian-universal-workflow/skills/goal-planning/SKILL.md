---
name: goal-planning
description: Use when planning should produce a goal-prefixed execution launch prompt.
---

# Goal Planning

Plan repo work, then produce the goal-prefixed execution launch prompt.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/goal-plan-structure.md`.

## Do

- Cite exploration; run `exploration` first if evidence is missing.
- Output the plan first, then a single next prompt that starts with `/goal <execution objective>` and invokes `maximilian-universal-workflow:execution`.
- The `/goal` objective describes the desired executed repo end state, not the planning task.
- Keep the objective durable, repo-scoped, verifiable, concise, and under 4,000 characters.
- Put long execution detail in the execution prompt body or a repo file, not in the `/goal` objective.
- Expect `goals = true`; if `/goal` is unavailable, output the same execution launch prompt without claiming goal setup.
- Use `request_user_input` for replacement, budget, ownership, or execution choices when supported; otherwise ask one direct question.
- Do not call `create_goal` during planning; produce the plan and launch prompt text.

## Stop

Stop when evidence, approval, replacement, ownership, or verification is unresolved.
