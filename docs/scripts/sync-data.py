#!/usr/bin/env python3
"""sync-data.py — generate the docs site's data from the repository it documents.

Reads, from the repo root:
  skills/*/SKILL.md          name, description, modes table
  brand/cards/*.svg          the card words: verb headline, sentence, mode line
  foundry/MANIFEST.json      every vendored file: upstream, path, pinned sha, class, skill
  foundry/LEDGER.md          rulings, and which upstreams each involves
  README.md                  the Sources table (the one-line "what's vendored" per author)
  NOTICE                     license notes (Steve Ruiz's permission record)

Writes:
  docs/src/data/skills.json
  docs/src/data/people.json
  docs/src/content/docs/people/<slug>.md      one generated page per author
  docs/src/content/docs/reference/<name>.md   reference files copied with a provenance line

Run from anywhere: python3 docs/scripts/sync-data.py. CI runs it and fails if the
generated files differ from what is committed (--check).
"""
import json, os, re, sys, xml.etree.ElementTree as ET
from html import unescape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DOCS = os.path.join(ROOT, "docs")
DATA = os.path.join(DOCS, "src", "data")
PEOPLE_DIR = os.path.join(DOCS, "src", "content", "docs", "people")
REF_DIR = os.path.join(DOCS, "src", "content", "docs", "reference")
KIT = "https://github.com/backnotprop/product-engineering/blob/main/"

SKILLS = ["product-engineering", "pe-design", "pe-build", "pe-review", "pe-verify", "pe-product-description", "pe-brand-assets"]

# upstream key -> person. The one hand-kept mapping; everything else is read.
PEOPLE = {
    "emil-kowalski": {"name": "Emil Kowalski", "upstreams": ["emilkowalski/skills"], "private": ["animationsdev"], "match": r"emilkowalski|emil\b|animationsdev"},
    "jakub-krehel": {"name": "Jakub Krehel", "upstreams": ["jakubkrehel/skills"], "match": r"jakubkrehel|jakub\b"},
    "julien-thibeaut": {"name": "Julien Thibeaut", "upstreams": ["ibelick/ui-skills"], "match": r"ibelick"},
    "plannotator": {"name": "Plannotator", "upstreams": ["plannotator/effective-html"], "match": r"plannotator|design-artifact"},
    "vercel": {"name": "Vercel", "upstreams": ["vercel-labs/web-interface-guidelines", "vercel-labs/agent-skills"], "match": r"vercel"},
    "leon": {"name": "Leon", "upstreams": ["Leonxlnx/taste-skill"], "match": r"leonxlnx|taste v2|taste-skill|gpt-taste"},
    "steve-ruiz": {"name": "Steve Ruiz", "upstreams": ["steveruizok/product-description"], "match": r"steveruiz"},
    "paul-bakaus": {"name": "Paul Bakaus", "upstreams": ["pbakaus/impeccable"], "match": r"impeccable|pbakaus"},
}
REFERENCES = [
    ("report-contract", "skills/pe-verify/references/report-schema.md", "The report contract", "The JSON a pe-verify run produces, and the rules the validator enforces."),
    ("design-md", "skills/pe-design/references/understand/design-format.md", "DESIGN.md", "The format pe-design writes and the other skills read."),
    ("approved-record", "skills/pe-review/references/fidelity.md", "The approved record", "What an approval under .product/approved/ holds, and how fidelity mode reads it."),
    ("qa-list", "skills/pe-verify/references/qa-list.md", "The QA list and the memories file", "Where pe-verify looks for the list, and the kit's home-folder note."),
]


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f: return f.read()


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    for line in (m.group(1) if m else "").splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1); fm[k.strip()] = v.strip()
    return fm, text[m.end():] if m else text


def modes_table(body):
    """Rows of the first table whose header starts with 'Mode' (or 'The user wants' for the router)."""
    rows, inside = [], False
    for line in body.splitlines():
        if line.startswith("| Mode") or line.startswith("| The user wants"):
            inside = True; continue
        if inside and line.startswith("| ---"): continue
        if inside and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                name = re.sub(r"\*\*|`", "", cells[0]).strip()
                rows.append({"mode": name, "when": cells[1], "load": cells[2] if len(cells) > 2 else ""})
        elif inside and not line.startswith("|"):
            break
    return rows


def card_words(skill):
    p = os.path.join(ROOT, "brand", "cards", f"{skill}.svg")
    if not os.path.exists(p): return {}
    texts = [unescape(t.text or "") for t in ET.parse(p).getroot().iter("{http://www.w3.org/2000/svg}text")]
    if len(texts) < 4: return {}
    return {"verb": texts[1], "sentence": texts[2], "modeline": texts[3]}


def sources_table():
    """README Sources table: upstream url -> what's vendored (one line)."""
    out = {}
    for line in read("README.md").splitlines():
        m = re.match(r"^\| \[([^\]]+)\]\(([^)]+)\) \| ([^|]+) \| ([^|]+) \|", line)
        if m: out[m.group(2).strip()] = {"label": m.group(1), "author": m.group(3).strip(), "carry": m.group(4).strip()}
    return out


def rulings():
    out = []
    text = read("foundry/LEDGER.md")
    for m in re.finditer(r"\*\*(L-\d+) · ([^*]+)\*\* — (.*?)\n\*\*Ruling:\*\* (.*?)(?=\n\n|\Z)", text, re.S):
        out.append({"id": m.group(1), "topic": m.group(2).strip(), "positions": m.group(3).strip(), "ruling": m.group(4).strip()})
    return out


def upstream_file_url(up_key, up, path, sha):
    url = up["url"].removesuffix(".git")
    if "gist.github.com" in url:
        return f"https://gist.github.com/steveruizok/{url.rsplit('/', 1)[-1]}/{sha}"
    return f"{url}/blob/{sha}/{path}"


def main(argv):
    manifest = json.loads(read("foundry/MANIFEST.json"))
    ups, files = manifest["upstreams"], manifest["files"]
    notice = read("NOTICE")
    src = sources_table()
    rules = rulings()

    # ---- skills ----
    skills = {}
    for s in SKILLS:
        fm, body = frontmatter(read(f"skills/{s}/SKILL.md"))
        mine = {p: e for p, e in files.items() if e.get("skill") == s}
        by_up = {}
        for p, e in mine.items():
            if e.get("private"): continue
            by_up.setdefault(e.get("upstream") or "authored", 0); by_up[e.get("upstream") or "authored"] += 1
        vendored = []
        for slug, person in PEOPLE.items():
            n = sum(by_up.get(u, 0) for u in person["upstreams"])
            if n: vendored.append({"person": person["name"], "slug": slug, "count": n})
        vendored.sort(key=lambda v: -v["count"])
        skills[s] = {
            "slug": s, "name": fm.get("name", s), "description": fm.get("description", ""), "license": fm.get("license", ""),
            **card_words(s),
            "modes": modes_table(body),
            "provenance": {"authored": by_up.get("authored", 0), "vendored": vendored,
                           "private": sum(1 for e in mine.values() if e.get("private")),
                           "total": sum(1 for e in mine.values() if not e.get("private"))},
        }

    # ---- people ----
    people = []
    for slug, person in PEOPLE.items():
        rows = []
        for p, e in files.items():
            if e.get("upstream") in person["upstreams"] and not e.get("private"):
                up = ups[e["upstream"]]
                rows.append({"path": p, "short": p.split("/references/", 1)[-1] if "/references/" in p else p.split("/", 2)[-1],
                             "class": e["class"], "skill": e.get("skill", ""), "upstream": e["upstream"], "upstream_path": e.get("upstream_path", ""),
                             "sha": e.get("pinned_sha", ""), "upstream_url": upstream_file_url(e["upstream"], up, e.get("upstream_path", ""), e.get("pinned_sha", "")),
                             "kit_url": KIT + p, "patched": bool(e.get("patch"))})
        rows.sort(key=lambda r: (r["skill"], r["path"]))
        by_class, by_skill = {}, {}
        for r in rows:
            by_class[r["class"]] = by_class.get(r["class"], 0) + 1
            by_skill[r["skill"]] = by_skill.get(r["skill"], 0) + 1
        private_n = sum(1 for e in files.values() if e.get("private") and e.get("upstream") in person.get("private", []))
        involved = [r for r in rules if re.search(person["match"], r["positions"] + " " + r["ruling"], re.I)]
        sources = []
        for u in person["upstreams"]:
            up = ups[u]; url = up["url"].removesuffix(".git")
            if "gist.github.com" in url: url = "https://gist.github.com/steveruizok/" + url.rsplit("/", 1)[-1]
            entry = src.get(url) or next((v for k, v in src.items() if k.rstrip("/") in url or url in k), None)
            sources.append({"key": u, "url": url, "license": up.get("license", ""), "license_note": up.get("license_note", ""),
                            "carry": entry["carry"] if entry else ""})
        people.append({"slug": slug, "name": person["name"], "sources": sources, "files": rows, "by_class": by_class, "by_skill": by_skill,
                       "private_files": private_n, "rulings": involved, "total": len(rows)})

    os.makedirs(DATA, exist_ok=True)
    out_skills = json.dumps(skills, indent=2, ensure_ascii=False) + "\n"
    out_people = json.dumps(people, indent=2, ensure_ascii=False) + "\n"

    # ---- generated pages ----
    pages = {}
    for i, p in enumerate(people):
        L = [f"---", f"title: {p['name']}", f"description: {p['sources'][0]['carry'].capitalize().rstrip('.')}.", f"sidebar:", f"  order: {i + 1}", f"---", ""]
        L.append(" · ".join(f"[{s['key']}]({s['url']}) ({s['license']})" for s in p["sources"]))
        L.append("")
        for s in p["sources"]:
            if s["license_note"]: L.append(f"{s['license_note']}"); L.append("")
        L.append(f"**Carried:** {p['total']} files, " + ", ".join(f"{n} {c}" for c, n in sorted(p["by_class"].items(), key=lambda x: -x[1])) + ", each hash-locked to a pinned upstream commit.  ")
        L.append("**Lives in:** " + " · ".join((f"[{s}](/skills/{s}) {n}" if s in SKILLS else f"{s} {n}") for s, n in sorted(p["by_skill"].items(), key=lambda x: -x[1])) + "  ")
        if p["private_files"]:
            L.append(f"**Not distributed:** {p['private_files']} files from the animations.dev course pack are mapped for owners to install locally and are never committed.  ")
        if p["rulings"]:
            L.append("**Rulings:** " + ", ".join(f"[{r['id']}](#{r['id'].lower()})" for r in p["rulings"]) + " involve this work; each is below.  ")
        L.append("**Watcher:** compared against upstream weekly; when a carried file changes upstream, an issue opens in the kit.")
        L.append("")
        if p["rulings"]:
            L.append("## Rulings"); L.append("")
            for r in p["rulings"]:
                L.append(f"### {r['id']} · {r['topic']}"); L.append("")
                L.append(f"{r['positions']}  "); L.append(f"**Ruling:** {r['ruling']}"); L.append("")
        L.append("## Receipts"); L.append("")
        L.append("Every row links to the upstream file at its pinned commit and to the kit's copy. Verbatim rows are the same bytes; verbatim-minus rows carry a recorded patch beside a pristine copy; distilled rows are authored from the source and say so.")
        L.append("")
        L.append("| File in the kit | Class | Skill | Upstream |"); L.append("| --- | --- | --- | --- |")
        for r in p["files"]:
            cls = r["class"] + (" (patched)" if r["patched"] else "")
            sk = f"[{r['skill']}](/skills/{r['skill']})" if r["skill"] in SKILLS else r["skill"]
            L.append(f"| [{r['short']}]({r['kit_url']}) | {cls} | {sk} | [{r['upstream_path']}]({r['upstream_url']}) |")
        L.append("")
        pages[os.path.join(PEOPLE_DIR, f"{p['slug']}.md")] = "\n".join(L)

    for i, (slug, path, title, desc) in enumerate(REFERENCES):
        body = read(path)
        entry = files.get(path, {})
        prov = "Authored in the kit." if entry.get("class", "authored") == "authored" else f"Carried from {entry.get('upstream')} ({entry.get('class')})."
        body = re.sub(r"^# .*\n", "", body, count=1)  # the page title replaces the file's H1
        pages[os.path.join(REF_DIR, f"{slug}.md")] = f"---\ntitle: {title}\ndescription: {desc}\nsidebar:\n  order: {i + 1}\n---\n\n{body.strip()}\n\n---\n\n{prov} Source: [{path}]({KIT}{path}), rendered as-is at build time.\n"

    if "--check" in argv:
        bad = []
        for path, content in [(os.path.join(DATA, "skills.json"), out_skills), (os.path.join(DATA, "people.json"), out_people), *pages.items()]:
            if not os.path.exists(path) or open(path, encoding="utf-8").read() != content: bad.append(os.path.relpath(path, ROOT))
        if bad:
            print("docs data is stale; run python3 docs/scripts/sync-data.py and commit:\n  " + "\n  ".join(bad)); return 1
        print(f"docs data: OK · {len(skills)} skills · {len(people)} people · {len(pages)} generated pages"); return 0

    open(os.path.join(DATA, "skills.json"), "w", encoding="utf-8").write(out_skills)
    open(os.path.join(DATA, "people.json"), "w", encoding="utf-8").write(out_people)
    os.makedirs(PEOPLE_DIR, exist_ok=True); os.makedirs(REF_DIR, exist_ok=True)
    for path, content in pages.items():
        open(path, "w", encoding="utf-8").write(content)
    print(f"docs data: wrote {len(skills)} skills · {len(people)} people · {len(pages)} generated pages")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
