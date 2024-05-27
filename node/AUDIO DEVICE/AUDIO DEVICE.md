# AUDIO DEVICE (JOV) 📺

## JOVIMETRIX 🔺🟩🔵/DEVICE

The Audio Device node allows you to interact with audio input devices to capture audio data. It provides options to select the audio input device, control automatic recording triggered by the Q system, and manually adjust the recording state. This node enables integration with external audio hardware and facilitates audio data acquisition for processing within the JOVIMETRIX environment.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
📟 | STRING | device | dynamic | system list of audio devices
⚡ | BOOLEAN | trigger | True | 
⏺ | BOOLEAN | arm record capture from selected<br>device | True | 

### OUTPUT

name | type | desc
:---:|:---:|---
♒ | WAVE | Wave Function 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project