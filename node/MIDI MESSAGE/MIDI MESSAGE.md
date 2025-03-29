  
Processes MIDI messages received from an external MIDI controller or device. It accepts MIDI messages as input and returns various attributes of the MIDI message, including whether the message is valid, the MIDI channel, control number, note number, value, and normalized value. This node is useful for integrating MIDI control into creative projects, allowing users to respond to MIDI input in real-time.  
![MIDI MESSAGE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/MIDI%20MESSAGE/MIDI%20MESSAGE.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 🎛️ | JMIDIMSG | Midi |  |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🎛️ | JMIDIMSG | MIDI bus that contains the full MIDI message |
| 🔛 | BOOLEAN | The state of the note -- either `ON` or `OFF` |
| chan | INT | MIDI channel sent in the MIDI message |
| 🎚️ | INT | The control number sent in the MIDI message |
| 🎶 | INT | Note value (0-127) sent in the MIDI message |
| val | FLOAT | If this was a control messge, the control value (0-127) sent in the MIDI message |
| 0-1 | FLOAT | If this was a control messge, the control value normalized to 0-1 |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project