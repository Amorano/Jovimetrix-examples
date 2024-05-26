# FLATTEN (JOV) ⬇️

## JOVIMETRIX 🔺🟩🔵/COMPOSE

The Flatten Node combines multiple input images into a single image by summing their pixel values. This operation is useful for merging multiple layers or images into one composite image, such as combining different elements of a design or merging masks. Users can specify the blending mode and interpolation method to control how the images are combined. Additionally, a matte can be applied to adjust the transparency of the final composite image.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
MODE|COMBO[STRING]|scaling mode|NONE|NONE, CROP, MATTE, FIT, ASPECT, ASPECT_SHORT
🇼🇭|VEC2|width and height|(32, 32)|
🎞️|COMBO[STRING]|sampling method to apply when<br>rescaling|LANCZOS4|NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR_EXACT, NEAREST_EXACT
MATTE|VEC4|background color|(0, 0, 0, 255)|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|IMAGE|Image
🌈|IMAGE|RGB (no alpha) Color
😷|MASK|Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project