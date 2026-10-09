# Releasing

How to ship a new version of the Email Marketing Bible. The root `SKILL.md` and `references/` are the source; the plugin reads an identical copy under `skills/email-marketing-bible/`.

## 1. Sync the plugin copy

```bash
cp SKILL.md skills/email-marketing-bible/SKILL.md && rsync -a --delete references/ skills/email-marketing-bible/references/
```

## 2. Run the CI checks locally

The same five checks run on every push (`.github/workflows/skill-sync.yml`):

1. `cmp SKILL.md skills/email-marketing-bible/SKILL.md`
2. `diff -r references skills/email-marketing-bible/references`
3. One version string in the SKILL.md frontmatter, the SKILL.md version line, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and the README version line.
4. No em dashes in `SKILL.md`, `references/`, `README.md`, `CHANGELOG.md` or `RELEASING.md`.
5. `wc -w < SKILL.md` at or under 2,600, and `wc -c < SKILL.md` at or under 18,000 bytes (about 4,500 tokens).

## 3. Validate the plugin

On a current Claude Code CLI (tested with 2.1.286; 2.0.76 rejects `--strict` and the manifest's listing fields):

```bash
claude plugin validate --strict .
```

## 4. Check the install paths

- **Double load.** Clone fresh into a scratch skills folder, then run `claude plugin list` and `claude plugin details email-marketing-bible`. Record the on-invoke token count (target under 4,500) and whether the skill is listed twice.
- **Links.** Check every URL in `SKILL.md` and `references/` returns 200. Some sites (OpenAI, Meta, the FTC, Légifrance, the CRTC, Figma) block non-browser requests; open those in a browser.

## 5. Update the surfaces outside this repo

- The GitHub release title and notes.
- The copy and JSON-LD on nitrosend.com/email-marketing-bible.
- The hero and `llms.txt` on emailmarketingskill.com.

## 6. Commit

No commit, PR or release note carries an AI attribution trailer (`Co-Authored-By`, "Generated with"). Before pushing:

```bash
git log --format=%B origin/main..HEAD | grep -iE '^(Co-Authored-By|Generated with)'
```

It must print nothing.
