# Install Technical Writer

Use these steps to install the writing skill from this handoff in Codex or Claude Code. The installer prints the path you need for the Python setup.

## Requirements

- A host with file access and code execution: Codex, filesystem-enabled ChatGPT desktop, Claude Code, or a Claude environment supporting custom skills and Python.
- Python 3.11 or later on macOS, Linux, or WSL, with the packages in `scripts/requirements-lock.txt`.
- Source facts, a draft, or project files appropriate to the requested task. Missing evidence stays visible.

An external model CLI is optional. The native evaluation workflow uses the model already available in your host.

## Get the source

```sh
git clone --branch docs/autonomous-implementation https://github.com/fatonsopa/ai-technical-writer.git technical-writer
cd technical-writer
```

You can also download and extract the repository ZIP, then open its `technical-writer` folder.

## Codex and ChatGPT desktop

```sh
python3 scripts/install_skill.py --host codex
```

The installer prints its destination, normally `~/.agents/skills/technical-writer`. Invoke `$technical-writer` in Codex or select `@technical-writer` in ChatGPT desktop. If discovery does not refresh, start a new session or restart the app.

## Claude Code

```sh
python3 scripts/install_skill.py --host claude-code
```

The normal destination is `~/.claude/skills/technical-writer`. Invoke `/technical-writer` in Claude Code. An existing installation is preserved; use `--destination NEW_FOLDER` to test a separate installation.

## Set up the Python environment

Change to the installed folder printed by the installer, then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-lock.txt
.venv/bin/python scripts/smoke_check.py
```

The self-check reports `passed: true`. It checks installed resources and exercises the document gate; it does not establish writing quality across all future inputs.

The repository is the complete skill. You can download its GitHub ZIP instead of cloning. For a Claude custom-skill upload, extract the repository, give the folder the name `technical-writer`, and compress that folder with your archive tool. Enable code execution in the host. See [Claude's upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Planned release installation

The commands below are release targets. Use the source installation above today. The release is planned for macOS, Linux and WSL. SpecDev needs Python 3.11+ for writing and Node.js 22.20.0+ for the locked OpenSpec 2.1.1 integration.

1. Install the CLI once. The primary route downloads the installer from this repository’s GitHub release. It selects a compatible release asset and verifies it against that release’s `SHA256SUMS` before replacing the installed version. The alternative npm command will become available after publication under the verified package name.

   ```sh
   install_dir=$(mktemp -d)
   curl -fsSL https://github.com/fatonsopa/ai-technical-writer/releases/latest/download/install.sh -o "$install_dir/install.sh" && sh "$install_dir/install.sh"
   ```

   Or, for the planned npm package:

   ```sh
   npm install -g @fatonsopa/specdev@latest
   ```

2. Run `specdev --version`. Check the version and executable path before continuing if a second copy is already on your PATH. Then make the skill available in the hosts you use:

   ```sh
   specdev host init --tools codex,claude
   ```

   You can select just one host. Setup reports its destination, any missing prerequisite and the exact invocation to use in a fresh session. This connects SpecDev to the hosts. To start an OpenSpec project, separately invoke `/specdev init` in Claude Code or `$specdev init` in Codex from the intended project. That request delegates to OpenSpec.

3. To upgrade, use the original install channel again, then run `specdev host update` to refresh the entries you selected. For removal, first run `specdev host remove`. Then use `npm uninstall -g @fatonsopa/specdev` for npm, or the owned launcher and release paths printed by the GitHub installer. Keep user edits, other skills and project documents.

To have an agent help, ask it to follow this section for your chosen hosts, check for an existing installation first, and report the version, destination and working invocation. [Release acceptance](../openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#install-the-release-and-connect-a-host) · [OpenSpec’s installation method](https://github.com/Fission-AI/OpenSpec/blob/v2.1.1/docs/installation.md)
