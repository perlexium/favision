# favision — FA Vision Jalisco

Automated, standardized analysis of Failure Analysis (FA) evidence for electronic
and semiconductor components — starting with cross-section images, using digital
image processing and computer vision to identify, segment and quantify voids,
cracks, thicknesses, dimensions and other anomalies.

FA Vision Jalisco reduces manual inspection, measurement and documentation work,
providing quantitative, traceable results as a support tool for the FA engineer.

!!! info "Project status"
    Pre-MVP / definition stage (Circuito 14). No functional product, users or
    commercial validation yet. See the [Roadmap](roadmap.md).

- Project site: [sites.google.com/alumnos.udg.mx/fa-vision-jalisco](https://sites.google.com/alumnos.udg.mx/fa-vision-jalisco)
- Demo (private): [sites.google.com/view/fa-vision-jalisco](https://sites.google.com/view/fa-vision-jalisco)

## What it does

Pipeline for the MVP, focused on cross-section images:

1. Preprocessing
2. Segmentation
3. Region-of-interest detection
4. Feature extraction
5. Quantitative measurement of defects and observable structures

## Roadmap summary

- **Phase 1 — MVP:** cross-section image analysis pipeline
- **Phase 2 — Validation:** with FA/Reliability specialists and potential users
- **Phase 3 — Platform:** Windows/Linux x86_64 + Raspberry Pi (ARM)
- **Phase 4 — ML:** scikit-learn / PyTorch, when data allows
- **Phase 5 — Multi-technique:** CSAM, X-Ray, microscopy correlation
- **Phase 6 — Productization:** reporting, UI, B2B licensing

Full detail in the [Roadmap](roadmap.md).

## Tech stack

- Python 3.10+
- OpenCV, NumPy, SciPy, scikit-image (image processing and analysis)
- Pandas (data handling and analysis)
- Matplotlib (result visualization)
- scikit-learn / PyTorch: evaluated later for machine learning tasks
- Managed with [uv](https://docs.astral.sh/uv/), developed with Git/GitHub

## Target market / model

B2B software for FA and Reliability laboratories and electronics/semiconductor
manufacturing companies, via licenses or subscriptions and specialized modules.

## Quick start

```bash
uv sync --group dev
uv run favision
uv run pytest
uv run ruff check src tests
uv run mypy src tests
uv run mkdocs serve
```

See [Getting Started](getting-started.md) for full commands and
[Platform Support](platform.md) for Windows/Linux/ARM notes.
