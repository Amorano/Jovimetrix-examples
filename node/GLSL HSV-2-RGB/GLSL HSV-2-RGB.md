## [GLSL HSV-2-RGB (JOV) 🧙🏽](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/GLSL%20HSV-2-RGB/GLSL%20HSV-2-RGB.md)

## JOVIMETRIX 🔺🟩🔵/GLSL/COLOR/CONVERT

Convert HSV image into RGB color space. Maintains alpha/mask.

![GLSL HSV-2-RGB](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20HSV-2-RGB/GLSL%20HSV-2-RGB.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
image  |  IMAGE  | HSV image |  | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🇼🇭  |  VEC2INT  | Width and Height as a Vector2 (x,y) | [512, 512] | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4INT  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | [0, 0, 0, 255] | 
FRAGMENT  |  JDATABUCKET  | Select a fragment program to load |  | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project