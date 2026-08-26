# Derivation: review

Read-only UI judgment with verdicts. Seven modes: screen · change · plans · guidelines ·
stress · motion · a11y. Adjudicated in the convergence round (see the Moneyball Roster
artifact); grades below are from full-read comparative adjudication with quoted evidence.

## Spine

`skills/review/SKILL.md` — authored. Thin router: mode table with cues, the read-only
contract, the better-* name-mapping table (see note below), rulings block (L-09, L-11),
handoffs to `build`. Never restates reference content.

**Name-mapping note:** the lifted Jakub texts route to his `better-*` domain skills by
name. Those names don't exist in this kit. Rather than editing his prose (forbidden),
the spine carries a mapping table (e.g. `better-typography` → build skill's typography
references). This preserves bytes and keeps his routing semantics.

## Files

| dest (references/) | source | grade | class | notes |
| --- | --- | --- | --- | --- |
| engine.md | jakubkrehel/skills · skills/better-interface/SKILL.md | GOLD | verbatim | the engine: evidence bar, 13 escalation triggers, cheaper-fix ladder, consolidation, verdict |
| review-format.md | jakubkrehel/skills · skills/better-interface/review-format.md | GOLD | verbatim | output tables |
| change-review.md | jakubkrehel/skills · skills/interface-review/SKILL.md | GOLD | verbatim | diff/branch/PR mode |
| scope-resolution.md | jakubkrehel/skills · skills/interface-review/scope-resolution.md | GOLD | verbatim | diff-scoping machinery |
| removed-signals.md | jakubkrehel/skills · skills/interface-review/removed-signals.md | GOLD | verbatim | refactor-vs-regression guards |
| stress.md | jakubkrehel/skills · skills/break/SKILL.md | GOLD | verbatim | hostile-state harness |
| stress-scenarios.md | jakubkrehel/skills · skills/break/scenarios.md | GOLD | verbatim | axis/cue scenario list |
| motion-review.md | emilkowalski/skills · skills/review-animations/SKILL.md | GOLD | verbatim | MIT lineage per licensing ruling |
| motion-standards.md | emilkowalski/skills · skills/review-animations/STANDARDS.md | GOLD | verbatim | includes the gestures/drag section unique to MIT lineage |
| plan-template.md | emilkowalski/skills · skills/improve-animations/PLAN-TEMPLATE.md | GOLD | verbatim | the standard plan format (H8 ruling); generalized by spine prose, not by editing |
| audit-method.md | ibelick/ui-skills · skills/improve-ui/SKILL.md | SOLID | verbatim-minus | KEEP: falsification pass, three-proof gate, read-only discipline. CUT (patch): the a11y-discard rule (overruled by L-09) and the stop-at-three cap (a roster adjudication cut — the cap biases audits toward reporting nothing, inconsistent with the engine's consolidation model; not itself ledger text) |
| web-interface-guidelines.md | vercel-labs/web-interface-guidelines · command.md | GOLD | verbatim-minus | KEEP: ~150 lintable rules. CUT (patch, per L-11): house-taste rows (Title Case, "&" over "and") and the autocomplete self-contradiction (resolved: autocomplete on purposeful fields; "off" only for non-auth-sensitive) |
| a11y-audit.md | ibelick/ui-skills · skills/fixing-accessibility/SKILL.md | SOLID | distilled | SALVAGE LIST (the contract): the priority-ordered audit table; the "tool boundaries" category (don't add ARIA where native semantics suffice); the complex-widgets guidance (prefer established accessible primitives). Everything else retired — its three contradictions with better-accessibility lose on evidence (see LEDGER context for L-08) |
| experience-rubric.md | ours (legacy skills/ui-review) | GOLD | authored | moved from legacy ui-review; Impeccable-derived, ours |
| technical-rubric.md | ours (legacy skills/ui-review) | GOLD | authored | moved from legacy ui-review |
| screen-review.md | ours (legacy skills/ui-review/SKILL.md) | GOLD | authored | the two-pass screen flow + Nielsen 0–4 scoring, converted from skill to reference; frontmatter dropped, body kept |
| motion-audit.md | emilkowalski/skills · skills/improve-animations/SKILL.md | GOLD | verbatim | whole-codebase motion audit → plans (read-only, so it lives here not in build) |
| motion-audit-signals.md | emilkowalski/skills · skills/improve-animations/AUDIT.md | GOLD | verbatim | hunt-for signal lists for the motion audit |
| motion-opportunities.md | emilkowalski/skills · skills/find-animation-opportunities/SKILL.md | GOLD | verbatim | lowest-loss twin (~10% delta vs course); read-only proposer |

## Rulings applied

- **L-09**: audit-method.md patch cuts the a11y-discard rule. (The stop-at-three cap
  is cut in the same patch as a roster adjudication, not under L-09 — see the table.)
- **L-11**: web-interface-guidelines.md patch cuts house-taste rows and resolves the
  autocomplete contradiction.
- Severity: HIGH/MED/LOW + escalation triggers is the standard (engine.md); the
  P0–P3 scale in screen-review.md is kept as that mode's output flavor with the
  mapping stated in the spine (P0+P1→HIGH, P2→MEDIUM, P3→LOW).

## Retirements in this change

Legacy `skills/ui-review/` is superseded by `skills/review/` and removed;
`skills.sh.json` updated. Its texts survive as the three authored files above.
