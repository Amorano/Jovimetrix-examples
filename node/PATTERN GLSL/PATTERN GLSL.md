# PATTERN GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

The PATTERN GLSL (JOV) node generates patterns using GLSL shaders, providing a variety of pattern types for image processing tasks. Users can select from different pattern types, including the checkerboard pattern. The generated patterns can be customized further by specifying parameters such as tile size and image dimensions. GLSL shaders corresponding to each pattern type are loaded dynamically based on the user's selection, enabling flexible and efficient pattern generation in the image processing pipeline.

![PATTERN GLSL](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/PATTERN%20GLSL/PATTERN%20GLSL.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
❓ | STRING | type | CHECKER | CHECKER
TILE | VEC2 | title | (1, 1) | 
🇼🇭 | VEC2 | set the target dimensions for<br>the output image if scaling is<br>applied | (32, 32) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project