# 10. Code Quality (Pre-commit)

## Status

Accepted

## Context

Consistent code style and formatting are essential for team collaboration. Relying on manual review for style nits wastes time. We need automated tools to enforce standards before code is even committed.

## Decision

We use **pre-commit** hooks to run:
1.  **Ruff**: An extremely fast Python linter and formatter (replaces Black, Isort, Flake8).
2.  **DjLint**: Linter and formatter for Django templates (HTML).

## Consequences

**Easier**:
- Code is automatically formatted on commit.
- CI pipelines fail less often on style issues.
- `Ruff` is fast enough to act as a "save hook" in editors.

**More Difficult**:
- Developers must `mise run install` to set up the hooks.
- Occasionally, strict linting rules might be annoying and require explicit ignores (`# noqa`).
