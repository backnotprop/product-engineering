#!/usr/bin/env python3
"""test-render.py — regression tests for the validator and renderer. Run: python3 test-render.py

Uses ../assets/sample/ as the fixture. No dependencies. Exit 0 = all pass.
"""
import copy, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(HERE, "..", "assets", "sample")
sys.path.insert(0, HERE)
from validate_report_lib import validate  # noqa: E402

fails = 0
def check(name, cond, detail=""):
    global fails
    print(("  ok   " if cond else "  FAIL ") + name + (f" — {detail}" if detail and not cond else ""))
    if not cond: fails += 1

def run(args, cwd=None):
    return subprocess.run([sys.executable] + args, capture_output=True, text=True, cwd=cwd)

def scratch():
    d = tempfile.mkdtemp(prefix="pe-verify-test-")
    for f in os.listdir(SAMPLE): shutil.copy(os.path.join(SAMPLE, f), d)
    return d

base = json.load(open(os.path.join(SAMPLE, "report.json")))

print("validator")
check("sample is valid", validate(base, SAMPLE) == [])
def errs_of(mutate):
    r = copy.deepcopy(base); mutate(r); return [e["path"] for e in validate(r, SAMPLE)]
check("missing required field", "$.items[0].summary" in errs_of(lambda r: r["items"][0].pop("summary")))
check("bad status enum", "$.items[0].status" in errs_of(lambda r: r["items"][0].update(status="passed")))
check("bad check_type enum", "$.items[0].check_type" in errs_of(lambda r: r["items"][0].update(check_type="ui")))
check("unknown top-level field", "$.bogus" in errs_of(lambda r: r.update(bogus=1)))
check("unknown item field", "$.items[0].extra" in errs_of(lambda r: r["items"][0].update(extra=1)))
check("wrong schema_version", "$.schema_version" in errs_of(lambda r: r.update(schema_version=2)))
check("feature run with two items", "$.items" in errs_of(lambda r: r["items"].append(copy.deepcopy(r["items"][0]) | {"id": "second"})))
check("duplicate ids", any("duplicate" in e["message"] for e in validate((lambda r: (r["items"].append(copy.deepcopy(r["items"][0])), r.update(mode="list"), r)[2])(copy.deepcopy(base)), SAMPLE)))
check("bad id pattern", "$.items[0].id" in errs_of(lambda r: r["items"][0].update(id="-bad id")))
check("missing video file", "$.items[0].media.video" in errs_of(lambda r: r["items"][0]["media"].update(video="nope.mp4")))
check("missing screenshot file", "$.items[0].media.checkpoints[0].screenshot" in errs_of(lambda r: r["items"][0]["media"]["checkpoints"][0].update(screenshot="nope.png")))
check("checkpoint time order", "$.items[0].media.checkpoints[1].t" in errs_of(lambda r: r["items"][0]["media"]["checkpoints"][1].update(t=0)))
check("negative checkpoint time", "$.items[0].media.checkpoints[0].t" in errs_of(lambda r: r["items"][0]["media"]["checkpoints"][0].update(t=-1)))
check("checkpoints without video", "$.items[0].media.checkpoints" in errs_of(lambda r: r["items"][0]["media"].pop("video")))
check("bad finding severity", "$.items[0].findings[0].severity" in errs_of(lambda r: r["items"][0]["findings"][0].update(severity="critical")))
check("empty items", "$.items" in errs_of(lambda r: r.update(items=[])))
check("media: null rejected", "$.items[0].media" in errs_of(lambda r: r["items"][0].update(media=None)))
check("title over 200 chars", "$.items[0].title" in errs_of(lambda r: r["items"][0].update(title="x"*201)))
check("label over 80 chars", "$.items[0].media.checkpoints[0].label" in errs_of(lambda r: r["items"][0]["media"]["checkpoints"][0].update(label="x"*81)))
check("absolute media path", "$.items[0].media.video" in errs_of(lambda r: r["items"][0]["media"].update(video="/etc/hosts")))
check("quote in media path", "$.items[0].media.checkpoints[0].screenshot" in errs_of(lambda r: r["items"][0]["media"]["checkpoints"][0].update(screenshot='a".png')))
check("dotdot in media path", "$.items[0].media.screenshots[0].path" in errs_of(lambda r: r["items"][0]["media"]["screenshots"][0].update(path="../cp-4.png")))
check("bad ran_at", "$.ran_at" in errs_of(lambda r: r.update(ran_at="yesterday")))
check("findings not a list → one error", [e for e in errs_of(lambda r: r["items"][0].update(findings="oops"))] == ["$.items[0].findings"])
check("list run without selection", "$.selection" in errs_of(lambda r: r.update(mode="list")))
check("selective run without basis", "$.selection_basis" in errs_of(lambda r: r.update(mode="list", selection="selective")))
check("bad selection value", "$.selection" in errs_of(lambda r: (r.update(mode="list", selection="some"))))
check("selection in feature mode", "$.selection" in errs_of(lambda r: r.update(selection="all")))
check("basis without selective", "$.selection_basis" in errs_of(lambda r: r.update(mode="list", selection="all", selection_basis="diff")))
check("not-run outside a selective run", "$.items[0].status" in errs_of(lambda r: (r.update(mode="list"), r["items"][0].update(status="not-run"), r["items"][0].pop("media"))))
check("not-run with media", "$.items[0].media" in errs_of(lambda r: (r.update(mode="list", selection="selective"), r["items"][0].update(status="not-run"))))
check("selective run with not-run item is valid", validate((lambda r: (r.update(mode="list", selection="selective", selection_basis="diff main...HEAD, 3 files"), r["items"][0].update(status="not-run"), r["items"][0].pop("media"), r)[3])(copy.deepcopy(base)), SAMPLE) == [])
check("code item without media is valid", validate((lambda r: (r["items"][0].pop("media"), r["items"][0].update(check_type="code"), r)[2])(copy.deepcopy(base)), SAMPLE) == [])

print("validate-report.py CLI")
d = scratch()
r = run([os.path.join(HERE, "validate-report.py"), os.path.join(d, "report.json")]); check("valid → exit 0", r.returncode == 0, r.stdout + r.stderr)
bad = copy.deepcopy(base); bad["items"][0]["status"] = "nope"; json.dump(bad, open(os.path.join(d, "bad.json"), "w"))
r = run([os.path.join(HERE, "validate-report.py"), os.path.join(d, "bad.json")]); check("invalid → exit 1 with path", r.returncode == 1 and "$.items[0].status" in r.stdout, r.stdout)
r = run([os.path.join(HERE, "validate-report.py"), os.path.join(d, "bad.json"), "--json"])
check("--json output parses", r.returncode == 1 and json.loads(r.stdout)["valid"] is False)
open(os.path.join(d, "broken.json"), "w").write("{ not json")
r = run([os.path.join(HERE, "validate-report.py"), os.path.join(d, "broken.json")]); check("unreadable → exit 2", r.returncode == 2 and "not valid JSON" in r.stdout, r.stdout)
r = run([os.path.join(HERE, "validate-report.py"), d]); check("directory → exit 2, no traceback", r.returncode == 2 and "Traceback" not in r.stderr, r.stderr)
open(os.path.join(d, "bin.json"), "wb").write(b"\xff\xfe{}")
r = run([os.path.join(HERE, "validate-report.py"), os.path.join(d, "bin.json")]); check("non-UTF-8 → exit 2, no traceback", r.returncode == 2 and "Traceback" not in r.stderr, r.stderr)

print("render-report.py")
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "report.json"), "--no-convert"])
html = open(os.path.join(d, "report.html")).read()
check("valid → exit 0, report.html beside JSON", r.returncode == 0 and os.path.exists(os.path.join(d, "report.html")), r.stdout)
check("report JSON injected", '"toolbar-integrity"' in html and "__REPORT_JSON__" not in html)
check("media paths stay relative", '"recording.mp4"' in html and '"cp-4.png"' in html)
inj = copy.deepcopy(base); inj["title"] = 'a<!--<script>b</script>c'; json.dump(inj, open(os.path.join(d, "inj.json"), "w"))
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "inj.json"), "--no-convert", "--out", os.path.join(d, "inj.html")])
ihtml = open(os.path.join(d, "inj.html")).read(); start = ihtml.index("__REPORT__ =")
check("no '<' survives inside the injected JSON", r.returncode == 0 and "<" not in ihtml[start:ihtml.index(";", start)] and "\\u003c!--" in ihtml)
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "report.json"), "--no-convert", "--out"])
check("--out without a path → exit 2", r.returncode == 2 and "Traceback" not in r.stderr, r.stderr)
sub = os.path.join(d, "elsewhere"); os.makedirs(sub)
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "report.json"), "--no-convert", "--out", os.path.join(sub, "r.html")])
ohtml = open(os.path.join(sub, "r.html")).read()
check("--out elsewhere rewrites media paths", r.returncode == 0 and '"../recording.mp4"' in ohtml and '"../cp-4.png"' in ohtml, r.stdout)
check("--out elsewhere leaves the JSON untouched", json.load(open(os.path.join(d, "report.json")))["items"][0]["media"]["video"] == "recording.mp4")
check("template has the checkpoint player", 'class="bar"' in html and "checkpoints" in html)
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "bad.json"), "--no-convert"])
ehtml = open(os.path.join(d, "report.html")).read()
check("invalid → exit 1 and error page", r.returncode == 1 and "could not be rendered" in ehtml and "$.items[0].status" in ehtml, r.stdout)
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "broken.json"), "--no-convert", "--out", os.path.join(d, "broken.html")])
check("unreadable → exit 2 and error page", r.returncode == 2 and "not valid JSON" in open(os.path.join(d, "broken.html")).read(), r.stdout)

# list mode: 3 items from the fixture, one code item without media
lst = copy.deepcopy(base); lst["mode"] = "list"; lst["selection"] = "all"; lst["title"] = "Release QA"; lst["list_source"] = ".product/qa-list.md"
a = copy.deepcopy(base["items"][0]); a["id"] = "bun-version"; a["title"] = "Bun 1.3.11"; a["check_type"] = "code"; a["status"] = "flag"; a.pop("media")
b = copy.deepcopy(base["items"][0]); b["id"] = "remote-urls"; b["status"] = "fail"; b.pop("media")
c = copy.deepcopy(a); c["id"] = "install-paths"; c["title"] = "Install paths still diverge for Pi and OpenCode"; c["status"] = "not-run"; c["summary"] = "No change under install/ in this change set."; c.pop("findings", None)
lst["items"] += [a, b, c]; lst["selection"] = "selective"; lst["selection_basis"] = "diff main...HEAD, 14 files"; json.dump(lst, open(os.path.join(d, "list.json"), "w"))
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "list.json"), "--no-convert", "--out", os.path.join(d, "list.html")])
lhtml = open(os.path.join(d, "list.html")).read()
check("list run renders", r.returncode == 0 and '"mode": "list"' in lhtml.replace('"mode":"list"', '"mode": "list"'), r.stdout)

# sparse items: optional fields absent everywhere the template reads them
sparse = copy.deepcopy(base); it = sparse["items"][0]; it["status"] = "fail"; it.pop("findings"); it.pop("checked_by"); it["media"].pop("checkpoints"); it["media"].pop("screenshots")
sparse.pop("repo"); sparse.pop("commit"); json.dump(sparse, open(os.path.join(d, "sparse.json"), "w"))
check("sparse report validates", validate(sparse, d) == [])
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "sparse.json"), "--no-convert", "--out", os.path.join(d, "sparse.html")])
check("sparse report renders", r.returncode == 0, r.stdout)

# runtime checks in a real browser when playwright is available (python package or npx)
def browser_checks():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None
    results = {}
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(); errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        def load(f):
            errors.clear(); pg.goto("file://" + os.path.join(d, f)); pg.wait_for_timeout(150)
        load("sparse.html"); results["sparse: feature viewer renders without JS errors"] = not errors and pg.locator(".player").count() == 1
        load("list.html")
        pg.click('.pill[data-f="status"][data-v="pass"]'); pg.wait_for_timeout(50)
        results["list: filtering out failed rows raises nothing"] = not errors and pg.locator(".row").count() >= 1
        pg.click('.pill[data-clear]'); pg.wait_for_timeout(50)
        results["list: selective run shows the not-run pill and meta"] = pg.locator('.pill[data-v="not-run"]').count() == 1 and "selective run · diff main...HEAD, 14 files" in pg.inner_text("header.run .meta")
        pg.click('.pill[data-f="status"][data-v="not-run"]'); pg.wait_for_timeout(50)
        results["list: not-run filter isolates the deselected row"] = not errors and pg.locator(".row").count() == 1 and "not run" in pg.inner_text(".row .st").lower()
        pg.click('.pill[data-clear]'); pg.fill("#q", "bun"); pg.wait_for_timeout(50)
        results["list: search that hides the fail row raises nothing"] = not errors and pg.locator(".row").count() == 1
        r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "bad.json"), "--no-convert", "--out", os.path.join(d, "err.html")])
        load("err.html"); results["error page: jump button hidden"] = pg.evaluate("getComputedStyle(document.getElementById('jumpbtn')).display") == "none"
        pg.keyboard.press("j"); pg.wait_for_timeout(50); results["error page: J raises nothing"] = not errors
        load("inj.html"); results["injected title renders as text"] = not errors and "a<!--<script>b</script>c" in pg.inner_text("h1")
        # screenshot lightbox: click opens, caption + count, arrows navigate, Esc closes
        run([os.path.join(HERE, "render-report.py"), os.path.join(d, "report.json"), "--no-convert", "--out", os.path.join(d, "feat.html")])
        load("feat.html")  # a feature run: the screenshots card is already visible
        pg.click(".shots .shot"); pg.wait_for_timeout(100)
        results["lightbox: opens on screenshot click"] = not errors and pg.evaluate("document.getElementById('lightbox').open") and pg.get_attribute("#lb-img", "src") != ""
        first = pg.get_attribute("#lb-img", "src")
        pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(50)
        results["lightbox: arrow moves to the next shot"] = pg.get_attribute("#lb-img", "src") != first and "2 / 2" in pg.inner_text("#lb-count")
        pg.keyboard.press("Escape"); pg.wait_for_timeout(50)
        results["lightbox: Esc closes"] = not errors and not pg.evaluate("document.getElementById('lightbox').open")
        b.close()
    return results
bc = browser_checks()
if bc is None: print("browser checks skipped (pip install playwright && playwright install chromium)")
else:
    print("browser (playwright)")
    for k, v in bc.items(): check(k, v)

shutil.rmtree(d)
print(f"\n{'ALL PASS' if not fails else str(fails) + ' FAILED'}")
sys.exit(1 if fails else 0)
