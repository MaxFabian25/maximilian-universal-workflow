---
name: verification
description: Use when execution claims need fresh current-state proof mapped to acceptance criteria and goal state.
---

# Verification

Prove completion claims with fresh repo-state evidence.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/evidence-discipline.md`, `../../docs/workflow-contracts/proof-first-change.md`, `../../docs/workflow-contracts/information-structure.md`, `../../docs/workflow-contracts/request-user-input.md`, and `../../docs/workflow-contracts/native-tool-map.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Run or identify the command/checklist proving the claim in the current repo state.
- Map acceptance criteria to command/check evidence, exit status, pass/fail counts, and unverified gaps.
- Verify information-structure changes through links, imports, paths, schemas, commands, rendered outputs, or reference checks when relevant.
- Treat summaries and old output as inputs, not proof.
- Use Codex-native subagents for independent proof checks when the proof surface is broad, specialized, or easy to misread.
- Confirm scratch work is deleted, archived, folded into durable work, or assigned a residual owner before reporting success.
- Call `get_goal` before `update_goal`; mark the goal complete only when the active objective matches the verified outcome and no required work remains. When completing a budgeted goal, report final token usage from the tool result.
- If verification cannot run, state exactly why and what risk remains.
- On pass, update the shared phase bundle and continue to `review`. On fail, return to `execution` when repair is clear and in scope. Use `request_user_input` only for residual-risk, scope, side-effect, or stop-with-evidence choices. When the user selects stop-with-evidence or accepts residual risk after a failed verification, route to `handoff` without marking the work complete.

## Stop

Stop when the proving command is unknown, running it would require unapproved destructive/external action, or verification fails without an approved execution route or user disposition.
