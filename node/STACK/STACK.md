# STACK (JOV) ➕

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Merge multiple input images into a single composite image by stacking them along a specified axis. Options include axis, stride, scaling mode, width and height, interpolation method, and matte color. The axis parameter allows for horizontal, vertical, or grid stacking of images, while stride controls the spacing between them.

![STACK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STACK/STACK.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
AXIS | STRING | axis | GRID | HORIZONTAL, VERTICAL, GRID
🦶🏽 | INT | step | 1 | 
MODE | STRING | decide whether the images should<br>be resized to fit a specific<br>dimension. available modes<br>include scaling to fit within<br>given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT,<br>ASPECT SHORT
🇼🇭 | VEC2 | set the target dimensions for<br>the output image if scaling is<br>applied | (512, 512) | 
🎞️ | STRING | select the method for resizing<br>images. options range from<br>nearest neighbor to advanced<br>methods like lanczos, ensuring<br>the best quality for the<br>specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA,<br>LANCZOS4, LINEAR EXACT, NEAREST<br>EXACT
MATTE | VEC4 | define a background color for<br>padding, if necessary. this is<br>useful when images do not fit<br>perfectly into the designated<br>area and need a filler color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project