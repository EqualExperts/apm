"""Create a new APM skill. Python 3.10+, standard library only."""
import argparse
import json
import re
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    parser.add_argument("--root", type=Path, required=True, help="Repository root")
    parser.add_argument("--description", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--short-description", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--body-file", type=Path, required=True, help="UTF-8 Markdown instructions")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.name) or len(args.name) > 64:
        parser.error("name must be lowercase kebab-case and at most 64 characters")
    if not all(value.strip() for value in (args.description, args.title, args.short_description, args.prompt)):
        parser.error("metadata values must not be empty")
    if not 25 <= len(args.short_description) <= 64 or "$" + args.name not in args.prompt:
        parser.error("short description must be 25-64 characters and prompt must mention the skill")
    skills = args.root / ".apm" / "skills"
    if not skills.is_dir():
        parser.error("root must contain .apm/skills")
    if any(child.name.casefold() == args.name.casefold() for child in skills.iterdir() if child.is_dir()):
        parser.error("skill name already exists")
    body = args.body_file.read_text(encoding="utf-8").strip()
    if not body:
        parser.error("body must not be empty")
    target = skills / args.name
    target.mkdir()
    (target / "agents").mkdir()
    (target / "SKILL.md").write_text("---\nname: " + json.dumps(args.name) + "\ndescription: " + json.dumps(args.description) + "\n---\n\n" + body + "\n", encoding="utf-8")
    metadata = "interface:\n" + "".join("  " + key + ": " + json.dumps(value) + "\n" for key, value in (("display_name", args.title), ("short_description", args.short_description), ("default_prompt", args.prompt)))
    (target / "agents" / "openai.yaml").write_text(metadata, encoding="utf-8")
    print(target)

if __name__ == "__main__":
    main()
