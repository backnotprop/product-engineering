# Derivation: product-description

Adopted whole, byte-for-byte, per explicit ruling — the only skill in the kit with a
vendored spine. Grade from adjudication: GOLD ("best-engineered skill in the set" —
compounding method, production-grade bug triage, a real link checker).

## Source

steveruizok/product-description — the gist `83ae5c53f2784ebf8f5fe0a3fb94480f`
(gists are git repos; watchable like any upstream). The gist has no license file;
Steve granted reuse permission via Twitter — the permission record belongs in NOTICE.

The gist is flat (gists cannot hold directories); its `install.sh` maps the reference
files into a `references/` folder on install. We replicate that layout, so the
SKILL.md's internal `references/…` links resolve as the author intended. `install.sh`
and the gist's own `README.md` are install plumbing, not skill content — not lifted.

## Files

| dest | gist path | class |
| --- | --- | --- |
| skills/product-description/SKILL.md | SKILL.md | verbatim (vendored spine — never edited) |
| skills/product-description/references/README-template.md | README-template.md | verbatim |
| skills/product-description/references/bug-triage-template.md | bug-triage-template.md | verbatim |
| skills/product-description/references/check-links.py | check-links.py | verbatim |
| skills/product-description/references/document-template.md | document-template.md | verbatim |
| skills/product-description/references/glossary-guide.md | glossary-guide.md | verbatim |
| skills/product-description/references/goal-template.md | goal-template.md | verbatim |
| skills/product-description/references/product-kinds.md | product-kinds.md | verbatim |
| skills/product-description/references/verification-template.md | verification-template.md | verbatim |

## Rulings applied

None — no contradictions touch this skill. No cuts, no distillation, no grafts.
Cross-linking from design's understand mode is one sentence in design's spine already
("Behavior specs beyond PRODUCT.md's scope → product-description").
