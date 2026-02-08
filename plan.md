# Email Marketing Bible — Project Plan

> **See also:** `memory.md` (project history & context), `CLAUDE.md` (instructions for Claude)
> **To continue:** Start a new Claude Code session and say "Review the plan.md and keep going"

---

## Status: Step 1 Complete → Step 2 Next

---

## Step 1: Research & Compile EMB v4 ✅ COMPLETE

- 12 research sprints across all major email marketing topics
- 908 sources crawled, 4,798 insights extracted
- Compiled into EMB v4: 16 chapters + 4 appendices (~59,300 words)
- Split across 4 files in `emb-research/`

---

## Step 2: Expert Edit of EMB v4 🔜 NEXT

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

### Reference
- George's tone: Use the `george-tone` skill
- EMB v4 intro (Part 1, lines 1–60) as voice benchmark

---

## Step 3: Create EMB Skill File

After the edit is complete, convert the final EMB v4 into a Claude Code `SKILL.md` file.

The skill file should:
- Contain the full knowledge base in a format optimised for Claude consumption
- Enable Claude to act as an email marketing co-pilot
- Support tasks: analyse setups, identify gaps, draft copy, build automation flows, pull benchmarks
- Be installable via the instructions in the EMB intro
- Live at the existing repo: [github.com/CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible)

### Reference
- Current skill description from system prompt: "Comprehensive email marketing knowledge base compiled from research across 4798 insights and 908 sources. Covers strategy, segmentation, automation, deliverability, benchmarks, and segment-specific playbooks."

---

## Step 4: Publish & Distribute

- Push final EMB v4 document to GitHub
- Push skill file to GitHub
- Update README with installation instructions
- Update any references in the EMB itself (links, version notes)

---

## Notes

- The project path is `/Users/georgehartley/AI Email/`
- All EMB content is in `emb-research/` subdirectory
- The transcript from the original build session is at: `/Users/georgehartley/.claude/projects/-Users-georgehartley-AI-Email-/92a9017e-c5ec-40d7-94cb-d5635441a5af.jsonl`
