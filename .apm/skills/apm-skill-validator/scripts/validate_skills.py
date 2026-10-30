"""Check APM skill structure. Requires PyYAML and Python 3.10+."""
import argparse
import re
from pathlib import Path
import yaml

def validate(path):
    errors, warnings = [], []
    name = path.name
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("invalid skill directory name")
    try:
        content = (path / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", content, re.S)
        if not match:
            raise ValueError("missing or malformed frontmatter")
        front = yaml.safe_load(match.group(1))
        if not isinstance(front, dict) or front.get("name") != name or not isinstance(front.get("description"), str) or not front["description"].strip():
            errors.append("frontmatter needs matching name and non-empty description")
        if re.search(r"(?im)^\s*#{1,6}\s*examples?\b|\bfor example\b", content[match.end():]):
            warnings.append("possible example in SKILL.md; review manually")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f"SKILL.md: {exc}")
    try:
        data = yaml.safe_load((path / "agents" / "openai.yaml").read_text(encoding="utf-8"))
        interface = data.get("interface", {}) if isinstance(data, dict) else {}
        for key in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(key), str) or not interface[key].strip():
                errors.append(f"missing interface.{key}")
        if isinstance(interface.get("short_description"), str) and not 25 <= len(interface["short_description"]) <= 64:
            errors.append("short_description must contain 25-64 characters")
        if isinstance(interface.get("default_prompt"), str) and "$" + name not in interface["default_prompt"]:
            errors.append("default_prompt must mention skill")
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"openai.yaml: {exc}")
    scripts = path / "scripts"
    if scripts.exists():
        for item in scripts.rglob("*"):
            if item.is_file() and item.suffix.lower() in (".sh", ".ps1", ".bat", ".cmd"):
                errors.append(f"non-Python script: {item.relative_to(path)}")
    warnings.append("review instructions, examples and compatibility claims manually")
    return errors, warnings

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Skill directory or APM skills directory")
    args = parser.parse_args()
    root = args.path
    if not root.is_dir():
        parser.error("path must be an existing directory")
    if root.name == "skills":
        paths = [p for p in root.iterdir() if p.is_dir()]
    else:
        paths = [root]
    failed = False
    seen = set()
    for path in sorted(paths):
        errors, warnings = validate(path)
        if path.name.casefold() in seen:
            errors.append("duplicate skill name")
        seen.add(path.name.casefold())
        for level, messages in (("ERROR", errors), ("WARN", warnings)):
            for message in messages:
                print(f"{level} {path}: {message}")
        failed |= bool(errors)
    print(f"Checked {len(paths)} skill(s)")
    return int(failed)

if __name__ == "__main__":
    raise SystemExit(main())
