# FILTER MASK (JOV) 🤿

## JOVIMETRIX 🔺🟩🔵/ADJUST

The `Filter Mask` node allows you to create masks based on color ranges within an image, ideal for selective filtering and masking tasks. You can specify the color range using start and end values along with an optional fuzziness factor to adjust the range. This node provides flexibility in defining precise color-based masks for various image processing applications.

![FILTER MASK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/FILTER%20MASK/FILTER%20MASK.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
START | VEC3 | start of the range | (128, 128, 128) | 
🇴 | BOOLEAN | boolean | False | 
END | VEC3 | end of the range | (128, 128, 128) | 
🛟 | VEC3 | linear | (0.5, 0.5, 0.5) | 
MATTE | VEC4 | background color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project