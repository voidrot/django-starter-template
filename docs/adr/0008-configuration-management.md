# 8. Configuration Management

## Status

Accepted

## Context

Django's default `settings.py` is a monolithic file that often contains complex logic for switching between development and production environments. This makes it hard to maintain and prone to security errors (e.g., debug settings leaking into production).

## Decision

We use **django-split-settings** and **environs** for configuration.

1.  **Split Settings**: Settings are broken down into components (`base.py`, `production.py`, `development.py`) and modular files (e.g., `components/celery.py`). This allows for clean overrides and organization.
2.  **Environs**: We use `environs` to type-cast environment variables (e.g., `env.bool("DEBUG")`, `env.list("ALLOWED_HOSTS")`). This prevents string parsing errors and handles defaults gracefully.

## Consequences

**Easier**:
- Environment-specific logic is isolated (no `if DEBUG:` scattered everywhere).
- Production settings are strictly separated and secured by default.
- Adding new integrations (like Sentry or Celery) involves adding a single component file.

**More Difficult**:
- Understanding the load order of settings requires looking at `base.py`'s inclusion logic.
