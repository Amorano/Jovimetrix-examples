# MIDI FILTER (JOV) ✳️

## JOVIMETRIX 🔺🟩🔵/DEVICE

The MIDI Filter node provides advanced filtering capabilities for MIDI messages based on various criteria, including MIDI mode (such as note on or note off), MIDI channel, control number, note number, value, and normalized value. It allows you to filter out unwanted MIDI events and selectively process only the desired ones. This node offers flexibility in MIDI data processing, enabling precise control over which MIDI messages are passed through for further processing.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🎛️ | JMIDIMSG | midi |  | 
🔛 | STRING | on | IGNORE | NOTE OFF, NOTE ON, IGNORE
CHAN | STRING | channel |  | 
🎚️ | STRING | control |  | 
🎶 | STRING | note |  | 
\# | STRING | value |  | 
0-1 | STRING | normalize |  | 

### OUTPUT

name | type | desc
:---:|:---:|---
🎛️ | JMIDIMSG | Midi 
⚡ | BOOLEAN | Trigger 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project