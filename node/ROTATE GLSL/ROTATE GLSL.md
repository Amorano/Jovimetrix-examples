# ROTATE GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

Applies a rotation transformation to an image using GLSL. Allows for setting the angle of rotation and the pivot point.

![ROTATE GLSL](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/ROTATE%20GLSL/ROTATE%20GLSL.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
📐 | FLOAT | rotation angle | 0 | 
PIVOT | VEC2 | pivot | (0.5, 0.5) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project