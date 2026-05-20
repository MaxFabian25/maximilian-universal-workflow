---
name: execution
description: Use when repo execution is needed.
---

# Execution

Execute approved repo plans with clear ownership and verification.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/worker-packets.md`.

## Do

- Check branch/status and instructions before mutation.
- Preserve and verify goal-backed planning objectives.
- When launched from planning with native goal state or `/goal`, treat the goal objective as the execution success target, not as a request to re-plan.
- Parent sends isolated worker packets; leaves do only their packet.
- Prefer `fork_turns: "none"` for self-contained packets; do not use `fork_context`.
- Tell workers not to overwrite others' work.
- Parent integrates, verifies, arbitrates, owns choices.
- Do not create or replace a Codex goal unless the invocation includes `/goal` or explicitly asks for that action.

## Stop

Stop when the plan is incomplete, branch safety is unclear, ownership overlaps, verification is missing, or execution requires unapproved external capability.
