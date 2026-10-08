# favision — FA Vision Jalisco

[![Check](https://github.com/perlexium/favision/actions/workflows/check.yml/badge.svg)](https://github.com/perlexium/favision/actions/workflows/check.yml) [![Lint](https://github.com/perlexium/favision/actions/workflows/lint.yml/badge.svg)](https://github.com/perlexium/favision/actions/workflows/lint.yml) [![Test](https://github.com/perlexium/favision/actions/workflows/test.yml/badge.svg)](https://github.com/perlexium/favision/actions/workflows/test.yml) [![Docs](https://github.com/perlexium/favision/actions/workflows/docs.yml/badge.svg)](https://github.com/perlexium/favision/actions/workflows/docs.yml)

Automated, standardized analysis of Failure Analysis (FA) evidence for electronic
and semiconductor components — starting with cross-section images, using digital
image processing and computer vision to identify, segment and quantify voids,
cracks, thicknesses, dimensions and other anomalies.

FA Vision Jalisco reduces manual inspection, measurement and documentation work,
providing quantitative, traceable results as a support tool for the FA engineer.

- Project site: [sites.google.com/alumnos.udg.mx/fa-vision-jalisco](https://sites.google.com/alumnos.udg.mx/fa-vision-jalisco)
- Demo (private): [sites.google.com/view/fa-vision-jalisco](https://sites.google.com/view/fa-vision-jalisco)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- References: [`REFERENCES.md`](REFERENCES.md)
- Documentation: `uv run mkdocs serve` (pages in `docs/`)

## What it does

Pipeline for the MVP, focused on cross-section images:

1. Preprocessing
2. Segmentation
3. Region-of-interest detection
4. Feature extraction
5. Quantitative measurement of defects and observable structures

## Roadmap

Phased plan in [`ROADMAP.md`](ROADMAP.md). Highlights (future stages, not yet
implemented):

- Incorporate additional FA techniques: CSAM, X-Ray, microscopy, and others —
  integrating and correlating different sources of evidence.
- Evaluate machine learning (scikit-learn, and PyTorch when required) for
  specific classification or detection tasks, once sufficient data is available.
- Generate technical reports with traceable results.

## Status

Pre-MVP / definition stage (Circuito 14). The problem, solution concept and an
initial state-of-the-art review are done; there is no functional product, users
or commercial validation yet. Next steps: build the prototype, test with
appropriate cross-section images, and validate with FA and Reliability
specialists.

## Target market / model

B2B software for FA and Reliability laboratories and electronics/semiconductor
manufacturing companies, via licenses or subscriptions and specialized modules.

## Tech stack

- Python 3.10+
- OpenCV, NumPy, SciPy, scikit-image (image processing and analysis)
- Pandas (data handling and analysis)
- Matplotlib (result visualization)
- scikit-learn / PyTorch: evaluated later for machine learning tasks
- Managed with [uv](https://docs.astral.sh/uv/), developed with Git/GitHub

## Platform support

Deployment targets:

| Platform | Architecture | Status |
| --- | --- | --- |
| Windows | x86_64 (workstation) | Target |
| Linux | x86_64 (workstation) | Target |
| Linux (Raspberry Pi) | aarch64 (64-bit Raspberry Pi OS) | Target |
| Linux (Raspberry Pi) | armv7 (32-bit) | Untested — depends on third-party wheel availability |

The codebase is pure Python (no compiled extensions of our own), so
portability depends on third-party wheels for OpenCV, NumPy and PyTorch.

**Known limitation:** the configured PyTorch CUDA index
(`download.pytorch.org/whl/cu126`) serves Linux x86_64 only. Installs on
Windows and ARM may require CPU wheels or index overrides. This will be
addressed when implementation starts.

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

## Install

Same commands on all supported platforms:

```bash
uv sync --group dev
```

Platform notes:

- **Windows x86_64 / Linux x86_64:** works out of the box; the CUDA index
  applies on Linux x86_64.
- **Linux ARM (Raspberry Pi, aarch64):** install may need CPU-only PyTorch
  wheels or an index override (see known limitation above); prefer 64-bit
  Raspberry Pi OS.
- **Linux ARM (armv7, 32-bit):** not tested; wheel availability for PyTorch
  and OpenCV is limited on 32-bit ARM.

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

pytest-only tests, ruff, mypy strict, MkDocs Material + mkdocstrings.

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

## License

LGPL-3.0-or-later. See `LICENSE.md` for the full text.
