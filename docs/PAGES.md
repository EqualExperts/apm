# Catalogue website

The GitHub Pages site presents the provider's published capabilities with search, type filters, instruction previews and copyable APM installation commands. Its source is `site/`; Python build automation in `scripts/build_site.py` writes only the static publication files to ignored `dist/`. Browser interaction is embedded in the HTML; repository automation remains Python-only. No frontend dependency installation, backend, analytics or external fonts are required.

Install the build dependency with `python -m pip install -r scripts/requirements-site.txt`. Run `python scripts/build_site.py`, then `python -m http.server 8000 --directory dist` to preview locally. Run `python -m unittest discover -s tests -v` for build checks. Search and clipboard behaviour require a browser; clipboard access may require HTTPS or localhost. Copy failures leave the command visible for manual selection.

## Catalogue inputs

Capability cards have styled native checkboxes. The right-hand Your toolkit panel keeps the selected packages while visitors search or change filters, expands stack selections into unique packages, and generates marketplace registration followed by one install command per selected package. Visitors choose an assistant, remove individual packages or clear the selection, then copy the entire script. Selection is held only for the current page session and resets on reload. On narrow screens the panel follows the results. Commands are plain APM CLI invocations suitable for PowerShell, Bash and Zsh with APM already installed; the website never executes them.

For browser checks, install the optional Python `playwright` package and use an installed Microsoft Edge browser. With the preview server running, execute `python scripts/check_site_browser.py`. This checks search, URL state, the details dialog, assistant selection, clipboard copying and mobile overflow. Screenshots are written under ignored `dist/`; do not include those preview files in the publication artifact. Hosted CI currently runs the Python build tests, not this browser check.

Root `marketplace.json` remains the authoritative package list. The build reads each local package source and its `SKILL.md` or `*.prompt.md` files. It rejects invalid names, duplicate package names and missing or out-of-repository source paths. Only published marketplace entries appear; an unregistered prompt is not advertised as installable.

Optional named collections live in `catalogue/stacks/*.json`. Each record has nonempty string fields `name`, `title` and `description`, plus a nonempty `packages` array of unique package names present in the marketplace. The build rejects unknown members. These records are website selections, not native APM stack manifests: the detail view lists every member and generates one install command per package. No stacks are seeded or represented as approved merely to populate the interface. Future ownership, revision constraints and compatibility metadata should be added before presenting collections as maintained releases.

When no prompts or stacks have been published, those filters explain the empty state and link to contribution guidance. Cards use a compact 270px width (shrinking on narrower screens) and display the YAML frontmatter description from the capability source. Quoted, folded and literal multiline descriptions are supported through safe YAML parsing. Missing or empty descriptions fall back to the marketplace description; malformed frontmatter fails the build. Search covers these descriptions, the original marketplace descriptions, names, categories and included instruction text. Query and type filters are shareable through URL parameters.

## Publication

`.github/workflows/pages.yml` tests and builds pull requests, and deploys changes on `main` through GitHub Actions when Pages has been enabled. Actions are pinned to source revisions. The deployment uses the `github-pages` environment and a deployment-only Pages/OIDC permission grant. Repository admin settings must select GitHub Actions as the Pages build source.

Confirm the intended site audience before enabling Pages: a private repository does not by itself guarantee a private website. The artifact includes capability descriptions and instruction text. Repository source links retain GitHub's access controls. GitHub plan and organisation policy determine whether a private Pages site is available. Do not change repository visibility to enable hosting.

Deployment is gated by the repository Actions variable `PAGES_ENABLED`. After confirming the audience and configuring Pages, set it to `true` and dispatch the workflow. Until then, pushes run build checks and upload the artifact but skip publication.

The website helps consumers choose guidance. It does not install packages from the browser or establish cross-harness compatibility. Installation commands use the registered marketplace name and selected assistant; review source, access requirements and revisions before running them in a consuming project.
