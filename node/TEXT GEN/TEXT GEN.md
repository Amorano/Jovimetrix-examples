## [TEXT GEN (JOV) 📝](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/TEXT%20GEN/TEXT%20GEN.md)

## JOVIMETRIX 🔺🟩🔵/CREATE

Generates images containing text based on parameters such as font, size, alignment, color, and position. Users can input custom text messages, select fonts from a list of available options, adjust font size, and specify the alignment and justification of the text. Additionally, the node provides options for auto-sizing text to fit within specified dimensions, controlling letter-by-letter rendering, and applying edge effects such as clipping and inversion.

![TEXT GEN](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/TEXT%20GEN/TEXT%20GEN.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
📝  |  STRING  | Your Message |  | 
FONT  |  STRING  | Available System Fonts | Almendra | Almendra, Alphabutt Base A, Alphabutt<br>Letters A, Arial, BIG BREAST FONT,<br>Bahnschrift, Caladea, Calibri, Cambria,<br>Candara, Carlito, Cascadia Code, Cascadia<br>Mono, Comic Sans MS, Consolas, Constantia,<br>Corbel, Courier New, Cyclopia, DejaVu<br>Sans, DejaVu Sans Display, DejaVu Sans<br>Mono, DejaVu Serif, DejaVu Serif Display,<br>Ebrima
LETTER  |  BOOLEAN  | If each letter be generated and output in<br>a batch | False | 
AUTOSIZE  |  BOOLEAN  | Scale based on Width & Height | False | 
🌈A  |  VEC4  | Color of the letters | (255, 255, 255, 255) | 
MATTE  |  VEC3  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0) | 
COLS  |  INT  | 0 = Auto-Fit, >0 = Fit into N columns | 0 | 
SIZE  |  INT  | Text Size | 16 | 
ALIGN  |  STRING  | Top, Center or Bottom alignment | CENTER | TOP, CENTER, BOTTOM
JUSTIFY  |  STRING  | How to align the text to the side margins<br>of the canvas: Left, Right, or Centered | CENTER | LEFT, CENTER, RIGHT
MARGIN  |  INT  | Whitespace padding around canvas | 0 | 
SPACING  |  INT  | Line Spacing between Text Lines | 25 | 
🇼🇭  |  VEC2  | Width and Height as a Vector2 (x,y) | (256, 256) | 
🇽🇾  |  VEC2  | Offset the position | (0, 0) | 
📐  |  FLOAT  | Rotation Angle | 0 | 
EDGE  |  STRING  | Clip or Wrap the Canvas Edge | CLIP | CLIP, WRAP, WRAPX, WRAPY
🔳  |  BOOLEAN  | Invert the mask input | False | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project