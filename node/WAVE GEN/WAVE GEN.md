  
Produce waveforms like sine, square, or sawtooth with adjustable frequency, amplitude, phase, and offset. It's handy for creating oscillating patterns or controlling animation dynamics. This node emits both continuous floating-point values and integer representations of the generated waves.  
![WAVE GEN](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/WAVE%20GEN/WAVE%20GEN.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| ♒ | STRING | Wave Function | SIN | SIN, COS, TAN, SAWTOOTH, TRIANGLE, SQUARE, PULSE, RAMP, STEP, EXPONENTIAL, LOGARITHMIC, NOISE, HAVERSINE, RECTANGULAR PULSE, GAUSSIAN, CHIRP |
| FREQ | FLOAT | Frequency | 1 |  |
| 🔊 | FLOAT | Amplitude | 1 |  |
| PHASE | FLOAT | Phase | 0 |  |
| OFFSET | FLOAT | Offset | 0 |  |
| 🕛 | FLOAT | Time | 0 |  |
| 🔳 | BOOLEAN | Color Inversion | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project