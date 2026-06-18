---
name: exploration
description: Use when repo evidence is missing or uncertain and read-only investigation should precede later phases.
---

# Exploration

Gather repo evidence before decisions, edits, verification, review.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/evidence-discipline.md`, and `../../docs/workflow-contracts/request-user-input.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Prefer `rg`, `rg --files`, direct reads, and non-mutating commands.
- Cite file, command, branch/status, test, log, or source evidence.
- For bugs, failed checks, bad output, disputed claims, or uncertain analysis, identify the lightest proof surface or tight feedback loop before recommending changes.
- Use Codex-native subagents for independent evidence areas, large search spaces, or competing hypotheses when parallel read-only investigation improves quality.
- Update the shared phase bundle with evidence, proof surface, uncertainty, next phase, and artifact state.
- When evidence is sufficient, continue to `ideation`. When evidence conflicts, use `request_user_input` for the next investigation or stop path.

## Stop

Stop when evidence conflicts or a user decision is required.
