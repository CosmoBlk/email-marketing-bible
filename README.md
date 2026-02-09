# The Email Marketing Bible

*By George Hartley | v4 | February 2026*

A comprehensive, data-backed email marketing guide. 55,000 words across 16 chapters and 4 appendices. Built from 908 sources and 4,798 insights.

I built SmartrMail (email marketing SaaS, 28,000 customers) and spent years watching what actually works across thousands of brands. This guide distils that into something you can act on. Every claim backed by data, every recommendation tested by practitioners.

## What's in it

| Chapter | Topic |
|---------|-------|
| 1 | The Fundamentals |
| 2 | Building Your List |
| 3 | Segmentation and Personalisation |
| 4 | The Emails That Make Money (Automation Flows) |
| 5 | Copywriting That Converts |
| 6 | Design and Technical |
| 7 | Deliverability |
| 8 | Testing and Optimisation |
| 9 | Analytics and Measurement |
| 10 | Compliance and Privacy |
| 11 | Industry Playbooks (19 verticals) |
| 12 | Choosing Your Platform |
| 13 | Cold Email and B2B Outbound |
| 14 | AI and the Future of Email |
| 15 | Company Case Studies |
| 16 | Expert Directory (40 practitioners) |

Plus appendices covering benchmarks by industry, email frequency guidelines, a marketing calendar, and methodology.

## Two ways to use it

### 1. Read it

The guide lives in `emb-research/` split across four files:

```
emb-research/
├── EMB_v4_part1.md   (Intro, Chapters 1–4)
├── EMB_v4_part2.md   (Chapters 5–8)
├── EMB_v4_part3.md   (Chapters 9–11)
└── EMB_v4_part4.md   (Chapters 12–16, Appendices)
```

Each chapter stands alone. If you're fixing deliverability, go to Chapter 7. If you're building your first welcome series, go to Chapter 4. The industry playbooks in Chapter 11 have segment-specific tactics whether you're running a DTC brand, a SaaS company, a newsletter, or a nonprofit.

### 2. Install it as a Claude Code skill

The `SKILL.md` file turns Claude into an email marketing co-pilot. It can analyse your current setup, identify gaps, draft copy, build automation flows, and pull benchmarks for your industry.

**Install:**

```bash
git clone https://github.com/CosmoBlk/email-marketing-bible.git
cp -r email-marketing-bible ~/.claude/skills/email-marketing-bible
```

Once installed, Claude can reference the full knowledge base when helping you with email strategy, copywriting, deliverability troubleshooting, or flow design.

**What the skill enables:**

- Analyse your email setup and identify gaps
- Draft email copy in proven frameworks (PAS, AIDA, Before-After-Bridge)
- Build automation flows (welcome, abandoned cart, post-purchase, win-back)
- Pull benchmarks for your industry
- Troubleshoot deliverability issues
- Advise on platform selection
- Review compliance (GDPR, CAN-SPAM, CASL)

## What's new in v4

- **Cold email chapter** — Cold outreach and email marketing are different disciplines with different infrastructure, legal requirements, and strategies. Chapter 13 covers cold email properly.
- **AI and email chapter** — Where AI genuinely helps and where it falls short.
- **Company case studies** — Ten companies that turned email into a competitive advantage, with real numbers.
- **Spam traps section** — Pristine traps, recycled traps, typo traps, role-based traps.
- **Sending identity guide** — Subdomains, domain separation, dedicated vs shared IPs, authentication stack.
- **Engagement-based sending** — Tiered sending based on subscriber engagement.
- **RFM implementation guide** — Practical Recency, Frequency, Monetary scoring you can implement this week.

## Research

The research behind this guide comes from 908 sources across industry reports (Litmus, Klaviyo, Campaign Monitor, HubSpot, Salesforce), practitioner blogs, academic research, platform documentation, and community discussions. 40 expert practitioners are referenced throughout.

The research crawler is open source at [github.com/CosmoBlk/emb-research](https://github.com/CosmoBlk/emb-research).

## License

Copyright 2026 George Hartley. All rights reserved.
