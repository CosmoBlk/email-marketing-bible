"""Output formatters — render pipeline results as Markdown or JSON."""

from __future__ import annotations

import json
from pathlib import Path

from .models import PipelineResult


def format_result_markdown(result: PipelineResult) -> str:
    """Format a single pipeline result as readable Markdown."""
    c = result.contact
    b = result.research_brief
    e = result.email_draft

    lines = []
    lines.append(f"## {c.full_name}")
    if c.company or c.role:
        lines.append(f"**{c.role}** at **{c.company}**" if c.role and c.company else f"**{c.company or c.role}**")
    lines.append("")

    if result.flagged_for_review:
        lines.append(f"> **Review flag:** {result.review_reason}")
        lines.append("")

    # Research brief
    lines.append("### A. Research Summary")
    for i, fact in enumerate(b.specific_facts, 1):
        lines.append(f"{i}. {fact}")
    lines.append("")

    lines.append("**Plausible reasons for outreach:**")
    for reason in b.plausible_reasons:
        lines.append(f"- {reason}")
    lines.append("")

    lines.append(f"**Confidence:** {b.confidence_score:.0%}")
    lines.append("")

    # Angle
    lines.append("### B. Best Angle")
    lines.append(f"- **Angle:** {b.recommended_angle}")
    lines.append(f"- **Emphasis:** {b.background_emphasis.value.replace('_', ' ').title()}")
    lines.append("")

    # Email
    lines.append("### C. Email Draft")
    lines.append("")
    lines.append(e.body)
    lines.append("")

    # Subject lines
    if e.subject_lines:
        lines.append("### D. Subject Line Ideas")
        for i, subj in enumerate(e.subject_lines, 1):
            lines.append(f"{i}. {subj}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def format_batch_markdown(results: list[PipelineResult]) -> str:
    """Format all results as a single Markdown document."""
    header = "# Cold Email Drafts\n\n"
    summary = f"**{len(results)} recipients** processed.\n"
    flagged = sum(1 for r in results if r.flagged_for_review)
    if flagged:
        summary += f"**{flagged}** flagged for manual review.\n"
    summary += "\n---\n\n"

    body = "".join(format_result_markdown(r) for r in results)
    return header + summary + body


def format_batch_json(results: list[PipelineResult]) -> str:
    """Format all results as a JSON array."""
    return json.dumps([r.to_dict() for r in results], indent=2)


def save_results(
    results: list[PipelineResult],
    output_dir: str | Path,
    fmt: str = "both",
) -> list[Path]:
    """Save results to files. Returns list of created file paths."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    created = []

    if fmt in ("markdown", "both"):
        md_path = output_dir / "email_drafts.md"
        md_path.write_text(format_batch_markdown(results), encoding="utf-8")
        created.append(md_path)

    if fmt in ("json", "both"):
        json_path = output_dir / "email_drafts.json"
        json_path.write_text(format_batch_json(results), encoding="utf-8")
        created.append(json_path)

    return created
