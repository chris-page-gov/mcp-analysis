# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Because the project has not reached a tagged release yet, sections are grouped by date to capture daily milestones.

## [Unreleased]

### Added
- DOCX conversion workflow: `scripts/python/docx_export.py` emits IRI-prefixed Markdown, LaTeX, and optional PDF artefacts via Pandoc/XeLaTeX.
- Documentation updates covering the export helper, glyph warning handling, and regenerated artefact links in `README.md`, `docs/reports/README.md`, and `docs/reports/deep-research-02-summary.md`.
- Dev container bootstrap now provisions Pandoc, the XeLaTeX toolchain (including `texlive-lang-cjk`), and installs the `ms-vscode.pdf` extension for in-editor PDF previews.
- Expanded `.github/copilot-instructions.md` with guidance on conversion workflows, tooling expectations, and communication norms for future contributors.
- Added GovUK MCP fork as `external/govuk-mcp` submodule with accompanying case-study docs under `docs/implementations/good/govuk-mcp/`.

### Changed
- GovUK MCP case study: submodule branch `crpage` now enforces per-tool rate limiting via `ToolRegistry.register`, with documentation and assessment updated accordingly.

### Notes
- XeLaTeX still emits missing glyph warnings for full-width brackets when the necessary fonts are absent; installing `texlive-lang-cjk` resolves the issue during container setup.

## [2025-11-15] Tooling Stabilization

### Added
- Introduced `scripts/typescript/specReferences.ts` to provide canonical MCP specification metadata.
- Regenerated `uv.lock` to capture pinned Python dev dependencies managed by uv.

### Changed
- Pinned `ruff` and `mypy` under uv dependency groups to eliminate lint/type-check drift.

## [2025-11-15] Documentation Refresh

### Added
- Recorded deep-research artefact summaries under `docs/prompts/` and `docs/reports/`, including prompt provenance and PDF links.

### Changed
- Updated `scripts/python/fetch_mcp_spec.py` and related docs to reference the correct upstream MCP specification repository and portal URLs.

## [2025-11-15] Devcontainer Alignment

### Changed
- Switched the devcontainer base image to the standard Ubuntu variant to match automation expectations and simplify package provisioning.

## [2025-11-15] Initial Foundation

### Added
- Initial repository scaffold: documentation hierarchy, devcontainer bootstrap, CI workflow placeholder, Python/TypeScript tooling configuration, and lint/type-check VS Code tasks for the MCP analysis project.
