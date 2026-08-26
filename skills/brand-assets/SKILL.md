---
name: brand-assets
description: Create standalone visual assets that stay on brand — SVG illustrations for articles and blog posts, repo and social/OG images, logo and identity work, on-brand concept images for features. Authors SVG in code. Reads the project's brand truth (DESIGN.md, style guides, a brand/ folder) first and refuses to invent brand values. Triggers on brand asset, on-brand, SVG illustration, article image, header image, og image, social card, repo image, logo, brand kit, identity, tagline panel. Not for UI mockups (design), production components (build), or judging existing assets (review).
license: Apache-2.0
metadata:
  provenance: New spine; identity method distilled from Leonxlnx/taste-skill brandkit — see foundry/derivations/brand-assets.md
---

# Brand Assets

Standalone assets that belong to the brand, authored as SVG in code and exported to
raster where the destination requires it.

## The workflow

1. **Locate brand truth — or stop.** Read, in order: `DESIGN.md` (the design skill's
   understand mode owns its format), any style guide, and a `brand/` folder (logos,
   fonts, reference assets) if present. Index what exists: palette tokens, type
   choices, radii/shape language, existing marks and motifs. If none of these exist,
   do not invent a brand — offer to run design·understand first, or proceed only with
   values the user supplies in the conversation, labeled as provisional.
2. **Derive the asset's rules.** Colors come only from the brand palette (cite the
   token names). Type in the asset is the brand's faces. Shapes follow the recorded
   shape language. The metaphor comes from the identity method
   (`references/identity-method.md`).
3. **Author the SVG — rules split by how it will be consumed.**
   Always: a real `viewBox`; named `<g>` groups for logical parts; no editor cruft
   (empty groups, default ids).
   *Inline in a page's DOM* (site illustrations, in-app art): `currentColor` or
   CSS-variable fills so it themes with the page; hard-coded brand hexes only for
   elements that must not re-theme (the logo mark); live `<text>` with the font named
   and a fallback stated; omit fixed root width/height and let layout size it;
   decorative → `aria-hidden="true"`, informative → `role="img"` + `<title>` wired
   via `aria-labelledby` — say which applies in the report.
   *Consumed as a file* (`<img>` src, README, anywhere external): `currentColor` and
   CSS variables do not resolve and webfonts do not load — use hard-coded brand hexes,
   convert text to paths, and set root width/height for intrinsic sizing.
   Static by default — this skill's own bar, stricter than L-10's motivated-motion
   rule: animate only on explicit request, with the craft from build·motion.
4. **Export where SVG can't go.** OG/social endpoints and GitHub's social preview
   accept raster only: render the SVG to PNG at the destination size (1200×630 for
   standard OG tags; 1280×640 for GitHub's social preview) and deliver both files,
   the SVG as the editable source of truth.
5. **Verify against the brand.** Every color maps to a cited token; the asset reads
   at its real display size (an OG image is judged at thumbnail size); it sits
   correctly on both light and dark grounds or names its required ground; it doesn't
   collide with the anti-generic bans in the design skill's
   `references/direct/slop-tells.md`.
6. **Report.** The tokens and motifs used, the metaphor and method chosen, placement,
   sizes and exported formats, and anything provisional that should graduate into
   DESIGN.md or the `brand/` folder.

## Asset-type notes

- **Article/blog illustrations:** one atmospheric asset per piece at most; supporting
  figures stay quiet — the identity method's panel rhythm, applied to a page.
- **Repo / social / OG images:** authored as SVG, delivered as PNG per step 4; text
  must survive the thumbnail render or be removed.
- **Logo and identity work:** the identity method governs; concepts come with the
  method named (e.g. "Negative Space: cutout initial") and two–three genuinely
  different candidates, not variations of one.
- **Feature concepts:** an on-brand *image* of a possible feature is this skill; an
  interactive mockup of it is design·mock — hand off when interaction matters.

## Handoffs

No brand truth exists → **design**, understand mode (document or generate the system
first). Asset needs to become a UI component → **build**. Judging existing assets →
**review**. Animating an asset → **build**, motion mode.
