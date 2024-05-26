# POLYGON GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

The POLYGON GLSL (JOV) node generates polygonal shapes using GLSL shaders. Users can specify the number of sides for the polygon and its radius, allowing for the creation of various polygonal shapes such as triangles, squares, pentagons, and more. The generated shapes can be further processed within the image processing pipeline. GLSL shaders corresponding to polygon generation are dynamically loaded, enabling efficient shape generation and manipulation.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
#️⃣|INT|value|3|
🅡|FLOAT|radius|1|
🇼🇭|VEC2|width and height|(32, 32)|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|IMAGE|Image
🌈|IMAGE|RGB (no alpha) Color
😷|MASK|Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project