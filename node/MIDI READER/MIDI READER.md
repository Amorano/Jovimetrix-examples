[MIDI READER (JOV) 🎹](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/MIDI%20READER/MIDI%20READER.md)
---------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/DEVICE
  
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
| 🎛️ | JMIDIMSG | Midi |
| 🔛 | BOOLEAN | On |
| chan | INT |  |
| 🎚️ | INT | Control |
| 🎶 | INT | Note |
| val | FLOAT |  |
| 0-1 | FLOAT | Normalize |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project