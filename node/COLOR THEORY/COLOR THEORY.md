# COLOR THEORY (JOV) 🛞

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Generate a color harmony based on the selected scheme. Supported schemes include complimentary, analogous, triadic, tetradic, and more. Users can customize the angle of separation for color calculations, offering flexibility in color manipulation and exploration of different color palettes.

![COLOR THEORY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20THEORY/COLOR%20THEORY.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
SCHEME  |  STRING  | Scheme | COMPLIMENTARY | COMPLIMENTARY, MONOCHROMATIC, SPLIT<br>COMPLIMENTARY, ANALOGOUS, TRIADIC, SQUARE,<br>COMPOUND, CUSTOM TETRAD
VAL  |  INT  | Custom angle of separation to use when<br>calculating colors | 45 | 
🔳  |  BOOLEAN  | Color Inversion | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🔵  |  IMAGE  | Color Scheme Result 1 
🟡  |  IMAGE  | Color Scheme Result 2 
🟣  |  IMAGE  | Color Scheme Result 3 
⚫️  |  IMAGE  | Color Scheme Result 4 
⚪  |  IMAGE  | Color Scheme Result 5 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project