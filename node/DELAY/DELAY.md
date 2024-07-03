# DELAY (JOV) ✋🏽

## JOVIMETRIX 🔺🟩🔵/CALC

Delay node used to introduce pauses in the workflow. It accepts an optional input to pass through and a timer parameter to specify the duration of the delay. If no timer is provided, it defaults to a maximum delay. During the delay, it periodically checks for messages to interrupt the delay. Once the delay is completed, it returns the input passed to it.

![DELAY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/DELAY/DELAY.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
📥  |  *  | Pass In |  | 
⏱  |  INT  | Timer | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
📤  |  *  | Pass Out 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project