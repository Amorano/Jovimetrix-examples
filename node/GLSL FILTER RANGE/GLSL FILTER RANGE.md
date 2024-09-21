[GLSL FILTER RANGE (JOV) 🧙🏽](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/GLSL%20FILTER%20RANGE/GLSL%20FILTER%20RANGE.md)
--------------------------------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/GLSL/FILTER
Select pixels from start color through end color. Maintains alpha/mask.
![GLSL FILTER RANGE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20FILTER%20RANGE/GLSL%20FILTER%20RANGE.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| image | \* | RGB(A) image |  |  |
| start | VEC3 | Start of the Range | [0, 0, 0] |  |
| end | VEC3 | End of the Range | [1.0, 1.0, 1.0] |  |
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