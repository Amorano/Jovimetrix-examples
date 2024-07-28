# [LERP (JOV) 🔰](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/LERP/LERP.md)

## JOVIMETRIX 🔺🟩🔵/CALC

Calculate linear interpolation between two values or vectors based on a blending factor (alpha). The node accepts optional start (IN_A) and end (IN_B) points, a blending factor (FLOAT), and various input types for both start and end points, such as single values (X, Y), 2-value vectors (IN_A2, IN_B2), 3-value vectors (IN_A3, IN_B3), and 4-value vectors (IN_A4, IN_B4). Additionally, you can specify the easing function (EASE) and the desired output type (TYPE). It supports various easing functions for smoother transitions.

![LERP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/LERP/LERP.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️  |  *  | Custom Start Point |  | 
🅱️  |  *  | Custom End Point |  | 
🛟  |  FLOAT  | Blend Amount. 0 = full A, 1 = full B | 0.5 | 
EASE  |  STRING  | Easing function | NONE | NONE, QUAD IN, QUAD OUT, QUAD IN OUT,<br>CUBIC IN, CUBIC OUT, CUBIC IN OUT, QUARTIC<br>IN, QUARTIC OUT, QUARTIC IN OUT, QUINTIC<br>IN, QUINTIC OUT, QUINTIC IN OUT, SIN IN,<br>SIN OUT, SIN IN OUT, CIRCULAR IN, CIRCULAR<br>OUT, CIRCULAR IN OUT, EXPONENTIAL IN,<br>EXPONENTIAL OUT, EXPONENTIAL IN OUT,<br>ELASTIC IN, ELASTIC OUT, ELASTIC IN OUT
❓  |  STRING  | Output type desired from resultant<br>operation | INT | BOOLEAN, FLOAT, INT, VEC2, VEC2INT, VEC3,<br>VEC3INT, VEC4, VEC4INT, COORD2D
🅰️🅰️  |  VEC4  | default value vector for A | (0, 0, 0, 0) | 
🅱️🅱️  |  VEC4  | default value vector for B | (1, 1, 1, 1) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🦄  |  *  | Any Type 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project