# ADJUST (JOV) 🕸️

## JOVIMETRIX 🔺🟩🔵/ADJUST

The `Adjust Node` lets you enhance and modify images with various effects.
You can apply blurring, sharpening, color tweaks, and edge detection.
Customize parameters like radius, value, and contrast, and use masks for
selective effects. Advanced options include pixelation, quantization, and
morphological operations like dilation and erosion. Handle transparency easily,
ensuring seamless blending of effects. Perfect for simple adjustments and
complex image transformations.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
👾| * | pixel data (rgba, rgb or grayscale) |  |
😷| * | mask or image to use as mask to<br>control where adjustments are<br>applied |  |
⚒️| COMBO[STRING] | function | BLUR | BLUR, STACK_BLUR, GAUSSIAN_BLUR, MEDIAN_BLUR,<br>SHARPEN, EMBOSS, INVERT, HSV, LEVELS,<br>EQUALIZE, PIXELATE, QUANTIZE, POSTERIZE,<br>FIND_EDGES, OUTLINE, DILATE, ERODE, OPEN,<br>CLOSE
🅡| INT | radius | 3 |
VALUE| FLOAT | value | 1 |
LoHi| VEC2 | low and high | (0, 1) |
LMH| VEC3 | low, middle, high | (0, 0.5, 1) |
🇭🇸‌🇻| VEC3 | hue, saturation and value | (0, 1, 1) |
🌓| FLOAT | contrast | 0 |
🔆| FLOAT | gamma | 1 |
MATTE| VEC4 | background color | (0, 0, 0, 255) |
🔳| BOOLEAN | color inversion | False |

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️| IMAGE | Image
🌈| IMAGE | RGB (no alpha) Color
😷| MASK | Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project