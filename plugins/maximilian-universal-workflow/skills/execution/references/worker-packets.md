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
Constraints: Stay inside ownership. If overlap is needed, stop and return decision_needed.
Leaf rule: no agent coordination or sibling waits.
Verification: Run or describe <focused check>.
Output: changed paths, acceptance criteria status, verification, assumptions, overlap concerns, decision_needed if any, follow-up.
Decision payload: when blocked, return header, id, question, 2-3 options, recommended option, evidence, and blocking_phase.
```
