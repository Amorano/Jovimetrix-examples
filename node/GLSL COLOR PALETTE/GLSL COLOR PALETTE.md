[GLSL COLOR PALETTE (JOV) 🧙🏽](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/GLSL%20COLOR%20PALETTE/GLSL%20COLOR%20PALETTE.md)
-----------------------------------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/GLSL/CREATE
Color palette creation using the formula: color(t) = a + b \* cos[tau(c\*t+d)]. See https://iquilezles.org/articles/palettes for more information.
![GLSL COLOR PALETTE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20COLOR%20PALETTE/GLSL%20COLOR%20PALETTE.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| bias | VEC3 | scale and bias (dc offset) | [0.5, 0.5, 0.5] |  |
| amp | VEC3 | contrast and brightness (amplitude) | [0.5, 0.5, 0.5] |  |
| freq | VEC3 | color cycle (R, G and B) (frequency) | [1.0, 1.0, 1.0] |  |
| phase | VEC3 | starting offset for the cycle | [0, 0, 0] |  |
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