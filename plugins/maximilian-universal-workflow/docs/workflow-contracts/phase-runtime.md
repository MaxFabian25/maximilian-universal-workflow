# Phase Runtime

Runtime loop:

`intake -> exploration -> ideation -> planning -> execution -> verification -> review -> handoff`

`AGENTS.md`, user instructions, and task packets outrank this runtime.

## Loop Semantics

A general invocation of the plugin starts at `intake` and advances through the loop in the same turn when the next phase is clear. Do not stop after naming the next phase unless a user decision, missing evidence, permission boundary, or safety stop requires it.

Phase skills may hand off by applying the next phase directly or by emitting the exact next prompt. Prefer direct continuation when the user asked Codex to do the work and repo evidence, approval, and ownership are sufficient.

## Phase Table

| Phase | Native tools | Required evidence | Exit condition | Next phase |
| --- | --- | --- | --- | --- |
| intake | `git status --short`, branch command, `rg --files`, `AGENTS.md` reads | repo/worktree, branch, status, instructions, requested outcome | repo mechanics and phase are known | continue to exploration, ideation, planning, execution, or cleanup |
| exploration | `rg`, reads, non-mutating commands, `explorer` fanout | cited files, commands, branch/status, uncertainty | evidence is enough for a decision or plan | ideation or planning |
| ideation | repo evidence, root `request_user_input`, optional `explorer` critique | 2-3 branch choices, tradeoffs, selected direction | direction and acceptance criteria are chosen | planning |
| planning | repo reads, optional `explorer` checks, root `request_user_input`, native goal tools | exploration evidence, scope, task order, ownership, verification, native goal state | implementation plan and goal-backed setup are decision-complete | execution |
| execution | `worker` fanout, `apply_patch`, commands, integration | ownership map, changed paths, local checks, blockers | work is integrated and ready to prove | verification |
| verification | parent-side commands/checklists, `update_goal` after proof | command/check result in current repo state | claims are proven or failures reported | review or execution |
| review | `git status`, `git diff --stat`, `git diff`, tests, `rg`, `explorer` fanout | findings with file/line evidence and severity | findings resolved or accepted | handoff or execution |
| receiving-review | full review text, repo reads, optional `explorer` checks, root `request_user_input` | each review item, evidence, disposition, changed paths if fixed | all items are fixed, rejected with evidence, or escalated | execution, verification, review, or handoff |
| handoff | status, branch/PR commands, root `request_user_input` | changed paths, verification, review, risks, closeout choice | operator has next action and owner | done |

## Fanout Bias

Use subagents whenever they improve speed, breadth, critique, or isolation. Prefer `explorer` for read-only evidence and review. Prefer `worker` for isolated write ownership. The limiting rules are ownership, role boundary, and native tool correctness, not token cost.

## Decision Gates

Use root-thread `request_user_input` whenever a phase has 2-3 concrete paths and the choice affects scope, ownership, side effects, goal replacement, verification confidence, review disposition, or closeout. Include a recommended option first.

- intake: choose current phase or approve mutation after read-only state is known.
- exploration: choose deeper probe, ideation, or planning when evidence is incomplete but actionable.
- ideation: choose one branch from 2-3 repo-grounded options.
- planning: choose replace/create goal, proceed to execution, revise plan, or stop with plan.
- execution: choose parent integration path when worker ownership overlaps or side effects expand.
- verification: choose fix failures, accept residual risk, or stop with evidence.
- review: choose fix findings, accept findings, or request more review.
- receiving-review: choose fix, push back, defer, or escalate when feedback changes scope.
- handoff: choose stop with evidence, keep branch, or create PR; ask again before merge, push, delete, discard, or destructive cleanup.

## Stop Output Contract

When stopping instead of continuing, return: blocker, evidence checked, uncertainty, decision owner, recommended option, 2-3 choices for `request_user_input` when applicable, and the exact next prompt if a later turn should continue the workflow.
