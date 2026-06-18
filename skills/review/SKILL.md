---
name: review
description: Use when verified work needs read-only correctness, scope, test, risk, support-artifact, and handoff-readiness review.
---

# Review

Run read-only review for correctness, scope, tests, risks, support-artifact quality, and handoff readiness.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/evidence-discipline.md`, `../../docs/workflow-contracts/information-structure.md`, `../../docs/workflow-contracts/work-item-shaping.md`, and `../../docs/workflow-contracts/request-user-input.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Review boundary, requirements, evidence, changed paths, and support artifacts are explicit.
- Use concrete repo evidence surfaces: `git status`, `git diff --stat`, `git diff`, changed tests, and relevant `rg`.
- Use Codex-native subagents for separate correctness, scope, risk, or artifact-quality passes when review breadth matters.
- Check that proof surfaces match the acceptance criteria and that scratch work has a disposition.
- Check information-structure locality, structural depth, stale references, duplicated authority, and overloaded files when structure changed.
- The running thread arbitrates findings; review does not replace verification.
- When review has no blocking findings, update the shared phase bundle and continue to `handoff`. Send valid in-scope findings to `execution`; use `request_user_input` only for accepting, rejecting, deferring, or broadening findings when the choice remains material.

## Stop

Stop when review scope is unclear, evidence is missing, or findings reveal unresolved spec/verification gaps.
