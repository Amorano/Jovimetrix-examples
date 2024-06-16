# LERP (JOV) 🔰

## JOVIMETRIX 🔺🟩🔵/CALC

The Lerp Node calculates linear interpolation between two values or vectors based on a blending factor (alpha). The node accepts optional start (IN_A) and end (IN_B) points, a blending factor (FLOAT), and various input types for both start and end points, such as single values (X, Y), 2-value vectors (IN_A2, IN_B2), 3-value vectors (IN_A3, IN_B3), and 4-value vectors (IN_A4, IN_B4). Additionally, you can specify the easing function (EASE) and the desired output type (TYPE). It supports various easing functions for smoother transitions.

![LERP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/LERP/LERP.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️ | * | input a |  | 
🅱️ | * | input b |  | 
🛟 | FLOAT | linear | 0.0 | 
EASE | STRING | easing function | NONE | NONE, QUAD IN, QUAD OUT, QUAD IN<br>OUT, CUBIC IN, CUBIC OUT, CUBIC<br>IN OUT, QUARTIC IN, QUARTIC OUT,<br>QUARTIC IN OUT, QUINTIC IN,<br>QUINTIC OUT, QUINTIC IN OUT, SIN<br>IN, SIN OUT, SIN IN OUT,<br>CIRCULAR IN, CIRCULAR OUT,<br>CIRCULAR IN OUT, EXPONENTIAL IN,<br>EXPONENTIAL OUT, EXPONENTIAL IN<br>OUT, ELASTIC IN, ELASTIC OUT,<br>ELASTIC IN OUT, BACK IN, BACK<br>OUT, BACK IN OUT, BOUNCE IN,<br>BOUNCE OUT, BOUNCE IN OUT
❓ | STRING | type | INT | BOOLEAN, FLOAT, INT, VEC2,<br>VEC2INT, VEC3, VEC3INT, VEC4,<br>VEC4INT
🇽 | FLOAT | x | 0 | 
🅰️2 | VEC2 | 2-value vector | (0, 0) | 
🅰️3 | VEC3 | 3-value vector | (0, 0, 0) | 
🅰️4 | VEC4 | 4-value vector | (0, 0, 0, 0) | 
🇾 | FLOAT | y | 0 | 
🅱️2 | VEC2 | 2-value vector | (0, 0) | 
🅱️3 | VEC3 | 3-value vector | (0, 0, 0) | 
🅱️4 | VEC4 | 4-value vector | (0, 0, 0, 0) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🦄 | * | Any Type 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project