# Explorer Packets

Use these for read-only leaf explorers.

## Read-Only Investigation

```text
Task: Investigate <question>.
Agent type: explorer.
Scope: Read only <files/directories/commands>.
Constraints: no edits, user questions, coordination, or sibling waits.
Evidence: Cite exact paths, lines, command output, or observations.
Output: finding, evidence, uncertainty, acceptance criteria implications, decision_needed if any, next probe.
Decision payload: when blocked, return a `decision_needed:` block with `header`, `id`, `question`, `options`, `recommended_option`, `evidence`, and `blocking_phase`.
```

## Root-Cause Map

```text
Task: Map likely root causes for <symptom>.
Agent type: explorer.
Scope: Read only <subsystem/test/log area>.
Constraints: no edits, coordination, or sibling waits.
Output: ranked causes, evidence for/against, missing evidence, acceptance criteria implications, next verification step, decision payload if blocked.
Decision payload: when blocked, return a `decision_needed:` block with `header`, `id`, `question`, `options`, `recommended_option`, `evidence`, and `blocking_phase`.
```
