# CONSTANT (JOV) 🟪

## JOVIMETRIX 🔺🟩🔵/CREATE

The Constant node generates constant images or masks of a specified size and color. It can be used to create solid color backgrounds or matte images for compositing with other visual elements. The node allows you to define the desired width and height of the output and specify the RGBA color value for the constant output. Additionally, you can input an optional image to use as a matte with the selected color.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
👾|*|pixel data (rgba, rgb or grayscale)||
🌈A|VEC4|rgb with alpha color|(0, 0, 0, 255)|
🇼🇭|VEC2|width and height|(512, 512)|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|IMAGE|Image
🌈|IMAGE|RGB (no alpha) Color
😷|MASK|Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project