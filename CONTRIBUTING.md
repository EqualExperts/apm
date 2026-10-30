# Contributing

Contributions follow either of two routes: submit a pull request from a fork, or raise a detailed AI-created issue for maintainers to assess and implement. Start with [APM principles](docs/PRINCIPLES.md) and the [skill standard](docs/SKILL_STANDARD.md).

## Fork and pull request

1. Identify the problem, intended users and scope. Check for an existing capability before adding a new one.
2. Create a branch in your fork and make a focused change. Generalise engagement knowledge only with appropriate authorisation.
3. Document applicable provenance, licences, dependencies, maintainers, supported environments and limitations. Preserve attribution when adapting upstream work.
4. Verify the change at the appropriate level: structure and links, Python behaviour where changed, and representative skill invocation and outcomes where feasible. Record what was tested and what remains unverified.
5. Submit a pull request describing the problem, change, evidence and risks. Maintainers review accuracy, portability, maintainability and suitability for the shared catalogue.

## AI-created issue

Use an AI assistant to prepare a detailed issue that maintainers can assess and use to carry out the work. Review its accuracy before submission. Include:

- The problem, intended users and desired outcome, including why the change is useful.
- Scope, relevant existing capabilities, requirements, constraints and acceptance criteria.
- Relevant source links, evidence, provenance and applicable licences.
- Suggested approach, dependencies, compatibility considerations, risks and alternatives when known.
- Reproduction steps and expected and actual behaviour for defects.
- Open questions, assumptions and verification performed, clearly distinguishing observations from proposals.

Mark unknowns explicitly; do not present generated claims as verified facts. Maintainers decide how to address the issue and may request more information. An issue does not itself authorise external actions or guarantee implementation.

## Shared expectations

Do not submit client-confidential information, credentials, personal data or material that cannot be shared. Forks and installations update independently; coordinate upstream changes and downstream adoption explicitly. Report sensitive vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

Use Mermaid for diagrams. Include Mermaid source in Markdown and explain the relationships in accompanying text where needed.
