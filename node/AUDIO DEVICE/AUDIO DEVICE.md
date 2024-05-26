# AUDIO DEVICE (JOV) 📺

## JOVIMETRIX 🔺🟩🔵/DEVICE

The Audio Device node allows you to interact with audio input devices to capture audio data. It provides options to select the audio input device, control automatic recording triggered by the Q system, and manually adjust the recording state. This node enables integration with external audio hardware and facilitates audio data acquisition for processing within the JOVIMETRIX environment.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
📟|COMBO[STRING]|device|Microsoft Sound Mapper - Input|Microsoft Sound Mapper - Input, Microphone (Logitech USB<br>Microp, Microsoft Sound Mapper - Output, Speakers (High<br>Definition Audio, Sceptre Z27 (NVIDIA High Defini, Primary<br>Sound Capture Driver, Microphone (Logitech USB Microphone),<br>Primary Sound Driver, Speakers (High Definition Audio<br>Device), Sceptre Z27 (NVIDIA High Definition Audio), Output<br>(NVIDIA High Definition Audio), SPDIF Out (HD Audio SPDIF<br>out), Speakers (HD Audio Headphone/Speakers), Microphone<br>(Logitech StreamCam)
⚡|BOOLEAN|trigger|True|
⏺|BOOLEAN|arm record capture from selected device|True|

### OUTPUT

name|type|desc
:---:|:---:|---
♒|Wave Function|WAVE

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project