# BLEND (JOV) ⚗️

## JOVIMETRIX 🔺🟩🔵/COMPOSE

The Blend Node combines two input images using various blending modes, such as normal, screen, multiply, overlay, etc. It also supports alpha blending and masking to achieve complex compositing effects. This node is essential for creating layered compositions and adding visual richness to images.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
👾A|*|pixel data (rgba, rgb or grayscale)||
👾B|*|pixel data (rgba, rgb or grayscale)||
😷|*|mask or image to use as mask to control<br>where adjustments are applied||
⚒️|COMBO[STRING]|function|NORMAL|NORMAL, ADDITIVE, NEGATION, DIFFERENCE, MULTIPLY, DIVIDE,<br>LIGHTEN, DARKEN, SCREEN, BURN, DODGE, OVERLAY, HUE,<br>SATURATION, LUMINOSITY, COLOR, SOFT, HARD, PIN, VIVID,<br>EXCLUSION, REFLECT, GLOW, XOR, EXTRACT, MERGE, DESTIN,<br>DESTOUT, SRCATOP, DESTATOP
⬜|FLOAT|alpha|1|
🙃|BOOLEAN|flip input a and input b with each other|False|
🔳|BOOLEAN|color inversion|False|
MODE|COMBO[STRING]|scaling mode|NONE|NONE, CROP, MATTE, FIT, ASPECT, ASPECT_SHORT
🇼🇭|VEC2|width and height|(32, 32)|
🎞️|COMBO[STRING]|sampling method to apply when rescaling|LANCZOS4|NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR_EXACT,<br>NEAREST_EXACT
MATTE|VEC4|background color|(0, 0, 0, 255)|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|Image|IMAGE
🌈|RGB (no alpha) Color|IMAGE
😷|Mask or Image to use as Mask to control<br>where adjustments are applied|MASK

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project