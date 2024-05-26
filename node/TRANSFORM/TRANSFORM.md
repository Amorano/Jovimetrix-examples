# TRANSFORM (JOV) 🏝️

## JOVIMETRIX 🔺🟩🔵/COMPOSE

The Transform Node applies various geometric transformations to images, including translation, rotation, scaling, mirroring, tiling, perspective projection, and more. It offers extensive control over image manipulation to achieve desired visual effects.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
👾| * | pixel data (rgba, rgb or grayscale) |  | 
🇽🇾| VEC2 | x and y | (0, 0) | 
📐| FLOAT | rotation angle | 0 | 
📏| VEC2 | scalar by which to scale the input | (1.0, 1.0) | 
TILE| VEC2 | title | (1.0, 1.0) | 
EDGE| COMBO[STRING] | clip or wrap the canvas edge | CLIP | CLIP, WRAP, WRAPX, WRAPY
🪞| COMBO[STRING] | mirror | NONE | NONE, X, FLIP X, Y, FLIP Y, XY, X FLIP Y,<br>FLIP XY, FLIP X FLIP Y
PIVOT| VEC2 | pivot | (0.5, 0.5) | 
PROJ| COMBO[STRING] | projection | NORMAL | NORMAL, POLAR, SPHERICAL, FISHEYE,<br>PERSPECTIVE
TL-TR| VEC4 | top left - top right | (0, 0, 1, 0) | 
BL-BR| VEC4 | bottom left - bottom right | (0, 1, 1, 1) | 
💪🏽| FLOAT | strength | 1 | 
MODE| COMBO[STRING] | scaling mode | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT SHORT
🇼🇭| VEC2 | width and height | (32, 32) | 
🎞️| COMBO[STRING] | sampling method to apply when<br>rescaling | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE| VEC4 | background color | (0, 0, 0, 255) | 

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️| IMAGE | Image 
🌈| IMAGE | RGB (no alpha) Color 
😷| MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project