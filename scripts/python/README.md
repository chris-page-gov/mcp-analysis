# Python Tooling

Python scripts in this folder should run via uv to guarantee repeatable environments:

```bash
uv run scripts/python/fetch_mcp_spec.py --help
```

Keep dependencies declared in `pyproject.toml` so `uv sync` captures them automatically.
