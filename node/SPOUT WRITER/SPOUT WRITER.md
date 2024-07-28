# [SPOUT WRITER (JOV) 🎥](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/SPOUT%20WRITER/SPOUT%20WRITER.md)

## JOVIMETRIX 🔺🟩🔵/DEVICE

Sends frames to a specified Spout receiver application for real-time video sharing. Accepts tensors representing images and allows configuration of parameters such as the Spout host, frame rate, resolution, scaling mode, interpolation method, and matte color. The node continuously streams frames to the specified Spout host, enabling real-time visualization or integration with other applications that support Spout.

![SPOUT WRITER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/SPOUT%20WRITER/SPOUT%20WRITER.png)

#### OUTPUT NODE?: `True`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
🚌  |  STRING  | Route | Spout Sender | 
🏎️  |  INT  | @@@ NOT USED @@@ | 30 | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🇼🇭  |  VEC2  | Width and Height as a Vector2 (x,y) | (512, 512) | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 

### OUTPUT

NONE

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project