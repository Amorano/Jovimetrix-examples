# SELECT RANGE GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

The SELECT RANGE GLSL (JOV) node applies a GLSL shader to select a specific range of colors within the input image. This node allows users to define the start and end points of the color range using RGB values, providing precise control over color selection. The GLSL shader used for this operation is loaded from the specified fragment file, enabling customizable color range selection for various image processing tasks.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
👾A|*|pixel data (rgba, rgb or grayscale)||
START|VEC3|start of the range|(0.0, 0.0, 0.0)|
END|VEC3|end of the range|(1.0, 1.0, 1.0)|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|IMAGE|Image
🌈|IMAGE|RGB (no alpha) Color
😷|MASK|Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project