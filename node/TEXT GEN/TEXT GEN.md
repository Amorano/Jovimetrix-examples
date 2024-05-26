# TEXT GEN (JOV) 📝

## JOVIMETRIX 🔺🟩🔵/CREATE

The Text Generation node generates images containing text based on user-defined parameters such as font, size, alignment, color, and position. Users can input custom text messages, select fonts from a list of available options, adjust font size, and specify the alignment and justification of the text. Additionally, the node provides options for auto-sizing text to fit within specified dimensions, controlling letter-by-letter rendering, and applying edge effects such as clipping and inversion.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
📝|STRING|string entry||
FONT|COMBO[STRING]|available system fonts|Almendra|Almendra, Arial, Bahnschrift, Caladea,<br>Calibri, Cambria, Candara, Carlito, Cascadia<br>Code, Cascadia Mono, Comic Sans MS, Consolas,<br>Constantia, Corbel, Courier New, DejaVu Sans,<br>DejaVu Sans Display, DejaVu Sans Mono, DejaVu<br>Serif, DejaVu Serif Display, Ebrima, Franklin<br>Gothic Medium, Gabriola, Gadugi, Gentium<br>Basic, Gentium Book Basic, Georgia, HoloLens<br>MDL2 Assets, Impact, Ink Free, IntelOne Mono,<br>Javanese Text, JetBrains Mono, JetBrains Mono<br>NL, Leelawadee UI, Lora, Lucida Console,<br>Lucida Sans Unicode, MS Gothic, MV Boli,<br>Malgun Gothic, Microsoft Himalaya, Microsoft<br>JhengHei, Microsoft New Tai Lue, Microsoft<br>PhagsPa, Microsoft Sans Serif, Microsoft Tai<br>Le, Microsoft YaHei, Microsoft Yi Baiti,<br>MingLiU-ExtB, Mongolian Baiti, Montserrat,<br>Myanmar Text, Nirmala UI, OpenSymbol,<br>Palatino Linotype, Raleway, STIXGeneral,<br>STIXNonUnicode, STIXSizeFiveSym,<br>STIXSizeFourSym, STIXSizeOneSym,<br>STIXSizeThreeSym, STIXSizeTwoSym, Segoe MDL2<br>Assets, Segoe Print, Segoe Script, Segoe UI,<br>Segoe UI Emoji, Segoe UI Historic, Segoe UI<br>Symbol, SimSun, SimSun-ExtB, Sitka Small,<br>Sylfaen, Symbol, Tahoma, Times New Roman,<br>Trebuchet MS, Verdana, Webdings, Wingdings,<br>Yu Gothic, cmb10, cmex10, cmmi10, cmr10,<br>cmss10, cmsy10, cmtt10
LETTER|BOOLEAN|if each letter be generated and<br>output in a batch|False|
AUTOSIZE|BOOLEAN|scale based on width & height|False|
🌈A|VEC3|rgb with alpha color|(255, 255, 255, 255)|
MATTE|VEC3|background color|(0, 0, 0)|
COLS|INT|0 = auto-fit, >0 = fit into n<br>columns|0|
SIZE|INT|text size|16|
ALIGN|COMBO[STRING]|top, center or bottom alignment|CENTER|TOP, CENTER, BOTTOM
JUSTIFY|COMBO[STRING]|how to align the text to the side<br>margins of the canvas: left, right,<br>or centered|CENTER|LEFT, CENTER, RIGHT
MARGIN|INT|whitespace padding around canvas|0|
SPACING|INT|line spacing between text lines|25|
🇼🇭|VEC2|width and height|(32, 32)|
🇽🇾|VEC2|x and y|(0, 0)|
📐|FLOAT|rotation angle|0|
EDGE|COMBO[STRING]|clip or wrap the canvas edge|CLIP|CLIP, WRAP, WRAPX, WRAPY
🔳|BOOLEAN|color inversion|False|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|IMAGE|Image
🌈|IMAGE|RGB (no alpha) Color
😷|MASK|Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project