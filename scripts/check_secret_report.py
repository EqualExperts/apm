"""Fail CI on detect-secrets findings without printing secret values."""
import json
from pathlib import Path
import sys


def main():
    report = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    findings = report["results"]
    for filename, entries in sorted(findings.items()):
        for entry in entries:
            print(f"Secret finding: {filename}:{entry['line_number']} ({entry['type']})")
    return int(any(findings.values()))


if __name__ == "__main__":
    raise SystemExit(main())
