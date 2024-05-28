# STEREOGRAM (JOV) 📻

## JOVIMETRIX 🔺🟩🔵/CREATE

The Stereogram node creates stereograms, generating 3D images from 2D input. Set tile divisions, noise, gamma, and shift parameters to control the stereogram's appearance.

![STEREOGRAM](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STEREOGRAM/STEREOGRAM.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
DEPTH | * | grayscale image representing a<br>depth map |  | 
TILE | INT | title | 8 | 
NOISE | FLOAT | noise | 0.33 | 
🔆 | FLOAT | gamma | 0.33 | 
SHIFT | FLOAT | shift | 1.0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project