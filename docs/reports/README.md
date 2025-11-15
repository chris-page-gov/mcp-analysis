# Published Reports

Use this folder for finalized deliverables (Word documents, PDFs, regenerated Markdown). For every binary document add a sibling Markdown file summarizing the scope, sources, key findings, and prompt references.

Rebuild Markdown, LaTeX, and optional PDF outputs from a DOCX source with the automation helper:
```bash
uv run scripts/python/docx_export.py docs/reports/source.docx --pdf
```
Outputs default to the DOCX directory and use the `IRI-` prefix required for archival.

If `pandoc` warns about missing glyphs in PDF output (e.g., full-width brackets), install an appropriate TeX font bundle such as `texlive-lang-cjk` and re-run the export.
