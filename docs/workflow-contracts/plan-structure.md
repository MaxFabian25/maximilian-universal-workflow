# Plan Structure

Detailed decision-complete, goal-backed repo plan contract for `../../skills/planning/SKILL.md`.

## Required Fields

- Goal
- Exploration evidence: files inspected, commands run, and unresolved evidence gaps
- Approved direction
- Acceptance criteria
- Repo state and branch assumption
- Scope and non-goals
- Files or areas to create/modify
- Information-structure changes: file placement, file role, file structure, locality, or explicit none
- Vocabulary and decision capture: new terms, decision records, or explicit none
- Work-item shape: task table, vertical slices, external destination, or explicit none
- Task order
- Ownership model
- Worktree decision: current branch approved, isolated worktree required, or decision needed
- Proof surface: command, checklist, source set, query, prototype, dry-run, or manual evidence needed to prove the work
- Scratch work/prototype disposition
- Subagent plan: where independent exploration, implementation, verification, or review would improve quality
- Verification commands or checklists
- Review expectations
- Handoff target
- Goal state: current goal checked, conflict disposition if any, new goal id/status if created, or explicit planning-only/no-goal/stop-with-evidence decision needed
- Goal-backed execution setup: native goal id/status, execution prompt, phase bundle, `continue_now`, and artifact path for substantial runs
- Open questions that block execution

## Task Table

| Task | Ownership | Files/Areas | Actions | Proof Surface | Verification | Review Need |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Goal-Backed Setup

Every completed planning phase that passes the Goal Tool Gates establishes native goal-backed execution state after current-goal conflicts are settled:

```text
Use maximilian-universal-workflow:execution.

Objective:
<same durable execution end state>

Acceptance criteria:
<criteria that verification and handoff must prove>

Plan:
<task order, ownership, allowed side effects, proof surface, subagent plan, verification, review, handoff>

Phase bundle:
<current shared phase bundle fields that execution must preserve or update>
```

Rules: the goal objective names the durable executed repo end state, is current-state verifiable, and stays under 4,000 characters. Put long instructions in the execution prompt body or a repo file and reference that file from the objective. Use `get_goal` before creating a goal. When this workflow is invoked, this contract explicitly instructs default goal-backed planning unless the user asks for planning-only, no-goal, or stop-with-evidence; do not infer goals for ordinary non-workflow tasks. If a different current goal exists, resolve the conflict with `request_user_input` instead of implying native goal overwrite. Create the default goal when no current goal exists after the plan is complete. Set `token_budget` only when the user explicitly requested a token budget. Set `continue_now: yes` after goal state, worktree state, ownership, and approval are settled unless the user explicitly asked for planning-only, no-goal, or stop-with-evidence work.

## Goal Tool Gates

Before calling `create_goal`, the plan is decision-complete only when all of these are present:

- durable executed repo objective;
- acceptance criteria with proof expectations;
- repo state and governing instruction evidence;
- scope, non-goals, files or areas, and allowed side effects;
- information-structure, vocabulary, decision-capture, scratch-work, and work-item-shaping disposition where relevant;
- task order and ownership model;
- proof surface, scratch work/prototype disposition, and subagent plan;
- verification commands or checklists;
- worktree disposition with no pending user decision: `current-branch` explicitly approved, `worktree-needed`, or `worktree-ready`;
- no open question that blocks execution;
- no explicit planning-only, no-goal, or stop-with-evidence instruction.

Goal tool routing:

- Call `get_goal` during planning after the planned objective is known.
- Call `request_user_input` when the active goal conflicts with the planned objective.
- Call `create_goal` only when no active goal exists and the plan is decision-complete.
- Set `token_budget` only when the user explicitly requested a token budget.
- Do not call `create_goal` for planning-only, no-goal, or stop-with-evidence requests; record the objective in the phase bundle instead.
- Call `update_goal(status="complete")` only from verification or later, after `get_goal` confirms identity and fresh proof shows no required work remains; when completing a budgeted goal, report final token usage from the tool result.
- Call `update_goal(status="blocked")` only after the same blocking condition has repeated for at least three consecutive goal turns and the agent cannot make meaningful progress without user input or an external-state change.

## Artifact Use

Apply `artifact-floor.md` for supporting artifact requirements and exceptions. Use `html-artifact-template.md` for HTML artifact shape.
