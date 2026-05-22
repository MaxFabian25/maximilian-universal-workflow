---
name: verification
description: Use when execution claims need fresh parent-side proof mapped to acceptance criteria and goal state.
---

# Verification

Prove completion claims with fresh repo-state evidence.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, and `../../docs/workflow-contracts/native-tool-map.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Run or identify the command/checklist proving the claim in the current repo state.
- Map acceptance criteria to command/check evidence, exit status, pass/fail counts, and unverified gaps.
- Treat child summaries and old output as inputs, not proof.
- Call `get_goal` before `update_goal`; mark the goal complete only when the active objective matches the verified outcome and no required work remains.
- If verification cannot run, state exactly why and what risk remains.
- On pass, update the shared phase bundle and continue to `review`. On fail, return to `execution` when repair is clear and in scope. Use `request_user_input` only for residual-risk, scope, side-effect, or stop-with-evidence choices.

## Stop

Stop when verification fails, the proving command is unknown, or running it would require unapproved destructive/external action.
