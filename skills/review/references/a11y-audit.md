# A11y audit order

Deep accessibility judgment — focus mechanics, screen-reader behavior, hit-area
geometry, form-error routing — lives in the build skill's accessibility references;
this file only orders the audit and bounds the tooling. Severity and reporting follow
engine.md (escalation triggers apply; several name a11y failures directly).

## Audit in this order

| priority | category | impact |
|----------|----------|--------|
| 1 | accessible names | critical |
| 2 | keyboard access | critical |
| 3 | focus and dialogs | critical |
| 4 | semantics | high |
| 5 | forms and errors | high |
| 6 | announcements | medium-high |
| 7 | contrast and states | medium |
| 8 | media and motion | low-medium |
| 9 | tool boundaries | critical |

Work down the table; do not report category-7 polish while a category-1 control has
no accessible name. Findings still pass through the engine's evidence bar
(engine.md) before they are reported.

## Tool boundaries (apply to proposed fixes)

- Prefer minimal changes; do not refactor unrelated code.
- Do not add ARIA when native semantics already solve the problem.
- Do not migrate UI libraries unless requested.
- For complex widgets (menu, dialog, combobox), prefer established accessible
  primitives over custom behavior.
