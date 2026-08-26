# Generated-system mode

Distilled from Leonxlnx/taste-skill `stitch-skill` (see MANIFEST for the pin).
Salvage contract: the taste dials as Overview fields, the anti-pattern ban list, and
the chosen-not-observed discipline. Use this mode when a greenfield project has no
system to document and the user wants a DESIGN.md generated from a chosen direction.
The schema and validation gates from `index.md` and `url-and-validation.md` apply
unchanged — this mode changes only where values come from.

## Chosen, never observed

Every value in a generated DESIGN.md is a decision, not evidence. Label the document
as a generated system (in the Overview) so downstream agents and future refreshes know
nothing here was extracted from an implementation. When the project later ships real
UI, refresh in documented mode and reconcile — decisions that didn't survive contact
with the build are updated, not defended.

## The taste dials (record in the Overview)

State the chosen position on each spectrum so the direction is explicit and revisable:

- **Density:** "Art Gallery Airy" (1–3) → "Daily App Balanced" (4–7) → "Cockpit Dense" (8–10)
- **Variance:** "Predictable Symmetric" (1–3) → "Offset Asymmetric" (4–7) → "Artsy Chaotic" (8–10)
- **Motion:** "Static Restrained" (1–3) → "Fluid CSS" (4–7) → "Cinematic Choreography" (8–10)

Derive the positions from the brief (the direct mode's design read), not from a
default; write one line of rationale per dial.

## Ban list for generated values

A generated system must not encode the AI-default look. Do not write into DESIGN.md:

- pure black (`#000000`) grounds, neon/outer-glow shadows, oversaturated accents
- generic default serifs (Times New Roman, Georgia, Garamond) as system faces
- three-equal-column card layouts as the canonical grid
- fake round numbers in example content (`99.99%`, `50%`) — use organic data (`47.2%`)
- AI copywriting clichés ("Elevate", "Seamless", "Unleash", "Next-Gen") in voice rules
- filler UI text patterns ("Scroll to explore", bouncing chevrons) as sanctioned components
- `h-screen` for full-height sections — specify `min-h-[100dvh]` (iOS Safari jump)

The full anti-generic vocabulary lives in `../direct/slop-tells.md`; this list is only
what must be kept out of the *document*.
