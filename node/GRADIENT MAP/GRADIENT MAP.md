# GRADIENT MAP (JOV) 🇲🇺

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Remaps an input image using a gradient lookup table (LUT) to allow precise control over color mapping by applying the gradient to the input image. The gradient image will be translated into a single row lookup table. This node is useful for artistic effects, color grading, and mapping specific color ranges to achieve desired visual effects.

![GRADIENT MAP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GRADIENT%20MAP/GRADIENT%20MAP.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
🇲🇺 | * | gradient |  | 
🙃 | BOOLEAN | flip input a and input b with<br>each other | False | 
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