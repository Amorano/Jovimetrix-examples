## [WAVE GRAPH (JOV) ▶ ılıılı](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/WAVE%20GRAPH/WAVE%20GRAPH.md)

## JOVIMETRIX 🔺🟩🔵/CREATE

The Wave Graph node visualizes audio waveforms as bars. Adjust parameters like the number of bars, bar thickness, and colors.

![WAVE GRAPH](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/WAVE%20GRAPH/WAVE%20GRAPH.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
♒  |  AUDIO  | Audio Wave Object |  | 
VAL  |  INT  | Number of Vertical bars to try to fit<br>within the specified Width x Height | 100 | 
THICK  |  FLOAT  | The percentage of fullness for each bar;<br>currently scaled from the left only | 0.72 | 
🇼🇭  |  VEC2  | Final output size of the wave bar graph | (256, 256) | 
🌈A  |  VEC4  | Bar Color | (128, 128, 0, 255) | 
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 128, 128, 255) | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project