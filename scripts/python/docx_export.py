"""Convert DOCX reports into Markdown, LaTeX, and optional PDF artefacts."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

DEFAULT_PREFIX = "IRI-"


def run_pandoc(args: list[str]) -> None:
    """Execute pandoc and raise on failure."""
    try:
        subprocess.run(args, check=True, text=True)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"pandoc failed with exit code {exc.returncode}") from exc


def build_targets(source: Path, destination: Path, export_pdf: bool) -> dict[str, Path]:
    """Compute output files for each requested format."""
    base = DEFAULT_PREFIX + source.stem
    targets: dict[str, Path] = {
        "markdown": destination / f"{base}.md",
        "latex": destination / f"{base}.tex",
    }
    if export_pdf:
        targets["pdf"] = destination / f"{base}.pdf"
    return targets


def convert(source: Path, destination: Path, export_pdf: bool) -> dict[str, Path]:
    """Convert the DOCX source into reusable formats."""
    destination.mkdir(parents=True, exist_ok=True)
    targets = build_targets(source, destination, export_pdf)

    run_pandoc([
        "pandoc",
        str(source),
        "--from",
        "docx",
        "--to",
        "gfm",
        "--output",
        str(targets["markdown"]),
    ])

    run_pandoc([
        "pandoc",
        str(source),
        "--from",
        "docx",
        "--to",
        "latex",
        "--output",
        str(targets["latex"]),
    ])

    if export_pdf:
        run_pandoc([
            "pandoc",
            str(source),
            "--from",
            "docx",
            "--pdf-engine",
            "xelatex",
            "--output",
            str(targets["pdf"]),
        ])

    return targets


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert DOCX reports into Markdown/LaTeX exports."
    )
    parser.add_argument("source", type=Path, help="Source DOCX file to convert.")
    parser.add_argument(
        "--dest",
        type=Path,
        default=None,
        help="Optional output directory (defaults to the source directory).",
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Also emit a PDF using xelatex.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = args.source.resolve()
    if not source.exists():
        raise FileNotFoundError(f"DOCX source not found: {source}")
    if source.suffix.lower() != ".docx":
        raise ValueError("Source file must have a .docx extension")

    dest = (args.dest or source.parent).resolve()
    targets = convert(source, dest, args.pdf)

    for label, path in targets.items():
        print(f"{label}: {path}")


if __name__ == "__main__":
    main()
