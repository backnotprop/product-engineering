---
name: brand-assets
description: Create standalone visual assets that stay on brand — SVG illustrations for articles and blog posts, repo and social/OG images, logo and identity work, on-brand concept images for features. Authors SVG in code. Reads the project's brand truth (DESIGN.md, style guides, a brand/ folder) first and refuses to invent brand values. Triggers on brand asset, on-brand, SVG illustration, article image, header image, og image, social card, repo image, logo, brand kit, identity, tagline panel. Not for UI mockups (design), production components (build), or judging existing assets (review).
license: Apache-2.0
metadata:
  provenance: New spine; identity method distilled from Leonxlnx/taste-skill brandkit — see foundry/derivations/brand-assets.md
---

# Brand Assets

Standalone assets that belong to the brand, authored as SVG in code. The lookup you
used to do by hand is step one here, and it is not skippable.

## The workflow

1. **Locate brand truth — or stop.** Read, in order: `DESIGN.md` (the design skill's
   understand mode owns its format), any style guide, and a `brand/` folder (logos,
   fonts, reference assets) if present. Index what exists: palette tokens, type
   choices, radii/shape language, existing marks and motifs. If none of these exist,
   do not invent a brand — offer to run design·understand first, or proceed only with
   values the user supplies in the conversation, labeled as provisional.
2. **Derive the asset's rules.** Colors come only from the brand palette (cite the
   token names). Type in the asset is the brand's faces. Shapes follow the recorded
   shape language. The metaphor comes from the identity method (`references/
   identity-method.md`) — an asset that can't name its meaning doesn't ship.
3. **Author the SVG.** Quality rules:
   - a real `viewBox`; no fixed pixel width/height on the root — the consumer sizes it;
   - `currentColor` or CSS-variable fills for anything that must survive theming;
     hard-coded brand hexes only for elements that must not re-theme (the logo mark);
   - named `<g>` groups for logical parts; no editor cruft (empty groups, default ids);
   - text converted to paths only for logo-grade marks; live `<text>` otherwise, with
     the font named and a fallback stated;
   - decorative assets get `aria-hidden="true"` guidance; informative ones get a
     `<title>` — say which applies in the report;
   - static by default (ruling L-10); animation only on explicit request, and the
     craft then comes from build·motion.
4. **Verify against the brand.** Every color in the file maps to a cited token; the
   asset reads at its intended size (check small: an OG image is seen at thumbnail
   size); it sits correctly on both light and dark grounds or names its required
   ground; it doesn't collide with the anti-generic bans in design's
   `direct/slop-tells.md`.
5. **Report.** The tokens and motifs used, the metaphor and method chosen, the
   intended placement and sizes, and anything provisional that should graduate into
   DESIGN.md or the `brand/` folder.

## Asset-type notes

- **Article/blog illustrations:** one atmospheric asset per piece at most; supporting
  figures stay quiet (the panel-rhythm rule in the identity method).
- **Repo / social / OG images:** design at display size (1200×630 for OG), verify at
  thumbnail size; text must survive the small render or be removed.
- **Logo and identity work:** the identity method governs; concepts come with the
  method named (e.g. "Negative Space: cutout initial") and two–three genuinely
  different candidates, not variations of one.
- **Feature concepts:** an on-brand *image* of a possible feature is this skill; an
  interactive mockup of it is design·mock — hand off when interaction matters.

## Handoffs

No brand truth exists → **design**, understand mode (document or generate the system
first). Asset needs to become a UI component → **build**. Judging existing assets →
**review**. Animating an asset → **build**, motion mode.
