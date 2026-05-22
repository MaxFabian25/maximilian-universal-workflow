---
name: verification
description: Use when repo verification is needed.
---

# Verification

Prove completion claims with fresh repo-state evidence.

## Read

Follow `../../docs/workflow-contracts/README.md`.

## Do

- Run or identify the command/checklist proving the claim in the current repo state.
- Map acceptance criteria to command/check evidence, exit status, pass/fail counts, and unverified gaps.
- Treat child summaries and old output as inputs, not proof.
- Call `get_goal` before `update_goal`; mark the goal complete only when the active objective matches the verified outcome and no required work remains.
- If verification cannot run, state exactly why and what risk remains.
- On pass, update the shared phase bundle and continue to `review`. On fail, continue to `execution` or use `request_user_input`.

## Stop

Stop when verification fails, the proving command is unknown, or running it would require unapproved destructive/external action.
