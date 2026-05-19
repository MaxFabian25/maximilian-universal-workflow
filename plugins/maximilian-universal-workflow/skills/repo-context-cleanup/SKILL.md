---
name: repo-context-cleanup
description: Use when stale repo context needs cleanup.
---

# Repo Context Cleanup

Clean stale agent context while preserving live authority.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/cleanup-playbook.md`. Active instructions/specs/docs outrank this skill.

## Avoid

- Ordinary source refactoring.
- Active source, tests, schemas, tooling, or preserved archives.

## Do

- Identify `AGENTS.md`, cleanup conventions, and authority first.
- Classify as authority, archive, stale bloat, generated evidence, or uncertain.
- Actions: delete, archive, consolidate, rewrite as authority, or leave.
- Use `request_user_input` from the root thread for delete vs archive vs report-only policy choices.
- Do not delete uncertain items without explicit approval.

## Stop

Stop when ownership, archive rules, authority, or delete permission is unclear.
