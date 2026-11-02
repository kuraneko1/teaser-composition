[日本語](README.md)

# Teaser Composition

A collection of skills for creating teaser images and key visuals in code, with attention to the scale of the subject, negative space, visual flow, and typography. It reads the compositional skeleton of reference artwork and adapts it to a new subject. The skills run as-is in DSH (DeepSeek Harness) and keep Codex-compatible metadata.

## Features

- Choose from 12 approaches: atmosphere, geometry, drafting, pixel, radial light, flow, editorial collage, specimen, object, orbit, scenic, and proof.
- Compare typefaces using the actual title and refine spacing, line breaks, and readability at smaller sizes.
- Use generated or supplied images only where a material is missing; control typography and layout in code.
- Each approach ships a starter renderer (Python + Pillow / CairoSVG) and example configuration.

## Installation

~~~bash
git clone https://github.com/kuraneko1/teaser-composition.git
cd teaser-composition
./install.sh
~~~

`install.sh` does three things:

1. Symlinks the 13 `skills/teaser-*` bundles into `~/.dsh/skills/`
2. Creates `.venv` and installs `requirements.txt` (Pillow, numpy, CairoSVG)
3. Writes the `~/.local/bin/teaser-render` wrapper

DSH watches the skill directory, so no restart is needed: `/teaser-composition` appears in the catalog on the next turn, even mid-session.

Options: `--copy` (copy instead of symlink; rerun after updating the repo), `--no-env` (skip the Python environment), `--no-skills` (skip only the skill install). Override the destinations with `DSH_SKILLS_DIR` and `BIN_DIR`.

### Requirements

- Python 3.10+ (`python3-venv`)
- System Cairo (`libcairo2`) for CairoSVG rasterization
- A Japanese-capable font (Noto Sans CJK); `--font` accepts any font file

## Usage

Ask for the skill in a DSH chat:

~~~text
/teaser-composition Create three teaser concepts for a new AI model. Finish the typography and layout in code.
~~~

The 12 approaches are callable directly (`/teaser-atmosphere`, `/teaser-orbit`, ...). Include reference images, intended use, dimensions, exact copy, and any typeface or brand requirements when available.

Render from the shell:

~~~bash
teaser-render --list
teaser-render atmosphere --title "NOVA" --output out/nova.png
teaser-render orbit --preset source-102 --width 1200 --height 1200 --output out/orbit.png
~~~

`teaser-render <type> [render.py flags...]` runs that type's `scripts/render.py` in the shared venv and writes PNG, SVG, and the resolved JSON. It accepts `--config`, `--preset`, `--title`, `--subtitle`, `--variant`, `--width`, `--height`, `--seed`, `--font`, `--glyph`, `--asset`, and `--list-presets`.

## The 12 approaches

| Approach | Skill | Core idea |
|---|---|---|
| Negative space | `/teaser-atmosphere` | Type leads; the background is a low-frequency presence |
| Geometry | `/teaser-geometry` | Huge circles and bands around a stable type axis |
| Drafting | `/teaser-drafting` | Construction lines and a measured drawing space |
| Pixel modules | `/teaser-pixel` | Oversized cropped motif against a small card |
| Radial light | `/teaser-radial` | Converging light and a small subject |
| Flow | `/teaser-flow` | Continuous surfaces that briefly read as a form |
| Editorial collage | `/teaser-editorial` | Seams between unlike materials, deliberate imbalance |
| Specimen type | `/teaser-specimen` | One letter at a distance, dozens of specimens up close |
| Object | `/teaser-object` | One object carrying touch and expectation |
| Orbit | `/teaser-orbit` | Cosmic scale cropped at the edge, tiny type |
| Scenic | `/teaser-scenic` | A scene with its own type layer |
| Proof | `/teaser-proof` | Density of real work as the argument |

Classification data and source mapping live in [`references/catalog.json`](skills/teaser-composition/references/catalog.json); typography guidance in [`references/typography.md`](skills/teaser-composition/references/typography.md).

## Layout

- [`skills/teaser-composition/SKILL.md`](skills/teaser-composition/SKILL.md): composition selection, asset handling, typography guidance
- `skills/teaser-*`: the 12 approach skills, each with `SKILL.md`, `scripts/`, `presets.json`, `examples/`, `references/`
- `install.sh`: DSH install, Python environment, `teaser-render`
- `scripts/smoke.sh`: renders all 12 approaches

## Codex

The frontmatter and `agents/openai.yaml` stay Codex-compatible.

~~~bash
mkdir -p ~/.codex/skills
cp -R skills/teaser-* ~/.codex/skills/
~~~

## Notes

The repository includes written observations of reference compositions, but not the third-party reference images themselves. Adapt the compositional principles rather than copying source logos or artwork. Check the applicable usage and redistribution terms for any fonts and generated assets you use.
