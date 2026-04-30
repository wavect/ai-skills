# Contributing to Wavect AI Skills

Thank you for your interest. This repository contains open-source AI agent
skills published by Wavect GmbH. Contributions that improve the quality,
accuracy, or breadth of the skills are welcome.

## What makes a good contribution

- **Corrections**: frameworks cited incorrectly, outdated advice, broken links
- **Improvements**: sharper questions, better anti-patterns, clearer output templates
- **New skills**: additional product/go-to-market skills in the same spirit
  (founder-focused, framework-grounded, direct, actionable)

## What does not belong here

- Promotional content or advertising
- Skills outside the product strategy / go-to-market domain
- Vague or generic advice that could appear in any business blog

## Skill format

Each skill lives in its own directory:

```
skill-name/
└── SKILL.md
```

`SKILL.md` must include a YAML frontmatter block at the top:

```yaml
---
schema: skill-md/1.0
name: skill-name
version: 1.0.0
provider: Your Name or Org
contact: your@email.com
---
```

Recommended sections: Purpose, When to Activate, Frameworks / Question Framework,
Output template, Anti-Patterns, Progression Logic (by stage).

## Updating index.json

After adding or editing a `SKILL.md`, regenerate its SHA-256 digest and update
`index.json`:

```bash
shasum -a 256 skill-name/SKILL.md
```

Update the corresponding `digest` field in `index.json` with the result prefixed
by `sha256:`.

## Pull request process

1. Fork the repository
2. Create a branch: `git checkout -b skill/your-skill-name`
3. Add or edit the `SKILL.md` file
4. Update `index.json` with the correct digest
5. Open a pull request with a short description of what changed and why

All PRs are reviewed by the Wavect team. We may suggest edits for tone,
accuracy, or alignment with the existing skill style before merging.

## Questions

Open an issue or email office@wavect.io.
