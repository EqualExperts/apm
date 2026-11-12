"""Run the reviewed Node contract example using a temporary file."""
from pathlib import Path
import re
import shutil
import subprocess  # nosec B404
import tempfile


def extract_example(text):
    blocks = re.findall(r"^```javascript\n(.*?)^```", text, re.M | re.S)
    if len(blocks) != 1:
        raise ValueError("Expected exactly one JavaScript fixture")
    return blocks[0]


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / ".apm/skills/quarkus-to-nodejs/references/http-contract.md"
    node = shutil.which("node")
    if node is None:
        raise RuntimeError("Node.js is required")
    with tempfile.TemporaryDirectory(prefix="node-migration-") as directory:
        fixture = Path(directory) / "contract.test.mjs"
        fixture.write_text(extract_example(source.read_text(encoding="utf-8")), encoding="utf-8")
        # Fixed test command and reviewed repository fixture; no shell or external input.
        subprocess.run([node, "--test", str(fixture)], check=True, timeout=60)  # nosec B603


if __name__ == "__main__":
    main()
