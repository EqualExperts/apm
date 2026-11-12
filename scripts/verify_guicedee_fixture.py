"""Linux CI: verify pinned marketplace installation and GuicedEE fixture.

Run on a disposable runner; registration affects that runner's APM catalogue.
Release archive digests are pinned from the vendors' published checksums.
"""
import hashlib
from pathlib import Path
# Fixed, checksum-verified tools; no shell execution.
import subprocess  # nosec B404
import tarfile
import tempfile
import urllib.request


REVISION = "5b243e2ec3b332212c2755d4e1e46fc855446a41"  # pragma: allowlist secret - public commit
PACKAGES = ("guicedee-installer", "guicedee-creator", "guicedee-inject", "guicedee-client", "guicedee-vertx")


def unpack(url, digest, algorithm, destination):
    # URLs are fixed HTTPS vendor release locations supplied below, not user input.
    with urllib.request.urlopen(url, timeout=120) as response:  # nosec B310
        data = response.read()
    if hashlib.new(algorithm, data).hexdigest() != digest:
        raise ValueError("Release archive checksum mismatch")
    archive = destination / "release.tar.gz"
    archive.parent.mkdir(parents=True)
    archive.write_bytes(data)
    with tarfile.open(archive) as bundle:
        bundle.extractall(destination, filter="data")


def run(args, cwd):
    # The executable is a verified tool or Python; arguments are fixed paths/names.
    subprocess.run([str(arg) for arg in args], cwd=cwd, check=True, timeout=600)  # nosec B603


def main():
    import sys
    root = Path(__file__).resolve().parents[1]
    fixture = root / "tests/fixtures/quarkus-to-guicedee"
    with tempfile.TemporaryDirectory(prefix="guicedee-verification-") as directory:
        work = Path(directory)
        unpack("https://github.com/microsoft/apm/releases/download/v0.35.1/apm-linux-x86_64.tar.gz",
               "e7f06b9c80e26152ab579fe50d7dcd3d76ebbd8eacd44eed424e39880044eb3e", "sha256", work / "apm")  # pragma: allowlist secret - public archive hash
        unpack("https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/4.0.0-rc-7/apache-maven-4.0.0-rc-7-bin.tar.gz",
               "17b886c0ffb7ec225e514afa8179b3143d855d196cfbb4607ece6272a9b4f51501a389438ab6841b393a4b1391a1b714f07f450daba1951f53f732b400338184",  # pragma: allowlist secret - public archive hash
               "sha512", work / "maven")
        apm = next(path for path in (work / "apm").rglob("apm") if path.is_file())
        consumer = work / "consumer"
        consumer.mkdir()
        run([apm, "marketplace", "add", "GuicedEE/ai-rules", "--name", "guicedee-ai-rules", "--ref", REVISION], consumer)
        run([apm, "marketplace", "validate", "guicedee-ai-rules"], consumer)
        run([apm, "install", *(name + "@guicedee-ai-rules" for name in PACKAGES), "--target", "codex"], consumer)
        skills = consumer / ".agents/skills"
        for name in PACKAGES:
            for relative in ("SKILL.md", "agents/openai.yaml"):
                if not (skills / name / relative).is_file():
                    raise RuntimeError(f"Missing installed resource: {name}/{relative}")
        run([sys.executable, skills / "guicedee-creator/scripts/verify_guicedee_baseline.py", "--project-root", fixture], root)
        run([work / "maven/apache-maven-4.0.0-rc-7/bin/mvn", "--batch-mode", "--no-transfer-progress", "-f", fixture / "pom.xml", "verify"], root)


if __name__ == "__main__":
    main()
