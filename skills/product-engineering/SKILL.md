---
name: product-engineering
description: The front door to the product-engineering kit. Use when the user says "product engineering" followed by any product, design, UI, review, or asset request; when they ask which pe-* skill fits a task; or when a product task doesn't clearly match one skill. Routes to pe-design, pe-build, pe-review, pe-verify, pe-product-description, or pe-brand-assets and then follows that skill. If a request already names or clearly matches a specific pe-* skill, that skill takes it directly — this router yields.
license: Apache-2.0
metadata:
  provenance: foundry/derivations/product-engineering.md in the source repository
---

# Product Engineering

Route, then defer. Decide which skill owns the request, read that skill's SKILL.md,
and follow it completely. Never do the work from this file's summaries.

## Route by the deliverable

Ask what should exist when the work is done:

| The user wants | Route to |
| --- | --- |
| A document or design artifact — context docs, a design brief for one feature, a direction, wireframes, mockups, prototypes, variants, an onboarding flow | `pe-design` |
| Working production code — a component built, polished, animated, made accessible, or hardened; a UI bug fixed | `pe-build` |
| A judgment on what exists — a review, critique, audit, or stress test of a screen, diff, or PR; fidelity to an approved design | `pe-review` |
| Proof that something works — a verification run with recordings and screenshots, or the project's QA list re-checked before a release | `pe-verify` |
| A behavior spec — documentation of what users see and do, verified against the product | `pe-product-description` |
| A standalone asset — an illustration, social/OG image, or logo in the project's brand | `pe-brand-assets` |

## Disambiguation

- **Verb beats noun.** "Review the animation" → `pe-review`. "Fix the animation" →
  `pe-build`.
- **A named diff, branch, or PR** always means `pe-review`, change mode.
- **A bug in UI behavior** is code to fix → `pe-build`. If the user only wants to
  know what's wrong, not a fix → `pe-review`.
- **A spec or plan for something new** — a feature not yet built → `pe-design`, brief
  mode. **A spec of how the existing product behaves** → `pe-product-description`.
- **A mockup of something new** → `pe-design`. **N takes on one existing piece** →
  `pe-design`, vary mode.
- **"Did we match the design / mock?"** → `pe-review`, fidelity mode (checks against
  the record in `.product/approved/`). **"Make it match the mock"** → `pe-build`.
- **"Does it work?" vs "Is it good?"** Proof of behavior with evidence → `pe-verify`.
  Judgment of quality — looks, motion, accessibility — → `pe-review`. "Run the QA
  list" or "release check" is always `pe-verify`, list mode.
- Still ambiguous after that: ask one short question naming the two candidate
  skills, then proceed.

## After routing

State the choice in one line ("Routing to pe-build, motion mode"), load that skill,
and follow its contract — including its handoffs back to the other skills.
