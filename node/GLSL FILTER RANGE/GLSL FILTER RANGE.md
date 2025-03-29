Select pixels from start color through end color. Maintains alpha/mask.
![GLSL FILTER RANGE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL%20FILTER%20RANGE/GLSL%20FILTER%20RANGE.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| image | IMAGE, MASK | RGB(A) image |  |  |
| start | VEC3 | Start of the Range | [0, 0, 0] |  |
| end | VEC3 | End of the Range | [1.0, 1.0, 1.0] |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT, RESIZE MATTE |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [512, 512] |  |
| 🎞️ | STRING | Method for resizing images. | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
| MATTE | VEC4INT | Background color for padding | [0, 0, 0, 255] |  |
| EDGE\_X | STRING | Clip or Wrap the Canvas Edge | CLAMP | CLAMP, WRAP, MIRROR |
| EDGE\_Y | STRING | Clip or Wrap the Canvas Edge | CLAMP | CLAMP, WRAP, MIRROR |
| FRAGMENT | JDATABUCKET | Select a fragment program to load |  |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output. |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha. |
| 😷 | MASK | Single channel mask output. |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project