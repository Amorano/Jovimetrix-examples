# STEREOGRAM (JOV) 📻

## JOVIMETRIX 🔺🟩🔵/CREATE

The Stereogram node creates stereograms, generating 3D images from 2D input. Set tile divisions, noise, gamma, and shift parameters to control the stereogram's appearance.

![STEREOGRAM](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STEREOGRAM/STEREOGRAM.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | Pixel Data (RGBA, RGB or Grayscale) |  | 
DEPTH | * | Grayscale image representing a depth map |  | 
TILE | INT | Title | 8 | 
NOISE | FLOAT | Noise | 0.33 | 
🔆 | FLOAT | Gamma | 0.33 | 
SHIFT | FLOAT | Shift | 1.0 | 
🔳 | BOOLEAN | Color Inversion | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control where<br>adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project