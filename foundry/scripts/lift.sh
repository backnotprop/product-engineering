#!/usr/bin/env bash
# lift.sh — the ONLY way vendored bytes enter this repository.
#
# Copies a file from a pinned upstream commit into the repo, records provenance
# (upstream, path, commit SHA, sha256) in foundry/MANIFEST.json, and appends a
# LOG.md entry. LLM agents must never retype vendored content; they call this.
#
# Usage:
#   foundry/scripts/lift.sh --upstream <id> --path <upstream-path> --dest <repo-path> \
#       --skill <skill> [--sha <commit|HEAD>] [--class verbatim|verbatim-minus|distilled-source] \
#       [--actor <name>] [--dry-run]
#
#   --upstream   key in MANIFEST.json "upstreams"
#   --sha        upstream commit to lift from (default: HEAD of default branch)
#   --class      verbatim (default) | verbatim-minus (also stores a pristine copy;
#                author the cut afterwards with make-patch.sh) | distilled-source
#                (records the source for a distilled file WITHOUT copying bytes)
#   --dry-run    print what would happen, change nothing
#
# Env: FOUNDRY_MANIFEST overrides the manifest path (used by tests).
set -euo pipefail
REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
export REPO_ROOT
exec python3 - "$@" <<'PYEOF'
import hashlib, json, os, re, subprocess, sys
from datetime import date

ROOT = os.environ["REPO_ROOT"]
MANIFEST = os.environ.get("FOUNDRY_MANIFEST", os.path.join(ROOT, "foundry", "MANIFEST.json"))
LOG = os.path.join(os.path.dirname(MANIFEST), "LOG.md")
CACHE = os.path.join(ROOT, ".foundry-cache")

def die(msg): print(f"lift: ERROR: {msg}", file=sys.stderr); sys.exit(1)

args = sys.argv[1:]
opt = {"sha": "HEAD", "class": "verbatim", "actor": os.environ.get("USER", "unknown"), "dry_run": False}
i = 0
while i < len(args):
    a = args[i]
    if a == "--dry-run": opt["dry_run"] = True; i += 1; continue
    if not a.startswith("--") or i + 1 >= len(args): die(f"bad argument: {a}")
    opt[a[2:].replace("-", "_")] = args[i + 1]; i += 2
for req in ("upstream", "path", "dest", "skill"):
    if req not in opt: die(f"--{req} is required")
if opt["class"] not in ("verbatim", "verbatim-minus", "distilled-source"):
    die(f"unknown class: {opt['class']}")

manifest = json.load(open(MANIFEST))
up = manifest["upstreams"].get(opt["upstream"]) or die(f"unknown upstream: {opt['upstream']}")
if not up.get("url"): die(f"upstream {opt['upstream']} has no URL (private source — use course-dropin.sh)")

# --- cache clone, pinned fetch ---
cachedir = os.path.join(CACHE, re.sub(r"[^A-Za-z0-9._-]", "_", opt["upstream"]))
if not os.path.isdir(cachedir):
    subprocess.run(["git", "clone", "--quiet", up["url"], cachedir], check=True)
subprocess.run(["git", "-C", cachedir, "fetch", "--quiet", "origin"], check=True)
sha = opt["sha"]
if sha == "HEAD":
    head = subprocess.run(["git", "-C", cachedir, "ls-remote", "origin", "HEAD"],
                          capture_output=True, text=True, check=True).stdout.split()
    sha = head[0]
sha = subprocess.run(["git", "-C", cachedir, "rev-parse", f"{sha}^{{commit}}"],
                     capture_output=True, text=True, check=True).stdout.strip()

# --- extract blob at pinned SHA (bytes, never through a model) ---
blob = subprocess.run(["git", "-C", cachedir, "show", f"{sha}:{opt['path']}"],
                      capture_output=True, check=True).stdout
digest = hashlib.sha256(blob).hexdigest()

dest_abs = os.path.join(ROOT, opt["dest"])
entry = {
    "class": opt["class"], "upstream": opt["upstream"], "upstream_path": opt["path"],
    "pinned_sha": sha, "sha256": digest, "lifted": date.today().isoformat(),
    "skill": opt["skill"], "rulings": [],
}

if opt["dry_run"]:
    print(f"lift: DRY RUN — would write {len(blob)} bytes to {opt['dest']}")
    print(json.dumps({opt["dest"]: entry}, indent=2)); sys.exit(0)

if opt["class"] != "distilled-source":
    os.makedirs(os.path.dirname(dest_abs), exist_ok=True)
    open(dest_abs, "wb").write(blob)
if opt["class"] == "verbatim-minus":
    pristine = os.path.join(os.path.dirname(MANIFEST), "pristine", opt["dest"].replace("/", "__"))
    os.makedirs(os.path.dirname(pristine), exist_ok=True)
    open(pristine, "wb").write(blob)
    entry["pristine"] = os.path.relpath(pristine, ROOT)
    entry["patch"] = entry["pristine"] + ".patch"
    open(os.path.join(ROOT, entry["patch"]), "w").write("")  # authored next via make-patch.sh
if opt["class"] == "distilled-source":
    entry["class"] = "distilled"
    entry["note"] = "source recorded; file content is authored — hash set by check-integrity --update-distilled"
    entry.pop("sha256")

manifest["files"][opt["dest"]] = entry
json.dump(manifest, open(MANIFEST, "w"), indent=2); open(MANIFEST, "a").write("\n")
with open(LOG, "a") as f:
    f.write(f"- {date.today().isoformat()} · lift · {opt['actor']} · {opt['dest']} ← "
            f"{opt['upstream']}:{opt['path']} @ {sha[:9]} · class={entry['class']} · sha256={digest[:12]}…\n")
print(f"lift: OK · {opt['dest']} ← {opt['upstream']}:{opt['path']} @ {sha[:9]} · {entry['class']}")
PYEOF
