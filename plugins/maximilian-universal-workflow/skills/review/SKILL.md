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
- Apply the shared subagent role boundary: parent sends self-contained review packets; leaves do only their packet.
- Parent arbitrates findings; review does not replace verification.

## Stop

Stop when review scope is unclear, evidence is missing, or findings reveal unresolved spec/verification gaps.
