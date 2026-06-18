# Decision Interrogation

Use this contract when a plan, direction, review response, cleanup, or handoff depends on a material choice.

## Core Rule

Ask only for decisions that repo evidence cannot settle and that change scope, side effects, ownership, proof surface, risk, closeout, or approval.

## Process

1. Inspect first when the answer is discoverable from files, commands, docs, prior decisions, or current repo state.
2. Ask one material question at a time when conversation is needed.
3. Provide the recommended answer and the tradeoff behind it.
4. Use Codex-native `request_user_input` when there are 2-3 concrete, mutually exclusive options.
5. Preserve decisions, assumptions, rejected alternatives, and remaining uncertainty in the phase bundle.
6. Stop only when the next answer changes a material boundary.

Do not emulate `request_user_input` with prose menus when the tool is available. Do not ask for low-risk implementation details that existing conventions, tests, or approved plans decide.

## Phase Hooks

- exploration: answer factual questions with repo evidence before asking the user.
- ideation: interrogate options, tradeoffs, proof strategy, and selected direction.
- planning: interrogate only unresolved execution blockers or material ownership choices.
- receiving-review and review: interrogate disputed feedback only when evidence cannot settle it.
- handoff: interrogate closeout only when more than one material owner or action remains.
