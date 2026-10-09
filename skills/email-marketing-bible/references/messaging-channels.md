# Messaging channels: WhatsApp, SMS and RCS

Read this when: WhatsApp, SMS, RCS or cross-channel consent.
Last checked: 9 Oct 2026
Gather first: channel, consent basis, region.

Broad sends on any channel go through the core §0 gate. Channel consent is separate from email consent.

## WhatsApp Business

- **Measurement.** WhatsApp reports a read status when a message is shown in an open chat, which is not an email open; ignore the folklore "98% open rate" and judge on delivered-and-billed plus your own link clicks and orders [primary] https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status
- **Cost.** Billed per delivered message since 1 Jul 2025 (category × country × volume tier; live-fetch rates). From 1 Oct 2026 only two lanes are free: the first 1,000 service messages a month per business number, and the Free Entry Point window (up to 7 days) that opens when you answer a Click-to-WhatsApp ad conversation inside the 24h service window. Utility replies inside the service window are charged again [primary] https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
- **Where it pays.** Meta does not deliver marketing templates to US phone numbers, defined as a +1 dialling code with a US area code, so Canadian +1 numbers fall outside the block [primary] https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits. BSPs date the pause from 1 Apr 2025 [vendor]. European rates run above SMS. So it pays through the free lanes, CTWA conversations and WhatsApp-default markets (India, Brazil, LATAM, MENA), never as a cheaper blast.
- **Opted-in ≠ delivered.** Meta caps marketing templates per user (the cap is unpublished); error **131049** means too much marketing to this person: wait 24h, never fast-retry.
- **Consent and region.** Opt-in is mandatory. Geo-branch hard: US utility and authentication only; EU means GDPR; India's rules differ from SMS DLT.
- **AI chatbots.** Scoped business agents are fine. Meta's policy of 15 Oct 2025 barred general-purpose third-party AI chatbots from the Business API from 15 Jan 2026; Meta re-admitted them for a fee on 4 Mar 2026, and on 9 Jun 2026 the European Commission ordered free access restored in the EEA while its antitrust case runs [primary] https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1276. Re-verify before building one.

## SMS (US)

- TCPA requires prior express *written* consent for marketing ($500-$1,500 per message). Sending window 8am-9pm recipient local time. **10DLC** brand and campaign registration is necessary, not sufficient: content, SHAFT categories, links and volume are still filtered. CTIA STOP/HELP. Confirm by jurisdiction. The FCC's broader "revoke consent by any reasonable means" rules are changing; check the current status before relying on a date.
- SMS is the time-sensitive nudge (cart, back-in-stock, last chance) as a step inside high-intent email flows, never a duplicate broadcast. Judge SMS conversion by message type against the bands below, not the folklore 21-30%.
- Benchmarks as bands, not averages (Postscript 2026, 17,000+ Shopify stores, 2025 data, 25th to 75th percentile) [vendor] https://postscript.io/sms-benchmarks: campaign click 2.87-8.01% and conversion 0.12-0.54%; abandoned cart click 9.53-17.28%, conversion 3.97-7.84%, revenue per message $3.52-$10.95; back-in-stock click 36.71-58.70%; campaign unsubscribe 0.33-0.88%.

## RCS

Testable in the US with mandatory SMS fallback; reach depends on carrier and provider provisioning. RBM (brand-sent) lacks person-to-person RCS's end-to-end encryption, so never claim it. Launch: agent vetting, reach check, fallback copy, rich-card degradation, opt-out handling, one measurement scheme across RCS and fallback.

## Unified consent

Per channel and category, read before any send. SMS and WhatsApp need explicit prior opt-in; email's floor in some regions is opt-out; consent never travels across channels. Sending windows, frequency caps and suppression apply per channel. Regulators enforce this: Australia's ACMA treated marketing sent to customers who had opted out of one channel as sent without consent (TAB, Jul 2026; compliance.md) [primary].
