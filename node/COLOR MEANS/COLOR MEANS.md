  
The top-k colors ordered from most->least used as a strip, tonal palette and 3D LUT.  
![COLOR MEANS](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20MEANS/COLOR%20MEANS.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| VAL | INT | The top K colors to select. | 12 |  |
| 📏 | INT | Height of the tones in the strip. Width is based on input. | 32 |  |
| COUNT | INT | Number of nodes to use in interpolation of full LUT (256 is every pixel). | 33 |  |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [256, 256] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Sequence of top-K colors. Count depends on value in `VAL`. |
| 🎨 | IMAGE | Simple Tone palette based on result top-K colors. Width is taken from input. |
| 🇲🇺 | IMAGE | Gradient of top-K colors. |
| 😎 | JLUT | Full 3D LUT of the image mapped to the resultant top-K colors chosen. |
| 🌈 | IMAGE | Visualization of full 3D .cube LUT in JLUT output |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project