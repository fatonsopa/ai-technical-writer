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

## Install from the source checkout

The development checkout below uses the original `technical-writer` entry. The installer prints the path for Python setup.

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

The installer prints its destination, normally `~/.agents/skills/technical-writer`. Invoke `$technical-writer` in Codex or select `@technical-writer` in ChatGPT desktop. If discovery does not refresh, start a new session or restart the app.

### Claude Code

```sh
python3 scripts/install_skill.py --host claude-code
```

The normal destination is `~/.claude/skills/technical-writer`. Invoke `/technical-writer` in Claude Code. An existing installation is preserved; use `--destination NEW_FOLDER` to test a separate installation.

### Set up the Python environment

Change to the installed folder printed by the installer, then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-lock.txt
.venv/bin/python scripts/smoke_check.py
```

The self-check reports `passed: true`. It checks installed resources and exercises the document gate; it does not establish writing quality across all future inputs.

The repository is the complete skill. You can download its GitHub ZIP instead of cloning. For a Claude custom-skill upload, extract the repository, give the folder the name `technical-writer`, and compress that folder with your archive tool. Enable code execution in the host. See [Claude's upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
