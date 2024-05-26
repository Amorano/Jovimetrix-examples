# FILTER MASK (JOV) 🤿

## JOVIMETRIX 🔺🟩🔵/ADJUST

The `Filter Mask` node allows you to create masks based on color ranges within an image, ideal for selective filtering and masking tasks. You can specify the color range using start and end values along with an optional fuzziness factor to adjust the range. This node provides flexibility in defining precise color-based masks for various image processing applications.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
👾A| * | pixel data (rgba, rgb or grayscale) |  | 
START| VEC3 | start of the range | (128, 128, 128) | 
🇴| BOOLEAN | boolean | False | 
END| VEC3 | end of the range | (255, 255, 255) | 
🛟| FLOAT | linear | 0.5 | 

### OUTPUT

name|type|desc
:---:|:---:|---
image| IMAGE |  
mask| MASK |  

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project