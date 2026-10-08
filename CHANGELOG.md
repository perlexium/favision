# Changelog

All notable changes to `favision` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
with CalVer-style pre-releases (`YYYYaN`).

## [Unreleased]

### Changed

- 

## [2026a0] - 2026-10-08

### Added

- Initial `src/`-layout package `favision` with typed `main()` entry point
  (`favision = "favision:main"`) and `py.typed` marker.
- pytest-only test suite in `tests/` (`testpaths = ["tests"]`).
- Ruff lint + format configuration (`target-version = "py310"`).
- Mypy `strict = true` configuration (`python_version = "3.10"`).
- MkDocs documentation with `material` theme and `mkdocstrings[python]`
  (`mkdocs.yml`, `docs/index.md`, `docs/api.md`).
- Project metadata in `pyproject.toml` managed with `uv` (`uv.lock`,
  `[dependency-groups] dev`, `uv_build` backend).
- `README.md`, `AUTHORS.md`, `.gitignore` for `uv` + Python + pytest +
  mypy + ruff + MkDocs.
- `LICENSE.md` with GNU Affero General Public License v3 or later
  (`AGPL-3.0-or-later`).

### Changed

- Minimum supported Python lowered to `>=3.10`
  (`requires-python = ">=3.10"`, Ruff `py310`, mypy `3.10`).
  Development interpreter remains pinned to 3.12 in `.python-version`.

[Unreleased]: https://github.com/perlexium/favision/compare/2026a0...HEAD
[2026a0]: https://github.com/perlexium/favision/releases/tag/2026a0
