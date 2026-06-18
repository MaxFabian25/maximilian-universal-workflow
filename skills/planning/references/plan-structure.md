# Plan Structure

Use this compact structure for decision-complete, goal-backed repo plans. Extended contract: `../../../docs/workflow-contracts/plan-structure.md`.

## Required Payload

Include goal, evidence, approved direction, acceptance criteria, repo state, scope/non-goals, files/areas, task order, ownership, worktree decision, proof surface, scratch work/prototype disposition, subagent plan, verification, review, handoff target, goal state, execution prompt, phase bundle, `continue_now`, artifact path, and blockers.

Task tables must show task, owner, files/areas, actions, proof surface, verification, and review need. Worker-suitable tasks need non-overlapping mutable ownership.

## Goal Tool Gates

Before `create_goal`, the plan must have a durable executed repo objective, proof-backed criteria, instruction evidence, scope/non-goals, allowed side effects, tasks, ownership, proof surface, subagent plan or explicit none, verification, settled worktree disposition, no blocker, and no explicit planning-only/no-goal/stop-with-evidence instruction. This workflow explicitly authorizes that default goal creation after the gates pass; ordinary non-workflow tasks do not imply `create_goal`.

Route goal tools this way:

- Call `get_goal` after the planned objective is known.
- Use `request_user_input` for active-goal conflicts.
- Call `create_goal` only when no active goal exists and the plan is decision-complete.
- Set `token_budget` only when the user explicitly requested a token budget.
- Do not create goals for planning-only, no-goal, or stop-with-evidence requests; record the objective in the phase bundle.
- Call `update_goal(status="complete")` only from verification or later after identity and fresh proof are confirmed; when completing a budgeted goal, report final token usage from the tool result.
- Call `update_goal(status="blocked")` only after the same blocking condition has repeated for at least three consecutive goal turns and the agent cannot make meaningful progress without user input or an external-state change.

Keep the goal objective current-state verifiable and under 4,000 characters. Put long detail in the execution prompt or repo file. Set `continue_now: yes` only after goal, worktree, ownership, and approval are settled.
