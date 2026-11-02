[日本語](README.md)

# Teaser Composition

A collection of Codex skills for creating teaser images and key visuals in code, with attention to the scale of the subject, negative space, visual flow, and typography. It adapts compositional ideas to new subjects rather than copying existing artwork.

## Features

- Choose from 12 approaches: atmosphere, geometry, drafting, pixel, radial light, flow, editorial collage, specimen, object, orbit, scenic, and proof.
- Compare typefaces using the actual title and refine spacing, line breaks, and readability at smaller sizes.
- Use generated or supplied images as materials where useful; control typography and layout in code.
- Includes starter renderers and example configurations for each approach.

## Installation

Clone the repository and copy all directories inside `skills/` into your Codex skills directory. The main skill refers to the 12 composition skills, so install them together.

```bash
git clone https://github.com/kuraneko1/teaser-composition.git
mkdir -p ~/.codex/skills
cp -R teaser-composition/skills/teaser-* ~/.codex/skills/
```

Copying can overwrite existing skills with the same names; back them up first if needed. Restart Codex if the skills are not detected.

## Usage

Mention the skill in a Codex chat and describe the visual you want:

```text
$teaser-composition Create three teaser concepts for a new AI model. Use image generation for assets and finish the typography and layout in code.
```

Include reference images, intended use, dimensions, exact copy, and any typeface or brand requirements when available. Depending on the approach, rendering requires Python, Pillow, and CairoSVG. Image generation requires an available image-generation tool.

## Contents

- [`skills/teaser-composition`](skills/teaser-composition/SKILL.md): composition selection, asset usage, and typography guidance.
- `skills/teaser-*`: 12 composition-specific skills and starter renderers.

The repository includes written observations of reference compositions, but not the third-party reference images themselves. Adapt the compositional principles rather than copying source logos or artwork. Check the applicable usage and redistribution terms for any fonts and generated assets you use.
