# STEREOSCOPIC (JOV) 🕶️

## JOVIMETRIX 🔺🟩🔵/CREATE

The Stereoscopic node simulates depth perception in images by generating stereoscopic views. It accepts an optional input image for color matte. Adjust baseline and focal length for customized depth effects.

![STEREOSCOPIC](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STEREOSCOPIC/STEREOSCOPIC.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
🔟 | FLOAT | integer | 0.1 | 
VAL | FLOAT | value | 500 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project