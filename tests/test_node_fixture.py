"""Reject ambiguous executable examples rather than running the wrong block."""
import unittest
from scripts.check_node_migration import extract_example


class NodeFixtureTests(unittest.TestCase):
    def test_single_block(self):
        self.assertEqual(extract_example("# Example\n\n```javascript\ncode\n```\n"), "code\n")

    def test_missing_or_multiple_blocks(self):
        for text in ("no code", "```javascript\na\n```\n```javascript\nb\n```\n"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                extract_example(text)
