# 3. Authentication UI

## Status

Accepted

## Context

We use `django-allauth` for its robust authentication flows (Signup, Login, Password Reset, Email Verification). However, its default templates are basic, unstyled HTML that does not match the project's design system.

## Decision

We override `django-allauth` templates with custom, **Tailwind CSS**-styled versions.

- **Location**: `templates/account/`
- **Styling**: Uses the standard UI components (cards, form inputs, buttons) defined in the project's design system.
- **Logic**: We retain the underlying logic and template tags from `allauth` but completely replace the HTML key structure.

## Consequences

**Easier**:
- The user experience is seamless; auth pages look exactly like the rest of the application.
- We have full control over the layout (e.g., centering the login form, adding responsiveness).

**More Difficult**:
- Upgrading `django-allauth` requires checking for breaking changes in their template logic or context variables, as our overrides might miss new features or security updates if we don't sync them.
