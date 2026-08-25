# Runbook: new ruling — sources contradict, or a ruling must change

1. Write the entry in `foundry/LEDGER.md` with the next L-nn id: topic, positions
   with short quotes, ruling, rationale. A changed ruling is a NEW entry marked
   "supersedes L-nn" — never edit the old one.
2. Add the ruling id to the `rulings` array of each affected manifest entry.
3. Apply consequences in the same PR: authored spines edited directly; cuts to
   vendored text via the verbatim-minus patch flow (edit + make-patch.sh).
4. LOG line (`ruling`), integrity green, PR.

Resolution order: measured evidence beats assertion · exact enforceable value beats
a range · domain owner wins per the ownership matrix · ties get decided and logged.
