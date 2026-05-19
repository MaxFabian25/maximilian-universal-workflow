# Phase Runtime

Runtime loop:

`intake -> exploration -> ideation -> planning or goal-planning -> execution -> verification -> review -> handoff`

`AGENTS.md`, user instructions, and task packets outrank this runtime.

## Phase Table

| Phase | Native tools | Required evidence | Exit condition | Next phase |
| --- | --- | --- | --- | --- |
| intake | `git status --short`, branch command, `rg --files`, `AGENTS.md` reads | repo/worktree, branch, status, instructions, requested outcome | repo mechanics and phase are known | exploration, ideation, planning, execution, cleanup |
| exploration | `rg`, reads, non-mutating commands, `explorer` fanout | cited files, commands, branch/status, uncertainty | evidence is enough for a decision or plan | ideation or planning |
| ideation | repo evidence, root `request_user_input`, optional `explorer` critique | 2-3 branch choices, tradeoffs, selected direction | direction and acceptance criteria are chosen | planning or goal-planning |
| planning | repo reads, optional `explorer` checks, root `request_user_input` | exploration evidence, scope, task order, ownership, verification | implementation plan is decision-complete | execution |
| goal-planning | repo reads, `/goal` launch bundle, goal tool state when useful | concise objective, execution prompt, blockers, verification | launch bundle is ready | `/goal` submission then execution |
| execution | `worker` fanout, `apply_patch`, commands, integration | ownership map, changed paths, local checks, blockers | work is integrated and ready to prove | verification |
| verification | parent-side commands/checklists | command/check result in current repo state | claims are proven or failures reported | review or execution |
| review | read-only parent review, native review surfaces, `explorer` fanout | findings with file/line evidence and severity | findings resolved or accepted | handoff or execution |
| handoff | status, branch/PR commands, root `request_user_input` | changed paths, verification, review, risks, closeout choice | operator has next action and owner | done |

## Fanout Bias

Use subagents whenever they improve speed, breadth, critique, or isolation. Prefer `explorer` for read-only evidence and review. Prefer `worker` for isolated write ownership. The limiting rules are ownership, role boundary, and native tool correctness, not token cost.
