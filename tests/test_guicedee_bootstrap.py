"""Exercise archive integrity and traversal rejection without external tools."""
import hashlib
import io
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch
from scripts.verify_guicedee_fixture import unpack


class GuicedeeBootstrapTests(unittest.TestCase):
    def test_bad_checksum_rejected_before_extraction(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "release"
            with patch("urllib.request.urlopen", return_value=io.BytesIO(b"invalid")):
                with self.assertRaisesRegex(ValueError, "checksum"):
                    unpack("https://example.invalid/archive", "0" * 64, "sha256", destination)
            self.assertFalse(destination.exists())

    def test_traversal_rejected_even_with_valid_checksum(self):
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
            entry = tarfile.TarInfo("../escape.txt")
            entry.size = 1
            archive.addfile(entry, io.BytesIO(b"x"))
        data = buffer.getvalue()
        with tempfile.TemporaryDirectory() as directory:
            with patch("urllib.request.urlopen", return_value=io.BytesIO(data)):
                with self.assertRaises(tarfile.FilterError):
                    unpack("https://example.invalid/archive", hashlib.sha256(data).hexdigest(), "sha256", Path(directory) / "release")
            self.assertFalse((Path(directory) / "escape.txt").exists())
