---
colors:
  ground:
    dark: "#101114"
    darkHigh: "#23252B"
    light: "#FFFFFF"
    lightLow: "#F1F1EF"
  text:
    onDark: "#F5F5F4"
    onDarkMuted: "#8B8D94"
    onDarkFaint: "#5C5E66"
    onLight: "#1A1B1E"
    onLightMuted: "#71737A"
  line:
    light: "#E8E8E6"
typography:
  display:
    fontFamily: Geist
    fontWeight: 600
    letterSpacing: "-0.03em"
  body:
    fontFamily: Geist
    fontWeight: 400
  meta:
    fontFamily: Geist Mono
    fontWeight: 400
---

# Design System: product-engineering

## Overview

This is a **generated system** (chosen, not observed) — selected 2026-08-26 from a
variant round; no prior implementation existed. Dials: Creativity 3 (type set well,
nothing else), Density 2 (generous space), Variance 1 (one repeating card pattern),
Motion 1 (static assets). Rationale: the repo's subject is restraint enforced by
process; the brand demonstrates it.

The brand is text, a quiet gradient, and space. There is no logo mark; the lowercase
wordmark "product engineering" set in Geist 600 is the identity.

## Colors

Dark ground is a radial gradient `#101114 → #23252B` from the top-left, read as a
light source, not a color. Light ground is `#FFFFFF → #F1F1EF` vertical with a
1px `#E8E8E6` border. Text steps: primary / muted / faint per frontmatter. There is
no accent color; if one is ever needed it is a single muted blue for links only.

## Typography

Wordmark and headlines: Geist 600, tracking −0.03em, lowercase. Body: Geist 400.
Names, modes, metadata: Geist Mono. In file-consumed SVG (GitHub embeds), webfonts do
not load; assets declare the fallback stack
`Geist, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif` (and the
ui-monospace stack for mono) and are designed to hold up in the fallback.

## Components

The card is the one component. Pattern, top to bottom: mono skill name (faint) ·
the verb headline (Geist 600 — "Design it.", "Build it.", "Judge it.") · one factual
sentence (muted) · mode list in mono at the base (faint). Dark linear gradient ground `#1D1F24 → #121316`. 600×320 for
skill cards; heroes are 1200-wide.

## Do's and Don'ts

- Do set the wordmark lowercase; never uppercase, never a logo mark.
- Do keep gradients subtle enough to read as lighting.
- Don't add decoration, icons, illustrations, or borders on dark cards.
- Don't introduce an accent color into assets.
- The verb headlines ("Design it.") are the chosen voice and stay. Sentences state
  what the skill delivers, positively ("Prioritized findings on any screen, diff,
  or PR.") — no caveats, no negative definitions, no contrasts, no stacked
  fragments. Boundaries live in the skills, never in the copy.
