  
Captures MIDI messages from an external MIDI device or controller. It monitors MIDI input and provides information about the received MIDI messages, including whether a note is being played, the MIDI channel, control number, note number, value, and a normalized value. This node is essential for integrating MIDI control into various applications, such as music production, live performances, and interactive installations.  
![MIDI READER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/MIDI%20READER/MIDI%20READER.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 📟 | STRING | Device |  |  |
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