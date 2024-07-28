# [TICK (JOV) ⏱](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TICK/TICK.md)

## JOVIMETRIX 🔺🟩🔵/CALC

A timer and frame counter, emitting pulses or signals based on time intervals. It allows precise synchronization and control over animation sequences, with options to adjust FPS, BPM, and loop points. This node is useful for generating time-based events or driving animations with rhythmic precision.

![TICK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TICK/TICK.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
⚡  |  *  | Output to send when beat (BPM setting) is<br>hit |  | 
VAL  |  INT  | the current frame number of the tick | 0 | 
🔄  |  INT  | number of frames before looping starts. 0<br>means continuous playback (no loop point) | 0 | 
🏎️  |  INT  | Fixed frame step rate based on FPS (1/FPS) | 24 | 
BPM  |  FLOAT  | BPM trigger rate to send the input. If<br>input is empty, TRUE is sent on trigger | 120 | 
🎶  |  INT  | Number of beats per measure. Quarter note<br>is 4, Eighth is 8, 16 is 16, etc. | 4 | 
✋🏽  |  BOOLEAN  | Wait | False | 
RESET  |  BOOLEAN  | Reset | False | 
BATCH  |  INT  | Number of frames wanted | 1 | 
🦶🏽  |  INT  | Steps/Stride between pulses -- useful to<br>do odd or even batches. If set to 0 will<br>stretch from (VAL -> LOOP) / Batch giving<br>a linear range of values. | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
VAL  |  INT  | Value 
🛟  |  FLOAT  | Linear 
🏎️  |  FLOAT  | Frames per second 
⚡  |  *  | Trigger 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project