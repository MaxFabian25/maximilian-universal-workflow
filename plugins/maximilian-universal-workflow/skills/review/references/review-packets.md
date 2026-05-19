# Review Packets

Use this packet for read-only leaf review explorers.

## Read-Only Review Packet

```text
Task: Review <change/artifact/output>.
Agent type: explorer.
Scope: Read only <paths/artifacts/commands>.
Requirements: <plan/spec/expected behavior>.
Constraints: Do not edit files, ask the user, coordinate agents, or wait for siblings.
Check: correctness, scope, tests/evidence, integration risks, unsupported claims, handoff gaps.
Output findings by severity with evidence.
```

## Severity

- Critical: blocks correctness, data safety, or required behavior.
- Important: fix or explicitly accept before handoff.
- Minor: non-blocking improvement.
