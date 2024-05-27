# SHAPE GEN (JOV) ✨

## JOVIMETRIX 🔺🟩🔵/CREATE

The Shape Generation node creates images representing various shapes such as circles, squares, rectangles, ellipses, and polygons. These shapes can be customized by adjusting parameters such as size, color, position, rotation angle, and edge blur. The node provides options to specify the shape type, the number of sides for polygons, the RGBA color value for the main shape, and the RGBA color value for the background. Additionally, you can control the width and height of the output images, the position offset, and the amount of edge blur applied to the shapes.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🇸🇴 | STRING | circle, square or polygonal<br>forms | CIRCLE | CIRCLE, SQUARE, ELLIPSE,<br>RECTANGLE, POLYGON
♾️ | INT | number of sides polygon has<br>(3-100) | 3 | 
🌈A | VEC4 | rgb with alpha color | (255, 255, 255, 255) | 
MATTE | VEC4 | background color | (0, 0, 0, 255) | 
🇼🇭 | VEC2 | width and height | (32, 32) | 
🇽🇾 | VEC2 | x and y | (0, 0) | 
📐 | FLOAT | rotation angle | 0 | 
📏 | VEC2 | scalar by which to scale the<br>input | (1.0, 1.0) | 
EDGE | STRING | clip or wrap the canvas edge | CLIP | CLIP, WRAP, WRAPX, WRAPY
BLUR | FLOAT | blur | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project