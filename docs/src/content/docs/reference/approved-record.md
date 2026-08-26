---
title: The approved record
description: What an approval under .product/approved/ holds, and how fidelity mode reads it.
sidebar:
  order: 3
---

The fidelity mode of the pe-review skill: the implementation measured against the
artifact the user approved.

## Locate the record

- Read `.product/approved/`. Each folder is one record: the approved artifact
  byte-for-byte, plus `approval.md`. Match the folder to the feature, route, or
  component under review by slug; when two could match, ask which, naming both.
- A folder named `<slug>--YYYY-MM-DD` is superseded (the pe-design skill's Approval
  rule). Review against the undated one only.
- No matching record: say so in one line, then run screen or change mode. When the user
  points at a mock that was never stamped, hand to the pe-design skill's Approval step
  first; review once the record exists.
- Where `approval.md` and the artifact disagree, `approval.md` wins. Its approved-state
  section names the layout, toggles, and filters chosen; put the artifact into that state
  before comparing, not its default state.
- Nothing listed under the record's out-of-scope section is a fidelity finding; engine
  escalation triggers still fire.
- The Scope and coverage block names the record path, the artifact file, and the
  deviation count by severity.

## Compare

Open the artifact and the implementation side by side, in the approved state, at every
viewport the artifact demonstrates, with the artifact's sample data where it embeds any.
Walk the surface in this order and record every difference as it appears:

1. **Structure** — regions present, their order, their nesting. Note what the artifact
   has that the build lacks, and what the build added.
2. **Hierarchy** — what reads first, second, third, by size, weight, contrast, and
   position. A region present but demoted is a difference.
3. **States** — every state the artifact shows or `approval.md` describes: empty,
   loading, error, hover, focus, selected, expanded, disabled, and what opens on load.
   The build must show the same states with the same transitions between them.
4. **Copy** — headings, labels, buttons, empty-state and error text, compared verbatim,
   casing and punctuation included.
5. **Spacing** — measured, not eyeballed: gaps, padding, alignment, column widths against
   the artifact's value, exact, unless the record states a tolerance.
6. **Behavior** — each interaction the artifact demonstrates or the record describes:
   keyboard shortcuts, navigation, filtering, seeking, persistence. Exercise it; a still
   frame proves nothing about behavior.

A responsive behavior the artifact lacks is not a fidelity finding; engine escalation
triggers still fire. One it shows and the build lacks is.

## Report

One finding per deviation, in the engine's verdict format, carrying: file:line, the
artifact region it maps to, what the artifact shows, what the build shows, severity,
and the named change that restores fidelity.

- **HIGH** — a region, state, or behavior in the approved state is missing or does
  something else; copy whose meaning changed.
- **MEDIUM** — hierarchy inverted or flattened; a state present but visibly different;
  a behavior that reaches the same result by another route.
- **LOW** — spacing off the artifact's value (or outside a stated tolerance); copy
  casing or punctuation; a visual detail with no effect on reading order or use.

Zero deviations is a valid outcome: state it and stop. A deviation you judge to be an
improvement is still a finding at its severity; the record stands until the user
approves a new version.

## Sanctioned deviations

A deviation the build report stated before it was made, with its reason (constraint,
platform, accessibility), is sanctioned: list it under its own heading with the reason,
no severity, no fix. A deviation present in the code and absent from the build report
is a finding at its severity, even when its reason is obvious. When a sanctioned
deviation fixes a real defect in the artifact, add one line proposing that the user
re-approve the artifact with the fix folded in.

## Handoff

Findings go to **pe-build** with file:line, the artifact region, and the named change;
pe-build implements to the record. When the user prefers the build's version, the record
is stale: hand to **pe-design** to approve a new version, which supersedes the old
record. Never edit a record, the artifact, or the code yourself.

---

Authored in the kit. Source: [skills/pe-review/references/fidelity.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/fidelity.md), rendered as-is at build time.
