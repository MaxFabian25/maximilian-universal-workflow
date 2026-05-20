# Plan Structure

Use this structure for decision-complete, goal-backed repo plans.

## Required Fields

- Goal
- Exploration evidence: files inspected, commands run, explorer summaries if any, and unresolved evidence gaps
- Approved direction
- Repo state and branch assumption
- Scope and non-goals
- Files or areas to create/modify
- Task order
- Ownership model
- Verification commands or checklists
- Review expectations
- Handoff target
- Goal state: existing goal checked when relevant, new goal created when approval allows, or replacement/proceed decision needed
- Goal-backed execution setup: native goal id/status and execution prompt
- Open questions that block execution

## Task Table

| Task | Ownership | Files/Areas | Actions | Verification | Review Need |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Goal-Backed Setup

Every completed planning phase establishes native goal-backed execution state:

```text
Use maximilian-universal-workflow:execution.

Objective:
<same durable execution end state>

Plan:
<task order, ownership, verification, review, handoff>
```

Rules: the goal objective names the durable executed repo end state, is current-state verifiable, and stays under 4,000 characters. Put long instructions in the execution prompt body or a repo file and reference that file from the objective. Resolve active-goal replacement and proceed intent with `request_user_input` before `create_goal`.

## Artifact Use

Use `./workflow-artifacts/YYYY-MM-DD-<slug>.html` only for supporting evidence, plans, ledgers, or handoff reports. Source changes, tests, docs, commits, branches, and PRs remain the primary repo outputs.
