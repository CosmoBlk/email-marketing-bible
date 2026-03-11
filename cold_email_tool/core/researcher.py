"""Research pipeline — gathers public information about each contact."""

from __future__ import annotations

import json
import logging
from typing import Optional

from .models import Contact, ResearchBrief, AngleCategory
from .config import SenderProfile, PipelineConfig

logger = logging.getLogger(__name__)

RESEARCH_SYSTEM_PROMPT = """\
You are a research assistant. Your job is to analyze raw web search results about \
a person and produce a structured research brief.

RULES:
- Only include facts that are clearly supported by the search results provided.
- If a fact is ambiguous or uncertain, omit it entirely.
- Never invent, hallucinate, or speculate about the person.
- Be specific: names of companies, projects, publications, investment rounds, etc.
- Focus on what makes this person distinctive and interesting.
"""

RESEARCH_USER_TEMPLATE = """\
I need a research brief on the following person:

Name: {name}
Company: {company}
Role: {role}
Website: {website}
LinkedIn: {linkedin}
Twitter/X: {twitter}
Additional links: {other_links}
Notes: {notes}

Here are the raw search results I gathered:

<search_results>
{search_results}
</search_results>

Based ONLY on the search results above, produce a research brief in the following \
JSON format. Do not invent any information. If you cannot find enough, say so.

{{
  "specific_facts": [
    "Fact 1 — something concrete they built, wrote, invested in, or achieved",
    "Fact 2 — another specific, verifiable fact",
    "Fact 3 — a third specific fact (or 'INSUFFICIENT DATA' if not enough info)"
  ],
  "plausible_reasons": [
    "Reason 1 — why the sender (described below) is a plausible person to reach out",
    "Reason 2 — a second reason"
  ],
  "recommended_angle": "One sentence describing the best angle for outreach",
  "background_emphasis": "One of: aviation_engineering | investing_economic_development | global_infrastructure_china | ai_tools_technical_initiative | builder_ambition_intellectual",
  "confidence_score": 0.0 to 1.0,
  "key_themes": ["theme1", "theme2"]
}}

About the sender (for context on plausible reasons):
- Name: {sender_name}
- Role: {sender_role} at {sender_company}
- Education: {sender_education}
- Background facets: {sender_facets}

Choose the background_emphasis that best aligns with this recipient's world. \
The confidence_score should reflect how much verifiable information you found \
(1.0 = rich, detailed info; 0.0 = almost nothing found).
"""


class Researcher:
    """Runs web searches and builds research briefs for contacts."""

    def __init__(
        self,
        config: PipelineConfig,
        sender: SenderProfile,
        search_fn=None,
    ):
        self.config = config
        self.sender = sender
        self.client = None
        if config.anthropic_api_key:
            from anthropic import Anthropic
            self.client = Anthropic(api_key=config.anthropic_api_key)
        # search_fn: async callable(query: str) -> str  (raw results text)
        # If None, we use a stub that returns empty results (for offline/testing)
        self._search_fn = search_fn or self._default_search

    @staticmethod
    def _default_search(query: str) -> str:
        """Stub search — returns empty results. Replace with real search integration."""
        return f"[No search results available for: {query}]"

    def search_contact(self, contact: Contact) -> str:
        """Run search queries for a contact and aggregate results."""
        queries = contact.search_queries[: self.config.max_search_queries_per_contact]
        all_results = []
        for q in queries:
            try:
                result = self._search_fn(q)
                all_results.append(f"--- Query: {q} ---\n{result}\n")
            except Exception as e:
                logger.warning("Search failed for query '%s': %s", q, e)
                all_results.append(f"--- Query: {q} ---\n[Search error: {e}]\n")
        return "\n".join(all_results)

    def build_brief(self, contact: Contact, search_results: str) -> ResearchBrief:
        """Use Claude to synthesize search results into a structured research brief."""
        if not self.client:
            raise RuntimeError("Anthropic API key required. Set ANTHROPIC_API_KEY or pass via config.")

        facets_str = "\n".join(
            f"  - {k}: {v}" for k, v in self.sender.background_facets.items()
        )

        user_msg = RESEARCH_USER_TEMPLATE.format(
            name=contact.full_name,
            company=contact.company,
            role=contact.role,
            website=contact.website,
            linkedin=contact.linkedin,
            twitter=contact.twitter,
            other_links=", ".join(contact.other_links) if contact.other_links else "N/A",
            notes=contact.notes or "N/A",
            search_results=search_results,
            sender_name=self.sender.name,
            sender_role=self.sender.current_role,
            sender_company=self.sender.company,
            sender_education=self.sender.education,
            sender_facets=facets_str,
        )

        response = self.client.messages.create(
            model=self.config.model,
            max_tokens=1500,
            system=RESEARCH_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
        )

        raw_text = response.content[0].text
        brief = self._parse_brief(contact, raw_text, search_results)
        return brief

    def _parse_brief(
        self, contact: Contact, raw_text: str, search_results: str
    ) -> ResearchBrief:
        """Parse Claude's JSON response into a ResearchBrief."""
        # Extract JSON from the response (handle markdown code blocks)
        text = raw_text.strip()
        if text.startswith("```"):
            # Remove code fences
            lines = text.split("\n")
            lines = [l for l in lines if not l.strip().startswith("```")]
            text = "\n".join(lines)

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            logger.error("Failed to parse research brief JSON: %s", raw_text[:200])
            return ResearchBrief(
                contact=contact,
                raw_research=search_results,
                confidence_score=0.0,
            )

        try:
            emphasis = AngleCategory(data.get("background_emphasis", "builder_ambition_intellectual"))
        except ValueError:
            emphasis = AngleCategory.BUILDER_AMBITION

        return ResearchBrief(
            contact=contact,
            specific_facts=data.get("specific_facts", [])[:3],
            plausible_reasons=data.get("plausible_reasons", [])[:2],
            recommended_angle=data.get("recommended_angle", ""),
            background_emphasis=emphasis,
            raw_research=search_results,
            confidence_score=float(data.get("confidence_score", 0.0)),
        )

    def research_contact(self, contact: Contact) -> ResearchBrief:
        """Full pipeline: search + synthesize for one contact."""
        logger.info("Researching %s...", contact.full_name)
        search_results = self.search_contact(contact)
        brief = self.build_brief(contact, search_results)
        logger.info(
            "Research complete for %s (confidence: %.2f)",
            contact.full_name,
            brief.confidence_score,
        )
        return brief
