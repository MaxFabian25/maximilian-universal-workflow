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
- Goal state: existing goal checked when relevant, new goal created if applicable, or replacement decision needed
- Goal-backed execution launch prompt
- Open questions that block execution

## Task Table

| Task | Ownership | Files/Areas | Actions | Verification | Review Need |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Goal-Backed Launch

Every completed planning phase produces one self-contained launch prompt:

```text
/goal <execution objective>

Use maximilian-universal-workflow:execution.

Objective:
<same durable execution end state>

Plan:
<task order, ownership, verification, review, handoff>
```

Rules: the `/goal` objective names the durable executed repo end state, is current-state verifiable, and stays under 4,000 characters. Put long instructions in the execution prompt body or a repo file and reference that file from the objective. Resolve active-goal replacement with `request_user_input` before launch. When native goal tools are available and the user intent is to proceed, `create_goal` may create the objective directly after the plan is complete.

## Artifact Use

Use `./workflow-artifacts/YYYY-MM-DD-<slug>.html` only for supporting evidence, plans, ledgers, or handoff reports. Source changes, tests, docs, commits, branches, and PRs remain the primary repo outputs.
