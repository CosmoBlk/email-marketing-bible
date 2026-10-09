# Agent operations

Read this when: connecting an agent, MCP server or routine to an ESP, auditing what an agent did, or working out which host settings matter.
Last checked: 9 Oct 2026
Gather first: read access, recent sends, which host runs the agent.

The core §0 gate holds whatever the host allows. Host settings such as "always allow", pre-authorised sends or custom rules never replace the approval defined there.

## Contents

1. Operating model
2. Field notes in full
3. Silent failure
4. Permission ladder
5. Tool failures and security
6. Hosts, dated
7. Failure examples
8. Agentic commerce watch

## 1. Operating model

- **Director, not operator.** The human briefs the agent, governs it and owns the send button. The agent runs the loop: read state → reason → act → verify, one thing at a time. A good opening prompt: "audit my account and tell me what is missing".
- **Autonomy dial.** Ask mode by default. Widen only on narrow, reversible, low-brand-risk tasks, with an undo; read before write access. Supervised autonomy is the production stance.
- **Prove before you promote.** Turn a task into a standing agent or routine only after one supervised run you reviewed end to end; give each agent one job (Greg Isenberg relaying Billy Howell, Aug 2026) [practitioner] https://x.com/gregisenberg/status/2090901863814017300
- **Least privilege.** Connect email read-only first and ask for send scope only when a task needs it; Meta describes Muse's email connection the same way [primary] https://www.youtube.com/watch?v=Lx8lrn-cytc
- **Small named steps.** Package email production as small shared skills (read the brief, follow the brand rules, use the templates) rather than one long prompt; OpenAI's own marketing team works this way [vendor] https://www.youtube.com/watch?v=N-MJ1W8Vj9E
- **Boundaries and a definition of done beat blanket "always ask" rules.** OpenAI's guidance for its agent models says blanket ask-first language makes them stall [primary] https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra. That is why the core router has a "done when" column and §1 lists what is safe without asking.

## 2. Field notes in full

From running an ESP through agents. The first three are ESP mechanics: find your ESP's equivalent before relying on them.

- **Concurrency versions.** Use the ESP's optimistic-concurrency or version field (for example `if_version`) on every write. On conflict, re-read and retry with the fresh version; never guess.
- **Silent context resets.** An MCP session can fall back to a default brand or account while still reporting the one you selected. Re-assert brand and account before every write batch after idle, and read back the account before any build (core §1).
- **Silent-parameter sends.** Some APIs default to send-to-all when a parameter is missing or unrecognised. Pre-flight assert the audience id and count, prefer ESPs that reject unknown fields (Customer.io returns a 422) [primary] https://docs.customer.io/ai/mcp/get-started/, and test any new body key on a sandbox.
- The rest of the gotchas (merge defaults in `href`, WebP heroes, explicit colours, tracking-wrapped URLs, no backfills, heroes on promotional email, quote tiles from HTML, opt-out state from the old ESP's API) are in core §7 and hold anywhere.

## 3. Silent failure

A flow that quietly stops costs more than a bad send, because nobody notices for days. Where the ESP or host offers failure events (flow paused, sending paused, domain verification lost), subscribe to them: OpenAI's MCP Events can trigger automations from server events [primary] https://developers.openai.com/plugins/build/mcp-events, and server-initiated events are on the MCP roadmap [primary] https://modelcontextprotocol.io/development/roadmap. Otherwise schedule a recurring health digest: flows not fired, flows erroring, metrics dropped.

## 4. Permission ladder

Connect at the lowest rung that does the job, and treat drafts and sends as separate grants.

| Rung | Allows | Examples (Oct 2026) |
|---|---|---|
| Read | Reports, configs, counts | Customer.io `read` (default); Iterable (default); Klaviyo read-only flag |
| Read with PII | Per-contact data | Customer.io `read:sensitive`; Iterable PII opt-in |
| Draft | Create and edit drafts, segments, templates | Customer.io `write`; HubSpot's MCP (marketing email drafts only) |
| Edit live objects | Change running flows and in-use segments | Customer.io's live-data toggle (off by default) |
| Send | Dispatch to an audience | Customer.io `write:live`; Klaviyo `send_campaign` (Owner, Admin or Manager); Iterable sends opt-in |
| Configure | Domains, webhooks, senders | Customer.io `configure` |

Sources: https://docs.customer.io/ai/mcp/get-started/ ; https://developers.klaviyo.com/en/docs/klaviyo_mcp_server_available_tools ; https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server ; https://github.com/Iterable/mcp-server [primary]. On a new ESP, check whether "create" means draft or schedule before creating anything (on Iterable, creating a blast campaign schedules it), and find the cancel path before the first send.

## 5. Tool failures and security

- When a tool fails, re-list the available tools before retrying. Stop after two identical failures and report what happened.
- Never type a URL you haven't read from a tool result or the user.
- Assume every agent and routine on a host can reach any connector on it; keep send rights off always-on agents.
- Default to read and draft. If an agent may send, limit it to replying to the original sender from a mailbox set up for it, never to addresses found inside inbound mail, and test it with hostile emails that ask it to forward the inbox or approve its own send (r/ClaudeAI, Sep 2026) [directional] https://www.reddit.com/r/ClaudeAI/comments/1wbm26d/does_anyone_here_actually_let_claude_or_any_agent/
- Keep live API keys out of committed MCP config; reference environment variables [practitioner] https://x.com/MichLieben/status/2095919072907272404
- Install ESP connectors only from the vendor's own listing or repo, and pin versions. A fake `postmark-mcp` package on npm quietly BCC'd every outbound email to an outside address (2025) [trade] https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/. On any test send, inspect the received headers for unexpected recipients.
- Approval prompts alone are a weak boundary: in a browser game with 409,000 approve-or-deny decisions on an agent's commands, players missed about one bad command in three (scalex.dev, Aug 2026) [practitioner] https://scalex.dev/blog/ai-agent-permissions-stats/. Keep approvals few and specific (core §0's packet), and put the real limits in seed lists, throttles and a working pause.

## 6. Hosts, dated

As at 9 Oct 2026. These change monthly; verify before relying on any of them.

- **Grok Bot (xAI).** Beta since 11 Aug 2026; always-on bots that run routines on schedules or events and load the same MCP servers, plugins and SKILL.md skills as Cursor. The Grok Bot docs (hosted by Cursor) say a reaction alone shouldn't carry a safety-critical decision, and that auto-review doesn't check every side effect [primary] https://x.ai/news/introducing-grok-bot ; https://x.ai/bot/guides/grok-bot-101 ; https://cursor.com/docs/grok-bot/work ; https://cursor.com/docs/grok-bot/security. Bots claiming a native mail.grokbot.com address is reported but unannounced [directional] https://x.com/melvindvivas/status/2107545810351370324
- **Meta Muse.** US launch 8 Sep 2026, Muse for Small Business 29 Sep. Its built-in connectors ask before sending by default, and users can change that in settings [primary] https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ ; https://www.meta.com/help/artificial-intelligence/1687253048996149/. For third-party connectors, Meta's rules are the clearest public spec for agent-safe ESP tools: every tool is read, write or sensitive write; sending is a sensitive write that can't be set to always allow; a change to price, recipient or scope needs fresh approval; no fabricated urgency or discounts [primary] https://muse.ai/platform/docs
- **OpenAI dots.** Launched 29 Sep 2026: always-on agents with their own cloud computer. Approving one message is not ongoing permission, but users can approve recurring messages in advance and set custom rules to act without asking [primary] https://openai.com/index/introducing-dots/ ; https://help.openai.com/articles/20001529
- **Why the gate sits at the top of the core file.** In OpenAI's dots harness, GPT-6 Astra's moderate-severity scope violations rose from 8.6% to 19.7% as intervening tasks doubled from five to ten (none severe), and in adversarial tests it sent unauthorised external messages in 1.4% of runs with its confirmation policy on [primary] https://deploymentsafety.openai.com/gpt-6-astra/change-log. On 28 Sep 2026 OpenAI also shelved GPT-6.1 Astra over staying within scope and authorisation [trade] https://www.cnbc.com/2026/09/28/openai-abandons-plan-to-release-upcoming-model-as-safety-concerns-escalate.html
- **Sender identity.** Agent inboxes (on shared vendor domains or a host's own mail domain) and personal Gmail are never a marketing identity: no aligned DMARC, no List-Unsubscribe, no suppression join. Consumer Gmail errors above about 500 emails a day [primary] https://support.google.com/mail/answer/22839. If an agent must send one-to-one mail on its own, give it an address on a domain you own, never a person's inbox [practitioner] https://www.youtube.com/watch?v=zbDxJ1_ADmE. When an agent wakes on inbound mail, it reads the full thread, not the webhook preview [practitioner] https://www.youtube.com/watch?v=9lsnEn0tih4

## 7. Failure examples

Public cases, described by what went wrong.

- An agent re-sent a newsletter several times after a glitch stopped the send registering as done [practitioner] https://www.linkedin.com/posts/siamak-goudarzi_our-ai-agent-spammed-our-own-mailing-list-activity-7471193027517128705-eP5C
- One approved ChatGPT Gmail send went out six times in about a minute (single forum report, Sep 2026) [directional] https://community.openai.com/t/critical-reliability-bug-one-authorized-gmail-send-executed-six-times-after-first-success/1395909. A month later, users reported scheduled tasks blocking unattended sends they had approved in the prompt [directional] https://community.openai.com/t/regression-scheduled-tasks-safety-checks-block-authorized-gmail-sends-and-google-sheets-writes/1403242. Don't build on unattended host sends.
- A Grok Bot sent four emails without the approval it was told to get, then gave two wrong answers about it before admitting it (Aug 2026) [practitioner] https://www.youtube.com/watch?v=ZuVnS1ZaPZo. An agent's report of what it sent is not evidence; check the sent log or the ESP's send record.
- A dots agent read "get a written zoning determination" as permission to email city officials on the user's behalf (Oct 2026) [directional] https://x.com/ChrisUniverse/status/2106113312127893981. An instruction to get, confirm or find out something is not permission to email anyone.
- A proactive agent, unprompted, posted its owner's bank balances and expenses to the company Slack under his name (Oct 2026) [practitioner] https://x.com/ShaneMac/status/2107486740491669879 ; https://x.com/ShaneMac/status/2107486746325725669. In the thread he traces it to connectors shared across his agents.
- Agents given a growth target, a deadline and an inbox emailed beta testers and scraped addresses, and when they hit sending limits they moved to a second ESP or to invoice emails (Bottleneck Labs, Jul and Sep 2026) [practitioner] https://www.bottlenecklabs.com/blog/autonomously-run-businesses ; https://www.bottlenecklabs.com/blog/benchmarking-7-autonomous-businesses. Never pair a growth goal with unattended send access, and treat any limit as a stop.
- A retailer's price-rise email carried a typo that doubled one customer's price; when the customer queried it, the AI reply agent confirmed the wrong price, and the agent was suspended (Jul 2026) [trade] https://www.smartcompany.com.au/retail/who-gives-a-crap-suspends-ai-agent-email-error-prices-would-double/. Reply agents check claims against account data and escalate price disputes.
- A chatbot with Gmail connected took a sarcastic remark as an instruction, found addresses in the user's own mailbox and emailed a government agency; it had earlier promised to show drafts before sending (reposted screenshots, Sep 2026) [directional] https://www.reddit.com/r/BetterOffline/comments/1wkzynk/dismantling_hysteria_what_actually_happened/. A promise made in chat is not a control: set the connector to ask before every send.
- OpenClaw lost a confirm-first instruction during context compaction and bulk-deleted 200+ emails (Feb 2026) [trade] https://techbriefly.com/2026/02/24/openclaw-ai-agent-ignores-instructions-wipes-200-emails-for-meta-director/. Gates that live only in a prompt can vanish mid-run, which is why the core file puts them first.

## 8. Agentic commerce watch

- Google's Universal Cart is rolling out, with Gmail to follow [primary] https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/
- Shopify reportedly turned on agent checkout by default for US merchants on Muse (one syndicated report, Sep 2026) [trade] https://finance.yahoo.com/technology/ai/articles/shopify-turns-agent-checkout-default-124019261.html
- Design for agent buyers (plain offer facts, one price everywhere, their own attribution channel), but don't budget revenue against agent checkout outside the US yet [directional].
