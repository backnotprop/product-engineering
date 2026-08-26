#!/usr/bin/env python3
"""validate-report.py — check a pe-verify report.json before rendering.

Usage:  validate-report.py <report.json>            exit 0 valid, 1 invalid, 2 unreadable
        validate-report.py <report.json> --json     machine-readable error list on stdout

The rules live in validate_report_lib.py (shared with render-report.py) and mirror
../assets/report.schema.json. Agents run this on their own JSON before rendering.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_report_lib import main
if __name__ == "__main__":
    sys.exit(main(sys.argv))
