# Models

Read this when: choosing models for design, critique, images or video.
Last checked: 9 Oct 2026
Gather first: which hosts and API keys the user actually has, and the task (critique, build, stills, motion).

Model names go stale within weeks: three of the six names in v2.7 had a successor within three weeks. Fill the roles first, then check the shelf. If this file's date is more than about 90 days old, look up current names before recommending one (core §0b).

## Roles

- **Critic:** the strongest vision-capable model you can reach, in a fresh context (no code, history or earlier critiques). The fresh context matters more than the gap in model strength: with Opus 5.5 near Fable 5.1 quality at lower cost, "stronger critic, cheaper implementer" is no longer the point.
- **Implementer:** your coding agent, building in MJML, React Email or Maizzle.
- **Stills:** the current image model, for hero and lifestyle imagery only. Never for quote tiles, type or real people presented as real (core §7, compliance.md).
- **Motion:** the current video model, for a looping hero or a state transition, exported as animated WebP with a first frame that works as a still.

## The shelf, as at 9 Oct 2026 (verify before use)

| Role fit | Model | Released | Source |
|---|---|---|---|
| Critic | Claude Fable 5.1 | 1 Sep 2026 | https://platform.claude.com/docs/en/models/fable-5-1/overview |
| Critic or implementer | Claude Opus 5.5 | 22 Sep 2026 | https://www.anthropic.com/claude-opus-5-5 |
| Implementer | Claude Sonnet 5.5 | 28 Sep 2026 | https://www.anthropic.com/claude-sonnet-5-5 |
| Fast drafts, lint passes | Claude Haiku 5.5 | 7 Oct 2026 | https://www.anthropic.com/claude-haiku-5-5 |
| Implementer (Codex) | GPT-6 Astra | 3 Sep 2026 | https://openai.com/index/gpt-6-astra/ |
| Implementer (Codex) | GPT-6.1 Sol | 29 Sep 2026 | https://openai.com/index/introducing-gpt-6-1-sol/ |
| Everyday drafting | GPT-6 Sol and GPT-6 Luna | 22 Sep 2026 | https://openai.com/index/introducing-gpt-6-sol-and-luna/ |
| Stills | GPT Images 2.5 (Flare and Sunburst) | 8 Sep 2026 | https://community.openai.com/t/introducing-gpt-images-2-5-in-the-api-and-chatgpt/1395897 |
| Motion | Gemini Omni 1.1 | carried from v2.7; not re-verified in Oct 2026 | Check Google's current model list |

Claude release dates: https://support.claude.com/en/articles/12138966-release-notes [primary]. All rows are vendor announcements [primary]; none of them is a quality ranking.

## Old names

For anyone matching older prompts, v2.7 (Sep 2026) named: Claude Fable 5.1 as critic; Claude Opus 5 or Sonnet 5 (Claude Code) or GPT-6 Astra (Codex CLI) as implementer; gpt-image-2 for stills; Gemini Omni 1.1 for video.
