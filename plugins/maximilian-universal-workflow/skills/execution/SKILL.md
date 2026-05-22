---
name: execution
description: Use when executing approved repo changes, coordinating workers, and handing off to verification.
---

# Execution

Execute approved repo plans with clear ownership and verification.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/worker-packets.md`.

## Do

- Check branch/status and instructions before mutation.
- If planned mutation should not happen on the current branch, invoke `git-worktrees` before editing.
- Preserve and verify goal-backed planning objectives.
- When launched from planning with native goal state or `/goal`, treat the goal objective as the execution success target, not as a request to re-plan.
- Execute against the plan acceptance criteria and allowed side effects.
- Parent sends isolated worker packets; leaves do only their packet.
- Prefer `fork_turns: "none"` for self-contained packets; do not use `fork_context`.
- Tell workers not to overwrite others' work.
- Parent integrates, verifies, arbitrates, owns choices.
- Do not create a Codex goal unless the invocation includes `/goal` or explicitly asks for that action.
- On integrated work, update the shared phase bundle and continue to `verification`. On failure or ownership overlap, use `request_user_input`.

## Stop

Stop when the plan is incomplete, branch safety is unclear, required worktree isolation is missing, ownership overlaps, verification is missing, or execution requires unapproved external capability.
