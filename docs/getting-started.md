# Getting Started

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

## Install

Same commands on all supported platforms:

```bash
uv sync --group dev
```

Platform notes are covered in [Platform Support](platform.md).

## Usage

```bash
uv run favision
```

Entry point (`pyproject.toml`):

```toml
[project.scripts]
favision = "favision:main"
```

## Development

pytest-only tests, ruff, mypy strict, MkDocs Material + mkdocstrings (with `htmlproofer` link checking).

```bash
uv sync --group dev
uv run ruff check src tests
uv run ruff format --check src tests
uv run mypy src tests
uv run pytest
uv run mkdocs serve
uv run mkdocs build --strict
```

Tooling:

- `ruff` for lint + format, `target-version = "py310"`
- `mypy` in `strict` mode, `python_version = "3.10"`
- `pytest` with `testpaths = ["tests"]`, tests in `tests/test_*.py`
- `MkDocs` with `material` theme + `mkdocstrings[python]`, `htmlproofer` link checking, config in `mkdocs.yml`, pages in `docs/`

## Project structure

```text
favision/
├── src/favision/
│   ├── __init__.py
│   └── py.typed
├── tests/test_main.py
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   ├── platform.md
│   ├── roadmap.md
│   ├── references.md
│   ├── api.md
│   ├── authors.md
│   ├── assets/favicon.svg
│   └── stylesheets/extra.css
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── ROADMAP.md
├── REFERENCES.md
├── CHANGELOG.md
├── AUTHORS.md
├── CONTRIBUTORS.md
├── LICENSE.md
└── .gitignore
```
