  
Takes an input image and splits it into its individual color channels (red, green, blue), along with a mask channel. This node is useful for separating different color components of an image for further processing or analysis.  
![PIXEL SPLIT](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/PIXEL%20SPLIT/PIXEL%20SPLIT.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| ❤️ | MASK | Single channel output of Red Channel. |
| 💚 | MASK | Single channel output of Green Channel |
| 💙 | MASK | Single channel output of Blue Channel |
| 🤍 | MASK | Single channel output of Alpha Channel |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project