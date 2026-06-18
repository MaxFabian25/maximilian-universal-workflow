# Proof-First Change

Use this contract before material repo mutation in code, docs, data, config, research, cleanup, generated outputs, workflow contracts, or operations.

## Core Rule

A material change needs a proof surface before mutation, a current baseline or gap, the smallest useful change, and fresh proof before any completion claim.

## Loop

1. State the claim, acceptance criterion, or risk the change must prove.
2. Choose the proof surface: command, checklist, source set, query, calculation, dry-run, screenshot, prototype, manual check, rendered output, schema validation, or test.
3. Prove baseline or red capability: show the current gap, failure, absence, disputed state, or check that would catch the wrong outcome. If this is impossible, record why and route risk through `request_user_input` when needed.
4. Make one minimal change inside approved ownership and side-effect boundaries.
5. Rerun the same proof surface and relevant regressions against current repo state.
6. Refine only after proof; rerun proof when refinement can affect the outcome.
7. Record completion evidence, residual gaps, and scratch-work disposition.

## Anti-Cheat Rules

- Do not weaken proof to make the change pass.
- Do not silently change acceptance criteria.
- Do not rely on old output or subagent summaries as proof.
- Do not stack speculative edits before checking the current proof surface.
- Do not treat tests as the only valid proof surface for non-software work.

## Phase Hooks

- planning: each task names a proof surface and expected baseline signal.
- execution: preserve or establish proof-first state before write-owning mutation.
- verification: map acceptance criteria to fresh proof output.
- review: check that proof surfaces actually match acceptance criteria.
- handoff: report proof commands or checks, status, gaps, and owner.
