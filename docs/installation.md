# Install SpecDev

Follow [Installation in the README](../README.md#installation) to install SpecDev on macOS, Linux or WSL and connect Codex, Claude Code or both. You need Python 3.11 or later for writing and Node.js 22.20.0 or later for OpenSpec.

<a id="planned-release-installation"></a>

## Install with npm

If you use npm, you can install the same command this way.

```sh
npm install -g @fatonsopa/specdev@latest
```

## Connect your coding tool

Run `specdev --version` in a terminal to check which release is installed. If you have a second copy on your PATH, check the executable path before continuing.

```sh
specdev host init --tools codex,claude
```

To connect one tool, use `--tools codex` or `--tools claude`. Setup prints the installation path and the command to use in a fresh session. To initialize OpenSpec for a project, open that project and enter `$specdev init` in Codex or `/specdev init` in Claude Code.

## Update or remove SpecDev

To update a GitHub installation, rerun the [installer](../README.md#installation), then run `specdev host update` to refresh the tools you connected. The installer verifies the release checksum before it replaces your copy.

For an npm installation, run the npm install command again, then run `specdev host update`.

To uninstall, run `specdev host remove`. For a GitHub installation, remove the launcher and release files listed by the installer. For npm, run `npm uninstall -g @fatonsopa/specdev`. Keep your project documents and any entries you edited.

### Maintain the OpenSpec runtime

SpecDev pins OpenSpec in `tools/openspec/package.json` and its lockfile, and installs that exact version with `npm ci` the first time you use an OpenSpec command. From the installed skill folder, use its Python environment:

- `.venv/bin/python scripts/openspec_runtime.py --check` compares the pin, the lockfile and the installed CLI. SpecDev refuses to run OpenSpec while they disagree.
- `--preview NEW_PACKAGE_JSON NEW_LOCK` shows which files an upgrade would replace and which it keeps. `--upgrade` with the same files installs them and keeps the prior pair in `tools/openspec/.previous`; `--restore` puts that pair back.
- `--remove` deletes only the installed runtime (`node_modules`). The manifest, the lockfile and any other file stay.

Dependabot proposes OpenSpec updates as pull requests. A proposal doesn't change the pin until a maintainer reviews it against the release notes and merges it.

## Install from the source checkout

The source installer below installs the `specdev` skill and a small `technical-writer` entry that keeps the former name working. The installer prints both paths and the path for Python setup.

- A host with file access and code execution: Codex, filesystem-enabled ChatGPT desktop, Claude Code, or a Claude environment supporting custom skills and Python.
- Python 3.11 or later on macOS, Linux, or WSL, with the packages in `scripts/requirements-lock.txt`.
- Source facts, a draft, or project files appropriate to the requested task. Missing evidence stays visible.

An external model CLI is optional. The native evaluation workflow uses the model already available in your host.

### Get the source

```sh
git clone --branch docs/autonomous-implementation https://github.com/fatonsopa/ai-technical-writer.git technical-writer
cd technical-writer
```

You can also download and extract the repository ZIP, then open its `technical-writer` folder.

### Codex and ChatGPT desktop

```sh
python3 scripts/install_skill.py --host codex
```

The installer prints its destination, normally `~/.agents/skills/specdev`. Invoke `$specdev` in Codex or select `@specdev` in ChatGPT desktop; `$technical-writer` still reaches the same writer. If discovery does not refresh, start a new session or restart the app.

### Claude Code

```sh
python3 scripts/install_skill.py --host claude-code
```

The normal destination is `~/.claude/skills/specdev`. Invoke `/specdev` in Claude Code; `/technical-writer` still reaches the same writer. An existing installation is preserved; use `--destination NEW_FOLDER` to test a separate installation.

### Set up the Python environment

Change to the installed folder printed by the installer, then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-lock.txt
.venv/bin/python scripts/smoke_check.py
```

The self-check reports `passed: true`. It checks installed resources and exercises the document gate; it does not establish writing quality across all future inputs.

The repository is the complete skill. You can download its GitHub ZIP instead of cloning. For a Claude custom-skill upload, extract the repository, give the folder the name `specdev`, and compress that folder with your archive tool. Enable code execution in the host. See [Claude's upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
