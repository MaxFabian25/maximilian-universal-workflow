# Phase Runtime

Runtime loop:

`intake -> exploration -> ideation -> planning -> git-worktrees -> execution -> verification -> review -> handoff`

`AGENTS.md`, user instructions, and task packets outrank this runtime.

## Loop Semantics

A general invocation of the plugin starts at `intake` and advances through the loop in the same turn when the next phase satisfies the Decision Precedence in `phase-transition.md`. Do not stop after naming the next phase unless a user-owned decision, missing evidence, permission boundary, or safety stop requires it.

Phase skills consume and update the current phase bundle state described by `phase-bundle.md`, then route with `phase-transition.md`. Apply the next phase directly when the phase footer has `continue_now: yes`. Normal workflow invocations continue through clear phase handoffs and use this workflow's explicit default goal-backed planning unless the user explicitly asks for planning-only, no-goal, or stop-with-evidence behavior.

## Phase Table

| Phase | Native tools | Required evidence | Exit condition | Next phase |
| --- | --- | --- | --- | --- |
| intake | `git status --short`, branch command, `rg --files`, `AGENTS.md` reads | repo/worktree, branch, status, instructions, requested outcome | repo mechanics and phase are known | exploration |
| exploration | `rg`, reads, non-mutating commands | cited files, commands, branch/status, uncertainty | evidence is enough for a decision or plan | ideation |
| ideation | repo evidence, `request_user_input` | 2-3 implementation-path choices, tradeoffs, selected direction | direction and acceptance criteria are chosen | planning |
| planning | repo reads, `request_user_input`, native goal tools | exploration evidence, acceptance criteria, scope, task order, ownership, verification, native goal state | implementation plan and goal-backed setup are decision-complete | git-worktrees |
| git-worktrees | `git worktree`, branch/status commands, setup command, baseline command, `request_user_input` | branch safety, worktree mode/path when used, branch, ignore check, setup result, baseline result | branch safety is resolved and current branch or worktree is ready | execution |
| execution | `apply_patch`, commands, integration | ownership map, changed paths, local checks, blockers | work is integrated and ready to prove | verification |
| verification | current-state commands/checklists, `get_goal`, `update_goal` after proof | acceptance criteria mapped to command/check results in current repo state | claims are proven, failures are repaired, or a failed state has an explicit stop disposition | review, execution, or handoff |
| review | `git status`, `git diff --stat`, `git diff`, tests, `rg` | findings with file/line evidence and severity | findings resolved or accepted | handoff or execution |
| receiving-review | full review text, repo reads, `request_user_input` | each review item, evidence, disposition, changed paths if fixed | all items are fixed, rejected with evidence, or escalated | execution, verification, review, or handoff |
| handoff | `git status --short`, branch/upstream commands, branch/PR commands, `request_user_input` | changed paths, verification, review, risks, git closeout state, closeout choice | git state is clean, PR/branch closeout is complete, or remaining git work is explicitly user-owned | done |

## Decision Gates

Use `request_user_input` proactively whenever it is available and a phase has 2-3 concrete paths where the choice affects scope, ownership, side effects, active-goal conflict disposition, verification confidence, review disposition, or closeout. Include a recommended option first.

- intake (`phase_route`): choose current phase or approve mutation after read-only state is known.
- exploration (`phase_route`): choose deeper probe, ideation, or stop with evidence when evidence is incomplete but actionable.
- ideation (`ideation_direction`): choose one implementation path from 2-3 repo-grounded options.
- planning (`active_goal_conflict`, `planning_disposition`): choose active-goal conflict disposition, handle explicit planning-only, no-goal, or stop-with-evidence requests, use worktree isolation, revise plan, or stop with plan. Normal workflow invocations create the default goal after decision-complete planning without a separate continuation decision.
- git-worktrees (`worktree_location`, `dirty_state`, `baseline_failure`): choose worktree location, dirty-state disposition, baseline failure disposition, or stop with evidence.
- execution (`ownership_overlap`): choose integration path when ownership overlaps or side effects expand.
- verification (`verification_failure`): choose fix failures, accept residual risk, or stop with evidence; accepted risk or stop-with-evidence routes to handoff without marking completion.
- review (`review_finding`): choose fix findings, accept findings, or request more review.
- receiving-review (`review_finding`): choose fix, push back, or `request_user_input` when feedback changes scope; return `decision_needed` only when `request_user_input` is unavailable or the active workflow phase cannot own the choice.
- handoff (`handoff_closeout`, `cleanup_choice`): choose 2-3 relevant options from stage/commit, push/create PR, keep branch, stop with evidence, or user-owned remaining git work; ask before staging, committing, pushing, merging, deleting, discarding, or destructive cleanup unless the user already explicitly requested that exact closeout action.

## Stop Output Contract

When stopping instead of continuing, update the phase bundle and phase footer with: blocker, evidence checked, uncertainty, decision owner, recommended option, 2-3 choices for `request_user_input` when a decision is required, `continue_now: no`, and the exact next prompt if a later turn should continue the workflow.
