# Work Item Shaping

Use this contract when turning a request, finding, plan, PRD, issue, review thread, or handoff into work another agent or human can pick up.

## Core Rule

A shaped work item describes end-to-end behavior, acceptance criteria, proof surface, ownership, non-goals, and destination without depending on hidden conversation context.

## Work Item Forms

Work items may be tracker issues, repo docs, PRDs, plan tasks, handoff packets, review findings, HTML support reports, or inline next prompts. Publishing to an issue tracker is an optional destination, not the contract itself.

## Process

1. Gather context first: request, prior decisions, current repo state, evidence, and related work.
2. For bugs or disputed outputs, reproduce or bound the symptom when feasible before shaping.
3. Write behavior-first briefs: current state, desired state, acceptance criteria, proof surface, scope, non-goals, and owner.
4. Prefer durable language over fragile file paths unless exact paths are necessary for the worker.
5. Split large work into vertical tracer slices that are independently demoable or verifiable.
6. Use `request_user_input` for granularity, destination, or ownership choices when 2-3 concrete options remain.
7. Publish, comment, close, or label only with explicit side-effect approval and the relevant external tool authority.

## Phase Hooks

- exploration: gather request evidence, prior decisions, and reproduction status.
- ideation: choose brief, PRD, slice, or report strategy.
- planning: convert shaped work into executable task order and ownership.
- review and receiving-review: shape findings into fix, reject, defer, or decision-needed items.
- handoff: preserve unpublished work items or publish only with approved destination and side effects.
