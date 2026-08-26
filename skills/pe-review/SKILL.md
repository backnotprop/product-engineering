---
name: pe-review
description: Read-only review of existing UI with verdicts. Use to critique a screen, site, or screenshot; review a diff, branch, or PR for interface quality; produce a prioritized audit with implementation plans for another agent; check code against the Web Interface Guidelines; stress-test a component in hostile states; review animation and motion craft; or audit accessibility. Triggers on review, critique, audit, UX review, design review, interface review, "review my PR", "check accessibility", "will this survive", "review the animations". Produces findings and verdicts only — never edits code.
license: Apache-2.0
metadata:
  provenance: foundry/derivations/review.md in the source repository
---

# Review

Read-only judgment of existing UI. This spine routes; the judgment lives in the
reference files — load only what the mode needs.

## Contract (all modes)

- **Read-only.** Never edit product code, even for a one-character fix. Findings name
  the change; applying it is the pe-build skill's job — hand off by name.
- **Engine rules govern every mode.** Read `references/engine.md` first, always: its
  evidence bar, escalation triggers, cheaper-fix ladder, consolidation, and the
  verdict format in `references/review-format.md`.
- **Severity** is HIGH / MEDIUM / LOW plus the engine's escalation triggers.
  Accessibility findings are never discarded.

## Modes

| Mode | When | Load |
| --- | --- | --- |
| **change** | A diff, branch, PR, or "review my changes" is named. Always wins over screen when both could apply. | `change-review.md`, `scope-resolution.md`, `removed-signals.md` |
| **screen** | A screen, page, site, or screenshot; "review this UI." | `screen-review.md`, `experience-rubric.md`, `technical-rubric.md` |
| **plans** | "Audit this and give me a roadmap" — findings become self-contained plans another agent executes. Explicit invocation only. | `audit-method.md`, `plan-template.md` |
| **guidelines** | "Check against best practices / the guidelines"; terse file:line lint of UI code. | `web-interface-guidelines.md` |
| **stress** | "Does this component survive?" — render one component in every hostile state. Explicit invocation only. | `stress.md`, `stress-scenarios.md` |
| **motion** | "Review the animations / motion." For a whole-codebase motion audit with plans, add `motion-audit.md` + `motion-audit-signals.md` + `plan-template.md`. | `motion-review.md`, `motion-standards.md` |
| **opportunities** | "What could be animated here?" — read-only; proposes motion with exact values, never implements. Explicit invocation only. | `motion-opportunities.md` |
| **a11y** | "Is this accessible?" — audit, not implementation. | `a11y-audit.md` (+ engine triggers) |

Disambiguation: **verb beats noun** — "review the animation" is motion mode here;
"fix the animation" is not this skill at all (pe-build). A request that mixes modes runs
the engine once and consolidates, never two parallel reviews.

## Name mapping

Some references route to skills by name. Those names resolve as follows — apply the
mapping silently:

| Text says | Use |
| --- | --- |
| better-accessibility | `a11y-audit.md` for ordering; the engine's own triggers for severity; the pe-build skill's `references/a11y/` for depth |
| better-ui, better-layout, better-typography, better-colors, better-writing | the pe-build skill's `references/craft/{ui,layout,typography,colors,writing}/` |
| better-interface | this skill's engine mode itself |

## House rules

- Autocomplete: on for purposeful fields; `off` only for non-auth-sensitive cases.
- P0–P3 appears only inside screen mode's files; report severity as HIGH/MED/LOW
  (P0+P1 → HIGH, P2 → MEDIUM, P3 → LOW).

## Handoffs

Fixes → **pe-build** (findings include exact file:line and the named change).
Documenting the system a review revealed → **pe-design**, understand mode.
Never resolve a finding by editing anything yourself.
