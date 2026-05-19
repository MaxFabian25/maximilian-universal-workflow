---
name: ideation
description: Use when repo ideation is needed.
---

# Ideation

Generate repo-grounded options, then converge through root-thread user choice.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/ideation-branches.md`.

## Do

- Tie each option to repo evidence, constraints, risks, and tradeoffs.
- Use `request_user_input` for two or three concrete branch choices when available.
- Use the root thread for user-facing choices; child agents return `decision_needed`.
- End with a selected direction ready for `planning`.

## Stop

Stop when audience, target behavior, risk tolerance, or decision authority is too unclear to make useful options.
