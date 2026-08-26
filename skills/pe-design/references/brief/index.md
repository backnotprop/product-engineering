# Brief (one feature, before code)

Discover what should be made and how it should work, then return a confirmed design
brief — without writing code. Scope is a single feature, surface, or flow;
whole-product durable context belongs to understand mode.

## Discovery interview

Do not write code or choose visual direction yet.

Cadence: ask two or three related questions per round, then wait. One round is the
default; add a second only when the answers expose a material gap. Never dump a
questionnaire, repeat settled facts, or turn obvious facts into menus — assert the
likely reading and invite correction. A sparse prompt requires at least one answer
round; a precise prompt may need only a compact confirmation. Read `PRODUCT.md` and
`DESIGN.md` first when they exist and skip everything they already settle; proceed
from repository evidence and the user's answers when they don't.

**Round 1 — purpose, people, outcome.** Choose the two or three questions that most
change the result:

- What is this surface or feature for, and what problem must it solve?
- Who specifically reaches it, in what situation and state of mind?
- What is the primary thing they must understand or do, and what does success look
  like?
- What is uniquely true here that a neighboring product or generic template could
  not claim?

Frame by the surface's job where it sharpens the questions: **persuade** (who must
act, what they should believe, what real proof earns it) · **operate** (the task,
its states, frequency, constraints) · **read** (the reader's question, the source
material, structure, wayfinding) · **experience** (what leads, how exploration unfolds).

**Round 2 — material, behavior, boundaries.** Run only for material unresolved
decisions:

- What real content, evidence, data, and assets must the experience carry — with
  realistic minimum, typical, and maximum ranges?
- Which states and transitions matter: first-run, empty, loading, error, success,
  permissions, overflow, expert use?
- What fidelity, breadth, and interactivity is intended: exploration,
  production-ready screen, full flow, broader surface?
- What must remain untouched, and what would make the result feel wrong even if it
  looked polished?
- Which platform, framework, performance, accessibility, localization, or delivery
  constraints are binding?

Never ask for CSS values or canned aesthetic lanes.

## Visual direction, only if unresolved

First decide what is already true:

- **Redesign** — preserve product truth, content, function, constraints, and
  explicit brand commitments; the old visual world is replaced, not polished. The
  old look is evidence of what the subject is, not authority over what it becomes.
  Direction is materially unresolved.
- **Established world** — a coherent identity exists in code or `DESIGN.md`: inherit
  it; the brief records it as settled.
- **Incomplete brand** — preserve confirmed assets and recognizable traits; note
  what the brief leaves open.
- **No visual authority** — direction is materially unresolved.

A section, component, or state inside an established surface inherits that surface —
never turn a local addition into an identity exercise.

Where direction is materially unresolved, run direct mode (`../direct/index.md`) to
choose it, then return here and record the selection. This file never chooses
direction itself.

## Write the brief

Write the smallest useful brief:

1. **Job and audience** — who arrives, their context, need, and mode.
2. **Outcome and proof** — primary task or action, success, real evidence,
   product-specific truth.
3. **Selected direction** — visual authority, structural and interaction thesis,
   sequence, focal moment, implementation consequence.
4. **Scope and boundaries** — fidelity, breadth, interactivity, the named target,
   what remains untouched, explicit anti-goals.
5. **States and ranges** — realistic content and data ranges, material states.
6. **Interaction and layout** — hierarchy, topology, responsiveness, affordances,
   feedback, transitions; intent, not CSS.
7. **Constraints and open decisions** — platform, delivery, accessibility,
   localization, reusable components, and choices a builder must not invent.

Use three to five bullets when the task is settled; use the full structure only for
ambiguous, multi-screen, or standalone planning. Do not restate the conversation.

## Confirm and stop

Present the brief in chat for explicit confirmation or one correction round, then
stop — no implementation, no code. Write the brief to a file only when the user asks,
wherever they say; there is no required format or storage. When no answer mechanism
exists, mark assumptions plainly, return the brief, and stop.
