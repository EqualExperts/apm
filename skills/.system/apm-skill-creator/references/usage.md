Run `python scripts/create_skill.py --help` for options. The initializer requires complete user-supplied instructions and metadata; it creates a new skill only and refuses existing names across tiers. Run the validator after creation. Python 3.10 or newer is required.

The workflow is informed by the locally installed OpenAI skill-creator and its initializer and validator; the APM scripts are independently written. Upstream: https://github.com/openai/skills/tree/main/skills/.system/skill-creator . The local upstream revision was not identified, so no exact revision is claimed.
