"""Email generation engine — turns research briefs into personalized cold emails."""

from __future__ import annotations

import json
import logging

from .models import Contact, ResearchBrief, EmailDraft, AngleCategory
from .config import SenderProfile, PipelineConfig

logger = logging.getLogger(__name__)

EMAIL_SYSTEM_PROMPT = """\
You are a cold email ghostwriter. You write emails on behalf of the sender \
that are warm, sharp, polished, and human. Each email must feel individually \
crafted — never mass-produced.

STRICT RULES:
1. 3–5 sentences ONLY. No more.
2. Mention 1–2 specific things the sender has done or is working on.
3. Include credible, specific admiration for the recipient's work — tied to \
   something concrete they built, wrote, invested in, researched, or said.
4. End with a low-friction CTA (quick call, brief conversation, whenever convenient).
5. NEVER use vague praise like "I admire your impressive background" or \
   "Your work is inspiring."
6. NEVER invent facts about the recipient or sender.
7. NEVER use exclamation marks in the email body.
8. Vary the sender's framing based on the angle — do not reuse the same intro.
9. Sound human. No corporate jargon. No filler. No buzzwords.
10. The email should make the recipient feel that the sender is paying close \
    attention to them specifically.
"""

EMAIL_USER_TEMPLATE = """\
Write a personalized cold email for the following recipient.

RECIPIENT:
- Name: {recipient_name}
- Company: {recipient_company}
- Role: {recipient_role}

RESEARCH BRIEF:
- Specific facts about them:
{facts}
- Recommended angle: {recommended_angle}

SENDER:
- Name: {sender_name}
- Background emphasis to use: {emphasis_label}
- Details: {emphasis_detail}
- Education: {sender_education}
- Company: {sender_company}

PREVIOUS ANGLES USED (do NOT repeat these framings):
{previous_angles}

TONE:
{tone_guidelines}

ANTI-PATTERNS (avoid these):
{anti_patterns}

Return your response as JSON:
{{
  "subject_lines": ["Subject 1", "Subject 2", "Subject 3"],
  "body": "The email body, 3-5 sentences.",
  "sender_details_used": ["brief note on which sender details you emphasized"]
}}

Write the email now. Remember: 3-5 sentences, specific praise, low-friction CTA, human tone.
"""


class EmailGenerator:
    """Generates personalized cold emails from research briefs."""

    def __init__(self, config: PipelineConfig, sender: SenderProfile):
        self.config = config
        self.sender = sender
        self.client = None
        if config.anthropic_api_key:
            from anthropic import Anthropic
            self.client = Anthropic(api_key=config.anthropic_api_key)
        self._previous_angles: list[str] = []

    def generate(self, brief: ResearchBrief) -> EmailDraft:
        """Generate a personalized email from a research brief."""
        if not self.client:
            raise RuntimeError("Anthropic API key required.")

        if not brief.is_sufficient:
            logger.warning(
                "Low confidence brief for %s (%.2f). Generating with caution.",
                brief.contact.full_name,
                brief.confidence_score,
            )

        emphasis_key = brief.background_emphasis.value
        emphasis_detail = self.sender.background_facets.get(
            emphasis_key,
            self.sender.background_facets.get("builder_ambition_intellectual", ""),
        )

        facts_str = "\n".join(f"  {i+1}. {f}" for i, f in enumerate(brief.specific_facts))

        previous_str = (
            "\n".join(f"  - {a}" for a in self._previous_angles[-5:])
            if self._previous_angles
            else "  (none yet — this is the first email)"
        )

        tone_str = "\n".join(f"  - {t}" for t in self.sender.tone_guidelines)
        anti_str = "\n".join(f"  - {a}" for a in self.sender.anti_patterns)

        user_msg = EMAIL_USER_TEMPLATE.format(
            recipient_name=brief.contact.full_name,
            recipient_company=brief.contact.company,
            recipient_role=brief.contact.role,
            facts=facts_str,
            recommended_angle=brief.recommended_angle,
            sender_name=self.sender.name,
            emphasis_label=brief.background_emphasis.value.replace("_", " ").title(),
            emphasis_detail=emphasis_detail,
            sender_education=self.sender.education,
            sender_company=self.sender.company,
            previous_angles=previous_str,
            tone_guidelines=tone_str,
            anti_patterns=anti_str,
        )

        response = self.client.messages.create(
            model=self.config.model,
            max_tokens=1000,
            system=EMAIL_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
        )

        raw_text = response.content[0].text
        draft = self._parse_draft(brief, raw_text)

        # Track this angle so we don't repeat framing
        self._previous_angles.append(
            f"{brief.contact.full_name}: {brief.background_emphasis.value} — {brief.recommended_angle}"
        )

        return draft

    def _parse_draft(self, brief: ResearchBrief, raw_text: str) -> EmailDraft:
        """Parse the JSON email draft from Claude's response."""
        text = raw_text.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            lines = [l for l in lines if not l.strip().startswith("```")]
            text = "\n".join(lines)

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            logger.error("Failed to parse email draft JSON: %s", raw_text[:200])
            return EmailDraft(
                recipient=brief.contact,
                research_brief=brief,
                body="[GENERATION FAILED — manual draft required]",
                angle_used=brief.background_emphasis,
            )

        return EmailDraft(
            recipient=brief.contact,
            research_brief=brief,
            subject_lines=data.get("subject_lines", [])[:3],
            body=data.get("body", ""),
            angle_used=brief.background_emphasis,
            sender_details_used=data.get("sender_details_used", []),
        )
