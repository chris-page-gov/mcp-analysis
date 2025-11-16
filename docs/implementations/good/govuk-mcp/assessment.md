# GovUK MCP Assessment Log

| Field | Notes |
| --- | --- |
| Spec baseline | Python `mcp` client >=1.0.0 (aligns with late-2024 spec cut); confirm against 2025 spec revisions |
| Evaluators | Chris Page, GitHub Copilot |
| Last reviewed | 2025-11-16 (rate-limiting rollout) |

## 1. Context
- **Mission:** Deliver GOV.UK datasets and search functionality to MCP clients for policy research and service design.
- **Operating constraints:** Must run within UK government security baselines, with auditable access to public but rate-limited APIs.
- **Architecture notes:** Single-process Python server exposing 33 tools via the Anthropic `mcp` stdio adapter; relies on JSON text payloads rendered back to clients.

## 2. Setup Notes
- Clone submodule with `git submodule update --init external/govuk-mcp`.
- Install deps using `uv sync` (Python >=3.10); runtime also pulls `.env` secrets when present.
- Requires at minimum `COMPANIES_HOUSE_API_KEY` and `EPC_API_KEY`; optional `TFL_API_KEY` lifts journey-planner rate limits.
- Server entrypoint: `uv run python -m gov_uk_mcp.server`; tests via `uv run pytest`.
- Upstream README documents 33 tool commands and sample prompts for Claude Desktop.

## 3. MCP Contract Review
- **Tool registration:** Central `ToolRegistry` registers each tool with description and JSON schema; coverage exists for query params but lacks examples/usage hints for several complex tools (e.g., `plan_journey`, `search_cqc_providers`).
- **Session flow:** Relies on synchronous tooling executed via `asyncio.to_thread`; no streaming or background task management. Long-running API calls block responses.
- **Error semantics:** Errors returned as JSON strings embedded in `TextContent`; still human-readable but not rich MCP error objects. Missing differentiation between retriable vs fatal failures.
- **Rate limit integration:** `ToolRegistry.register` now applies the shared token-bucket decorator based on per-tool configuration; successful responses include remaining quota and reset metadata.
- **Validation:** `validation.py` provides strong input sanitisation for postcodes, company numbers, coordinates, etc., and sanitises outward-facing API errors.

## 4. Security & Governance
- No authentication/authorization layer; assumes desktop client runs in trusted environment. Need story for multi-tenant hub.
- `.env` secrets loaded via `python-dotenv`; repository does not ship sample `.env`, so deployment docs should emphasise secret storage.
- Logging limited to tool invocation names; no request/response auditing, redaction, or PII handling assurances.
- External API calls made over HTTPS but without configurable proxies or outbound allow-listing controls.

## 5. Operational Considerations
- Packaging: pure Python project; no container spec or deployment manifest. Would benefit from Dockerfile/Helm for reproducibility.
- Observability: no tracing/metrics; would need wrappers to emit Prometheus/OpenTelemetry data for production.
- Resilience: no retry/backoff strategy; reliance on direct `requests` calls with 10s timeout; thread offloading means concurrency limited by Python threads.
- Configuration: environment variables only; no config layering per environment.

## 6. Improvement Backlog
- [x] Apply `rate_limit` decorator to API-hitting tools and surface quota telemetry to clients (per-tool config in `tool_definitions.py`).
- [ ] Introduce structured MCP error objects (`ErrorResult`) instead of JSON strings.
- [ ] Document and automate `.env` management (sample file, secret-store guidance).
- [ ] Add container image or devcontainer task to run server for reviewers.
- [ ] instrument logging/metrics for API latency and failures.
- [ ] Evaluate tool coverage against 2025 MCP capability taxonomy (listing vs. actions, progressive disclosure, pagination).

> Update this log after each evaluation session to keep the case study actionable.
