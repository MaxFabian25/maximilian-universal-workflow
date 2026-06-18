---
name: execution
description: Use when approved repo plans need implementation, integration, ownership control, and verification handoff.
---

# Execution

Execute approved repo plans with clear ownership and verification.

## Read

Read `../../docs/workflow-contracts/phase-core.md`. Use other workflow-contract files only when the core requires deeper authority.

## Do

- Check branch/status and instructions before mutation.
- Require a completed `git-worktrees` handoff before write-owning mutation; invoke `git-worktrees` first when the handoff is missing.
- Preserve active native goal state. When launched from planning, treat the goal objective as the execution success target, not a re-plan request.
- Execute against the plan acceptance criteria and allowed side effects.
- Keep changed-path ownership explicit and non-overlapping.
- Integrate, verify, arbitrate, and own final choices in the running thread.
- Do not create goals during execution. If direct execution lacks a verified matching active goal, route through `planning` before mutation.
- Update the shared phase bundle and continue to `verification`. Fix ordinary in-scope failures directly. Use `request_user_input` only for scope, side-effect, ownership, or material risk changes.

## Stop

Stop when the plan is incomplete, branch safety or required isolation is unresolved, ownership overlaps, verification is missing, or execution needs unapproved external capability.
