# Use a lightweight Python image
FROM python:3.12-slim

# Install uv for high-speed dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory
WORKDIR /app

# Copy dependency files first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies without installing the project itself
RUN uv sync --frozen --no-install-project

# Copy the rest of the application (skills, tests, etc.)
COPY . .

# Set the entrypoint to uv to allow running scripts easily
ENTRYPOINT ["uv", "run"]