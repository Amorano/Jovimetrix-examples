# CROP (JOV) ✂️

## JOVIMETRIX 🔺🟩🔵/COMPOSE

The Crop Node extracts a portion of an input image or resizes it to a specified size. It supports various cropping modes, including center cropping, custom XY cropping, and freeform polygonal cropping. This node is useful for preparing image data for specific tasks or extracting regions of interest.

![CROP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/CROP/CROP.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
⚒️ | STRING | function | CENTER | CENTER, XY, FREE
🇽🇾 | VEC2 | x and y | (0, 0) | 
🇼🇭 | VEC2 | width and height | (512, 512) | 
TL-TR | VEC4 | top left - top right | (0, 0, 0, 1) | 
BL-BR | VEC4 | bottom left - bottom right | (1, 0, 1, 1) | 
🌈 | VEC3 | rgb (no alpha) color | (0, 0, 0) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project