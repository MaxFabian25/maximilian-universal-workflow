# Goal Planning Structure

Goal planning produces a plan plus the exact next prompt for goal-backed execution.

## Required Plan

- Evidence: inspected files, commands, explorer summaries, gaps
- Direction, repo/branch, scope, non-goals
- Task order, ownership, verification, review, handoff
- Execution blockers

## Required Launch Prompt

Output one self-contained next prompt:

```text
/goal <execution objective>

Use maximilian-universal-workflow:execution.

Objective:
<same durable execution end state>

Plan:
<task order, ownership, verification, review, handoff>
```

Rules: the `/goal` objective names the durable executed repo end state, is current-state verifiable, and stays under 4,000 characters. Put long instructions in the execution prompt body or a repo file and reference that file from the objective. Resolve active-goal replacement before launch. If `/goal` is unavailable, output the same execution launch prompt without claiming command execution.
