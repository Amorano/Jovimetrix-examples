# KALEIDOSCOPE GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

Applies a kaleidoscope effect to an image using GLSL. Allows for adjusting various parameters such as segments, radius, zoom, offset, rotation, size, and skip to create intricate patterns.

![KALEIDOSCOPE GLSL](./KALEIDOSCOPE%20GLSL.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
SEGMENT | FLOAT | number of parts which the input<br>image should be split | 2.5 | 
🅡 | FLOAT | radius | 1 | 
🔎 | FLOAT | zoom | 1 | 
OFFSET | VEC2 | offset | (0.5, 0.5) | 
🔃 | FLOAT | rotation angle | 0 | 
📏 | FLOAT | scalar by which to scale the<br>input | 0.5 | 
SKIP | FLOAT | interval between segments | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project