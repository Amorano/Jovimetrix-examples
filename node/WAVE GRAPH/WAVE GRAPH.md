# WAVE GRAPH (JOV) ▶ ılıılı

## JOVIMETRIX 🔺🟩🔵/AUDIO

The Wave Graph node visualizes audio waveforms as bars. Adjust parameters like the number of bars, bar thickness, and colors.

![WAVE GRAPH](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/WAVE%20GRAPH/WAVE%20GRAPH.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
♒ | WAVE | wave function |  | 
VAL | INT | value | 100 | 
THICK | FLOAT | thickness | 0.72 | 
🇼🇭 | VEC2 | width and height | (32, 32) | 
🌈A | VEC4 | rgb with alpha color | (128, 128, 0, 255) | 
MATTE | VEC4 | background color | (0, 128, 128, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project