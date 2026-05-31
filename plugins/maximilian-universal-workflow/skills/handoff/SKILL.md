---
name: handoff
description: Use when verified or stopped repo work needs outcome, branch, evidence, risk, owner, and closeout reporting.
---

# Handoff

Close with evidence, risks, branch state, and operator choices.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/handoff-checklist.md`.

## Do

- Report outcome delivered, acceptance criteria status, repo path, worktree path when used, branch, changed paths, verification commands with exit status, review disposition, risks, unverified gaps, stop condition, and next owner.
- Inspect and report git closeout state: unstaged, staged, untracked, unpushed, upstream, PR state when available, and current owner.
- Use root-thread `request_user_input` for 2-3 relevant closeout choices selected from: stop with evidence, keep branch, stage and commit, push/create PR, or user-owned remaining git work.
- Do not stage, commit, discard, delete, merge, push, or create PR without approval and verification.
- Use `workflow-artifacts/` for evidence and handoff support, and update the interactive HTML artifact for substantial runs.
- Update the shared phase bundle and include the final phase footer.

## Stop

Stop when verification failed, blockers remain, base branch is unclear, git closeout is pending without a selected owner, or a mutating/destructive closeout action lacks confirmation.
