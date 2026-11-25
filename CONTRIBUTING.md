# Contributing to Wavect AI Skills

Start with a decision an agent got wrong, a missing input that changed its advice, or a method whose source has changed. Put the skill's purpose and activation conditions in the frontmatter description. Keep the workflow and a worked example in `SKILL.md`. Put optional methods in `reference/` and link them relative to the entry point. This path also serves existing website links. [Agent Skills specification](https://agentskills.io/specification) · [Skill authoring practices](https://agentskills.io/skill-creation/best-practices)

Use a neighboring skill as a frontmatter example. Keep the directory and skill name identical. Use standard top-level fields and place Wavect's version, schema, provider and contact under `metadata` as strings. Increment the version when the published instructions change.

## Check a change

Run these commands from the repository root with Python 3 and PyYAML installed. Add a catalogue row to `index.json` for a new skill. The script fills in its description, raw URL and digest.

```sh
python3 scripts/registry.py
python3 scripts/registry.py --check
```

Use the relevant scenario in the evaluation set with a fresh agent. Give it only the prompt, skill and supplied inputs. Review the result against the decision criteria. Include the observed behavior and any correction in the pull request. [Behavioral checks](evals/scenarios.md)

## Publish the website copy

Copy the six published skill directories into `themes/raditiy/static/.well-known/agent-skills/` in the Wavect homepage checkout. Synchronize the affected directory only when updating one skill. In that checkout, update the affected skill descriptions and example prompts in the four localized `pages.yml` files and run `npm run generate:agent-skills`. Follow the homepage's discovery and rendered verification guide.

From this repository, compare the checked-out copies before opening the two pull requests.

```sh
python3 scripts/registry.py --check --site-root /path/to/Wavect_Tech_Homepage
```
