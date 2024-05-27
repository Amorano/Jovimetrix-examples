# EXPORT (JOV) 📽

## JOVIMETRIX 🔺🟩🔵/UTILITY

The Export node is responsible for saving images or animations to disk. It supports various output formats such as GIF and GIFSKI. Users can specify the output directory, filename prefix, image quality, frame rate, and other parameters. Additionally, it allows overwriting existing files or generating unique filenames to avoid conflicts. The node outputs the saved images or animation as a tensor.

#### OUTPUT NODE?: `True`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
📤 | STRING | pass out | C:\dev\ComfyUI\ComfyUI\output | 
FORMAT | STRING | format | gifski | gifski, gif, png, jpg
PREFIX | STRING | prefix | jovi | 
OVERWRITE | BOOLEAN | overwrite | False | 
OPT | BOOLEAN | optimize | False | 
QUALITY | INT | quality | 90 | 
MOTION | INT | motion quality | 100 | 
🏎️ | INT | frames per second | 20 | 
🔄 | INT | loop | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project