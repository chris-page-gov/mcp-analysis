"""Utility for cloning or refreshing the upstream MCP specification.

The script wraps `git` so that Python and automation tooling can keep the
`external/mcp-spec` folder up to date without manually running Git commands.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from typing import Sequence

DEFAULT_REPO = "https://github.com/modelcontextprotocol/modelcontextprotocol.git"
DEFAULT_DEST = Path("external/mcp-spec")


def run(command: Sequence[str], *, cwd: Path | None = None) -> None:
    """Run a subprocess and fail fast on error."""
    completed = subprocess.run(command, cwd=cwd, check=False, text=True)
    if completed.returncode != 0:
        location = f" in {cwd}" if cwd else ""
        raise RuntimeError(f"Command {' '.join(command)} failed{location} with exit code {completed.returncode}")


def clone_or_update(repo: str, destination: Path) -> None:
    """Clone the specification repo or fetch updates if it already exists."""
    if destination.exists():
        run(["git", "fetch", "--all"], cwd=destination)
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        run(["git", "clone", repo, str(destination)])


def checkout(destination: Path, reference: str | None) -> None:
    """Checkout a specific ref if requested."""
    if reference is None:
        return
    run(["git", "checkout", reference], cwd=destination)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync the upstream MCP specification repository")
    parser.add_argument("--repo", default=DEFAULT_REPO, help="Git repository URL for the specification")
    parser.add_argument(
        "--dest",
        default=str(DEFAULT_DEST),
        help="Destination path relative to the project root",
    )
    parser.add_argument(
        "--ref",
        default=None,
        help="Optional git reference (branch, tag, or commit) to check out after syncing",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    destination = Path(args.dest)
    clone_or_update(args.repo, destination)
    checkout(destination, args.ref)


if __name__ == "__main__":
    main()
