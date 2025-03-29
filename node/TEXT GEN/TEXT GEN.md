  
Generates images containing text based on parameters such as font, size, alignment, color, and position. Users can input custom text messages, select fonts from a list of available options, adjust font size, and specify the alignment and justification of the text. Additionally, the node provides options for auto-sizing text to fit within specified dimensions, controlling letter-by-letter rendering, and applying edge effects such as clipping and inversion.  
![TEXT GEN](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TEXT%20GEN/TEXT%20GEN.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 📝 | STRING | Your Message | jovimetrix |  |
| FONT | STRING | Available System Fonts | Almendra | Almendra, Alphabutt Base A, Alphabutt Letters A, Arial, BIG BREAST FONT, Bahnschrift, Caladea, Calibri, Cambria, Candara, Carlito, Cascadia Code, Cascadia Mono, Comic Sans MS, Consolas, Constantia, Corbel, Courier New, Cyclopia, DejaVu Sans, DejaVu Sans Display, DejaVu Sans Mono, DejaVu Serif, DejaVu Serif Display, Ebrima |
| LETTER | BOOLEAN | If each letter be generated and output in a batch | False |  |
| AUTOSIZE | BOOLEAN | Scale based on Width & Height | False |  |
| 🌈A | VEC4INT | Color of the letters | [255, 255, 255, 255] |  |
| MATTE | VEC4INT | Background Color | [0, 0, 0, 255] |  |
| COLS | INT | 0 = Auto-Fit, >0 = Fit into N columns | 0 |  |
| SIZE | INT | Text Size | 16 |  |
| ALIGN | STRING | Top, Center or Bottom alignment | CENTER | TOP, CENTER, BOTTOM |
| JUSTIFY | STRING | How to align the text to the side margins of the canvas: Left, Right, or Centered | CENTER | LEFT, CENTER, RIGHT |
| MARGIN | INT | Whitespace padding around canvas | 0 |  |
| SPACING | INT | Line Spacing between Text Lines | 0 |  |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [256, 256] |  |
| 🇽🇾 | VEC2 | Offset the position | [0, 0] |  |
| 📐 | FLOAT | Rotation Angle | 0 |  |
| EDGE | STRING | Clip or Wrap the Canvas Edge | CLIP | CLIP, WRAP, WRAPX, WRAPY |
| 🔳 | BOOLEAN | Invert the mask input | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output. |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha. |
| 😷 | MASK | Single channel mask output. |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project