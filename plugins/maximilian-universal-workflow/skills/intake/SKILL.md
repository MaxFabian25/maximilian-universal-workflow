---
name: intake
description: Use when starting the repo workflow loop, routing phases, and opening material decisions.
---

# Intake

Start and advance repo workflows by confirming authority, state, and phase.

## Read

Follow `../../docs/workflow-contracts/README.md`.

## Do

- Confirm git repo, branch, `git status --short`, and applicable `AGENTS.md` before mutation.
- When the user invokes the plugin generally, run the phase loop; do not stop at classification.
- Route to the narrowest phase: exploration, ideation, planning, execution, verification, review, receiving-review, handoff, or cleanup.
- Create or update the shared phase bundle with repo state, objective, acceptance criteria if known, allowed side effects, evidence, chosen phase, and open decisions.
- Continue into the next phase when evidence, approval, and permissions are already sufficient.
- If continuation needs a later user turn, provide the exact next skill invocation prompt.
- Call root-thread `request_user_input` for routing, approval, ambiguity, and material choices only when there are 2-3 concrete paths; keep gathering read-only evidence when that can resolve the ambiguity.
- Child agents never ask the user directly; they return `decision_needed`.

## Stop

Stop when repo, branch safety, instructions, or next phase is unclear. Require mutation permission only before a mutating phase.
