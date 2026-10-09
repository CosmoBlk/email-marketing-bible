# Segmentation and list building

Read this when: building segments, lists, engagement tiers, lead magnets, sunsets or list hygiene.
Last checked: 9 Oct 2026
Gather first: data fields available, list size, consent records.

Any send to a segment goes through the core §0 gate. Tier and sunset numbers are in thresholds.md.

## Structure

- **5K engaged beats 50K messy.**
- **Lists vs tags vs segments:** one master list; tags are facts; segments are dynamic rules. Minimum segments: new (30d), engaged (clicked 60d), customer vs non-customer, lapsed (90d+).

## Building segments with an agent

- **Segments from natural language:** let the agent build the rules, then verify against actual counts before sending. A segment that jumps 10x between runs is a bug until proven otherwise.
- **Show any bulk audience as rules, count and five sample rows** before it's used.
- **Send to rule-based segments you can explain.** Use model scores and predictions to help build them, not to replace them, so a bad send can be traced (Send It! podcast, Jul 2026) [practitioner] https://www.youtube.com/watch?v=7S1tUExRVhw
- **Engagement-based sending (highest-impact lever):** clicked 30d → every send; 60d → 75%; 90d → best only; 90-180d → re-engagement only; 180d+ → sunset (EMB policy). Build tiers on bot-filtered clicks, never opens (measurement.md). Practitioners report complaints falling 20-40% with revenue holding or rising [directional].

## Personalisation

- **Hierarchy (high → low):** behavioural → lifecycle stage → dynamic blocks → send time → location → name. Above all: agent-generated 1:1 content from real behavioural data (clean data first; draft-and-approve).
- **Relevance over recognition.** Ask whether the personalisation improves the customer's decision or reduces friction, and whether it would still feel helpful if they noticed it. Ten AI variants is not a reason for ten to exist (Kath Pay, "Personalisation is not a merge tag, it's a judgement call", 28 Jul 2026) [practitioner] https://holisticemailacademy.com/2026/07/28/personalisation-is-not-a-merge-tag-its-a-judgement-call/

## List building

- Lead magnets (templates convert best) · content upgrades (5-10x sidebar forms) · forms beat links (+20-50%). Popups 3-5% (top decile ~9%); exit-intent 4-7%; two-step beats one-step [directional].
- **Double opt-in for lead magnets.** It matters more now that agents and bots fill forms [directional]. Confirm marketing permission for buyers too; a purchase alone isn't consent everywhere (compliance.md).
- Opt-in boxes start unticked and keep the person's choice through scrolling, re-renders and back navigation; test the form on a phone and store consent per channel at submit. An airline app that appeared to re-tick its marketing box drew 13,000 upvotes of anger (r/assholedesign, Jul 2026) [directional] https://www.reddit.com/r/assholedesign/comments/1v9lnxz/the_united_airlines_app_sneakily_remarks_the_i/
- Chrome's Email Verification Protocol (origin trial, with Gmail as issuer) confirms address ownership at signup without a code. It cuts typos and fake signups, but it proves ownership, not consent [primary] https://developer.chrome.com/blog/email-verification-protocol-origin-trial
- After any change to an AI chat or assistant on the site, test that it still captures email and consent: Shopify Inbox's July 2026 update stopped asking chat visitors for an email, and one merchant lost a $500 lead with no way to reply (Shopify Community) [practitioner] https://community.shopify.com/t/warning-about-the-new-shopify-inbox/657638

## Hygiene and sunsets

- Lists decay 22-30% a year [directional].
- **Sunset:** reduce frequency → 2-3 re-engagement emails → suppress.
- **Preference centre:** offer "fewer" and "snooze" before "leave" (measurement.md).
- **Relevance by recipient:** suppress recent buyers from promotions for what they just bought, and rotate content for heavy recipients. Gmail is testing a thumbs-down on Promotions whose reasons include "I already own the product" and "repetitive content" (screenshot of a test, Oct 2026) [directional] https://www.reddit.com/r/Emailmarketing/comments/1wy681x/gmail_will_now_soon_give_an_option_to_readers_to/
- **Trap prevention:** double opt-in, real-time validation, engagement-based sending.
- Zero bounces is not proof the reader is there: Gmail users can now change their address and the old one keeps receiving [primary] https://support.google.com/accounts/answer/19870. Sunset on engagement.
