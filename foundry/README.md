# The foundry

The machinery that builds and maintains the kit. The main README states the promise;
this directory proves it.

## Provenance model

Every file in the kit belongs to exactly one class, recorded in `MANIFEST.json`:

| Class | Meaning | Integrity check |
| --- | --- | --- |
| `verbatim` | byte-for-byte lift from a pinned upstream commit | sha256 vs manifest, and disk bytes vs the upstream blob at the pin (watcher) |
| `verbatim-minus` | verbatim with a recorded cut | patch applied to the pristine copy in `pristine/` must reproduce the shipped file |
| `distilled` | authored condensation of a recorded source | sha256 vs manifest; updated only via the distill runbook |
| `authored` | ours | normal review |

Bytes enter the repo only through `scripts/lift.sh`, which extracts the blob from
the upstream git object, records the pin and hash, and appends to `LOG.md`. Agents
working in this repo never retype vendored prose (see the repo's `AGENTS.md`).

## Verification

- `scripts/check-integrity.sh` runs in CI on every push and PR: recomputes every
  hash, re-applies every patch against pristine, and fails if any file under a
  skill's `references/` is unclassified.
- `scripts/check-upstream.sh` runs weekly (`upstream-watch.yml`): compares each
  pinned upstream blob against upstream HEAD, verifies disk bytes against the pin
  independently of the manifest (TAMPER), and opens one summary issue on drift.
- Drift is classified by the runbooks, never auto-merged.

## Records

- `MANIFEST.json` — per-file provenance: upstream, path, pinned commit, sha256.
- `LEDGER.md` — the rulings where sources contradicted each other; binding on all
  skill text until superseded.
- `derivations/` — per-skill receipts: what was lifted, cut, distilled, and why.
- `LOG.md` — append-only history of every lift, patch, ruling, and incident.
- `pristine/` — untouched originals and their patches for `verbatim-minus` files.

## Operating it

The process itself is a skill: `.claude/skills/foundry/` loads for any agent session
in this repo and carries the seven runbooks (lift, re-lift, distill refresh, new
ruling, integrity failure, course drop-in, new skill). The division of labor is
fixed: agents propose, hashes verify, humans merge.
