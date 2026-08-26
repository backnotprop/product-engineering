# Screen review (two-pass flow)

The screen mode of the pe-review skill: full assessment of a concrete UI target.
Severity here uses P0–P3; map to the engine's scale as P0+P1 → HIGH,
P2 → MEDIUM, P3 → LOW.

Review any concrete UI target without requiring project context files, a detector, persistence, or a larger workflow.

## Resolve the target

Identify the exact surface: URL, screenshot, route, component, source path, or flow. Narrow vague requests to the smallest useful target and state the chosen scope.

Use the strongest available evidence:

- inspect the rendered interface when it is available;
- exercise the primary path rather than judging a still frame alone;
- inspect relevant source and shared conventions when code is available;
- evaluate representative desktop, intermediate, and mobile sizes;
- distinguish observed behavior from inference.

Do not start a server, install tooling, or mutate a browser session unless the user authorized that operation.

## Run two passes

Keep the first pass independent of mechanical findings so lint-like output does not anchor visual judgment.

When permitted and useful, separate agents may run the two passes in parallel using self-contained context. They are not required. Without them, complete and record Pass A before beginning Pass B. Independence of judgment matters; dependence on a particular orchestration tool does not.

### Pass A: experience and design

Evaluate:

- product specificity versus category-interchangeable design;
- primary task, reading order, hierarchy, and information architecture;
- discoverability, feedback, control, consistency, and recovery;
- typography, color, layout, density, imagery, and motion;
- cognitive load and decision complexity;
- emotional fit and high-stakes moments;
- loading, empty, error, success, disabled, and permission states;
- relevant user perspectives.

Read `references/experience-rubric.md` for the complete heuristic, cognitive-load, persona, and severity rubrics.

For a full review, score all applicable Nielsen heuristics from 0–4, mark truly inapplicable items `n/a`, and calculate the result against the applicable maximum.

### Pass B: implementation evidence

Evaluate only what the available evidence supports:

- accessibility;
- responsive behavior and input methods;
- theming and token consistency;
- performance risks;
- implementation integrity and repeated shortcuts.

Read `references/technical-rubric.md` for the technical dimensions and scoring anchors.

For a full web review with source or runtime evidence, score the five applicable technical dimensions from 0–4. For a screenshot-only or deliberately scoped review, mark dimensions that cannot be verified `not assessed`; do not guess scores.

Use existing project checks when they are already available and relevant. Automated findings are evidence to verify, not proof. Do not require or install a proprietary detector.

## Synthesize

Do not concatenate two reports. Explain:

- where visual judgment and technical evidence agree;
- which issues are visible only in behavior or source;
- which automated findings are false positives or uncertain;
- which strengths should be preserved.

Prioritize by user impact, frequency, reach, and remediation cost. A short list of high-confidence problems is better than padded output.

## Output

For a full review, use this structure:

1. **Method and evidence**: target, rendered states, source, checks, and limitations.
2. **Experience health**: Nielsen table, total against applicable maximum, cognitive-load result, and product-specificity verdict.
3. **Technical health**: five-dimension table and total against applicable maximum.
4. **Overall verdict**: clearest judgment and largest opportunity.
5. **What works**: two to four specific strengths worth preserving.
6. **Priority findings**: three to seven issues ordered by severity.
7. **Persona red flags**: exact failures from two or three relevant perspectives.
8. **Systemic patterns**: recurring causes rather than isolated symptoms.
9. **Recommended actions**: ordered, concrete next steps.
10. **Evidence limits**: what could not be verified and any assumptions.

For a scoped review, include only applicable sections, but keep the same finding format and evidence standards.

For each finding include:

- **Severity**: P0, P1, P2, or P3;
- **Evidence**: element, state, behavior, file, or line;
- **Impact**: the user harm or product cost;
- **Recommendation**: a specific correction;
- **Confidence**: include only when evidence is incomplete.

Do not combine the experience and technical totals into a false universal score. Mark inapplicable items `n/a`, mark unverified dimensions `not assessed`, and adjust each denominator. Never inflate a score to be polite.

## Boundaries

- Remain read-only unless implementation was explicitly requested.
- Do not create report history, hidden state, or project files unless asked.
- Do not require `PRODUCT.md`, `DESIGN.md`, subagents, browser injection, or a detector.
- Use context documents when present, but treat the rendered product and code as evidence too.
- Do not report generic advice without tying it to the target.
- Do not report an issue without explaining why it matters.
- Do not call a visual preference an accessibility or correctness defect.
