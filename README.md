# Email Marketing Bible

**The AI email automation skill for Claude, ChatGPT, and any agent.** v2.7, 8 September 2026.

Install it and your AI stops guessing about email. It audits your setup, builds flows from a prompt, drafts copy in your voice, directs email design instead of accepting the model's defaults, tells you why you are in spam, and runs your ESP through MCP with a hard rule that nothing blasts without your say-so.

Built from 908 sources, the experience of running [SmartrMail](https://www.smartrmail.com) (~28,000 customers, 6 billion emails, acquired 2022), and three months of running Nitrosend's own sending through agents. 19 chapters, 19 industry playbooks, 47 curated email designs. Free and open source.

## Install

```bash
git clone https://github.com/CosmoBlk/email-marketing-bible.git ~/.claude/skills/email-marketing-bible
```

Works wherever you run skills: Claude Code, Claude Desktop, and any agent that reads the skill format.

## Why this exists

In 2026 the job changed. Agents build the campaign, segment the audience, draft the copy and stage the send; the marketer directs. That only works if the agent runs on real benchmarks and hard guardrails. This skill is that discipline layer: the patterns that repeat across industries, the mistakes that destroy deliverability, the anti-slop rules for copy and design, and the send-safety gates that keep one prompt from mailing the wrong thing to your whole list.

## What the skill does

| Task | What it does |
|------|-------------|
| **Run email automation** | Build welcome, cart, post-purchase and win-back flows from a prompt, then review exits, timing and copy before anything goes live |
| **Audit your setup** | Review flows, segments, deliverability and compliance, and say what is missing |
| **Draft and de-slop copy** | Write with proven frameworks (PAS, AIDA, BAB) and strip the AI tells before send |
| **Direct email design** | Seed strings for divergence, a critic loop that scores screenshots, chained image and video models, delivery by subtraction; output as inbox-safe MJML or React Email |
| **Drive your ESP from AI** | Operate Klaviyo, Resend, beehiiv, Mailchimp, Omnisend or Nitrosend through MCP and connectors, with pre-send gates and field-tested operating rules |
| **Fix deliverability** | Step-by-step triage covering authentication, reputation, content and the AI-mediated inbox |
| **Pull industry benchmarks** | Open, click, conversion and revenue-per-email figures by vertical |
| **Compare platforms** | Honest comparison by list size, budget and whether an agent can drive it |
| **Review compliance** | GDPR, CAN-SPAM, CASL, CCPA and the Australian Spam Act as a gate before any send |
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

The skill has two parts: an operating manual for when the AI is acting (building, sending, diagnosing, designing) and a dense reference (benchmarks, frameworks, playbooks).

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

### 19 industry playbooks

`Ecommerce DTC` · `SaaS B2B` · `SaaS B2C` · `Newsletter & Creator` · `Agency` · `Nonprofit` · `Healthcare` · `Financial Services` · `Real Estate` · `Travel & Hospitality` · `Education` · `Professional Services` · `Retail` · `Events` · `B2B Manufacturing` · `Restaurant & Food` · `Fitness` · `Media & Publishing` · `Marketplace & Platform`

### Expert contributors

Insights from practitioners including Chad S. White (Zeta Global), Joanna Wiebe (Copyhackers), Chase Dimond (Structured Agency), Nathan Barry (Kit), Ann Handley (MarketingProfs), Troy Ericson, Tyler Denk (beehiiv), Ben Settle, and many others. Full directory in Chapter 18.

## What changed in v2.7

- An AI email design method, Discover, Define, Deliver, adapted for email from Anshu Chimala's Lenny's Newsletter piece: seed strings, broad-first direction picking, a screenshot critic loop, chained image and video models, delivery by subtraction.
- Five practitioners on designing with AI added to the expert directory (Anshu Chimala, Karri Saarinen, Ryo Lu, Jenny Wen, Lee Munroe), taking it to 49.
- Field notes from three months of running an ESP through agents, in the skill and in Chapter 16.
- Model references updated to the September 2026 state.
- The skill file cut by a fifth; the send-safety gates are unchanged.

## Read the full guide

The complete Email Marketing Bible is at **[emailmarketingskill.com](https://emailmarketingskill.com)**, searchable and browsable, with all 19 chapters and 4 appendices, plus a free PDF.

## Research

908 sources across industry reports (Litmus, Klaviyo, HubSpot, Salesforce, Validity), practitioner blogs, podcasts and transcripts, platform documentation, and community discussions, refreshed mid-2026 with a focus on AI email automation.

## Contributing

Found an error, better data, or a missing tactic? Issues and PRs welcome.

## License

MIT.

---

*Built by [George Hartley](https://x.com/GTHartley). Follow for updates.*
