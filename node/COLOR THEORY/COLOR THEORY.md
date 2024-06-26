# COLOR THEORY (JOV) 🛞

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Apply various color harmony schemes to an input image using the Color Theory Node, generating multiple color variants based on the selected scheme. Supported schemes include complimentary, analogous, triadic, tetradic, and more. Users can customize the angle of separation for color calculations, offering flexibility in color manipulation and exploration of different color palettes.

![COLOR THEORY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20THEORY/COLOR%20THEORY.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
SCHEME | STRING | scheme | COMPLIMENTARY | COMPLIMENTARY, MONOCHROMATIC,<br>SPLIT COMPLIMENTARY, ANALOGOUS,<br>TRIADIC, SQUARE, COMPOUND,<br>CUSTOM TETRAD
VAL | INT | value | 45 | 
🔳 | BOOLEAN | color inversion | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🔵 | IMAGE | Color Scheme Result 1 
🟡 | IMAGE | Color Scheme Result 2 
🟣 | IMAGE | Color Scheme Result 3 
⚫️ | IMAGE | Color Scheme Result 4 
⚪ | IMAGE | Color Scheme Result 5 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project