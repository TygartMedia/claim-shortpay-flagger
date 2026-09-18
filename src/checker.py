#!/usr/bin/env python3
"""Claim Short-Pay Flagger — carrier estimate in, short-pay flags out.

Pipeline:
    estimate PDF / photo set -> line-item + photo-density analysis -> flags with statutory hooks

Current state: scaffold. Analysis is a stub with TODO markers; the CLI and
the flag contract are real.
"""
import argparse
import json
import sys


def load_estimate(estimate_path):
    """TODO: parse the carrier estimate PDF into line items."""
    print(f"[stub] loading estimate {estimate_path} ...", file=sys.stderr)
    return {"line_items": [], "note": "STUB — PDF parsing not wired up"}


def analyze(estimate, photos):
    """TODO: flag missing line items, labor-hour density gaps, and scale
    problems against the short-pay checklist (see data/README.md),
    each flag carrying its statutory hook."""
    print("[stub] analyzing against the short-pay checklist ...", file=sys.stderr)
    return {
        "flags": [],
        "note": "STUB — needs the checklist and the photo-density pass",
    }


def main():
    ap = argparse.ArgumentParser(
        description="Claim Short-Pay Flagger: surface the short-pay before the file closes."
    )
    ap.add_argument("--estimate", required=True, help="Path to the carrier estimate PDF")
    ap.add_argument("--photos", nargs="*", default=[], help="Same-day damage photo paths")
    args = ap.parse_args()

    estimate = load_estimate(args.estimate)
    result = analyze(estimate, args.photos)
    print(json.dumps({"estimate": estimate, "result": result}, indent=2))


if __name__ == "__main__":
    main()
