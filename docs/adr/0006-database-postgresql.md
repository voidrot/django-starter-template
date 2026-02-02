# 6. Database (PostgreSQL)

## Status

Accepted

## Context

Django supports multiple databases, but production applications require a robust, ACID-compliant relational database with strong support for concurrent writes, JSON fields, and full-text search. SQLite is insufficient for high-concurrency usages, and MySQL often lacks some of the advanced features Django leverages.

## Decision

We use **PostgreSQL** as the primary database.

- **Driver**: `psycopg` (v3) for modern async support and performance.
- **Features**: We leverage Postgres-specific features like `JSONField`, `ArrayField`, and Full-Text Search where appropriate.

## Consequences

**Easier**:
- Seamless integration with Django (it's the preferred DB for Django).
- Excellent performance and reliability in production.
- Docker makes running it locally trivial.

**More Difficult**:
- Requires a running service (Docker) for local development, unlike SQLite which is a single file.
