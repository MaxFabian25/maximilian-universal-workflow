---
name: receiving-review
description: Use when review feedback, PR comments, CI review notes, or user critique has been received and must be triaged before repo changes.
---

# Receiving Review

Triage received review feedback before changing repo code, docs, artifacts, or workflow outputs.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/disposition-ledger.md`.

## Do

- Read the full review before acting on any individual point.
- Confirm repo, branch, status, instructions, and review source.
- Verify each item against code, tests, docs, specs, artifacts, and current branch evidence.
- Decide per item: fix, push back with evidence, or return `decision_needed` through root-thread `request_user_input`.
- Implement accepted fixes one item at a time; then run fresh verification for each fixed item.
- Reply with concise dispositions and supporting evidence.
- Update the shared phase bundle for execution, verification, review, or handoff after disposition.
- For GitHub inline review comments, reply in the inline thread, not as a top-level PR comment.

## Stop

Stop when the full review text is missing, an item is ambiguous, the feedback conflicts with repo instructions or support contracts, verification cannot prove the disposition, or destructive/external action lacks approval.
