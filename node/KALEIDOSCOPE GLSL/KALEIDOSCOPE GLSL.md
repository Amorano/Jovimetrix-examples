# KALEIDOSCOPE GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
👾A|*|pixel data (rgba, rgb or grayscale)||
SEGMENT|FLOAT|number of parts which the input<br>image should be split|2.5|
🅡|FLOAT|radius|1|
🔎|FLOAT|zoom|1|
OFFSET|VEC2|offset|(0.5, 0.5)|
🔃|FLOAT|rotation angle|0|
📏|FLOAT|scalar by which to scale the input|0.5|
SKIP|FLOAT|interval between segments|0|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|IMAGE|Image
🌈|IMAGE|RGB (no alpha) Color
😷|MASK|Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project