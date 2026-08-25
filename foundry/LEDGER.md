# Ledger — contradiction rulings

Where graded sources disagree, we rule once and every skill follows the ruling. A ruling
changes only by a new entry that supersedes it (never by silent edit). No skill text —
authored or vendored-with-patch — may contradict an active ruling. Resolution order used
throughout: measured evidence beats assertion · an exact enforceable value beats a range ·
the domain owner wins per the ownership matrix · ties get a decision anyway, logged.

Format: id · topic · positions · ruling · rationale. `Affects` lists repo files once they exist.

---

**L-01 · Press scale** — jakubkrehel: exactly `0.96` vs emilkowalski: `0.95–0.98` range.
**Ruling:** 0.96 exact. An exact value is enforceable; a range invites drift. Emil's range noted as tolerance.

**L-02 · Spring bounce** — jakubkrehel: always `0` vs emilkowalski: subtle `0.1–0.3` when used.
**Ruling:** bounce 0 by default; nonzero only when the design direction's register explicitly calls for playful.

**L-03 · Reduced motion** — emil monolith: gentler-not-zero, keep opacity/color vs animationsdev refs: disable all, no exceptions.
**Ruling:** gentler-not-zero. Matches the two-variant doctrine; blanket disable is the lazier reading.

**L-04 · Exit easing** — jakubkrehel + emil monolith: ease-out both directions vs emil design-rules: accelerate away (ease-in).
**Ruling:** ease-out for exits by default. Two of three sources, including Emil against himself. Accelerate-away allowed as a deliberate, stated choice.

**L-05 · will-change** — animationsdev: apply proactively vs jakubkrehel: only on observed first-frame stutter vs ibelick baseline: never outside an active animation.
**Ruling:** reactive (jakub) — evidence-driven application only. Baseline's phrasing survives as the generation guardrail.

**L-06 · Custom easing curves** — emilkowalski: "built-ins are too weak" vs ibelick baseline: "never introduce custom curves."
**Ruling:** split by intent. Custom curves from the kit's named set: yes. Inventing novel curves ad hoc: no.

**L-07 · Stagger** — emilkowalski: 30–80ms per item vs jakubkrehel: ~100ms per group.
**Ruling:** both — the units differ (list items vs semantic chunks). Reconciled in one paragraph; not a conflict.

**L-08 · Disabled submit buttons** — ibelick: explain why disabled vs jakubkrehel: never disable; validate on submit.
**Ruling:** never disable. Wins on accessibility evidence — an enabled button that validates is discoverable; a disabled one is a dead end.

**L-09 · Accessibility findings in audits** — ibelick improve-ui: "discard a11y findings unless requested" vs every other source.
**Ruling:** a11y findings are never discarded. improve-ui's falsification pass survives without its discard rule.

**L-10 · Motion by default** — leonxlnx gpt-taste/soft-skill: "static is forbidden" vs design-artifact + taste v2: motion must be motivated.
**Ruling:** motivated motion. "If you cannot articulate the reason in one sentence, drop the animation." Mandated-motion texts were cut or stripped.

**L-11 · Guidelines house taste** — vercel web-interface-guidelines: Title Case headings, "&" over "and", autocomplete stated both ways vs jakubkrehel: "evidence, not taste."
**Ruling:** the evidence bar. House-taste rows are cut from the vendored copy (via its patch); the autocomplete tension resolves to: autocomplete on purposeful fields, off only for non-auth-sensitive cases.
