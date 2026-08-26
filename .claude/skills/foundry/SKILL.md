---
name: foundry
description: The build-and-maintenance process for this repository's converged skill kit. Use for ANY convergence or maintenance work here — lifting files from upstream sources, building or revising one of the five skills, handling upstream drift or a failed integrity check, adding a contradiction ruling, distilling source material, installing the private course drop-in, or evaluating a new upstream or skill for the kit. Load BEFORE editing anything.
metadata:
  internal: "true"
license: Apache-2.0
---

# Foundry

This repo converges 84 upstream design-engineering skills into five
(`pe-design`, `pe-build`, `pe-review`, `pe-product-description`, `pe-brand-assets`), preserving the
best source prose **byte-for-byte** and proving it with hashes. You are operating a
factory with strict rules, not editing a normal repo. AGENTS.md is the fence; this
skill is the manual.

## Before anything else

1. Read `foundry/MANIFEST.json` — look up the class of every file you intend to touch.
2. Read `foundry/LEDGER.md` — rulings bind everything you author.
3. Pick the runbook that matches the task (table below) and follow it exactly.
4. End every session that changed provenance state with a `foundry/LOG.md` line and a
   green `foundry/scripts/check-integrity.sh`.

## File classes

| Class | Meaning | Your permissions |
| --- | --- | --- |
| `verbatim` | Byte-for-byte lift from a pinned upstream commit | Never edit. Re-lift via script or nothing. |
| `verbatim-minus` | Verbatim with a recorded cut (pristine + `.patch` in `foundry/pristine/`) | Never edit the file directly. Changing the cut = edit file, run `make-patch.sh`, PR shows the patch diff. |
| `distilled` | Authored condensation of recorded sources; the salvage list in its derivation file is the contract | Edit only via the distill-refresh runbook; finish with `check-integrity.sh --update-distilled <path>`. |
| `authored` | Ours: spines, glue, foundry docs | Edit freely, subject to the ledger and the anti-slop gates. |

`private: true` entries are course drop-in files — purchased content that exists only on
local machines, never in a commit.

## The convergence method (for building or revising a skill)

- **Architecture:** each skill is a thin authored **spine** (router: modes, cues,
  contract, rulings block; target < 150 lines) over **references** lifted verbatim from
  graded sources. New prose is written only for glue, routing, and rulings.
- **Grades bind handling:** GOLD → lift verbatim, never reword (cut whole sections only,
  via verbatim-minus, logged) · SOLID → lift, dedupe only · PADDED → distill against a
  named salvage list · SLOP → exclude.
- **Anti-slop gates on anything you author:** no restatement between spine and
  references (principle in the spine, recipe in the ref, never both) · every sentence
  must change an implementation choice · no adjective stacks, personas, or dial theater ·
  skill activation load stays under ~500 lines · **no provenance in runtime text** —
  MANIFEST, derivations, and NOTICE own provenance; skill prose states rules without
  citing sources, patches, pins, or ledger ids (frontmatter carries only a one-line
  derivations pointer).
- **Plan first:** write `foundry/derivations/<skill>.md` (sources, classes, cuts,
  rulings applied) before running a single lift. The receipts precede the work.
- **Verify:** `check-integrity.sh` green, `skills-ref validate` (or equivalent) clean,
  spine checked against every ledger ruling it touches.

## Runbooks

| Task | Runbook |
| --- | --- |
| Bring a file in from an upstream | `runbooks/lift.md` |
| An upstream changed a vendored file | `runbooks/re-lift.md` |
| A distilled file's source changed, or the distillation needs work | `runbooks/distill-refresh.md` |
| Sources contradict, or a ruling needs to change | `runbooks/new-ruling.md` |
| CI integrity check is red | `runbooks/integrity-failure.md` |
| Install/refresh the purchased course files locally | `runbooks/course-dropin.md` |
| Evaluate a new upstream or add a skill to the kit | `runbooks/new-skill.md` |

## Division of labor — never blur it

**LLMs propose** (grade, classify drift, author spines, draft PRs) ·
**hashes verify** (`check-integrity.sh`, in CI on every push) ·
**humans merge** (nothing you produce lands on main without review).
Your token stream is never the channel vendored prose travels through.
