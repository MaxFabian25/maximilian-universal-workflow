# Contributing

Contributions should preserve the plugin's purpose: universal, repeatable, phase-oriented Codex-native workflows for git repository workspaces.

## Guidelines

- Keep workflow policy in readable prose before adding code-based control planes.
- Prefer hard cutovers when changing skill topology or workflow contracts.
- Preserve the repo-universal assumption.
- Keep execution ownership explicit where it improves speed, breadth, critique, or isolation.
- Keep ownership boundaries explicit: each task owns its assigned scope and returns results or `decision_needed`.

## Validation

Run the checks available in your local Codex environment before opening a pull request:

```bash
jq empty .agents/plugins/marketplace.json
jq empty .codex-plugin/plugin.json
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

When available, also run skill validation against the repository root.
