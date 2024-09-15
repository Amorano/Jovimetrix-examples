[MIDI FILTER EZ (JOV) ❇️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/MIDI%20FILTER%20EZ/MIDI%20FILTER%20EZ.md)
-----------------------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/DEVICE
  
Filter MIDI messages based on various criteria, including MIDI mode (such as note on or note off), MIDI channel, control number, note number, value, and normalized value. This node is useful for processing MIDI input and selectively passing through only the desired messages. It helps simplify MIDI data handling by allowing you to focus on specific types of MIDI events.  
![MIDI FILTER EZ](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/MIDI%20FILTER%20EZ/MIDI%20FILTER%20EZ.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 🎛️ | JMIDIMSG | Midi |  |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | IGNORE | NOTE OFF, NOTE ON, IGNORE |
| CHAN | INT | Channel | -1 |  |
| 🎚️ | INT | Control | -1 |  |
| 🎶 | INT | Note | -1 |  |
| VAL | INT | Value | -1 |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🎛️ | JMIDIMSG | Midi |
| ⚡ | BOOLEAN | Trigger |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project