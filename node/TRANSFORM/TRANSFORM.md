[TRANSFORM (JOV) 🏝️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/TRANSFORM/TRANSFORM.md)
------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/COMPOSE
  
Apply various geometric transformations to images, including translation, rotation, scaling, mirroring, tiling and perspective projection. It offers extensive control over image manipulation to achieve desired visual effects.  
![TRANSFORM](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TRANSFORM/TRANSFORM.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | \* | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 🇽🇾 | VEC2 | X and Y | [0, 0] |  |
| 📐 | FLOAT | Rotation Angle | 0 |  |
| 📏 | VEC2 | Scalar by which to scale the input | [1.0, 1.0] |  |
| TILE | VEC2 | Title | [1.0, 1.0] |  |
| EDGE | STRING | Clip or Wrap the Canvas Edge | CLIP | CLIP, WRAP, WRAPX, WRAPY |
| 🪞 | STRING | Mirror | NONE | NONE, X, FLIP X, Y, FLIP Y, XY, X FLIP Y, FLIP XY, FLIP X FLIP Y |
| PIVOT | VEC2 | Pivot | [0.5, 0.5] |  |
| PROJ | STRING | Projection | NORMAL | NORMAL, POLAR, SPHERICAL, FISHEYE, PERSPECTIVE |
| TL-TR | VEC4 | Top Left - Top Right | [0, 0, 1, 0] |  |
| BL-BR | VEC4 | Bottom Left - Bottom Right | [0, 1, 1, 1] |  |
| 💪🏽 | FLOAT | Strength | 1 |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT |
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