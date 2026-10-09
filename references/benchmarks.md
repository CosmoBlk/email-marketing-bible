# Benchmarks

Read this when: someone asks for a benchmark or wants to compare performance.
Last checked: 9 Oct 2026
Gather first: industry, email type, platform, region.

Every row carries a source, a label and a date. Nothing here is a gate: the core §0 blocks are the only gates, and action thresholds live in thresholds.md. A benchmark is a starting hypothesis; the account's own data wins.

**Quoting rules.** Name the dataset, period and audience. Say whether bots and Apple MPP are filtered. Vendor data describes that vendor's customers, not the market. Opens are left out of this file on purpose (measurement.md).

## Campaign click and placed-order rates

| Dataset | Segment | Click rate | Placed-order rate | Label |
|---|---|---|---|---|
| Klaviyo 2026 (183,000+ customers) | All campaigns | 1.69% average; 3.38% top 10% | 0.16% average; 0.36% top 10% | [vendor] |
| Klaviyo 2026 | Electronics | 1.85% | | [vendor] |
| Klaviyo 2026 | Sporting goods | 1.88% | | [vendor] |
| Klaviyo 2026 | Home and garden | 1.78% | | [vendor] |
| Klaviyo 2026 | Food and beverage | 1.70% | | [vendor] |
| Klaviyo 2026 | Jewellery | 1.60% | | [vendor] |
| Klaviyo 2026 | Health and beauty | 1.24% | | [vendor] |
| MailerLite (medians, 3.6M campaigns, Dec 2024 to Nov 2025) | All | 2.09% | | [vendor] |
| MailerLite | Ecommerce | 1.07% | | [vendor] |
| MailerLite | Non-profit | 2.90% | | [vendor] |
| MailerLite | Higher education | 2.15% | | [vendor] |
| MailerLite | Software and web apps | 1.15% | | [vendor] |
| MailerLite | Media | 4.10% | | [vendor] |
| MailerLite | Publishing | 2.82% | | [vendor] |
| Brevo 2026 (2025 data) | Marketing email, all industries | 2.27% average; 5.22% top 10% | | [vendor] |
| Omeda Q2 2026 (media and B2B publishers) | Bot-filtered unique clicks | 1.04% | | [vendor] |
| DMA UK 2026 benchmarking (six ESPs) | Retail; travel | 1.0%; 1.2% | | [vendor, via sponsor Validity's write-up] |

Sources: https://www.klaviyo.com/uk/blog/email-marketing-benchmarks-open-click-and-conversion-rates ; https://www.mailerlite.com/blog/compare-your-email-performance-metrics-industry-benchmarks ; https://www.brevo.com/resources/brevo-marketing-benchmark/ ; https://www.omeda.com/resources/report/email-engagement-report-for-q2-2026/ ; https://www.validity.com/blog/the-2026-dma-email-benchmark-report-what-the-numbers-really-mean-for-revenue/

MailerLite's median unsubscribe rate rose to 0.22% (from 0.08%), which it puts down to Gmail making unsubscribing easier [vendor].

## Flows by type

Klaviyo Abandoned Cart Benchmark Report, 2 Oct 2026, 110,000+ customers, email [vendor] https://www.klaviyo.com/blog/abandoned-cart-benchmarks

| Flow | RPR average | RPR top 10% | Click average | Click top 10% |
|---|---|---|---|---|
| Welcome series | $5.75 | $13.27 | 6.5% | 13.3% |
| Browse abandonment | $2.08 | $4.32 | 5.6% | 9.8% |
| Abandoned cart | $6.77 | $13.70 | 6.0% | 11.3% |
| Post-purchase | $1.80 | $2.77 | 5.1% | 10.5% |
| Win-back | $0.82 | $1.60 | 2.8% | 5.8% |

All flows (Klaviyo 2026): click 5.58% average (10.48% top 10%), placed-order rate 2.11% (4.3%); flows earn about 18x campaign revenue per recipient and 13x the placed-order rate [vendor] https://www.klaviyo.com/products/email-marketing/benchmarks. Omnisend 2025: automations were 2% of email sends and 30% of email-driven revenue, earning 16x more per send than campaigns [vendor] https://www.omnisend.com/resources/reports/2026-ecommerce-marketing-report/

## ROI

- About £41 per £1, up from about £38 (DMA UK Marketer Email Tracker 2026: 250 UK marketers, self-reported, Mar 2026) [trade] https://www.dma.org.uk/resources/report/marketer-email-tracker-2026 ; figures via https://www.actionrocket.co/blog/dma-email-tracker-2026-key-takeaways-for-email-marketers
- $76 per $1 for email, $79 across email, SMS and push (Omnisend merchants, Omnisend's internal analysis) [vendor] https://www.omnisend.com/resources/reports/2026-ecommerce-marketing-report/

## Deliverability

- Validity 2026 (2025 seed data): inbox placement 87.2%, spam 6.1%, missing 6.6%. By provider: Gmail 89.8%, Yahoo 87.3%, Apple 82.0%, Microsoft 77.4%. Average complaint rate 0.06% [vendor] https://www.validity.com/wp-content/uploads/2026/03/2026-Benchmark-Report.pdf
- DMA UK 2026 (six ESPs): 99.2% delivered. Validity, the report's sponsor, puts inbox placement near 91% in the UK and 87% globally [vendor] https://www.validity.com/blog/the-2026-dma-email-benchmark-report-what-the-numbers-really-mean-for-revenue/
- DMARC enforcement: 68.4% of 67,336 company domains tracked by CipherCue had no DMARC record or sat at p=none (Jul 2026) [vendor, not a representative sample] https://ciphercue.com/blog/dmarc-enforcement-gap-rua-fragmentation-2026

## List decay

- About 1.1% of a freshly verified, opted-in list of 64,000 addresses changed status within 90 days, including 22 new spam-trap flags (the verifier's classifications; one list, Sep 2026) [practitioner] https://www.reddit.com/r/Emailmarketing/comments/1wdmifr/90_days_of_email/. It backs the rule to re-verify anything not mailed in about 90 days (deliverability.md).

## Measurement context

Details in measurement.md.

- Apple 62.26% of tracked opens, Gmail 27.03%, Outlook 5.83% (Litmus, Jul 2026; MPP opens count as Apple) [vendor] https://www.litmus.com/email-client-market-share
- Brevo opens without and with MPP: 20.73% against 33.87% for marketing email; 15.50% against 30.02% in ecommerce [vendor]
- Omeda Q2 2026: 88.9% of recorded clicks labelled bot-driven in media and B2B publisher mail [vendor]
- Validity: Gmail image loading fell by roughly a third in late Nov 2025 (Validity's engagement data); some customers' Gmail opens fell 30% or more in a quarter [vendor]

## SMS

Postscript 2026 percentile bands are in messaging-channels.md.

## Don't cite

- "45.6% opens, CTR 4.35% to 3.93%" as evidence about AI summaries: it is Omeda's Q2 2025 publisher data with the AI link guessed at.
- "$36 per $1" for email ROI: the source page is from 2022 and reports bands, not $36.
- Salesforce's "$334B, 22% via AI agents" as 2026 data: it was a 2025 forecast.
- "AI-referred visitors spend 43% more per visit": not in Adobe's release.
- Klaviyo "$1.94 vs $0.11" revenue per recipient for flows against campaigns: secondary sources only.
- Washington CEMA "$500 per email" as current exposure: new suits get $100 (compliance.md).
