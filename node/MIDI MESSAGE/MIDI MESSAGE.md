[MIDI MESSAGE (JOV) 🎛️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/MIDI%20MESSAGE/MIDI%20MESSAGE.md)
-------------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/DEVICE
  
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
| 🎛️ | JMIDIMSG | Midi |
| 🔛 | BOOLEAN | On |
| chan | INT |  |
| 🎚️ | INT | Control |
| 🎶 | INT | Note |
| val | FLOAT |  |
| 0-1 | FLOAT | Normalize |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project