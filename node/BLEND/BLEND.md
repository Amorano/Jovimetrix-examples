# [BLEND (JOV) ⚗️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/BLEND/BLEND.md)

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Combine two input images using various blending modes, such as normal, screen, multiply, overlay, etc. It also supports alpha blending and masking to achieve complex compositing effects. This node is essential for creating layered compositions and adding visual richness to images.

![BLEND](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/BLEND/BLEND.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A  |  *  | Background Plate |  | 
👾B  |  *  | Image to Overlay on Background Plate |  | 
😷  |  *  | Optional Mask to use for Alpha Blend<br>Operation. If empty, will use the ALPHA of<br>B |  | 
⚒️  |  STRING  | Blending Operation | NORMAL | NORMAL, ADDITIVE, NEGATION, DIFFERENCE,<br>MULTIPLY, DIVIDE, LIGHTEN, DARKEN, SCREEN,<br>BURN, DODGE, OVERLAY, HUE, SATURATION,<br>LUMINOSITY, COLOR, SOFT, HARD, PIN, VIVID,<br>EXCLUSION, REFLECT, GLOW, XOR, EXTRACT
⬜  |  FLOAT  | Amount of Blending to Perform on the<br>Selected Operation | 1 | 
🙃  |  BOOLEAN  | Flip Input A and Input B with each other | False | 
🔳  |  BOOLEAN  | Invert the mask input | False | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🇼🇭  |  VEC2  | Width and Height as a Vector2 (x,y) | (512, 512) | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project