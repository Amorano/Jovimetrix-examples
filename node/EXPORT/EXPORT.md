  
Responsible for saving images or animations to disk. It supports various output formats such as GIF and GIFSKI. Users can specify the output directory, filename prefix, image quality, frame rate, and other parameters. Additionally, it allows overwriting existing files or generating unique filenames to avoid conflicts. The node outputs the saved images or animation as a tensor.  
![EXPORT](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/EXPORT/EXPORT.png)
### OUTPUT NODE?: True
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾 | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 📤 | STRING | Pass through another route node to pre-populate the outputs. | <comfy output dir> |  |
| FORMAT | STRING | Pass through another route node to pre-populate the outputs. | gifski | gifski, gif, png, jpg |
| PREFIX | STRING | Pass through another route node to pre-populate the outputs. | jovi |  |
| OVERWRITE | BOOLEAN | Pass through another route node to pre-populate the outputs. | False |  |
| OPT | BOOLEAN | Pass through another route node to pre-populate the outputs. | False |  |
| QUALITY | INT | Pass through another route node to pre-populate the outputs. | 90 |  |
| MOTION | INT | Pass through another route node to pre-populate the outputs. | 100 |  |
| 🏎️ | INT | Pass through another route node to pre-populate the outputs. | 24 |  |
| 🔄 | INT | Pass through another route node to pre-populate the outputs. | 0 |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project