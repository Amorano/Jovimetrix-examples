# WAVE GEN (JOV) 🌊

## JOVIMETRIX 🔺🟩🔵/ANIMATE

The `Wave Generator` node produces waveforms like sine, square, or sawtooth with adjustable frequency, amplitude, phase, and offset. It's handy for creating oscillating patterns or controlling animation dynamics. This node emits both continuous floating-point values and integer representations of the generated waves.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
♒| COMBO[STRING] | wave function | SIN | SIN, COS, TAN, SAWTOOTH, TRIANGLE, SQUARE,<br>PULSE, RAMP, STEP, EXPONENTIAL, LOGARITHMIC,<br>NOISE, HAVERSINE, RECTANGULAR PULSE,<br>GAUSSIAN, CHIRP
FREQ| FLOAT | frequency | 1 | 
🔊| FLOAT | amplitude | 1 | 
PHASE| FLOAT | phase | 0 | 
OFFSET| FLOAT | offset | 0 | 
🕛| FLOAT | time | 0 | 
🔳| BOOLEAN | color inversion | False | 

### OUTPUT

name|type|desc
:---:|:---:|---
🛟| FLOAT | Linear 
🔟| INT | Integer 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project