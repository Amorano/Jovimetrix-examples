# MIDI READER (JOV) 🎹

## JOVIMETRIX 🔺🟩🔵/DEVICE

Captures MIDI messages from an external MIDI device or controller. It monitors MIDI input and provides information about the received MIDI messages, including whether a note is being played, the MIDI channel, control number, note number, value, and a normalized value. This node is essential for integrating MIDI control into various applications, such as music production, live performances, and interactive installations.

![MIDI READER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/MIDI%20READER/MIDI%20READER.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
📟  |  STRING  | Device |  | 

### OUTPUT

name | type | desc
:---:|:---:|---
🎛️  |  JMIDIMSG  | Midi 
🔛  |  BOOLEAN  | On 
CHAN  |  INT  | Channel 
🎚️  |  INT  | Control 
🎶  |  INT  | Note 
VAL  |  FLOAT  | Value 
0-1  |  FLOAT  | Normalize 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project