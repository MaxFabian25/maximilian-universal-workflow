# Review Packets

Use this packet for read-only leaf review explorers.

## Read-Only Review Packet

```text
Task: Review <change/artifact/output>.
Agent type: explorer.
Scope: Read only <paths/artifacts/commands>.
Requirements: <plan/spec/expected behavior>.
Acceptance criteria: <criteria to preserve or prove>.
Constraints: Do not edit files, ask the user, coordinate agents, or wait for siblings.
Check: correctness, scope, tests/evidence, integration risks, unsupported claims, handoff gaps.
Output findings by severity with evidence.
Decision payload: when blocked, return a `decision_needed:` block with `header`, `id`, `question`, `options`, `recommended_option`, `evidence`, and `blocking_phase`.
```

## Severity

- Critical: blocks correctness, data safety, or required behavior.
- Important: fix or explicitly accept before handoff.
- Minor: non-blocking improvement.
