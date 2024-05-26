# MIDI READER (JOV) 🎹

## JOVIMETRIX 🔺🟩🔵/DEVICE

The MIDI Reader node captures MIDI messages from an external MIDI device or controller. It monitors MIDI input and provides information about the received MIDI messages, including whether a note is being played, the MIDI channel, control number, note number, value, and a normalized value. This node is essential for integrating MIDI control into various applications, such as music production, live performances, and interactive installations.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
📟|COMBO[STRING]|device|MPKmini2 0|MPKmini2 0

### OUTPUT

name|type|desc
:---:|:---:|---
🎛️|Midi|JMIDIMSG
🔛|On|BOOLEAN
CHAN|Channel|INT
🎚️|Control|INT
🎶|Note|INT
#️⃣|Value|FLOAT
0-1|Normalize|FLOAT

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project