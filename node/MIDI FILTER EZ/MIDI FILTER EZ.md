# MIDI FILTER EZ (JOV) ❇️

## JOVIMETRIX 🔺🟩🔵/DEVICE

The MIDI Filter EZ node allows you to filter MIDI messages based on various criteria, including MIDI mode (such as note on or note off), MIDI channel, control number, note number, value, and normalized value. This node is useful for processing MIDI input and selectively passing through only the desired messages. It helps simplify MIDI data handling by allowing you to focus on specific types of MIDI events.

![MIDI FILTER EZ](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/MIDI%20FILTER%20EZ/MIDI%20FILTER%20EZ.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🎛️ | JMIDIMSG | midi |  | 
MODE | STRING | scaling mode | IGNORE | NOTE OFF, NOTE ON, IGNORE
CHAN | INT | channel | -1 | 
🎚️ | INT | control | -1 | 
🎶 | INT | note | -1 | 
VAL | INT | value | -1 | 
0-1 | FLOAT | normalize | -1 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🎛️ | JMIDIMSG | Midi 
⚡ | BOOLEAN | Trigger 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project