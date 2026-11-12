# Email Marketing Bible

An email marketing skill for AI agents. Your agent plans, writes, designs, audits and sends email with it, and nothing goes to more than one person until you type "send it".

Works in Claude (web, desktop, Cowork and Claude Code), Codex, Cursor, ChatGPT and any agent that reads skills. Free, MIT licensed and vendor-neutral: it works with the email platform you already use.

**[Download for Claude (ZIP)](https://github.com/CosmoBlk/email-marketing-bible/releases/latest/download/email-marketing-bible.zip)** · [All install options](#install) · [Read the guide](https://emailmarketingskill.com)

By [George Hartley](https://www.linkedin.com/in/gthartley/), who founded [SmartrMail](https://smartrmail.com/about) (email marketing for about 12,000 ecommerce stores, sold to Relay Commerce in 2022) and co-founded [Nitrosend](https://nitrosend.com). Disclosure: Nitrosend is one of the platforms the skill compares.

Version 2.8.4, 12 November 2026.

## Install

| You use | Do this |
|---|---|
| Claude on the web or the desktop app, any plan | [Upload the ZIP](#claude-on-the-web-or-desktop-upload-the-zip) (2 minutes) |
| Claude on a paid plan | [Add it as a plugin](#claude-on-a-paid-plan-add-the-plugin), which also carries it into Cowork and Claude Code |
| Claude Code | [Two commands](#claude-code) |
| Codex, Cursor, Gemini CLI and other agents | `npx skills add CosmoBlk/email-marketing-bible` |
| ChatGPT or another chat app | [Paste one prompt](#chatgpt-gemini-or-any-chat-app) |

Pick one route per Claude account. The ZIP and the plugin together load the skill twice.

### Claude on the web or desktop: upload the ZIP

1. Download [email-marketing-bible.zip](https://github.com/CosmoBlk/email-marketing-bible/releases/latest/download/email-marketing-bible.zip) and keep it zipped. If your Mac unzips it, right-click the folder and choose **Compress**.
2. In Claude, open **Settings > Capabilities** and turn on **Code execution and file creation** (newer layouts call it **Create and edit files**).
3. Open **Customize > Skills**, click **+**, then **Create skill**, then **Upload a skill**, and choose the ZIP. Check it is switched on.
4. Start a new chat and try:

```
Use the Email Marketing Bible to plan a three-email welcome series for my
business. Ask me what you need first, and keep everything as drafts.
```

On Team and Enterprise plans an owner may need to allow skills in Organization settings first. To update, remove the old skill and upload the new ZIP.

### Claude on a paid plan: add the plugin

1. Open **Customize > Plugins**, click **Add**, then **Add marketplace**.
2. Choose **Add from a repository** and enter `CosmoBlk/email-marketing-bible`.
3. Add **Email Marketing Bible** from that marketplace. It is saved to your account, so it also works in Cowork, and in Claude Code when you sign in with the same account.

### Claude Code

In Claude Code, run:

```
/plugin marketplace add CosmoBlk/email-marketing-bible
/plugin install email-marketing-bible@email-marketing-bible
```

Use the plugin or a clone into `~/.claude/skills`, not both: the clone also carries the plugin manifest and can load the skill twice.

### Codex, Cursor and other agents

```bash
npx skills add CosmoBlk/email-marketing-bible
```

Or git clone the repo into that agent's skills folder.

### ChatGPT, Gemini or any chat app

Paste this into a new chat:

```
Read https://raw.githubusercontent.com/CosmoBlk/email-marketing-bible/main/SKILL.md
and follow it in this conversation. For detail, read
https://emailmarketingskill.com/llms.txt and the files it lists.
```

The core rules work on their own; the links you pasted let the agent read the reference files when it needs them.

**You can start without connecting anything.** The skill drafts, audits and plans in chat. To build or send inside your email platform, connect it to your agent (MCP, an API or a connector); the skill still holds every send to more than one person until you say "send it".

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

## How it is built

A short core file (`SKILL.md`) holds the rules and the send gates, so they survive a long session. Sixteen files in `references/` hold the depth: thresholds, deliverability, compliance, measurement, flows, copy, design, segmentation, cold email, messaging channels, platforms, benchmarks, playbooks, models, agent operations and sources. The agent reads a reference file only when the task needs it.

**Check any number it gives you.** Every dated fact in `references/` carries a source link, an evidence label (primary, vendor, trade, practitioner) and a Last checked date. Where a figure has no public source, the skill says so instead of inventing one.

**What it fetches.** Everything the skill follows ships in this package; it never tells the agent to pull instructions from another site. It may ask the agent to check a dated fact against its public source before stating it as current, and it reads the guide only when you ask for more depth.

## Why this exists

Agents now build the campaign, segment the audience, draft the copy and stage the send; the marketer directs. That only works if the agent runs on real benchmarks and hard guardrails. This skill is that discipline layer: the patterns that repeat across industries, the mistakes that destroy deliverability, the anti-slop rules for copy and design, and the send-safety gates that keep one prompt from mailing the wrong thing to your whole list.

## The long-form guide

The skill is distilled from the Email Marketing Bible guide at **[emailmarketingskill.com](https://emailmarketingskill.com)**: 19 chapters and 4 appendices, searchable, with a free PDF. The chapters are being rebuilt for v3. Where a chapter and a reference file disagree, the reference file wins, because it carries a Last checked date.

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
| 11 | Industry Playbooks | Tactics for 19 verticals |
| 12 | Choosing Your Platform | Comparison by list size and budget, including which tools an agent can actually drive |
| 13 | Cold Email & B2B Outbound | Infrastructure, writing, follow-up, AI in outbound |
| 14 | WhatsApp Business | The cost model and where it pays off, per-user caps, quality tiers, opt-in and geo-branching, the AI-chatbot rule |
| 15 | SMS & RCS | TCPA, 10DLC and CTIA compliance, quiet hours, a realistic read on RCS, and AI in two-way messaging |
| 16 | AI & Agentic Marketing | Supervised autonomy, agent preflight gates, data governance, non-deterministic optimisation, what the vendors shipped, and field notes from agent-run sending |
| 17 | Company Case Studies | How Casper, Morning Brew, Duolingo, Spotify, and others use email |
| 18 | Expert Directory | The practitioners referenced throughout, who to follow and why |
| 19 | Best Email Designs 2026 | Hand-curated emails with notes on why each works and what to steal |

Plus four appendices: benchmarks by industry, frequency guide, marketing calendar, and methodology.

**Playbooks by vertical:** `Ecommerce DTC` · `SaaS B2B` · `SaaS B2C` · `Newsletter & Creator` · `Agency` · `Nonprofit` · `Healthcare` · `Financial Services` · `Real Estate` · `Travel & Hospitality` · `Education` · `Professional Services` · `Retail` · `Events` · `B2B Manufacturing` · `Restaurant & Food` · `Fitness` · `Media & Publishing` · `Marketplace & Platform`. Five are in depth in the skill; the rest are summarised, with the full playbook in Chapter 11.

**Expert contributors:** the guide draws on practitioners including Chad S. White (Zeta Global), Joanna Wiebe (Copyhackers), Chase Dimond (Structured Agency), Nathan Barry (Kit), Ann Handley (MarketingProfs), Troy Ericson, Tyler Denk (beehiiv) and Ben Settle. Full directory in Chapter 18.

## What's new

v2.8.3 adds the Claude ZIP and plugin install routes above, and makes the skill ask before reading anything from the web when its reference files are missing. Full history, including v2.8's gate-first core and 16 reference files, is in [CHANGELOG.md](CHANGELOG.md).

## Reusing this guide

The skill and the guide are MIT licensed. You can copy, adapt and republish them, including commercially, as long as the copyright notice (`Copyright (c) 2026 George Hartley`) and the [MIT licence text](LICENSE) stay with your copy.

If you publish a copy of the guide on the web, please also link each page to its original on emailmarketingskill.com and mark your copy `noindex` (or point its canonical tag at the original). Those two are requests, not licence conditions. Cite it as: George Hartley, *Email Marketing Bible*, https://emailmarketingskill.com.

## Contributing

Found an error, better data, or a missing tactic? Issues and PRs welcome.

## License

MIT. Copyright (c) 2026 George Hartley.
