# COLOR THEORY (JOV) 🛞

## JOVIMETRIX 🔺🟩🔵/COMPOSE

The Color Theory Node applies various color harmony schemes to an input image, generating multiple color variants based on the selected scheme. It supports schemes such as complimentary, analogous, triadic, tetradic, and more. Additionally, users can specify a custom angle of separation for color calculation, offering flexibility in color manipulation. This node is useful for exploring different color palettes and creating visually appealing compositions.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
👾|*|pixel data (rgba, rgb or grayscale)||
SCHEME|COMBO[STRING]|scheme|COMPLIMENTARY|COMPLIMENTARY, MONOCHROMATIC, SPLIT_COMPLIMENTARY,<br>ANALOGOUS, TRIADIC, SQUARE, COMPOUND, CUSTOM_TETRAD
#️⃣|INT|value|45|
🔳|BOOLEAN|color inversion|False|

### OUTPUT

name|type|desc
:---:|:---:|---
🔵|Color Scheme 1|IMAGE
🟡|Color Scheme 2|IMAGE
🟣|Color Scheme 3|IMAGE
⚫️|Color Scheme 4|IMAGE
⚪|Color Scheme 5|IMAGE

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project