# The report contract

A verification run ends with one JSON file. The renderer turns it into the report;
nothing else the agent writes reaches the user's screen.

## Where files go

Create a run folder in the system temp directory (`$TMPDIR`, else `/tmp`), never in
the repo:

```
<tmp>/pe-verify/<repo-name>/<YYYY-MM-DD-HHMM>/
  report.json               the one file you author
  report.html               written by render-report.py
  recording-<item>.webm     Playwright recordings (converted to .mp4 when ffmpeg exists)
  cp-<item>-<n>.png         checkpoint stills
  shot-<item>-<n>.png       standalone screenshots
```

Every media path inside `report.json` is relative to that folder.

## Produce, validate, render, open

```bash
python3 <skill>/scripts/validate-report.py report.json     # fix every listed problem first
python3 <skill>/scripts/render-report.py report.json --open
```

`validate-report.py` prints `$.path: message` lines for each problem and exits 1
(2 when the file is unreadable); `--json` gives the same as a machine-readable list.
`render-report.py --out <path>` writes the HTML elsewhere and rewrites media paths
relative to it; the media files stay in the run folder. Never render a report that fails
validation: the renderer writes an error page instead of a report, and the user is told
to hand the problems back to you.

## The shape

`assets/report.schema.json` is the authoritative schema. In prose:

**Run** — `schema_version` (always `1`) · `title` · `mode` (`feature` for one item
rendered as the first-look viewer, `list` for the ledger) · `ran_at` (ISO 8601) ·
optional `repo`, `commit`, `list_source` (path of the QA list used), `notes`
(environment caveats, what could not be checked). List runs also carry `selection`:
`all` when every entry ran, `selective` when the agent chose entries from the change
set; a selective run adds `selection_basis` (what it chose from: `diff main...HEAD,
14 files`) and lists every unchosen entry as an item with status `not-run`.

**Item** — `id` (stable, `[A-Za-z0-9][A-Za-z0-9_-]*`, unique in the run) · `title` ·
`check_type` (`code` · `browser` · `mixed`) · `status` (`pass` · `fail` · `flag` ·
`skipped` · `not-run`) · `summary` (one to three plain sentences: what was checked, the outcome) ·
optional `findings`, `media`, `checked_by`.

**Finding** — `severity` (`high` · `medium` · `low` · `info`) · `text` · optional
`evidence` (`file:line`, a recording timestamp like `recording 0:16`, or a command).

**Media** — `video` (relative path) · `checkpoints` (each: `t` seconds, ascending;
`label` ≤ 80 chars; optional `narration`; `screenshot` relative path) · `screenshots`
(each: `path`, optional `caption`). Checkpoints require a video. A code-only item omits
the `media` key entirely (not `null`). Paths are relative, stay inside the run folder
(no `..`), and contain no quotes or angle brackets.

## Writing the fields

- `status` is the verdict: `pass` (verified), `fail` (verified broken), `flag`
  (needs a human decision — a suspected regression, a policy question, a risky
  change), `skipped` (could not be checked; say why in `summary`), `not-run` (not
  chosen in a selective run; `summary` says why in one line — "no change touches the
  install scripts"; selective runs only, no media).
- `summary` states what was checked and what happened. Findings carry the specifics;
  `summary` never repeats them.
- A checkpoint is a moment worth jumping to: the thing rendered, the action landed,
  the result appeared. Three to six per recording; label each with what is visible
  at that moment, narrate in one sentence, and capture the still at that exact time.
- For a browser item, `summary` is also the recording's overall narration: what the
  video shows from start to end.
- `checked_by` records who ran the item (`opus · browser`, `sonnet · code`) so a
  reader knows how much to trust it.
- Give every `fail` or `flag` finding an `evidence` value: a file:line, a recording
  timestamp, or the command that showed it.

A worked example lives in `assets/sample/report.json` (a feature run with a recording
and five checkpoints); `scripts/test-render.py` exercises every rule.
