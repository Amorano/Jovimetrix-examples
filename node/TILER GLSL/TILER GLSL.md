# TILER GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

Applies a tiling effect to an image using GLSL. Allows for setting the number of tiles in the x and y directions.

![TILER GLSL](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TILER%20GLSL/TILER%20GLSL.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
TILE | VEC2 | title | (1.0, 1.0) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project