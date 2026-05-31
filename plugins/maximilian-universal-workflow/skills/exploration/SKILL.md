---
name: exploration
description: Use when repo evidence is missing or uncertain and read-only investigation or explorer fanout should precede later phases.
---

# Exploration

Gather repo evidence before decisions, edits, verification, review.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/explorer-packets.md`.

## Do

- Prefer `rg`, `rg --files`, direct reads, and non-mutating commands.
- Parent sends self-contained explorer packets; leaves do only their packet.
- Cite file, command, branch/status, test, log, or source evidence.
- Update the shared phase bundle with evidence, uncertainty, next phase, and artifact state.
- When evidence is sufficient, continue to ideation or planning. When evidence conflicts, use `request_user_input` for the next probe or stop path.

## Stop

Stop when evidence conflicts, fanout overlaps, or a user decision is required.
