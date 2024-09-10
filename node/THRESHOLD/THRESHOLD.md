## [THRESHOLD (JOV) 📉](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/THRESHOLD/THRESHOLD.md)

## JOVIMETRIX 🔺🟩🔵/COMPOSE


Define a range and apply it to an image for segmentation and feature extraction. Choose from various threshold modes, such as binary and adaptive, and adjust the threshold value and block size to suit your needs. You can also invert the resulting mask if necessary. This node is versatile for a variety of image processing tasks.


![THRESHOLD](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/THRESHOLD/THRESHOLD.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾  |  IMAGE, MASK  | Pixel Data (RGBA, RGB or Grayscale) |  | 
🧬  |  STRING  | X-Men | ADAPT_NONE | ADAPT NONE, ADAPT MEAN, ADAPT GAUSS
⚒️  |  STRING  | Function | BINARY | BINARY, TRUNC, TOZERO
📉  |  FLOAT  | Threshold | 0.5 | 
📏  |  INT  | Scalar by which to scale the input | 3 | 
🔳  |  BOOLEAN  | Invert the mask input | False | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project