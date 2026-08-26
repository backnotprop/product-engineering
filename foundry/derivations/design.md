# Derivation: design

Everything before production code. Five modes: understand · direct · mock · vary ·
onboard. Consolidation ruling: the plannotator effective-html pipeline is copied and
compressed here (the upstream repo stays untouched and publishes independently).

## Spine

`skills/design/SKILL.md` — authored. Mode router with cues; the shared authority chain
(user's words → project's design system → subject → judgment); artifacts-not-code
contract (vary is the one sanctioned codebase touch, via a throwaway harness); handoffs.

## Files (all under skills/design/references/)

### understand/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| index.md | ours (legacy project-context SKILL.md) | GOLD | authored | move; frontmatter → reference header |
| design-format.md, templates.md | ours (legacy project-context refs) | GOLD | authored | moves |
| url-and-validation.md | ibelick/ui-skills · skills/create-design-md/SKILL.md | SOLID | distilled | SALVAGE (contract): the evidence pipeline (role → value → source → scope → recurrence → confidence) stated once; the URL-mode three-proof gate (Observation/Basis/Consequence); the `design.md lint/export/diff/spec` validation commands and export targets; the scalar-typography shape rule stated once. Retired: its ~5× defensive restatements of the same rules |
| generated-mode.md | Leonxlnx/taste-skill · skills/stitch-skill/SKILL.md (+ its DESIGN.md example) | PADDED | distilled | SALVAGE (contract): the concrete anti-pattern ban list (fake round numbers; h-screen iOS trap); the four taste dials (Creativity/Density/Variance/Motion 1–10) as Overview fields; the discipline that a generated system is labeled CHOSEN, never observed. Retired: SKILL/DESIGN self-duplication, the global aesthetic mandates ("Inter is BANNED", fixed spring values) |

### direct/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| index.md | plannotator/effective-html · skills/design-artifact/SKILL.md | GOLD | verbatim | the spine of taste: derive-from-subject, register sizing, AI-tell awareness |
| slop-tells.md | Leonxlnx/taste-skill · skills/taste-skill/SKILL.md | SOLID (GOLD veins) | verbatim-minus | KEEP byte-for-byte (per adjudication "graft §9 verbatim"): §9 production-test tells whole (incl. 9.F), the premium-consumer palette ban with hex families, the eyebrow ration with its mechanical count, the layout hard rules (hero stack, zigzag cap, bento cell counts), the brief→official-design-system map. CUT (patch, large — ~80% of the 1206 lines): the dial arithmetic, triplicated rule statements, 60-box pre-flight (dupes), GSAP skeletons (motion family owns motion), §11 redesign protocol (build's deslop-audit.md already covers redesigns — one owner), §12 empty Block Library, vendored install appendices, the source frontmatter block, and the dangling cross-references to cut sections (whole-sentence deletions only) |
| presets/minimalist.md | Leonxlnx/taste-skill · skills/minimalist-skill/SKILL.md | SOLID | verbatim | commission preset, never a default |
| presets/brutalist.md | Leonxlnx/taste-skill · skills/brutalist-skill/SKILL.md | SOLID | verbatim | the better preset ("judgment, not inherited dogma") |
| presets/premium-dark-glass.md | Leonxlnx/taste-skill · skills/soft-skill/SKILL.md | PADDED | verbatim-minus | KEEP: Double-Bezel concentric-radius math, button-in-button, the `cubic-bezier(0.32,0.72,0,1)` spec, blur/grain performance constraints. CUT (patch): the persona framing (title line and §1), the Variance Engine, and every never-static motion mandate (L-10) — including the instant-state-change ban, "never use default transitions", and the do-not-just-appear nav phrasing |

### mock/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| index.md | plannotator/effective-html · skills/html/SKILL.md | SOLID | verbatim | the router; its skill-name routing resolves inside this mode (mapping in spine) |
| wireframe.md / prototype.md / diagram.md / plan.md | plannotator/effective-html · skills/html-{wireframe,prototype,diagram,plan}/SKILL.md | SOLID | verbatim ×4 | fidelity ladder intact |
| charts-and-data.md, diagrams.md, documents-and-presentations.md, interfaces.md | plannotator/effective-html · skills/html/references/* | SOLID | verbatim ×4 | shared craft refs. `creative-direction.md` deliberately NOT lifted — it is the documented degraded-install fallback for design-artifact, redundant when direct/index.md ships in the same skill |

### vary/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| index.md | emilkowalski/skills · skills/prototype/SKILL.md | GOLD | verbatim | byte-identical across both Emil lineages — zero licensing ambiguity |
| picker.md | emilkowalski/skills · skills/prototype/PICKER.md | GOLD | verbatim | the engineered picker (keyboard, URL persistence, replay, reduced-motion) |
| axes.md | jakubkrehel/skills · skills/variant/SKILL.md | SOLID | distilled | SALVAGE (contract): the single-primary-axis rule with its rationale ("varying every axis at once produces three unattributable results"); the accessibility floor as a pre-picker gate; named URL params (`?variant=quiet`) replacing `?v=N`. Retired: its under-engineered picker prose (Emil's picker wins) and jakub-collection skill-name routing |

### brief/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| index.md | pbakaus/impeccable · skill/reference/shape.md (+ new-work.md §1 authority states and §2 surface-job questions) | SOLID | distilled | SALVAGE (the contract = issue #1's lists): the discovery cadence and both question rounds; the surface-job framing; the four visual-authority states; the seven-section brief structure; smallest-useful-brief; confirm-and-stop. EXCLUDED per issue #1's standalone constraints: concept-seed/serve-question scripts, decision pages, comps, config/state, mandatory PRODUCT.md/DESIGN.md, direction selection (one owner — direct mode). Chat by default, file only on request. Upstream is Apache-2.0 and now watcher-tracked — the first pinned Impeccable source |

### onboard/
| dest | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| index.md | ours (legacy ui-onboarding SKILL.md) | SOLID | authored | move; frontmatter → reference header |
| patterns.md | ours (legacy ui-onboarding refs) | SOLID | authored | move |

## Rulings applied

L-10 (motivated motion) drives the premium-dark-glass cut. The prescriptive-vs-
derivational conflict resolves as the register split: derivation (direct/index.md) is
the default; presets are commissions invoked by explicit direction match.

## Also in this change

Review spine's name-mapping rows updated: build now exists, so "once present" hedges
for build's craft/a11y references resolve to real paths.

## Retirements

Legacy `skills/project-context` and `skills/ui-onboarding` are superseded and removed;
their authored texts survive as understand/ and onboard/ references. `skills.sh.json`:
converged group only (review, build, design).
