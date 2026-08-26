# The QA list

A markdown file the user keeps in the repo: the things they want checked, re-run on
demand. It stays in the repo; nothing else this skill produces does.

## Finding it

1. Look in `.product/` for a markdown file whose name says what it is: `qa-list.md`,
   `qa.md`, `checks.md`, `release-checklist.md`, `verify.md`. One match is the list.
   Several matches: ask which.
2. No match: read `~/.product-engineering/memories.md` for a `## pe-verify` entry
   naming this repo. Use that path.
3. Still nothing: ask one question — where the list is, or whether to seed one — and
   record the answer in the memories file so the question is never asked again for
   this repo.

Tell users the convention once, when it is relevant: keep a `.product/` folder at the
repo root with the QA list in it.

## The memories file

`~/.product-engineering/memories.md` is the kit's home folder note. Plain markdown; one
`##` section per skill; other skills keep their own durable notes here in their own
sections. Create the folder and file when absent. This skill's section:

```markdown
## pe-verify

- github.com/backnotprop/plannotator: docs/release-qa.md
- /Users/me/work/internal-tool: .product/qa-list.md
```

One line per repo: the remote (host/owner/name, no scheme) or the absolute path when
there is no remote, then the list's path relative to the repo root. Add a line when the
user answers the question above; replace it when they move the list.

## Reading the list

No required format. Each list item or heading is one check.

- A nested bullet is detail for its parent check, not a separate check.
- A heading with bullets under it groups checks; the heading is context, the bullets
  are the checks. A heading with no bullets is itself a check.
- A trailing hint — `(browser)`, `— code`, `(always flag)` — is honored. "Always
  flag" means the item reports `flag` whenever the condition is true, regardless of
  whether anything else passed.
- Terse items ("Bun not naively upgraded") are interpreted from the repo: find what
  pins the version, confirm it is unchanged since the last tag, cite the line.
- Rich items (a 29-entry release list mixing browser behavior, install-path
  divergence, prompt-cache preservation, supply-chain version checks, doc staleness)
  are run in full. Length is not a reason to sample.

Item ids in the report are slugs of the check titles (`bun-version`,
`toolbar-buttons-present`), stable across runs so reports line up release to release.

## Seeding a list

Only when the user asks. Draft it from repo evidence — routes and pages, install and
build scripts, the package manager and runtime pins, CI steps, the README's claims —
as a flat list of checks with one line each. Write it to `.product/qa-list.md`, then
hand it to the user to prune.
