#!/usr/bin/env python3
"""render-report.py — turn a pe-verify report.json into report.html beside it.

Usage:  render-report.py <report.json> [--open] [--no-convert] [--out <path>]

  --out <path>   write the HTML somewhere other than beside the JSON; media paths are
                 rewritten relative to that location, so the media files stay where
                 they are (the run folder) and still resolve.

Steps: validate (same rules as validate-report.py) → optionally convert webm
recordings to mp4 when ffmpeg is available (browsers play mp4 reliably) → inject the
report into the template → write report.html next to the JSON → print the path
(and open it with --open). Media paths in the JSON are relative to the JSON file, and
the HTML is written beside it, so they resolve unchanged.

If the JSON is invalid the script still writes report.html — one that lists every
validation problem in the report's own styling — and exits 1, so the user sees exactly
what to hand back to the agent. Agents should run validate-report.py first and never
ship a report that renders the error page.

Exit codes: 0 rendered · 1 rendered the error page (invalid JSON) · 2 unreadable input
"""
import json, os, pathlib, shutil, subprocess, sys, webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "assets", "report-template.html")
sys.path.insert(0, HERE)
from validate_report_lib import load, validate  # noqa: E402


def convert_webm(report, base_dir):
    """Replace .webm recordings with .mp4 siblings when ffmpeg can produce them.
    Returns (converted_paths, skipped_messages). The report dict is updated in place."""
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg: return [], []
    converted, skipped = [], []
    for it in report.get("items", []):
        v = (it.get("media") or {}).get("video")
        if not v or not v.lower().endswith(".webm"): continue
        src = os.path.join(base_dir, v); dst = os.path.splitext(src)[0] + ".mp4"
        if not os.path.exists(dst):
            proc = subprocess.run([ffmpeg, "-y", "-loglevel", "error", "-i", src, "-c:v", "libx264", "-pix_fmt", "yuv420p",
                                   "-movflags", "+faststart", "-crf", "28", "-preset", "veryfast", dst], capture_output=True, text=True)
            if proc.returncode != 0:
                skipped.append(f"ffmpeg failed on {v}: {proc.stderr.strip()[:200]}"); continue
            converted.append(dst)
        it["media"]["video"] = os.path.relpath(dst, base_dir)
    return converted, skipped


def rebase_media(report, base_dir, out_dir):
    """When report.html is written elsewhere, media paths must be relative to that place."""
    if os.path.abspath(base_dir) == os.path.abspath(out_dir): return
    fix = lambda p: os.path.relpath(os.path.join(base_dir, p), out_dir)
    for it in report.get("items", []):
        m = it.get("media")
        if not isinstance(m, dict): continue
        if m.get("video"): m["video"] = fix(m["video"])
        for c in m.get("checkpoints") or []: c["screenshot"] = fix(c["screenshot"])
        for s in m.get("screenshots") or []: s["path"] = fix(s["path"])


def inject(report):
    tpl = open(TEMPLATE, encoding="utf-8").read()
    payload = json.dumps(report).replace("<", "\\u003c")  # no "<" in the script block: covers </script> and <!--<script>
    return tpl.replace("__REPORT_JSON__", payload, 1)


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__); return 2
    src = os.path.abspath(argv[1]); base = os.path.dirname(src)
    if "--out" in argv:
        if argv.index("--out") + 1 >= len(argv): print("--out needs a path"); return 2
        out = os.path.abspath(argv[argv.index("--out") + 1])
    else:
        out = os.path.join(base, "report.html")
    report, err = load(src)
    if err:
        html = inject({"title": "pe-verify", "__errors": [{"path": "$", "message": err}]})
        open(out, "w", encoding="utf-8").write(html)
        print(f"unreadable: {err}\nwrote error page: {out}"); return 2
    errs = validate(report, base)
    if errs:
        html = inject({"title": report.get("title", "pe-verify") if isinstance(report, dict) else "pe-verify", "__errors": errs})
        open(out, "w", encoding="utf-8").write(html)
        print(f"invalid: {len(errs)} problem(s) — wrote error page: {out}")
        for e in errs: print(f"  {e['path']}: {e['message']}")
        if "--open" in argv: webbrowser.open(pathlib.Path(out).as_uri())
        return 1
    if "--no-convert" not in argv:
        converted, skipped = convert_webm(report, base)
        for c in converted: print(f"converted: {c}")
        for s in skipped: print(f"warning: {s}")
        if converted:  # keep the JSON on disk consistent with what was rendered
            with open(src, "w", encoding="utf-8") as f: json.dump(report, f, indent=2)
    rebase_media(report, base, os.path.dirname(out))
    open(out, "w", encoding="utf-8").write(inject(report))
    print(f"rendered: {out}")
    if "--open" in argv: webbrowser.open(pathlib.Path(out).as_uri())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
