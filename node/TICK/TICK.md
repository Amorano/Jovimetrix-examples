  
A timer and frame counter, emitting pulses or signals based on time intervals. It allows precise synchronization and control over animation sequences, with options to adjust FPS, BPM, and loop points. This node is useful for generating time-based events or driving animations with rhythmic precision.  
![TICK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TICK/TICK.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| ⚡ | \* | Output to send when beat (BPM setting) is hit |  |  |
| VAL | INT | the current frame number of the tick | 0 |  |
| 🔄 | INT | number of frames before looping starts. 0 means continuous playback (no loop point) | 0 |  |
| 🏎️ | INT | Fixed frame step rate based on FPS (1/FPS) | 24 |  |
| BPM | INT | BPM trigger rate to send the input. If input is empty, TRUE is sent on trigger | 120 |  |
| 🎶 | INT | Number of beats per measure. Quarter note is 4, Eighth is 8, 16 is 16, etc. | 4 |  |
| ✋🏽 | BOOLEAN | Wait | False |  |
| RESET | BOOLEAN | Reset | False |  |
| BATCH | INT | Number of frames wanted | 1 |  |
| 🦶🏽 | INT | Steps/Stride between pulses -- useful to do odd or even batches. If set to 0 will stretch from (VAL -> LOOP) / Batch giving a linear range of values. | 0 |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| val | INT | Current value for the configured tick as ComfyUI List |
| 🛟 | FLOAT | Normalized tick value (0..1) based on BPM and Loop |
| 🏎️ | FLOAT | Current 'frame' in the tick based on FPS setting |
| ⚡ | \* | Based on the BPM settings, on beat hit, output the input at '⚡' |
| batch | \* | Current batch of values for the configured tick as standard list which works in other Jovimetrix nodes |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project