# TICK (JOV) ⏱

## JOVIMETRIX 🔺🟩🔵/ANIMATE

The `Tick` node acts as a timer and frame counter, emitting pulses or signals based on time intervals or BPM settings. It allows precise synchronization and control over animation sequences, with options to adjust FPS, BPM, and loop points. This node is useful for generating time-based events or driving animations with rhythmic precision.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
🔮| * | any type |  | 
VALUE| INT | value | 0 | 
🔄| INT | loop | 0 | 
🏎️| INT | frames per second | 24 | 
BPM| FLOAT | the number of beats per minute | 120 | 
🎶| INT | note | 4 | 
✋🏽| BOOLEAN | wait | False | 
RESET| BOOLEAN | reset | False | 
BATCH| INT | process multiple images | 1 | 

### OUTPUT

name|type|desc
:---:|:---:|---
VALUE| INT | Value 
🛟| FLOAT | Linear 
🏎️| FLOAT | Frames per second 
🔮| * | Any Type 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project