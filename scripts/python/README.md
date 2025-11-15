# Python Tooling

Python scripts in this folder should run via uv to guarantee repeatable environments:
```bash
uv run scripts/python/fetch_mcp_spec.py --help
```

To convert DOCX research reports into reusable artefacts with IRI-prefixed filenames:
```bash
uv run scripts/python/docx_export.py docs/reports/source.docx --pdf
```

Keep dependencies declared in `pyproject.toml` so `uv sync` captures them automatically.
