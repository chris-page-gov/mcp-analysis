#!/usr/bin/env bash
set -euo pipefail

# Ensure uv is available for Python environment management.
if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

# Enable corepack and ensure pnpm is ready for TypeScript tooling.
if ! command -v pnpm >/dev/null 2>&1; then
    if command -v corepack >/dev/null 2>&1; then
        corepack enable pnpm
    else
        npm install --global pnpm
    fi
fi

# Synchronize Python dependencies into a local .venv managed by uv.
if [ -f "pyproject.toml" ]; then
    uv sync
fi

# Install Node/TypeScript dependencies.
if [ -f "package.json" ]; then
    pnpm install
fi
