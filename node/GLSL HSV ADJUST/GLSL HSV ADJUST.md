## [GLSL HSV ADJUST (JOV) 🧙🏽](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/GLSL%20HSV%20ADJUST/GLSL%20HSV%20ADJUST.md)

## JOVIMETRIX 🔺🟩🔵/GLSL/COLOR

Hue, Saturation and Value adjustment control. Maintains alpha/mask.

![GLSL HSV ADJUST](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20HSV%20ADJUST/GLSL%20HSV%20ADJUST.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
image  |  IMAGE, MASK  | RGB(A) image |  | 
HSV  |  VEC3  | Adjust the Hue, Saturation or Value | [0, 1.0, 1.0] | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT
🇼🇭  |  VEC2INT  | Width and Height as a Vector2 (x,y) | [512, 512] | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4INT  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | [0, 0, 0, 255] | 
EDGE_X  |  STRING  | Clip or Wrap the Canvas Edge | CLAMP | CLAMP, WRAP, MIRROR
EDGE_Y  |  STRING  | Clip or Wrap the Canvas Edge | CLAMP | CLAMP, WRAP, MIRROR
FRAGMENT  |  JDATABUCKET  | Select a fragment program to load |  | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project