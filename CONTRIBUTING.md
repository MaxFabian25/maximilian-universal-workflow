# Contributing

Contributions should preserve the plugin's purpose: universal, repeatable, phase-oriented Codex-native workflows for git repository workspaces.

## Guidelines

- Keep workflow policy in readable prose before adding code-based control planes.
- Prefer hard cutovers when changing skill topology or workflow contracts.
- Preserve the repo-universal assumption.
- Encourage subagent spawning where it improves speed, breadth, critique, or isolated ownership.
- Keep child-agent role boundaries explicit: leaves do their assigned packet and return results or `decision_needed`.

## Validation

Run the checks available in your local Codex environment before opening a pull request:

```bash
jq empty .agents/plugins/marketplace.json
jq empty plugins/maximilian-universal-workflow/.codex-plugin/plugin.json
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/maximilian-universal-workflow
```

When available, also run skill validation and Plugin Eval against `plugins/maximilian-universal-workflow`.
