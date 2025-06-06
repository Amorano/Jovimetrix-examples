  
Define a range and apply it to an image for segmentation and feature extraction. Choose from various threshold modes, such as binary and adaptive, and adjust the threshold value and block size to suit your needs. You can also invert the resulting mask if necessary. This node is versatile for a variety of image processing tasks.  
![THRESHOLD](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/THRESHOLD/THRESHOLD.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 🧬 | STRING | X-Men | ADAPT\_NONE | ADAPT NONE, ADAPT MEAN, ADAPT GAUSS |
| ⚒️ | STRING | Function | BINARY | BINARY, TRUNC, TOZERO |
| 📉 | FLOAT | Threshold | 0.5 |  |
| 📏 | INT | Scalar by which to scale the input | 3 |  |
| 🔳 | BOOLEAN | Invert the mask input | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output. |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha. |
| 😷 | MASK | Single channel mask output. |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project