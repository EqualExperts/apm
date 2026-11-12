"""Ensure secret scan findings cannot silently pass the CI gate."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from scripts.check_secret_report import main


class SecretReportTests(unittest.TestCase):
    def check_report(self, results):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            path.write_text(json.dumps({"results": results}), encoding="utf-8")
            output = io.StringIO()
            with patch("sys.argv", ["check", str(path)]), contextlib.redirect_stdout(output):
                status = main()
            return status, output.getvalue()

    def test_clean_report_passes(self):
        self.assertEqual(self.check_report({})[0], 0)

    def test_finding_fails_without_echoing_value(self):
        status, output = self.check_report({"example.txt": [{"line_number": 2, "type": "Test", "secret": "sensitive-value"}]})
        self.assertEqual(status, 1)
        self.assertIn("example.txt:2", output)
        self.assertNotIn("sensitive-value", output)
