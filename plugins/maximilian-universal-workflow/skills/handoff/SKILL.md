---
name: handoff
description: Use when repo closeout is needed.
---

# Handoff

Close with evidence, risks, branch state, and operator choices.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/handoff-checklist.md`.

## Do

- Report repo path, branch, changed paths, verification, review, risks, and next owner.
- Use root-thread `request_user_input` for non-destructive closeout choices first: stop with evidence, keep branch, or create PR.
- Do not discard, delete, merge, or push without approval and verification.
- Use `workflow-artifacts/` for evidence and handoff support only.

## Stop

Stop when verification failed, blockers remain, base branch is unclear, or destructive closeout lacks confirmation.
