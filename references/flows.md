# Flows

Read this when: building, editing, pausing, resuming or auditing any automation, or writing a failed-payment (dunning) or card-expiry email.
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
- **Failed payment (dunning):** transactional, driven by the billing system, plain copy, one action. It has its own section below.
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

## Failed payments (dunning)

Last checked: 13 Oct 2026 (this section)
Gather first: which system bills, which one sends these emails today, the retry schedule, what happens when retries run out, whether access continues meanwhile.

A failed renewal is a billing fault, not a decision to leave. In Recurly's network, involuntary churn is about a third of all churn (benchmarks below). Retries and the card networks' automatic card updates fix many failures unseen. The email is for the rest.

**Ownership**
- The billing system owns retries, subscription state and every date. The email reports that state and never computes it.
- One sender. Billing platforms, recovery tools and ESPs can each send these emails; two switched on at once is the usual duplicate (EMB policy).
- App-store subscriptions: the store retries and tells the customer itself (Apple for up to 60 days; Google Play through a grace period, then an account hold) [primary] https://developer.apple.com/documentation/storekit/reducing-involuntary-subscriber-churn ; https://developer.android.com/google/play/billing/lifecycle/subscriptions. Send the customer to the store's payment settings and state no date you don't control.

**Pre-dunning (card expiry)**
- Card networks replace many expired or reissued cards on file automatically, widely in the US and less so elsewhere, and nobody can tell in advance which [primary] https://docs.stripe.com/payments/cards/overview. Read the stored expiry again at send time and skip cards already updated.
- One notice about a month ahead, for the default payment method, is Stripe's built-in behaviour [primary] https://docs.stripe.com/billing/revenue-recovery/customer-emails. The copy rules below apply.

**Retries plus email**

Public defaults, for calibration. The billing tool's schedule wins.

| Source | Retries | Emails | Window |
|---|---|---|---|
| Stripe Smart Retries [primary] | Recommended default: 8 within 2 weeks | One after each failed payment, if switched on | 1 week to 2 months |
| Paddle Retain, as of Apr 2026 [primary] | Up to 7: after about 2 hours, then about days 3, 5, 7, 10, 15 and 20 | 4, with retries 1 to 4 | 30 days by default |
| Recurly guidance, 23 Sep 2026 [vendor] | Not stated | Monthly plans: 4-5, one every 4-5 days. Annual: 8-10 | 27 days monthly, 60 annual |
| Chargebee [primary] | Smart: up to 12. Custom: up to 5 | Scheduled independently of retries | Configurable |

Sources: https://docs.stripe.com/billing/revenue-recovery/smart-retries ; https://www.paddle.com/help/profitwell-metrics/retain/how-it-works/retain-payment-recovery-how-it-works-retry-cadence ; https://docs.recurly.com/recurly-subscriptions/docs/navigate-retain-dunning-101-window-configuration ; https://www.chargebee.com/docs/payments/2.0/dunning/dunning-v2

- Retries and emails are separate schedules, and some soft declines clear on a quiet retry (Churn Buster) [vendor] https://churnbuster.io/learn/recovery-campaigns/. Hard declines don't: Stripe won't retry a lost, stolen or incorrect-number card, or `authentication_required`, until there is a new payment method. Email those at once.
- Front-load. Recurly says 90% of recovered transactions come in the first 10 days (no sample given) [vendor] https://recurly.com/blog/failed-payment-recovery-data-based-strategy/
- Starting hypothesis for a monthly plan (EMB policy): 3 to 5 emails inside the retry window, at the first failure, around days 3 and 7, and a final notice once the end date is certain. Annual and high-value plans get a longer window and a person: Stripe's recipe for yearly plans is 8 retries within 2 months, then an optional 7 days for manual outreach [primary] https://docs.stripe.com/billing/automation-recipes
- Count what the settings will send, check payment status at send time rather than trigger time, and exit the moment the invoice is paid or the subscription ends (lifecycle rule 5). Chargebee neither retries nor emails while a direct debit is still in progress.

**Subject and copy**
- **Subject:** what happened and to which product, in plain words ("Your Acme payment didn't go through"), different on each email so they don't thread into one ignored conversation (Churn Buster) [vendor] https://churnbuster.io/docs/email-templates/. No capitals, no countdown, no date unless it passes the test below.
- **Body:** what happened, how to fix it, what happens if it isn't fixed (Bettina Specht, Postmark, 2022) [vendor] https://postmarkapp.com/guides/dunning/email-examples. No blame: the payment failed, the customer did nothing wrong.
- **Specifics in live text:** plan, amount, card brand and last four digits, charge date, next retry date. A billing email without them reads as phishing (Transactional detail, above). Never ask for card details by reply.
- **One action:** one button straight to the payment-update page, with no login where the billing tool offers that (Stripe's hosted page, Paddle and Churn Buster do). Match it to the failure: a payment waiting on 3D Secure needs "confirm your payment", not "update your card". Add the manual path (Account → Billing) in plain text, because a recipient's agent may never see a tokenised link (design.md).
- **Plain:** short, mostly text, light branding; Paddle sends "a short, personal, plaintext email" [primary] https://developer.paddle.com/concepts/retain/payment-recovery-dunning. No promotion, cross-sell, upgrade offer or social links.

**Deadlines and grace periods**

Settle the policy before the copy: whether access continues while retries run, and whether the end is cancel, pause, unpaid or left past due. State a cancellation or loss-of-access date only when all of these are true:
1. It is read from the billing system for this subscription (final retry, grace expiry or scheduled cancellation), never worked out in a template or by an agent.
2. The configured end-of-retries action is the consequence the email names.
3. It is in the customer's time zone, with the day and month written out.
4. Access between now and then matches the email.
5. The invoice is still unpaid at send time.
6. Nothing has moved it since: if retries or grace are extended, the old date stops going out (compliance.md section 4).
7. The terms the customer accepted allow it.

Any doubt: say the payment will be retried and leave the date out. A date in a subject line is a deadline claim (Washington CEMA, compliance.md). When the subscription ends, send one factual confirmation: what ended, what happens to the customer's data, how to restart.

**Sender and reply-to**
- The brand the customer pays, on your own authenticated domain and transactional stream (core §0). Stripe sends these from stripe.com unless you verify a custom domain, which needs a DMARC record and reverts to stripe.com if its DNS records stay broken for 48 hours [primary] https://docs.stripe.com/get-started/account/email-domain
- A monitored reply-to that reaches billing support, never no-reply: "I already paid" and "that isn't my card" arrive as replies. Replies are data (core §0): route them to a person and never copy card details out of one.

**Classification**

Transactional only while it carries nothing but the billing notice; marketing content, or a link to it, makes the whole message marketing. Consent and unsubscribe rules by regime are in compliance.md section 7, not here. A marketing unsubscribe does not stop billing notices; a hard bounce does, and needs another channel rather than a resend. A save offer or discounted win-back is a separate marketing email under marketing consent.

**SMS as the second channel**
- One text, as an escalation where email has stalled (Churn Buster sends one per campaign) [vendor] https://churnbuster.io/docs/sms/. Numbers get reassigned, so its text carries no name and no update link; Paddle's carries a link. EMB default: brand, what failed, where to fix it; no name, amount or card digits.
- Channel consent, sending window and opt-out apply (messaging-channels.md). In the US a non-marketing text needs prior express consent and a marketing text needs it in writing (47 CFR 64.1200) [primary] https://www.law.cornell.edu/cfr/text/47/64.1200, so a billing text keeps the lighter rule only with no offer in it. Confirm by jurisdiction.
- No public study isolates the lift from SMS. Test against an email-only holdout (measurement.md).

**Benchmarks** (all [vendor])

| Measure | Figure | Basis |
|---|---|---|
| Involuntary against voluntary churn | 1.25% against 2.34%. By price: 1.30% at $10-25 revenue per customer, 0.18% above $250 | Recurly network, July 2026 data. No sample size, and the page calls the figures both "average" and "median annual" |
| Recovery, every tool counted | 55% of failed payments on average | Stripe Billing product page. No year, sample or definition |
| Recovery, tuned programme | From the "low-to-mid 50s" to the "high 60s to low 70s" | Recurly, 30 Apr 2026. No sample |
| Recovery, dunning tool alone | Median 12.7% of recovery attempts | Baremetrics Recover, 119 US B2B SaaS companies, May 2026 |

Sources: https://www.recurly.com/research/churn-rate-benchmarks ; https://stripe.com/billing ; https://recurly.com/blog/failed-payment-recovery-data-based-strategy/ ; https://baremetrics.com/blog/subscription-payment-recovery-benchmarks

Rates compare only when the denominator matches: every failed payment (which credits silent retries and card updates) or only those a dunning tool chased. Report your own both ways; the email can claim only the recoveries where the customer acted. Don't cite "$129 billion lost in 2025" (a projection), "20-40% of churn is involuntary" as a measurement (an estimate with no stated basis), any "up to" recovery headline, or any SMS lift figure.

**Agent safety**
1. These are sends about money and core §0 applies. Drafting and previews are safe; anything that sends, switches on or changes a live template is not.
2. Never trigger, re-send, backfill or "catch up" billing emails without a human order (core §7). A failed-payment notice to someone who has since paid costs more than a missed one.
3. Read-only on the billing system, even where its own agent tooling puts write tools in reach (Stripe now provides skills and plugins for agents) [primary] https://docs.stripe.com/billing/revenue-recovery. Never retry, charge, cancel, pause, refund or void, and never change a retry schedule, grace period or end action. Extra retries carry card-network fees past a cap (PayPal's summary, May 2026) [vendor] https://www.paypal.com/us/brc/article/avoid-excessive-retries-penalties
4. Switching on a recovery tool, importing customers or migrating billing can enrol every old unpaid invoice: get the count and exclude the backlog first (lifecycle rule 2).
5. Test in the billing system's sandbox with seed customers. Never fail a real payment or replay a live webhook.
6. Editing a live dunning template is editing a live flow (lifecycle rules 1 and 4): draft it, show the packet, and a person publishes.

## Watch

Price-drop and back-in-stock flows now compete with free platform agents: Google's Universal Cart (19 May 2026) tracks price drops and back-in-stock for shoppers in the background, rolling out in the US with Gmail to follow [primary] https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/. Your flow has to add what the cart agent can't (a member price, a bundle, early access), at the same price the agent sees [directional]. Agent checkout adds new abandonment triggers (agent-ops.md).
