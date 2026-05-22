---
name: ideation
description: Use when repo evidence needs implementation options, tradeoffs, and a root-thread direction choice before planning.
---

# Ideation

Generate repo-grounded options, then converge through root-thread user choice.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/ideation-branches.md`.

## Do

- Tie each option to repo evidence, constraints, risks, and tradeoffs.
- Use root-thread `request_user_input` to choose among 2-3 concrete implementation paths.
- Use the root thread for user-facing choices; child agents return `decision_needed`.
- Update the shared phase bundle with selected direction, acceptance criteria, rejected alternatives worth preserving, and a planning-ready next phase.

## Stop

Stop when audience, target behavior, risk tolerance, or decision authority is too unclear to make useful options.
