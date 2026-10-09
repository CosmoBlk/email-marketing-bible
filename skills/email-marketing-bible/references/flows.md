# Flows

Read this when: building, editing, pausing, resuming or auditing any automation.
Last checked: 9 Oct 2026
Gather first: model, trigger, audience, offer, exclusions.

Going live on a flow is a send: the core §4 checklist runs first and the core §0 gate applies.

## Flows before campaigns

Flows earn about 18x campaign revenue per recipient and 13x the placed-order rate (Klaviyo 2026) [vendor] https://www.klaviyo.com/products/email-marketing/benchmarks. Omnisend's 2025 data has automations at 2% of email sends and 30% of email-driven revenue [vendor] https://www.omnisend.com/resources/reports/2026-ecommerce-marketing-report/. Build the flows before polishing campaigns.

Build in this order (you specify trigger → wait → condition → send; the agent scaffolds; you review):

Welcome → Abandoned cart → Browse abandonment → Post-purchase → Win-back → Cross-sell → VIP → Sunset → Birthday → Replenishment → Back-in-stock → Price drop.

## Recipes

- **Welcome (4-6):** promise + reply ask + one segmenting question → brand story → social proof → best content by answer → soft sell → expectations. Welcome email RPR $5.75 average, $13.27 top 10% (Klaviyo, 2 Oct 2026) [vendor].
- **Abandoned cart (3):** reminder, no discount (1-4h) → objections: reviews, shipping, guarantee (24h) → small incentive if margins allow, first-timers only (48h). Cart email RPR $6.77 average, $13.70 top 10% (Klaviyo, 2 Oct 2026) [vendor] https://www.klaviyo.com/blog/abandoned-cart-benchmarks
- **Post-purchase:** confirm → shipping → satisfaction check → review → cross-sell → replenishment. Don't send a discount to someone who just paid full price for the same thing (after Kath Pay, Aug 2026) [practitioner].
- **Transactional detail in live text.** Order number, merchant, items, total, dates and tracking go in plain text, never only in an image, so the customer, Apple Mail, Siri and inbox agents can all read them [trade] https://emailexpert.com/what-ios-27-changes-in-apple-mail-for-senders/. Amazon cut item names from order emails from July 2026, and shoppers said the vague emails looked like phishing (The Verge, 11 Aug 2026) [trade] https://www.theverge.com/ai-artificial-intelligence/977733/amazon-order-emails-google-gmail-ai-agents-data. If you remove detail on purpose, keep the order number, a recognisable sender, the item count and the total.
- **Win-back (60-90d inactive):** "we miss you" → value offer → breakup (highest reply) → confirm + resubscribe.
- **BFCM:** build the list (Sep-Oct) → warm volume (Oct-early Nov) → tease (2-3 weeks out) → daily sends, engaged first → post-BFCM thanks, cross-sell, shipping deadline. For 2026: Adobe forecasts US online holiday spend of $275.1B for 1 Nov to 31 Dec, with October alone at $95.8B [primary] https://news.adobe.com/news/2026/09/adobe-us-holiday-shopping-season-to-hit-record; half of Q4 campaign volume went out before Cyber Week in 2025 (Attentive) [vendor] https://www.attentive.com/blog/bfcm-message-sending-guide; keep discounts shallow and tiered (in BFCM 2025, Klaviyo found brands with the smallest discounts grew fastest) [vendor] https://www.klaviyo.com/newsroom/bfcm-holiday-shopping. Offer a "fewer emails" or snooze option before the ramp. Don't quote Salesforce's "$334B, 22% via AI agents" as 2026 data (it was a 2025 forecast), or "AI visitors spend 43% more per visit" (not in Adobe's release).
- **Consistency beats perfection:** a 20-minute weekly (Liz Wilcox) or 2-3 short sends a week beat one polished monthly (Ian Brodie) [directional].

## Lifecycle safety rules

Plain best practice. These are the flow mistakes that cause the worst sends: duplicates, backlog bursts, stale senders, the wrong people in a sequence.

1. **Activating, resuming or editing a live flow is a send.** Run the core checklist and get approval (core §0) first, and never activate on a shared or unverified domain.
2. **Narrow triggers.** Use "added to list X" or "event Y", never "any new contact". Say whether existing and imported contacts enrol, and check enrolment counts after any import or sync.
3. **Before resuming a paused flow,** inspect the queue, choose whether in-flight journeys stop or continue, stagger any release, and re-check time-sensitive copy. Resuming is a send (rule 1).
4. **Edits may not reach live flows.** Changing a template, sender, domain or brand kit may not update the flows that use it: list every live flow that uses it, republish (a send, rule 1), and confirm the next send with a seed test.
5. **Exits and content.** Every flow declares its exit conditions and re-checks them at each step. Every node has content before activation. Read the built flow back as a numbered list before asking for approval.

Also:
- Find an existing flow by name or id and edit it; don't make a duplicate.
- A test send is not a flow test. Trigger the flow end to end with a seed contact only, in the ESP's test mode or a copy whose entry filter admits only seed addresses, so no real contact enrols.
- Check every live flow's status and revenue weekly; an automated optimiser can switch a flow off without anyone noticing for weeks (Send It! podcast, Jul 2026) [practitioner] https://www.youtube.com/watch?v=7S1tUExRVhw
- Audit live flows at least quarterly (EMB policy) for overlapping triggers and duplicate steps; Klaviyo's own Composer demo flags abandoned cart against abandoned checkout [vendor] https://www.youtube.com/watch?v=rQGuK1k9TmY
- Ship an agent-proposed flow change to a small split first, with a holdout (measurement.md).

## Watch

Price-drop and back-in-stock flows now compete with free platform agents: Google's Universal Cart (19 May 2026) tracks price drops and back-in-stock for shoppers in the background, rolling out in the US with Gmail to follow [primary] https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/. Your flow has to add what the cart agent can't (a member price, a bundle, early access), at the same price the agent sees [directional]. Agent checkout adds new abandonment triggers (agent-ops.md).
