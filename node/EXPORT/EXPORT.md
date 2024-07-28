# [EXPORT (JOV) 📽](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/EXPORT/EXPORT.md)

## JOVIMETRIX 🔺🟩🔵/UTILITY

Responsible for saving images or animations to disk. It supports various output formats such as GIF and GIFSKI. Users can specify the output directory, filename prefix, image quality, frame rate, and other parameters. Additionally, it allows overwriting existing files or generating unique filenames to avoid conflicts. The node outputs the saved images or animation as a tensor.

![EXPORT](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/EXPORT/EXPORT.png)

#### OUTPUT NODE?: `True`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
📤  |  STRING  | Pass Out | <comfy output dir> | 
FORMAT  |  STRING  | Format | gifski | gifski, gif, png, jpg
PREFIX  |  STRING  | Prefix | jovi | 
OVERWRITE  |  BOOLEAN  | Overwrite | False | 
OPT  |  BOOLEAN  | Optimize | False | 
QUALITY  |  INT  | Quality | 90 | 
MOTION  |  INT  | Motion Quality | 100 | 
🏎️  |  INT  | Frames per second | 24 | 
🔄  |  INT  | Loop | 0 | 

### OUTPUT

NONE

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project