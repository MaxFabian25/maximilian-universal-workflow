---
name: receiving-review
description: Use when triaging user, PR, CI, reviewer, or agent feedback before repo changes continue.
---

# Receiving Review

Triage received review feedback before changing repo code, docs, artifacts, or workflow outputs.

## Read

Follow `../../docs/workflow-contracts/README.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/request-user-input.md`, and `references/disposition-ledger.md`.

## Do

- Read the full review before acting on any individual point.
- Confirm repo, branch, status, instructions, and review source.
- Verify each item against code, tests, docs, specs, artifacts, and current branch evidence.
- Decide per item: fix, push back with evidence, use root-thread `request_user_input`, or return a child `decision_needed` payload for the parent to convert into root-thread `request_user_input`.
- Before mutating repo files, confirm branch safety is already resolved through a `git-worktrees` handoff; otherwise route to `git-worktrees` or stop with the disposition ledger.
- Implement accepted fixes one item at a time only after branch safety is resolved; then run fresh verification for each fixed item.
- Reply with concise dispositions and supporting evidence.
- Update the shared phase bundle for execution, verification, review, or handoff after disposition.
- For GitHub inline review comments, reply in the inline thread, not as a top-level PR comment.

## Stop

Stop when the full review text is missing, an item is ambiguous, the feedback conflicts with repo instructions or support contracts, verification cannot prove the disposition, or destructive/external action lacks approval.
