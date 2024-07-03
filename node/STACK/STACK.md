# STACK (JOV) ➕

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Merge multiple input images into a single composite image by stacking them along a specified axis. Options include axis, stride, scaling mode, width and height, interpolation method, and matte color. The axis parameter allows for horizontal, vertical, or grid stacking of images, while stride controls the spacing between them.

![STACK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STACK/STACK.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
AXIS | STRING | Choose the direction in which to stack the<br>images. Options include horizontal,<br>vertical, or a grid layout | GRID | HORIZONTAL, VERTICAL, GRID
🦶🏽 | INT | Specify the spacing between each stacked<br>image. This determines how far apart the<br>images are from each other | 1 | 
MODE | STRING | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🇼🇭 | VEC2 | Set the target dimensions for the output<br>image if scaling is applied | (512, 512) | 
🎞️ | STRING | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE | VEC4 | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control where<br>adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project