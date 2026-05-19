---
name: intake
description: Use when repo phase routing is needed.
---

# Intake

Start repo workflows by confirming authority, state, phase.

## Read

Follow `../../docs/workflow-contracts/README.md`.

## Do

- Confirm git repo, branch, `git status --short`, and applicable `AGENTS.md` before mutation.
- Route to the narrowest phase: exploration, ideation, planning, goal-planning, execution, verification, review, handoff, or cleanup.
- Use root-thread `request_user_input` only for two or three material choices.
- Child agents never ask the user directly; they return `decision_needed`.

## Stop

Stop when repo, branch safety, instructions, mutation permission, or next phase is unclear.
