# Approved: docs-site-concept

- **Approved:** 2026-08-26
- **By:** ramos
- **From:** this session's concept artifact (https://claude.ai/code/artifact/f43af588-41c0-4382-84a0-d1eb02f9e0fc), version "approved-no-foundry"
- **Artifact:** `docs-concept.html`, byte-for-byte as approved

## The state approved

A documentation site for this repository, built on Nimbus (Astro), with:

- Sections: Start, Skills (one page per skill, seven), Workflows, People (one tribute
  page per author, eight), Reference. **No Foundry section** (the user's one change at
  approval); the provenance summary lives on the People index and links to `foundry/`
  on GitHub.
- The skill page anatomy: card header, "say this, get this", modes, setup in the fixed
  order required / optional / convention, what it produces with a rendered example,
  handoffs, provenance strip.
- The tribute page anatomy: name, upstream, license; what we carry in the author's own
  terms; manifest facts (files by class, skills, ledger rulings, watcher); the full
  receipts table linking upstream blob and kit copy. No bios unless supplied.
- Skill and People pages generated from SKILL.md frontmatter, MANIFEST.json, NOTICE,
  and LEDGER.md by a build-time sync script; the site fails CI the way the kit does.
- Brand on Nimbus per DESIGN.md: dark radial ground, light ground as the other theme,
  Geist / Geist Mono self-hosted, no accent (`--nb-primary` = foreground), the card
  gradient as `--nb-card`, the OG route restyled to the card. No hero on the home page.
- Mockups approved: home, the pe-verify skill page, the Jakub Krehel tribute page.

## Decisions on the way

- Foundry section: rejected at approval (redundant with the repo; People index carries
  the summary).
- Tribute pages carry receipts, not adjectives.

## Open at approval (not decided by this record)

- Where the site lives (`docs/` in this repo was recommended) · domain · whether to
  ask authors for a one-line bio · default theme (system preference recommended).
