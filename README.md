# news-image-20261124

A 1024x1024 newspaper front-page poster summing up world news for Tuesday, 24 November 2026.

## Contents

- **`entry.png`**: The rendered newspaper front page featuring:
  - Masthead banner with date `"TUESDAY 24 NOVEMBER 2026"`
  - Lead story panel covering the COP31 climate talks collapse in Antalya, Turkey
  - Grid panels covering the Indonesia candy factory fire, Russia's warning to Estonia, the Sparta II drone attack in the Gulf of Finland, India's aid pledge for Nepal, and Carlos Alcaraz's ATP Finals victory.
- **`draw.py`**: Python script using Pillow and DejaVu Sans Bold to render the poster with precise font measurement text wrapping and custom geometric emblems.
- **`main.py`**: Python 3.13 standard-library deployment script that copies `entry.png` to `MAKEFUN_OUTPUT_DIR` (default `/output`) with integrity verification (SHA256 and size check) and robust path resolution relative to `__file__`.

## Usage

```bash
python3 draw.py
python3 main.py
```
