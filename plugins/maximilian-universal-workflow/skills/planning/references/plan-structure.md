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
- Goal state: current goal checked, conflict disposition if any, new goal id/status if created, or proceed decision needed
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

Rules: the goal objective names the durable executed repo end state, is current-state verifiable, and stays under 4,000 characters. Put long instructions in the execution prompt body or a repo file and reference that file from the objective. Use `get_goal` before creating a goal. If a different current goal exists, resolve the conflict with `request_user_input` instead of implying native goal overwrite. Set `continue_now: yes` only after goal state, worktree state, ownership, and approval are settled.

## Artifact Use

Use `./workflow-artifacts/YYYY-MM-DD-<slug>.html` for supporting evidence, plans, ledgers, and handoff reports in substantial runs. Follow `../../../docs/workflow-contracts/html-artifact-template.md`. Source changes, tests, docs, commits, branches, and PRs remain the primary repo outputs.
