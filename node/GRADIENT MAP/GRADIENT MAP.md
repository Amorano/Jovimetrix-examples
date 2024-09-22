[GRADIENT MAP (JOV) 🇲🇺](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/GRADIENT%20MAP/GRADIENT%20MAP.md)
-------------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/COMPOSE
  
Remaps an input image using a gradient lookup table (LUT). The gradient image will be translated into a single row lookup table.  
![GRADIENT MAP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GRADIENT%20MAP/GRADIENT%20MAP.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | \* | Image to remap with gradient input |  |  |
| 🇲🇺 | \* | Look up table (LUT) to remap the input image in `👾` |  |  |
| 🙃 | BOOLEAN | Reverse the gradient from left-to-right  | False |  |
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