[SHAPE GEN (JOV) ✨](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/SHAPE%20GEN/SHAPE%20GEN.md)
---------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/CREATE
  
Create n-sided polygons. These shapes can be customized by adjusting parameters such as size, color, position, rotation angle, and edge blur. The node provides options to specify the shape type, the number of sides for polygons, the RGBA color value for the main shape, and the RGBA color value for the background. Additionally, you can control the width and height of the output images, the position offset, and the amount of edge blur applied to the shapes.  
![SHAPE GEN](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/SHAPE%20GEN/SHAPE%20GEN.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| SHAPE | STRING | Circle, Square or Polygonal forms | CIRCLE | CIRCLE, SQUARE, ELLIPSE, RECTANGLE, POLYGON |
| SIDES | INT | Number of sides polygon has (3-100) | 3 |  |
| 🌈A | VEC4INT | Main Shape Color | [255, 255, 255, 255] |  |
| MATTE | VEC4INT | Background Color | [0, 0, 0, 255] |  |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [256, 256] |  |
| 🇽🇾 | VEC2 | X and Y | [0, 0] |  |
| 📐 | FLOAT | Rotation Angle | 0 |  |
| 📏 | VEC2 | Scalar by which to scale the input | [1.0, 1.0] |  |
| EDGE | STRING | Clip or Wrap the Canvas Edge | CLIP | CLIP, WRAP, WRAPX, WRAPY |
| BLUR | FLOAT | Edge blur amount (Gaussian blur) | 0 |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project