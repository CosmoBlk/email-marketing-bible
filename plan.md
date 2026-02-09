# Email Marketing Bible — Project Plan

> **See also:** `memory.md` (project history & context), `CLAUDE.md` (instructions for Claude)
> **To continue:** Start a new Claude Code session and say "Review the plan.md and keep going"

---

## Status: Step 5 In Progress

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

## Step 5: Build emailmarketingskill.com 🔜 IN PROGRESS

### Goals

Build a website at emailmarketingskill.com that serves as:
1. **Landing page** — SEO-optimised for "Email Marketing Skill for Claude Code". Dark terminal aesthetic (modeled on marketing-skills.com). Install command, GitHub link, expert social proof, email capture for PDF download.
2. **Searchable wiki** — The full 55K-word EMB hosted as a browsable, searchable reference with sidebar navigation.

### Framework

**Astro Starlight** — splash template for landing page, doc template for wiki, built-in Pagefind search, markdown-native, deploys to Vercel.

### Key Features

- Terminal install command with copy button
- GitHub repo link (now public)
- Twitter link to @GTHartley
- Email capture via Resend → sends PDF download link, subscribers get EMB update notifications
- All 19 industry playbooks highlighted
- 8 featured experts with specialty + company
- Full chapter navigation with search
- Dark-mode-only, monospace/terminal aesthetic

### Separate Repo

New repo: `CosmoBlk/emailmarketingskill.com`

### Status

- ✅ GitHub repo made public
- ✅ Plan written (see `~/.claude/plans/purring-imagining-swan.md`)
- 🔜 Landing page design (Google AI Studio prompt)
- ⬜ Scaffold Astro Starlight project
- ⬜ Split EMB content into chapter files
- ⬜ Build landing page components
- ⬜ Build Resend email capture
- ⬜ Deploy to Vercel

---

## Notes

- The project path is `/Users/georgehartley/AI Email/`
- All EMB content is in `emb-research/` subdirectory
- The transcript from the original build session is at: `/Users/georgehartley/.claude/projects/-Users-georgehartley-AI-Email-/92a9017e-c5ec-40d7-94cb-d5635441a5af.jsonl`
