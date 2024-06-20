# STREAM READER (JOV) 📺

## JOVIMETRIX 🔺🟩🔵/DEVICE

The Stream Reader node captures frames from various sources such as URLs, cameras, monitors, windows, or Spout streams. It supports batch processing, allowing multiple frames to be captured simultaneously. The node provides options for configuring the source, resolution, frame rate, zoom, orientation, and interpolation method. Additionally, it supports capturing frames from multiple monitors or windows simultaneously. The captured frames are returned as tensors, enabling further processing downstream.

![STREAM READER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STREAM%20READER/STREAM%20READER.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
SRC | STRING | source | URL | URL, CAMERA, MONITOR, WINDOW,<br>SPOUT
🌐 | STRING | url |  | 
📹 | STRING | camera | dynamic | list of system streaming devices
🖥 | STRING | monitor | dynamic | list of system monitor devices
🪟 | STRING | window | dynamic | list of available system windows
DPI | BOOLEAN | use dpi mode from os | True | 
🔲 | VEC4 | bounding box | (0, 0, 1, 1) | 
🏎️ | INT | frames per second | 30 | 
✋🏽 | BOOLEAN | wait | False | 
BATCH | VEC2 | output as a batch (all images in<br>a single tensor) or as a list of<br>images (each image processed<br>separately) | (1, 30) | 
🧭 | STRING | orientation | NORMAL | NORMAL, FLIPX, FLIPY, FLIPXY
🔎 | FLOAT | zoom | 0 | 
MODE | STRING | decide whether the images should<br>be resized to fit a specific<br>dimension. available modes<br>include scaling to fit within<br>given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT,<br>ASPECT SHORT
🇼🇭 | VEC2 | set the target dimensions for<br>the output image if scaling is<br>applied | (32, 32) | 
🎞️ | STRING | select the method for resizing<br>images. options range from<br>nearest neighbor to advanced<br>methods like lanczos, ensuring<br>the best quality for the<br>specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA,<br>LANCZOS4, LINEAR EXACT, NEAREST<br>EXACT
MATTE | VEC4 | define a background color for<br>padding, if necessary. this is<br>useful when images do not fit<br>perfectly into the designated<br>area and need a filler color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project