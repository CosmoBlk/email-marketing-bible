"""Main pipeline — orchestrates research and email generation for a batch of contacts."""

from __future__ import annotations

import csv
import json
import logging
from pathlib import Path
from typing import Optional

from .models import Contact, PipelineResult
from .config import SenderProfile, PipelineConfig, DEFAULT_SENDER
from .researcher import Researcher
from .email_generator import EmailGenerator

logger = logging.getLogger(__name__)


def load_contacts_csv(path: str | Path) -> list[Contact]:
    """Load contacts from a CSV file.

    Expected columns (all optional except full_name):
        full_name, company, role, website, linkedin, twitter, other_links, notes
    """
    contacts = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            other = row.get("other_links", "")
            other_list = [l.strip() for l in other.split(";") if l.strip()] if other else []
            contacts.append(
                Contact(
                    full_name=row.get("full_name", "").strip(),
                    company=row.get("company", "").strip(),
                    role=row.get("role", "").strip(),
                    website=row.get("website", "").strip(),
                    linkedin=row.get("linkedin", "").strip(),
                    twitter=row.get("twitter", "").strip(),
                    other_links=other_list,
                    notes=row.get("notes", "").strip(),
                )
            )
    return [c for c in contacts if c.full_name]


def load_contacts_json(path: str | Path) -> list[Contact]:
    """Load contacts from a JSON file (list of objects)."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    contacts = []
    for item in data:
        other = item.get("other_links", [])
        if isinstance(other, str):
            other = [l.strip() for l in other.split(";") if l.strip()]
        contacts.append(
            Contact(
                full_name=item.get("full_name", "").strip(),
                company=item.get("company", "").strip(),
                role=item.get("role", "").strip(),
                website=item.get("website", "").strip(),
                linkedin=item.get("linkedin", "").strip(),
                twitter=item.get("twitter", "").strip(),
                other_links=other,
                notes=item.get("notes", "").strip(),
            )
        )
    return [c for c in contacts if c.full_name]


class ColdEmailPipeline:
    """End-to-end pipeline: contacts in, personalized emails out."""

    def __init__(
        self,
        config: PipelineConfig,
        sender: Optional[SenderProfile] = None,
        search_fn=None,
    ):
        self.config = config
        self.sender = sender or DEFAULT_SENDER
        self.researcher = Researcher(config, self.sender, search_fn=search_fn)
        self.generator = EmailGenerator(config, self.sender)

    def process_contact(self, contact: Contact) -> PipelineResult:
        """Run the full pipeline for a single contact."""
        # Step 1: Research
        brief = self.researcher.research_contact(contact)

        # Step 2: Check confidence
        flagged = False
        review_reason = ""
        if brief.confidence_score < self.config.low_confidence_threshold:
            flagged = True
            review_reason = (
                f"Low research confidence ({brief.confidence_score:.2f}). "
                "Verify facts before sending."
            )

        if not brief.is_sufficient:
            flagged = True
            review_reason = (
                "Insufficient research data. Manual research recommended "
                "before sending this email."
            )

        # Step 3: Generate email
        draft = self.generator.generate(brief)

        return PipelineResult(
            contact=contact,
            research_brief=brief,
            email_draft=draft,
            flagged_for_review=flagged,
            review_reason=review_reason,
        )

    def process_batch(self, contacts: list[Contact]) -> list[PipelineResult]:
        """Process a list of contacts sequentially."""
        results = []
        for i, contact in enumerate(contacts, 1):
            logger.info("Processing %d/%d: %s", i, len(contacts), contact.full_name)
            try:
                result = self.process_contact(contact)
                results.append(result)
            except Exception as e:
                logger.error("Failed to process %s: %s", contact.full_name, e)
                # Create a flagged result so we don't silently drop anyone
                from .models import ResearchBrief, EmailDraft
                results.append(
                    PipelineResult(
                        contact=contact,
                        research_brief=ResearchBrief(contact=contact),
                        email_draft=EmailDraft(
                            recipient=contact,
                            research_brief=ResearchBrief(contact=contact),
                            body="[PIPELINE ERROR — manual draft required]",
                        ),
                        flagged_for_review=True,
                        review_reason=f"Pipeline error: {e}",
                    )
                )
        return results

    def run_from_file(self, path: str | Path) -> list[PipelineResult]:
        """Load contacts from CSV or JSON and process them all."""
        path = Path(path)
        if path.suffix == ".csv":
            contacts = load_contacts_csv(path)
        elif path.suffix == ".json":
            contacts = load_contacts_json(path)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}. Use .csv or .json")

        logger.info("Loaded %d contacts from %s", len(contacts), path)
        return self.process_batch(contacts)
