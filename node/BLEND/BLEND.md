  
Combine two input images using various blending modes, such as normal, screen, multiply, overlay, etc. It also supports alpha blending and masking to achieve complex compositing effects. This node is essential for creating layered compositions and adding visual richness to images.  
![BLEND](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/BLEND/BLEND.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾A | IMAGE, MASK | Background Plate |  |  |
| 👾B | IMAGE, MASK | Image to Overlay on Background Plate |  |  |
| 😷 | IMAGE, MASK | Optional Mask to use for Alpha Blend Operation. If empty, will use the ALPHA of B |  |  |
| ⚒️ | STRING | Blending Operation | NORMAL | NORMAL, ADDITIVE, NEGATION, DIFFERENCE, MULTIPLY, DIVIDE, LIGHTEN, DARKEN, SCREEN, BURN, DODGE, OVERLAY, HUE, SATURATION, LUMINOSITY, COLOR, SOFT, HARD, PIN, VIVID, EXCLUSION, REFLECT, GLOW, XOR, EXTRACT |
| ⬜ | FLOAT | Amount of Blending to Perform on the Selected Operation | 1 |  |
| 🙃 | BOOLEAN | Flip Input A and Input B with each other | False |  |
| 🔳 | BOOLEAN | Invert the mask input | False |  |
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