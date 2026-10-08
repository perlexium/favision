# Roadmap — FA Vision Jalisco

> Status legend: 🟡 planned · 🔵 in progress · ✅ done · ⬜ not started
>
> The project is currently in the **pre-MVP / definition stage** (Circuito 14).
> Nothing below is implemented yet unless explicitly marked as done. Phases and
> dates are indicative and will be revised as validation progresses.

## Phase 0 — Definition ✅

- [x] Identify the problem: manual, tool-dependent FA analysis and documentation
- [x] Define the solution concept and initial architecture
- [x] Initial state-of-the-art review of FA automation work
- [x] Define target users, business model and staged development route
- [x] Project documentation (`README.md`, `pyproject.toml`, MkDocs site)

## Phase 1 — MVP: cross-section image analysis 🔵

Goal: first functional prototype for cross-section images.

- [ ] Project scaffolding and CI (lint, type check, tests)
- [ ] Image acquisition/loading module
- [ ] Preprocessing (normalization, filtering, contrast)
- [ ] Segmentation of regions of interest
- [ ] Feature extraction (voids, cracks, thicknesses, dimensions)
- [ ] Quantitative measurement and metrics
- [ ] Results export (quantitative, traceable data)
- [ ] Test with appropriate cross-section images

## Phase 2 — Validation

- [ ] Technical validation with FA and Reliability specialists
- [ ] Validate need and functionality with potential users
- [ ] Gather feedback and refine measurements/metrics
- [ ] Validate commercial need with companies in the sector

## Phase 3 — Platform and packaging

- [ ] Windows x86_64 workstation builds
- [ ] Linux x86_64 workstation builds
- [ ] Linux ARM (Raspberry Pi, aarch64) support
- [ ] Resolve the PyTorch CUDA-index limitation for Windows/ARM (CPU wheels / index overrides)
- [ ] Packaging and installation flow for B2B distribution

## Phase 4 — ML capabilities

> Evaluate only once sufficient labeled data exists and utility is validated.

- [ ] Dataset collection and labeling pipeline
- [ ] Evaluate scikit-learn for classification/detection tasks
- [ ] Evaluate PyTorch (deep learning) when the application requires it

## Phase 5 — Multi-technique FA integration

- [ ] CSAM image ingestion and analysis
- [ ] X-Ray image ingestion and analysis
- [ ] Microscopy image ingestion and analysis
- [ ] Cross-technique evidence correlation
- [ ] Integration with formats/software of specific inspection equipment

## Phase 6 — Reporting and productization

- [ ] Technical report generation with traceable results
- [ ] Platform UI
- [ ] Licensing/subscription model, specialized modules
- [ ] Commercial validation: pricing, first clients, revenue projection

## Contributing

Development workflow, tooling and commands are documented in
[`README.md`](README.md) and the [MkDocs site](docs/index.md).
