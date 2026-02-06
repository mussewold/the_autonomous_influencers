.PHONY: setup test spec-check clean

# Standardize dependency installation
setup:
	@echo "🚀 Setting up Project Chimera environment..."
	uv sync
	@echo "✅ Setup complete."

# Run tests inside a fresh Docker container to ensure CloudOps compliance
test:
	@echo "🧪 Running failing tests in Docker (TDD Safety Net)..."
	docker build -t chimera-agent .
	docker run --rm chimera-agent pytest tests/

# Verify code alignment with SRS (searches for key mandatory files)
spec-check:
	@echo "🔍 Verifying alignment with Project Chimera SRS..."
	@test -f SOUL.md && echo "✅ SOUL.md found" || echo "❌ Missing SOUL.md"
	@test -d skills && echo "✅ skills/ directory found" || echo "❌ Missing skills/ directory"
	@grep -q "mcp" pyproject.toml && echo "✅ MCP SDK included" || echo "❌ MCP SDK missing"

clean:
	@echo "🧹 Cleaning up..."
	rm -rf .pytest_cache
	docker rmi chimera-agent