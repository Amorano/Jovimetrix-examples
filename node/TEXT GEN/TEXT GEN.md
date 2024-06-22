# TEXT GEN (JOV) 📝

## JOVIMETRIX 🔺🟩🔵/CREATE

The Text Generation node generates images containing text based on user-defined parameters such as font, size, alignment, color, and position. Users can input custom text messages, select fonts from a list of available options, adjust font size, and specify the alignment and justification of the text. Additionally, the node provides options for auto-sizing text to fit within specified dimensions, controlling letter-by-letter rendering, and applying edge effects such as clipping and inversion.

![TEXT GEN](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TEXT%20GEN/TEXT%20GEN.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
📝 | STRING | string entry |  | 
FONT | STRING | available system fonts | Almendra | Almendra, Alphabutt Base A,<br>Alphabutt Letters A, Arial, BIG<br>BREAST FONT, Bahnschrift,<br>Caladea, Calibri, Cambria,<br>Candara, Carlito, Cascadia Code,<br>Cascadia Mono, Comic Sans MS,<br>Consolas, Constantia, Corbel,<br>Courier New, Cyclopia, DejaVu<br>Sans, DejaVu Sans Display,<br>DejaVu Sans Mono, DejaVu Serif,<br>DejaVu Serif Display, Ebrima
LETTER | BOOLEAN | if each letter be generated and<br>output in a batch | False | 
AUTOSIZE | BOOLEAN | scale based on width & height | False | 
🌈A | VEC4 | rgb with alpha color | (255, 255, 255, 255) | 
MATTE | VEC3 | define a background color for<br>padding, if necessary. this is<br>useful when images do not fit<br>perfectly into the designated<br>area and need a filler color | (0, 0, 0) | 
COLS | INT | 0 = auto-fit, >0 = fit into n<br>columns | 0 | 
SIZE | INT | text size | 16 | 
ALIGN | STRING | top, center or bottom alignment | CENTER | TOP, CENTER, BOTTOM
JUSTIFY | STRING | how to align the text to the<br>side margins of the canvas:<br>left, right, or centered | CENTER | LEFT, CENTER, RIGHT
MARGIN | INT | whitespace padding around canvas | 0 | 
SPACING | INT | line spacing between text lines | 25 | 
🇼🇭 | VEC2 | set the target dimensions for<br>the output image if scaling is<br>applied | (256, 256) | 
🇽🇾 | VEC2 | x and y | (0, 0) | 
📐 | FLOAT | rotation angle | 0 | 
EDGE | STRING | clip or wrap the canvas edge | CLIP | CLIP, WRAP, WRAPX, WRAPY
🔳 | BOOLEAN | color inversion | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project