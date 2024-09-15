[GLSL COLOR CONVERSION (JOV) 🧙🏽](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/GLSL%20COLOR%20CONVERSION/GLSL%20COLOR%20CONVERSION.md)
--------------------------------------------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/GLSL/COLOR
Convert an image from one color space (RGB, HSV, LAB, XYZ) to another.
![GLSL COLOR CONVERSION](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20COLOR%20CONVERSION/GLSL%20COLOR%20CONVERSION.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| image | \* | Image to convert |  |  |
| operator | STRING | conversion operation to perform. | RGB2HSV | RGB2HSV, RGB2LAB, RGB2XYZ, HSV2RGB, HSV2LAB, HSV2XYZ, LAB2RGB, LAB2HSV, LAB2XYZ, XYZ2RGB, XYZ2HSV, XYZ2LAB |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [512, 512] |  |
| 🎞️ | STRING | Select the method for resizing images. Options range from nearest neighbor to advanced methods like Lanczos, ensuring the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
| MATTE | VEC4INT | Define a background color for padding, if necessary. This is useful when images do not fit perfectly into the designated area and need a filler color | [0, 0, 0, 255] |  |
| EDGE\_X | STRING | Clip or Wrap the Canvas Edge | CLAMP | CLAMP, WRAP, MIRROR |
| EDGE\_Y | STRING | Clip or Wrap the Canvas Edge | CLAMP | CLAMP, WRAP, MIRROR |
| FRAGMENT | JDATABUCKET | Select a fragment program to load |  |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project