---
name: review
description: Use when repo review is needed.
---

# Review

Run read-only review for correctness, scope, tests, risks, artifact quality, and handoff readiness.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/review-packets.md`.

## Do

- Review boundary, requirements, evidence, and changed paths or artifacts are explicit.
- Use concrete repo evidence surfaces: `git status`, `git diff --stat`, `git diff`, changed tests, relevant `rg`, and read-only explorer review packets.
- Apply the shared subagent role boundary: parent sends self-contained review packets; leaves do only their packet.
- Parent arbitrates findings; review does not replace verification.
- On no blocking findings, emit a phase-transition packet and continue to `handoff`. On findings, continue to `execution` or use `request_user_input`.

## Stop

Stop when review scope is unclear, evidence is missing, or findings reveal unresolved spec/verification gaps.
