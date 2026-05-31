---
name: intake
description: Use when starting the repo workflow loop, routing phases, and opening material decisions.
---

# Intake

Start and advance repo workflows by confirming authority, state, and phase.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, and `../../docs/workflow-contracts/phase-bundle.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Confirm git repo, branch, `git status --short`, and applicable `AGENTS.md` before mutation.
- When the user invokes the plugin generally, run the phase loop; do not stop at classification.
- For a general workflow invocation, route to `exploration` after repo state is known. Route directly to a narrower phase only when the user explicitly selected that phase or the current phase bundle already owns it.
- Create or update the shared phase bundle with repo state, objective, acceptance criteria if known, allowed side effects, evidence, chosen phase, and open decisions.
- Continue into the next phase when evidence, approval, and permissions are already sufficient.
- If continuation needs a later user turn, provide the exact next skill invocation prompt.
- Call root-thread `request_user_input` for routing, approval, ambiguity, and material choices only when there are 2-3 concrete paths; keep gathering read-only evidence when that can resolve the ambiguity.
- Child agents never ask the user directly; they return `decision_needed`.

## Stop

Stop when repo, branch safety, instructions, or next phase is unclear. Require mutation permission only before a mutating phase.
