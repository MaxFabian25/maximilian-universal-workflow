---
name: exploration
description: Use when repo exploration is needed.
---

# Exploration

Gather repo evidence before decisions, edits, verification, review.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/explorer-packets.md`.

## Do

- Prefer `rg`, `rg --files`, direct reads, and non-mutating commands.
- Parent sends self-contained explorer packets; leaves do only their packet.
- Cite file, command, branch/status, test, log, or source evidence.
- Synthesize findings and choose the next phase.

## Stop

Stop when evidence conflicts, fanout overlaps, or a user decision is required.
