# Cold Email Personalization Tool — Architecture

## Overview

A modular Python pipeline that researches recipients, builds structured briefs,
and generates personalized cold emails. Designed for quality over volume.

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
│  Input       │────▶│  Researcher  │────▶│  Email Generator │────▶│  Formatter   │
│  (CSV/JSON)  │     │  (Search +   │     │  (Personalized   │     │  (MD/JSON)   │
│              │     │   Synthesis) │     │   Draft)         │     │              │
└─────────────┘     └──────────────┘     └─────────────────┘     └──────────────┘
                           │                      │
                     Claude API              Claude API
                     (research brief)        (email draft)
```

## System Components

### 1. Input Layer (`core/pipeline.py`)

**Accepted formats:**
- CSV with columns: `full_name, company, role, website, linkedin, twitter, other_links, notes`
- JSON array of contact objects with the same fields

**Design choice:** Both formats use the same `Contact` dataclass internally.
The `other_links` field in CSV is semicolon-separated; in JSON it's a list.

### 2. Research Pipeline (`core/researcher.py`)

**Two-stage process:**

**Stage A — Search.** For each contact, generate 3–5 targeted search queries:
- `"{name} {company}"` — role context
- `"{name} {role}"` — professional identity
- `"{name} interview OR podcast OR essay OR talk"` — recent public appearances
- `"{name} recent projects OR investments OR research"` — current work
- `"{company} recent news OR announcements"` — organizational context

The `search_fn` is a pluggable callable. By default it's a stub (for offline use).
In production, wire it to a web search API (Tavily, SerpAPI, Brave Search, etc.).

**Stage B — Synthesis.** Feed aggregated search results to Claude with a structured
prompt that produces:
- 3 specific, verified facts
- 2 plausible reasons for outreach
- 1 recommended angle
- 1 background emphasis category
- Confidence score (0–1)

**Hallucination safeguards:**
- The prompt explicitly instructs: "Based ONLY on the search results above"
- Facts must be "something concrete they built, wrote, invested in, or achieved"
- Insufficient data entries are labeled `INSUFFICIENT DATA`
- Low-confidence briefs are flagged for human review

### 3. Personalization Engine (`core/email_generator.py`)

**Angle selection:** The research brief determines which of 5 sender facets to emphasize:

| Angle | When to use |
|-------|-------------|
| `aviation_engineering` | Recipient is in aerospace, defense, safety, or regulatory tech |
| `investing_economic_development` | Recipient works in investing, policy, macro, or progress studies |
| `global_infrastructure_china` | Recipient focuses on infrastructure, geopolitics, or emerging markets |
| `ai_tools_technical_initiative` | Recipient is in AI/ML, developer tools, or applied technology |
| `builder_ambition_intellectual` | General ambitious builder — default fallback |

**Variation enforcement:** The generator tracks previous angles used and passes them
to each subsequent prompt with the instruction "do NOT repeat these framings."
This prevents the system from converging on a single template.

**Prompt structure:**
1. System prompt: strict rules (3–5 sentences, no vague praise, no invented facts, etc.)
2. User prompt: recipient data + research brief + sender profile + emphasis details +
   previous angles + tone guidelines + anti-patterns

### 4. Quality Control

**Automatic flagging triggers:**
- Confidence score < 0.6 → flagged for review
- Fewer than 2 verified facts → flagged with "insufficient research data"
- Pipeline errors → flagged with error message, never silently dropped

**Manual review workflow:** All flagged results include a `review_reason` field.
The Markdown output renders these as blockquotes for easy scanning.

### 5. Output Layer (`core/formatter.py`)

**Formats:**
- **Markdown:** Human-readable document with sections A–D per recipient
- **JSON:** Machine-readable for downstream integrations (UI, Gmail API, CRM)

**Per-recipient output schema:**
```json
{
  "contact": { "full_name": "", "company": "", "role": "", ... },
  "research_brief": {
    "specific_facts": ["...", "...", "..."],
    "plausible_reasons": ["...", "..."],
    "recommended_angle": "...",
    "background_emphasis": "aviation_engineering",
    "confidence_score": 0.92
  },
  "email_draft": {
    "subject_lines": ["...", "...", "..."],
    "body": "...",
    "angle_used": "aviation_engineering",
    "sender_details_used": ["..."]
  },
  "flagged_for_review": false,
  "review_reason": ""
}
```

## Data Flow

```
1. Load contacts from CSV/JSON
2. For each contact:
   a. Generate search queries from name + company + role
   b. Execute searches via pluggable search_fn
   c. Feed results to Claude → structured ResearchBrief
   d. Check confidence threshold → flag if low
   e. Select angle based on brief's background_emphasis
   f. Feed brief + sender profile + previous angles to Claude → EmailDraft
   g. Package as PipelineResult
3. Format all results as Markdown + JSON
4. Save to output directory
```

## Prompt Stack

| Stage | System Prompt | User Prompt | Output |
|-------|---------------|-------------|--------|
| Research | "You are a research assistant..." (fact-only, no invention) | Contact details + raw search results + sender context | JSON: facts, reasons, angle, confidence |
| Email | "You are a cold email ghostwriter..." (10 strict rules) | Recipient + brief + sender emphasis + previous angles + tone + anti-patterns | JSON: subject lines, body, details used |

## Extension Points

### Web Search Integration
Replace the default stub `search_fn` with any search API:

```python
import requests

def tavily_search(query: str) -> str:
    resp = requests.post("https://api.tavily.com/search", json={
        "api_key": TAVILY_KEY,
        "query": query,
        "max_results": 5,
    })
    results = resp.json().get("results", [])
    return "\n".join(f"- {r['title']}: {r['content']}" for r in results)

pipeline = ColdEmailPipeline(config, search_fn=tavily_search)
```

### Gmail Integration (Future)
The JSON output maps cleanly to the Gmail API:
- `email_draft.body` → message body
- `email_draft.subject_lines[0]` → subject
- `contact.full_name` → To header (once email address is added to contact)

### UI Integration (Future)
The JSON schema is designed for frontend consumption:
- Render each `PipelineResult` as a card
- Show research brief as expandable section
- Highlight flagged results
- Allow inline editing of drafts before sending

### Spreadsheet Integration
Already supported — the CSV loader accepts any standard spreadsheet export.

## File Structure

```
cold_email_tool/
├── __init__.py
├── cli.py                    # CLI entry point
├── core/
│   ├── __init__.py
│   ├── models.py             # Contact, ResearchBrief, EmailDraft, PipelineResult
│   ├── config.py             # SenderProfile, PipelineConfig, DEFAULT_SENDER
│   ├── researcher.py         # Search + synthesis pipeline
│   ├── email_generator.py    # Personalized email drafting
│   ├── pipeline.py           # Orchestrator + CSV/JSON loaders
│   └── formatter.py          # Markdown + JSON output formatters
├── prompts/
│   ├── __init__.py
│   └── templates.py          # All prompt templates (centralized)
└── examples/
    ├── sample_contacts.csv
    ├── sample_contacts.json
    └── sample_output.md
```

## Usage

```bash
# Basic usage
python -m cold_email_tool.cli contacts.csv -o ./output

# With options
python -m cold_email_tool.cli contacts.json \
  --model claude-sonnet-4-20250514 \
  --format both \
  --output ./drafts \
  --verbose
```

## Design Principles

1. **Quality over volume.** Every safeguard is designed to catch bad emails before they're sent.
2. **No hallucination.** Two-layer defense: prompt instructions + confidence scoring + human review flags.
3. **No repetition.** Angle tracking + explicit "don't repeat" instructions prevent template convergence.
4. **Modular.** Each stage (search, research, generation, formatting) can be swapped independently.
5. **Human in the loop.** The tool drafts; you review and send. Manual review is a feature, not a bug.
