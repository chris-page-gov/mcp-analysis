# MCP Analysis Repository

This repository captures the evolution of the Model Context Protocol (MCP) specification, implementations, critiques, and adjacent technologies. It pairs deep research artifacts (including Word documents) with reproducible tooling in Python and TypeScript. A dev container ensures every contributor works with the same stack using [uv](https://github.com/astral-sh/uv) for Python dependency management and `pnpm` for Node/TypeScript tooling.

## Getting Started

1. **Open in Dev Container (Recommended)**
   - Install the Dev Containers extension and reopen this folder in the container. The startup script installs uv, configures `pnpm`, syncs Python dependencies into `.venv`, and installs Node dev dependencies.
2. **Local setup (optional)**
   - Install Python 3.11+, uv, Node.js 20+, and pnpm 8+.
   - Run `uv sync` to create `.venv` and install Python tooling.
   - Run `pnpm install` to install TypeScript dependencies.
3. **Validation**
   - Python lint: `uv run ruff check .`
   - TypeScript lint: `pnpm lint`.

## Repository Layout

- `docs/` — Primary documentation assets.
  - `prompts/` — Prompts that generated research or reports.
  - `research/` — Raw notes, interview transcripts, and sourced material.
  - `reports/` — Published deliverables, including Word documents (`.docx`).
  - `implementations/` — Case studies of good and bad MCP implementations.
  - `spec/` — Specification change logs, annotated readings, and cross references.
  - `alternatives/` — Technologies that compete with or complement MCP.
  - `templates/` — Templates for prompts, reports, and change logs.
  - `timeline/` — Chronological narratives of the MCP ecosystem.
- `scripts/python/` — Automation written in Python (e.g., cloning specification snapshots).
- `scripts/typescript/` — TypeScript scripts for data processing or tooling.
- `external/` — Optional working copies or submodules for upstream repositories (e.g., the canonical MCP spec).

## Capturing Word Documents

Place source `.docx` files under `docs/reports/`. Include a companion Markdown summary describing:

- Context and scope of the document.
- Data sources and prompt(s) used.
- Key conclusions or insights.

Use the prompt template in `docs/templates/prompt-template.md` to track inputs that generated the research artifacts.

## Tracking the Upstream MCP Specification

You have a few options depending on workflow:

The published specification is versioned at https://modelcontextprotocol.io/specification, with the latest release linked on the Versioning page.

- **Git submodule**: Add the upstream specification as `external/mcp-spec`.

   ```bash
   git submodule add https://github.com/modelcontextprotocol/modelcontextprotocol external/mcp-spec
   ```

   Update with `git submodule update --remote`. Summaries or diffs belong in `docs/spec/`.
- **Snapshot script**: Use `scripts/python/fetch_mcp_spec.py` to clone or refresh a local copy via GitHub's API, optionally converting Markdown to annotated Markdown.
- **Issue references**: When referencing upstream changes, link to tagged releases or specific pull requests inside the documentation to keep context durable.

Document each sync or notable change in `docs/spec/change-log.md` (see template in `docs/templates`).

## Tooling

### Python (uv)

- Dependencies are declared in `pyproject.toml` and installed with `uv sync`.
- Run Python utilities through `uv run`, for example `uv run scripts/python/fetch_mcp_spec.py --help`.
- Linting uses `ruff`; type checking uses `mypy`.

### TypeScript (`pnpm`)

- Project metadata and scripts live in `package.json`.
- `tsconfig.json` is configured for ES2022 modules with output in `dist/`.
- Linting uses `eslint` with `@typescript-eslint` rules; formatting uses `prettier`.

## Continuous Integration

`.github/workflows/ci.yml` provides a placeholder pipeline that installs dependencies and runs the lint/typecheck tasks with uv and pnpm. Extend it as automation requirements grow.

## Contributing

1. Open an issue describing the documentation or tooling change.
2. Work in the dev container or ensure local parity with the pinned tool versions.
3. Update relevant docs under `docs/` and keep prompts synchronized.
4. Run `pnpm lint` and `uv run ruff check .` before opening a pull request.

## Next Steps

- Populate `docs/reports/` with the initial Word document and create a matching Markdown summary.
- Configure `external/mcp-spec` as a submodule or run the provided fetch script to capture the upstream specification.
- Flesh out automation tasks for diffing spec changes and aligning them with internal research deliverables.
