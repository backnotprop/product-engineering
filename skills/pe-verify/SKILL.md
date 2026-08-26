---
name: pe-verify
description: Prove that behavior works, with evidence. Use after a feature is built ("verify this", "create a verification for the toolbar") or to re-run the project's QA list before a release ("run the QA list", "release check"). Classifies each check as code, browser, or mixed; drives the product with Playwright, recording video and checkpoint screenshots; writes one report.json and renders it into a branded HTML report with a checkpoint video player. Triggers on verify, verification, "does it work", "prove it works", QA, QA list, release check, smoke test, regression check. Read-only toward product code — reports pass, fail, flag, or skipped; fixes go to pe-build, and judgment of design quality is pe-review.
license: Apache-2.0
metadata:
  provenance: foundry/derivations/verify.md in the source repository
---

# Verify

Proof that behavior works. This spine routes; the report contract, the QA-list
conventions, and the capture method live in `references/` — load what the run needs.

## Contract (both modes)

- **Read-only toward product code.** A failed check is reported, never fixed here; hand
  it to the pe-build skill by name. The only repo write this skill ever makes is the
  user's QA list, and only when the user asks to seed or edit it.
- **Everything a run produces lands in a temp folder**: `pe-verify/<repo>/<YYYY-MM-DD-HHMM>/`
  under the system temp directory (`$TMPDIR`, else `/tmp`) — JSON, HTML, recordings,
  screenshots. Never inside the repo, never committed. Copy
  `report.json` into `.product/runs/` only on an explicit request.
- **One JSON file is the deliverable.** Never write HTML. This skill's
  `scripts/render-report.py` turns `report.json` into `report.html` beside it; validate
  first, render, then open it (`--open`) and print the path. The contract is
  `references/report-schema.md`.
- **Evidence or it is not a finding.** Every fail and flag carries a `file:line`, a
  recording timestamp, or the command that showed it.
- **A missing browser skips, never blocks.** The orchestrator checks for a browser once,
  in Scope, and may offer the install there; workers never prompt. Browser items without
  a browser report `skipped` with the reason; code items still run.

## Modes

| Mode | When | Load |
| --- | --- | --- |
| **feature** | "Verify this", "create a verification for X", or the last step after a build. The checks come from the change and the conversation: what was built, what the user said it must do, what it must not break. | `report-schema.md`, `evidence.md` |
| **list** | "Run the QA list", "release check", "QA". The user's own markdown list, found under `.product/`; one report item per list entry. | `qa-list.md`, `report-schema.md`, `evidence.md` |

A feature run is one item: the feature, with its checks as checkpoints (browser) and
findings (code), and one verdict. When the derived checks need separate verdicts —
three independent behaviors, each able to fail on its own — run a list-mode report
with `list_source: null` and the feature as the title.

## Classify every check

Decide per item, at run time. A list entry may carry a hint ("— browser"); most do not.

- **code** — read, trace, run tests or commands; no browser. "Bun is still pinned to
  1.3.x", "no config-breaking changes in this release", "the install script still
  targets both paths".
- **browser** — Playwright drives the product and records it. "Annotating HTML works
  headlessly", "every toolbar button is present", "the diff loads on a 2MB file".
- **mixed** — both: a behavior in the browser plus the code path behind it.

Bias is liberal: run any check plausibly relevant to the change. Skip only for a
reason, and put the reason in the item's `summary`.

## Orchestrate with what exists

Use the running harness as it is: parallel subagents when they exist, a cheaper model
for quick code checks and a stronger one for browser or multi-step checks where the
choice exists, sequential execution when nothing else is available. Never require a
specific harness, model, or workflow engine. Each worker returns its item as a JSON
fragment shaped by the contract; the orchestrator assembles `report.json`, sets
`checked_by` on each item, validates, renders.

## Steps

1. **Scope.** Name the mode, the target (a feature, or the list and its path), the
   commit, and how the product will be reached (local server, built artifact, CLI).
   Check that Playwright has a browser; when it does not, offer
   `npx playwright install chromium` in one line and continue with whatever answer
   comes — no answer means browser items skip.
2. **Classify** each check as above.
3. **Run.** Browser items per `references/evidence.md`: a recording, three to six
   checkpoints with stills, one-line narration each. Code items: the command or the
   trace, captured as evidence.
4. **Assemble** `report.json` in the run folder, then, with `<skill>` as this skill's
   installed folder and `<run>` as the run folder:
   `python3 <skill>/scripts/validate-report.py <run>/report.json` — fix every listed
   problem — then `python3 <skill>/scripts/render-report.py <run>/report.json --open`.
5. **Report in chat:** the path, counts by status, and one line per fail or flag. Fails
   go to **pe-build** with their evidence.

## Handoffs

Fixes → **pe-build**. Judgment of quality — does it look right, is the motion good, is
it accessible — → **pe-review**. Whether the build matches the approved mock →
**pe-review**, fidelity mode. Documenting the behavior that was verified →
**pe-product-description**.
