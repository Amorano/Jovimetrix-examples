# [GLSL FILTER RANGE (JOV) 🧙🏽‍♀️](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20FILTER%20RANGE/GLSL%20FILTER%20RANGE.md)

## JOVIMETRIX 🔺🟩🔵/GLSL
Range select clipped at start and end
![GLSL FILTER RANGE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20FILTER%20RANGE/GLSL%20FILTER%20RANGE.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
image  |  IMAGE  | Unknown Explanation! |  | 
start  |  VEC3  | 0 | (0, 0, 0) | 
end  |  VEC3  | 0 | (0, 0, 0) | 
🇼🇭  |  VEC2  | Width and Height as a Vector2 (x,y) | (512, 512) | 
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 
BATCH  |  INT  | Output as a BATCH (all images in a single<br>Tensor) or as a LIST of images (each image<br>processed separately) | 0 | 
🏎️  |  INT  | Frames per second | 24 | 
🕛  |  FLOAT  | Time | 0 | 
✋🏽  |  BOOLEAN  | Wait | False | 
RESET  |  BOOLEAN  | Reset | False | 
FRAGMENT  |  JDATABUCKET  | Select a fragment program to load |  | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project