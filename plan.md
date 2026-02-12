# Email Marketing Bible — Project Plan

> **See also:** `memory.md` (project history & context), `CLAUDE.md` (instructions for Claude)
> **To continue:** Start a new Claude Code session and say "Review the plan.md and keep going"

---

## Status: Step 6 In Progress — Launch Thu 20 Feb

---

## Step 1: Research & Compile EMB v4 ✅ COMPLETE

- 12 research sprints across all major email marketing topics
- 908 sources crawled, 4,798 insights extracted
- Compiled into EMB v4: 16 chapters + 4 appendices (~59,300 words)
- Split across 4 files in `emb-research/`

---

## Step 2: Expert Edit of EMB v4 ✅ COMPLETE

### The Brief

Do a big, expert, fresh edit of the entire EMB v4 from first principles. This is not a polish pass — it's a structural and editorial overhaul.

### Three Goals

**1. Tighten the writing.**
Every sentence should earn its place. Cut filler, redundancy, and anything that doesn't add value a practitioner can act on. If the document needs to shrink from 59K to 35K words to be better, then it shrinks to 35K. Quality over volume.

**2. Ensure George's voice is consistent throughout.**
The document was compiled across many sessions. George's voice is direct, practical, Australian English, speaks from operator experience (SmartrMail, 28K customers). No marketing-speak. No hedging. No filler phrases. Read the intro (Part 1, first ~60 lines) as the gold standard for tone. Use the `george-tone` skill as reference.

**3. Make every section earn its place.**
- Does this chapter add something no other email marketing guide covers?
- Is there overlap between chapters that should be consolidated?
- Are there sections that read like generic advice rather than hard-won insight?
- Is the chapter ordering optimal for the reader?
- Do the case studies and examples add genuine value or just word count?

### How to Execute

1. Read all 4 parts end-to-end first. Take notes on structural issues before editing.
2. Work through one part at a time, editing in place.
3. Track what was cut/changed/moved in a summary.
4. The document can change structure — chapters can merge, split, or reorder if it serves the reader.
5. Don't preserve word count for its own sake. A 30K-word document that's all signal is better than a 59K-word document with noise.

### Files to Edit
- `emb-research/EMB_v4_part1.md` (~16K words)
- `emb-research/EMB_v4_part2.md` (~15K words)
- `emb-research/EMB_v4_part3.md` (~12K words)
- `emb-research/EMB_v4_part4.md` (~16K words)

### Results

- Reduced from ~59,300 → ~55,000 words (~4,300 words cut)
- Fixed all voice consistency issues (36 "I'd suggest" → 3, removed "Here's the thing", "deep dive" headings, "landscape" in titles)
- Fixed chapter numbering errors in intro
- Consolidated duplicate content (Subscriber LTV, Halo Effect cross-referenced instead of duplicated)
- Major structural cuts to Industry Playbooks (Ch 11): consolidated 8 niche playbooks into 3 grouped sections
- Condensed Expert Directory (Ch 16) from individual bios to compact grouped format
- Trimmed platform write-ups (Ch 12) after comparison table
- Renamed Ch 12 from "The Platform Landscape" to "Choosing Your Platform"

### Reference
- George's tone: Use the `george-tone` skill
- EMB v4 intro (Part 1, lines 1–60) as voice benchmark

---

## Step 3: Create EMB Skill File ✅ COMPLETE

Converted the edited EMB v4 into a Claude Code `SKILL.md` file.

### The Brief

- Contain the full knowledge base in a format optimised for Claude consumption
- Enable Claude to act as an email marketing co-pilot
- Support tasks: analyse setups, identify gaps, draft copy, build automation flows, pull benchmarks
- Be installable via the instructions in the EMB intro
- Live at the existing repo: [github.com/CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible)

### Results

- Complete rewrite from v2 (1,160 lines of unstructured bullet dumps) to v4 (824 lines, structured for retrieval)
- Distilled 55K words of EMB v4 into a dense skill reference covering all 16 chapters + appendices
- 15 structured sections: Fundamentals, List Building, Segmentation & Personalisation, Automation Flows, Copywriting, Design & Technical, Deliverability, Testing & Optimisation, Analytics & Measurement, Compliance, Industry Playbooks (19 industries), Platform Selection, Cold Email, AI & Email, Case Study Patterns
- Key data tables, benchmark numbers, framework summaries, decision trees retained
- Appendix with benchmarks by industry, by email type, ROI by channel, key thresholds, frequency guide
- Expert Directory: 40 practitioners grouped by specialty
- Removed fake API section and generic filler from v2
- File: `~/.claude/skills/email-marketing-bible/SKILL.md`

---

## Step 4: Publish & Distribute ✅ COMPLETE

- ✅ Pushed all EMB v4 content to GitHub
- ✅ Added SKILL.md to repo
- ✅ Created README.md with chapter overview, installation instructions, and two usage modes
- ✅ Added missing repo link to Part 4 closing
- ✅ All 3 commits pushed to `origin/main`
- Repo: [github.com/CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) (now public)

---

## Step 5: Build emailmarketingskill.com ✅ COMPLETE

### Goals

Build a website at emailmarketingskill.com that serves as:
1. **Landing page** — SEO-optimised for "Email Marketing Skill for Claude Code". Dark terminal aesthetic with light docs. Install command, GitHub link, expert social proof, email capture for PDF download.
2. **Searchable wiki** — The full 55K-word EMB hosted as a browsable, searchable reference with sidebar navigation.

### Framework

**Astro Starlight** — splash template for landing page, doc template for wiki, built-in Pagefind search, markdown-native, deploys to Vercel.

### Separate Repo

`CosmoBlk/emailmarketingskill.com`

### Status

- ✅ Site live at emailmarketingskill.com (Vercel)
- ✅ Dark landing page + light GitHub-style docs
- ✅ All 16 chapters + 4 appendices as individual pages with sidebar navigation
- ✅ Pagefind search across all content
- ✅ Resend email capture (landing page + doc page footers)
- ✅ Custom Hero.astro (terminal install, GitHub link, expert grid, chapter list)
- ✅ Custom Footer.astro (author credits, Twitter, GitHub)
- ✅ Platform coverage updated: SmartrMail, Bento, Omnisend added to Ch12
- ✅ AI hype toned down in Ch14 per editorial direction
- ✅ SKILL.md refined (415 lines, URL references to EMB chapters)
- ✅ Miscapitalisation scan: clean throughout

---

## Step 6: Launch — Thu 20 Feb 2026 🔜 IN PROGRESS

### Goals

Compressed 7-day launch plan. Maximum reach through expert network + organic channels. Target audience: AI builders, email marketers, Claude Code users.

### Launch Timeline

**Thu 13 Feb — Expert Outreach (Round 1: Review Request)**
- ⬜ Draft personalised emails to all 40 experts cited in EMB Ch16 (use Expert Reference Map below)
- ⬜ Each email includes: specific chapter + line where they're quoted, link to their section on emailmarketingskill.com
- ⬜ Ask 1: Review the section where you're cited — does this look right?
- ⬜ Ask 2: Try the skill on a real task and share feedback before Thursday launch
- ⬜ Send all outreach emails

**Mon 17 Feb — Directory Listings**
- ⬜ Submit to skills.sh
- ⬜ Submit to agentskills.io
- ⬜ Submit to Awesome Claude Code lists on GitHub
- ⬜ Check for Claude Code community / Anthropic Discord channels

**Tue 18 Feb — Content Prep**
- ⬜ Draft X/Twitter long-form article (George's voice, data-driven, operator angle)
- ⬜ Draft Reddit post for r/ClaudeAI ("I built this, here's what I learned" angle)
- ⬜ Draft Reddit post for r/emailmarketing (practitioner angle)
- ⬜ Draft LinkedIn post (shorter, professional audience)
- ⬜ Prep Product Hunt listing page + maker comment (launch same day or following week)
- ⬜ Draft Hacker News "Show HN" post (open-source + 908-source methodology angle)

**Wed 19 Feb — Expert Outreach (Round 2: Launch Reminder)**
- ⬜ Send follow-up emails to expert list
- ⬜ Include X article link (pre-published or preview)
- ⬜ Ask them to share/comment when it goes live Thursday
- ⬜ Give them a specific share prompt or suggested post

**Thu 20 Feb — LAUNCH DAY**
- ⬜ Publish X article (morning)
- ⬜ Post to Reddit r/ClaudeAI
- ⬜ Post to Reddit r/emailmarketing
- ⬜ Post to LinkedIn
- ⬜ Launch on Product Hunt (if prepped, otherwise following week)
- ⬜ Submit to Hacker News ("Show HN")
- ⬜ Email experts with live links — ask for shares
- ⬜ Monitor and engage with comments/replies all day

### Expert Outreach Email Structure

**Email 1 (Thu 13 Feb — TOMORROW'S TASK):**
- Subject: "You're cited in the Email Marketing Bible — quick review?"
- Body: Personal intro, explain EMB + Claude Code skill, link to their specific section, ask for review + skill feedback
- Include: direct link to emailmarketingskill.com/[chapter], specific quote/line
- Tone: George's voice — direct, respectful, not salesy. Operator-to-operator.

**Email 2 (Wed 19 Feb):**
- Subject: "Launching tomorrow — would love your support"
- Body: Remind them of the skill, link to X article, suggest a share/quote-tweet, thank them for any feedback from email 1

### Expert Reference Map (for Email 1 personalisation)

Each expert below is listed with their chapter citations and the URL slug for their section on emailmarketingskill.com. The email should link to the most substantive mention (not just the Ch16 directory listing).

**Strategy:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Chad S. White | "Head of Research at Oracle... author of Email Marketing Rules" | Ch1 | /01-fundamentals |
| Kath Pay | "founder of Holistic Email Marketing, 26+ years" | Ch1 | /01-fundamentals |
| Jay Schwedelson | "over-contacting is one of the biggest destroyers of email performance" | Ch3 | /03-segmentation-and-personalisation |
| Jeanne Jennings | Systematic testing approach | Ch8 | /08-testing-and-optimisation |
| Dela Quist | Ch16 directory only | Ch16 | /16-expert-directory |
| Ann Handley | "respecting audience data isn't just a legal obligation, it's a competitive advantage" | Ch10 | /10-compliance-and-privacy |
| Ryan Phelan | "focus on incrementality" | Ch9 | /09-analytics-and-measurement |

**Platform Builders:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Nathan Barry | "founder of Kit, formerly ConvertKit" | Ch2 | /02-building-your-list |
| Tyler Denk | "employee number two at Morning Brew" + beehiiv founding story | Ch15 | /15-company-case-studies |
| Jimmy Kim | "recommends running both platforms in parallel for 2-4 weeks during migration" | Ch12 | /12-choosing-your-platform |
| Brennan Dunn | Self-identification technique for welcome emails | Ch4 | /04-the-emails-that-make-money |

**Copywriting:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Joanna Wiebe | "coined the term 'conversion copywriting'" | Ch1 | /01-fundamentals |
| Laura Belgray | "read like a person, not a brand" | Ch5 | /05-copywriting-that-converts |
| Ben Settle | Daily email approach, unconventional subject lines | Ch5 | /05-copywriting-that-converts |
| Chris Orzechowski | "CTA should be the natural conclusion of your email's argument" | Ch5 | /05-copywriting-that-converts |
| Samar Owais | "making the offer feel like a natural next step rather than a hard pivot" | Ch4 | /04-the-emails-that-make-money |
| Tarzan Kay | Ch16 directory only | Ch16 | /16-expert-directory |

**Deliverability:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Matthew Vernhout | "strongest advocates for DMARC adoption" | Ch7 | /07-deliverability |
| Troy Ericson | "'Email Paramedic' approach" | Ch7 | /07-deliverability |
| Lauren Meyer | Ch16 directory only | Ch16 | /16-expert-directory |

**Design and Technical:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Mark Robbins | "pioneered CSS-only techniques for email" | Ch6 | /06-design-and-technical |
| Paul Airy | "leading voice on email accessibility" | Ch6 | /06-design-and-technical |
| Justin Khoo | Ch16 directory only | Ch16 | /16-expert-directory |
| Jason Rodriguez | Progressive enhancement champion | Ch6 | /06-design-and-technical |

**Ecommerce and Retention:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Chase Dimond | "$200M+ in email revenue" + revenue attribution framework | Ch4 | /04-the-emails-that-make-money |
| Val Geisler | "behaviour-based onboarding" distinction | Ch4 | /04-the-emails-that-make-money |
| Reinis Krumins | Engagement-based sending for DTC | Ch11 | /11-industry-playbooks |
| Danavir Sarria | Ch16 directory only | Ch16 | /16-expert-directory |

**Agency:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Scott Cohen | "tracking metrics per client vertical" | Ch11 | /11-industry-playbooks |
| Garin Hobbs | Ch16 directory only | Ch16 | /16-expert-directory |

**Newsletter Growth:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Dan Oshinsky | "first 100 subscribers are the hardest" | Ch11 | /11-industry-playbooks |
| Matt McGarry | "first 100 subscribers are the hardest" | Ch11 | /11-industry-playbooks |
| Liz Wilcox | "community of over 4,000 email marketing enthusiasts" | Ch2 | /02-building-your-list |

**Consultants:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Ian Brodie | "teach, don't pitch" principle | Ch11 | /11-industry-playbooks |
| Jordie van Rijn | "don't just compare features on paper. Get demos." | Ch12 | /12-choosing-your-platform |
| Eman Ismail | Ch16 directory only | Ch16 | /16-expert-directory |
| Andrew Kordek | Ch16 directory only | Ch16 | /16-expert-directory |

**Content Creators:**
| Expert | Best Citation | Chapter | URL |
|--------|--------------|---------|-----|
| Alex Cattoni | Ch16 directory only | Ch16 | /16-expert-directory |
| Noah Kagan | "Law of 100" for list building | Ch2 | /02-building-your-list |
| Gavin Laugenie | Quarterly testing plans tied to business questions | Ch8 | /08-testing-and-optimisation |

**Note:** Experts with "Ch16 directory only" (Dela Quist, Tarzan Kay, Lauren Meyer, Justin Khoo, Danavir Sarria, Garin Hobbs, Eman Ismail, Andrew Kordek, Alex Cattoni) are listed in the Expert Directory but don't have deep chapter citations. The email for these experts should reference their directory listing and their area of expertise, and still ask for review + skill feedback.

### Channels Summary

| Channel | Audience | Angle |
|---------|----------|-------|
| Expert outreach | 40+ email practitioners with audiences | Personal, review-based |
| X/Twitter article | AI builders, vibe coders | Long-form, data-driven |
| r/ClaudeAI | Claude Code users | "I built this" story |
| r/emailmarketing | Email practitioners | Practitioner value |
| LinkedIn | Professional marketers | Shorter, professional |
| Product Hunt | Tech/product community | Product launch |
| Hacker News | Developers, open-source | Show HN, methodology |
| skills.sh / agentskills.io | Skill directory users | Listing |
| Anthropic Discord/community | Claude ecosystem | Direct target |

---

## Notes

- The project path is `/Users/georgehartley/AI Email/`
- The website repo is `/Users/georgehartley/emailmarketingskill.com/`
- All EMB source content is in `emb-research/` subdirectory
- Chapter markdown files for the website are in `/Users/georgehartley/emailmarketingskill.com/src/content/docs/`
- Expert directory: `/Users/georgehartley/emailmarketingskill.com/src/content/docs/16-expert-directory.md`
- The base URL for all chapter links is `https://emailmarketingskill.com/`
