# Copilot Working Notes

## Repository Status
- Documentation-first repo tracking MCP specification history, research, and tooling.
- Python automation managed by uv; TypeScript utilities managed by pnpm.
- Devcontainer provisions Python 3.11, Node 20, uv, pnpm, and the Pandoc/XeLaTeX toolchain (pandoc, texlive-latex-* packages, texlive-lang-cjk) plus the VS Code PDF viewer (`ms-vscode.pdf`).
- Example MCP implementation tracked as submodule under `external/govuk-mcp`, with evaluation notes in `docs/implementations/good/govuk-mcp/`.

## Critical Workflows
- Run Python scripts with `uv run` (e.g., `uv run scripts/python/fetch_mcp_spec.py`).
- Convert DOCX reports using `uv run scripts/python/docx_export.py <docx> --pdf`; outputs must keep the `IRI-` prefix and land beside the source file.
- After each conversion, update the related Markdown summary in `docs/reports/` with links to all artefacts and note any Pandoc warnings.
- Address XeLaTeX missing glyph warnings by ensuring `texlive-lang-cjk` remains installed (already covered in the devcontainer).

## Development Practices
- Use repository-absolute paths with file-edit tools (the workspace enforces absolute paths).
- Favor `apply_patch` or scripted rewrites for updates; avoid manual reformatting that breaks Ruff/Prettier rules.
- Keep dependencies pinned in `pyproject.toml` and rely on `uv sync` rather than ad-hoc `pip` installs.
- Run existing VS Code tasks for lint/type-check (`lint:python`, `typecheck:python`, `lint:typescript`, `typecheck:typescript`) to verify changes.

## Documentation Expectations
- Every binary research artefact requires a sibling Markdown summary capturing prompts, sources, and key findings.
- Record spec syncs and notable upstream changes in `docs/spec/change-log.md`.
- Update README sections when workflows or tooling change (e.g., new scripts or container dependencies).

## Communication Guidelines
- Work through checklist-style requests sequentially and note blockers immediately.
- Keep responses concise, action-oriented, and reference file paths with inline code formatting.
