"""CLI interface for the cold email personalization tool."""

from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path

from .core.config import PipelineConfig, DEFAULT_SENDER
from .core.pipeline import ColdEmailPipeline
from .core.formatter import save_results, format_batch_markdown


def main():
    parser = argparse.ArgumentParser(
        prog="cold-email",
        description="Cold Email Personalization Tool — research, personalize, and draft high-signal outreach.",
    )
    parser.add_argument(
        "contacts",
        help="Path to contacts file (.csv or .json)",
    )
    parser.add_argument(
        "-o", "--output",
        default="./output",
        help="Output directory (default: ./output)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "markdown", "both"],
        default="both",
        help="Output format (default: both)",
    )
    parser.add_argument(
        "--model",
        default="claude-sonnet-4-20250514",
        help="Claude model to use (default: claude-sonnet-4-20250514)",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="Anthropic API key (default: ANTHROPIC_API_KEY env var)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("Error: Anthropic API key required. Set ANTHROPIC_API_KEY or use --api-key.", file=sys.stderr)
        sys.exit(1)

    config = PipelineConfig(
        anthropic_api_key=api_key,
        model=args.model,
        output_format=args.format,
    )

    pipeline = ColdEmailPipeline(config=config, sender=DEFAULT_SENDER)
    results = pipeline.run_from_file(args.contacts)

    # Print to stdout
    print(format_batch_markdown(results))

    # Save to files
    created = save_results(results, args.output, fmt=args.format)
    for p in created:
        print(f"Saved: {p}", file=sys.stderr)

    # Summary
    flagged = sum(1 for r in results if r.flagged_for_review)
    print(f"\nDone. {len(results)} emails drafted, {flagged} flagged for review.", file=sys.stderr)


if __name__ == "__main__":
    main()
