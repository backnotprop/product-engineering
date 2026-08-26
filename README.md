<img src="brand/hero.svg" alt="product engineering — five agent skills for product design and engineering" width="100%">

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

Install once. Say what you need — the right skill triggers on your words and routes
itself to the right mode. The kit follows the product journey:
**understand → shape → build → review**, plus two specialists.

### 1 · Understand the product, set the direction

| Say | Skill · mode | You get |
| --- | --- | --- |
| "Document our product and design system" | `pe-design` · understand | `PRODUCT.md` + `DESIGN.md` from repo evidence — or extracted from a public URL |
| "We're greenfield — generate a design system" | `pe-design` · understand | A generated system, labeled chosen-not-observed |
| "How should this look and feel?" | `pe-design` · direct | A creative direction derived from your subject, checked against the AI-slop tells |

### 2 · Shape it before code

| Say | Skill · mode | You get |
| --- | --- | --- |
| "Wireframe the settings flow" | `pe-design` · mock | Self-contained HTML at the right fidelity: wireframe → mockup → prototype |
| "Show me three takes on this card" | `pe-design` · vary | Genuinely different variants behind a picker in your real page; promote the winner |
| "Users bail during setup" | `pe-design` · onboard | An activation flow: empty states, checklists, the lightest pattern that teaches |

### 3 · Build it

| Say | Skill · mode | You get |
| --- | --- | --- |
| "Build the pricing card" · "polish this" | `pe-build` · craft | Production code at the craft bar: spacing, type, color, copy, states |
| "Animate the drawer" · "this feels janky" | `pe-build` · motion | Motion built to exact values, gestures included |
| "Make this table keyboard-accessible" | `pe-build` · a11y | Implemented accessibility: keyboard, screen readers, focus, forms |
| "Get this ready for production" | `pe-build` · harden | Data extremes, failure states, devices, languages, offline, metadata |

### 4 · Judge it — read-only, findings never edits

| Say | Skill · mode | You get |
| --- | --- | --- |
| "Review my PR" | `pe-review` · change | Diff-scoped review; introduced vs pre-existing, classified |
| "Review this screen" | `pe-review` · screen | The full two-pass critique with scored rubrics |
| "Audit the app, give me a roadmap" | `pe-review` · plans | Findings as self-contained plans another agent can execute |
| "Will this survive real data?" | `pe-review` · stress | The component rendered in every hostile state |

Also modes of `pe-review`: guidelines check ("check against best practices"),
animation review, a11y audit.

### Anytime · the specialists

| Say | Skill | You get |
| --- | --- | --- |
| "Write a product description for the editor" | `pe-product-description` | A behavior-spec repo — what users see, can do, and what exactly happens — verified against the running product |
| "Make an SVG header image for this post" | `pe-brand-assets` | On-brand SVG (PNG exported where destinations need it); it reads your brand truth first and refuses to invent it |

**Skills hand off by name.** A review's findings go to pe-build. A winning variant
goes to pe-build. Hardening verifies through pe-review. Enter the loop at any stage.

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

<img src="brand/credits.svg" alt="Built from the work of Emil Kowalski, Jakub Krehel, Julien Thibeaut, Vercel, Leon, Steve Ruiz, Impeccable — preserved byte-for-byte, hash-verified" width="100%">

## License

Apache-2.0 for this repository's own work; vendored files remain under their
authors' licenses with provenance in `foundry/MANIFEST.json` and attribution in
`NOTICE`.
