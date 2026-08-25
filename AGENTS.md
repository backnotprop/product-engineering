# AGENTS.md — the fence

This repository vendors other authors' writing **byte-for-byte** and proves it with
hashes. Most files here are not editable, even to fix a typo. Before touching ANY
file, look it up in `foundry/MANIFEST.json`.

## The five rules

1. **Never retype vendored content.** Bytes enter this repo only through
   `foundry/scripts/lift.sh`. If you find yourself reproducing text from an upstream
   repo in your own output, stop — run the script instead.
2. **Locked files are never edited.** Classes `verbatim`, `verbatim-minus`, and
   `distilled` are hash-locked; CI fails on one changed character. If a change seems
   needed, propose it: a re-lift (upstream changed), a ledger ruling (we disagree with
   the content), or an upstream PR (the content has a bug). Never edit in place.
3. **Every change is a logged event.** Append one line to `foundry/LOG.md` for any
   provenance-changing action. Scripts log their own actions. Never edit existing lines.
4. **Upstream drift is classified, never auto-merged.** You may draft re-lift PRs and
   drift issues; only a human merges. See the runbooks.
5. **The ledger is law.** `foundry/LEDGER.md` holds the contradiction rulings (L-01…).
   No text you author may contradict an active ruling. Changing a ruling is a new
   superseding entry, never a silent edit.

## Where the full process lives

The foundry skill — `.claude/skills/foundry/SKILL.md` — carries the methodology
(grading, spine + byte-preserved references, anti-slop gates) and seven runbooks
(lift, re-lift, distill refresh, new ruling, integrity failure, course drop-in,
new skill/upstream). Load it before doing any convergence or maintenance work.

Verify before any PR: `foundry/scripts/check-integrity.sh` must pass.

Never commit anything under `skills/*/references/course/` — purchased content,
gitignored by design.
