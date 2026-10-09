# Copy

Read this when: writing subject lines, body copy, CTAs, or rewriting AI-sounding drafts beyond the core lint.
Last checked: 9 Oct 2026
Gather first: audience, offer, voice, one real proof; for a whole campaign, also the segment, consent basis, sender and timing.

The core §5 lint runs on every draft; this file goes deeper. Copy goes out only through the core §0 gate.

## Contents

1. Why the lint matters now
2. Workflow
3. More tells to lint for
4. Subject lines and preview text
5. Body, frameworks and CTAs
6. Writing for summaries and agents
7. The context line

## 1. Why the lint matters now

- **Trust.** 40% of US consumers would trust a retailer's emails less if they knew AI wrote them (Validity, 1 Jun 2026) [vendor] https://www.prnewswire.com/news-releases/validity-research-reveals-consumers-let-ai-curate-their-inboxes-while-marketers-struggle-to-keep-up-302785148.html. In a self-selected survey of 668 developers, 78% said they stop reading once they suspect AI writing (Cynthia Dunlop, cited by Bryan Cantrill, Sep 2026) [directional] https://bcantrill.dtrace.org/2026/09/05/the-revolt-of-the-reader/
- **Detection is now a product.** Pangram labels incoming Gmail that AI wrote and can route fully AI mail away from the inbox (Sep 2026) [vendor] https://x.com/max_spero_/status/2100242436991705542. Since 21 Jul 2026 any Substack reader can scan a post for AI text [primary] https://post.substack.com/p/against-claudefishing. Detectors misfire (Freddie deBoer got a 300-word section called 100% AI inside an essay rated 100% human) [practitioner] https://freddiedeboer.substack.com/p/i-wouldnt-say-pangram-is-broken-but, so never chase a score and never run copy through a "humaniser". Claude marks its generated text, and OpenAI has announced EU watermarking (compliance.md).
- **AI copy can perform.** In three RCTs at one wine retailer, human, AI and hybrid newsletter copy each roughly doubled gross profit against sending nothing, with similar results between them, and net of labour and software costs an AI option always came out ahead (Dubé and Xu, QME, Jan 2026) [primary] https://link.springer.com/article/10.1007/s11129-025-09303-9. The goal is helpful, specific and checked, not undetectable.
- **How teams use it.** 64% of email marketers use AI, and 1.1% start an email with it (Really Good Emails "AI Confessions", 25 Sep 2026) [vendor survey] https://reallygoodemails.com/school/blog/ai-in-email-marketing-ai-confessions
- **What the lint is for.** The popular tells are also ordinary human writing (Ann Handley, "AI Slop, Accusations, And A Better Way") [practitioner] https://annhandley.com/ai-slop/. Treat the blacklist as a lint for model defaults, not an AI detector. The real tell is still the absence of stakes.

## 2. Workflow

- **Human strategy → AI draft → human edit.** Rough human notes first for high-personality formats (founder letter, welcome) [directional].
- **Brief before draft.** Ask the model for audience, the job of the send, the promise, the main objection, proof with a source per claim, three angles and what's missing, and tell it not to write the email yet. A human corrects the brief and picks the angle. When mining reviews for angles, any angle the evidence doesn't support comes back as NOT ENOUGH EVIDENCE (Chase Dimond, 26 and 27 Aug 2026) [practitioner] https://x.com/ecomchasedimond/status/2092738505936081245 ; https://x.com/ecomchasedimond/status/2093025060974219562
- **Real material in, angles out.** Feed the agent the sender's own material (call transcripts, posts, past winners) and ask for angles, subject variations and bullets, not finished emails; write or heavily edit the body yourself (Daniel Fazio, Jul 2026) [practitioner] https://www.youtube.com/watch?v=6Emeh3mLp7M. Each quarter, rebuild the house checklist from what the top 20 emails by click rate have in common.
- **Slot-fill pattern.** The AI fills marked slots in a human-written template; footer, unsubscribe and legal blocks stay locked and outside its edit scope (Really Good Emails, above) [vendor survey]. Keep slots short (about 10 words each), write results to a new field rather than overwriting source data, and read a sample of merged emails in full before any send (Nick Saraev, Aug 2026) [practitioner] https://www.youtube.com/watch?v=yulWjh3rq28

## 3. More tells to lint for

- **Em dashes** stay banned in output as a house rule, but they no longer prove AI on their own: Claude Sonnet 5.5 uses 94% to 99% fewer than Sonnet 5 on Vals AI's benchmarks (Sep 2026) [vendor eval] https://x.com/ValsAI/status/2104771555163254979
- **Structural tells** (Ruben Hassid, Aug 2026) [practitioner] https://x.com/rubenhassid/status/2087856703773508025: "That's not X. That's Y."; paired fragments ("Fast. Simple."); self-applause lines ("And that matters."); warm-up openers ("Here's the thing."); reflexive threes; invented ranges ("5 to 10 minutes"); recap endings. Keep a brand forbidden-patterns file and add every new tell you catch. A reader-side list with wide agreement adds "You don't need X. You need Y.", "And the best part?", "The truth?", "Stop X. Start Y.", "Read that again", "Let that sink in", "Nobody talks about this", "X is dead", "No fluff" and fortune-cookie endings (r/ChatGPT, Aug 2026; 774 points) [directional] https://www.reddit.com/r/ChatGPT/comments/1vlddcq/writing_formats_i_can_no_longer_read_because_ai/
- **Literal-read test.** Read every metaphor literally. If the verb doesn't fit the noun (a toolkit that "buys" you something, pillars that "undergird"), rewrite it in plain words (Taylor Jones, Language Jones, Aug 2026) [practitioner] https://www.youtube.com/watch?v=ORgKY9AlybA. Treat model pet words ("honestly", "quietly", "amid", "blueprint", "toolkit", "buckets") as warnings, not automatic fails.
- **Fake familiarity.** A personalised opener that has nothing to do with the ask is worse than none. Every personal detail must justify the ask in the next sentence, or cut it [practitioner] https://blog.pentlander.com/the-deeply-impersonal-personalized-recruiter-mail/
- **Pasted markup.** Paste AI drafts as plain text: copying out of a chat window can carry its class names and data attributes, even the model's name, into the email HTML. Check the received test's HTML source (a tool maker's finding, Oct 2026) [vendor] https://www.reddit.com/r/hubspot/comments/1wvphae/pasting_from_chatgpt_into_hubspot_leaves_hidden/
- **Leaked instructions.** Scan final copy for pasted prompt text and placeholders ("make a response", "as an AI", [First Name], unrendered `{{ }}`) [directional] https://x.com/Cartidise/status/2086055932275130429
- **Hidden text.** No hidden text beyond a short preheader, nothing addressed to an AI, and no pre-filled "summarise with AI" links. Hidden instructions are an attack signature: Forcepoint showed invisible HTML hijacking a lab summariser (25 Aug 2026) and Barracuda documents "text salting" in phishing (16 Jul 2026) [vendor] https://www.forcepoint.com/blog/x-labs/html-payload-hijacks-email-summarizer ; https://blog.barracuda.com/2026/07/16/text-salting-ai-email-security. Microsoft found companies planting memory-poisoning prompts in "Summarize with AI" links [primary] https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/. Strip invisible Unicode too (deliverability.md).

## 4. Subject lines and preview text

- Lowercase casual can beat title case (about 14%) and a first-person CTA can beat second-person [directional].
- Action + product + deadline in plain words is a strong default (Jay Schwedelson reports about 19% more clicks, with no published method) [directional]. The deadline must be real (compliance.md).
- Length is not the lever. Mobile truncates at about 45 characters (thresholds.md); test the extremes against your median and judge on clicks.
- Preview text adds information; it never repeats the subject.
- No fake "Re:" or "Fwd:", and no badge emoji in the sender name (deliverability.md).

## 5. Body, frameworks and CTAs

- **Body:** inverted pyramid, short paragraphs, write then cut 30%. 3:1 value-to-promo.
- **Frameworks:** AIDA (promo) · PAS (cold/B2B) · BAB (case studies) · Soap Opera Sequence (narrative) · 1-3-1 newsletter (one story, three items, one CTA).
- **CTAs:** buttons beat text links (+27%); one CTA beats several (+42%) [directional, source not published]; place it above the fold and again below the main content.

## 6. Writing for summaries and agents

BuzzStream tested 628 AI summaries one variable at a time: Gmail drew 87.1% of summary content from the first half of the email, Apple Intelligence 82.5% and Outlook Copilot 65.4%, and about one summary in three misstated data (Vince Nero, 15 Jul 2026; digital-PR pitch emails, small cells) [practitioner] https://www.buzzstream.com/blog/ai-generated-email-summary/

So: put the offer, the number and the deadline in the first live sentence; carry the key facts in two or three short bullets; never put a price, date or code only in an image or table. Where seed inboxes have summaries switched on, read the generated summary and fix the email if it drops or misstates the offer. Some of your readers will forward the email to an agent that acts on it, so state offers, prices, dates and links plainly.

## 7. The context line

One true reason this person is getting this email, taken from their consent record: the actual signup source and date, not a list of every possible route. A vague or wrong one sends people who can't remember signing up to the spam button (Al Iverson, "The Context Box: Do It, But Right", 26 Jul 2026, building on Dylan Redekop's term) [practitioner] https://www.spamresource.com/2026/07/the-context-box-do-it-but-right.html
