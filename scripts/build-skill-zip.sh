#!/usr/bin/env bash
# Build dist/email-marketing-bible.zip: the upload package for claude.ai and
# Claude desktop (Customize > Skills > + > Create skill > Upload a skill).
#
# The ZIP holds one folder named after the skill, with SKILL.md, references/
# and LICENSE inside. claude.ai's upload form caps the description at 200
# characters, so the packaged SKILL.md carries SHORT_DESCRIPTION below in place
# of the full trigger description. Everything else is byte-for-byte the root
# SKILL.md and references/.
set -euo pipefail

NAME="email-marketing-bible"
SHORT_DESCRIPTION="Email marketing manual with send-safety gates. Use for any email campaign, newsletter, flow, list, deliverability, compliance, copy, design or ESP task, and before any send to a list."

root="$(cd "$(dirname "$0")/.." && pwd)"
out="$root/dist"
stage="$out/$NAME"

rm -rf "$out"
mkdir -p "$stage"
cp -R "$root/references" "$stage/references"
cp "$root/LICENSE" "$stage/LICENSE"

SHORT_DESCRIPTION="$SHORT_DESCRIPTION" python3 -I - "$root/SKILL.md" "$stage/SKILL.md" "$NAME" <<'PY'
import os, re, sys
src, dst, name = sys.argv[1], sys.argv[2], sys.argv[3]
short = os.environ["SHORT_DESCRIPTION"]
text = open(src, encoding="utf-8").read()
m = re.match(r"---\n(.*?)\n---\n", text, re.S)
if not m:
    sys.exit("SKILL.md has no YAML frontmatter")
front = m.group(1)
# Swap the folded description block for the short one.
new_front, n = re.subn(r"^description: >\n(?:  .*\n?)+", 'description: "%s"\n' % short.replace('"', "'"), front + "\n", flags=re.M)
if n != 1:
    sys.exit("could not find the folded description block in the frontmatter")
fm_name = re.search(r"^name: (.+)$", new_front, re.M).group(1).strip()
errors = []
if fm_name != name:
    errors.append(f"frontmatter name '{fm_name}' must match folder '{name}'")
if len(fm_name) > 64:
    errors.append("name is over 64 characters")
if len(short) > 200:
    errors.append(f"short description is {len(short)} characters (claude.ai cap is 200)")
if re.search(r"[<>]", short):
    errors.append("short description must not contain < or >")
if errors:
    sys.exit("; ".join(errors))
open(dst, "w", encoding="utf-8").write("---\n" + new_front.rstrip("\n") + "\n---\n" + text[m.end():])
print(f"SKILL.md packaged with a {len(short)}-character description")
PY

(cd "$out" && rm -f "$NAME.zip" && zip -q -X -r "$NAME.zip" "$NAME")

# Check the archive the way the upload form does: one top-level folder named
# after the skill, SKILL.md directly inside it, every reference file present.
python3 -I - "$out/$NAME.zip" "$NAME" "$root/references" <<'PY'
import os, sys, zipfile
zpath, name, refs = sys.argv[1], sys.argv[2], sys.argv[3]
z = zipfile.ZipFile(zpath)
names = [n for n in z.namelist() if not n.endswith("/")]
tops = {n.split("/")[0] for n in names}
assert tops == {name}, f"top level must be only '{name}/', found {sorted(tops)}"
assert f"{name}/SKILL.md" in names, "SKILL.md must sit directly inside the skill folder"
assert f"{name}/LICENSE" in names, "LICENSE missing"
want = {f"{name}/references/{f}" for f in os.listdir(refs) if f.endswith(".md")}
missing = want - set(names)
assert not missing, f"missing reference files: {sorted(missing)}"
size = os.path.getsize(zpath)
print(f"{zpath}: {len(names)} files, {size // 1024} KB")
PY
