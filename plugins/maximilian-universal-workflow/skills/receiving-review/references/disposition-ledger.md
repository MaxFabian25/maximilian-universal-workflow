# Review Disposition Ledger

Use this structure when review feedback contains multiple items or when the final reply needs durable evidence.

| Item | Source | Claim | Evidence checked | Disposition | Action | Verification | Reply |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | user/PR/CI/agent |  | file/line, command, spec, artifact | fix/push back/escalate/defer |  |  |  |

## Disposition Rules

- `fix`: the item is valid and scoped; implement only the needed change, then verify.
- `push back`: the item does not apply; cite repo evidence, tests, specs, or explicit support contracts.
- `escalate`: the item is ambiguous, changes scope, changes architecture, or conflicts with instructions; call root-thread `request_user_input`.
- `defer`: evidence is missing or the fix belongs to a later owner; state what evidence or owner is needed.

## Reply Patterns

- `Fixed in <path>: <what changed>. Verified with <command/check>.`
- `Keeping current approach: <evidence-backed reason>.`
- `Need decision on <item>: <specific branch choice>.`
- `Deferred: <missing evidence or owner>.`

Keep replies technical and brief. Do not use social filler as a substitute for a disposition.
