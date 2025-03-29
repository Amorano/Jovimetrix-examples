  
Apply various geometric transformations to images, including translation, rotation, scaling, mirroring, tiling and perspective projection. It offers extensive control over image manipulation to achieve desired visual effects.  
![TRANSFORM](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TRANSFORM/TRANSFORM.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 😷 | IMAGE, MASK | Override Image mask |  |  |
| 🇽🇾 | VEC2 | X and Y | [0.0, 0.0] |  |
| 📐 | FLOAT | Rotation Angle | 0.0 |  |
| 📏 | VEC2 | Scalar by which to scale the input | [1.0, 1.0] |  |
| TILE | VEC2 | Title | [1.0, 1.0] |  |
| EDGE | STRING | Clip or Wrap the Canvas Edge | CLIP | CLIP, WRAP, WRAPX, WRAPY |
| 🪞 | STRING | Mirror | NONE | NONE, X, FLIP X, Y, FLIP Y, XY, X FLIP Y, FLIP XY, FLIP X FLIP Y |
| PIVOT | VEC2 | Pivot | [0.5, 0.5] |  |
| PROJ | STRING | Projection | NORMAL | NORMAL, POLAR, SPHERICAL, FISHEYE, PERSPECTIVE |
| TL-TR | VEC4 | Top Left - Top Right | [0.0, 0.0, 1.0, 0.0] |  |
| BL-BR | VEC4 | Bottom Left - Bottom Right | [0.0, 1.0, 1.0, 1.0] |  |
| 💪🏽 | FLOAT | Strength | 1 |  |
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