# Measurement

Read this when: reporting, attribution, open or click questions, an open-rate drop, A/B test design, or AI optimisation.
Last checked: 9 Oct 2026
Gather first: provider split, date range, denominators.

No benchmark here is a gate; the core §0 blocks are the only gates, and the numbers that trigger actions are in thresholds.md.

## Contents

1. Open truth
2. Scanner clicks
3. Gmail open-drop diagnostic
4. Analytics hygiene
5. KPIs by type
6. Attribution
7. AI optimisation and decisioning
8. Testing rules
9. Testing AI-assisted email

## 1. Open truth

Opens are unreliable in both directions.

- **Apple Mail Privacy Protection inflates them.** It pre-loads pixels. Brevo publishes both: marketing email averaged 20.7% opens without MPP against 33.9% with it [vendor] https://www.brevo.com/resources/brevo-marketing-benchmark/. Apple accounted for about 62% of tracked opens in July 2026 (Litmus; MPP-inflated, not a share of people) [vendor] https://www.litmus.com/email-client-market-share
- **Gmail cut them.** Validity's engagement data shows Gmail image loading, including tracking pixels, fell by roughly a third in late November 2025; some of its customers saw Gmail opens fall 30% or more in a quarter while clicks held [vendor] https://www.validity.com/blog/whats-really-behind-gmails-open-rate-drop-and-what-to-do-about-it/. In one Badsender case, a client's Gmail opens fell by more than half between campaigns while clicks stayed stable [practitioner] https://www.badsender.com/en/2026/05/19/prefetch-gmail-impact-open-rate/
- **Summaries are unproven either way.** Whether AI summaries fire pixels is not established. The "45.6% opens, CTR 4.35% to 3.93%" pair is Omeda's Q2 2025 platform data (2.03 billion publisher emails), with the AI link only guessed at [trade] https://mediacat.uk/ai-summaries-are-affecting-email-clicks-according-to-study/; don't cite it as summary evidence.
- **Consent can remove them.** In France, open tracking for measurement needs pixel consent (compliance.md). Where that applies, run any open-based test only inside the opted-in group, read it there, and decide on clicks, because people who agree to tracking select themselves (EMB policy). Jay Schwedelson argues the consented group still supports directional tests (Jul 2026) [practitioner] https://www.linkedin.com/posts/schwedelson_whats-up-this-week-open-rate-tracking-activity-7480253939079270400-ROPK
- **Rules.** Never award lead-score points or trigger high-stakes branches (sunsets, resends, suppression) on opens. Label open-only reads low-confidence. Never compare opens across ESPs. A subscriber who opens everything may be a machine, so don't treat them as a best reader without a click or reply [directional].

## 2. Scanner clicks

Clicks on every link within seconds of delivery, with no open, are a security scanner until proven otherwise. Filter them before engagement tiers, sunsets or A/B winners. Omeda labelled 88.9% of recorded clicks as bots in media and B2B publisher mail in Q2 2026 (not ecommerce) [vendor] https://www.omeda.com/resources/report/email-engagement-report-for-q2-2026/. Before trusting an "engaged" segment or attributed revenue, confirm MPP opens and bot clicks are excluded from it (a 2026 agency audit found both inflating attributed revenue and skewing segments) [practitioner] https://www.youtube.com/watch?v=p0xNL2axCB8

## 3. Gmail open-drop diagnostic

Run this before anyone "fixes" deliverability.

1. **Gmail-only open drop, clicks flat:** most likely a measurement change. Confirm with a seed placement test and Postmaster v2, then re-baseline on clicks and pause open-based sunsets and "resend to non-openers".
2. **Gmail opens and clicks both falling, or a 0.00% Postmaster spam rate beside collapsing Gmail opens:** likely filtering. Confirm with seed placement and the bounce logs (deliverability.md), then cut to recent engagers. Causes can overlap, so treat each branch as a hypothesis to test, not a verdict.
3. **Unsubscribes clustered by time or user agent, with no content change:** suspect bulk or agent-driven unsubscribes and check that before rewriting copy. Gmail's Manage subscriptions view unsubscribes in batches (deliverability.md), and one practitioner reports that nearly every personal agent he tried offered to unsubscribe him almost at once [directional] https://www.linkedin.com/posts/davidroberteagan_ai-agents-are-about-to-quietly-break-one-activity-7513644720682635265-Ao0Q. Agent deletions leave no unsubscribe at all: in The Verge's hands-on, Muse deleted thousands of promotional emails for a tester [trade] https://carney.co/daily-carnage/insights/meta-muse-what-the-new-ai-agent-means-for-marketers/, and Siri can delete by sender, so also watch clicks by provider. Offer "fewer" and "snooze" first in the preference centre: senders who added a snooze option cut unsubscribes by 82% (Oracle, undated, reported by Guy Hanson of Validity) [vendor] https://www.litmus.com/blog/we-want-your-email-preference-new-approach-to-opting-in
4. **Unsubscribes up after a bad week elsewhere:** join unsubscribes to order, delivery, return and support events from the prior 14 days before blaming content or frequency (the window is EMB policy; the idea is Kath Pay's, Aug 2026) [practitioner] https://holisticemailacademy.com/2026/08/18/your-unsubscribes-may-not-be-an-email-problem

## 4. Analytics hygiene

- Split every rate by mailbox provider before reading it.
- Small samples are "unknown", not good or bad. Count by cohort, not by calendar.
- A proportion over 100% (opens, clicks or bounces per recipient) is a counting bug. Disaffection rate is a ratio to clicks and can exceed 100%.
- Label each figure as measured, user-provided or benchmark.
- Never compute a rate from a paged MCP sample; ActiveCampaign's own plugin tells agents the same [primary] https://github.com/ActiveCampaign/activecampaign-plugin/blob/main/commands/audience-health.md. Every number an agent quotes comes with its query, filters and count.
- Ask your data through MCP instead of building dashboards; use AI for anomaly flags and A/B readouts. Give the agent a fixed brief (date range, metric definitions, campaign ids, sample sizes): an open question gets a confident story about your own dashboard (r/shopify and r/Emailmarketing threads, Sep 2026) [directional] https://www.reddit.com/r/shopify/comments/1wbih4o/whats_the_best_email_marketing_mcp_use_case_youve/
- Reply rate can include one-tap assisted replies (Gmail Suggested Replies, iOS 27 Smart Reply) [directional]. Still a strong signal; label it when you benchmark it.

## 5. KPIs by type

| Type | Judge on | Reference |
|---|---|---|
| Welcome | Conversion and revenue per recipient (RPR) | Klaviyo Oct 2026: welcome email RPR $5.75 average, $13.27 top 10% [vendor] |
| Abandoned cart | Recovery and RPR | Klaviyo Oct 2026: $6.77 average, $13.70 top 10% [vendor] |
| Promotional campaign | Revenue and click rate | Klaviyo 2026 campaigns: about 1.7% average to 3.4% top 10% click [vendor] |
| Nurture | Clicks and conversion | No open-based KPIs |
| Cold | Positive reply rate | 3-5% [directional] |
| Newsletter | Clicks and replies | Paid retention where it applies |

Sources: https://www.klaviyo.com/blog/abandoned-cart-benchmarks ; https://www.klaviyo.com/uk/blog/email-marketing-benchmarks-open-click-and-conversion-rates. More in benchmarks.md.

## 6. Attribution

- Start with U-shaped attribution: 40% to the first touch, 40% to the last, 20% across the middle (EMB policy). Incrementality is the gold standard.
- The cleanest public holdout in email: Dubé and Xu ran three RCTs on Wine Access's twice-daily newsletter (27,500 customers). The first held 500 customers out of the tested emails for two weeks, and the human, AI and hybrid arms each roughly doubled gross profit from orders against them [primary] https://link.springer.com/article/10.1007/s11129-025-09303-9. Copy the design: a randomised group that gets none of the emails being tested.
- Give agent-originated orders (agent checkout, shopping agents) their own attribution channel [directional].

## 7. AI optimisation and decisioning

Where "AI optimisation" means bandits or decisioning reallocating live traffic:

- Measure with holdouts, never last-touch credit.
- Set do-not-optimise constraints up front: margin, fatigue, complaints, brand safety.
- Set a frequency ceiling at or below today's volume, a complaint ceiling that pauses an arm, and a margin floor.
- Prove every ESP AI feature before trusting it: a 30-day off period or a holdout (Send It! podcast, Jul 2026) [practitioner] https://www.youtube.com/watch?v=7S1tUExRVhw. Mailchimp's claim that AI-feature emails had a 50% higher order rate compares self-selected users, so it shows why a holdout matters, not what AI is worth [vendor] https://mailchimp.com/newsroom/peak-season-marketing-insights/
- Ryo Lu argues that copying whatever measures well, now frictionless with AI, pulls work towards the mean ("convergence to the mean", 3 Oct 2026) [practitioner] https://ryo.lu/journal/convergence-to-the-mean. An optimiser that only exploits winners does the same. Reserve a share of sends for genuinely new directions (design.md) and judge them on clicks and revenue, not only against the incumbent.

## 8. Testing rules

- Decide the sample size before you start.
- Never peek and stop at the first significant result, or use a sequential test built for peeking. In Evan Miller's worked example, checking after every observation and stopping at the first 5% result produced false positives 26.1% of the time [primary] https://www.evanmiller.org/how-not-to-run-an-ab-test.html
- Pick winners on clicks or conversions, never opens.
- On lists under about 10K, test big swings only: sender name, offer, format.
- Highest-value tests: sender name (it compounds), CTA format, template structure. Test flows over campaigns.

Recipients needed per arm (two-sided alpha 0.05, power 0.8, two-proportion test; arithmetic, not a source):

| Baseline | Lift to detect | Per arm |
|---|---|---|
| 2% click rate | 20% (to 2.4%) | about 21,100 |
| 2% click rate | 10% (to 2.2%) | about 80,700 |
| 4% click rate | 20% (to 4.8%) | about 10,300 |
| 0.5% conversion | 10% (to 0.55%) | about 328,000 |

## 9. Testing AI-assisted email

- Guard against homogenisation: test AI-assisted email explicitly on reply rate and Primary-tab placement, never opens. In one small newsletter's test, opens held on AI-drafted issues while replies fell by about half [directional] https://www.reddit.com/r/Newsletters/comments/1wum71w/i_let_ai_draft_my_last_three_issues_my_open_rate/
- The Mirror Test: feed the model a clean, high-intent customer signal. Generic output points to the model or prompt; good output that falls apart on production data points to the data (Chad S. White, CMSWire, 7 Oct 2026; he works at Zeta Global and credits the idea to Zeta's Neej Gore) [practitioner] https://www.cmswire.com/digital-marketing/is-your-email-program-scaling-bad-data-or-bad-strategy
