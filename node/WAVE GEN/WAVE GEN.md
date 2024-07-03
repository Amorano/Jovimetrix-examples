# WAVE GEN (JOV) 🌊

## JOVIMETRIX 🔺🟩🔵/CALC

The `Wave Generator` node produces waveforms like sine, square, or sawtooth with adjustable frequency, amplitude, phase, and offset. It's handy for creating oscillating patterns or controlling animation dynamics. This node emits both continuous floating-point values and integer representations of the generated waves.

![WAVE GEN](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/WAVE%20GEN/WAVE%20GEN.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
♒  |  STRING  | Wave Function | SIN | SIN, COS, TAN, SAWTOOTH, TRIANGLE, SQUARE,<br>PULSE, RAMP, STEP, EXPONENTIAL,<br>LOGARITHMIC, NOISE, HAVERSINE, RECTANGULAR<br>PULSE, GAUSSIAN, CHIRP
FREQ  |  FLOAT  | Frequency | 1 | 
🔊  |  FLOAT  | Amplitude | 1 | 
PHASE  |  FLOAT  | Phase | 0 | 
OFFSET  |  FLOAT  | Offset | 0 | 
🕛  |  FLOAT  | Time | 0 | 
🔳  |  BOOLEAN  | Color Inversion | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🛟  |  FLOAT  | Linear 
🔟  |  INT  | Integer 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project