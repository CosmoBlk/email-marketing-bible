# Thresholds

Read this when: any number decides an action (block, pause, ramp, sunset, frequency).
Last checked: 9 Oct 2026

This is the one place where numbers that drive actions live. A broad send is any send beyond people who clicked in the last 30 days; a recovery send goes only to them. Core §0 holds the send blocks: a complaint rate at or above 0.1% or a Gmail Postmaster spam-rate-high verdict blocks broad sends (recovery sends to recent clickers continue), and a Postmaster not-compliant verdict blocks every send until fixed. The stop conditions below (bounce, disaffection, deferral, mailbox full, ramp) pause sends as EMB policy; everything else is a starting hypothesis, labelled as such. Account data beats every benchmark in this file. Labels: [primary] official source, [vendor] vendor data, [trade] trade press, [practitioner] a named practitioner's field experience, [directional] anecdote or inference, EMB policy (this skill's own rule).

## The table

| Metric | Value | Action | Source | Label | Checked |
|---|---|---|---|---|---|
| Complaint rate | At or above 0.1% | Blocks broad sends (core §0). Recover: restrict to clicked-30d, inspect acquisition source and expectation mismatch, confirm unsubscribe visibility | Google asks bulk senders to stay under 0.1% and never reach 0.3%: https://support.google.com/mail/answer/81126 | EMB policy, in line with [primary] | 9 Oct 2026 |
| Complaint rate | 0.3% | Gmail's hard ceiling: Google says to avoid ever reaching it | https://support.google.com/mail/answer/81126 | [primary] | 9 Oct 2026 |
| Complaint rate, context | 0.06% average | A reference point, not a target | Validity 2026 Deliverability Benchmark: https://www.validity.com/wp-content/uploads/2026/03/2026-Benchmark-Report.pdf | [vendor] | 9 Oct 2026 |
| Complaint denominator | Mail delivered to providers that send feedback-loop reports | Gmail sends no per-complaint reports; it shows aggregate spam rates, by domain and by Feedback-ID, computed on inbox-delivered mail, so a rate blended over all mail understates the real one when Gmail is a big share of the list | https://support.google.com/a/answer/14668346 | EMB policy, mechanism [primary] | 9 Oct 2026 |
| Unsubscribe rate | Healthy under 0.3%; red flag above 0.5% | Above 0.5%: review frequency, list source and the promise made at signup | MailerLite median 0.22% (3.6M campaigns, Dec 2024 to Nov 2025): https://www.mailerlite.com/blog/compare-your-email-performance-metrics-industry-benchmarks | Bands EMB policy; median [vendor] | 9 Oct 2026 |
| Hard bounce rate | Healthy under 2%; at or above 2% on a send stops a ramp | Stop the ramp, read the bounce text, verify the source list before the next send | Amazon SES puts an account under review at a 5% bounce rate and may pause it at 10%, a public example of ESP enforcement: https://docs.aws.amazon.com/ses/latest/dg/faqs-enforcement.html | EMB policy; SES [primary] | 9 Oct 2026 |
| Disaffection rate | (unsubscribes + complaints + bounces) / clicks x 100 | 100% or more: stop broad sends and cut to recent engagers. 50% to 100%: review source and frequency. Example: 0.25% + 0.05% + 0.2% against a 1.5% click rate is 33%, so every three clicks cost one subscriber | Formula from Validity 2026, which calls a disaffection rate "larger than its click rate" a crisis | Formula [vendor]; the 100% and 50% lines are EMB policy | 9 Oct 2026 |
| Click rate, campaigns | 1.69% average; 3.38% top 10% | Below 1% on an engaged segment: investigate | Klaviyo 2026 benchmarks (183,000+ customers): https://www.klaviyo.com/uk/blog/email-marketing-benchmarks-open-click-and-conversion-rates | [vendor]; trigger EMB policy | 9 Oct 2026 |
| Click rate, flows | 5.58% average; 10.48% top 10% | Compare flows with flows, never with campaigns | Klaviyo 2026, as above | [vendor] | 9 Oct 2026 |
| Click rate, marketing email | 2.27% average; 5.22% top 10% | Context | Brevo Marketing Benchmark 2026: https://www.brevo.com/resources/brevo-marketing-benchmark/ | [vendor] | 9 Oct 2026 |
| Inbox placement | Global 87.2%; Gmail 89.8%; Yahoo 87.3%; Apple 82.0%; Microsoft 77.4% | Context; judge your own seeds and Postmaster data | Validity 2026, as above | [vendor] | 9 Oct 2026 |
| Postmaster v2: SENDER_NOT_COMPLIANT | Verdict | Block every send until every failing requirement on the Postmaster compliance dashboard is fixed (authentication, TLS, PTR records, message format, unsubscribe headers, spam rate) (core §0) | Verdict names: https://developers.google.com/workspace/gmail/postmaster/reference/rest/v2/domains/getComplianceStatus | Names [primary]; action EMB policy | 9 Oct 2026 |
| Postmaster v2: SPAM_RATE_HIGH | Verdict | Block broad sends (core §0); recover on clicked-30d as for complaints | Verdict names: https://developers.google.com/workspace/gmail/postmaster/reference/rest/v2/domains/getComplianceStatus | Names [primary]; action EMB policy | 9 Oct 2026 |
| Postmaster v2: USER_FEEDBACK_NEGATIVE | Verdict | Restrict to clicked-30d; audit acquisition sources | As above | EMB policy | 9 Oct 2026 |
| Postmaster v2: USER_FEEDBACK_LOW | Verdict | Start the sunset path for non-clickers | As above; mapping after Al Iverson: https://www.spamresource.com/2026/09/gpt-lets-talk-deliverability-analysis.html | EMB policy, [practitioner] | 9 Oct 2026 |
| Postmaster v2: SMTP_ERRORS_HIGH | Verdict | Stop and read the bounce text (often a volume jump or an infrastructure fault) | As above | EMB policy, [practitioner] | 9 Oct 2026 |
| Postmaster v2: MESSAGE_VOLUME_LOW | Verdict | Not a problem in itself; keep volume steady | As above | EMB policy, [practitioner] | 9 Oct 2026 |
| Gmail 421 deferral | Any | Pause 15 minutes, then send one test. Only if it delivers, hold below the volume that triggered the deferral for 24 hours, then raise 25-100% a day. Never fast-retry | Google, Top 10 Gmail sender issues: https://support.google.com/mail/answer/15256272 | [primary] | 9 Oct 2026 |
| Gmail 552 mailbox full | Any | Pause 7-14 days, then suppress if it keeps bouncing | Al Iverson: https://www.spamresource.com/2026/08/mailbox-full-not-always-inbox-problem.html | [practitioner] | 9 Oct 2026 |
| Engagement tiers | Last click 0-30 days: every send. 31-60 days: about 75% of sends. 61-90 days: best sends only. 91-180 days: re-engagement only. Over 180 days: sunset. New subscribers count from their signup date | Build tiers on bot-filtered clicks, never opens | EMB policy | EMB policy | 9 Oct 2026 |
| Ramp | Never more than double between sends | Grow only when the last send had hard bounces under 2%, complaints under 0.1% and clicks holding. Read limits from the ESP, never from plan names | EMB policy | EMB policy | 9 Oct 2026 |
| Seed tests | Up to five addresses, the human's own | Seeds count toward bounce and complaint budgets | EMB policy | EMB policy | 9 Oct 2026 |
| Subject length | About 45 characters before mobile truncation | Advisory only; judge subject lines on clicks | EMB policy | [directional] | 9 Oct 2026 |
| List growth | Positive net growth after hygiene; 2-5% a month as a starting hypothesis | Negative net growth: check acquisition and sunset rules | EMB policy | [directional] | 9 Oct 2026 |
| Dedicated IP | Only with steady volume around 1M+ a month | Below that, shared pools usually beat a cold dedicated IP | EMB policy | [directional] | 9 Oct 2026 |
| DMARC policy | Floor p=none at Gmail, Yahoo and Outlook | On sending subdomains, move to quarantine, then reject, after aggregate reports show every legitimate sender aligned and DKIM-signed. Domains where people send everyday mail and may post to mailing lists stop at quarantine (RFC 9989 section 7.4) | https://support.google.com/a/answer/81126 ; Microsoft: https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730 | Floor [primary]; ramp EMB policy | 9 Oct 2026 |

## Frequency: starting hypotheses

Frequency is a test, not a rule. Start here, then judge on revenue per email sent and on the unsubscribe and complaint deltas after each change.

| Programme | Starting frequency | Notes |
|---|---|---|
| Ecommerce DTC | 2-5 a week to engaged tiers | Less to lapsing tiers (engagement tiers above) |
| Retail | 2-5 a week | Loyalty and promo calendar drive it |
| Newsletter | As promised at signup, weekly to daily | The promise is the contract |
| SaaS B2B | 1-2 a week | Behaviour-triggered mail on top |
| Nonprofit | 1-2 a month plus appeals | Year-end campaign from November |

Context: in the DMA's 2026 survey of 250 UK marketers, about 14% of customers were reported to get four or more emails a week from one brand (Marketer Email Tracker 2026, recap by its sponsor Action Rocket: https://www.actionrocket.co/blog/dma-email-tracker-2026-key-takeaways-for-email-marketers) [trade].
