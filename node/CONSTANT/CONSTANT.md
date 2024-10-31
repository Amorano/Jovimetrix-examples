[CONSTANT (JOV) 🟪](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/CONSTANT/CONSTANT.md)
--------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/CREATE
  
Generate a constant image or mask of a specified size and color. It can be used to create solid color backgrounds or matte images for compositing with other visual elements. The node allows you to define the desired width and height of the output and specify the RGBA color value for the constant output. Additionally, you can input an optional image to use as a matte with the selected color.  
![CONSTANT](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/CONSTANT/CONSTANT.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | \* | Optional Image to Matte with Selected Color |  |  |
| 🌈A | VEC4INT | Constant Color to Output | [0, 0, 0, 255] |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT, RESIZE MATTE |
| 🇼🇭 | VEC2INT | Desired Width and Height of the Color Output | [512, 512] |  |
| 🎞️ | STRING | Select the method for resizing images. Options range from nearest neighbor to advanced methods like Lanczos, ensuring the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project