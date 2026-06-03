# MultiAgentV2 Source Notes

Source evidence for `../../skills/multi-agent-v2/SKILL.md` and `../../skills/multi-agent-v2/references/contract.md`.

## Pin

`@openai/codex@0.137.0-alpha.4` maps to GitHub prerelease `rust-v0.137.0-alpha.4`, published 2026-06-03. Release target is `main`; use the release URL and raw GitHub source at the tag for source-backed refreshes. The local `codex --version` used for this refresh reported `codex-cli 0.137.0-alpha.4`. `npm view @openai/codex dist-tags version --json` reported `alpha: 0.137.0-alpha.4`.

Core evidence: `codex-rs/core/src/tools/handlers/multi_agents_v2/*.rs`, `codex-rs/core/src/tools/handlers/multi_agents_spec.rs`, `multi_agents_spec_tests.rs`, `multi_agents_tests.rs`, `codex-rs/core/src/session/multi_agents.rs`, goal tool specs in `codex-rs/core/src/tools/handlers/goal_spec.rs`, and TUI multi-agent/goal files at tag `rust-v0.137.0-alpha.4`. The current v2 handler directory contains `close_agent.rs`, `followup_task.rs`, `list_agents.rs`, `message_tool.rs`, `send_message.rs`, `spawn.rs`, and `wait.rs`.

Refresh evidence also included merged upstream PRs: #25266 "Set multi-agent v2 dogfood defaults", #25267 and #25636 for the `followup_task` hard cutover, #25720/#25721/#25722 for multi-agent runtime metadata and per-thread runtime resolution, #25723/#25724 runtime selector tests, and #25841 startup prewarm alignment with resolved multi-agent runtime.

## Tool Contracts

- `spawn_agent`: requires `task_name`, `message`; optional `agent_type`, `fork_turns`, `model`, `reasoning_effort`, `service_tier`; returns `task_name` plus optional `nickname`.
- `send_message`: requires `target`, `message`; queue-only; accepts relative or canonical targets; can target root; no output schema; empty success text.
- `followup_task`: requires `target`, `message`; trigger-turn; resolves targets like message flow, rejects root, and has no output schema. This is the canonical v2 follow-up tool; do not document or use compatibility paths.
- `wait_agent`: only optional `timeout_ms`; returns `message` and `timed_out`; never completed content.
- `list_agents`: optional relative or canonical `path_prefix`; returns `agent_name`, `agent_status`, `last_task_message`; status includes strings, `completed`, `errored`.
- `close_agent`: requires `target`; rejects root; returns `previous_status`; closes live descendants.

Evidence: `create_*_tool`, v2 handlers, result structs, output-schema tests, rejection tests.

## Spawn, Fork, And Message Details

`SpawnAgentArgs` uses `serde(deny_unknown_fields)`. `fork_context` is present only to reject it with: `fork_context is not supported in MultiAgentV2; use fork_turns instead`. `AgentPath::join` creates the child path under the spawning agent path, so root spawns become `/root/task_name` and child spawns become `/root/parent/task_name`. `fork_turns` defaults to `all`; valid values are `none`, `all`, positive integer string. Full-history forks reject `agent_type`, `model`, `reasoning_effort`; `service_tier` is separate. V2 ignores depth limit, applies runtime overrides, and passes selected environments into spawned agents. `send_message` sets `trigger_turn: false`; `followup_task` sets `true`; successful messages update `last_task_message`.

## Paths

`AgentPath` absolutes start with `/root` or `/morpheus`. `task_name` is one segment: not empty, not `root`/`.`/`..`, no `/`, only ASCII lowercase/digit/underscore. Relative references resolve from current path; use canonical paths for cross-branch targets. `list_agents(path_prefix=...)` uses the same relative-or-absolute task-path syntax and omits closed agents. Missing paths say `live agent path '...' not found`; duplicates say `agent path '...' already exists`.

## Wait, List, And Result Behavior

`wait_agent` returns for pending mail, any mailbox change, or timeout; it is not target-specific and strips content. Completed child results are in `list_agents` status. Root `last_task_message` is `Main thread`.

## Close, Config, Failures

`close_agent` rejects root, returns `previous_status`, shuts down target plus live descendants, removes registry entries, and releases the slot.

Current plugin runtime contract sets max concurrent threads to `32` and wait default/min/max to `900_000`/`600_000`/`3_600_000` ms. `features.multi_agent_v2.max_concurrent_threads_per_session` is the thread-cap surface; do not reintroduce `agents.max_threads`. `hide_spawn_agent_metadata` removes role/model/reasoning/service-tier controls. `non_code_mode_only` uses `DirectModelOnly`.

`features.multi_agent_v2.root_agent_usage_hint_text` and `subagent_usage_hint_text` are injected as standalone developer messages when MultiAgentV2 is enabled. Root threads receive only root guidance; `SessionSource::SubAgent(ThreadSpawn)` receives only subagent guidance. Full-history forks filter parent MultiAgentV2 usage-hint developer messages so children receive a fresh hint matching their own session source/config.

`features.multi_agent_v2.usage_hint_text` is appended to the `spawn_agent` tool description when usage hints are enabled. User-defined agent roles are declared as `[agents.<role>]` with `description` and optional `config_file`. Role files can set `developer_instructions`; user-defined roles override built-in role declarations with the same name, including `default`, `explorer`, and `worker`.

`0.137.0-alpha.4` persists multi-agent runtime metadata and resolves the runtime per thread before the first turn and startup prewarm. Configured hints and role files remain the workflow-level control surface; source-backed diagnostics should verify the resolved runtime when behavior differs between local, remote, root, and spawned sessions.

Observed failures to keep handling at the workflow layer: acknowledgement-only completion despite correct `last_task_message`; follow-up ending in `shutdown` without useful text; repeated `running` through waits; close failing after disappearance. Refresh with `npm view @openai/codex dist-tags version --json`, `gh release view rust-v0.137.0-alpha.4 --repo openai/codex --json tagName,name,publishedAt,url,isPrerelease,targetCommitish`, and raw `gh api ...contents/<path>?ref=rust-v0.137.0-alpha.4`.
