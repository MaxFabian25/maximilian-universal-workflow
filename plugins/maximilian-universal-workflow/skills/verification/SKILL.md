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
- Report command, exit status, pass/fail counts or key evidence, and unverified gaps.
- Treat child summaries and old output as inputs, not proof.
- If an active goal is complete and no required work remains, mark it complete with `update_goal`.
- If verification cannot run, state exactly why and what risk remains.

## Stop

Stop when verification fails, the proving command is unknown, or running it would require unapproved destructive/external action.
