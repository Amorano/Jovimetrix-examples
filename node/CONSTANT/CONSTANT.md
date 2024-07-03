# CONSTANT (JOV) 🟪

## JOVIMETRIX 🔺🟩🔵/CREATE

The Constant node generates constant images or masks of a specified size and color. It can be used to create solid color backgrounds or matte images for compositing with other visual elements. The node allows you to define the desired width and height of the output and specify the RGBA color value for the constant output. Additionally, you can input an optional image to use as a matte with the selected color.

![CONSTANT](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/CONSTANT/CONSTANT.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾  |  *  | Optional Image to Matte with Selected<br>Color |  | 
🌈A  |  VEC4  | Constant Color to Output | (0, 0, 0, 255) | 
🇼🇭  |  VEC2  | Desired Width and Height of the Color<br>Output | (512, 512) | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project