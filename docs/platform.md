# Platform Support

Deployment targets:

| Platform | Architecture | Status |
| --- | --- | --- |
| Windows | x86_64 (workstation) | Target |
| Linux | x86_64 (workstation) | Target |
| Linux (Raspberry Pi) | aarch64 (64-bit Raspberry Pi OS) | Target |
| Linux (Raspberry Pi) | armv7 (32-bit) | Untested — depends on third-party wheel availability |

The codebase is pure Python (no compiled extensions of our own), so
portability depends on third-party wheels for OpenCV, NumPy and PyTorch.

!!! warning "Known limitation"
    The configured PyTorch CUDA index (`download.pytorch.org/whl/cu126`)
    serves Linux x86_64 only. Installs on Windows and ARM may require CPU
    wheels or index overrides. This will be addressed when implementation
    starts (see [Roadmap](roadmap.md), Phase 3).

## Install notes per platform

- **Windows x86_64 / Linux x86_64:** works out of the box; the CUDA index
  applies on Linux x86_64.
- **Linux ARM (Raspberry Pi, aarch64):** install may need CPU-only PyTorch
  wheels or an index override (see known limitation above); prefer 64-bit
  Raspberry Pi OS.
- **Linux ARM (armv7, 32-bit):** not tested; wheel availability for PyTorch
  and OpenCV is limited on 32-bit ARM.

Installation itself is identical on all platforms:

```bash
uv sync --group dev
```
