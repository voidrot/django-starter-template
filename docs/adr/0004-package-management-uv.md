# 4. Package Management (UV)

## Status

Accepted

## Context

Python package management and virtual environment creation can be slow and fragmented. Tools like `pip`, `virtualenv`, and `poetry` all solve parts of the problem but often suffer from performance bottlenecks or complex dependency resolution times. We need a tool that is fast, reliable, and handles both package installation and environment management.

## Decision

We use **uv** (by Astral) for all Python package management.

- **Lockfile**: `uv.lock` ensures deterministic builds.
- **Speed**: `uv` is significantly faster than pip or poetry for resolving dependencies and syncing environments.
- **Workflow**: We use `uv run` to execute commands in the virtual environment without needing to mutually activate it (though `mise` handles activation in shells).

## Consequences

**Easier**:
- CI/CD pipelines are much faster.
- Local setup is nearly instant (`uv sync`).
- Dependency resolution conflicts are handled explicitly and quickly.

**More Difficult**:
- Developers must install `uv` (handled by `mise`).
- Not the default "standard" (pip), so newcomers might need a brief introduction.
