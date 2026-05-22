---
name: handoff
description: Use when verified or stopped repo work needs outcome, branch, evidence, risk, owner, and closeout reporting.
---

# Handoff

Close with evidence, risks, branch state, and operator choices.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/handoff-checklist.md`.

## Do

- Report outcome delivered, acceptance criteria status, repo path, worktree path when used, branch, changed paths, verification commands with exit status, review disposition, risks, unverified gaps, stop condition, and next owner.
- Use root-thread `request_user_input` for non-destructive closeout choices first: stop with evidence, keep branch, or create PR.
- Do not discard, delete, merge, or push without approval and verification.
- Apply `../../docs/workflow-contracts/artifact-floor.md` for substantial handoff support artifacts.

## Stop

Stop when verification failed, blockers remain, base branch is unclear, or destructive closeout lacks confirmation.
