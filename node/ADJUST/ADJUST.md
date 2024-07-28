## [ADJUST (JOV) 🕸️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/ADJUST/ADJUST.md)

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Enhance and modify images with various effects such as blurring, sharpening, color tweaks, and edge detection. Customize parameters like radius, value, and contrast, and use masks for selective effects. Advanced options include pixelation, quantization, and morphological operations like dilation and erosion. Handle transparency effortlessly to ensure seamless blending of effects. This node is ideal for simple adjustments and complex image transformations.

![ADJUST](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/ADJUST/ADJUST.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
😷  |  *  | Mask or Image to use as Mask to control<br>where adjustments are applied |  | 
⚒️  |  STRING  | Type of adjustment (e.g., blur, sharpen,<br>invert) | BLUR | BLUR, STACK BLUR, GAUSSIAN BLUR, MEDIAN<br>BLUR, SHARPEN, EMBOSS, INVERT, HSV,<br>LEVELS, EQUALIZE, PIXELATE, QUANTIZE,<br>POSTERIZE, FIND EDGES, OUTLINE, DILATE,<br>ERODE, OPEN, CLOSE
🅡  |  INT  | Radius | 3 | 
VAL  |  FLOAT  | Value | 1 | 
LoHi  |  VEC2  | Low and High | (0, 1) | 
LMH  |  VEC3  | Low, Middle, High | (0, 0.5, 1) | 
HSV  |  VEC3  | Hue, Saturation and Value | (0, 1, 1) | 
🌓  |  FLOAT  | Contrast | 0 | 
🔆  |  FLOAT  | Gamma | 1 | 
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 
🔳  |  BOOLEAN  | Invert the mask input | False | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project