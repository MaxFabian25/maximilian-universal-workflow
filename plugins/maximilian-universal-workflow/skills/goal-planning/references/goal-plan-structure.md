# Goal Plan Structure

Required launch bundle:

- Evidence: inspected files, commands, explorer summaries, gaps
- Direction, repo/branch, scope, non-goals
- Command: `/goal <objective>` or, only when requested, `/goal --tokens <budget> <objective>`; objective must stay under 4,000 characters
- `maximilian-universal-workflow:execution` prompt carrying the same objective, task order, ownership, verification, review, handoff
- Execution blockers

Rules: objective names the durable repo end state, is current-state verifiable, and stays concise. Put long instructions in the execution prompt or a repo file and reference that file from the objective. Resolve active-goal replacement before launch. If `/goal` is unavailable, output the same objective bundle without claiming command execution. If `/goal` cannot be submitted separately, the execution prompt must explicitly ask whether to create or set the goal.
