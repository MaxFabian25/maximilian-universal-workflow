# Phase Runtime

Runtime loop:

`intake -> exploration -> ideation -> planning or goal-planning -> execution -> verification -> review -> handoff`

`AGENTS.md`, user instructions, and task packets outrank this runtime.

## Loop Semantics

A general invocation of the plugin starts at `intake` and advances through the loop in the same turn when the next phase is clear. Do not stop after naming the next phase unless a user decision, missing evidence, permission boundary, or safety stop requires it.

Phase skills may hand off by applying the next phase directly or by emitting the exact next prompt. Prefer direct continuation when the user asked Codex to do the work and repo evidence, approval, and ownership are sufficient.

## Phase Table

| Phase | Native tools | Required evidence | Exit condition | Next phase |
| --- | --- | --- | --- | --- |
| intake | `git status --short`, branch command, `rg --files`, `AGENTS.md` reads | repo/worktree, branch, status, instructions, requested outcome | repo mechanics and phase are known | continue to exploration, ideation, planning, execution, or cleanup |
| exploration | `rg`, reads, non-mutating commands, `explorer` fanout | cited files, commands, branch/status, uncertainty | evidence is enough for a decision or plan | ideation or planning |
| ideation | repo evidence, root `request_user_input`, optional `explorer` critique | 2-3 branch choices, tradeoffs, selected direction | direction and acceptance criteria are chosen | planning or goal-planning |
| planning | repo reads, optional `explorer` checks, root `request_user_input` | exploration evidence, scope, task order, ownership, verification | implementation plan is decision-complete | execution |
| goal-planning | repo reads, goal-prefixed execution launch prompt, goal tool state when useful | plan, concise execution objective, execution prompt, blockers, verification | launch prompt is ready | goal-backed execution |
| execution | `worker` fanout, `apply_patch`, commands, integration | ownership map, changed paths, local checks, blockers | work is integrated and ready to prove | verification |
| verification | parent-side commands/checklists | command/check result in current repo state | claims are proven or failures reported | review or execution |
| review | read-only parent review, native review surfaces, `explorer` fanout | findings with file/line evidence and severity | findings resolved or accepted | handoff or execution |
| handoff | status, branch/PR commands, root `request_user_input` | changed paths, verification, review, risks, closeout choice | operator has next action and owner | done |

## Fanout Bias

Use subagents whenever they improve speed, breadth, critique, or isolation. Prefer `explorer` for read-only evidence and review. Prefer `worker` for isolated write ownership. The limiting rules are ownership, role boundary, and native tool correctness, not token cost.
