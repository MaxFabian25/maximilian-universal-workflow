---
name: execution
description: Use when approved repo plans need implementation, integration, ownership control, and verification handoff.
---

# Execution

Execute approved repo plans with clear ownership and verification.

## Read

Read `../../docs/workflow-contracts/phase-core.md`, `../../docs/workflow-contracts/evidence-discipline.md`, `../../docs/workflow-contracts/proof-first-change.md`, `../../docs/workflow-contracts/diagnosis-loop.md`, and `../../docs/workflow-contracts/information-structure.md`. Use other workflow-contract files only when the core requires deeper authority.

## Do

- Check branch/status and instructions before mutation.
- Require a completed `git-worktrees` handoff before write-owning mutation; invoke `git-worktrees` first when the handoff is missing.
- Preserve active native goal state. When launched from planning, treat the goal objective as the execution success target, not a re-plan request.
- Execute against the plan acceptance criteria and allowed side effects.
- For unexpected failures or bad outputs, follow `diagnosis-loop.md`; for material mutation, preserve proof-first state from `proof-first-change.md`.
- Apply `information-structure.md` when execution moves, splits, merges, deletes, or changes file roles.
- Keep changed-path ownership explicit and non-overlapping.
- Use Codex-native subagents for non-overlapping implementation, support-artifact work, or independent checks when ownership is clear and integration stays in the running thread.
- Track scratch work, scripts, drafts, or prototypes and disposition them before handoff.
- Integrate, verify, arbitrate, and own final choices in the running thread.
- Do not create goals during execution. If direct execution lacks a verified matching active goal, route through `planning` before mutation.
- Update the shared phase bundle and continue to `verification`. Fix ordinary in-scope failures directly. Use `request_user_input` only for scope, side-effect, ownership, or material risk changes.

## Stop

Stop when the plan is incomplete, branch safety or required isolation is unresolved, ownership overlaps, verification is missing, or execution needs unapproved external capability.
