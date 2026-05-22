---
name: review
description: Use when verified work needs read-only correctness, scope, test, risk, artifact, and handoff-readiness review.
---

# Review

Run read-only review for correctness, scope, tests, risks, artifact quality, and handoff readiness.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, and `references/review-packets.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Review boundary, requirements, evidence, and changed paths or artifacts are explicit.
- Use concrete repo evidence surfaces: `git status`, `git diff --stat`, `git diff`, changed tests, relevant `rg`, and read-only explorer review packets.
- Apply the shared subagent role boundary: parent sends self-contained review packets; leaves do only their packet.
- Parent arbitrates findings; review does not replace verification.
- On no blocking findings, update the shared phase bundle and continue to `handoff`. Send valid in-scope findings to `execution`; use `request_user_input` only for accepting, rejecting, deferring, or broadening findings when the choice remains material.

## Stop

Stop when review scope is unclear, evidence is missing, or findings reveal unresolved spec/verification gaps.
