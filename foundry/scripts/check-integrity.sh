#!/usr/bin/env bash
# check-integrity.sh — the gate. Fails (nonzero) if any vendored byte drifted.
#
# Checks, per foundry/MANIFEST.json:
#   verbatim        sha256(file) must equal the recorded hash
#   verbatim-minus  patch applied to the pristine copy must reproduce the file,
#                   AND sha256(file) must equal the recorded hash
#   distilled       sha256(file) must equal the recorded hash (updated only via
#                   the distill runbook: --update-distilled <path>)
#   authored        no hash check
#   private: true   skipped when absent (course drop-in); verified when present
# Coverage: every file under skills/*/references/ must have a manifest entry.
#
# Usage: foundry/scripts/check-integrity.sh [--update-distilled <repo-path>]
set -euo pipefail
REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
export REPO_ROOT
exec python3 - "$@" <<'PYEOF'
import hashlib, json, os, subprocess, sys, tempfile
from datetime import date

ROOT = os.environ["REPO_ROOT"]
MANIFEST = os.environ.get("FOUNDRY_MANIFEST", os.path.join(ROOT, "foundry", "MANIFEST.json"))
LOG = os.path.join(os.path.dirname(MANIFEST), "LOG.md")
manifest = json.load(open(MANIFEST))
files = manifest["files"]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""): h.update(chunk)
    return h.hexdigest()

# --- deliberate distilled update (the distill runbook's final step) ---
if len(sys.argv) == 3 and sys.argv[1] == "--update-distilled":
    p = sys.argv[2]
    e = files.get(p) or sys.exit(f"integrity: no manifest entry for {p}")
    if e["class"] != "distilled": sys.exit(f"integrity: {p} is class {e['class']}, not distilled")
    e["sha256"] = sha256(os.path.join(ROOT, p)); e["updated"] = date.today().isoformat()
    json.dump(manifest, open(MANIFEST, "w"), indent=2); open(MANIFEST, "a").write("\n")
    with open(LOG, "a") as f:
        f.write(f"- {date.today().isoformat()} · distill-update · {os.environ.get('USER','unknown')} · {p} · sha256={e['sha256'][:12]}…\n")
    print(f"integrity: distilled hash updated for {p}"); sys.exit(0)

failures = []

for path, e in sorted(files.items()):
    abs_path = os.path.join(ROOT, path)
    cls = e["class"]
    if not os.path.exists(abs_path):
        if e.get("private"): continue                    # drop-in not installed here
        failures.append(f"MISSING   {path} (class {cls})"); continue
    if cls == "authored": continue
    if "sha256" in e:
        actual = sha256(abs_path)
        if actual != e["sha256"]:
            failures.append(f"DRIFT     {path} (class {cls})\n"
                            f"            expected {e['sha256']}\n"
                            f"            actual   {actual}\n"
                            f"            Locked file changed. Revert it, or use the re-lift/distill runbook.")
    elif cls == "distilled":
        failures.append(f"NO-HASH   {path} — distilled entry missing sha256; run --update-distilled after authoring")
    if cls == "verbatim-minus":
        pristine = os.path.join(ROOT, e["pristine"]); patch = os.path.join(ROOT, e["patch"])
        if not (os.path.exists(pristine) and os.path.exists(patch)):
            failures.append(f"NO-BASE   {path} — pristine or patch file missing"); continue
        with tempfile.TemporaryDirectory() as td:
            work = os.path.join(td, "work")
            with open(pristine, "rb") as s, open(work, "wb") as d: d.write(s.read())
            if os.path.getsize(patch) > 0:
                r = subprocess.run(["patch", "--quiet", "--posix", work, patch], capture_output=True)
                if r.returncode != 0:
                    failures.append(f"BAD-PATCH {path} — patch does not apply cleanly to pristine"); continue
            if sha256(work) != sha256(abs_path):
                failures.append(f"PATCH-DRIFT {path} — pristine+patch does not reproduce the shipped file")

# --- coverage: nothing under references/ escapes classification ---
skills_dir = os.path.join(ROOT, "skills")
if os.path.isdir(skills_dir):
    for dirpath, _, names in os.walk(skills_dir):
        for n in names:
            rel = os.path.relpath(os.path.join(dirpath, n), ROOT)
            parts = rel.split(os.sep)
            if len(parts) >= 3 and parts[2] == "references" and rel not in files:
                if n == "README.md" and "course" in parts: continue   # drop-in folder README
                failures.append(f"UNTRACKED {rel} — every references/ file needs a manifest entry (authored counts)")

if failures:
    print("integrity: FAIL\n")
    print("\n".join("  " + f for f in failures))
    print(f"\n  {len(failures)} problem(s). Locked files are never edited in place —")
    print("  see .claude/skills/foundry/runbooks/integrity-failure.md")
    sys.exit(1)
print(f"integrity: OK · {len(files)} tracked file(s) verified")
PYEOF
