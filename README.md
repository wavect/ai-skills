# Wavect AI Skills

Six MIT-licensed Agent Skills for product, go-to-market and engineering decisions. Choose a skill by the question you need to answer. Supply the evidence you already have, even if it is incomplete.

| Skill | Question | What to bring |
| --- | --- | --- |
| [PMF Advisor](pmf-advisor/SKILL.md) | Should you increase acquisition spend? | Survey counts, eligible cohorts or a recent customer workaround |
| [ICP Discovery](icp-discovery/SKILL.md) | Who buys when the problem becomes urgent? | A win, a loss and the buyer's timeline |
| [Pricing Strategy](pricing-strategy/SKILL.md) | Which price should you test next? | Comparable quotes, paid deals and delivery costs |
| [QA Advisor](qa-advisor/SKILL.md) | Would your tests catch the release risk? | A diff, failing workflow or test excerpt |
| [Website ICP-Fit Auditor](website-icp-fit/SKILL.md) | Does the page deliver what brought the buyer there? | An existing page, the intended buyer and the entry channel |
| [High-Ticket Conversion Architect](high-ticket-conversion-architect/SKILL.md) | What proof can you publish for a premium offer? | Offer scope, price, buyer and approved proof |

## Try one

Open a skill page and use the starter prompt, replacing the example with your own facts. You can also give a URL-capable agent the raw skill URL and your task. [Wavect skills catalogue](https://wavect.io/skills/)

> Read https://raw.githubusercontent.com/wavect/ai-skills/main/pmf-advisor/SKILL.md. We have 20 survey replies and 14 people would be very disappointed if our product disappeared. What else should we check before raising ad spend?

## Install in a project

From your project root, copy the entire selected directory from a local clone into your agent's skills directory. This keeps the method references available offline. For Claude Code, for example, replace the source path below with your clone location.

```sh
mkdir -p .claude/skills
cp -R /path/to/ai-skills/pmf-advisor .claude/skills/
```

Invoke the installed skill with `/pmf-advisor` in Claude Code and add your question. For another agent, use its project-level skills directory. [Claude Code skills](https://code.claude.com/docs/en/skills)

## Discovery and maintenance

The registry lists each entry point with a SHA-256 digest of its exact bytes. The website mirrors the six skill directories and serves its own discovery index. [GitHub registry](https://raw.githubusercontent.com/wavect/ai-skills/main/index.json) · [Wavect registry](https://wavect.io/.well-known/agent-skills/index.json)

See the contributor guide for how to update a skill, run its behavioral checks, and verify that both copies match. [Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)
