# Runbook: distill refresh — regenerate a distilled file

The salvage list in `foundry/derivations/<skill>.md` is the contract: it names
exactly what the distillation must carry. Never regenerate without it in context.

1. Read the derivation entry and the upstream diff (if drift triggered this).
2. Update the recorded source pin: `lift.sh --class distilled-source` with the new SHA
   (records provenance without copying bytes).
3. Rewrite the distilled file against the salvage list. Anti-slop gates apply.
4. Lock the new hash: `foundry/scripts/check-integrity.sh --update-distilled <path>`.
5. PR: the reviewable diff is the distillation change itself. Human merges.
