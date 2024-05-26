# LERP (JOV) 🔰

## JOVIMETRIX 🔺🟩🔵/CALC

The Lerp Node performs linear interpolation between two values or vectors based on a blending factor. It supports easing functions for smoother transitions and outputs the result as either floats or integers.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
🅰️| * | input a |  | 
🅱️| * | input b |  | 
🛟| FLOAT | linear | 0.0 | 
EASE| COMBO[STRING] | easing function | NONE | NONE, QUAD_IN, QUAD_OUT, QUAD_IN_OUT,<br>CUBIC_IN, CUBIC_OUT, CUBIC_IN_OUT,<br>QUARTIC_IN, QUARTIC_OUT, QUARTIC_IN_OUT,<br>QUINTIC_IN, QUINTIC_OUT, QUINTIC_IN_OUT,<br>SIN_IN, SIN_OUT, SIN_IN_OUT, CIRCULAR_IN,<br>CIRCULAR_OUT, CIRCULAR_IN_OUT,<br>EXPONENTIAL_IN, EXPONENTIAL_OUT,<br>EXPONENTIAL_IN_OUT, ELASTIC_IN, ELASTIC_OUT,<br>ELASTIC_IN_OUT, BACK_IN, BACK_OUT,<br>BACK_IN_OUT, BOUNCE_IN, BOUNCE_OUT,<br>BOUNCE_IN_OUT
❓| COMBO[STRING] | type | FLOAT | INT, FLOAT

### OUTPUT

name|type|desc
:---:|:---:|---
🔮| * | Any Type 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project