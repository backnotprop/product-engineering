---
name: review
description: Read-only review of existing UI with verdicts. Use to critique a screen, site, or screenshot; review a diff, branch, or PR for interface quality; produce a prioritized audit with implementation plans for another agent; check code against the Web Interface Guidelines; stress-test a component in hostile states; review animation and motion craft; or audit accessibility. Triggers on review, critique, audit, UX review, design review, interface review, "review my PR", "check accessibility", "will this survive", "review the animations". Produces findings and verdicts only — never edits code.
license: Apache-2.0
metadata:
  provenance: Converged from jakubkrehel/skills (engine, change, stress), our legacy ui-review (screen), ibelick/ui-skills (audit method, a11y order), emilkowalski/skills (motion), and vercel-labs/web-interface-guidelines (guidelines) — see foundry/derivations/review.md
---

# Review

Read-only judgment of existing UI. This spine routes; the judgment lives in the
reference files, which are preserved from their authors — load only what the mode needs.

## Contract (all modes)

- **Read-only.** Never edit product code, even for a one-character fix. Findings name
  the change; applying it is the build skill's job — hand off by name.
- **Engine rules govern every mode.** Read `references/engine.md` first, always: the
  evidence bar ("a check you cannot run is Not verified, never a finding"), the
  escalation triggers, the cheaper-fix ladder, consolidation, and the verdict format
  in `references/review-format.md`.
- **Severity** is HIGH / MEDIUM / LOW plus the engine's escalation triggers.
  Accessibility findings are never discarded or deferred (ruling L-09).

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
"fix the animation" is not this skill at all (build). A request that mixes modes runs
the engine once and consolidates, never two parallel reviews.

## Name mapping for lifted texts

The engine and change references route to their author's `better-*` skills by name.
In this kit those names resolve as follows — apply the mapping silently:

| Text says | Use |
| --- | --- |
| better-accessibility | `a11y-audit.md` for ordering; the engine's own triggers for severity; the build skill's accessibility references for depth, once present |
| better-ui, better-layout, better-typography, better-colors, better-writing | the build skill's craft references once present; until then, engine judgment plus `web-interface-guidelines.md` |
| better-interface | this skill's engine mode itself |

## Rulings applied here

- **L-09** — a11y findings are never discarded; `audit-method.md` ships with its
  discard rule and finding cap cut (see its patch).
- **L-11** — `web-interface-guidelines.md` ships with house-taste rows cut; the
  autocomplete rule stands as: autocomplete on purposeful fields, `off` only for
  non-auth-sensitive cases.
- P0–P3 appears only inside screen mode's rubrics; report severity as HIGH/MED/LOW
  (P0+P1 → HIGH, P2 → MEDIUM, P3 → LOW).

## Handoffs

Fixes → **build** (findings include exact file:line and the named change).
Documenting the system a review revealed → **design**, understand mode.
Never resolve a finding by editing anything yourself.
