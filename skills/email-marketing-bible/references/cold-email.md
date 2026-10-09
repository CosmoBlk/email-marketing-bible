# Cold email

Read this when: cold outbound, B2B prospecting, sequences or cold infrastructure.
Last checked: 9 Oct 2026
Gather first: offer, ICP, domains, volume.

Legal line first: check jurisdiction, recipient type and basis before any cold send. Germany needs prior consent for B2B email, Canada and Australia require consent, and a platform's acceptable-use policy is not a legal basis (compliance.md). Cold contacts never move into a marketing list or newsletter without opting in. Sends to more than one person still go through the core §0 gate.

## Infrastructure

- Never your primary domain. Separate domains, warmed for 2-4 weeks by real sending, 10-30 a day per inbox [directional], and a dedicated cold tool kept legally and technically apart from marketing.
- **No warming networks or inbox-exchange services.** Validity's Heatwave blocklist (3 Sep 2026) targets synthetic warming and cold outreach, and Validity says mailbox providers and security vendors use it [vendor] https://www.prnewswire.com/news-releases/validity-launches-heatwave-blocklist-to-combat-unethical-cold-email-practices-and-synthetic-domain-warming-302868287.html
- **Secondary domains may not shield the primary** once a blocklist links them (Laura Atkins, "Gambling with cold email", 17 Sep 2026) [practitioner] https://www.wordtothewise.com/2026/09/gambling-with-cold-email/. SURBL appears to be escalating listings to corporate domains [directional].
- **Speed of setup is not a deliverability plan.** One operator had Claude Code stand up 1,000 inboxes across look-alike domains in minutes, mostly on .info; a blocklist then listed .info domains en masse and the backups were on .info too (Aaron Shepherd, Jul 2026) [practitioner] https://www.youtube.com/watch?v=RQg5jgraVg8. Spread across TLDs, and fix targeting first: his narrowest list performed best.
- Re-verify enriched or provider-supplied addresses before the first send; don't trust the provider's own check [practitioner] https://www.youtube.com/watch?v=mD7JpNHLT70

## Writing

- 50-125 words. Personalised opening → observation → value → soft interest-based CTA (2-3x the replies of a meeting ask) [directional].
- Persona-level copy with one verifiable proof point is a strong default [practitioner] https://x.com/coldemailchris/status/2097421665621705132. Scraped "loved your recent post" openers now read as bot-written (Richard Illingworth, Aug 2026) [practitioner] https://x.com/RCIllingworth/status/2086890412174692863
- Put most of the effort into email one: 58% of replies come from the first step (Instantly Cold Email Benchmark Report 2026) [vendor] https://instantly.ai/cold-email-benchmark-report-2026
- With AI: personalise the offer line, not a fake-familiar opener; restrict claims to a fixed list of what the offer really includes; allow a blank output where nothing fits; QA a sample of every batch; score positive replies divided by sent (GrowthEngineX's open-source outbound skills, Aug 2026) [practitioner] https://github.com/growthenginenowoslawski/coldoutboundskills
- Every personal fact in an AI-written email needs a source the agent can show. A wrong fact costs more than none (Hunter Walk, 24 Sep 2026) [practitioner] https://hunterwalk.com/2026/09/24/i-used-to-respond-to-every-cold-email-but-now-ai-slop-is-killing-my-inbox/
- Receivers now filter the 2026 cold pattern itself: lookalike burner domains, reply-only opt-outs with no link, and invented familiarity (r/sysadmin, Aug 2026) [practitioner] https://www.reddit.com/r/sysadmin/comments/1vttcps/i_finally_figured_out_why_my_spam_looks_different/. Send from a real, branded secondary domain with a working unsubscribe link and an honest reason for writing.
- Models follow prompt rules literally and have no tact with bad news: one opened with a prospect's layoffs. Write rules as the outcome you want, add an explicit rule for sensitive signals (never mention layoffs or bad press), and keep a human pass before send (r/salesdevelopment, Jul 2026) [practitioner] https://www.reddit.com/r/salesdevelopment/comments/1uxhlaa/hope_this_helps_someone_cold_email_rules_for/
- Recipients can now auto-label AI-written mail and route it to spam (copy.md). Unedited AI copy is a placement risk, first in cold and one-to-one email.

## Follow-up

4 emails over 2-3 weeks, each adding value; the breakup gets 2-3x the reply rate [directional].

## AI in outbound and agent senders

- Prospecting and personalisation (2-3x reply vs templates) [directional] plus reply handling, under the same domain, suppression and consent guardrails. Founder-led 1:1 from a real inbox still beats cold blast on B2B reply and deliverability.
- **Before an agent emails strangers,** it needs four controls (EMB policy): a stop or unsubscribe path, one suppression list shared across every agent, per-recipient caps, and a do-not-contact check. Recipients are already pushing back on agent-sent floods (Arvind Narayanan, Sep 2026) [practitioner] https://x.com/random_walker/status/2099104048620122430
- **Agent-sent cold email is still commercial email:** an unsubscribe link and physical address in every message, a named human who owns the programme behind any agent persona, and a stop at the first no. An agent network's pitches went out with no unsubscribe link until the press noticed (Tedium, 11 Sep 2026) [trade] https://tedium.co/2026/09/11/ilands-agents-email-spam-kaixin-tang/
- **A person approves the outreach list in batches.** An agent allowed to email anyone it chose reported contacting about 2,000 people over four months, with 45 ongoing replies (Science, 2 Oct 2026; the agent's own figures) [trade] https://www.science.org/content/article/exclusive-ai-agent-emailed-hundreds-researchers-help-it-told-us-why. Disclose AI authorship in the first lines, not only in the signature; an agent writing to people must not pass as human (compliance.md).
