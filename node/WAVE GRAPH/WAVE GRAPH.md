# WAVE GRAPH (JOV) ▶ ılıılı

## JOVIMETRIX 🔺🟩🔵/CREATE

The Wave Graph node visualizes audio waveforms as bars. Adjust parameters like the number of bars, bar thickness, and colors.

![WAVE GRAPH](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/WAVE%20GRAPH/WAVE%20GRAPH.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
♒ | AUDIO | wave function |  | 
VAL | INT | value | 100 | 
THICK | FLOAT | thickness | 0.72 | 
🇼🇭 | VEC2 | set the target dimensions for<br>the output image if scaling is<br>applied | (256, 256) | 
🌈A | VEC4 | rgb with alpha color | (128, 128, 0, 255) | 
MATTE | VEC4 | define a background color for<br>padding, if necessary. this is<br>useful when images do not fit<br>perfectly into the designated<br>area and need a filler color | (0, 128, 128, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project