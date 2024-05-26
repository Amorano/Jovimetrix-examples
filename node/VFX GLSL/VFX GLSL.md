# VFX GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
👾A|*|pixel data (rgba, rgb or grayscale)||
radius|FLOAT||2.0|
strength|FLOAT||1.0|
center|VEC2||(0.5, 0.5)|
❓|COMBO[STRING]|type|BULGE|BULGE, CHROMATIC, CROSS_STITCH, CROSS_HATCH,<br>CRT, FILM_GRAIN, FROSTED, PIXELATION, SEPIA,<br>VHS

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|IMAGE|Image
🌈|IMAGE|RGB (no alpha) Color
😷|MASK|Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project