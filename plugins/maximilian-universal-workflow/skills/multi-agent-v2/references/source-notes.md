# MultiAgentV2 Source Notes

Source evidence for `../SKILL.md` and `contract.md`.

## Pin

`@openai/codex@0.133.0-alpha.4` maps to GitHub prerelease `rust-v0.133.0-alpha.4`, published 2026-05-21. Release target is `main`; use the release URL and raw GitHub source at the tag for source-backed refreshes.

Core evidence: `codex-rs/core/src/tools/handlers/multi_agents_v2/*.rs`, `multi_agents_spec.rs`, `multi_agents_spec_tests.rs`, `multi_agents_tests.rs`, `codex-rs/core/src/session/multi_agents.rs`, and TUI multi-agent/goal files at tag `rust-v0.133.0-alpha.4`.

## Tool Contracts

- `spawn_agent`: requires `task_name`, `message`; optional `agent_type`, `fork_turns`, `model`, `reasoning_effort`, `service_tier`; returns `task_name` plus optional `nickname`.
- `send_message`: requires `target`, `message`; queue-only; accepts relative or canonical targets; can target root; no output schema; empty success text.
- `followup_task`: requires `target`, `message`; trigger-turn; resolves targets like message flow but rejects root; no output schema.
- `wait_agent`: only optional `timeout_ms`; returns `message` and `timed_out`; never completed content.
- `list_agents`: optional relative or canonical `path_prefix`; returns `agent_name`, `agent_status`, `last_task_message`; status includes strings, `completed`, `errored`.
- `close_agent`: requires `target`; rejects root; returns `previous_status`; closes live descendants.

Evidence: `create_*_tool`, v2 handlers, result structs, output-schema tests, rejection tests.

## Spawn, Fork, And Message Details

`SpawnAgentArgs` uses `serde(deny_unknown_fields)`. `fork_context` is present only to reject it with: `fork_context is not supported in MultiAgentV2; use fork_turns instead`. `AgentPath::join` creates the child path under the spawning agent path, so root spawns become `/root/task_name` and child spawns become `/root/parent/task_name`. `fork_turns` defaults to `all`; valid values are `none`, `all`, positive integer string. Full-history forks reject `agent_type`, `model`, `reasoning_effort`; `service_tier` is separate. V2 ignores depth limit and refreshes child runtime config. `send_message` sets `trigger_turn: false`; `followup_task` sets `true`; successful messages update `last_task_message`.

## Paths

`AgentPath` absolutes start with `/root` or `/morpheus`. `task_name` is one segment: not empty, not `root`/`.`/`..`, no `/`, only ASCII lowercase/digit/underscore. Relative references resolve from current path; use canonical paths for cross-branch targets. `list_agents(path_prefix=...)` uses the same relative-or-absolute task-path syntax and omits closed agents. Missing paths say `live agent path '...' not found`; duplicates say `agent path '...' already exists`.

## Wait, List, And Result Behavior

`wait_agent` returns for pending mail, any mailbox change, or timeout; it is not target-specific and strips content. Completed child results are in `list_agents` status. Root `last_task_message` is `Main thread`.

## Close, Config, Failures

`close_agent` rejects root, returns `previous_status`, shuts down target plus live descendants, removes registry entries, and releases the slot.

Current plugin runtime contract sets max concurrent threads to `32`. Current tool schema/local config use wait default/min/max `900_000`/`600_000`/`3_600_000` ms. `agents.max_threads` conflicts with v2. `hide_spawn_agent_metadata` removes role/model/reasoning/service-tier controls. `non_code_mode_only` uses `DirectModelOnly`.

`features.multi_agent_v2.root_agent_usage_hint_text` and `subagent_usage_hint_text` are injected as standalone developer messages when MultiAgentV2 is enabled. Root threads receive only root guidance; `SessionSource::SubAgent(ThreadSpawn)` receives only subagent guidance. Full-history forks filter parent MultiAgentV2 usage-hint developer messages so children receive a fresh hint matching their own session source/config.

`features.multi_agent_v2.usage_hint_text` is appended to the `spawn_agent` tool description when usage hints are enabled. User-defined agent roles are declared as `[agents.<role>]` with `description` and optional `config_file`. Role files can set `developer_instructions`; user-defined roles override built-in role declarations with the same name, including `default`, `explorer`, and `worker`.

Observed failures: acknowledgement-only completion despite correct `last_task_message`; follow-up ending in `shutdown` without useful text; repeated `running` through waits; close failing after disappearance. Refresh with `npm view @openai/codex dist-tags version --json`, `gh release view rust-v0.133.0-alpha.4 --repo openai/codex --json tagName,name,publishedAt,url,isPrerelease,targetCommitish`, and raw `gh api ...contents/<path>?ref=rust-v0.133.0-alpha.4`.
