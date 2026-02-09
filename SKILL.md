---
name: email-marketing-bible
description: >
  The Email Marketing Bible v0.4 — comprehensive, data-backed email marketing
  knowledge base by George Hartley (SmartrMail, 28K customers). Built from
  908 sources and 4,798 insights. Covers strategy, flows, deliverability,
  copywriting, segmentation, compliance, cold email, AI, platform selection,
  and 19 industry playbooks. Updated February 2026.
version: 0.4
topics:
  - email marketing
  - campaign strategy
  - marketing automation
  - deliverability
  - segmentation
  - personalisation
  - copywriting
  - cold email
  - compliance
  - AI and email
  - platform selection
  - industry playbooks
---

# Email Marketing Bible v0.4 — Skill Reference

> Source: EMB v0.4 (~55K words, 16 chapters, 4 appendices). George Hartley, Feb 2026.
> Use this skill to: analyse email setups, identify gaps, draft copy, build automation flows, pull benchmarks, troubleshoot deliverability, and advise on platform selection.

---

## 1. FUNDAMENTALS

### Why Email Wins
- ROI: $36 per $1 spent (3,600%). Newsletter-as-business: 122%. Social: 28%. Paid search: 25%.
- 89% of marketers use email as primary lead gen channel. 51% of consumers prefer email from brands.
- Email is owned media — no algorithm throttling, no platform risk.
- Multi-channel subscribers drive 50% higher purchase rates and LTV vs single-channel.
- Email produces a revenue "halo effect" — higher daily revenue on send days even among non-openers.

### The Email Stack (6 components)
1. **ESP** — sending platform (Klaviyo, Mailchimp, etc.). Chapter 12 covers selection.
2. **Authentication** — SPF, DKIM, DMARC. Non-negotiable since Feb 2024 Google/Yahoo rules.
3. **List management** — quality > size. 5K engaged beats 50K messy.
4. **Content & design** — 60%+ opens on mobile. Mobile-first is essential.
5. **Automation** — flows generate 30x more RPR than campaigns. Set up flows before campaigns.
6. **Analytics** — 21% of marketers don't measure ROI. Don't be one of them.

### Key Metrics & Benchmarks

| Metric | Good | Strong | Red Flag |
|---|---|---|---|
| Click-through rate | 2-3% | 4%+ | Below 1% |
| Click-to-open rate | 10-15% | 20%+ | Below 5% |
| Unsubscribe rate | Under 0.2% | Under 0.1% | Above 0.5% |
| Bounce rate | Under 2% | Under 1% | Above 3% |
| Spam complaint rate | Under 0.1% | Under 0.05% | Above 0.3% |
| List growth rate | 3-5%/month | 5%+/month | Negative |
| Delivery rate | 95%+ | 98%+ | Below 85% |
| Inbox placement | 85-94% | 94%+ | Below 70% |

**Post-Apple MPP:** Open rates are directional only (50-60% of opens are Apple Mail bot pre-fetches). Use click-based metrics as primary. Open rates still useful for A/B comparisons.

### Tags vs Segments vs Lists
- **Lists:** Use ONE master list. Multiple lists = duplicate subscribers, inconsistent data.
- **Tags:** Labels on subscribers (facts). Applied manually or via automation.
- **Segments:** Dynamic groups based on rules. Auto-update as conditions change.
- Rule of thumb: tags store information, segments target sends.
- Minimum segments: new (last 30 days), engaged (clicked last 60 days), customers vs non-customers, lapsed (90+ days).

### Gmail Tabs
- Promotions tab ≠ spam. It's correct categorisation for commercial email.
- Promotions tab emails can have higher conversion rates (buying mindset).
- To increase Primary tab chances: encourage replies, ask subscribers to drag to Primary, use text-heavy emails, send from personal names.
- Don't obsess over tabs. Many successful brands operate entirely from Promotions.

---

## 2. LIST BUILDING

### Organic Growth
- **Lead magnets:** Templates/swipe files convert highest. Free template increased signups by 384%. Gifts/giveaways increase signups by 300%.
- **Content upgrades:** 5-10x better opt-in vs generic sidebar forms. Match offer to content.
- **Signup forms:** Form > link (20-50% more opt-ins). Optimal fields: 3-5 for top-of-funnel. "Get my templates" > "Subscribe" (33% lift from specific button copy).
- Best performing 2025-2026: templates, checklists, calculators/tools, mini-courses (3-5 day), quizzes.
- Declining: long PDFs/ebooks, generic guides, webinar registrations.

### Popups
- Well-timed popups: 3-5% conversion. Top 10%: 9.28%.
- Exit-intent: 4-7%. Timed (15-30s delay): 2-4%. Scroll-triggered (50%+): 2-5%.
- Two-step popups (yes/no then email field): 30-50% better than single-step.
- Mobile: don't cover primary content on load (Google penalty). Use bottom bar or delayed slide-in.
- A/B test the offer, not just the design.

### Double vs Single Opt-in
- Double opt-in recommended for most. Validates addresses, prevents bots/traps, GDPR-ready.
- Trade-off: lose 20-30% of signups (but those are low-quality).
- Compromise: single opt-in for purchasers, double for lead magnets/popups.
- Double opt-in = best defence against spam traps and list bombing.

### List Hygiene
- Lists decay 22-30% annually. B2B: ~2.1%/month.
- Unengaged subscribers cost money (ESP fees) AND hurt deliverability.
- **Sunset flow:** Reduce frequency → re-engagement series (2-3 emails) → suppress non-responders.
- Brands removing unengaged contacts often see revenue INCREASE (better inbox placement).

### Spam Traps
- **Pristine:** Never-used honeypots. One hit = potential Spamhaus SBL listing. Signals purchased/scraped list.
- **Recycled:** Abandoned addresses reactivated as traps. Signals poor bounce handling.
- **Typo:** gnail.com, hotmial.com etc. Signals no validation at signup.
- **Role-based:** info@, admin@, sales@ repurposed. Signals scraped business contacts.
- **Prevention:** Double opt-in, real-time validation at signup, regular list cleaning (quarterly), engagement-based sending, CAPTCHA/honeypot fields.

### Email Validation Services

| Service | Price/1K | Strength |
|---|---|---|
| ZeroBounce | $3-8 | AI scoring, abuse detection |
| NeverBounce | $3-8 | Real-time API, Zapier |
| BriteVerify | $5-10 | Enterprise, CRM integrations |
| Kickbox | $4-8 | Sendex deliverability score |
| EmailListVerify | $2-5 | Budget bulk cleaning |

---

## 3. SEGMENTATION & PERSONALISATION

### Personalisation Hierarchy (most to least impactful)
1. **Behavioural:** Product recs from browse/purchase history. Highest impact.
2. **Lifecycle:** Different content for new, active, VIP, at-risk, lapsed.
3. **Dynamic content blocks:** Different images/products/sections per segment in one template.
4. **Send-time:** Per-subscriber optimal timing. Most ESPs offer this.
5. **Location-based:** Weather, events, timezone, nearby stores.
6. **Name/demographic:** First name, birthday. Fine as addition, not meaningful alone.

First-name-only personalisation can actually HURT performance (sets expectation of relevance that generic body fails to deliver).

### Segmentation Types
- **Demographic:** Age, gender, income, location. Useful for broad targeting. Timezone segmentation alone meaningfully improves opens.
- **Behavioural:** Purchase history, email engagement, browsing, cart abandonment. Highest conversion rates.
- **Lifecycle stages:** Prospect → New customer (30d) → Active (90d, 2+ purchases) → VIP → At-risk → Lapsed (90-180d) → Churned (180d+).
- **Psychographic:** Lifestyle, values, interests. Best collected via zero-party data.
- **RFM:** Recency, Frequency, Monetary scoring (1-5 each).

### RFM Quick Start
Simple version captures 80% of value: segment by recency of last purchase into 4 groups:
1. Purchased last 30 days (active)
2. 31-90 days ago (warm)
3. 91-180 days ago (cooling)
4. 180+ days ago (cold)

Full RFM treatment:
| Score | Type | Treatment |
|---|---|---|
| 5-5-5 | Champions | VIP, early access, referral asks |
| 5-1-1 | New customers | Onboarding, educate, build habit |
| 4-4-4 to 5-4-4 | Loyal | Cross-sell, upsell, reviews |
| 1-5-5 | At-risk champions | Win-back urgently |
| 1-1-1 | Hibernating | Sunset or heavy discount |

### Engagement-Based Sending (highest-impact optimisation)
- **Tier 1:** Clicked last 30 days → every campaign
- **Tier 2:** Clicked last 60 days → 75% of sends
- **Tier 3:** Clicked last 90 days → best content only (50%)
- **Tier 4:** No engagement 90-180 days → re-engagement flow only
- **Tier 5:** 180+ days → sunset flow
- Results: 15-30% better open rates, 20-40% fewer complaints, revenue stays flat or increases.

### Engagement Scoring Model

| Action | Points |
|---|---|
| Reply | 15 |
| Purchase | 10 |
| Click | 5 |
| Website visit | 3 |
| Open | 1 |

Decay: 10% per week. Use score for send frequency, content type, flow eligibility, sunset timing.

### Zero-Party Data Collection
- Welcome survey (email 2-3): ask one segmentation question.
- Preference centres: 20-30% who click "unsubscribe" will adjust preferences instead.
- Quizzes, post-purchase surveys.
- More reliable than inferred data. Builds trust.

### Waterfall Segmentation
Priority order prevents "three emails in one day":
1. Abandoned cart (highest)
2. Post-purchase follow-up
3. Browse abandonment
4. Win-back
5. Promotional (lowest)

Customer gets enrolled only in highest-priority qualifying flow.

---

## 4. AUTOMATION FLOWS (Revenue Engines)

### Performance: Automations vs Campaigns

| Metric | Automations | Campaigns |
|---|---|---|
| Revenue per recipient | 30x higher | Baseline |
| Open rate | 40-55% | 15-25% |
| Click rate | 5-10% | 2-3% |
| Relevance | Behaviour-triggered | Calendar-triggered |

### Flow Priority Order (by revenue impact per setup hour)
1. Welcome series
2. Abandoned cart
3. Browse abandonment
4. Post-purchase follow-up
5. Win-back / re-engagement
6. Cross-sell / upsell
7. VIP / loyalty flows
8. Sunset flow
9. Birthday / anniversary
10. Replenishment (consumables)
11. Back-in-stock notifications
12. Price drop alerts

### Welcome Series (4-6 emails, 1-2 weeks)
- Open rate: 51-55%. Revenue: 320% more per email vs promotional.
- **Email 1 (immediate):** Deliver promise + ask for reply (deliverability hack) + one segmentation question.
- **Email 2 (Day 2):** Brand story. Who you are, why you exist.
- **Email 3 (Day 4):** Social proof. Testimonials, reviews, case studies.
- **Email 4 (Day 7):** Best content/product. Use segmentation data from Email 1.
- **Email 5 (Day 10):** Soft sell. Most purchases happen within 10 days of signup.
- **Email 6 (Day 14):** Set expectations + preference centre link.
- Exit condition: stop if subscriber converts (move to post-purchase flow).

### Abandoned Cart (3 emails)
- 70% of carts abandoned. Recovery: 17.12% conversion. Top 10%: $3.07 RPR.
- **Email 1 (1-4h):** Simple reminder. "Having trouble checking out?" > guilt trip (30% conversion increase). NO discount. Speed is critical — 1 hour beats 4 hours.
- **Email 2 (24h):** Address objections. Reviews, shipping info, guarantee.
- **Email 3 (48h, optional):** Small incentive if margins allow. Unique expiring code. First-time abandoners only.
- Smart discount: first-time visitors get discount, returning customers don't.
- Browse abandonment: lighter version, 24h after browsing, show viewed + similar items.

### Post-Purchase Sequence
| Timing | Email | Purpose |
|---|---|---|
| Immediately | Order confirmation | Receipt + product recs in first 300px |
| Day 2-3 | Shipping confirmation | Tracking + anticipation |
| Day 7-10 | Delivery follow-up | Check satisfaction, offer help |
| Day 14 | Review request | Social proof collection |
| Day 21-30 | Cross-sell | Complementary products |
| Day 25-30 | Replenishment | Easy reorder (consumables) |

### Win-Back (2-4 emails, target 60-90 day inactive)
1. "We miss you" — what's new, what they're missing
2. Value offer — discount or exclusive access
3. Breakup email — "Should I remove you?" (highest reply rate, 10-15% re-engagement)
4. Confirmation — "You've been unsubscribed" + easy re-subscribe link
- Suppression ≠ deletion. Keep data, stop mailing.

### Nurture Sequences
- 4-10 emails, 4 days to 2 weeks apart. 63% convert within 3 months when nurtured.
- Each email: standalone value, not just teasing a sale.
- B2B: behaviour-triggered > time-based. Target: >20% open, >12% CTOR.

### Promotional Campaigns
- 3:1 ratio: three value emails per one promotional.
- Segmented promotions: 780% more revenue than non-segmented.
- Resending to non-openers (different subject, 24-48h later): 15-20% extra opens. Use sparingly.

### Transactional Emails
- 3-8x higher open rates than marketing. 6x more revenue. Users spend ~8 seconds reading.
- Separate infrastructure: different subdomain/IP from marketing.
- Speed: password resets — users give up after 60 seconds. Target 99%+ delivery, sub-second.
- Don't use no-reply@ — kills engagement signals and frustrates customers.
- Keep transaction content in first 300px. Can add recs below.

---

## 5. COPYWRITING

### Subject Lines
- 64% decide to open based on subject line. 45% on sender name.
- Length: under 25 chars = highest opens. 30-50 chars = best balance opens + conversions. Mobile: under 30 chars.
- Be specific, not clever. Numbers work well.
- Personalisation: +14% opens. But body must deliver on promise.
- Skip emojis in triggered emails. Use sparingly in campaigns.
- In campaigns: avoid "you"/"your" (triggers "being sold to" filter).
- Negative framing can outperform positive (loss aversion).
- First-person CTA copy > second-person ("Start my free trial" > "Start your free trial", 25-35% lift).

### Preview Text
- +5 percentage points open rate with intentional preheader. Under 50 chars.
- Complement, don't repeat subject line. Write as a pair.
- If blank, email clients pull "View in browser" or alt tags. Looks sloppy.

### Body Copy
- Inverted pyramid: key message first. Short paragraphs (1-3 sentences).
- "I" > "we". Write for one person.
- Read aloud before sending. Write, then cut 30%.
- Positive language: +22% conversion.
- Drip sequences: 80% higher opens, 3x more clicks vs single sends.

### Copywriting Frameworks
- **AIDA:** Attention → Interest → Desire → Action. Best for promotional.
- **PAS:** Problem → Agitate → Solution. Best for cold email, B2B.
- **BAB:** Before → After → Bridge. Best for case studies.
- **4Ps:** Promise → Picture → Proof → Push. Best for mid-funnel.
- **Star-Story-Solution:** Character + story + your solution. Best for nurture.
- **Soap Opera Sequence (Andre Chaperon):** Multi-email narrative with cliffhangers. 70%+ open rates deep in sequence.
- **1-3-1 Newsletter:** One big story + three shorter items + one CTA.

### Psychology Principles
- **Curiosity Gap** (Loewenstein): gap between what we know and want to know. Always deliver.
- **Loss Aversion** (Kahneman/Tversky): losses felt 2x as intensely as gains. "Don't miss" > "Get".
- **Narrative Transportation:** Stories lower resistance to persuasion.
- **Commitment/Consistency** (Cialdini): micro-commitments prime bigger yeses.
- **Social Proof:** Specific numbers + named companies + real testimonials.
- **Zeigarnik Effect:** Uncompleted tasks remembered more vividly. Powers open loops.

### CTAs
- Buttons > text links (+27% CTR). Single CTA: +42% clicks vs multiple.
- Specific text: "Get my 20% discount" > "Shop now".
- Place CTA above fold AND below main content (+35% total clicks).
- Cold email: interest-based CTAs ("Worth exploring?") get 2-3x more replies than meeting requests.

### Plain Text vs HTML
- Plain text outperforms in B2B, personal brands, relationship businesses.
- Designed emails outperform in ecommerce (product images essential).
- "Designed plain text" hybrid: clean template, minimal branding, primarily text. Right for most SaaS/education/services.
- Heavy HTML → spam filters + Promotions tab.

---

## 6. DESIGN & TECHNICAL

### Mobile-First
- 60%+ opens on mobile. 64% delete emails that display poorly on phone.
- Single-column layouts. Width: 600-640px. Touch targets: 44x44px minimum.
- Font: 14-16px body, 20-22px headlines. 13px minimum on iPhone (avoids auto-zoom).
- Images: under 200KB each, total email under 800KB. Use web-safe fonts as primary stack.

### Email Client Compatibility
- Still building with HTML tables (Outlook uses Word's rendering engine).
- Inline CSS (external stylesheets stripped). Hybrid/spongy design as fallback.
- Test on actual devices (Litmus, Email on Acid, or manual on phone).
- Retina: export images at 2x display size.

### Dark Mode (33%+ of recipients)
- Transparent PNGs for logos. Off-white (#F5F5F5) backgrounds > pure white.
- `@media (prefers-color-scheme: dark)` — supported in Apple Mail, Outlook. Gmail ignores it.
- Dark grey text (#333) > pure black (#000). Borders on buttons.

### Accessibility
- Colour contrast: 4.5:1 normal text, 3:1 large text.
- Alt text on all images. Logical reading order. `lang` attribute. role="presentation" on layout tables.
- Links: clear purpose from text alone ("Download report" > "Click here").
- Don't rely on colour alone to convey info.

### Design Tools

| Tool | Type | Best For |
|---|---|---|
| Beefree (BEE) | No-code | Marketing teams, saved modules |
| Stripo | No-code + code | AMP support, 1400+ templates |
| Litmus | Testing | 90+ email client previews |
| MJML | Code framework | Developers, responsive markup |
| Maizzle | Code framework | Tailwind CSS for email |
| React Email | Code framework | React developers |

---

## 7. DELIVERABILITY

### Authentication (all three required)
**SPF:** DNS TXT record listing authorised sending IPs. 10 DNS lookup limit. End with `-all` (hard fail). Use SPF flattening if hitting lookup limit.

**DKIM:** Digital signature on every email. 2048-bit RSA keys. Rotate annually. `d=` domain must align with From address for DMARC.

**DMARC:** Policy layer tying SPF + DKIM together. Implement in stages:
1. `p=none` (monitoring, 2-4 weeks)
2. `p=quarantine` (failed → spam)
3. `p=reject` (failed → rejected)

**BIMI:** Brand logo in inbox. Requires DMARC enforcement + VMC (~$1,500/year). Supported by Gmail, Yahoo, Apple Mail.

**Implementation order:** SPF → DKIM → DMARC (p=none) → advance DMARC → BIMI.

### Sender Reputation
- Domain reputation > IP reputation for Gmail (120-day window).
- Bounce rates: < 1%. Spam complaints: < 0.1%. Engagement heavily weighted.
- Dedicated IP: only if sending 1M+/month. Below that, shared IPs from reputable ESPs are fine.
- Recovery sequence (Troy Ericson): fix auth → clean list → rebuild engagement with healthiest segments.

### Inbox Placement vs Delivery Rate
- Delivery rate: % accepted by server (95%+ good). Does NOT mean inbox.
- Inbox placement: % that land in inbox vs spam (85-94% good, 94%+ excellent).
- Can have 98% delivery and 50% inbox placement. Monitor both.
- Tools: GlockApps, Validity Everest, mail-tester.com.

### Gmail Engagement-Based Filtering
- Gmail seeds initial batch to subset, watches engagement, decides for remainder.
- Send to most engaged subscribers first. Tier by engagement level, stagger sends.
- Positive signals: opens, clicks, replies, move from Promotions → Primary.
- Negative signals: delete without opening, mark as spam, ignore.

### Domain/IP Warming

| Phase | Daily Volume |
|---|---|
| Days 1-3 | 50-100 |
| Days 4-7 | 200-500 |
| Week 2 | 500-1,000 |
| Week 3 | 1,000-5,000 |
| Week 4 | 5,000-10,000 |
| Week 5+ | Scale to full |

Start with most engaged subscribers. Ramp 20-50%/day. If bounces >2% or complaints >0.1%, slow down.

### Spam Filter Triggers (2026)
- **High impact:** URL reputation (most important content factor), URL shorteners, image-only emails, mismatched link text/URLs.
- **Medium:** ALL CAPS, excessive punctuation, spam phrases (only matters with borderline reputation).
- **Low/myth:** Individual "spam words" like "free" or "discount" — negligible with good reputation.
- **Required:** List-Unsubscribe header + List-Unsubscribe-Post (one-click) for bulk senders (5K+/day to Gmail/Yahoo).

### Sending Identity
- Separate marketing from transactional: different subdomains (mail.brand.com vs transact.brand.com). Worth it at 40K+/month.
- From name: personal names get +3.81% opens. "George from SmartrMail" > "SmartrMail" > "SmartrMail Team".
- Always set monitored reply-to. Replies = positive engagement signal. no-reply@ is actively harmful.
- Branded sending domain once database > 5,000 profiles.

### Deliverability Diagnosis (10-step framework)
1. Identify symptom (lower placement? higher bounces? specific provider?)
2. Check authentication (SPF, DKIM, DMARC passing?)
3. Check blocklists (Spamhaus, Barracuda, SpamCop via MXToolbox)
4. Check reputation (Google Postmaster Tools, Microsoft SNDS, Cisco Talos)
5. Analyse bounce logs (categorise by type and ISP)
6. Review sending patterns (volume spikes? old segments? template changes?)
7. Check content (bad URLs? shorteners? image-only? missing List-Unsubscribe?)
8. Test and validate (seed lists via GlockApps, InboxReady)
9. Remediate root cause before anything else
10. Monitor recovery (2-4 weeks typical, Gmail up to 120 days)

### Monitoring Tools
- **Google Postmaster Tools** (free, essential, needs 200-500 msgs/day to Gmail)
- **Microsoft SNDS** (IP-level for Outlook)
- **MXToolbox** (100+ blocklist check)
- **Sender Score** (0-100, above 80 good)

---

## 8. TESTING & OPTIMISATION

### What to Test (priority framework: impact × compounding)
- **Highest priority:** Sender name (compounds across every future send), CTA format, email template structure.
- **High priority:** Subject lines (high impact, low compounding — each is unique).
- **Worth testing:** Send time, content length, plain text vs HTML, hero image vs none, preheader text.

### Statistical Significance
- Only 1 in 7 tests produces significant winner. 6/7 = a draw. Normal.
- Sample sizes: <5K list: test 20-30%. 5K-50K: 15-25%. 50K+: 10-20%.
- Wait times: open rate: 2 hours for 80% accuracy. Revenue: full day for 90%.
- Use significance calculator (95% confidence). Don't eyeball.
- Prioritise testing automated flows over campaigns (flow improvements compound indefinitely).

### Send Time Optimisation
- STO: 5-15% improvement in open rates. Per-subscriber timing.
- Platforms: Klaviyo (Smart Send Time, ML per individual), Seventh Sense (deepest analysis), ActiveCampaign (per-contact), Mailchimp (audience-level only).
- Doesn't help for: time-sensitive content, lists under 1K, transactional emails.
- General: 4-6am sends → top of inbox at wake. Tue/Thu best for B2B. Weekends can work for B2C.

---

## 9. ANALYTICS & MEASUREMENT

### KPIs by Campaign Type

| Type | Primary KPI | Target |
|---|---|---|
| Welcome series | Conversion rate, RPR | 2.5x baseline |
| Abandoned cart | Recovery rate, RPR | $3+ RPR (top 10%) |
| Promotional | Revenue, CTR | 2-5% CTR |
| Nurture | Engagement, Lead-to-customer | >20% open, >12% CTOR (B2B) |
| Transactional | Delivery rate, Speed | 99%+, <60s |
| Re-engagement | Reactivation rate | 5-10% |
| Cold email | Positive reply rate | 3-5% positive replies |
| Newsletter | Open rate, CTR, Growth rate | >40% open, >5% CTR |

### Attribution Models
- **Last-click:** Default, undervalues email. Inflates brand search.
- **U-shaped (position-based):** 40/40/20. Best starting point for most businesses.
- **Time-decay:** 7-day half-life. Best for longer sales cycles.
- **Data-driven (GA4):** Most accurate. Needs 300-400+ monthly conversions.
- **Incrementality testing:** Gold standard. Holdout 5-10%, compare purchase rates.

### Subscriber LTV
- LTV = avg revenue per subscriber per month × avg active months.
- Segment LTV by acquisition source (organic search vs paid social — can differ 2-3x).
- LTV:CAC ratio should be > 3:1. Below = spending too much. Above 5:1 = under-investing in growth.

### Email Revenue Tracking
- Use UTM parameters on every link: utm_source, utm_medium, utm_campaign, utm_content.
- ESP attribution > GA attribution (ESPs use generous windows). True revenue sits between.
- Well-optimised ecommerce: email should drive 25-40% of total revenue. Below 20% = room to improve.

---

## 10. COMPLIANCE

### Regulation Summary

| Regulation | Consent Required? | Key Rules | Penalty |
|---|---|---|---|
| **CAN-SPAM (US)** | No prior consent needed | Accurate headers, physical address, honour opt-outs in 10 days | $51,744/email |
| **GDPR (EU)** | Yes, freely given + specific + informed | Right to erasure (30 days), data minimisation, consent records 3-7 years | 4% global turnover or €20M |
| **CASL (Canada)** | Express or implied (implied expires) | Purchase: 2-year consent. Inquiry: 6-month. Express = indefinite | $10M CAD/violation |
| **CCPA (California)** | N/A (data rights law) | Right to know, delete, opt-out of sale. Sensitive data protections | $2,500-7,500/violation |
| **Spam Act (Australia)** | Yes (express or inferred) | Consent + sender ID + functional unsubscribe (5 biz days) | $2.22M AUD/day |

### Cold Email Compliance by Jurisdiction
- **US:** B2B cold email legal without consent. Must include opt-out + physical address.
- **UK:** B2B permitted under soft opt-in if relevant to professional role.
- **EU:** Varies by country. Germany strictest (opt-in required). France, Italy more permissive for B2B.
- **Canada:** Consent required. No cold email without prior relationship.
- **Australia:** Consent required. Cold email to purchased lists is illegal.

### One-Click Unsubscribe (RFC 8058)
- Required by Google/Yahoo for bulk senders (5K+/day).
- List-Unsubscribe + List-Unsubscribe-Post headers. Honour within 2 days.
- Most ESPs handle automatically. Verify by checking email headers.

---

## 11. INDUSTRY PLAYBOOKS

### Ecommerce DTC
- Email should drive 25-40% of total revenue. Split ~evenly between flows and campaigns.
- Core three flows: welcome (8% conversion target), abandoned cart ($3+ RPR), post-purchase.
- Engagement-based sending: most engaged get 3-4 campaigns/week, least engaged get 1/week max.
- RFM segmentation essential. Year-in-review emails (Spotify Wrapped model): 2-3x engagement.

### SaaS B2B
- Behaviour-based onboarding > time-based sequences. Trigger by what user has/hasn't done.
- One CTA per email. Feature adoption emails after onboarding reduce churn.
- Segment by company size + industry + product interest.
- Targets: >20% open rate, >12% CTOR. Study: Linear, Notion, Figma.

### SaaS B2C
- 5% retention increase = 25-95% profit increase. Email = retention channel.
- Duolingo streak model: cue → routine → reward.
- Re-engagement at 7 days inactive (not 30). Usage-based emails: 3-4x better than calendar-based.

### Newsletter/Creator
- 122% ROI. Inflection point: 10K subscribers (meaningful ad revenue).
- Minimum viable newsletter: 25K subs, 40% open, 3 sponsors/issue, $35 CPM = $150-200K/year.
- Revenue stack: sponsorships → paid subscriptions → affiliates → digital products → events.
- Referral programmes grow 30-40% faster. SparkLoop: $1-3/subscriber.
- Daily = stronger habits, faster burnout. Weekly = more sustainable.

### Agency
- Track metrics per client vertical. Quarterly strategy reviews.
- Build testing calendar per client: one subject line, one send time, one content test/month minimum.
- Document results in shared knowledge base across all clients.

### Nonprofit
- 3:1 ratio: three value emails per donation ask.
- Mission-driven storytelling. Make supporter the hero. Specificity creates connection.
- Separate cancelled donations from payment failures (different responses).
- End-of-year: start November, not December.

### Other Industries (key tactics)
- **Healthcare:** HIPAA non-negotiable. Separate clinical from marketing. 8th-grade reading level.
- **Financial:** Build compliance review into production timeline. Pre-approved content modules.
- **Real Estate:** Leads contacted within 5 min are 21x more likely to convert.
- **Travel:** Map email to traveller journey (inspiration → booking → pre-trip → in-stay → post-trip). Pre-arrival upsell emails 3-5 days before: +$20-50/booking.
- **Education:** Consolidate departmental sends. Text-only from individuals > branded HTML.
- **Retail:** Birthday emails: +25% opens, +40% clicks. Loyalty: progress visibility, personalised offers.
- **Events:** Start at registration, not week before. Follow up within 7 days post-event.
- **B2B Manufacturing:** Reorder triggers at ~day 80 of 90-day cycle: +15-25% reorder rate.
- **Restaurant:** Loyalty patrons order 3x more. "We haven't seen you" trigger at 2x avg visit interval.
- **Fitness:** Get first class within 7 days (50%+ more likely to retain at 6 months). Milestone celebrations.
- **Media:** 1-3-1 structure. First ad placement: 60-70% of total ad engagement. Segment by content interest.
- **Marketplace:** Two-sided strategy (buyers + sellers). Transactional emails near-instant. Weekly seller performance summaries = most opened.

---

## 12. CHOOSING YOUR PLATFORM

### Decision Factors (ranked)
1. **Deliverability** (85% vs 95% inbox placement = huge revenue difference)
2. **Automation capabilities** (event-triggered, conditional branching, A/B within flows)
3. **Segmentation depth** (behavioural + engagement + custom properties combined)
4. **Integrations** (native quality, API, webhooks)
5. **Pricing model** (subscriber-based vs volume-based vs value-based)

### Platform Comparison

| Platform | Best For | Starting Price | Key Strength |
|---|---|---|---|
| Klaviyo | Ecommerce (Shopify) | Free (250 contacts) | Deep ecommerce data, predictive analytics |
| Mailchimp | Small businesses | Free (500 contacts) | Ease of use, AI features |
| ActiveCampaign | Automation-heavy | $15/mo | 135+ triggers and actions |
| HubSpot | B2B, inbound | Free (2K emails/mo) | CRM integration, full suite |
| Kit (ConvertKit) | Creators | Free (10K subscribers) | Creator-focused, simplicity |
| Brevo | Multi-channel | Free (300 emails/day) | Email + SMS + chat, volume pricing |
| beehiiv | Newsletters | Free (2.5K subscribers) | Growth tools, ad network |
| Loops | SaaS, PLG | Free (1K contacts) | Product email focus |
| Postmark | Transactional | Free (100 emails/mo) | 99%+ delivery, sub-1s |
| Bento | Dev-first, AI | $30/mo | Tanuki AI agent, MCP server |

### Budget Guide
- **Under 500 subs:** Any free tier. Platform barely matters. Just start.
- **500-5K:** Brevo ~$25/mo, MailerLite ~$10/mo, Kit free tier.
- **5K-25K:** Klaviyo $60-150/mo (ecommerce), ActiveCampaign $49/mo (automation), Kit $49/mo (creators).
- Choose for where you'll be in 12 months, not today. Migration at 25K with 15 automations is a project.

### Migration Process (4-8 weeks typical)
1. Export everything (subscribers, engagement data, flows, templates, suppression list)
2. Set up authentication on new platform (SPF, DKIM, DMARC)
3. Rebuild core automations first (welcome, cart, post-purchase)
4. Send from new platform to most engaged segment only
5. Gradually migrate remaining segments over 2-4 weeks
6. Monitor deliverability daily during transition
7. Keep old platform as fallback for 30 days

---

## 13. COLD EMAIL

### When Appropriate
- B2B sales outreach to business contacts at work email only.
- NOT for: consumer marketing, mass outreach to purchased lists, no connection to recipient's role.
- LinkedIn screenshot test: if you'd be embarrassed seeing your email posted publicly, rewrite it.

### Infrastructure (critical — get this wrong and everything suffers)
- **NEVER send from primary domain.** Complaints damage all email (marketing, transactional, business).
- Buy 3-5 separate domains (variations: getbrand.com, trybrand.com). $10-15/domain/year.
- Google Workspace or M365 on each domain. 2-3 mailboxes per domain.
- Configure SPF, DKIM, DMARC on every domain.
- Warm each inbox 2-4 weeks before sending.
- Limit: 10-30 emails per inbox per day.
- Use dedicated cold email tool (NOT marketing ESP — they'll ban you).

### Cold Email Tools

| Tool | Best For | Key Feature |
|---|---|---|
| Apollo.io | All-in-one | 275M+ contact database |
| Instantly.ai | Scale | Largest warmup network, unlimited accounts |
| Lemlist | Personalisation | Custom images, LinkedIn multi-channel |
| Clay | Data enrichment | 75+ data sources, AI personalisation |

### Writing Cold Emails
- **Optimal length: 50-125 words.** Over 200 = significantly lower reply rates.
- Structure: personalised opening (1 sentence showing research) → problem/observation (1-2 sentences) → value prop focused on outcome (1 sentence) → soft CTA ("Worth exploring?").
- No attachments. Zero/minimal links. Plain text only. No HTML.
- Don't start with "My name is...". Don't use HTML templates.
- Interest-based CTAs: 2-3x more replies than meeting requests.

### Personalisation Levels
| Level | Research/email | Reply Rate | Scale |
|---|---|---|---|
| Hyper-personalised | 5+ min | 15-25% | 20-30/day |
| Semi-personalised | 1-2 min | 8-15% | 50-100/day |
| Segmented | Template per segment | 3-8% | 100s/day |
| Pure mail merge | Name + company only | 1-3% | Effectively dead |

Clay workflow: prospect list → enrich via 75+ sources → AI-generate personalised first lines → export to sending tool. Level 2 quality at Level 3 scale.

### Follow-Up Sequence
| Email | Timing | Purpose |
|---|---|---|
| 1 | Day 1 | Initial outreach |
| 2 | Day 3-4 | New value or different angle |
| 3 | Day 7-10 | Social proof or different use case |
| 4 | Day 14-17 | Breakup (2-3x reply rate of mid-sequence) |

Each follow-up MUST add new value. "Just checking in" = worst follow-up opener. Keep follow-ups shorter than original.

### Benchmarks
- Average reply: 1-5%. Good: 5-10%. Excellent: 10-20%.
- Positive reply rate: 30-50% of total replies.
- Best days: Tue/Wed/Thu. Best time: 8-10am recipient timezone.
- Multichannel (email + LinkedIn): 2-3x outperform either alone.

---

## 14. AI & EMAIL

### Where AI Excels Now
- **Subject lines:** Generate 50 variations in seconds. 80% comparable or better than human. 10% of time investment.
- **Send time optimisation:** Per-subscriber ML models. 10-25% open rate improvement.
- **Segmentation:** Engagement clusters, churn predictors, purchase propensity. Klaviyo predictive analytics: CLV, churn risk, next order date.
- **Content personalisation at scale:** Dynamic blocks powered by AI recs.
- **First drafts:** Solves blank page problem. 70% of the way there with good prompt + brand voice examples.
- **Analytics/pattern recognition:** Anomaly detection, trend identification, proactive issue flagging.

### Where AI Falls Short
- **Brand voice consistency:** Generic AI copy detectable. Needs heavy editing.
- **Strategic thinking:** Can't decide whether to send promotional or value email this week.
- **Emotional nuance:** Different emotional registers for different situations.
- **Creative breakthroughs:** AI optimises within patterns, doesn't make creative leaps.

### Human-AI Workflow
1. Brief AI with context (voice guidelines, audience, goals, examples of winning emails)
2. Generate first draft
3. Edit heavily for brand voice
4. A/B test against human-written versions
5. Feed results back — winning emails become examples for future prompts

### Practical AI Integration (ordered by impact)
1. Subject line generation (50 options → pick best 2-3 → A/B test)
2. First drafts of email sequences (especially standard flows)
3. Predictive analytics for churn risk and CLV (if ESP offers it)
4. Send time optimisation (enable in ESP)
5. AI-powered customer segmentation

### MCP & AI-Native Email
- Anthropic's Model Context Protocol: AI directly interacts with email platforms through natural language.
- Bento Tanuki AI (Jan 2026): first true AI marketing agent for email automations. Build flows via conversation.
- Shift from "build campaigns" → "approve recommendations".
- AI handles optimisation (what, when, who). Humans handle strategy (why, voice, ethics, direction).

---

## 15. CASE STUDY PATTERNS

### Key Patterns from 10 Companies
- **Casper:** Brand voice as competitive moat. "Come back to bed" cart email. Consistency across every touchpoint.
- **Morning Brew:** Referral programme drove 30% of acquisition. Format consistency builds daily habit. $50M+ revenue from newsletter sponsorships.
- **Duolingo:** Loss aversion for retention. Escalating urgency sequence (happy → concerned → sad → heartbroken owl). Breakup email = highest reactivation.
- **Spotify Wrapped:** Personal data + shareability + identity reinforcement. 461% increase in tweets. 21% app download spike.
- **Booking.com:** Real-time data makes urgency credible. But cautionary tale on crossing persuasion → manipulation line.
- **Amazon:** Every transactional email = revenue opportunity. Recommendation engine: 35% of revenue. Replenishment reminders based on consumption rates.
- **Patagonia:** Mission before product. "Don't Buy This Jacket" paradoxically drives loyalty. Sustainability storytelling must be backed by real action.
- **Nike:** Personalise by identity/activity, not just purchase history. "You're a runner" > "You bought running shoes."
- **Starbucks:** Simple loyalty mechanics. Progress visibility. Goal gradient effect. 50% of US revenue from 30M+ rewards members.
- **Basecamp/Hey:** Anti-tracking philosophy. Focus on clicks not opens. Respect for privacy and strong email marketing aren't mutually exclusive.

---

## APPENDIX: BENCHMARKS

### By Industry

| Industry | Avg Open Rate | Avg CTR | Avg Unsub Rate |
|---|---|---|---|
| Ecommerce | 15-20% | 2-3% | 0.2% |
| SaaS/Tech | 20-25% | 2-3% | 0.2% |
| Financial | 20-25% | 2.5-3.5% | 0.15% |
| Healthcare | 20-25% | 2-3% | 0.15% |
| Education | 25-30% | 3-4% | 0.1% |
| Nonprofit | 25-30% | 2.5-3.5% | 0.1% |
| Media/Publishing | 20-25% | 4-5% | 0.1% |
| Real Estate | 20-25% | 2-3% | 0.2% |
| Travel | 18-22% | 2-3% | 0.2% |
| Retail | 15-20% | 2-3% | 0.2% |

### By Email Type

| Type | Open Rate | CTR | Revenue Impact |
|---|---|---|---|
| Welcome | 50-60% | 5-8% | Sets tone for relationship |
| Abandoned Cart | 40-50% | 5-10% | Highest direct RPE |
| Post-Purchase | 40-50% | 3-5% | Drives repeat purchase |
| Transactional | 60-80% | 5-15% | Highest opens |
| Promotional | 15-20% | 2-3% | Bulk of revenue |
| Newsletter | 20-30% | 3-5% | Engagement + brand |
| Win-Back | 10-15% | 1-2% | Low rate, high value/conversion |

### ROI by Channel

| Channel | Avg ROI |
|---|---|
| Email | $36-42 per $1 |
| SMS | $20-25 per $1 |
| SEO | $15-20 per $1 |
| Content Marketing | $10-15 per $1 |
| Social (Paid) | $2-5 per $1 |
| PPC | $2-8 per $1 |

### Key Thresholds

| Metric | Healthy | Warning | Critical |
|---|---|---|---|
| Bounce Rate | < 2% | 2-5% | > 5% |
| Complaint Rate | < 0.05% | 0.05-0.1% | > 0.1% |
| Unsub Rate | < 0.3% | 0.3-0.5% | > 0.5% |
| List Growth | > 2%/mo | 0-2% | Negative |
| CTOR | > 10% | 5-10% | < 5% |

### Email Frequency Guide

| Industry | Recommended | Notes |
|---|---|---|
| Ecommerce DTC | 3-5x/week | Revenue scales with frequency. Test ceiling. |
| SaaS B2B | 1-2x/week | Quality > quantity. Each must justify itself. |
| SaaS B2C | 2-3x/week | Mix product updates + educational value. |
| Newsletter | Daily to 3x/week | Only daily if quality sustains. |
| Nonprofit | 1-2x/month | Donor fatigue risk. Space donation asks. |
| Retail | 3-5x/week | Promotional intensity expected. |
| Events | Ramp to 3-5x/week pre-event | Daily final week is normal. |

---

## EXPERT DIRECTORY (40 practitioners)

**Strategy:** Chad S. White (Oracle) | Kath Pay (Holistic Email Marketing) | Jay Schwedelson (SubjectLine.com, GURU Conference) | Jeanne Jennings (Email Optimization Shop) | Dela Quist (Alchemy Worx) | Ann Handley (MarketingProfs) | Ryan Phelan (RPEOrigin)

**Platform Builders:** Nathan Barry (Kit) | Tyler Denk (beehiiv) | Jimmy Kim (Sendlane) | Brennan Dunn (RightMessage)

**Copywriting:** Joanna Wiebe (Copyhackers) | Laura Belgray (Talking Shrimp) | Ben Settle (Email Players) | Chris Orzechowski (Orzy Media) | Samar Owais (Emails Done Right) | Tarzan Kay

**Deliverability:** Matthew Vernhout (Netcore Cloud) | Troy Ericson (EmailDeliverability.com) | Lauren Meyer (SocketLabs)

**Design/Technical:** Mark Robbins (Customer.io) | Paul Airy (Beyond the Envelope) | Justin Khoo (FreshInbox) | Jason Rodriguez (GitHub)

**Ecommerce/Retention:** Chase Dimond (Structured Agency) | Val Geisler (Fix My Churn) | Reinis Krumins (agencyJR) | Danavir Sarria (SupplyDrop)

**Agency:** Scott Cohen (InboxArmy) | Garin Hobbs (InboxArmy)

**Newsletter Growth:** Dan Oshinsky (Inbox Collective) | Matt McGarry (GrowLetter) | Liz Wilcox

**Consultants:** Ian Brodie | Jordie van Rijn (Emailmonday) | Eman Ismail | Andrew Kordek (iPost)

**Content Creators:** Alex Cattoni (Copy Posse) | Noah Kagan (AppSumo) | Gavin Laugenie (Dotdigital)
