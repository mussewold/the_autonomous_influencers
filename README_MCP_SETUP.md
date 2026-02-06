# Local MCP Servers (stdio) — Project Chimera

Overview
- Three local MCP server configs are provided in `specs/mcp/`:
  - `filesystem_mcp.yaml` — filesystem tool (read/write) for project files like `SOUL.md` and `AGENTS.md`.
  - `git_mcp.yaml` — git tool (commit/branch/log) for GitOps.
  - `postgres_mcp.yaml` — Postgres DB tool; reads `POSTGRES_DSN` from `.env`.

Verification
1. Ensure your local MCP servers are running with stdio transport and these configs mounted.
2. Install dependencies (if needed):
```bash
pip install python-dotenv mcp
```
3. Run the verifier:
```bash
python3 scripts/verify_mcp_tools.py
```

Notes
- The verifier expects an `mcp` Python SDK providing `Client` with `list_tools()`.
- The Postgres MCP config refers to the environment variable `POSTGRES_DSN` — set this in `.env`.
