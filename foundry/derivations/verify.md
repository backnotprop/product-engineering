# Derivation: pe-verify

The kit's sixth skill: proof that behavior works, with evidence (issue #37). Nothing
vendored — every file is authored. The gap it fills: pe-review judges the quality of
what exists; nothing in the source repos drove a product, recorded what happened, and
reported pass/fail against the user's own list of concerns.

## Sources

- Issue #37 (the spec: two entry points, check types, orchestration bias, temp-folder
  rule, JSON shape, the Plannotator 29-item release list as the reference case).
- `.product/approved/pe-verify-report/` — the approved report prototype (ledger layout,
  show-all default, checkpoint player with hover previews). The shipped template is a
  surgery on that source: prototype chrome, Inspector and Dossier layouts, and the sample
  data removed; the only additions are the deviations recorded below.

## Files

| File | Class | Note |
| --- | --- | --- |
| `SKILL.md` | authored | spine: contract, two modes, classification, orchestration, steps, handoffs |
| `references/report-schema.md` | authored | the JSON contract in prose |
| `references/qa-list.md` | authored | discovery in `.product/`, the memories file at `~/.product-engineering/memories.md`, reading and seeding the list |
| `references/evidence.md` | authored | Playwright recording, checkpoints, stills, code evidence |
| `assets/report.schema.json` | authored | the authoritative schema |
| `assets/report-template.html` | authored | derived from the approved artifact |
| `assets/sample/` | authored | a feature run with a recording and five checkpoints; the test fixture |
| `scripts/validate_report_lib.py`, `validate-report.py`, `render-report.py`, `test-render.py` | authored | validate, render (webm→mp4, `--out` rebasing, error page); the test count is printed by `test-render.py` |

## Deviations from the approved artifact

- Screenshots open in a lightbox (user direction, 2026-08-26): click or Enter on a still opens it full size in a dialog; arrow keys move within the item's screenshots; Esc closes. The approved prototype showed stills at grid size only.
- Rows start collapsed in list mode (user direction, 2026-08-26); the approved prototype opened failed rows on load. The needs-attention block stacks each finding under its title instead of beside it.
- Status `not-run` and the "selective run · basis" meta line (user direction, after
  approval): a list run is `selective` or `all`; unchosen entries stay in the ledger,
  muted, with their reason, and get their own count pill and filter. The record in
  `.product/approved/pe-verify-report/` predates this; the user's words rank above it.

## Rulings applied

- L-09 by analogy: a console error during a browser check is never dropped — `low`
  when explained, `flag` when not.
- Evidence bar (engine): every fail and flag carries a file:line, a timestamp, or a
  command.

## Ripple

Router deliverable row and the "does it work / is it good" disambiguation; pe-build and
pe-review handoffs; brand card `pe-verify.svg` ("Verify it."); hero, light hero, and
router card mode lines gain `verify`; README intro "Five" → "Six", grid, examples, index;
`skills.sh.json`; the foundry skill's own count.
