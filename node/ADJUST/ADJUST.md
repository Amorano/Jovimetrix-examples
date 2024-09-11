[ADJUST (JOV) 🕸️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/ADJUST/ADJUST.md)
---------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/COMPOSE
  
Enhance and modify images with various effects such as blurring, sharpening, color tweaks, and edge detection. Customize parameters like radius, value, and contrast, and use masks for selective effects. Advanced options include pixelation, quantization, and morphological operations like dilation and erosion. Handle transparency effortlessly to ensure seamless blending of effects. This node is ideal for simple adjustments and complex image transformations.  
![ADJUST](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/ADJUST/ADJUST.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | \* | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 😷 | \* | Mask or Image to use as Mask to control where adjustments are applied |  |  |
| ⚒️ | STRING | Type of adjustment (e.g., blur, sharpen, invert) | BLUR | BLUR, STACK BLUR, GAUSSIAN BLUR, MEDIAN BLUR, SHARPEN, EMBOSS, INVERT, HSV, LEVELS, EQUALIZE, PIXELATE, QUANTIZE, POSTERIZE, FIND EDGES, OUTLINE, DILATE, ERODE, OPEN, CLOSE |
| 🅡 | INT | Radius | 3 |  |
| VAL | FLOAT | Value | 1 |  |
| LoHi | VEC2 | Low and High | [0, 1] |  |
| LMH | VEC3 | Low, Middle, High | [0, 0.5, 1] |  |
| HSV | VEC3 | Hue, Saturation and Value | [0, 1, 1] |  |
| 🌓 | FLOAT | Contrast | 0 |  |
| 🔆 | FLOAT | Gamma | 1 |  |
| MATTE | VEC4INT | Define a background color for padding, if necessary. This is useful when images do not fit perfectly into the designated area and need a filler color | [0, 0, 0, 255] |  |
| 🔳 | BOOLEAN | Invert the mask input | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project