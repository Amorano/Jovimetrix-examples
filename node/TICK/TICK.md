# TICK (JOV) ⏱

## JOVIMETRIX 🔺🟩🔵/CALC

The `Tick` node acts as a timer and frame counter, emitting pulses or signals based on time intervals or BPM settings. It allows precise synchronization and control over animation sequences, with options to adjust FPS, BPM, and loop points. This node is useful for generating time-based events or driving animations with rhythmic precision.

![TICK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TICK/TICK.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
⚡ | * | trigger |  | 
VAL | INT | value | 0 | 
🔄 | INT | loop | 0 | 
🏎️ | INT | frames per second | 24 | 
BPM | FLOAT | the number of beats per minute | 120 | 
🎶 | INT | note | 4 | 
✋🏽 | BOOLEAN | wait | False | 
RESET | BOOLEAN | reset | False | 
BATCH | INT | output as a batch (all images in<br>a single tensor) or as a list of<br>images (each image processed<br>separately) | 1 | 
🦶🏽 | INT | step | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
VAL | INT | Value 
🛟 | FLOAT | Linear 
🏎️ | FLOAT | Frames per second 
⚡ | * | Trigger 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project