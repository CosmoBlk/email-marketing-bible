# Design

Read this when: designing or critiquing an email, briefing a design agent, or choosing an archetype.
Last checked: 9 Oct 2026
Gather first: the design inputs in core §6 (screenshots of the brand's best emails or landing page, brand document, light and dark logos, approved real images), plus the email's goal and the archetype (section 6).

A design ships only through the core §0 gate and the §4 checklist.

## Contents

1. Inputs and context
2. Write for every reader
3. Substrate and production
4. Anti-slop and compliant-by-default rules
5. Direct the agent: Discover, Define, Deliver
6. Decision table: archetypes
7. The collection and who to follow

## 1. Inputs and context

- Before the first compose, gather two or three screenshots of the brand's best emails or landing page, the brand document, the logo in light and dark variants, and a folder of approved real images. Name the images to use in each email.
- After any brand-kit scrape, read it back (logo, brand name, colours, footer, social links, dark-mode logo) and fix it before the first draft. A site on a store or link-in-bio platform can hand the scrape that platform's branding instead of the brand's.
- When the brand kit changes, re-apply it to existing templates, or flag the ones still on the old version.
- **Context beats prompt.** Feed the brand kit, design tokens, a tested module library and a rules file before iterating on wording. A strong pattern: have the agent pull the brand's past emails, break them into a design system with dark-mode rules, and assemble new emails only from approved components (Email Love's StreetEasy walkthrough, Aug 2026) [vendor] https://www.youtube.com/watch?v=rZVXD2FO9nw
- Use the brand's real product and lifestyle photos. Models assemble clean blocks well and invent imagery badly (Adam Coleman, Jul 2026) [practitioner] https://www.linkedin.com/feed/update/urn:li:activity:7488231897261580289/

## 2. Write for every reader

People, inbox summarisers and the recipient's own agents now all read the email.

- **Facts first, in live text.** Offer, price, code and expiry in the first live sentence, identical across email, landing page and cart, with semantic headings and never image-only. Summaries draw mostly on the first half of the email (copy.md), and live text also wins on accessibility and dark mode.
- **Plain URLs and codes.** Put the offer's canonical public URL and any code in plain live text. OpenAI's agents auto-open only URLs a public index has already seen, so a unique tracked link doesn't qualify [primary] https://openai.com/index/ai-agent-link-safety/
- **No magic-link journeys.** Meta's Muse email connector strips one-time codes, reset links and magic links before the agent reads the mail [primary] https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse, so a login that depends on one can't be completed by a user's agent.
- **No hidden text, nothing addressed to an AI.** Hidden instructions are now an attack signature (copy.md), and Gemini leaves suspected prompt-injection mail out of its summaries (deliverability.md).
- **Image-only emails are invisible** to inbox AI and to agents reading through connectors: one tester found Claude could read text-only Klaviyo emails through the connector but not designed ones [practitioner] https://www.youtube.com/watch?v=ldMEaX8PmPw
- **Transactional email is a data feed.** Order numbers, dates, totals and tracking in live text, so Apple Mail, Siri and inbox agents can parse them (flows.md).

## 3. Substrate and production

- **Safe substrate.** Emit MJML, React Email or Maizzle (compile to inbox-safe HTML), never raw HTML from a prompt.
- **Design tools are for direction.** Production HTML comes from an email-native compiler or editor. An AI design prototype is not an email: one test exported a Claude Design "standalone HTML" file that turned out to be a zipped web app, and nothing rendered in the inbox (Mailtrap, Aug 2026) [vendor] https://www.youtube.com/watch?v=z9rXPX4ujFk. Rebuild in email-safe HTML from approved components, never send the export, and render-test dark mode before any send.
- **Don't build on fragile CSS.** Research showed CSS alone could track opens, spoof UI and hide injected text in major webmail clients, and recommended clients block selectors such as `:has`, `:checked`, `:focus` and `:not`. Content and the CTA must still work with those stripped (PortSwigger Research, Aug 2026) [primary for the findings; directional for client changes] https://portswigger.net/research/css-the-bomb-inside-your-inbox

## 4. Anti-slop and compliant-by-default rules

- AI defaults to competent and generic; force it off its defaults.
- **Anti-slop:** own one colour (30-60% of the surface); restraint over decoration; real photography, never AI stock; bold live-text headlines; one message, real negative space. Ban the purple-to-blue gradient and the beige wash. Restraint means no decoration that does no work, not empty space: dense layouts with strong hierarchy can beat minimal ones.
- **Distinctiveness.** Models and measure-and-copy loops converge on the median (Ryo Lu, "convergence to the mean", 3 Oct 2026) [practitioner] https://ryo.lu/journal/convergence-to-the-mean. Really Good Emails' most-saved Q3 2026 emails skewed playful over minimal [vendor, flagged: list size unstated and its two framings don't reconcile] https://reallygoodemails.com/school/blog/q3-2026-email-trends. Their test: which part could someone describe to a coworker tomorrow?
- **Compliant by default:** single column ≤600px, 44px tap targets, `role="presentation"` tables, dark-mode-safe colours (~#121212, never pure #000 backgrounds or #fff logos), alt text everywhere, explicit text and button colours.
- **AI imagery and the law.** Realistic AI people or scenes that could pass as real need a label for EU recipients, and AI performers in ads need a disclosure in New York; an accurately shown real product on an AI background generally doesn't (compliance.md). Plan label placement in the module library.

## 5. Direct the agent: Discover, Define, Deliver

Adapted for email from Anshu Chimala, "How to turn your AI into a world-class designer" (Lenny's Newsletter, 1 Sep 2026, https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world) via the design-director skill (the command, counts and brief format are the skill's). LLMs predict the median; divergence has to come from outside the model.

- **Seed strings.** The agent generates a random string in a shell (`openssl rand -base64 48`), derives palette, layout and type from its patterns inside the brand tokens, and never reveals it; a new string per direction.
- **Broad before deep.** Ask for 12-20 directions as one-liners, "go broad, not deep". The human picks from text before any image or code exists, then approves the brief before code. Reject anything guessable from the category alone.
- **Ambitious briefs.** One sentence naming a real reference (Graza's chartreuse drench, Aesop's restraint) plus two anti-references.
- **The critic loop.** Screenshot the rendered seed test and hand it to a separate model (the strongest vision-capable one you can reach) in a fresh context (no code, history or earlier critiques). It names the aesthetic, imagines how a top studio would execute it, lists the biggest gaps and scores /10. Fix, re-screenshot and re-critique with the same prompt (target score kept out of it) until the critic scores 9/10, capped at four rounds. The critic is about 10% of output tokens and most of the taste. With top models now close in quality, the fresh context matters more than which model is "stronger".
- **Chain models by role.** Code model for structure, image model for stills, video model for a looping hero or state transition. Current names: models.md.
- **Deliver by subtraction.** Cut glows, gradients, decorative containers and labels that repeat the visual, then a light anti-slop pass on copy (core §5) and visuals (reflex fonts, centred hero + three cards, purple on dark).
- **Keep failed prompts**; retest them on the next model generation.

## 6. Decision table: archetypes

47 curated 2026 designs, one rule: personality, restraint and point of view beat generic polish. Pick an archetype and commit; never minimal-lux by reflex.

| Situation | Archetype | The one rule | Exemplars |
|---|---|---|---|
| Boring category | Bold mono / punk | the more boring the product, the wilder the voice | Liquid Death, Frank Body |
| Premium | Minimal-lux | restraint signals quality; never discount-led; 472-520px | Aesop, Apple, Stripe |
| Visual product | Lookbook | the product is the design, full-bleed editorial photo | Dior, Clare Paint |
| Newsletter | Editorial | voice beats design; sell the moment | Patagonia, Tracksmith |
| Welcome / win-back | Founder letter | plain-text feel, first person, ask for a reply | Ugmonk, Superhuman |
| Cart abandonment | Conversation | objections in sequence or founder-personal; discount last | Tuft & Needle, Alo Yoga |
| Transactional | Brand moment | your most-opened email; design it | Stripe, Omsom |

Also: narrow width, one font family, personalise with unexpected data. Feed the collection to the agent as design context.

## 7. The collection and who to follow

- Collection: https://emailmarketingskill.com/19-best-email-designs-2026/
- Repo: https://github.com/CosmoBlk/bestemaildesigns
- Figma file: https://www.figma.com/community/file/1626130771879679378 (returns 403 to non-browser fetches; open it in a browser).
- Who to follow on designing with AI (Chapter 18): Anshu Chimala @anshuc, Karri Saarinen @karrisaarinen, Ryo Lu @ryolu_, Jenny Wen @jenny_wen, Lee Munroe @leemunroe. The full directory is in sources.md.
