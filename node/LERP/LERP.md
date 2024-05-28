# LERP (JOV) 🔰

## JOVIMETRIX 🔺🟩🔵/CALC

The Lerp Node performs linear interpolation between two values or vectors based on a blending factor. It supports easing functions for smoother transitions and outputs the result as either floats or integers.

![LERP](./LERP.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️ | * | input a |  | 
🅱️ | * | input b |  | 
🛟 | FLOAT | linear | 0.0 | 
EASE | STRING | easing function | NONE | NONE, QUAD IN, QUAD OUT, QUAD IN<br>OUT, CUBIC IN, CUBIC OUT, CUBIC<br>IN OUT, QUARTIC IN, QUARTIC OUT,<br>QUARTIC IN OUT, QUINTIC IN,<br>QUINTIC OUT, QUINTIC IN OUT, SIN<br>IN, SIN OUT, SIN IN OUT,<br>CIRCULAR IN, CIRCULAR OUT,<br>CIRCULAR IN OUT, EXPONENTIAL IN,<br>EXPONENTIAL OUT, EXPONENTIAL IN<br>OUT, ELASTIC IN, ELASTIC OUT,<br>ELASTIC IN OUT, BACK IN, BACK<br>OUT, BACK IN OUT, BOUNCE IN,<br>BOUNCE OUT, BOUNCE IN OUT
❓ | STRING | type | FLOAT | INT, FLOAT

### OUTPUT

name | type | desc
:---:|:---:|---
🔮 | * | Any Type 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project