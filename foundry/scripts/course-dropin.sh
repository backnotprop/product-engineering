#!/usr/bin/env bash
# course-dropin.sh — LOCAL MACHINES ONLY. Fills the gitignored references/course/
# folders from a purchased animations.dev skill pack install. Nothing this script
# touches may ever be committed; the paths it writes to are gitignored, and
# check-integrity.sh verifies the ignore rules are intact.
#
# Usage:
#   COURSE_SRC=~/oss/backnotprop/design/animationsdev foundry/scripts/course-dropin.sh [--record]
#
#   --record   first run on a machine that owns the pack: store private hashes in
#              the manifest so later runs (and integrity checks) verify the copies.
#
# Mappings live in MANIFEST.json as entries with "private": true and
# "upstream": "animationsdev"; upstream_path is relative to $COURSE_SRC.
set -euo pipefail
REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
export REPO_ROOT
exec python3 - "$@" <<'PYEOF'
import hashlib, json, os, shutil, sys
from datetime import date
ROOT = os.environ["REPO_ROOT"]
SRC = os.path.expanduser(os.environ.get("COURSE_SRC", "~/oss/backnotprop/design/animationsdev"))
MANIFEST = os.environ.get("FOUNDRY_MANIFEST", os.path.join(ROOT, "foundry", "MANIFEST.json"))
LOG = os.path.join(os.path.dirname(MANIFEST), "LOG.md")
record = "--record" in sys.argv
manifest = json.load(open(MANIFEST))

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""): h.update(c)
    return h.hexdigest()

# refuse to run if the ignore fence is missing
gi = open(os.path.join(ROOT, ".gitignore")).read() if os.path.exists(os.path.join(ROOT, ".gitignore")) else ""
if "references/course/" not in gi:
    sys.exit("course-dropin: REFUSING — .gitignore does not fence references/course/")

n = 0
for path, e in manifest["files"].items():
    if not e.get("private") or e.get("upstream") != "animationsdev": continue
    src = os.path.join(SRC, e["upstream_path"]); dst = os.path.join(ROOT, path)
    if not os.path.exists(src): print(f"course-dropin: skip (not in pack): {e['upstream_path']}"); continue
    os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copyfile(src, dst)
    h = sha256(dst)
    if record:
        e["sha256"] = h; e["lifted"] = date.today().isoformat()
    elif e.get("sha256") and e["sha256"] != h:
        print(f"course-dropin: WARNING — {path} differs from recorded hash (course updated?). "
              f"Re-run with --record after confirming.", file=sys.stderr)
    n += 1
if record:
    json.dump(manifest, open(MANIFEST, "w"), indent=2); open(MANIFEST, "a").write("\n")
    with open(LOG, "a") as f:
        f.write(f"- {date.today().isoformat()} · course-dropin --record · {os.environ.get('USER','unknown')} · {n} file(s)\n")
print(f"course-dropin: {n} file(s) installed locally from {SRC}")
PYEOF
