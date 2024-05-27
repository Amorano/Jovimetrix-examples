# VFX GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
radius | FLOAT |  | 2.0 | 
strength | FLOAT |  | 1.0 | 
center | VEC2 |  | (0.5, 0.5) | 
❓ | STRING | type | BULGE | BULGE, CHROMATIC, CROSS STITCH,<br>CROSS HATCH, CRT, FILM GRAIN,<br>FROSTED, PIXELATION, SEPIA, VHS

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project