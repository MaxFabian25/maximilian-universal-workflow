# Plan Structure

Use this structure for decision-complete, goal-backed repo plans.

## Required Fields

- Goal
- Exploration evidence: files inspected, commands run, explorer summaries if any, and unresolved evidence gaps
- Approved direction
- Acceptance criteria
- Repo state and branch assumption
- Scope and non-goals
- Files or areas to create/modify
- Task order
- Ownership model
- Worktree decision: current branch approved, isolated worktree required, or decision needed
- Verification commands or checklists
- Review expectations
- Handoff target
- Goal state: current goal checked, conflict disposition if any, new goal id/status if created, or explicit planning-only/no-goal decision needed
- Goal-backed execution setup: native goal id/status, execution prompt, phase bundle, `continue_now`, and artifact path for substantial runs
- Open questions that block execution

## Task Table

| Task | Ownership | Files/Areas | Actions | Verification | Review Need |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Goal-Backed Setup

Every completed planning phase establishes native goal-backed execution state after current-goal conflicts are settled:

```text
Use maximilian-universal-workflow:execution.

Objective:
<same durable execution end state>

Acceptance criteria:
<criteria that verification and handoff must prove>

Plan:
<task order, ownership, allowed side effects, verification, review, handoff>

Phase bundle:
<current shared phase bundle fields that execution must preserve or update>
```

Rules: the goal objective names the durable executed repo end state, is current-state verifiable, and stays under 4,000 characters. Put long instructions in the execution prompt body or a repo file and reference that file from the objective. Use `get_goal` before creating a goal. Normal workflow invocation is goal setup intent unless the user asks for planning-only, no-goal, or stop-with-evidence. If a different current goal exists, resolve the conflict with `request_user_input` instead of implying native goal overwrite. Create the default goal when no current goal exists after the plan is complete. Set `continue_now: yes` after goal state, worktree state, ownership, and approval are settled unless the user explicitly asked for planning-only or no-goal work.

## Goal Tool Gates

Before calling `create_goal`, the plan is decision-complete only when all of these are present:

- durable executed repo objective;
- acceptance criteria with proof expectations;
- repo state and governing instruction evidence;
- scope, non-goals, files or areas, and allowed side effects;
- task order and ownership model;
- verification commands or checklists;
- proposed worktree mode or `decision-needed` from `git-worktrees`;
- no open question that blocks execution;
- no explicit planning-only or no-goal instruction.

Goal tool routing:

- Call `get_goal` during planning after the planned objective is known.
- Call `request_user_input` when the active goal conflicts with the planned objective.
- Call `create_goal` only when no active goal exists and the plan is decision-complete.
- Do not call `create_goal` for planning-only or no-goal requests; record the objective in the phase bundle instead.
- Call `update_goal` only from verification or later, after `get_goal` confirms identity and fresh proof shows no required work remains.

## Artifact Use

Apply `../../../docs/workflow-contracts/artifact-floor.md` for supporting artifact requirements and exceptions. Use `../../../docs/workflow-contracts/html-artifact-template.md` for HTML artifact shape.
