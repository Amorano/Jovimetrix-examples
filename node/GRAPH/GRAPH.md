# GRAPH (JOV) 📈

## JOVIMETRIX 🔺🟩🔵/UTILITY

Visualize a series of data points over time. It accepts a dynamic number of values to graph and display, with options to reset the graph or specify the number of values. The output is an image displaying the graph, allowing users to analyze trends and patterns.

![GRAPH](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GRAPH/GRAPH.png)

#### OUTPUT NODE?: `True`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
RESET  |  BOOLEAN  | Reset | False | 
VAL  |  INT  | Number of values to graph and display | 60 | 
🇼🇭  |  VEC2  | Set the target dimensions for the output<br>image if scaling is applied | (512, 512) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project