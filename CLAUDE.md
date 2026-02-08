# CLAUDE.md — Project Instructions

> Instructions for any Claude Code session working on this project.
> **See also:** `plan.md` (what to do next), `memory.md` (project history & context)

## Quick Start

When starting a new session on this project:
1. Read `plan.md` to see what step is next
2. Read `memory.md` for full context on what's been done
3. Continue from where the plan indicates

The user's standing instruction is: **"Review the plan.md and keep going"**

## Project

The Email Marketing Bible (EMB) v4 by George Hartley. A comprehensive, data-backed email marketing guide (~59K words, 16 chapters + appendices). Built from 908 sources and 4,798 insights.

## Key Files

```
/Users/georgehartley/AI Email/
├── CLAUDE.md          ← You are here. Session instructions.
├── memory.md          ← Project history, progress, decisions.
├── plan.md            ← Roadmap with next steps.
└── emb-research/
    ├── EMB_v4_part1.md  (Intro, Chapters 1–4, ~16K words)
    ├── EMB_v4_part2.md  (Chapters 5–8, ~15K words)
    ├── EMB_v4_part3.md  (Chapters 9–11, ~12K words)
    └── EMB_v4_part4.md  (Chapters 12–16, Appendices A–D, ~16K words)
```

## George's Voice

Direct. Practical. Data-driven. Australian English. Speaks from operator experience (built SmartrMail, 28K customers). No marketing-speak, no hedging, no filler. Every claim backed by data. Use the `george-tone` skill as reference. The intro of Part 1 (lines 1–60) is the gold standard for tone.

## Skills Available

- `george-tone` — Write in George Hartley's voice for long-form content
- `email-marketing-bible` — The EMB knowledge base as a Claude skill (this is what we're building toward)

## Rules

- Always check `plan.md` before starting work to know what step is current
- Update `memory.md` after completing significant work
- Update `plan.md` status markers as steps are completed
- Commit to git after meaningful progress
- When editing EMB content, maintain George's voice throughout
- Quality over word count — cutting content that doesn't earn its place is encouraged
- Australian English spelling (organisation, optimisation, behaviour, etc.)
