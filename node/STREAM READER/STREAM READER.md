  
Capture frames from various sources such as URLs, cameras, monitors, windows, or Spout streams. It supports batch processing, allowing multiple frames to be captured simultaneously. The node provides options for configuring the source, resolution, frame rate, zoom, orientation, and interpolation method. Additionally, it supports capturing frames from multiple monitors or windows simultaneously. The captured frames are returned as tensors, enabling further processing downstream.  
![STREAM READER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STREAM%20READER/STREAM%20READER.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| SRC | STRING | Source | URL | URL, CAMERA, MONITOR, WINDOW, SPOUT |
| 🌐 | STRING | URL |  |  |
| 📹 | STRING | Camera | dynamic | list of system streaming devices |
| 🖥 | STRING | Monitor | dynamic | list of system monitor devices |
| 🪟 | STRING | Window | dynamic | list of available system windows |
| DPI | BOOLEAN | Use DPI mode from OS | True |  |
| 🔲 | VEC4 | Define an inner bounding box using relative coordinates [0..1] as a box region to clip. | [0, 0, 1, 1] |  |
| 🏎️ | INT | Frames per second | 30 |  |
| ✋🏽 | BOOLEAN | Wait | False |  |
| BATCH | VEC2INT | Number of frames wanted and the FPS | [1, 30] |  |
| 🧭 | STRING | Orientation | NORMAL | NORMAL, FLIPX, FLIPY, FLIPXY |
| 🔎 | FLOAT | ZOOM | 0.0 |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT, RESIZE MATTE |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [512, 512] |  |
| 🎞️ | STRING | Method for resizing images. | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
| MATTE | VEC4INT | Background color for padding | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output. |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha. |
| 😷 | MASK | Single channel mask output. |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project