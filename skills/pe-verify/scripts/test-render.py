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

print("render-report.py")
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "report.json"), "--no-convert"])
html = open(os.path.join(d, "report.html")).read()
check("valid → exit 0, report.html beside JSON", r.returncode == 0 and os.path.exists(os.path.join(d, "report.html")), r.stdout)
check("report JSON injected", '"toolbar-integrity"' in html and "__REPORT_JSON__" not in html)
check("media paths stay relative", '"recording.mp4"' in html and '"cp-4.png"' in html)
check("script tag cannot be broken by content", "<\\/" in html or "</script" not in json.dumps(base))
check("template has the checkpoint player", 'class="bar"' in html and "checkpoints" in html)
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "bad.json"), "--no-convert"])
ehtml = open(os.path.join(d, "report.html")).read()
check("invalid → exit 1 and error page", r.returncode == 1 and "could not be rendered" in ehtml and "$.items[0].status" in ehtml, r.stdout)
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "broken.json"), "--no-convert", "--out", os.path.join(d, "broken.html")])
check("unreadable → exit 2 and error page", r.returncode == 2 and "not valid JSON" in open(os.path.join(d, "broken.html")).read(), r.stdout)

# list mode: 3 items from the fixture, one code item without media
lst = copy.deepcopy(base); lst["mode"] = "list"; lst["title"] = "Release QA"; lst["list_source"] = ".product/qa-list.md"
a = copy.deepcopy(base["items"][0]); a["id"] = "bun-version"; a["title"] = "Bun 1.3.11"; a["check_type"] = "code"; a["status"] = "flag"; a.pop("media")
b = copy.deepcopy(base["items"][0]); b["id"] = "remote-urls"; b["status"] = "fail"; b.pop("media")
lst["items"] += [a, b]; json.dump(lst, open(os.path.join(d, "list.json"), "w"))
r = run([os.path.join(HERE, "render-report.py"), os.path.join(d, "list.json"), "--no-convert", "--out", os.path.join(d, "list.html")])
lhtml = open(os.path.join(d, "list.html")).read()
check("list run renders", r.returncode == 0 and '"mode": "list"' in lhtml.replace('"mode":"list"', '"mode": "list"'))

shutil.rmtree(d)
print(f"\n{'ALL PASS' if not fails else str(fails) + ' FAILED'}")
sys.exit(1 if fails else 0)
