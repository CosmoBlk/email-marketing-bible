# Email Marketing Bible — Project Memory

> This file tracks project progress, decisions, and context so any new Claude Code session can pick up where the last one left off.
> **Start any new session with:** "Review the plan.md and keep going"
> **See also:** `plan.md` (next steps & roadmap), `CLAUDE.md` (project instructions for Claude)

---

## Project Overview

**What:** The Email Marketing Bible (EMB) v4 — a comprehensive, data-backed email marketing guide by George Hartley.

**Who:** George Hartley, founder of SmartrMail (email marketing SaaS, 28,000 customers).

**Goal:** Create the definitive email marketing reference, available as:
1. A standalone guide (read by chapter)
2. A Claude Code skill file (AI co-pilot for email strategy)

**Repo:** [github.com/CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible)

---

## Current State (as of 9 Feb 2026)

### EMB v4 Document — EDITED ✅

Expert edit complete. All 16 chapters + 4 appendices across 4 files:

| File | Chapters | Words | Status |
|------|----------|-------|--------|
| `emb-research/EMB_v4_part1.md` | Intro, Ch 1–4 | ~15,500 | Edited |
| `emb-research/EMB_v4_part2.md` | Ch 5–8 | ~15,100 | Edited |
| `emb-research/EMB_v4_part3.md` | Ch 9–11 | ~9,300 | Edited |
| `emb-research/EMB_v4_part4.md` | Ch 12–16, Appendices A–D, Closing | ~15,000 | Edited |
| **Total** | | **~55,000 words** | |

### Chapter Structure

1. The Fundamentals
2. Building Your List
3. Segmentation and Personalisation
4. The Emails That Make Money
5. Copywriting That Converts
6. Design and Technical
7. Deliverability
8. Testing and Optimisation
9. Analytics and Measurement
10. Compliance and Privacy
11. Industry Playbooks
12. Choosing Your Platform
13. Cold Email and B2B Outbound
14. AI and the Future of Email
15. Company Case Studies
16. Expert Directory
- Appendix A: Benchmarks by Industry
- Appendix B: Email Frequency Guide
- Appendix C: Email Marketing Calendar
- Appendix D: Methodology and Sources

### What's New in v4 (vs v3)
- Cold email chapter (Ch 13)
- Spam traps section (Ch 2)
- AI and email chapter (Ch 14)
- Company case studies throughout (Ch 15)
- Sending identity guide (domain separation, auth stack)
- Engagement-based sending framework
- Tags vs segments vs lists section
- RFM implementation guide

---

## Research Completed

All research phases are **complete**. 908 sources crawled, 4,798 insights extracted.

Research topics covered:
- ✅ Reddit/Shopify/X common questions
- ✅ Cold email best practices and B2B outbound
- ✅ Honey traps, spam traps, old subscriber dangers
- ✅ Sending identity best practices (from address, subdomains, transactional vs marketing)
- ✅ Deep YouTube/podcast research for operator insights
- ✅ Email marketing forums, blogs, X threads
- ✅ Advanced deliverability, authentication, infrastructure
- ✅ Email copywriting deep dive — frameworks, examples, psychology
- ✅ AI + email future, MCP integrations, Bento deep dive
- ✅ Specific company case studies and flow breakdowns
- ✅ Email design tools, workflows, resources for 2026
- ✅ Advanced segmentation, RFM, predictive analytics

---

## What's Been Done

1. **Research phase** — Completed across 12 research sprints covering all major email marketing topics
2. **EMB v4 compilation** — All research synthesised into 16 chapters + appendices (~59K words)
3. **4-part file split** — Document split for manageability (Part 1: Intro+Ch1-4, Part 2: Ch5-8, Part 3: Ch9-11, Part 4: Ch12-16+Appendices)
4. **Expert edit** — Full structural and editorial pass across all 4 parts. ~59K → ~55K words. Key changes:
   - Voice consistency: removed 33 of 36 "I'd suggest" instances (replaced with direct imperatives), fixed "Here's the thing", removed "deep dive" from headings, renamed "The Platform Landscape" → "Choosing Your Platform"
   - Fixed chapter numbering errors in intro
   - Consolidated duplicate content: Subscriber LTV (was in Ch3 and Ch9, now cross-referenced), Halo Effect (was in Ch1 and Ch9, now cross-referenced)
   - Major structural cuts to Industry Playbooks (Ch 11): consolidated Healthcare, Financial Services, Real Estate, Education, Professional Services, B2B Manufacturing, Restaurant/Food, Fitness into 3 grouped sections
   - Condensed Expert Directory (Ch 16) from ~2K words of individual bios to ~500 words grouped by specialty
   - Trimmed platform write-ups (Ch 12) after comparison table
   - General tightening throughout: cut filler, redundancy, repetitive closings

---

## What's Next

See `plan.md` for the detailed roadmap. Summary:

1. ~~**EMB v4 Expert Edit**~~ ✅ Complete
2. **🔜 EMB Skill File** — Convert the edited EMB v4 into a Claude Code SKILL.md file that can be installed and used as an AI email marketing co-pilot.
3. **Publish & Distribute** — Push to GitHub, update README.

---

## Key Decisions & Context

- **George's voice:** Direct, practical, data-driven. Australian English. No fluff. Speaks from experience (SmartrMail, 28K customers). See the george-tone skill for reference.
- **Document philosophy:** Every claim backed by data. Every recommendation tested by practitioners. Specific things you can implement this week.
- **40 experts referenced** throughout — full directory in Chapter 16.
- **Open source:** Research crawler at [github.com/CosmoBlk/emb-research](https://github.com/CosmoBlk/emb-research)
- **Target format:** Both standalone reading AND Claude Code skill consumption.
- **Edit reduced word count** — 59K → 55K. Cuts focused on duplicates, niche industry playbooks, verbose platform write-ups, and expert directory bios. The core instructional content is preserved.

---

## File Map

```
/Users/georgehartley/AI Email/
├── memory.md          ← You are here. Project history & context.
├── plan.md            ← Roadmap & next steps.
├── CLAUDE.md          ← Instructions for Claude Code sessions.
└── emb-research/
    ├── EMB_v4_part1.md  (Intro, Ch 1–4)
    ├── EMB_v4_part2.md  (Ch 5–8)
    ├── EMB_v4_part3.md  (Ch 9–11)
    └── EMB_v4_part4.md  (Ch 12–16, Appendices)
```
