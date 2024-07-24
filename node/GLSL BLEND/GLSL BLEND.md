# GLSL BLEND (JOV) 🧙🏽

## JOVIMETRIX 🔺🟩🔵/GLSL
Simple linear blend between two images
![GLSL BLEND](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20BLEND/GLSL%20BLEND.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
imageA  |  IMAGE  | Unknown Explanation! |  | 
imageB  |  IMAGE  | Unknown Explanation! |  | 
blend_amt  |  FLOAT  | Unknown Explanation! | 0.5 | 
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