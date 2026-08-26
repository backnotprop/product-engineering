# The report contract

A verification run ends with one JSON file. Nothing else the agent writes reaches the
user's screen — the renderer turns the JSON into the report, so the JSON has to be right.

## Where files go

Create a run folder in the system temp directory, never in the repo:

```
$TMPDIR/pe-verify/<repo-name>/<YYYY-MM-DD-HHMM>/
  report.json          the one file you author
  report.html          written by render-report.py
  recording-*.mp4      Playwright recordings (webm is converted when ffmpeg exists)
  cp-*.png             checkpoint stills
  shot-*.png           standalone screenshots
```

Every media path inside `report.json` is relative to that folder.

## Produce, validate, render, open

```bash
python3 <skill>/scripts/validate-report.py report.json     # fix every listed problem first
python3 <skill>/scripts/render-report.py report.json --open
```

`validate-report.py` prints `$.path: message` lines for each problem and exits 1;
`--json` gives the same as a machine-readable list. Never render a report that fails
validation: the renderer writes an error page instead of a report, and the user is told
to hand the problems back to you.

## The shape

`assets/report.schema.json` is the authoritative schema. In prose:

**Run** — `schema_version` (always `1`) · `title` · `mode` (`feature` for one item
rendered as the first-look viewer, `list` for the ledger) · `ran_at` (ISO 8601) ·
optional `repo`, `commit`, `list_source` (path of the QA list used), `notes`
(environment caveats, what could not be checked).

**Item** — `id` (stable, `[A-Za-z0-9][A-Za-z0-9_-]*`, unique in the run) · `title` ·
`check_type` (`code` · `browser` · `mixed`) · `status` (`pass` · `fail` · `flag` ·
`skipped`) · `summary` (one to three plain sentences: what was checked, the outcome) ·
optional `findings`, `media`, `checked_by`.

**Finding** — `severity` (`high` · `medium` · `low` · `info`) · `text` · optional
`evidence` (`file:line`, a recording timestamp like `recording 0:16`, or a command).

**Media** — `video` (relative path) · `checkpoints` (each: `t` seconds, ascending;
`label` ≤ 80 chars; `narration`; `screenshot` relative path) · `screenshots` (each:
`path`, `caption`). Checkpoints require a video. A code-only item has no media.

## Writing the fields

- `status` is the verdict: `pass` (verified), `fail` (verified broken), `flag`
  (needs a human decision — a suspected regression, a policy question, a risky
  change), `skipped` (could not be checked; say why in `summary`).
- `summary` states what was checked and what happened. Findings carry the specifics;
  `summary` never repeats them.
- A checkpoint is a moment worth jumping to: the thing rendered, the action landed,
  the result appeared. Three to six per recording; label each with what is visible
  at that moment, narrate in one sentence, and capture the still at that exact time.
- `checked_by` records who ran the item (`opus · browser`, `sonnet · code`) so a
  reader knows how much to trust it.
- `evidence` on a `fail` or `flag` finding is not optional in practice: a finding
  without a file:line or a timestamp cannot be acted on.

A worked example lives in `assets/sample/report.json` (a feature run with a recording
and five checkpoints); `scripts/test-render.py` exercises every rule.
