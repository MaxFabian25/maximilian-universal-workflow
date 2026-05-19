# Changelog

## 0.1.2

- Adds direct-question fallback language when `request_user_input` is unavailable.

## 0.1.1

- Improves general plugin invocation by making `intake` run the phase loop instead of only routing.
- Changes `goal-planning` to produce a plan plus a goal-prefixed `execution` launch prompt.
- Clarifies that `/goal` objectives target executed repository end states, not planning tasks.

## 0.1.0

- Initial public release of Maximilian Universal Workflow.
- Adds universal phase-oriented Codex workflows for git repository workspaces.
- Bundles phase skills for intake, exploration, ideation, planning, goal planning, execution, verification, review, handoff, and repository context cleanup.
- Bundles `multi-agent-v2` as the canonical future copy for Codex native subagent coordination.
