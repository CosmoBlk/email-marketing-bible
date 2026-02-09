# Google AI Studio Prompt — emailmarketingskill.com Landing Page Design

## Prompt

Design a landing page for emailmarketingskill.com. This is a single-page marketing site for an open-source Claude Code skill called "Email Marketing Bible." The skill is a distillation of the full Email Marketing Bible (2026) — the most comprehensive, data-backed email marketing guide ever published. It's free, open source, and covers 19 industries.

The design should be heavily inspired by https://www.marketing-skills.com — same dark terminal aesthetic, same vertical single-column centered layout, same monospace feel. But with more sections and content since this is a more comprehensive product.

---

### DESIGN SYSTEM

**Theme:** Dark mode only. No light mode toggle.

**Colours:**
- Background: `#0a0a0a` (near-black)
- Surface/card backgrounds: `#111111` or `#141414`
- Primary text: `#e5e5e5` (light gray)
- Muted text: `#888888`
- Accent: `#00ff00` (neon green) — used for highlights, hover states, active elements, and emphasis text
- Borders: `#333333` (subtle) or `#00ff00` (accent borders on key elements)

**Typography:**
- Headings: JetBrains Mono or Space Mono (monospace), bold/semibold
- Body text: Inter or system sans-serif stack
- Terminal/code blocks: JetBrains Mono
- Main title: very large (48-64px), uppercase or title case
- Body: 16-18px, 1.6 line height, max-width ~640px for readability

**Layout:**
- Single column, vertically centered
- Max-width container: ~720px for content, ~900px for wider elements like tables
- Generous vertical spacing between sections (80-120px)
- Horizontal padding: 24px on mobile, 48px on tablet+
- All text center-aligned in hero area, left-aligned in content sections below

**Components:**
- Buttons: 2px solid border, monospace text, `#e5e5e5` text on transparent background. On hover: background fills with `#e5e5e5`, text inverts to `#0a0a0a`. Pill or slightly rounded corners.
- Terminal blocks: dark card (`#111111`) with monospace text, `$` prompt prefix in muted color, copy-to-clipboard icon in top-right corner
- Cards: `#111111` background, 1px `#333333` border, subtle rounded corners
- Badges: small bordered pills with monospace text

---

### PAGE SECTIONS (top to bottom)

**Section 1: GitHub Badge**
Small bordered pill/badge at the top, centered. Contains a star icon and text. Links to the GitHub repo.
- Text: "★ Star on GitHub"
- Links to: https://github.com/CosmoBlk/email-marketing-bible
- Style: small monospace text, 1px border, rounded pill, `#333` border, `#888` text. On hover: `#00ff00` border.

---

**Section 2: Hero**
The main title block. Large, bold, centered.

- Line 1: **"Email Marketing Skill"** — very large (48-64px), white/light, bold, monospace
- Line 2: **"for Claude Code"** — same size, but in accent green (`#00ff00`)
- Below title (muted body text, max-width ~600px, centered):
  "The most comprehensive email marketing knowledge base ever compiled. 908 sources. 4,798 insights. 55,000 words. Distilled into a Claude Code skill that turns your AI into an email marketing expert."
- Author line (smaller, muted): "By George Hartley — founder of SmartrMail (28,000 customers)"

---

**Section 3: Terminal Install Command**
Dark terminal card with the install commands. This is the primary CTA.

```
$ git clone https://github.com/CosmoBlk/email-marketing-bible.git
$ cp -r email-marketing-bible ~/.claude/skills/email-marketing-bible
```

- Below the terminal: "Installs the email marketing skill to your Claude Code project" (muted, small text)
- Copy button in top-right corner of terminal card

---

**Section 4: Action Buttons**
Two buttons side by side (or stacked on mobile), centered.

- Button 1: **"Read the Full Guide"** — links to /introduction (the wiki). Primary style: `#00ff00` border, green text.
- Button 2: **"View on GitHub"** — links to https://github.com/CosmoBlk/email-marketing-bible. Secondary style: `#333` border, `#e5e5e5` text.

---

**Section 5: Stats Row**
Three stats displayed horizontally in a row, centered. Monospace numbers, muted labels below.

| 908 | 55,000 | 40 |
| Sources Crawled | Words | Expert Contributors |

Style: large monospace numbers in white, small muted labels below. Separated by vertical dividers or generous spacing.

---

**Section 6: What This Skill Does**
A section explaining what the Claude Code skill enables. Left-aligned text within centered container.

Heading: **"What you get"** (or "What this skill enables")

A clean list or grid of capabilities:
- "Analyse your email setup and identify gaps"
- "Draft email copy using proven frameworks (PAS, AIDA, Before-After-Bridge)"
- "Build automation flows — welcome series, abandoned cart, post-purchase, win-back"
- "Pull benchmarks for your industry from 19 vertical playbooks"
- "Troubleshoot deliverability issues with a 10-step diagnostic"
- "Compare email platforms for your specific needs"
- "Review compliance across GDPR, CAN-SPAM, CASL, and 4 other jurisdictions"
- "Write cold email sequences with proper infrastructure setup"

Style: minimal list with subtle green accent markers (dots, dashes, or `>` symbols). Or a 2-column grid of small cards.

---

**Section 7: Industry Playbooks**
Show all 19 industries covered. This demonstrates breadth.

Heading: **"Playbooks for 19 industries"**
Subtext: "Every vertical gets its own chapter with segment-specific tactics, benchmarks, and automation flows."

Display as a wrapped grid of small pills/tags:

Ecommerce DTC · SaaS B2B · SaaS B2C · Newsletter & Creator · Agency · Nonprofit · Healthcare · Financial Services · Real Estate · Travel & Hospitality · Education · Professional Services · Retail · Events · B2B Manufacturing · Restaurant & Food · Fitness · Media & Publishing · Marketplace & Platform

Style: small bordered pills, monospace text, `#333` border, `#888` text. Perhaps highlight 4-5 key ones in green (`#00ff00` border) — Ecommerce DTC, SaaS B2B, Newsletter & Creator, Agency, Retail.

---

**Section 8: Expert Contributors**
Social proof. Show 8 key experts referenced in the guide.

Heading: **"Built on insights from 40 leading practitioners"**

Grid of 8 expert cards (2x4 on desktop, 1-column on mobile). Each card:
- Name (bold, white)
- Specialty (muted, small)
- Company/brand (muted, small)

The 8 experts:
1. Chad S. White — Strategy — Oracle
2. Joanna Wiebe — Copywriting — Copyhackers
3. Chase Dimond — Ecommerce — Structured Agency
4. Nathan Barry — Platform — Kit (ConvertKit)
5. Ann Handley — Strategy — MarketingProfs
6. Troy Ericson — Deliverability — EmailDeliverability.com
7. Tyler Denk — Newsletter — beehiiv
8. Ben Settle — Copywriting — Email Players

Style: minimal cards, `#111` background, 1px `#333` border. Name in white, specialty and company in `#888`.

---

**Section 9: Chapter Overview**
Show the full table of contents. Demonstrates the depth and structure.

Heading: **"16 chapters. 4 appendices. Everything you need."**

Clean numbered list, each chapter is a link to its wiki page:

1. The Fundamentals
2. Building Your List
3. Segmentation and Personalisation
4. The Emails That Make Money (Automation Flows)
5. Copywriting That Converts
6. Design and Technical
7. Deliverability
8. Testing and Optimisation
9. Analytics and Measurement
10. Compliance and Privacy
11. Industry Playbooks (19 verticals)
12. Choosing Your Platform
13. Cold Email and B2B Outbound
14. AI and the Future of Email
15. Company Case Studies
16. Expert Directory

Appendix A: Benchmarks by Industry
Appendix B: Email Frequency Guide
Appendix C: Email Marketing Calendar
Appendix D: Methodology and Sources

Style: monospace numbering in `#00ff00`, chapter titles in `#e5e5e5`, links have subtle underline on hover. Left-aligned within centered container.

---

**Section 10: Case Studies**
Brief mention of the 10 company case studies included.

Heading: **"Real results from 10 companies"**
Subtext: "See exactly how these companies turned email into a competitive advantage — with real numbers."

Display company names as a horizontal row of logos or text:
Casper · Morning Brew · Duolingo · Spotify · Booking.com · Amazon · Patagonia · Nike · Starbucks · Basecamp

Style: muted text, horizontal wrap, monospace. Each name separated by `·` or displayed as small cards.

---

**Section 11: Email Capture / PDF Download CTA**
This is the lead capture section. Prominent but not aggressive.

Heading: **"Download the complete Email Marketing Bible as PDF"**
Subtext: "Get the full 55,000-word guide as a PDF. Free. We'll email you when new chapters or major updates are published."

Form:
- Email input field (dark background, `#333` border, placeholder: "you@company.com")
- Submit button: **"Get the PDF"** — green accent border/text, or solid green background with dark text

Below form (tiny muted text): "No spam. Just the guide and occasional updates. Unsubscribe anytime."

Style: the form should feel native to the dark terminal aesthetic. The input and button should be on the same line on desktop, stacked on mobile.

---

**Section 12: About / The Bible**
Brief explainer about what the Email Marketing Bible is and why it exists.

Heading: **"About the Email Marketing Bible"**

Body text (max-width ~640px, left-aligned within centered container):
"The Email Marketing Bible is the most comprehensive email marketing guide available. Version 4, published February 2026. It was built by crawling 908 sources — industry reports from Litmus, Klaviyo, HubSpot, and Salesforce; practitioner blogs; academic research; platform documentation; and thousands of community discussions from Reddit, Shopify forums, and X.

Every claim is backed by data. Every recommendation has been tested by practitioners. It covers everything from list building to deliverability to cold email infrastructure — with specific playbooks for 19 industries including ecommerce, SaaS, newsletters, agencies, nonprofits, healthcare, real estate, and more.

The guide is open source and free. The Claude Code skill distils the full 55,000 words into a structured knowledge base that Claude can reference in real time when helping you with email strategy, copywriting, automation flows, or deliverability troubleshooting."

Style: body text in `#e5e5e5`, relaxed line height, clean paragraphs.

---

**Section 13: Footer**
Minimal footer.

- Left (or centered): "Built by George Hartley"
- Link to @GTHartley on X/Twitter (use X icon)
- Link to GitHub repo (use GitHub icon)
- Small text: "SmartrMail — email marketing for 28,000 customers"

Style: muted text, small, monospace. Icons inline with text. Subtle top border (`#333`).

---

### SEO REQUIREMENTS

**Title tag:** "Email Marketing Skill for Claude Code — The Email Marketing Bible [2026]"

**Meta description:** "The most comprehensive email marketing knowledge base, distilled into a Claude Code skill. 908 sources, 55,000 words, 19 industry playbooks. Free and open source."

**H1:** "Email Marketing Skill for Claude Code" (the hero title)

**Key phrases to include naturally in page content:**
- "email marketing skill for Claude Code"
- "email marketing bible"
- "email marketing guide 2026"
- "Claude Code skill"
- "email marketing best practices"
- "email automation"
- "email deliverability"
- "email copywriting"
- "open source email marketing"

**Structured data:** SoftwareApplication schema (or Article schema for the guide)

**Open Graph:**
- og:title: "Email Marketing Skill for Claude Code"
- og:description: "The most comprehensive email marketing knowledge base. 908 sources. 55K words. 40 experts. Free and open source."
- og:image: custom OG image (dark background, green accent, title text)
- og:url: https://emailmarketingskill.com

---

### RESPONSIVE BEHAVIOUR

**Desktop (>768px):**
- Full layout as described above
- Stats row horizontal
- Expert grid 2x4
- Action buttons side by side
- Email form input + button on same line

**Mobile (<768px):**
- All sections stack vertically
- Stats row stacks to 3 rows or stays horizontal with smaller numbers
- Expert grid single column
- Action buttons stack
- Email form input + button stack
- Terminal command block scrolls horizontally if needed
- Generous touch targets (48px min)

---

### REFERENCE SITE

The primary design reference is https://www.marketing-skills.com

Match these specific elements:
1. The dark background with monospace/terminal aesthetic
2. The centered single-column layout with generous vertical spacing
3. The terminal command box with the `$` prefix
4. The bordered button style (2px border, text inversion on hover)
5. The GitHub star badge at the top
6. The "Built by [name]" footer treatment
7. The overall minimal, dev-focused feel

The difference is: emailmarketingskill.com has MORE content sections (industry playbooks, expert grid, chapter list, email capture, case studies, about section). So the page will be longer. Maintain the same visual density and spacing — don't cram sections together. Let each section breathe.

---

### OUTPUT

Generate a complete, production-ready single-page HTML file with:
1. All sections above implemented exactly as described
2. Inline CSS (or a `<style>` block) implementing the full design system
3. Responsive breakpoints for mobile/tablet/desktop
4. Working copy-to-clipboard functionality on the terminal command
5. Smooth scroll behaviour
6. All links pointing to the correct URLs
7. SEO meta tags, Open Graph tags, and structured data
8. Google Fonts import for JetBrains Mono
9. The email capture form as a client-side form (POST action to `/api/subscribe` — the backend is handled separately)
10. Favicon placeholder

The page should feel like a premium open-source developer tool landing page, not a marketing agency template. Think: Vercel, Linear, Raycast — clean, dark, monospace, technical, confident.
