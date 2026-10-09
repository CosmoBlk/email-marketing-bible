# Deliverability

Read this when: spam placement, bounces, complaints, a Gmail or Outlook rejection, a domain or DNS change, warm-up, or switching ESPs.
Last checked: 9 Oct 2026
Gather first: domain, ESP, bounce and complaint rate, recent changes.

The core §0 gate still applies: no broad send while any block holds. Every number that triggers an action is in thresholds.md.

## Contents

1. Authentication
2. DNS change protocol for agents
3. 2026 sender tooling
4. Reputation and separation
5. Diagnosis path
6. The AI-era inbox
7. Warm-up
8. Switching-ESP runbook

## 1. Authentication

Gmail requires SPF and DKIM for bulk senders, plus DMARC (p=none is enough) aligned through either SPF or DKIM [primary] https://support.google.com/mail/answer/81126. Settings beyond that are EMB policy unless marked.

- **SPF.** On domains that send, end with `~all`, as Google's own setup does, and let DMARC decide: `-all` can get mail rejected at SMTP before DMARC runs, even when DKIM would pass, and those messages never reach aggregate reports (RFC 9989) [primary] https://knowledge.workspace.google.com/admin/security/set-up-spf ; https://www.rfc-editor.org/rfc/rfc9989.txt. Keep `-all` for domains that never send. Stay inside the 10-DNS-lookup limit and publish one SPF record per name: more than one is a permanent error [primary] https://datatracker.ietf.org/doc/html/rfc7208#section-3.2
- **DKIM.** Gmail needs keys of 1024 bits or longer and recommends 2048 [primary] (same Google page). Use 2048-bit keys aligned with the From domain, and rotate them yearly (EMB policy).
- **DMARC.** Gmail, Yahoo and Outlook accept p=none as the floor, with alignment [primary] https://support.google.com/a/answer/81126. Outlook.com rejects mail from domains sending more than 5,000 a day that fail SPF, DKIM or aligned DMARC, with `550 5.7.515` [primary] https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730. EMB policy: on sending subdomains, move to quarantine, then reject, once aggregate reports show every legitimate sender aligned and DKIM-signed. On a domain where people send everyday mail and may post to mailing lists, stop at quarantine: RFC 9989 says such domains should not publish p=reject (section 7.4).
- **DMARCbis.** RFC 9989 (May 2026) obsoletes RFC 7489. `pct=` is gone, so test a policy with `t=y`, which applies one level below the stated policy; `np` (policy for non-existent subdomains, from RFC 9091) and `psd` are now core tags; a DNS tree walk replaces the Public Suffix List. Correctly configured records need no change [primary] https://www.rfc-editor.org/info/rfc9989. Any ramp written as `pct=10`, `pct=25` is out of date.
- **BIMI.** Gmail accepts a VMC (registered trademark, shows the checkmark) or a CMC (no trademark needed, but the certificate authority requires prior public use of the logo, typically 12 months [vendor] https://www.valimail.com/blog/google-cmc-bimi-announcement/; no checkmark) [primary] https://knowledge.workspace.google.com/admin/security/set-up-bimi. It needs DMARC at enforcement, not in testing mode. Check a mailbox provider's current certificate support before promising a logo there.
- **Non-sending domains.** Lock down every domain that never sends: a null MX (RFC 7505) [primary] https://datatracker.ietf.org/doc/html/rfc7505, `v=spf1 -all`, DMARC `p=reject` and an empty wildcard DKIM record. One real estate team that put 364 parked domains on DMARC reporting found 79 of them being spoofed within a month (r/sysadmin, Oct 2026) [practitioner] https://www.reddit.com/r/sysadmin/comments/1wz4ql2/i_connected_364_parked_domains_to_dmarc_and_79/. Most company domains still don't enforce DMARC: 68.4% of 67,336 domains tracked by CipherCue had no record or sat at p=none (Jul 2026) [vendor, not a representative sample] https://ciphercue.com/blog/dmarc-enforcement-gap-rua-fragmentation-2026

## 2. DNS change protocol for agents

Agents now change DNS for owners who aren't technical, and the damage lands on the owner's own inbox. Follow this every time.

1. **Ask who controls DNS first.** If it isn't the person in the chat, draft the records as an email to the owner, with hosts written the way their registrar expects (some want `_dmarc`, some want `_dmarc.example.com`).
2. **Put the ESP on a subdomain** (for example `mail.example.com` or `news.example.com`). Never edit apex MX.
3. **One SPF record per name and exactly one DMARC record at `_dmarc`: replace, never add.** Under RFC 9989, if a name returns more than one DMARC record, all of them are discarded and the receiver keeps walking up the DNS tree, so your intended policy is ignored and a parent or public-suffix policy may apply instead (section 4.10) [primary] https://www.rfc-editor.org/rfc/rfc9989.txt. A subdomain's own DMARC record wins over the organisational domain's. Check for a CNAME at `_dmarc` before adding a TXT record: Cloudflare accepted both at once, which silently dropped the intended policy while the vendor portal still showed p=reject. DMARC reports going quiet is the tell (r/sysadmin, Aug 2026) [practitioner] https://www.reddit.com/r/sysadmin/comments/1vud8av/cloudflare_dns_allows_two_dmarc_cname_txt_to/
4. **Never weaken DMARC to pass a tool's check.**
5. **Diff any one-click wizard against the existing records before accepting it.** Wizards delete and overwrite.
6. **Before any new tool sends as your domain, align it** (an SPF include or its own DKIM key) and test to an outside mailbox. With more domains at p=reject, unaligned mail is now refused outright, and corporate gateways can block it even after the recipient allowlists you (r/sysadmin, Aug and Sep 2026) [practitioner] https://www.reddit.com/r/sysadmin/comments/1vxkzwy/how_are_companies_not_using_spfdkimdmarc/
7. **After any change or DNS-host move, re-verify every record** (read them live, for example `dig TXT _dmarc.example.com`) and test inbound mail from an outside account.
8. **Never remove records on a screenshot diagnosis.** Read the live records first.
9. **"Delivered but missing" on a B2B test:** check the recipient's Microsoft 365 quarantine [primary] https://learn.microsoft.com/en-us/defender-office-365/quarantine-about

## 3. 2026 sender tooling

- **Gmail Postmaster Tools v2.** Read compliance status, spam rate and the deliverability verdict. The v1 domain and IP reputation dashboards are being retired; Google's FAQ still calls the timing "postponed" [primary] https://support.google.com/mail/answer/16594218, while Al Iverson reports v1 access being removed domain by domain [practitioner] https://www.spamresource.com/2026/08/gpt-v1-retirement-and-important-updates.html. So never tell anyone to check a Gmail "domain reputation" score. The verdict values are USER_FEEDBACK_POSITIVE, MESSAGE_VOLUME_LOW, SENDER_NOT_COMPLIANT, SMTP_ERRORS_HIGH, USER_FEEDBACK_NEGATIVE, USER_FEEDBACK_LOW and SPAM_RATE_HIGH [primary] https://developers.google.com/workspace/gmail/postmaster/reference/rest/v2/domains/getComplianceStatus. Actions are in thresholds.md.
- **Gmail enforcement.** No new sender requirement in 2026, but since November 2025 Gmail has been ramping up enforcement on non-compliant bulk traffic, with temporary and permanent rejections [primary] https://support.google.com/mail/answer/14229414. The rules: SPF, DKIM, aligned DMARC, RFC 8058 one-click unsubscribe for marketing, and spam rate kept under 0.3% [primary] https://support.google.com/mail/answer/81126.
- **Deferrals and mailbox full.** On a Gmail 421 deferral, follow Google's protocol (thresholds.md) and never fast-retry [primary] https://support.google.com/mail/answer/15256272. A 552 mailbox-full bounce at Gmail is often the shared 15GB quota across Gmail, Drive and Photos, not the inbox: pause 7-14 days, then suppress if it keeps bouncing [practitioner] https://www.spamresource.com/2026/08/mailbox-full-not-always-inbox-problem.html
- **Display names.** No fake "Re:" or "Fwd:", no display names that imply an existing thread, no emoji that imitate verification badges [primary] https://support.google.com/mail/answer/15256272
- **Microsoft.** SNDS moved to a new portal, and network access now lapses 10 months after approval unless reattested, so a complaint feed can stop for an admin reason [primary] https://substrate.office.com/ip-domain-management-snds/snds. Trade press reports that JMRP complaint reports went header-only with the complainant redacted, and that trap counts left SNDS (emailexpert, Jul 2026) [trade] https://emailexpert.com/microsoft-microsoft-snds-trap-hit-data-removedremoves-trap-hit-data-as-snds-and-jmrp-changes-disrupt-complaint-workflows/. Prove that a seed complaint from Outlook still reaches suppression.
- **Yahoo.** The 2024 rules stand: SPF, DKIM, DMARC p=none minimum with alignment, one-click unsubscribe honoured within 2 days, complaints under 0.3% [primary] https://senders.yahooinc.com/best-practices/
- **Send packets.** A broad-send packet carries Postmaster compliance status and spam rate where readable (core §0).

## 4. Reputation and separation

- Domain matters more than IP at Gmail [directional]. Dedicated IPs only with steady volume (thresholds.md).
- Marketing and transactional on separate subdomains by default (core §0). Volume changes the urgency, not the rule.
- Engagement is a primary signal: auto-sunset the chronically unengaged.
- "Low bounce" ≠ "safe": consent and engagement signals can suspend an account at 0.1% bounce [directional].
- Zero bounces is not proof someone is there. Gmail users can now change their address, and the old one keeps receiving [primary] https://support.google.com/accounts/answer/19870. Sunset on engagement, not on bounces.
- Agent inboxes on shared vendor domains and personal Gmail are for one-to-one mail only, never a marketing identity: the From domain can't align with your DMARC, you inherit the shared domain's reputation [directional], and consumer Gmail errors above about 500 emails a day [primary] https://support.google.com/mail/answer/22839. From January 2027 Gmail also stops supporting "Send as" for third-party addresses (Google's examples are Yahoo and Outlook; check whether your domain set-up is affected) [primary] https://support.google.com/mail/answer/22370

## 5. Diagnosis path

symptom → auth → blocklists → Postmaster v2 compliance status, spam rate and verdict → bounce logs → sending patterns → content → test → fix the root cause → monitor for 2-4 weeks.

- **Gmail open drop?** Run the open-drop diagnostic in measurement.md before touching deliverability. A Gmail-only open drop with flat clicks is usually measurement, not placement.
- **"Delivered" is not "inboxed".** The DMA's 2026 benchmarking puts the delivered rate at 99.2%, while Validity, its sponsor, puts global inbox placement near 87% [vendor] https://www.validity.com/blog/the-2026-dma-email-benchmark-report-what-the-numbers-really-mean-for-revenue/
- **Warm-up scores measure warm-up mail, not campaigns.** A mailbox can score 99 while its campaigns land in spam; confirm with a seed placement test before launch and monthly (Michel Lieben, ColdIQ, Sep 2026) [practitioner] https://x.com/MichLieben/status/2095919072907272404
- **Invisible characters.** Strip Unicode tag characters (the U+E0000 block) and stray zero-width characters from copy before send. Microsoft saw a phishing campaign hide them inside trigger words; it tells filter builders to treat them as a strong anomaly signal, and ActiveCampaign already flags heavy use. The England, Scotland and Wales flag emoji are built from the same characters, so exempt them [primary] https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/
- **Complaint loops must close.** After any provider format change, prove a complaint from each mailbox provider maps to a contact and lands in suppression.
- **Hidden text** is now an attack signature (copy.md). Keep only a short preheader.

## 6. The AI-era inbox

- **What's documented.** Gmail's AI Inbox reads the Primary tab only (US, English, paid tiers, beta) [primary] https://support.google.com/mail/answer/16845247. Promotions has a "most relevant" sort, and engagement is one input Google names [primary] https://blog.google/products-and-platforms/products/gmail/one-stop-purchase-tracking-in-gmail/. No provider documents a summary window or a penalty for AI-written text, so don't claim one.
- **Not every reader has the AI layer.** Turning Gmail's smart features off removes the Primary, Social and Promotions tabs and the summary cards [primary] https://support.google.com/mail/answer/15604322, and smart features are off by default in the EEA, the UK, Japan and Switzerland [primary] https://support.google.com/mail/answer/15195630. Consumer videos telling Gmail users to switch them off drew big audiences from Jul to Sep 2026 (one had 1.5M views by October) [directional] https://www.youtube.com/watch?v=bHPbynWyW_Q. Write so the email works with and without the AI layer, and never attribute a tab or summary effect to a whole Gmail segment.
- **Injection filtering.** Gemini leaves suspected prompt-injection mail out of its summaries [primary] https://knowledge.workspace.google.com/admin/security/how-google-helps-protect-gemini-users-from-malicious-content-and-prompt-injections?hl=en
- **Bulk exits.** Readers now cull senders in batches: Gmail's Manage subscriptions view [primary] https://x.com/gmail/status/2080357642099454213, Siri in iOS 27 deleting every email from a named sender on request (an opt-in beta: English, iPhone 15 Pro or later, not in the EU) [trade] https://emailexpert.com/what-ios-27-changes-in-apple-mail-for-senders/, and personal agents that offer to unsubscribe [directional]. One-click unsubscribe must work with no login and no extra step, or the exit becomes a complaint.
- **Autonomous sends.** The core §0 gates, plus hard volume caps on AI-triggered flows, engagement-tier targeting even when an agent composes, and the spam rate surfaced to the agent before it sends.

## 7. Warm-up

- Engaged-first, staggered; keep warming alongside live sends. Pacing examples [directional]: a new sending identity from about 20 to 80 a day over 2 weeks; a new domain from about 300 to 10K a day over about 14 days.
- Warming a new identity is a different job from spreading new contacts across a warm one.
- Warm-up means real sending to people who want the mail. Never a warming network or inbox-exchange service: Validity's Heatwave blocklist (3 Sep 2026) targets synthetic warming [vendor] https://www.prnewswire.com/news-releases/validity-launches-heatwave-blocklist-to-combat-unethical-cold-email-practices-and-synthetic-domain-warming-302868287.html
- The ramp rule and its stop conditions are in thresholds.md.

## 8. Switching-ESP runbook

Generic pacing; read the new ESP's own limits before any send.

1. **Inventory through the old ESP's API:** lists, tags, fields, flows with their triggers and waits, templates, events, suppressions by reason, last-click dates.
2. **Import suppressions first.** Pull opt-out state (unsubscribed, bounced, complained) from the old ESP's API or a full suppression export, never a subscriber CSV, which drops them.
3. **Prune** automations with no entrants in about 90 days. Don't pay to move the dead.
4. **Verify** anything not mailed in about 90 days with an SMTP-level verifier (EMB rule of thumb), because an old "deliverable" result isn't proof. Send valid addresses first, engaged-first. Verification status is separate from consent: hold unknown and catch-all addresses back, and mail them last, in small batches, only where consent is on record. Suppress invalid ones. An LLM read or a free scrub is not verification. Chrome's Email Verification Protocol proves ownership of an address, not consent [primary] https://developer.chrome.com/blog/email-verification-protocol-origin-trial. Zero bounces is not proof someone is there (section 4). Contacts with consent on record but dormant for about six months get one re-permission email; non-responders are sunset (thresholds.md).
5. **Recreate flows as drafts**, then dual-send events to prove each trigger fires.
6. **First send and ramp.** Start with a small batch of the most engaged, inside the new ESP's own limits, then apply the ramp rule and stop conditions in thresholds.md. On a small list, verify and send in two or three batches over a day.
7. **Cut over flow by flow, transactional last.** Sync unsubscribes both ways during the overlap. Keep the old account read-only for 30 days.

Public enforcement context: Amazon SES puts an account under review at a 5% bounce rate or a 0.1% complaint rate, and may pause sending at 10% or 0.5% [primary] https://docs.aws.amazon.com/ses/latest/dg/faqs-enforcement.html; Google's deferral protocol (thresholds.md) [primary].
