# Review Disposition Ledger

Use this structure when review feedback contains multiple items or when the final reply needs durable evidence.

| Item | Source | Claim | Evidence checked | Acceptance criteria impact | Disposition | Action | Verification | Reply |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | user/PR/CI/agent |  | file/line, command, spec, artifact |  | fix/push back/decision_needed |  |  |  |

## Disposition Rules

- `fix`: the item is valid and scoped; implement only the needed change, then verify.
- `push back`: the item does not apply; cite repo evidence, tests, specs, or explicit support contracts.
- `decision_needed`: the item is ambiguous, changes scope, changes architecture, conflicts with instructions, lacks required evidence, or belongs to a later owner; call root-thread `request_user_input`.

## Reply Patterns

- `Fixed in <path>: <what changed>. Verified with <command/check>.`
- `Keeping current approach: <evidence-backed reason>.`
- `Need decision on <item>: <specific implementation-path choice, missing evidence, or owner>.`

Keep replies technical and brief. Do not use social filler as a substitute for a disposition.
