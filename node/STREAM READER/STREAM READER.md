# STREAM READER (JOV) 📺

## JOVIMETRIX 🔺🟩🔵/DEVICE

The Stream Reader node captures frames from various sources such as URLs, cameras, monitors, windows, or Spout streams. It supports batch processing, allowing multiple frames to be captured simultaneously. The node provides options for configuring the source, resolution, frame rate, zoom, orientation, and interpolation method. Additionally, it supports capturing frames from multiple monitors or windows simultaneously. The captured frames are returned as tensors, enabling further processing downstream.

![STREAM READER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STREAM%20READER/STREAM%20READER.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
SRC  |  STRING  | Source | URL | URL, CAMERA, MONITOR, WINDOW, SPOUT
🌐  |  STRING  | URL |  | 
📹  |  STRING  | Camera | dynamic | list of system streaming devices
🖥  |  STRING  | Monitor | dynamic | list of system monitor devices
🪟  |  STRING  | Window | dynamic | list of available system windows
DPI  |  BOOLEAN  | Use DPI mode from OS | True | 
🔲  |  VEC4  | Bounding box | (0, 0, 1, 1) | 
🏎️  |  INT  | Frames per second | 30 | 
✋🏽  |  BOOLEAN  | Wait | False | 
BATCH  |  VEC2  | Number of frames wanted and the FPS | (1, 30) | 
🧭  |  STRING  | Orientation | NORMAL | NORMAL, FLIPX, FLIPY, FLIPXY
🔎  |  FLOAT  | ZOOM | 0.0 | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🇼🇭  |  VEC2  | Set the target dimensions for the output<br>image if scaling is applied | (512, 512) | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project