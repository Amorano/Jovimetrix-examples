# TEXT GEN (JOV) 📝

## JOVIMETRIX 🔺🟩🔵/CREATE

The Text Generation node generates images containing text based on user-defined parameters such as font, size, alignment, color, and position. Users can input custom text messages, select fonts from a list of available options, adjust font size, and specify the alignment and justification of the text. Additionally, the node provides options for auto-sizing text to fit within specified dimensions, controlling letter-by-letter rendering, and applying edge effects such as clipping and inversion.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
📝|STRING|string entry||
FONT|COMBO[STRING]|available system fonts|Almendra|Almendra, Arial, Bahnschrift, Caladea, Calibri, Cambria,<br>Candara, Carlito, Cascadia Code, Cascadia Mono, Comic Sans<br>MS, Consolas, Constantia, Corbel, Courier New, DejaVu Sans,<br>DejaVu Sans Display, DejaVu Sans Mono, DejaVu Serif, DejaVu<br>Serif Display, Ebrima, Franklin Gothic Medium, Gabriola,<br>Gadugi, Gentium Basic, Gentium Book Basic, Georgia, HoloLens<br>MDL2 Assets, Impact, Ink Free, IntelOne Mono, Javanese Text,<br>JetBrains Mono, JetBrains Mono NL, Leelawadee UI, Lora,<br>Lucida Console, Lucida Sans Unicode, MS Gothic, MV Boli,<br>Malgun Gothic, Microsoft Himalaya, Microsoft JhengHei,<br>Microsoft New Tai Lue, Microsoft PhagsPa, Microsoft Sans<br>Serif, Microsoft Tai Le, Microsoft YaHei, Microsoft Yi<br>Baiti, MingLiU-ExtB, Mongolian Baiti, Montserrat, Myanmar<br>Text, Nirmala UI, OpenSymbol, Palatino Linotype, Raleway,<br>STIXGeneral, STIXNonUnicode, STIXSizeFiveSym,<br>STIXSizeFourSym, STIXSizeOneSym, STIXSizeThreeSym,<br>STIXSizeTwoSym, Segoe MDL2 Assets, Segoe Print, Segoe<br>Script, Segoe UI, Segoe UI Emoji, Segoe UI Historic, Segoe<br>UI Symbol, SimSun, SimSun-ExtB, Sitka Small, Sylfaen,<br>Symbol, Tahoma, Times New Roman, Trebuchet MS, Verdana,<br>Webdings, Wingdings, Yu Gothic, cmb10, cmex10, cmmi10,<br>cmr10, cmss10, cmsy10, cmtt10
LETTER|BOOLEAN|if each letter be generated and output<br>in a batch|False|
AUTOSIZE|BOOLEAN|scale based on width & height|False|
🌈A|VEC3|rgb with alpha color|(255, 255, 255, 255)|
MATTE|VEC3|background color|(0, 0, 0)|
COLS|INT|0 = auto-fit, >0 = fit into n columns|0|
SIZE|INT|text size|16|
ALIGN|COMBO[STRING]|top, center or bottom alignment|CENTER|TOP, CENTER, BOTTOM
JUSTIFY|COMBO[STRING]|how to align the text to the side<br>margins of the canvas: left, right, or<br>centered|CENTER|LEFT, CENTER, RIGHT
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
🖼️|Image|IMAGE
🌈|RGB (no alpha) Color|IMAGE
😷|Mask or Image to use as Mask to control<br>where adjustments are applied|MASK

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project