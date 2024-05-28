# STACK (JOV) ➕

## JOVIMETRIX 🔺🟩🔵/COMPOSE

The Stack Node combines multiple input images into a single output image along a specified axis. It stacks the images together, optionally with a specified stride, to create a new image. This node is useful for creating composite images or preparing data for further processing.

![STACK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STACK/STACK.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
AXIS | STRING | axis | GRID | HORIZONTAL, VERTICAL, GRID
🦶🏽 | INT | step | 1 | 
MODE | STRING | scaling mode | NONE | NONE, CROP, MATTE, FIT, ASPECT,<br>ASPECT SHORT
🇼🇭 | VEC2 | width and height | (32, 32) | 
🎞️ | STRING | sampling method to apply when<br>rescaling | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA,<br>LANCZOS4, LINEAR EXACT, NEAREST<br>EXACT
MATTE | VEC4 | background color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project