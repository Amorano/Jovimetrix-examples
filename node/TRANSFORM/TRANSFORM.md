## [TRANSFORM (JOV) 🏝️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/TRANSFORM/TRANSFORM.md)

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Apply various geometric transformations to images, including translation, rotation, scaling, mirroring, tiling and perspective projection. It offers extensive control over image manipulation to achieve desired visual effects.

![TRANSFORM](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TRANSFORM/TRANSFORM.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
🇽🇾  |  VEC2  | X and Y | (0, 0) | 
📐  |  FLOAT  | Rotation Angle | 0 | 
📏  |  VEC2  | Scalar by which to scale the input | (1.0, 1.0) | 
TILE  |  VEC2  | Title | (1.0, 1.0) | 
EDGE  |  STRING  | Clip or Wrap the Canvas Edge | CLIP | CLIP, WRAP, WRAPX, WRAPY
🪞  |  STRING  | Mirror | NONE | NONE, X, FLIP X, Y, FLIP Y, XY, X FLIP Y,<br>FLIP XY, FLIP X FLIP Y
PIVOT  |  VEC2  | Pivot | (0.5, 0.5) | 
PROJ  |  STRING  | Projection | NORMAL | NORMAL, POLAR, SPHERICAL, FISHEYE,<br>PERSPECTIVE
TL-TR  |  VEC4  | Top Left - Top Right | (0, 0, 1, 0) | 
BL-BR  |  VEC4  | Bottom Left - Bottom Right | (0, 1, 1, 1) | 
💪🏽  |  FLOAT  | Strength | 1 | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🇼🇭  |  VEC2  | Width and Height as a Vector2 (x,y) | (512, 512) | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project