# 9. Frontend Stack

## Status

Accepted

## Context

We want a modern, reactive user interface without the complexity and overhead of a full Single Page Application (SPA) architecture (React/Vue + API). The "Django + HTMX" stack offers a sweet spot of productivity and performance for this type of application.

## Decision

We use a "PA" (Progressive Enhancement) stack:

1.  **Django Templates**: Server-side rendering for the initial page load and SEO.
2.  **Tailwind CSS**: Utility-first CSS for rapid, maintainable styling without context-switching to CSS files.
3.  **HTMX**: For dynamic interactions (partial page updates, infinite scrolls, modal forms) without writing custom JavaScript.
4.  **Alpine.js** (Optional/Available): For purely client-side state (dropdowns, toggles) where a server round-trip isn't necessary.

## Consequences

**Easier**:
- No build step for JavaScript (HTMX/Alpine are dropped in scripts).
- No API synchronization issues (the backend returns HTML fragments directly).
- State remains on the server, simplifying logic.

**More Difficult**:
- Tailwind requires a build process (handled by `mise run serve`).
- Complex client-side interactivity (like a drag-and-drop kanban board) might be harder than in React, though still possible.
