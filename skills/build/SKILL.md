---
name: build
description: Write and refine production UI code to a high craft bar. Use for building components, polish and detail work (spacing, typography, color, copy, icons, shadows, interaction states), implementing animation and gestures, implementing accessibility (keyboard, screen readers, focus, forms), and hardening for production (real data, failure states, devices, languages, offline, shipping metadata). Triggers on build, implement, polish, refine, tighten, "feels off", animate, transition, gesture, drawer, make accessible, keyboard navigation, production-ready, edge cases, empty states. The deliverable is code. Not for read-only critique (review) or pre-code design work (design).
license: Apache-2.0
metadata:
  provenance: Converged from emilkowalski/skills, jakubkrehel/skills (better-* domain fold), ibelick/ui-skills, vercel-labs/agent-skills, Leonxlnx/taste-skill, and our legacy ui-polish/ui-harden — see foundry/derivations/build.md
---

# Build

Production UI to the craft bar. This spine routes and carries the shared loop; the
craft itself lives in the reference files, preserved from their authors — load only
what the mode needs.

## The loop (every mode)

1. **Boundary** — name the exact target, what must remain unchanged, and the surface's
   job (persuade / operate / read / experience); read `DESIGN.md` when present and
   verify it against tokens, components, and rendered output. Preserve the incumbent
   identity: polish is refinement, never a concealed redesign.
2. **Evidence** — read the real code and, where possible, the rendered result before
   changing anything.
3. **Triage** — fix in order: blocked tasks and inaccessible paths → missing states
   and recovery → flow, hierarchy, responsiveness, drift → visual/copy/motion
   inconsistencies → cleanup. Don't perfect one corner while the path stays below bar.
4. **Implement** — complete fixes, in the project's stack and idiom.
5. **Verify** — walk the whole path; check states, viewports, zoom, focus, semantics,
   console, layout shift. At most two bounded visual rounds — no open-ended loop.
6. **Report** — what changed, what was preserved, what remains.

## Modes

| Mode | When | Load from `references/` |
| --- | --- | --- |
| **craft** (default) | Components, polish, detail work, "feels off" | `craft/emil-craft.md` for the canon; the domain folders as the work touches them: `craft/ui/` (details: surfaces, icons, enter/exit), `craft/layout/`, `craft/typography/`, `craft/colors/`, `craft/writing/` (each has `index.md`); `craft/polish-lenses.md` for trade-offs; `craft/library-choices.md` before adding a dependency |
| **motion** | Animate, transition, gesture, "feels janky" | `motion/build.md` + `motion/recipes.md`; `motion/apple-design.md` for gesture physics and fluid interfaces; `motion/view-transitions/` for React's View Transition API; `motion/perf-additions.md`; `motion/vocabulary.md` to name an effect |
| **a11y** | Make accessible, keyboard, screen reader, focus, forms | `a11y/index.md`, then its files per subtopic |
| **harden** | Production-ready, edge cases, real data, offline, metadata | `harden/index.md`, `harden/resilience-matrix.md`, `harden/adaptation-patterns.md`, `harden/performance-diagnostics.md`, `harden/metadata.md` |

**Generation guardrail:** when writing new UI from scratch in any mode, also load
`craft/generation-guardrails.md` (terse MUST/NEVER rules).

**Course preference:** if `references/course/` contains files, prefer them for their
topics — `craft-design-rules.md` and friends extend craft; the `motion-*` files extend
and deepen motion (CSS, Motion for React, gestures, scroll, debugging, performance,
reduced-motion snippets, and the motion-brief interview). They are a licensed local
install; never copy from them into tracked files.

## Gates

- **Redesign gate:** changing the visual identity (fonts, palette, layout language) is
  forbidden unless the user explicitly asked for a redesign. Only then load
  `craft/deslop-audit.md` and work audit-first within the existing stack.
- **Read-only requests are not this skill.** "Review/audit/critique" → hand to
  **review**. Findings received from review are implemented here at their stated
  file:line.

## Rulings (bind every mode — full text in foundry/LEDGER.md)

- L-01: press scale is exactly `0.96`.
- L-02: spring bounce `0` unless the design direction's register is explicitly playful.
- L-03: reduced motion means gentler-not-zero — keep opacity/color transitions.
- L-04: exits use ease-out; accelerate-away only as a stated deliberate choice. The
  `ease-in`-on-enter snippets in `motion/view-transitions/css-recipes.md` are upstream
  taste — use ease-out per this ruling.
- L-05: `will-change` only on observed first-frame stutter, never prophylactically.
- L-06: custom easing from the named curves in the motion references — never invent
  novel curves ad hoc.
- L-07: stagger ~30–80ms between list items, ~100ms between semantic groups.
- L-08: never disable submit buttons; validate on submit.

## Name mapping for lifted texts

References that route to `better-*` skills by name resolve inside this skill:
better-ui → `craft/ui/` · better-layout → `craft/layout/` · better-typography →
`craft/typography/` · better-colors → `craft/colors/` · better-writing →
`craft/writing/` · better-accessibility → `a11y/` · better-interface → the review
skill. Domain ownership (who decides vs who measures) follows
`foundry/ownership-matrix.md`.

## Handoffs

Verdicts and audits → **review**. Direction, mockups, variations → **design**.
Standalone brand assets → **brand-assets**. Documenting the system you built →
**design**, understand mode.
