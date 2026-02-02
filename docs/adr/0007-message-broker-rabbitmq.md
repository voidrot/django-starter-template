# 7. Message Broker (RabbitMQ)

## Status

Accepted

## Context

For background tasks (Celery), we need a robust message broker. While Redis is often used as a broker, it is primarily an in-memory datastore and can lose messages if not configured for persistence. For critical background tasks (emails, data processing), we need a dedicated broker that guarantees message delivery.

## Decision

We use **RabbitMQ** as the Celery broker.
We still use **Redis** as the Celery result backend and caching layer.

## Consequences

**Easier**:
- RabbitMQ is the industry standard for Celery and offers robust routing and reliability.
- Clear separation of concerns: Redis for Cache/Results, RabbitMQ for Queues.

**More Difficult**:
- Adds another service to the stack (handled via Docker Compose).
- Slightly more complex configuration than using Redis for everything.
