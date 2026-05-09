# Font Testing Workflow (Ultrawork)

This project uses the **Ultrawork** methodology for font engineering, characterized by autonomous, multi-agent parallel execution for QA and design refinement.

## Automated Testing Suite

### 1. Technical QA (Fontbakery)
We use `fontbakery` to check for Google Fonts compatibility, naming errors, and technical metadata correctness.
```bash
make test
```

### 2. Visual Regression (Diffenator)
We use `diffenator2` to compare Duyet Serif against its base (Instrument Serif) to ensure that widening and contrast adjustments haven't introduced regressions.

### 3. Agentic Design Refinement (Sisyphus Mode)
The "Ultrawork" approach involves using AI agents to programmatically adjust glyph geometry:
- **Widening:** Automated 15% horizontal expansion to match Anthropic Serif's grounded proportions (via `scripts/widen_font.py`).
- **De-contrasting:** Programmatic thickening of hairlines and serifs for better on-screen readability (via `scripts/refine_contrast.py`).
- **Tabularization:** Automatic enforcement of uniform widths for all digits (via `scripts/generate_vi.py` and `scripts/fix_vi_alignment.py`).

## Tools Used
- `fontmake`: For headless building.
- `gftools`: For metadata and fixing.
- `fontbakery`: For industry-standard testing.
- `diffenator2`: For visual diffing.
- `ultrawork`: AI orchestration logic for batch refinements.
