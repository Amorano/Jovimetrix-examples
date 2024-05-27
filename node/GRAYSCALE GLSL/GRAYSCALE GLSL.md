# GRAYSCALE GLSL (JOV)

## JOVIMETRIX 🔺🟩🔵/GLSL

The GRAYSCALE GLSL (JOV) node converts the input image to grayscale using a GLSL shader. This node applies a customizable grayscale conversion formula to each pixel of the input image, allowing users to specify the RGB weights for the conversion. The GLSL shader used for this operation is loaded from the specified fragment file, providing flexibility in grayscale conversion methods for different image processing requirements.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
🌈 | VEC3 | rgb (no alpha) color | (0.299, 0.587, 0.114) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project