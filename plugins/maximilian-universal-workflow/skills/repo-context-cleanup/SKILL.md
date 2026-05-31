---
name: repo-context-cleanup
description: Use when stale generated plans, scratch artifacts, duplicate notes, or uncertain repo context block a phase.
---

# Repo Context Cleanup

Clean stale agent context while preserving live authority.

## Read

Follow `../../docs/workflow-contracts/README.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/request-user-input.md`, and `references/cleanup-playbook.md`. Active instructions/specs/docs outrank this skill.

## Avoid

- Ordinary source refactoring.
- Active source, tests, schemas, tooling, or preserved archives.

## Do

- Identify `AGENTS.md`, cleanup conventions, and authority first.
- Classify as authority, archive, stale bloat, generated evidence, or uncertain.
- Actions: delete, archive, consolidate, rewrite as authority, or leave.
- Before mutating cleanup actions, confirm branch safety is already resolved through a `git-worktrees` handoff; otherwise route to `git-worktrees` or stop with the cleanup proposal.
- Use root-thread `request_user_input` when cleanup policy has concrete delete, archive, consolidate, or report-only options.
- Do not delete uncertain items without explicit approval.
- Update the shared phase bundle to return to the blocked phase or handoff.

## Stop

Stop when ownership, archive rules, authority, or delete permission is unclear.
