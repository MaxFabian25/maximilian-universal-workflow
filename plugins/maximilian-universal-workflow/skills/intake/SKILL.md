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
- Route to the narrowest phase: exploration, ideation, planning, execution, verification, review, receiving-review, handoff, or cleanup.
- Continue into the next phase when evidence, approval, and permissions are already sufficient.
- If continuation needs a later user turn, provide the exact next skill invocation prompt.
- Call root-thread `request_user_input` liberally for routing, approval, ambiguity, and material choices.
- Child agents never ask the user directly; they return `decision_needed`.

## Stop

Stop when repo, branch safety, instructions, or next phase is unclear. Require mutation permission only before a mutating phase.
