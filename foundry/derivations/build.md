# Derivation: build

Write and refine production UI to the craft bar. Four modes: craft · motion · a11y ·
harden. The Jakub domain fold (Decision 1) happens here: his skills come in file-for-file
intact as reference sets (`SKILL.md` → `index.md`, bytes unchanged), reversibly.

## Spine

`skills/build/SKILL.md` — authored. Basis: our legacy ui-polish workflow (boundary →
evidence → triage → implement → verify → report), generalized as the shared loop for all
modes; mode router; rulings block (L-01..L-08 — L-08 belongs here because build
implements forms); the explicit-redesign gate; course-folder preference; better-* name
mapping (same convention as review).

## Files (all under skills/build/references/)

### craft/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| emil-craft.md | emilkowalski/skills · skills/emil-design-eng/SKILL.md | GOLD | verbatim-minus | CUT (patch): the "Initial Response" chatbot-greeting section and the mandated Before/After review-report format — both interaction plumbing, not craft. Everything else byte-for-byte |
| ui/index.md + animations, enter-exit, icon-transitions, icons, performance, surfaces | jakubkrehel/skills · skills/better-ui/* | GOLD | verbatim ×7 | detail canon |
| layout/index.md + grouping-and-alignment, spacing-and-adaptivity | jakubkrehel/skills · skills/better-layout/* | GOLD | verbatim ×3 | domain fold |
| typography/index.md + choosing-fonts, css-cheat-sheet, details-and-accessibility, spacing-and-sizing, variable-fonts-and-opentype, wrapping-and-punctuation | jakubkrehel/skills · skills/better-typography/* | GOLD | verbatim ×7 | domain fold |
| colors/index.md + color-formats, color-usage, contrast, palette-generation, palette-structure, token-naming | jakubkrehel/skills · skills/better-colors/* | GOLD | verbatim ×7 | domain fold |
| writing/index.md | jakubkrehel/skills · skills/better-writing/SKILL.md | GOLD | verbatim | UX copy |
| generation-guardrails.md | ibelick/ui-skills · skills/baseline-ui/SKILL.md | SOLID | verbatim | terse MUST/NEVER layer; subordinated to L-05/L-06 by the spine |
| library-choices.md | emilkowalski/skills · skills/pick-ui-library/SKILL.md | SOLID | verbatim | curated registry; highest staleness pressure — watcher priority |
| deslop-audit.md | Leonxlnx/taste-skill · skills/redesign-skill/SKILL.md | PADDED | verbatim-minus | KEEP: the four audit checklists (AI-fingerprint content/component/layout/omissions). CUT (patch): "Upgrade Techniques" (mandates scroll-hijack/parallax — violates L-10 doctrine) and the process framing (the spine owns process). Behind the explicit-redesign gate |
| polish-lenses.md | ours (legacy ui-polish) | SOLID | authored | move |

### motion/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| build.md | emilkowalski/skills · skills/animate/SKILL.md | GOLD | verbatim | decision-ordered build procedure, MIT lineage |
| recipes.md | emilkowalski/skills · skills/animate/RECIPES.md | GOLD | verbatim | |
| apple-design.md | emilkowalski/skills · skills/apple-design/SKILL.md | GOLD | verbatim | momentum/rubberband math unique in corpus; §16 drift noted, not cut (whole-section cut not warranted) |
| vocabulary.md | emilkowalski/skills · skills/animation-vocabulary/SKILL.md | GOLD | verbatim | name-the-effect lookup, MIT glossary (~115 terms) |
| view-transitions/index.md + css-recipes, implementation, nextjs, patterns | vercel-labs/agent-skills · skills/react-view-transitions/* | GOLD | verbatim ×5 | complementary to everything else. Its css-recipes use ease-in on several `::view-transition-old` (exit) snapshots — an L-04 conflict handled by a spine note, not by editing; one recipe also eases-in on enter (craft-bar conflict, same note) |
| perf-additions.md | ibelick/ui-skills · skills/fixing-motion-performance/SKILL.md | SOLID | distilled | SALVAGE LIST (contract): layout read/write interleaving + FLIP; pause/stop off-screen animations (IntersectionObserver); blur ≤ 8px; view-transition boundaries; don't-migrate-animation-libraries. Everything else retired (subsumed by course-pack perf material or thin) |

### a11y/
| dest | source | grade | class |
| --- | --- | --- | --- |
| index.md + focus-and-keyboard, forms, hit-areas, motion-and-zoom, screen-readers, semantics-and-aria | jakubkrehel/skills · skills/better-accessibility/* | GOLD | verbatim ×7 |

### harden/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| index.md | ours (legacy ui-harden SKILL.md) | SOLID | authored | move; frontmatter converted to reference header |
| adaptation-patterns.md, performance-diagnostics.md, resilience-matrix.md | ours (legacy ui-harden) | SOLID | authored | moves |
| metadata.md | ibelick/ui-skills · skills/fixing-metadata/SKILL.md | SOLID | verbatim | folded whole per roster |

### course/ (private drop-in — never committed)
`course/README.md` (authored) explains the slot. Private manifest entries map the
purchased animationsdev files (craft: design-rules, forms-controls, touch-accessibility,
ui-polish, marketing · motion: css-animations, motion-react, gesture-ui, scroll-animations,
debug-animation, animation-performance, animation-accessibility + snippets, motion-brief,
animate refs). `upstream_path` is relative to the local pack install.

### foundry/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| foundry/ownership-matrix.md | jakubkrehel/skills · AGENTS.md | GOLD | verbatim | the rule-ownership arbitration table, adopted kit-wide (Decision 1) |

## Rulings applied

L-01 (0.96 exact), L-02 (bounce 0 default), L-03 (reduced motion gentler-not-zero),
L-04 (ease-out exits; + spine note on view-transitions exit easing), L-05 (reactive
will-change), L-06 (named curves yes / novel curves no), L-07 (stagger units),
L-08 (never disable submit — build implements forms) — all stated once in the spine's
rulings block. L-10 doctrine motivates the deslop-audit cut.

## Approval stamp (#38)

Spine only (authored). Loop step 1 (Boundary) reads `.product/approved/` for a record
matching the target; an approved artifact ranks above the agent's judgment and below the
user's words, and any deviation (constraint, platform, accessibility) is stated before
it is made. Step 6 (Report) names the record built against and each stated deviation —
the statement is what pe-review's fidelity mode later treats as sanctioned. No new
section, no reference changes.

## Retirements

Legacy `skills/ui-polish` and `skills/ui-harden` are superseded and removed; their
authored texts survive as spine basis / harden references. `skills.sh.json` updated.
