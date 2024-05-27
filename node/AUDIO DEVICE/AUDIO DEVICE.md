# AUDIO DEVICE (JOV) 📺

## JOVIMETRIX 🔺🟩🔵/DEVICE

The Audio Device node allows you to interact with audio input devices to capture audio data. It provides options to select the audio input device, control automatic recording triggered by the Q system, and manually adjust the recording state. This node enables integration with external audio hardware and facilitates audio data acquisition for processing within the JOVIMETRIX environment.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
📟 | STRING | device | Microsoft Sound Mapper - Input | Microsoft Sound Mapper - Input,<br>Microphone (Logitech USB Microp,<br>Microsoft Sound Mapper - Output,<br>Speakers (High Definition Audio,<br>Sceptre Z27 (NVIDIA High Defini,<br>Primary Sound Capture Driver,<br>Microphone (Logitech USB<br>Microphone), Primary Sound<br>Driver, Speakers (High<br>Definition Audio Device),<br>Sceptre Z27 (NVIDIA High<br>Definition Audio), Output<br>(NVIDIA High Definition Audio),<br>Output (), SPDIF Out (HD Audio<br>SPDIF out), Speakers (HD Audio<br>Headphone/Speakers), Microphone<br>(Logitech StreamCam)
⚡ | BOOLEAN | trigger | True | 
⏺ | BOOLEAN | arm record capture from selected<br>device | True | 

### OUTPUT

name | type | desc
:---:|:---:|---
♒ | WAVE | Wave Function 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project