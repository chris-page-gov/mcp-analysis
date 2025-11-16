# GovUK MCP Server

This example tracks a fork of Steve Chan's MCP server implementation maintained under [chris-page-gov/GovUK-MCP](https://github.com/chris-page-gov/GovUK-MCP). The service exposes a set of Gov.UK data sources via the Model Context Protocol so that compliant AI clients can explore policy guidance, service documentation, and organisational metadata.

## Repository Snapshot

- **Upstream fork:** `external/govuk-mcp`
- **Primary language:** Python (FastAPI) with MCP server scaffolding
- **Notable integrations:** GOV.UK content API, GOV.UK Search, GOV.UK departments and policy indexes
- **Latest update (2025-11-16):** Rate limiting now wraps all registered tools via `ToolRegistry.register`; per-tool quotas live in `gov_uk_mcp/tool_definitions.py` on branch `crpage`.
- **Reason for inclusion:** Represents a production-inspired implementation that balances public-sector governance requirements with MCP's tool abstraction model.

## Local Usage

1. Ensure the submodule is present:
   ```bash
   git submodule update --init --recursive external/govuk-mcp
   ```
2. Check out the working branch that carries the latest assessment fixes:
   ```bash
   cd external/govuk-mcp
   git checkout crpage
   ```
3. Follow the upstream README inside `external/govuk-mcp` to install dependencies and run the server locally. For quick experiments inside the devcontainer:
   ```bash
   uv sync
   uv run python src/server.py
   ```
4. Connect an MCP-compatible client (e.g., Anthropic's Claude desktop app or the OpenAI Apps SDK) using the host/port described in the upstream docs.

## Evaluation Checklist

Use `assessment.md` in this folder to capture findings that map back to MCP specification clauses, security posture, observability, and operational fit. Key investigation areas:

- Authentication, authorization, and auditing boundaries
- Tool discovery metadata completeness (prompts, schemas, human descriptions)
- Error handling and rate limiting behaviour under load
- Deployment ergonomics for constrained public-sector environments

When contributing fixes upstream, prefer opening pull requests on `chris-page-gov/GovUK-MCP` and updating the submodule reference here after merges.
