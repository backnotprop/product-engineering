#!/usr/bin/env bash
# check-upstream.sh — the watcher's data layer. For every tracked vendored file,
# compare the pinned upstream blob against the same path at upstream HEAD.
# Prints a machine-readable drift report; exits 0 always (classification happens
# downstream — see .github/workflows/upstream-watch.yml and the re-lift runbook).
#
# Output lines:
#   DRIFT <dest> <upstream> <upstream_path> <pinned_sha> <head_sha>
#   GONE  <dest> <upstream> <upstream_path> <head_sha>      (path removed upstream)
#   OK    <dest>
# Summary line last: "upstream-check: N drifted, M gone, K ok, S skipped"
set -euo pipefail
REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
export REPO_ROOT
exec python3 - "$@" <<'PYEOF'
import json, os, re, subprocess, sys
ROOT = os.environ["REPO_ROOT"]
MANIFEST = os.environ.get("FOUNDRY_MANIFEST", os.path.join(ROOT, "foundry", "MANIFEST.json"))
CACHE = os.path.join(ROOT, ".foundry-cache")
m = json.load(open(MANIFEST))
heads, drift, gone, ok, skipped = {}, [], [], 0, 0

def cache_for(up_id, url):
    d = os.path.join(CACHE, re.sub(r"[^A-Za-z0-9._-]", "_", up_id))
    if not os.path.isdir(d):
        subprocess.run(["git", "clone", "--quiet", url, d], check=True)
    subprocess.run(["git", "-C", d, "fetch", "--quiet", "origin"], check=True)
    head = subprocess.run(["git", "-C", d, "ls-remote", "origin", "HEAD"],
                          capture_output=True, text=True, check=True).stdout.split()[0]
    return d, head

def blob_sha(cachedir, commit, path):
    r = subprocess.run(["git", "-C", cachedir, "rev-parse", f"{commit}:{path}"],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None

for dest, e in sorted(m["files"].items()):
    up = e.get("upstream")
    if e["class"] == "authored" or not up: skipped += 1; continue
    info = m["upstreams"].get(up, {})
    if not info.get("url") or e.get("private"): skipped += 1; continue
    if up not in heads:
        heads[up] = cache_for(up, info["url"])
    cachedir, head = heads[up]
    pinned = blob_sha(cachedir, e["pinned_sha"], e["upstream_path"])
    current = blob_sha(cachedir, head, e["upstream_path"])
    if current is None:
        gone.append(dest); print(f"GONE  {dest} {up} {e['upstream_path']} {head[:9]}")
    elif current != pinned:
        drift.append(dest); print(f"DRIFT {dest} {up} {e['upstream_path']} {e['pinned_sha'][:9]} {head[:9]}")
    else:
        ok += 1; print(f"OK    {dest}")
print(f"upstream-check: {len(drift)} drifted, {len(gone)} gone, {ok} ok, {skipped} skipped")
PYEOF
