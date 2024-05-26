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
EASE| COMBO[STRING] | easing function | NONE | NONE, QUAD IN, QUAD OUT, QUAD IN OUT, CUBIC<br>IN, CUBIC OUT, CUBIC IN OUT, QUARTIC IN,<br>QUARTIC OUT, QUARTIC IN OUT, QUINTIC IN,<br>QUINTIC OUT, QUINTIC IN OUT, SIN IN, SIN OUT,<br>SIN IN OUT, CIRCULAR IN, CIRCULAR OUT,<br>CIRCULAR IN OUT, EXPONENTIAL IN, EXPONENTIAL<br>OUT, EXPONENTIAL IN OUT, ELASTIC IN, ELASTIC<br>OUT, ELASTIC IN OUT, BACK IN, BACK OUT, BACK<br>IN OUT, BOUNCE IN, BOUNCE OUT, BOUNCE IN OUT
❓| COMBO[STRING] | type | FLOAT | INT, FLOAT

### OUTPUT

name|type|desc
:---:|:---:|---
🔮| * | Any Type 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project