# STREAM READER (JOV) 📺

## JOVIMETRIX 🔺🟩🔵/DEVICE

The Stream Reader node captures frames from various sources such as URLs, cameras, monitors, windows, or Spout streams. It supports batch processing, allowing multiple frames to be captured simultaneously. The node provides options for configuring the source, resolution, frame rate, zoom, orientation, and interpolation method. Additionally, it supports capturing frames from multiple monitors or windows simultaneously. The captured frames are returned as tensors, enabling further processing downstream.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
SRC| COMBO[STRING] | source | URL | URL, CAMERA, MONITOR, WINDOW, SPOUT
🌐| STRING | url |  | 
📹| COMBO[STRING] | camera | NONE | 
🖥| COMBO[STRING] | monitor | 0 - 3840x2160 | 0 - 3840x2160, 1 - 1600x1200, 2 - 3840x2160
🪟| COMBO[STRING] | window | Mozilla Firefox - 198146 | Mozilla Firefox - 198146, COMFYUI - 4457256,<br>lexicon.py - jovimetrix (Workspace) - Visual<br>Studio Code - 1769950, @matisse - Discord -<br>131392, C:\dev\ComfyUI\ComfyUI\custom<br>nodes\Jovimetrix\ md - 1311414
DPI| BOOLEAN | use dpi mode from os | True | 
🔲| VEC4 | bounding box | (0, 0, 1, 1) | 
🏎️| INT | frames per second | 30 | 
✋🏽| BOOLEAN | wait | False | 
BATCH| VEC2 | process multiple images | (1, 30) | 
🧭| COMBO[STRING] | orientation | NORMAL | NORMAL, FLIPX, FLIPY, FLIPXY
🔎| FLOAT | zoom | 0 | 
MODE| COMBO[STRING] | scaling mode | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT SHORT
🇼🇭| VEC2 | width and height | (32, 32) | 
🎞️| COMBO[STRING] | sampling method to apply when<br>rescaling | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE| VEC4 | background color | (0, 0, 0, 255) | 

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️| IMAGE | Image 
🌈| IMAGE | RGB (no alpha) Color 
😷| MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project