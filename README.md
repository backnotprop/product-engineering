# product-engineering

Five agent skills covering the end-to-end product design process, converged from the
best published design-engineering skill work — with the source prose preserved
**byte-for-byte** and proven by hashes.

| Skill | The deliverable | Modes |
| --- | --- | --- |
| `pe-design` | documents & artifacts, before code | understand · direct · mock · vary · onboard |
| `pe-build` | production UI code | craft · motion · a11y · harden |
| `pe-review` | read-only findings & verdicts | change · screen · plans · guidelines · stress · motion · opportunities · a11y |
| `pe-product-description` | a behavior-spec repo | (Steve Ruiz's skill, vendored whole) |
| `pe-brand-assets` | standalone on-brand assets (SVG-first) | — |

Each skill is a thin router over reference files preserved from graded sources —
Emil Kowalski, Jakub Krehel, Julien Thibeaut, Vercel, Leon, plannotator, Steve Ruiz,
Impeccable (see NOTICE).

## Install

```bash
npx skills add backnotprop/product-engineering            # all five
npx skills add backnotprop/product-engineering --skill pe-review
```

## Using the skills

Install once; the skills trigger on what you ask for, or invoke one by name. Each
skill routes your request to the right mode from your words — the map below is the
product-development journey end to end.

**Starting something, or taming an existing codebase**
- "Document our product and design system" → `pe-design` writes `PRODUCT.md` and
  `DESIGN.md` from repo evidence (or from a public URL). Greenfield with no system
  yet? It generates one and labels it chosen, not observed.
- "How should this look and feel?" → `pe-design` derives a creative direction from your
  subject — palette, type, register — and checks it against the AI-slop tells.

**Shaping the thing before code**
- "Wireframe the settings flow" / "mock up the dashboard" → `pe-design` builds
  self-contained HTML at the right fidelity: wireframe → mockup → prototype
  (plus diagrams and plans).
- "Show me three takes on this card" → `pe-design` renders genuinely different variants
  behind a picker in your real page; promote the winner, the harness deletes itself.
- "Users bail during setup" → `pe-design` works the activation flow: empty states,
  checklists, the lightest pattern that teaches.

**Writing the code**
- "Build the pricing card" / "polish this, it feels off" → `pe-build` at the craft bar:
  spacing, type, color, copy, icons, interaction states.
- "Animate the drawer" / "this feels janky" → `pe-build`'s motion mode.
- "Make this table keyboard-accessible" → `pe-build`'s a11y mode.
- "Get this ready for production" → `pe-build`'s harden mode: real data extremes,
  failure states, devices, languages, offline, shipping metadata.

**Judging what exists** (read-only — findings, never edits)
- "Review my PR" → `pe-review` scopes to the diff and classifies introduced vs
  pre-existing.
- "Review this screen" → the full two-pass critique with scored rubrics.
- "Audit the app, give me a roadmap" → prioritized findings as self-contained plans
  another agent can execute.
- "Check against best practices" / "will this component survive real data?" /
  "review the animations" / "is this accessible?" → each a mode of `pe-review`.

**The two specialists**
- "Write a product description for the editor" → `pe-product-description` builds a
  behavior-spec repo: what users see, what they can do, what exactly happens —
  verified against the running product.
- "Make an SVG header image for this post" / "repo social image" / "logo concepts"
  → `pe-brand-assets` reads your brand truth first (it refuses to invent it) and
  authors on-brand SVG, exporting PNG where destinations require it.

The skills hand off to each other by name — a review's findings go to build, a
winning variant goes to build, build's hardening gates verify through review — so
you can enter the loop at any stage.

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
