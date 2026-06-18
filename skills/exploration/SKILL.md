---
name: exploration
description: Use when repo evidence is missing or uncertain and read-only investigation should precede later phases.
---

# Exploration

Gather repo evidence before decisions, edits, verification, review.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, and `../../docs/workflow-contracts/request-user-input.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Prefer `rg`, `rg --files`, direct reads, and non-mutating commands.
- Cite file, command, branch/status, test, log, or source evidence.
- Update the shared phase bundle with evidence, uncertainty, next phase, and artifact state.
- When evidence is sufficient, continue to `ideation`. When evidence conflicts, use `request_user_input` for the next probe or stop path.

## Stop

Stop when evidence conflicts or a user decision is required.
