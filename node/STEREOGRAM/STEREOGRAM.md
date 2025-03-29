  
Generates false perception 3D images from 2D input. Set tile divisions, noise, gamma, and shift parameters to control the stereogram's appearance.  
![STEREOGRAM](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STEREOGRAM/STEREOGRAM.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| DEPTH | IMAGE, MASK | Grayscale image representing a depth map |  |  |
| TILE | INT | Title | 8 |  |
| NOISE | FLOAT | Noise | 0.33 |  |
| 🔆 | FLOAT | Gamma | 0.33 |  |
| SHIFT | FLOAT | Shift | 1.0 |  |
| 🔳 | BOOLEAN | Color Inversion | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output. |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha. |
| 😷 | MASK | Single channel mask output. |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project