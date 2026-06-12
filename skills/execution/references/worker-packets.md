# Worker Packets

Use these for isolated write-owning leaf workers.

## Ownership Map

| task_name | files/areas | acceptance criteria | allowed actions | forbidden overlap | verification | review need |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Spawn only with credible non-overlap. Packets are self-contained; do not use `fork_context`.

## Write-Owning Worker Packet

```text
Task: Complete <narrow task>.
Agent type: worker.
Ownership: You may edit only <paths or artifact section>.
Context: Other agents or the parent may be working in the same repo. Do not revert, reformat, or overwrite their work.
Acceptance criteria: <criteria this worker must satisfy or preserve>.
Constraints: Stay inside ownership. If overlap needs operator direction and `request_user_input` is available, call it; return decision_needed only when the tool is unavailable, the parent owns the choice, or sibling synthesis must happen first.
Leaf rule: no agent coordination or sibling waits.
Verification: Run or describe <focused check>.
Output: changed paths, acceptance criteria status, verification, assumptions, overlap concerns, request_user_input result or decision_needed if any, follow-up.
Decision payload: when `request_user_input` cannot be called in the current agent, return a `decision_needed:` block with `header`, `id`, `question`, `options`, `recommended_option`, `evidence`, and `blocking_phase`.
```
