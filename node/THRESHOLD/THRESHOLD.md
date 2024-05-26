# THRESHOLD (JOV) 📉

## JOVIMETRIX 🔺🟩🔵/ADJUST

The `Threshold` node enables you to apply thresholding techniques to images, useful for segmentation and feature extraction. It offers various thresholding modes such as binary and adaptive, along with options to adjust the threshold value and block size. Additionally, you can invert the resulting mask if needed, making it versatile for image processing tasks.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
👾| * | pixel data (rgba, rgb or grayscale) |  | 
🧬| COMBO[STRING] | x-men | ADAPT_NONE | ADAPT NONE, ADAPT MEAN, ADAPT GAUSS
⚒️| COMBO[STRING] | function | BINARY | BINARY, TRUNC, TOZERO
📉| FLOAT | threshold | 0.5 | 
📏| INT | scalar by which to scale the input | 3 | 
🔳| BOOLEAN | color inversion | False | 

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️| IMAGE | Image 
🌈| IMAGE | RGB (no alpha) Color 
😷| MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project