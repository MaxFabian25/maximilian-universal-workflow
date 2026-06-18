# Vocabulary And Decision Capture

Use this contract when repo work changes the terms, concepts, or durable decisions future agents must understand.

## Core Rule

Preserve shared language and durable decisions where the repo already keeps authority. Create new vocabulary or decision files only when a real term or decision crystallizes.

## Vocabulary

- Read existing glossary, context, schema, naming, and decision files when present.
- Challenge overloaded, conflicting, or vague terms immediately.
- Propose canonical terms and avoid terms when they reduce ambiguity.
- Use concrete scenarios to test where one term ends and another begins.
- Keep glossary-style entries free of implementation detail unless the repo convention says otherwise.

Default to existing repo conventions. If none exist and durable vocabulary is needed, use `CONTEXT.md` for a single context or `CONTEXT-MAP.md` when multiple contexts need separate glossaries.

## Decisions

Capture a decision when all are true:

- it is hard enough to reverse that future agents need the reason;
- it would be surprising without context;
- it resolved a real tradeoff among plausible alternatives.

Skip decision records for obvious, temporary, or easy-to-reverse choices. When captured, include decision, context, alternatives, tradeoffs, consequences, date, and owner.

## Phase Hooks

- exploration: read vocabulary and decision records as evidence.
- ideation: sharpen terms and preserve selected or rejected conceptual choices.
- planning: include vocabulary or decision files in scope only when they are part of the durable outcome.
- execution: update vocabulary and decisions alongside the work that made them true.
- review: check terminology drift, duplicated decisions, and missing decision authority.
- handoff: report new, changed, or unresolved vocabulary and decisions.
