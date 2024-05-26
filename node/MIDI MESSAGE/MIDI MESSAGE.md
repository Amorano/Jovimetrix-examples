# MIDI MESSAGE (JOV) 🎛️

## JOVIMETRIX 🔺🟩🔵/DEVICE

The MIDI Message node processes MIDI messages received from an external MIDI controller or device. It accepts MIDI messages as input and returns various attributes of the MIDI message, including whether the message is valid, the MIDI channel, control number, note number, value, and normalized value. This node is useful for integrating MIDI control into creative projects, allowing users to respond to MIDI input in real-time.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
🎛️|JMIDIMSG|midi||

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