# MAP GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

The MAP GLSL (JOV) node applies mapping transformations to input images using GLSL shaders. It offers various mapping types such as polar mapping, Mercator projection, and rectangular equal-area projection. Users can choose the desired mapping type and optionally flip the output image. GLSL shaders corresponding to different mapping transformations are dynamically loaded, enabling efficient image mapping operations within the image processing pipeline.

![MAP GLSL](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/MAP%20GLSL/MAP%20GLSL.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
❓ | STRING | type | POLAR | MERCATOR, POLAR, RECT EQUAL
🙃 | BOOLEAN | flip input a and input b with<br>each other | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project