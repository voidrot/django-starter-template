# 2. Testing Strategy

## Status

Accepted

## Context

End-to-end (E2E) testing is critical for ensuring application reliability. However, traditional E2E tests often rely on:
1.  **Visual Regression (Screenshots)**: These are extremely brittle. A pixel-shift in a font or a change in border-radius causes tests to fail, leading to alert fatigue and ignored test suites.
2.  **CSS Selectors**: These are tied to implementation details. Renaming a class from `btn-primary` to `btn-blue` breaks tests even if the button works perfectly.

## Decision

We have adopted **Playwright** with **Aria Snapshots** for our E2E testing strategy.

1.  **Aria Snapshots**: We verify the *Accessibility Tree* of the page using `expect(page.locator("body")).to_match_aria_snapshot()`. This ensures the semantic structure (headings, buttons, links, roles) exists and is correct, regardless of visual styling.
2.  **Pytest**: We use `pytest` as the test runner for both unit tests (`tests/`, `apps/**/tests.py`) and E2E tests (`e2e/`).

## Consequences

**Easier**:
- Refactoring CSS or changing themes (e.g., updating Tailwind colors) does *not* break tests.
- Tests enforce accessibility best practices by default (if it's not in the accessibility tree, the test can't see it).

**More Difficult**:
- Writing tests requires thinking about the semantic document structure rather than just visual appearance.
- Debugging snapshot failures requires inspecting the accessibility tree (which Playwright provides in failure logs).
