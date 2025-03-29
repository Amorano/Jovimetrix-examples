  
Sends frames to a specified route, typically for live streaming or recording purposes. It accepts tensors representing images and allows configuration of parameters such as route, resolution, scaling mode, interpolation method, and matte color. The node continuously streams frames to the specified route, enabling real-time visualization or recording of processed video data.  
![STREAM WRITER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STREAM%20WRITER/STREAM%20WRITER.png)
### OUTPUT NODE?: True
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 🚌 | STRING | Route | /stream |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT, RESIZE MATTE |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [512, 512] |  |
| 🎞️ | STRING | Method for resizing images. | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
| MATTE | VEC4INT | Background color for padding | [0, 0, 0, 0] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project