# Email Marketing Bible

By [George Hartley](https://x.com/GTHartley), co-founder of [Nitrosend](https://nitrosend.com).

**The AI email automation skill for Claude, ChatGPT, and any agent.**

Version 2.8.0, 9 October 2026.

It audits your setup, builds flows from a prompt, drafts copy in your voice, directs email design instead of accepting the model's defaults, tells you why you are in spam, and runs your ESP through MCP with a hard rule that nothing blasts without your say-so.

Built from research across 900+ sources, the experience of running [SmartrMail](https://www.smartrmail.com) (~12,000 customers, 6 billion emails, acquired 2022), and field notes from running an ESP through agents. 19 chapters, playbooks for 19 verticals, 47 curated email designs. Free and open source.

## Install

Install one, not both. In Claude Code use the plugin; a clone into `~/.claude/skills` also carries the plugin manifest and can load the skill twice.

**Claude Code (plugin, needs a recent Claude Code).** In Claude Code, run:

```
/plugin marketplace add CosmoBlk/email-marketing-bible
/plugin install email-marketing-bible@email-marketing-bible
```

**Other agents (Codex, Cursor and others that read skills):**

```bash
npx skills add CosmoBlk/email-marketing-bible
```

Or git clone the repo into that agent's skills folder.

**ChatGPT, Gemini or any single-file tool:** give it the raw core file, https://raw.githubusercontent.com/CosmoBlk/email-marketing-bible/main/SKILL.md. The core works on its own: when `references/` isn't there, it fetches the matching reference file from this repo, or the chapter from emailmarketingskill.com.

## Why this exists

In 2026 the job changed. Agents build the campaign, segment the audience, draft the copy and stage the send; the marketer directs. That only works if the agent runs on real benchmarks and hard guardrails. This skill is that discipline layer: the patterns that repeat across industries, the mistakes that destroy deliverability, the anti-slop rules for copy and design, and the send-safety gates that keep one prompt from mailing the wrong thing to your whole list.

## What the skill does

| Task | What it does |
|------|-------------|
| **Run email automation** | Build welcome, cart, post-purchase and win-back flows from a prompt, then review exits, timing and copy before anything goes live |
| **Audit your setup** | Review flows, segments, deliverability and compliance, and say what is missing |
| **Draft and de-slop copy** | Write with proven frameworks (PAS, AIDA, BAB) and strip the AI tells before send |
| **Direct email design** | Seed strings for divergence, a critic loop that scores screenshots, chained image and video models, delivery by subtraction; output as inbox-safe MJML or React Email |
| **Drive your ESP from AI** | Operate any ESP an agent can reach through MCP or an API, with pre-send gates, a session-start check of the right account, and field-tested operating rules |
| **Fix deliverability** | Step-by-step triage covering authentication, DNS changes, Gmail Postmaster v2, content and the AI-mediated inbox, plus a switching-ESP runbook |
| **Pull industry benchmarks** | Click, placed-order and revenue-per-recipient figures by vertical and email type, each with its source and date |
| **Compare platforms** | Comparison by list size, budget, and how an agent can drive each one and where approval is enforced (disclosure: the author co-founded Nitrosend, one of the platforms compared) |
| **Review compliance** | GDPR, CAN-SPAM, Washington CEMA, CASL, UK PECR, the Australian Spam Act and EU AI Act Article 50 as a gate before any send, with CCPA as a privacy note |
| **Write cold email** | Sequences with proper infrastructure separation, warming and personalisation |
| **WhatsApp, SMS and RCS** | The real cost models, consent rules and where each channel pays off |

## How to use it

Talk to your AI like an email marketing consultant.

**Audit and build:**
```
"Audit my Klaviyo account for a DTC skincare brand doing $2M/year. I have a
welcome series, abandoned cart, and one weekly newsletter. What am I missing,
and build me whatever flow would earn the most first."
```

**Fix a problem:**
```
"My emails are landing in Gmail promotions and opens dropped from 22% to 14%
over three months. What is going on and how do I fix it?"
```

**De-slop:**
```
"Here is a draft welcome email. Make it sound like a person, not an AI, and
keep it on our brand voice."
```

**Design:**
```
"Design a launch email for a premium coffee brand. List 15 directions first,
I will pick. Then build the pick as MJML and run a critic loop on the render."
```

The skill is a short core file with the rules and gates (`SKILL.md`), plus `references/` for depth: thresholds, deliverability, compliance, measurement, flows, copy, design, segmentation, cold email, messaging channels, platforms, benchmarks, playbooks, models, agent operations and sources. The agent reads a reference file only when the task needs it.

## What is inside

### 19 chapters

| # | Chapter | What you get |
|---|---------|-------------|
| 1 | The Fundamentals | Why email wins, the stack, key metrics, the AI-mediated inbox |
| 2 | Building Your List | Organic growth, popups, opt-in, spam traps, validation |
| 3 | Segmentation & Personalisation | Engagement tiers, AI-built segments, 1:1 content from behaviour |
| 4 | The Emails That Make Money | Welcome, cart, post-purchase, win-back, and building flows with AI |
| 5 | Copywriting That Converts | Subject lines, frameworks, CTAs, and the anti-slop copy protocol |
| 6 | Design & Technical | Designing for two readers, tokens and modules, dark mode, accessibility, the anti-default ban list, and directing the agent (Discover, Define, Deliver) |
| 7 | Deliverability | SPF, DKIM, DMARC, BIMI, reputation, warming, autonomous-send safety |
| 8 | Testing & Optimisation | A/B testing, significance, send-time, testing AI-assisted email |
| 9 | Analytics & Measurement | KPIs by type, attribution, querying your data with AI |
| 10 | Compliance & Privacy | GDPR, CAN-SPAM, CASL, CCPA, AU Spam Act, AI accountability |
| 11 | Industry Playbooks | Tactics for 19 verticals (see below) |
| 12 | Choosing Your Platform | Honest comparison, including which tools an agent can actually drive |
| 13 | Cold Email & B2B Outbound | Infrastructure, writing, follow-up, AI in outbound |
| 14 | WhatsApp Business | The cost model and where it pays off, per-user caps, quality tiers, opt-in and geo-branching, the AI-chatbot rule |
| 15 | SMS & RCS | TCPA, 10DLC and CTIA compliance, quiet hours, a realistic read on RCS, and AI in two-way messaging |
| 16 | AI & Agentic Marketing | Supervised autonomy, agent preflight gates, data governance, non-deterministic optimisation, what the vendors shipped, and field notes from agent-run sending |
| 17 | Company Case Studies | How Casper, Morning Brew, Duolingo, Spotify, and others use email |
| 18 | Expert Directory | The practitioners referenced throughout, who to follow and why |
| 19 | Best Email Designs 2026 | 47 hand-curated emails with notes on why each works and what to steal |

Plus four appendices: benchmarks by industry, frequency guide, marketing calendar, and methodology.

### Playbooks for 19 verticals

`Ecommerce DTC` · `SaaS B2B` · `SaaS B2C` · `Newsletter & Creator` · `Agency` · `Nonprofit` · `Healthcare` · `Financial Services` · `Real Estate` · `Travel & Hospitality` · `Education` · `Professional Services` · `Retail` · `Events` · `B2B Manufacturing` · `Restaurant & Food` · `Fitness` · `Media & Publishing` · `Marketplace & Platform`

Five are in depth in the skill; the rest are summarised, with the full playbook in Chapter 11.

### Expert contributors

Insights from practitioners including Chad S. White (Zeta Global), Joanna Wiebe (Copyhackers), Chase Dimond (Structured Agency), Nathan Barry (Kit), Ann Handley (MarketingProfs), Troy Ericson, Tyler Denk (beehiiv), Ben Settle, and many others. Full directory in Chapter 18.

## What changed in v2.8

Added:
- A short core file with the gates at the top, and 16 reference files for depth, so the rules survive context compaction.
- A session-start routine: bind to the right account first, then draft, preview and seed-test by default.
- One dated thresholds table, replacing numbers that contradicted each other across the old file.
- A DNS change protocol, a rewrite of deliverability for Gmail Postmaster Tools v2 and DMARCbis (RFC 9989), Google's deferral protocol, and a switching-ESP runbook.
- Compliance rows for Washington CEMA, UK PECR and EU AI Act Article 50, the CNIL pixel-consent rule, and a rule that deadlines, scarcity and discounts must be real.
- Design inputs before the first compose, and readers rules for inbox summarisers and the recipient's own agents.
- Flow lifecycle rules, A/B testing rules with a sample-size table, and a Gmail open-drop diagnostic.
- A dated model shelf, a permission ladder for connecting agents to ESPs, and dated examples from Grok Bot, Muse and dots.
- Further reading: popular public work on AI and email from July to October 2026.

Changed:
- Corrected the CAN-SPAM penalty ($53,088), the Spam Act caps, GDPR erasure timing, the DMARC floor (p=none at Gmail, Yahoo and Outlook), who requires one-click unsubscribe, BIMI (CMC needs no trademark), the WhatsApp AI-chatbot rule and WhatsApp's free messaging lanes (changed 1 Oct 2026).
- SPF ends `~all` on sending domains, and DMARC goes to reject only on sending subdomains, following RFC 9989.
- Seed tests to your own addresses (up to five) no longer need a separate yes. Any other single send still needs an explicit yes, and anything to more than one person still waits for "send it".
- A trigger description written in the words people use, and one version number everywhere.

Removed:
- The claim that AI summaries auto-open mail, the AI-similarity filter claim, the fixed summary window, and open-rate benchmarks and KPIs.
- Unsourced figures, including the channel ROI table and "~30x" flow revenue.

Full detail, including the old-to-new heading map, is in [CHANGELOG.md](CHANGELOG.md).

## Read the full guide

The complete Email Marketing Bible is at **[emailmarketingskill.com](https://emailmarketingskill.com)**, searchable and browsable, with all 19 chapters and 4 appendices, plus a free PDF.

## Research

Research across 900+ sources: industry reports (Litmus, Klaviyo, HubSpot, Salesforce, Validity), practitioner blogs, podcasts and transcripts, platform documentation, and community discussions. v2.8 adds a sweep of public work from July to October 2026, and every dated fact in `references/` carries a source, an evidence label and a Last checked date.

## Contributing

Found an error, better data, or a missing tactic? Issues and PRs welcome.

## License

MIT.

---

*Built by [George Hartley](https://x.com/GTHartley). Follow for updates.*
