# STREAM READER (JOV) 📺

## JOVIMETRIX 🔺🟩🔵/DEVICE

The Stream Reader node captures frames from various sources such as URLs, cameras, monitors, windows, or Spout streams. It supports batch processing, allowing multiple frames to be captured simultaneously. The node provides options for configuring the source, resolution, frame rate, zoom, orientation, and interpolation method. Additionally, it supports capturing frames from multiple monitors or windows simultaneously. The captured frames are returned as tensors, enabling further processing downstream.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
SRC | STRING | source | URL | URL, CAMERA, MONITOR, WINDOW,<br>SPOUT
🌐 | STRING | url |  | 
📹 | STRING | camera | NONE | 
🖥 | STRING | monitor | 0 - 3840x2160 | 0 - 3840x2160, 1 - 1600x1200, 2<br>- 3840x2160
🪟 | STRING | window | 500 Internal Server Error — Mozilla Firefox - 723094 | 500 Internal Server Error —<br>Mozilla Firefox - 723094,<br>COMFYUI - 7669176, lexicon.py -<br>jovimetrix (Workspace) - Visual<br>Studio Code - 656876, Preview<br>ADJUST.md - jovimetrix-examples<br>(Workspace) - Visual Studio Code<br>- 984236, #apes | ☢ MORANOLAND ☢<br>- Discord - 263998, Jovimetrix-<br>examples/wf/texture/texture.md<br>at master · Amorano/Jovimetrix-<br>examples — Mozilla Firefox -<br>1377846, MatisseTec - Twitch —<br>Mozilla Firefox - 3737110
DPI | BOOLEAN | use dpi mode from os | True | 
🔲 | VEC4 | bounding box | (0, 0, 1, 1) | 
🏎️ | INT | frames per second | 30 | 
✋🏽 | BOOLEAN | wait | False | 
BATCH | VEC2 | process multiple images | (1, 30) | 
🧭 | STRING | orientation | NORMAL | NORMAL, FLIPX, FLIPY, FLIPXY
🔎 | FLOAT | zoom | 0 | 
MODE | STRING | scaling mode | NONE | NONE, CROP, MATTE, FIT, ASPECT,<br>ASPECT SHORT
🇼🇭 | VEC2 | width and height | (32, 32) | 
🎞️ | STRING | sampling method to apply when<br>rescaling | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA,<br>LANCZOS4, LINEAR EXACT, NEAREST<br>EXACT
MATTE | VEC4 | background color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project