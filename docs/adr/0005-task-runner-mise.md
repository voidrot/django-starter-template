# 5. Task Runner (Mise)

## Status

Accepted

## Context

Projects often accumulate a mix of `Makefiles`, shell scripts, `npm` scripts, and documentation on how to set up the environment (install Python, Node, etc.). This leads to:
1.  "Works on my machine" issues.
2.  Fragmented knowledge of available commands.
3.  Manual management of tool versions (e.g., ensuring everyone is on Python 3.13).

## Decision

We use **mise** (formerly rtx) as our unified task runner and environment manager.

- **Configuration**: `mise.toml` defines all tasks and tools.
- **Tools**: It manages the versions of Python, Node.js, and other CLI tools ensuring everyone uses the exact same version.
- **Env Vars**: It loads `.env` files automatically.

## Consequences

**Easier**:
- Onboarding is reduced to `mise run install` and `mise run serve`.
- Tasks are self-documenting in `mise.toml`.
- No need for global installs of tools; everything is scoped to the project.

**More Difficult**:
- `mise` must be installed on the host machine.
- Windows support (via WSL) or Docker is required, as distinct shell scripts are less portable than simple python commands, though `mise` abstracts much of this.
