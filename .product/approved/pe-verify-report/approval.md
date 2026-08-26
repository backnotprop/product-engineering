# Approved: pe-verify report

**Approved:** 2026-08-26, by ramos, in the session that produced issues #37 and #38.
**Artifact:** `report-prototype.html` (v3). Open it; keys 1–2 switch layout, L/F switch run mode.
**Source:** `source/template.html` + `source/media.json` (the prototype's renderer and embedded sample media; the real template is derived from `template.html`).

## The approved state

- **List run: Ledger layout.** One column; rows expand in place; failed rows open on load; "Needs attention" block above the list jumps to fails and flags.
- **Status filters are the summary pills** (top right): all · fail · flag · pass · skipped, toggleable, with counts. No separate status chip row.
- **Secondary filter row:** "showing X of Y" · type chips (browser / code / mixed) · search (`/`).
- **Jump palette** (`J` or the floating button): search + the same status filters + arrow/enter navigation. `N` / `P` step through fails and flags. Nothing is permanently pinned to the viewport.
- **Feature run: first-look viewer.** Recording full width; checkpoint storyboard (stills with labels and times, click to seek) directly beneath; findings and screenshots below in two columns.
- **Checkpoint player:** custom progress bar with checkpoint ticks; hovering near a tick shows that checkpoint's screenshot, label, and time; click seeks; the checkpoint list carries narration and highlights live; `←`/`→` jump checkpoints, space plays.
- **Brand:** DESIGN.md — dark radial ground, Geist / Geist Mono, no accent; status colors in their own lane (pass #3FB950, fail #F0616B, flag #E2B53E, skipped #6B7078).

## Decisions on the way

- Dossier layout: rejected (long-document form didn't earn its place once palette + N/P existed).
- Inspector layout: still present in the prototype as an alternative; not yet ruled in or out for the real template.
- Separate status chip row: rejected as redundant with the summary pills; merged.
- No framework, no CDN: the whole renderer is plain HTML/CSS/JS; media lives beside the report as files.

## Out of scope for this approval

The render script, the JSON contract's final field names, mp4 conversion, and where the temp folder lives — all per issue #37, to be built against this artifact.
