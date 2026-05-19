---
name: intake
description: Use when the plugin is invoked generally, repo phase routing is needed, or the workflow loop should start.
---

# Intake

Start and advance repo workflows by confirming authority, state, and phase.

## Read

Follow `../../docs/workflow-contracts/README.md`.

## Do

- Confirm git repo, branch, `git status --short`, and applicable `AGENTS.md` before mutation.
- When the user invokes the plugin generally, run the phase loop; do not stop at classification.
- Route to the narrowest phase: exploration, ideation, planning, goal-planning, execution, verification, review, handoff, or cleanup.
- Continue into the next phase when evidence, approval, and permissions are already sufficient.
- If continuation needs a later user turn, provide the exact next skill invocation prompt.
- Use root-thread `request_user_input` only for two or three material choices when supported; otherwise ask one direct question.
- Child agents never ask the user directly; they return `decision_needed`.

## Stop

Stop when repo, branch safety, instructions, mutation permission, or next phase is unclear.
