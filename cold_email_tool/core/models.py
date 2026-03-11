"""Data models for the cold email personalization pipeline."""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional


class AngleCategory(str, Enum):
    """Which facet of the sender's background to emphasize."""
    AVIATION_ENGINEERING = "aviation_engineering"
    INVESTING_ECON = "investing_economic_development"
    GLOBAL_INFRASTRUCTURE = "global_infrastructure_china"
    AI_TOOLS = "ai_tools_technical_initiative"
    BUILDER_AMBITION = "builder_ambition_intellectual"


@dataclass
class Contact:
    """A person to reach out to."""
    full_name: str
    company: str = ""
    role: str = ""
    website: str = ""
    linkedin: str = ""
    twitter: str = ""
    other_links: list[str] = field(default_factory=list)
    notes: str = ""

    @property
    def search_queries(self) -> list[str]:
        """Generate search queries to research this person."""
        queries = []
        base = self.full_name
        if self.company:
            queries.append(f"{base} {self.company}")
        if self.role:
            queries.append(f"{base} {self.role}")
        queries.append(f"{base} interview OR podcast OR essay OR talk")
        queries.append(f"{base} recent projects OR investments OR research")
        if self.company:
            queries.append(f"{self.company} recent news OR announcements")
        return queries


@dataclass
class ResearchBrief:
    """Structured research output for a single contact."""
    contact: Contact
    specific_facts: list[str] = field(default_factory=list)        # exactly 3
    plausible_reasons: list[str] = field(default_factory=list)     # exactly 2
    recommended_angle: str = ""                                     # 1 sentence
    background_emphasis: AngleCategory = AngleCategory.BUILDER_AMBITION
    raw_research: str = ""                                          # full research notes
    confidence_score: float = 0.0                                   # 0-1, how much we found

    @property
    def is_sufficient(self) -> bool:
        """Whether we have enough verified info to draft a quality email."""
        return (
            len(self.specific_facts) >= 2
            and self.confidence_score >= 0.4
        )


@dataclass
class EmailDraft:
    """A single personalized cold email."""
    recipient: Contact
    research_brief: ResearchBrief
    subject_lines: list[str] = field(default_factory=list)   # up to 3
    body: str = ""
    angle_used: AngleCategory = AngleCategory.BUILDER_AMBITION
    sender_details_used: list[str] = field(default_factory=list)


@dataclass
class PipelineResult:
    """Complete output for one contact."""
    contact: Contact
    research_brief: ResearchBrief
    email_draft: EmailDraft
    flagged_for_review: bool = False
    review_reason: str = ""

    def to_dict(self) -> dict:
        return {
            "contact": asdict(self.contact),
            "research_brief": {
                "specific_facts": self.research_brief.specific_facts,
                "plausible_reasons": self.research_brief.plausible_reasons,
                "recommended_angle": self.research_brief.recommended_angle,
                "background_emphasis": self.research_brief.background_emphasis.value,
                "confidence_score": self.research_brief.confidence_score,
            },
            "email_draft": {
                "subject_lines": self.email_draft.subject_lines,
                "body": self.email_draft.body,
                "angle_used": self.email_draft.angle_used.value,
                "sender_details_used": self.email_draft.sender_details_used,
            },
            "flagged_for_review": self.flagged_for_review,
            "review_reason": self.review_reason,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
