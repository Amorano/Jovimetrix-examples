[STACK (JOV) ➕](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/STACK/STACK.md)
-----------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/COMPOSE
  
Merge multiple input images into a single composite image by stacking them along a specified axis. Options include axis, stride, scaling mode, width and height, interpolation method, and matte color. The axis parameter allows for horizontal, vertical, or grid stacking of images, while stride controls the spacing between them.  
![STACK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STACK/STACK.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| AXIS | STRING | Choose the direction in which to stack the images. Options include horizontal, vertical, or a grid layout | GRID | HORIZONTAL, VERTICAL, GRID |
| 🦶🏽 | INT | Specify the spacing between each stacked image. This determines how far apart the images are from each other | 1 |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT, RESIZE MATTE |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [512, 512] |  |
| 🎞️ | STRING | Select the method for resizing images. Options range from nearest neighbor to advanced methods like Lanczos, ensuring the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
| MATTE | VEC4INT | Define a background color for padding, if necessary. This is useful when images do not fit perfectly into the designated area and need a filler color | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project