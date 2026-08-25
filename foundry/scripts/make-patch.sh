#!/usr/bin/env bash
# make-patch.sh — record the cut for a verbatim-minus file.
#
# After lift.sh --class verbatim-minus (which stores the pristine copy and an
# empty patch), edit the SHIPPED file to remove the sections being cut, then run
# this to regenerate the patch and re-lock the hash. The cut itself is reviewed
# as the patch diff.
#
# Usage: foundry/scripts/make-patch.sh <repo-path>
set -euo pipefail
REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
export REPO_ROOT
exec python3 - "$@" <<'PYEOF'
import hashlib, json, os, subprocess, sys
from datetime import date
ROOT = os.environ["REPO_ROOT"]
MANIFEST = os.environ.get("FOUNDRY_MANIFEST", os.path.join(ROOT, "foundry", "MANIFEST.json"))
LOG = os.path.join(os.path.dirname(MANIFEST), "LOG.md")
manifest = json.load(open(MANIFEST))
path = sys.argv[1]
e = manifest["files"].get(path) or sys.exit(f"make-patch: no manifest entry for {path}")
if e["class"] != "verbatim-minus": sys.exit(f"make-patch: {path} is class {e['class']}")
r = subprocess.run(["diff", "-u", os.path.join(ROOT, e["pristine"]), os.path.join(ROOT, path)],
                   capture_output=True, text=True)
if r.returncode not in (0, 1): sys.exit(f"make-patch: diff failed: {r.stderr}")
open(os.path.join(ROOT, e["patch"]), "w").write(r.stdout)
h = hashlib.sha256(open(os.path.join(ROOT, path), "rb").read()).hexdigest()
e["sha256"] = h
json.dump(manifest, open(MANIFEST, "w"), indent=2); open(MANIFEST, "a").write("\n")
with open(LOG, "a") as f:
    f.write(f"- {date.today().isoformat()} · make-patch · {os.environ.get('USER','unknown')} · {path} · patch regenerated · sha256={h[:12]}…\n")
print(f"make-patch: OK · {path} · patch {'empty (no cut yet)' if r.returncode == 0 else 'recorded'}")
PYEOF
