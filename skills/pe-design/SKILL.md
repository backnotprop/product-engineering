---
name: pe-design
description: Design-process work before production code. Use to capture product and design-system context (PRODUCT.md / DESIGN.md), write a design brief for one feature or flow, set creative direction and taste, build wireframes / mockups / prototypes / diagrams / plans as self-contained HTML, render competing variations of a UI piece behind a picker, or design onboarding and first-run flows. Triggers on design, design brief, "write a brief", "spec this feature", "shape this flow", direction, "how should this look/feel", wireframe, mockup, prototype, mock this up, diagram, "document our design system", DESIGN.md, "show me versions/variations", onboarding, empty states, first-run. The deliverable is a document or artifact — not production code (pe-build) and not a verdict on existing UI (pe-review).
license: Apache-2.0
metadata:
  provenance: foundry/derivations/design.md in the source repository
---

# Design

Everything before production code. This spine routes; the craft lives in the
reference files — load only what the mode needs.

## Contract (all modes)

- **Deliverables are documents and artifacts**, never production code. The one
  sanctioned codebase touch is vary mode's throwaway picker harness, removed when a
  variant is promoted.
- **Authority chain, every mode:** the user's words → the project's design system
  (DESIGN.md, tokens, components) → the subject itself → your judgment. Never let a
  preset or a habit override an upstream authority.
- **Derivation is the default; presets are commissions.** Direction comes from the
  subject and brief (`direct/index.md`). A named preset (`direct/presets/`) is used
  only when the user's direction explicitly matches it.
- **Motion in artifacts must be motivated.** If the reason doesn't fit one sentence,
  the element stays static.

## Modes

| Mode | When | Load from `references/` |
| --- | --- | --- |
| **understand** | "Document our product / design system", DESIGN.md work | `understand/index.md`; `understand/design-format.md` + `understand/templates.md` for the schema; `understand/url-and-validation.md` for public-URL extraction and the lint/export gates; `understand/generated-mode.md` for greenfield systems |
| **brief** | "Write a brief for X", "spec this feature" — planning one feature, surface, or flow before code | `brief/index.md` (runs direct mode first only when visual direction is materially unresolved) |
| **direct** | "How should this look / feel", creative direction, a register or palette decision | `direct/index.md`; check every visual choice against `direct/slop-tells.md`; `direct/presets/` only on explicit match |
| **mock** | Wireframe, mockup, prototype, diagram, or plan as an HTML artifact | `mock/index.md` (the router), then the fidelity file it names: `wireframe.md`, `prototype.md`, `diagram.md`, `plan.md`; shared craft in `charts-and-data.md`, `diagrams.md`, `documents-and-presentations.md`, `interfaces.md` |
| **vary** | "Show me N versions", compare directions in the real page | `vary/index.md` + `vary/picker.md` (the engineered picker), governed by `vary/axes.md` (one primary axis; the accessibility floor; `?variant=name` URLs) |
| **onboard** | First-run, activation, setup, empty states, tours | `onboard/index.md` + `onboard/patterns.md` |

Disambiguation: **understand** documents the whole product durably; **brief** plans one
feature, for now. A mockup of something new is **mock**; N takes on one existing piece
is **vary**. "Make it look better" on shipped UI is not this skill (pe-build). A named
diff/branch/PR is never this skill (pe-review).

## Name mapping

The mock files route to skills by name (html-wireframe, html-prototype,
html-diagram, html-plan, design-artifact — including `../design-artifact/SKILL.md`
links): resolve to this skill's `mock/wireframe.md`, `mock/prototype.md`,
`mock/diagram.md`, `mock/plan.md`, and `direct/index.md` respectively. Their relative
`references/*.md` links resolve to the same `mock/` folder. The `creative-direction.md`
fallback resolves to `direct/index.md`.

## Handoffs

Implementing a chosen direction, mock, or winning variant → **pe-build** (with the
DESIGN.md and any chosen preset named). Judging existing UI → **pe-review**. Behavior
specs beyond PRODUCT.md's scope → **pe-product-description**. On-brand
standalone assets → **pe-brand-assets**.
