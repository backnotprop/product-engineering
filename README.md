# product-engineering

Five agent skills covering the end-to-end product design process, converged from the
best published design-engineering skill work — with the source prose preserved
**byte-for-byte** and proven by hashes.

| Skill | The deliverable | Modes |
| --- | --- | --- |
| `design` | documents & artifacts, before code | understand · direct · mock · vary · onboard |
| `build` | production UI code | craft · motion · a11y · harden |
| `review` | read-only findings & verdicts | change · screen · plans · guidelines · stress · motion · opportunities · a11y |
| `product-description` | a behavior-spec repo | (Steve Ruiz's skill, vendored whole) |
| `brand-assets` | standalone on-brand assets (SVG-first) | — |

Each skill is a thin router over reference files preserved from graded sources —
Emil Kowalski, Jakub Krehel, Julien Thibeaut, Vercel, Leon, plannotator, Steve Ruiz,
Impeccable (see NOTICE).

## Install

```bash
npx skills add backnotprop/product-engineering            # all five
npx skills add backnotprop/product-engineering --skill review
```

## How this repo works

- **`foundry/MANIFEST.json`** records every non-authored file's upstream repo, path,
  pinned commit, and sha256. CI (`integrity.yml`) recomputes every hash on every
  push — a single reworded character in a vendored file fails the build.
- **Cuts are recorded, never silent**: files trimmed from their source
  (`verbatim-minus`) keep a pristine copy plus a `.patch` in `foundry/pristine/`;
  CI proves pristine + patch reproduces the shipped file.
- **`foundry/LEDGER.md`** holds the rulings where sources contradicted each other;
  no text in the kit may disagree with an active ruling.
- **`foundry/derivations/`** are the per-skill receipts: what was lifted, cut,
  distilled, and why. **`foundry/LOG.md`** is the append-only history.
- **`upstream-watch.yml`** runs weekly: it diffs every pinned upstream blob against
  upstream HEAD and opens an issue when authors improve something we vendored.
- Bytes enter this repo only through `foundry/scripts/lift.sh` — LLM agents working
  here never retype vendored prose (see AGENTS.md, the fence).

The animations.dev course pack is **not** in this repo — purchasers layer it locally
via `foundry/scripts/course-dropin.sh` into gitignored folders, and the build skill
prefers it when present.

## License

Apache-2.0 for this repository's own work; vendored files remain under their
authors' licenses with provenance in `foundry/MANIFEST.json` and attribution in
`NOTICE`.
