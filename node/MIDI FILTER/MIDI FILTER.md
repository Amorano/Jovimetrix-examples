## [MIDI FILTER (JOV) ✳️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/MIDI%20FILTER/MIDI%20FILTER.md)

## JOVIMETRIX 🔺🟩🔵/DEVICE

Provides advanced filtering capabilities for MIDI messages based on various criteria, including MIDI mode (such as note on or note off), MIDI channel, control number, note number, value, and normalized value. It allows you to filter out unwanted MIDI events and selectively process only the desired ones. This node offers flexibility in MIDI data processing, enabling precise control over which MIDI messages are passed through for further processing.

![MIDI FILTER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/MIDI%20FILTER/MIDI%20FILTER.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🎛️  |  JMIDIMSG  | Midi |  | 
🔛  |  STRING  | On | IGNORE | NOTE OFF, NOTE ON, IGNORE
CHAN  |  STRING  | Channel |  | 
🎚️  |  STRING  | Control |  | 
🎶  |  STRING  | Note |  | 
VAL  |  STRING  | Value |  | 
0-1  |  STRING  | Normalize |  | 

## OUTPUT

name | type | desc
:---:|:---:|---
🎛️  |  JMIDIMSG  | Midi 
⚡  |  BOOLEAN  | Trigger 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project