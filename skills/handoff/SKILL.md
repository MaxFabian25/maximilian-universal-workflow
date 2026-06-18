---
name: handoff
description: Use when verified or stopped repo work needs outcome, branch, evidence, risk, owner, and closeout reporting.
---

# Handoff

Close with evidence, risks, branch state, and operator choices.

## Read

Read `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/evidence-discipline.md`, `../../docs/workflow-contracts/request-user-input.md`, and `references/handoff-checklist.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Report outcome delivered, acceptance criteria status, repo path, worktree path when used, branch, changed paths, proof surfaces, scratch-work disposition, subagent evidence, verification commands with exit status, review disposition, risks, unverified gaps, stop condition, and next owner. Failed-verification handoffs must name the explicit stop-with-evidence or accepted-risk disposition and must not report the work as complete.
- Inspect and report git closeout state: unstaged, staged, untracked, unpushed, upstream, PR state when available, and current owner.
- Use Codex-native subagents to audit closeout state or residual-risk evidence when the handoff is substantial.
- Use root-thread `request_user_input` for 2-3 relevant closeout choices selected from: stop with evidence, keep branch, stage and commit, push/create PR, or user-owned remaining git work.
- Do not stage, commit, discard, delete, merge, push, or create PR without approval and verification.
- Apply `../../docs/workflow-contracts/artifact-floor.md` for substantial handoff support artifacts.
- Update the shared phase bundle and include the final phase footer.

## Stop

Stop when verification failed without an explicit stop-with-evidence or accepted-risk disposition, blockers remain, base branch is unclear, git closeout is pending without a selected owner, or a mutating/destructive closeout action lacks confirmation.
