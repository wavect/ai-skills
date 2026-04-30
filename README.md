# Wavect AI Skills

**Open-source agent skills for founders building products that actually sell.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-v0.2.0-green)](index.json)
[![Skills](https://img.shields.io/badge/Skills-3-orange)](index.json)
[![Provider](https://img.shields.io/badge/Provider-Wavect%20GmbH-black)](https://wavect.io)

---

These are [Agent Skills](https://agentskills.io) — structured instruction files
that give AI agents (Claude, Cursor, Copilot, and others) deep, opinionated
expertise in specific domains. This collection focuses on the three decisions
that most often determine whether a software product succeeds or dies:

| Skill | What it does |
|---|---|
| [pmf-advisor](pmf-advisor/SKILL.md) | Validates ideas, prioritizes roadmaps, and assesses PMF using RICE, JTBD, Value Proposition Canvas, and the Sean Ellis Test |
| [icp-discovery](icp-discovery/SKILL.md) | Destroys vague "anyone who..." ICPs through 6 stages of iterative questioning — behavioral, situational, economic, and channel profiling |
| [pricing-strategy](pricing-strategy/SKILL.md) | Finds the right value metric, pricing model, and price point using Van Westendorp, WTP interviews, and tier structuring frameworks |

Built by [Wavect GmbH](https://wavect.io) — "More than Engineers. Build to Sell."

---

## Quickstart

### Claude Code

```bash
# Install a single skill for the current project
cp -r pmf-advisor .claude/skills/

# Or install all three
for skill in pmf-advisor icp-discovery pricing-strategy; do
  mkdir -p .claude/skills/$skill
  curl -sL https://raw.githubusercontent.com/wavect/ai-skills/main/$skill/SKILL.md \
    -o .claude/skills/$skill/SKILL.md
done
```

Then in Claude Code:

```
/skills pmf-advisor
```

### Cursor / VS Code / other agents

Copy the `SKILL.md` file from any skill directory into your project's
`.claude/skills/` folder (Claude Code) or wherever your agent loads skill
context from. The SKILL.md format is tool-agnostic.

### Load directly from URL

Point your agent at the raw GitHub URL:

```
https://raw.githubusercontent.com/wavect/ai-skills/main/pmf-advisor/SKILL.md
https://raw.githubusercontent.com/wavect/ai-skills/main/icp-discovery/SKILL.md
https://raw.githubusercontent.com/wavect/ai-skills/main/pricing-strategy/SKILL.md
```

---

## Skills

### PMF Advisor

> *"Most software projects don't lack engineers, they lack product experience."*

Activates when you need to validate an idea, prioritize a backlog, or figure
out why traction isn't converting into retention.

**Frameworks included:**
- RICE Scoring — prioritize roadmap items by evidence, not gut feeling
- Jobs-to-Be-Done — surface the emotional job behind the functional request
- Value Proposition Canvas — map pains/gains to your actual offering
- Sean Ellis Test — the 40% threshold that separates PMF from delusion

**Output:** PMF Risk Assessment → Recommended Framework → Diagnostic Questions → Next Step

[View SKILL.md →](pmf-advisor/SKILL.md)

---

### ICP Discovery

> *"You cannot market to everyone. Everyone is no one."*

The most misused term in early-stage startups is "ICP." This skill will not
let you get away with "SMBs," "SaaS companies," or "people who need X." It
works through six stages until you can picture one specific human at their
desk with a specific problem.

**Frameworks included:**
- YC / Michael Seibel — "Hair on Fire" customer identification
- Steve Blank — behavior over demographics (work backwards from who paid)
- Rob Fitzpatrick — Mom Test applied to ICP qualification
- Peter Thiel — dominate the smallest market first, then expand
- April Dunford — position for the customer where you are the obvious choice

**Output:** ICP Card — role, triggering situation, burning problem, behavior today, economic profile, top 3 channels, riskiest assumption, beachhead size estimate

[View SKILL.md →](icp-discovery/SKILL.md)

---

### Pricing Strategy

> *"Your price is a signal. Undercharging says you don't believe in your own value."*

Most founders underprice by 2–5x. This skill starts by identifying the right
value metric (the unit pricing should scale on), then picks the right model,
then finds the right number — in that order. It never starts with the number.

**Frameworks included:**
- Patrick Campbell — value metric identification (the most leveraged pricing decision)
- Van Westendorp Price Sensitivity Meter — 4-question method to find acceptable price range
- Willingness-to-Pay interviews — how to ask without anchoring the answer
- Simon-Kucher pricing waterfall — discount and packaging discipline
- Tier structure principles — why 3 tiers, what goes where, upgrade trigger design

**Output:** Pricing Strategy Card — value metric, recommended model, price range, tier structure, upgrade trigger feature, biggest pricing risk, next experiment

[View SKILL.md →](pricing-strategy/SKILL.md)

---

## Agent Discovery

This repository publishes a machine-readable skill index at:

```
https://raw.githubusercontent.com/wavect/ai-skills/main/index.json
```

The index follows the [Agent Skills Discovery RFC v0.2.0](https://github.com/cloudflare/agent-skills-discovery-rfc)
and includes SHA-256 digests for each skill file so agents can verify integrity.

For sites that use the `.well-known` discovery pattern (e.g. `isitagentready.com`),
Wavect's skills are also published at:

```
https://wavect.io/.well-known/agent-skills/index.json
```

---

## About Wavect

[Wavect GmbH](https://wavect.io) is an Austrian software product studio that
helps startups and corporates hit Product-Market Fit. We combine technical
execution with product strategy — the two things most agencies pick one of.

**Services:**
- **Fractional Co-Founders** — strategic + technical co-founder, 0% equity, from €400/week
- **Software Development** — full-stack from MVP to scale (Web, Mobile, Web3, AI)
- **Software Quality Assurance** — manual + automated testing, from €750/week

These skills are our methodology made public. We use the same frameworks in
client engagements. If you want a sparring partner who has done this with real
products, [book a free call](https://zeeg.me/wavect/call).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: corrections, sharper
questions, and new product/go-to-market skills in the same spirit are welcome.
When editing a `SKILL.md`, regenerate the digest and update `index.json`:

```bash
shasum -a 256 skill-name/SKILL.md
# then update the digest field in index.json
```

---

## License

MIT — see [LICENSE](LICENSE). Use, fork, and adapt freely. Attribution
appreciated but not required.
