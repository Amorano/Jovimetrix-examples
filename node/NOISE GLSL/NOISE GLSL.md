# NOISE GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

The NOISE GLSL (JOV) node generates noise using GLSL shaders, providing various types of noise patterns for image processing applications. Users can select from different noise types, including Brownian, Gradient, Mosaic, Perlin 2D, Simplex 2D, and Value noise. The generated noise patterns can be customized further by specifying parameters such as seed and image dimensions. GLSL shaders corresponding to each noise type are loaded dynamically based on the user's selection, allowing for flexible and efficient noise generation in the image processing pipeline.

![NOISE GLSL](./NOISE%20GLSL.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
❓ | STRING | type | VALUE | BROWNIAN, VALUE, GRADIENT,<br>MOSAIC, PERLIN 2D, SIMPLEX 2D
SEED | INT | random generator's initial value | 0 | 
🇼🇭 | VEC2 | width and height | (32, 32) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project