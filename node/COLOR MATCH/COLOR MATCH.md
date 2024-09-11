[COLOR MATCH (JOV) 💞](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/COLOR%20MATCH/COLOR%20MATCH.md)
---------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/COMPOSE
  
Adjust the color scheme of one image to match another with the Color Match Node. Choose from various color matching LUTs or Reinhard matching. You can specify a custom user color maps, the number of colors, and whether to flip or invert the images.  
![COLOR MATCH](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20MATCH/COLOR%20MATCH.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾A | \* | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 👾B | \* | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | REINHARD | REINHARD, LUT |
| MAP | STRING | Custom image that will be transformed into a LUT or a built-in cv2 LUT | USER\_MAP | USER MAP, PRESET MAP |
| 🇸🇨 | STRING | One of two dozen CV2 Built-in Colormap LUT (Look Up Table) Presets | HSV | AUTUMN, BONE, JET, WINTER, RAINBOW, OCEAN, SUMMER, SPRING, COOL, HSV, PINK, HOT, PARULA, MAGMA, INFERNO, PLASMA, VIRIDIS, CIVIDIS, TWILIGHT, TWILIGHT SHIFTED, TURBO, DEEPGREEN |
| VAL | INT | The number of colors to use from the LUT during the remap. Will quantize the LUT range. | 255 |  |
| 🙃 | BOOLEAN | Flip Input A and Input B with each other | False |  |
| 🔳 | BOOLEAN | Invert the color match output | False |  |
| MATTE | VEC4INT | Define a background color for padding, if necessary. This is useful when images do not fit perfectly into the designated area and need a filler color | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project