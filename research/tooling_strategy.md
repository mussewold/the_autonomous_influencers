**Tooling Strategy**

Purpose
- Provide a concise, actionable strategy to provision and operate local MCP "spokes" (stdio transport) for Project Chimera during development. The goal is predictable, declarative tooling for filesystem, git, and Postgres resources that map directly to MCP primitives: Resources, Tools, and Prompts.

Design Principles
- Declarative: Keep runtime manifests, migrations, and environment bindings as YAML/SQL under `specs/` so MCP servers can mount/load them reproducibly.
- Least privilege: Expose only required operations per tool (e.g., filesystem read/write limited to project files; git limited to branch/commit/log; Postgres limited to the transactional DB schema).
- Traceability: Version control specs and migrations; use GitOps flows for persona/prompt changes; audit DB migrations and agent task state changes.
- Testability: Provide lightweight verifiers (e.g., `scripts/verify_mcp_tools.py`) and integration tests that exercise tool discovery and basic operations.

MCP Topology (Local Development)
- Hub: developer workstation running the MCP Client and orchestration scripts; coordinates starting local stdio MCP servers.
- Spokes (stdio): three distinct MCP servers, each exposing a single concern via the MCP Tool interface:
  - Filesystem spoke (`specs/mcp/filesystem_mcp.yaml`): read/write access to project root and specific config files (`SOUL.md`, `AGENTS.md`).
  - Git spoke (`specs/mcp/git_mcp.yaml`): commit/branch/log/status operations for GitOps workflows.
  - Postgres spoke (`specs/mcp/postgres_mcp.yaml`): a database tool that loads `specs/db/schema.sql` using `POSTGRES_DSN` from `.env`.

Resources / Tools / Prompts Mapping
- Resources: declare underlying resources first (directory, git repo, postgres DSN/migrations). Keep them in `specs/` and reference them from tool manifests.
- Tools: expose minimal surface area per tool (e.g., a `filesystem_tool` with a read/write path list; a `git_tool` with allowed commands; a `postgres_tool` with migrations and a DB connection placeholder).
- Prompts: system and persona prompts used by agents live in `research/` or `specs/` (for example `specs/agents/*.md`) and are treated as read-only artifacts consumed by the MCP Client.

Postgres & Data Model
- Environment: load `POSTGRES_DSN` from `.env` for local dev.
- Schema: provide SQL migrations under `specs/db/` (current schema: `agent_tasks` table with JSONB `task` payload and `status` text index).
- Operations: Postgres MCP tool should support applying migrations and basic CRUD for task lifecycle states: `pending`, `in_progress`, `review`, `complete`.
- Backups & local snapshots: recommend using `pg_dump` and storing snapshots outside the repo.

Security & Compliance
- Non-custodial secrets: do not store private keys in the repo. Use `.env` for local development and a secrets store in CI.
- EU AI Act compliance: require automated self-disclosure metadata on any generated public content; make the disclosure module a standard tool or middleware.
- Data isolation: enforce separate DB schemas or prefixes per influencer "Soul" to prevent persona leakage while developing locally.

Developer Experience
- Quick start:
  1. Copy `.env.example` to `.env` and set `POSTGRES_DSN`.
  2. Start local Postgres (Docker or local), apply `specs/db/schema.sql`.
  3. Launch MCP stdio servers (orchestration scripts / wrappers).
  4. Run `python3 scripts/verify_mcp_tools.py` to confirm tool availability.
- Tool wrappers: provide small shell scripts or systemd user units to start each MCP server bound to the corresponding YAML manifest.
- Verification: use the provided verifier to `list_tools()` and execute a smoke operation for each tool (read `SOUL.md`, run `git status`, insert a sample `agent_task`).

CI / GitOps
- Keep `specs/` authoritative: CI should apply DB migrations and run the MCP tool verifier during integration tests.
- Persona changes: require PR reviews for edits to `SOUL.md`/`AGENTS.md` and gate deployments behind the GitOps flow.

Observability & Testing
- Instrument MCP servers to log requests and responses (structured JSON) to a local logs table in Postgres for audit and replay.
- Add unit/integration tests that mock the MCP client and verify prompts/resources are loaded and tools accept expected commands.

