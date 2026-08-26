# URL extraction and validation

Distilled from ibelick/ui-skills `create-design-md` (see MANIFEST for the pin).
Salvage contract: the evidence pipeline, the URL-mode three-proof gate, the validation
commands, and the frontmatter shape rules — each stated once. This extends
`index.md` (the understand workflow) with its two machine-verified capabilities:
documenting from a public URL, and validating DESIGN.md before it ships.

## The evidence pipeline (both modes)

```
role → value → source → scope → recurrence → confidence
```

Collect evidence, record source/scope/recurrence per candidate, normalize into the
DESIGN.md schema, omit anything uncertain or not implementation-relevant, validate the
frontmatter shape, and only then write prose. Never let repository or URL evidence
introduce a second token schema.

## URL mode: the three-proof gate

A claim from a live site is written only when all three proofs hold:

1. **Observation** — the pattern or value is visible or computed on the rendered page.
2. **Basis** — it is measured, or recurs across the required sampled pages/viewports.
3. **Consequence** — it changes a concrete implementation choice in DESIGN.md.

Missing any proof → omit the claim. Never turn a visual impression into a token, a
single occurrence into a site-wide rule, or a guessed value into YAML. Exact values
require computed styles or loaded CSS; otherwise describe the role without a value.
A component section requires the same treatment to recur across at least two sampled
pages. URL-mode YAML is intentionally sparse, never padded to look complete.

## Frontmatter shape (hard gate, stated once)

Token groups are mappings whose children are the schema's fields — never scalar
entries (`sans: Geist`), never source-shaped nesting, never keys copied from CSS
variable names. Typography uses only the canonical fields `fontFamily`, `fontSize`,
`lineHeight`, `fontWeight`, `letterSpacing` (e.g. `typography.mono.fontFamily:
Geist Mono`). A lone group-level source token like `--radius` normalizes to `base`.
Resolve framework utilities through the active theme before writing exact values.

## Validation (the ship gate)

Identify the export target first — `css-tailwind` (Tailwind v4), `json-tailwind`
(v3), `dtcg` otherwise — then:

```bash
npx @google/design.md spec     # check the installed schema before encoding themes
npx @google/design.md lint     # shape validation
npx @google/design.md export   # must succeed for the chosen target
npx @google/design.md diff     # against the previous version, on refresh
```

The document is private until validation passes — never show a draft that hasn't
passed lint and export. If a category can't be repaired, remove it and report the
omission.
