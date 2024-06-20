# BLEND (JOV) ⚗️

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Combines two input images using various blending modes, such as normal, screen, multiply, overlay, etc. It also supports alpha blending and masking to achieve complex compositing effects. This node is essential for creating layered compositions and adding visual richness to images.

![BLEND](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/BLEND/BLEND.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
👾B | * | pixel data (rgba, rgb or<br>grayscale) |  | 
😷 | * | mask or image to use as mask to<br>control where adjustments are<br>applied |  | 
⚒️ | STRING | function | NORMAL | NORMAL, ADDITIVE, NEGATION,<br>DIFFERENCE, MULTIPLY, DIVIDE,<br>LIGHTEN, DARKEN, SCREEN, BURN,<br>DODGE, OVERLAY, HUE, SATURATION,<br>LUMINOSITY, COLOR, SOFT, HARD,<br>PIN, VIVID, EXCLUSION, REFLECT,<br>GLOW, XOR, EXTRACT
⬜ | FLOAT | alpha | 1 | 
🙃 | BOOLEAN | flip input a and input b with<br>each other | False | 
🔳 | BOOLEAN | color inversion | False | 
MODE | STRING | decide whether the images should<br>be resized to fit a specific<br>dimension. available modes<br>include scaling to fit within<br>given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT,<br>ASPECT SHORT
🇼🇭 | VEC2 | set the target dimensions for<br>the output image if scaling is<br>applied | (32, 32) | 
🎞️ | STRING | select the method for resizing<br>images. options range from<br>nearest neighbor to advanced<br>methods like lanczos, ensuring<br>the best quality for the<br>specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA,<br>LANCZOS4, LINEAR EXACT, NEAREST<br>EXACT
MATTE | VEC4 | define a background color for<br>padding, if necessary. this is<br>useful when images do not fit<br>perfectly into the designated<br>area and need a filler color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project