#!/usr/bin/env python3
"""validate-report.py — check a pe-verify report.json before rendering.

Usage:  validate-report.py <report.json>            exit 0 valid, 1 invalid, 2 unreadable
        validate-report.py <report.json> --json     machine-readable error list on stdout

No dependencies. Implements exactly the rules in ../assets/report.schema.json (the
schema file is the contract; this validator is its executable form) plus two checks a
schema cannot express: media paths must exist relative to the report, and a feature
run has exactly one item. Agents run this on their own JSON before rendering.
"""
import json, os, re, sys

STATUS = {"pass", "fail", "flag", "skipped"}
CHECK = {"code", "browser", "mixed"}
SEV = {"high", "medium", "low", "info"}
MODE = {"feature", "list"}
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}([T ]\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:?\d{2})?)?$")


def bad_path(s):
    """Media paths are relative, inside the run folder, and safe in an HTML attribute."""
    if not isinstance(s, str) or not s.strip(): return "required relative path string"
    if s.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:[\\/]", s) or "://" in s: return "must be relative to the report folder, not absolute"
    if any(part == ".." for part in re.split(r"[\\/]", s)): return "must stay inside the report folder (no ..)"
    if any(c in s for c in '"<>'): return "must not contain quotes or angle brackets"
    return None


def validate(report, base_dir):
    """Return a list of {path, message} problems. Empty list means valid."""
    errs = []
    E = lambda path, msg: errs.append({"path": path, "message": msg})

    if not isinstance(report, dict):
        return [{"path": "$", "message": "report must be a JSON object"}]

    allowed_top = {"schema_version", "title", "repo", "commit", "ran_at", "mode", "list_source", "notes", "items"}
    for k in report:
        if k not in allowed_top: E(f"$.{k}", "unknown field")
    for k in ("schema_version", "title", "mode", "ran_at", "items"):
        if k not in report: E(f"$.{k}", "required")
    if report.get("schema_version") != 1: E("$.schema_version", "must be 1")
    if "title" in report and (not isinstance(report["title"], str) or not report["title"].strip()): E("$.title", "must be a non-empty string")
    elif "title" in report and len(report["title"]) > 200: E("$.title", "must be at most 200 characters")
    if "mode" in report and report["mode"] not in MODE: E("$.mode", f"must be one of {sorted(MODE)}")
    if "ran_at" in report and (not isinstance(report["ran_at"], str) or not ISO_RE.match(report["ran_at"])): E("$.ran_at", "must be an ISO 8601 date or date-time string")
    for k in ("repo", "commit", "notes"):
        if k in report and not isinstance(report[k], str): E(f"$.{k}", "must be a string")
    if "list_source" in report and report["list_source"] is not None and not isinstance(report["list_source"], str):
        E("$.list_source", "must be a string or null")

    items = report.get("items")
    if not isinstance(items, list) or not items:
        E("$.items", "must be a non-empty array"); return errs
    if report.get("mode") == "feature" and len(items) != 1:
        E("$.items", f"a feature run has exactly one item (got {len(items)})")

    seen = set()
    for i, it in enumerate(items):
        p = f"$.items[{i}]"
        if not isinstance(it, dict): E(p, "must be an object"); continue
        allowed = {"id", "title", "check_type", "status", "summary", "findings", "media", "checked_by"}
        for k in it:
            if k not in allowed: E(f"{p}.{k}", "unknown field")
        for k in ("id", "title", "check_type", "status", "summary"):
            if k not in it: E(f"{p}.{k}", "required")
        if "id" in it:
            if not isinstance(it["id"], str) or not ID_RE.match(it["id"]): E(f"{p}.id", "must match ^[A-Za-z0-9][A-Za-z0-9_-]*$")
            elif it["id"] in seen: E(f"{p}.id", f"duplicate id '{it['id']}'")
            else: seen.add(it["id"])
        if "title" in it and (not isinstance(it["title"], str) or not it["title"].strip()): E(f"{p}.title", "must be a non-empty string")
        elif "title" in it and len(it["title"]) > 200: E(f"{p}.title", "must be at most 200 characters")
        if "check_type" in it and it["check_type"] not in CHECK: E(f"{p}.check_type", f"must be one of {sorted(CHECK)}")
        if "status" in it and it["status"] not in STATUS: E(f"{p}.status", f"must be one of {sorted(STATUS)}")
        if "summary" in it and (not isinstance(it["summary"], str) or not it["summary"].strip()): E(f"{p}.summary", "must be a non-empty string")
        if "checked_by" in it and not isinstance(it["checked_by"], str): E(f"{p}.checked_by", "must be a string")

        if "findings" in it and not isinstance(it["findings"], list): E(f"{p}.findings", "must be an array")
        for j, f in enumerate(it.get("findings") if isinstance(it.get("findings"), list) else []):
            fp = f"{p}.findings[{j}]"
            if not isinstance(f, dict): E(fp, "must be an object"); continue
            for k in f:
                if k not in {"severity", "text", "evidence"}: E(f"{fp}.{k}", "unknown field")
            if f.get("severity") not in SEV: E(f"{fp}.severity", f"must be one of {sorted(SEV)}")
            if not isinstance(f.get("text"), str) or not f.get("text", "").strip(): E(f"{fp}.text", "required non-empty string")
            if "evidence" in f and not isinstance(f["evidence"], str): E(f"{fp}.evidence", "must be a string")

        if "media" in it:
            m = it["media"]; mp = f"{p}.media"
            if not isinstance(m, dict): E(mp, "must be an object (omit the key for code-only items)"); continue
            for k in m:
                if k not in {"video", "checkpoints", "screenshots"}: E(f"{mp}.{k}", "unknown field")
            if "video" in m:
                bp = bad_path(m["video"])
                if bp: E(f"{mp}.video", bp)
                elif not os.path.exists(os.path.join(base_dir, m["video"])): E(f"{mp}.video", f"file not found: {m['video']}")
            cps = m.get("checkpoints")
            if cps is not None:
                if not isinstance(cps, list): E(f"{mp}.checkpoints", "must be an array")
                else:
                    if "video" not in m and cps: E(f"{mp}.checkpoints", "checkpoints require media.video")
                    last = -1
                    for k, c in enumerate(cps):
                        cp = f"{mp}.checkpoints[{k}]"
                        if not isinstance(c, dict): E(cp, "must be an object"); continue
                        for kk in c:
                            if kk not in {"t", "label", "narration", "screenshot"}: E(f"{cp}.{kk}", "unknown field")
                        t = c.get("t")
                        if not isinstance(t, (int, float)) or isinstance(t, bool) or t < 0: E(f"{cp}.t", "must be a number ≥ 0 (seconds)")
                        elif t < last: E(f"{cp}.t", "checkpoints must be in ascending time order")
                        else: last = t
                        if not isinstance(c.get("label"), str) or not c.get("label", "").strip(): E(f"{cp}.label", "required non-empty string")
                        elif len(c["label"]) > 80: E(f"{cp}.label", "must be at most 80 characters")
                        if "narration" in c and not isinstance(c["narration"], str): E(f"{cp}.narration", "must be a string")
                        s = c.get("screenshot"); bp = bad_path(s)
                        if bp: E(f"{cp}.screenshot", bp)
                        elif not os.path.exists(os.path.join(base_dir, s)): E(f"{cp}.screenshot", f"file not found: {s}")
            shots = m.get("screenshots")
            if shots is not None:
                if not isinstance(shots, list): E(f"{mp}.screenshots", "must be an array")
                else:
                    for k, s in enumerate(shots):
                        sp = f"{mp}.screenshots[{k}]"
                        if not isinstance(s, dict): E(sp, "must be an object"); continue
                        for kk in s:
                            if kk not in {"path", "caption"}: E(f"{sp}.{kk}", "unknown field")
                        bp = bad_path(s.get("path"))
                        if bp: E(f"{sp}.path", bp)
                        elif not os.path.exists(os.path.join(base_dir, s["path"])): E(f"{sp}.path", f"file not found: {s['path']}")
                        if "caption" in s and not isinstance(s["caption"], str): E(f"{sp}.caption", "must be a string")
    return errs


def load(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f), None
    except FileNotFoundError:
        return None, f"file not found: {path}"
    except IsADirectoryError:
        return None, f"is a directory, not a report file: {path}"
    except (PermissionError, OSError) as e:
        return None, f"cannot read {path}: {e.strerror or e}"
    except UnicodeDecodeError:
        return None, f"not UTF-8 text: {path}"
    except json.JSONDecodeError as e:
        return None, f"not valid JSON: line {e.lineno} col {e.colno}: {e.msg}"


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__); return 2
    path = argv[1]; as_json = "--json" in argv
    report, err = load(path)
    if err:
        if as_json: print(json.dumps({"valid": False, "errors": [{"path": "$", "message": err}]}))
        else: print(f"invalid: {err}")
        return 2
    errs = validate(report, os.path.dirname(os.path.abspath(path)))
    if as_json:
        print(json.dumps({"valid": not errs, "errors": errs}, indent=2))
    elif errs:
        print(f"invalid: {len(errs)} problem(s) in {path}")
        for e in errs: print(f"  {e['path']}: {e['message']}")
    else:
        n = len(report["items"]); print(f"valid: {path} · {report['mode']} run · {n} item(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
