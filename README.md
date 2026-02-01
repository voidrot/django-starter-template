# Django Starter Template

A production-ready, secure, and modern Django project template.

## Features

- **Modern Tooling**: Managed by `uv` for lightning-fast dependency resolution.
- **Dockerized**: Multi-stage `Dockerfile` and `compose.yml` for local development.
- **Strict Config**: `django-split-settings` and `environs` for robust configuration.
- **Authentication**: `django-allauth` pre-configured with a custom User model.
- **Best Practices**:
  - `src/` layout removed (root-level `apps/` and `config/`).
  - `ruff` for linting and formatting.
  - `pytest` for testing.
  - Security hardening in production settings.

## Getting Started

### Prerequisites

- Docker & Docker Compose
- [mise](https://mise.jdx.dev/) (for managing environment and tasks)

### Local Development (Shell)

1. **Install Dependencies**:
   ```bash
   mise run install
   ```

2. **Run Server**:
   ```bash
   mise run serve
   ```

### Common Tasks

- **Run Tests**: `mise run test`
- **Lint Code**: `mise run lint`
- **Format Code**: `mise run format`
- **Build Docker**: `mise run docker-build`

### Local Development (Docker)

1. **Build and Start**:
   ```bash
   mise run docker-up
   ```
   The app will be available at http://localhost:8000.

## Project Structure

- `apps/`: Django applications (e.g., `users`).
- `config/`: Configuration root.
  - `settings/`: Split settings (`base.py`, `development.py`, `production.py`).
- `tests/`: Pytest tests.
- `docker-compose.yml`: Local services (Postgres, Redis).
- `pyproject.toml`: Dependencies and tool config.

## Settings

Configuration is split into `base.py`, `development.py`, and `production.py`.
Environment variables are handled via `environs`.

See `.env.example` for available variables.
