  
Simulate color blindness effects on images. You can select various types of color deficiencies, adjust the severity of the effect, and apply the simulation using different simulators. This node is ideal for accessibility testing and design adjustments, ensuring inclusivity in your visual content.  
![COLOR BLIND](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20BLIND/COLOR%20BLIND.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| DEFICIENCY | STRING | Type of color deficiency: Red (Protanopia), Green (Deuteranopia), Blue (Tritanopia) | PROTAN | PROTAN, DEUTAN, TRITAN |
| SIMULATOR | STRING | Solver to use when translating to new color space | AUTOSELECT | AUTOSELECT, BRETTEL1997, COBLISV1, COBLISV2, MACHADO2009, VIENOT1999, VISCHECK |
| VAL | FLOAT | alpha blending | 1 |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output. |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha. |
| 😷 | MASK | Single channel mask output. |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project