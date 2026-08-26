# Generated-system mode

Use this mode when a greenfield project has no system to document and the user
wants a DESIGN.md generated from a chosen direction. The schema and validation
gates from `index.md` and `url-and-validation.md` apply unchanged — this mode
changes only where values come from.

## Chosen, never observed

Every value in a generated DESIGN.md is a decision, not evidence. Label the document
as a generated system (in the Overview) so downstream agents and future refreshes know
nothing here was extracted from an implementation. When the project later ships real
UI, refresh in documented mode and reconcile — decisions that didn't survive contact
with the build are updated, not defended.

## The taste dials (record in the Overview)

State the chosen position on each of the four spectrums so the direction is explicit
and revisable:

- **Creativity:** 1 = ultra-minimal, Swiss, silent, monochrome → 5 = balanced, clean
  with personality → 10 = expressive, editorial, bold typography experiments, strong
  asymmetry
- **Density:** 1 = gallery-airy, massive whitespace → 5 = balanced sections → 10 =
  cockpit-dense, data-heavy
- **Variance:** 1 = predictable, symmetric grids → 5 = subtle offsets → 10 = artsy
  chaotic, no two sections alike
- **Motion Intent:** 1 = static, no animation noted → 5 = subtle hover/entrance cues
  → 10 = cinematic orchestration noted per component

Derive the positions from the brief, not from a default; write one line of rationale
per dial.

## Ban list for generated values

A generated system must not encode the AI-default look. Do not write into DESIGN.md:

- pure black (`#000000`) grounds, neon/outer-glow shadows, oversaturated accents
- generic default serifs (Times New Roman, Georgia, Garamond) as system faces
- three-equal-column card layouts as the canonical grid
- fake round numbers in example content (`99.99%`, `50%`)
- AI copywriting clichés ("Elevate", "Seamless", "Unleash", "Next-Gen") in voice rules
- filler UI text patterns ("Scroll to explore", bouncing chevrons) as sanctioned components
- `h-screen` for full-height sections — specify `min-h-[100dvh]` (iOS Safari jump)

The full anti-generic vocabulary lives in `../direct/slop-tells.md`; this list is only
what must be kept out of the *document*.
