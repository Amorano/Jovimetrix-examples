  
Generate a color harmony based on the selected scheme. Supported schemes include complimentary, analogous, triadic, tetradic, and more. Users can customize the angle of separation for color calculations, offering flexibility in color manipulation and exploration of different color palettes.  
![COLOR THEORY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20THEORY/COLOR%20THEORY.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| SCHEME | STRING | Scheme | COMPLIMENTARY | COMPLIMENTARY, MONOCHROMATIC, SPLIT COMPLIMENTARY, ANALOGOUS, TRIADIC, SQUARE, COMPOUND, CUSTOM TETRAD |
| VAL | INT | Custom angle of separation to use when calculating colors | 45 |  |
| 🔳 | BOOLEAN | Color Inversion | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project