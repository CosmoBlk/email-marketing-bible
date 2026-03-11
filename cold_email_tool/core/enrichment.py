"""Smart enrichment engine — turns sparse inputs into rich contact profiles.

Given minimal info (name + one identifier), this engine:
1. Infers missing fields from what's available (e.g., email domain -> company)
2. Generates targeted search queries
3. Uses Claude to resolve identity and fill in role/company/details
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from typing import Optional

from .models import Contact

logger = logging.getLogger(__name__)

ENRICHMENT_SYSTEM = """\
You are an identity resolution and enrichment assistant. Given sparse information \
about a person (a name plus one or two identifiers), your job is to determine who \
they are and fill in their professional profile using ONLY the search results provided.

RULES:
- Only output facts clearly supported by the search results.
- If you cannot confidently determine something, leave it blank or mark it uncertain.
- Never invent or guess information.
- If multiple people match, pick the most prominent/likely match and note the ambiguity.
- Return valid JSON only.
"""

ENRICHMENT_USER = """\
I have sparse information about someone. Please identify them and enrich their profile \
using the search results below.

KNOWN INFORMATION:
- Name: {name}
- Email: {email}
- LinkedIn: {linkedin}
- Company: {company}
- Website: {website}
- Twitter/X: {twitter}
- Notes: {notes}

SEARCH RESULTS:
<search_results>
{search_results}
</search_results>

Based ONLY on the search results, return a JSON object with the enriched profile:
{{
  "full_name": "Their full name as commonly known",
  "company": "Current company or organization",
  "role": "Current role or title",
  "website": "Personal or company website if found",
  "linkedin": "LinkedIn URL if found",
  "twitter": "Twitter/X URL if found",
  "bio_summary": "1-2 sentence summary of who they are",
  "identity_confidence": 0.0 to 1.0,
  "ambiguity_note": "Any notes about identity uncertainty, or empty string"
}}

If the search results are empty or unhelpful, still return the JSON with what you know \
and set identity_confidence accordingly (low if uncertain).
"""


@dataclass
class SparseInput:
    """Minimal input for a person — only name is required."""
    name: str
    email: str = ""
    linkedin: str = ""
    company: str = ""
    website: str = ""
    twitter: str = ""
    notes: str = ""

    def infer_company_from_email(self) -> str:
        """Try to extract a company name from an email domain."""
        if not self.email or "@" not in self.email:
            return ""
        domain = self.email.split("@")[1].lower()
        # Skip generic email providers
        generic = {
            "gmail.com", "yahoo.com", "hotmail.com", "outlook.com",
            "icloud.com", "protonmail.com", "mail.com", "aol.com",
            "proton.me", "hey.com", "fastmail.com",
        }
        if domain in generic:
            return ""
        # Extract company name from domain (strip TLD)
        parts = domain.split(".")
        if len(parts) >= 2:
            return parts[0].capitalize()
        return ""

    def infer_website_from_email(self) -> str:
        """Try to infer a website from an email domain."""
        if not self.email or "@" not in self.email:
            return ""
        domain = self.email.split("@")[1].lower()
        generic = {
            "gmail.com", "yahoo.com", "hotmail.com", "outlook.com",
            "icloud.com", "protonmail.com", "mail.com", "aol.com",
            "proton.me", "hey.com", "fastmail.com",
        }
        if domain in generic:
            return ""
        return f"https://{domain}"

    def generate_search_queries(self) -> list[str]:
        """Generate smart search queries from whatever we have."""
        queries = []
        name = self.name.strip()
        if not name:
            return queries

        # Always search the name
        if self.company:
            queries.append(f'"{name}" "{self.company}"')
        if self.email and "@" in self.email:
            domain = self.email.split("@")[1]
            queries.append(f'"{name}" "{domain}"')
        if self.linkedin:
            # Extract the profile slug and search with it
            queries.append(f'"{name}" site:linkedin.com')
        if self.website:
            domain = re.sub(r"https?://", "", self.website).rstrip("/")
            queries.append(f'"{name}" "{domain}"')
        if self.twitter:
            handle = self.twitter.rstrip("/").split("/")[-1].lstrip("@")
            queries.append(f'"{name}" "@{handle}" OR "{handle}"')

        # General search
        queries.append(f'"{name}" who is OR about OR bio OR profile')
        queries.append(f'"{name}" interview OR podcast OR talk OR essay')

        # Deduplicate while preserving order
        seen = set()
        unique = []
        for q in queries:
            if q not in seen:
                seen.add(q)
                unique.append(q)
        return unique[:5]


@dataclass
class EnrichmentResult:
    """Result of enriching a sparse input."""
    original_input: SparseInput
    contact: Contact
    bio_summary: str = ""
    identity_confidence: float = 0.0
    ambiguity_note: str = ""
    enrichment_sources: list[str] = field(default_factory=list)

    @property
    def is_confident(self) -> bool:
        return self.identity_confidence >= 0.6

    @property
    def confidence_label(self) -> str:
        if self.identity_confidence >= 0.8:
            return "High"
        elif self.identity_confidence >= 0.5:
            return "Medium"
        else:
            return "Low"


class EnrichmentEngine:
    """Enriches sparse contact inputs into full Contact profiles."""

    def __init__(self, anthropic_api_key: str, model: str = "claude-sonnet-4-20250514", search_fn=None):
        self.api_key = anthropic_api_key
        self.model = model
        self._search_fn = search_fn or self._default_search
        self._client = None

    @property
    def client(self):
        if self._client is None:
            from anthropic import Anthropic
            self._client = Anthropic(api_key=self.api_key)
        return self._client

    @staticmethod
    def _default_search(query: str) -> str:
        return f"[No search results available for: {query}]"

    def enrich(self, sparse: SparseInput) -> EnrichmentResult:
        """Enrich a sparse input into a full contact profile."""
        # Step 1: Infer what we can locally
        inferred_company = sparse.company or sparse.infer_company_from_email()
        inferred_website = sparse.website or sparse.infer_website_from_email()

        # Step 2: Search
        queries = sparse.generate_search_queries()
        all_results = []
        for q in queries:
            try:
                result = self._search_fn(q)
                all_results.append(f"--- Query: {q} ---\n{result}\n")
            except Exception as e:
                logger.warning("Search failed for '%s': %s", q, e)
                all_results.append(f"--- Query: {q} ---\n[Error: {e}]\n")

        search_text = "\n".join(all_results)

        # Step 3: Use Claude to resolve identity
        user_msg = ENRICHMENT_USER.format(
            name=sparse.name,
            email=sparse.email or "not provided",
            linkedin=sparse.linkedin or "not provided",
            company=inferred_company or "not provided",
            website=inferred_website or "not provided",
            twitter=sparse.twitter or "not provided",
            notes=sparse.notes or "none",
            search_results=search_text,
        )

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            system=ENRICHMENT_SYSTEM,
            messages=[{"role": "user", "content": user_msg}],
        )

        raw = response.content[0].text
        return self._parse_result(sparse, raw, search_text)

    def _parse_result(self, sparse: SparseInput, raw: str, search_text: str) -> EnrichmentResult:
        text = raw.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            lines = [l for l in lines if not l.strip().startswith("```")]
            text = "\n".join(lines)

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            logger.error("Failed to parse enrichment JSON: %s", raw[:200])
            return EnrichmentResult(
                original_input=sparse,
                contact=Contact(
                    full_name=sparse.name,
                    company=sparse.company,
                    website=sparse.website,
                    linkedin=sparse.linkedin,
                    twitter=sparse.twitter,
                ),
                identity_confidence=0.1,
                ambiguity_note="Enrichment parsing failed",
            )

        contact = Contact(
            full_name=data.get("full_name", sparse.name),
            company=data.get("company", sparse.company) or "",
            role=data.get("role", "") or "",
            website=data.get("website", sparse.website) or "",
            linkedin=data.get("linkedin", sparse.linkedin) or "",
            twitter=data.get("twitter", sparse.twitter) or "",
            notes=sparse.notes,
        )

        return EnrichmentResult(
            original_input=sparse,
            contact=contact,
            bio_summary=data.get("bio_summary", ""),
            identity_confidence=float(data.get("identity_confidence", 0.5)),
            ambiguity_note=data.get("ambiguity_note", ""),
        )
