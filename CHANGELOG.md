# Changelog

## Unreleased

- Adds a cross-domain evidence discipline contract for proof surfaces, tight feedback loops, scratch work, subagent evidence, review feedback disposition, and completion gates across repo workflows.
- Refreshes goal-tool guidance for Codex `0.137.0-alpha.4`: workflow-invoked planning explicitly authorizes default goal creation after gates pass, `token_budget` is explicit-only, budgeted goal completion reports final usage, and blocked goals require the same blocker across at least three consecutive goal turns.
- Adds phase guidance for Codex-native subagent use when it improves exploration, planning, execution, verification, review, or handoff quality.

## 0.1.15

- Refreshes Codex `0.136.0-alpha.1` runtime setup paths, aligns native tool mappings with current goal tools, and tightens interactive choice gates.
- Aligns source docs and skills with the v0.1.15 default goal-backed workflow semantics: normal invocations create the default native goal after decision-complete planning unless the user explicitly asks for planning-only, no-goal, or stop-with-evidence behavior.
- Removes stale CSV batch guidance, makes planning goal creation conditional in the agent prompt, and adds phase-bundle/transition reads to mutating review and cleanup side paths.

## 0.1.14

- Adds the shared phase bundle contract, routes phase transitions through `continue_now`, and adds a standalone HTML artifact template for substantial workflow evidence dashboards.

## 0.1.13

- Corrects the lifecycle playbook headline chain to include `git-worktrees` between planning and execution.

## 0.1.12

- Adds `git-worktrees` for isolated branch workspaces before execution and wires worktree setup into the repo phase contracts.

## 0.1.11

- Adds shared phase-transition and request-user-input contracts, makes substantial runs artifact-backed, tightens native goal identity handling, and carries acceptance criteria through verification and handoff.

## 0.1.10

- Removes remaining soft-path workflow wording for native goal completion, validation, and review disposition.

## 0.1.9

- Requires native goal tools for goal-backed planning and removes non-native goal paths.

## 0.1.8

- Makes goal-backed planning tool-first, adds phase decision gates, standardizes stop payloads, and clarifies interactive HTML artifacts.

## 0.1.7

- Makes `/goal` the default planning behavior and removes the separate `/goal` planning front door.

## 0.1.6

- Adds runtime setup guidance for the plugin's Codex-native workflow surfaces.

## 0.1.5

- Adds `receiving-review` for triaging received review feedback before changing repo code or workflow artifacts.

## 0.1.4

- Makes root-thread `request_user_input` the expected liberal choice mechanism.

## 0.1.1

- Improves general plugin invocation by making `intake` run the phase loop instead of only routing.
- Changes planning to produce a plan plus goal-backed execution setup.
- Clarifies that `/goal` objectives target executed repository end states, not planning tasks.

## 0.1.0

- Initial public release of Maximilian Universal Workflow.
- Adds universal phase-oriented Codex workflows for git repository workspaces.
- Bundles phase skills for intake, exploration, ideation, goal-backed planning, execution, verification, review, handoff, and repository context cleanup.
