# Phase Transition

Use this packet whenever one phase hands work to the next phase, stops for a decision, or writes a durable support artifact.

## Packet

```text
Outcome: <repo end state or phase result>
Acceptance criteria: <criteria that prove the outcome>
Allowed side effects: <read-only/write paths/external actions/none>
Evidence gathered: <files, commands, subagent summaries, artifact paths>
Current phase result: <passed/failed/decision_needed/blocked>
Next phase: <phase name and reason>
Next prompt: <exact skill invocation or continuation prompt when a later turn is needed>
Open decisions: <request_user_input id or none>
Artifact: <workflow-artifacts path or none for trivial work>
```

## Rules

- Treat acceptance criteria as the thread running through planning, execution, verification, review, and handoff.
- Continue directly into the next phase when the user asked Codex to do the work and the packet proves approval, ownership, and evidence are sufficient.
- Use `request_user_input` before crossing a material side-effect, scope, ownership, goal, verification, review, or closeout decision.
- For substantial runs, create or update `workflow-artifacts/YYYY-MM-DD-<slug>.html` with the current packet, decisions, evidence, and next phase.
- Substantial runs include multi-phase work, multi-agent work, goal-backed execution, non-trivial verification, review ledgers, and handoff reports.
- Trivial single-step work may report the packet in the final response without an HTML artifact.

## Pass/Fail Routing

- Exploration sufficient -> ideation or planning.
- Ideation selected -> planning.
- Planning complete and goal state settled -> execution.
- Execution integrated -> verification.
- Verification pass -> review.
- Verification fail -> execution or `request_user_input`.
- Review pass -> handoff.
- Review findings -> execution or `request_user_input`.
- Handoff choice selected -> done, PR, branch continuation, or user-owned next action.
