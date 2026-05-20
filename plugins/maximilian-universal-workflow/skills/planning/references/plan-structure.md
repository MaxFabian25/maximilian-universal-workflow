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
- Goal state: existing goal checked when relevant, new goal created when tools and approval allow, or replacement/proceed decision needed
- Goal-backed execution launch: native goal id/status or manual `/goal` prompt
- Open questions that block execution

## Task Table

| Task | Ownership | Files/Areas | Actions | Verification | Review Need |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Goal-Backed Launch

Every completed planning phase establishes a goal-backed launch state. Prefer native goal tools when available and user intent is clear. Use a manual launch prompt only when native goal creation is unavailable or intentionally deferred:

```text
/goal <execution objective>

Use maximilian-universal-workflow:execution.

Objective:
<same durable execution end state>

Plan:
<task order, ownership, verification, review, handoff>
```

Rules: the goal objective names the durable executed repo end state, is current-state verifiable, and stays under 4,000 characters. Put long instructions in the execution prompt body or a repo file and reference that file from the objective. Resolve active-goal replacement and proceed intent with `request_user_input` before native `create_goal` or manual launch.

## Artifact Use

Use `./workflow-artifacts/YYYY-MM-DD-<slug>.html` only for supporting evidence, plans, ledgers, or handoff reports. Source changes, tests, docs, commits, branches, and PRs remain the primary repo outputs.
