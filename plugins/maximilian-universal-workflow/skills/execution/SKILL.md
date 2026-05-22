---
name: execution
description: Use when approved repo plans need implementation, integration, ownership control, and verification handoff.
---

# Execution

Execute approved repo plans with clear ownership and verification.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/native-tool-map.md`, and `references/worker-packets.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Check branch/status and instructions before mutation.
- Require a completed `git-worktrees` handoff before write-owning mutation. If it is missing, invoke `git-worktrees` before editing.
- Preserve and verify goal-backed planning objectives.
- When launched from planning with native goal state or `/goal`, treat the goal objective as the execution success target, not as a request to re-plan.
- Execute against the plan acceptance criteria and allowed side effects.
- Parent sends isolated worker packets; leaves do only their packet.
- Prefer `fork_turns: "none"` for self-contained packets; do not use `fork_context`.
- Tell workers not to overwrite others' work.
- Parent integrates, verifies, arbitrates, owns choices.
- Do not create a second Codex goal during execution; planning owns default goal-backed setup and execution preserves the active native goal state.
- On integrated work, update the shared phase bundle and continue to `verification`. Fix ordinary in-scope implementation failures directly. Use `request_user_input` only when the fix expands scope, changes side effects, creates ownership overlap, or leaves a material risk choice.

## Stop

Stop when the plan is incomplete, branch safety is unclear, required worktree isolation is missing, ownership overlaps, verification is missing, or execution requires unapproved external capability.
