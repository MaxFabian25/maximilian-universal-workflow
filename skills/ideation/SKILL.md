---
name: ideation
description: Use when repo evidence needs implementation options, tradeoffs, and a root-thread direction choice before planning.
---

# Ideation

Generate repo-grounded options, then converge through root-thread user choice.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/evidence-discipline.md`, `../../docs/workflow-contracts/request-user-input.md`, and `references/ideation-branches.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Tie each option to repo evidence, constraints, risks, and tradeoffs.
- Include how each option would prove the outcome, and whether it needs scratch work or a prototype to settle a material question.
- Use Codex-native subagents to compare materially different options when independent perspectives would improve tradeoff quality.
- Use `request_user_input` to choose among 2-3 concrete implementation paths when the tool is available.
- Return `decision_needed` only when `request_user_input` is unavailable or the active workflow phase cannot own the choice.
- Update the shared phase bundle with selected direction, acceptance criteria, rejected alternatives worth preserving, and a planning-ready next phase.

## Stop

Stop when audience, target behavior, risk tolerance, or decision authority is too unclear to make useful options.
