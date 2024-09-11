[CROP (JOV) ✂️](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/CROP/CROP.md)
---------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/COMPOSE
  
Extract a portion of an input image or resize it. It supports various cropping modes, including center cropping, custom XY cropping, and free-form polygonal cropping. This node is useful for preparing image data for specific tasks or extracting regions of interest.  
![CROP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/CROP/CROP.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | \* | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| ⚒️ | STRING | Function | CENTER | CENTER, XY, FREE, HEAD, BODY |
| 🇽🇾 | VEC2 | X and Y | [0, 0] |  |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [512, 512] |  |
| TL-TR | VEC4 | Top Left - Top Right | [0, 0, 0, 1] |  |
| BL-BR | VEC4 | Bottom Left - Bottom Right | [1, 0, 1, 1] |  |
| MATTE | VEC4INT | Define a background color for padding, if necessary. This is useful when images do not fit perfectly into the designated area and need a filler color | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project