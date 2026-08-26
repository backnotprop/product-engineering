# Variation axes and the floor

The picker implementation is `picker.md`; this file governs what enters it.

## One primary axis

Pick **one primary axis** and give each variant a different position on it. Secondary
choices follow from it rather than varying on their own — a dense variant may need a
smaller type step, and that is coherence, not a second axis. Varying every axis at
once produces three unattributable results: you learn which you liked, not what made
it work, so the next piece starts from nothing. If two variants differ only in accent
color or copy, move one to a different position on the primary axis or cut it.

## The floor every variant clears

A variant that wins on looks and fails an accessibility check is not a candidate — it
is a bug with a nice surface. Before a variant enters the picker: every control has an
accessible name, keyboard reaches everything a pointer does, focus is visible, nothing
clips at 320px, and no meaning rides on color alone. The floor is identical across
variants; it is not an axis and never trades against one. Where a direction can only
work by breaking it, say so and drop the direction. (The pe-review skill's engine
escalation triggers are the authoritative list.)

## Named URL params

Select variants with a named search param — `?variant=quiet`, not `?v=2` — so every
variant is a self-describing link you can send someone. Apply this on top of
`picker.md`'s wiring, whose engineering (keyboard, replay, reduced-motion) stands.
