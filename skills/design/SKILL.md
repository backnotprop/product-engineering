---
name: design
description: Design-process work before production code. Use to capture product and design-system context (PRODUCT.md / DESIGN.md), set creative direction and taste, build wireframes / mockups / prototypes / diagrams / plans as self-contained HTML, render competing variations of a UI piece behind a picker, or design onboarding and first-run flows. Triggers on design, direction, "how should this look/feel", wireframe, mockup, prototype, mock this up, diagram, "document our design system", DESIGN.md, "show me versions/variations", onboarding, empty states, first-run. The deliverable is a document or artifact — not production code (build) and not a verdict on existing UI (review).
license: Apache-2.0
metadata:
  provenance: Converged from our legacy project-context and ui-onboarding, plannotator/effective-html, emilkowalski/skills (prototype), jakubkrehel/skills (variant), ibelick/ui-skills (create-design-md), and Leonxlnx/taste-skill — see foundry/derivations/design.md
---

# Design

Everything before production code. This spine routes; the craft lives in the reference
files, preserved from their authors — load only what the mode needs.

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

## Modes

| Mode | When | Load from `references/` |
| --- | --- | --- |
| **understand** | "Document our product / design system", DESIGN.md work | `understand/index.md`; `understand/design-format.md` + `understand/templates.md` for the schema; `understand/url-and-validation.md` for public-URL extraction and the lint/export gates; `understand/generated-mode.md` for greenfield systems |
| **direct** | "How should this look / feel", creative direction, a register or palette decision | `direct/index.md`; check every visual choice against `direct/slop-tells.md`; `direct/presets/` only on explicit match |
| **mock** | Wireframe, mockup, prototype, diagram, or plan as an HTML artifact | `mock/index.md` (the router), then the fidelity file it names: `wireframe.md`, `prototype.md`, `diagram.md`, `plan.md`; shared craft in `charts-and-data.md`, `diagrams.md`, `documents-and-presentations.md`, `interfaces.md` |
| **vary** | "Show me N versions", compare directions in the real page | `vary/index.md` + `vary/picker.md` (the engineered picker), governed by `vary/axes.md` (one primary axis; the accessibility floor; `?variant=name` URLs) |
| **onboard** | First-run, activation, setup, empty states, tours | `onboard/index.md` + `onboard/patterns.md` |

Disambiguation: a mockup of something new is **mock**; N takes on one existing piece
is **vary**. "Make it look better" on shipped UI is not this skill (build). A named
diff/branch/PR is never this skill (review).

## Name mapping for lifted texts

`mock/index.md` routes to its sibling skills by name (html-wireframe, html-prototype,
html-diagram, html-plan, design-artifact): resolve to this skill's `mock/wireframe.md`,
`mock/prototype.md`, `mock/diagram.md`, `mock/plan.md`, and `direct/index.md`
respectively. Its reference to a bundled `creative-direction.md` fallback resolves to
`direct/index.md` (the fallback was deliberately not carried — one owner). Mentions of
jakub's `better-*` skills resolve per the build skill's mapping; `better-interface`
checks are the review skill.

## Rulings applied here

- **L-10** (motivated motion) — the premium-dark-glass preset ships with its
  never-static mandates cut (see its patch); no artifact animates without a reason.
- The prescriptive-vs-derivational conflict is settled as this skill's contract:
  derive by default, presets by explicit commission.

## Handoffs

Implementing a chosen direction, mock, or winning variant → **build** (with the
DESIGN.md and any chosen preset named). Judging existing UI → **review**. Behavior
specs beyond PRODUCT.md's scope → **product-description**. On-brand standalone assets
→ **brand-assets** (once present).
