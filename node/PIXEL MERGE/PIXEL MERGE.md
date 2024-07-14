# PIXEL MERGE (JOV) 🫂

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Combines individual color channels (red, green, blue) along with an optional mask channel to create a composite image. This node is useful for merging separate color components into a single image for visualization or further processing.

![PIXEL MERGE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/PIXEL%20MERGE/PIXEL%20MERGE.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🟥  |  *  | Red |  | 
🟩  |  *  | Green |  | 
🟦  |  *  | Blue |  | 
⬜  |  *  | Alpha |  | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🇼🇭  |  VEC2  | Set the target dimensions for the output<br>image if scaling is applied | (512, 512) | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 
🙃  |  VEC4  | Invert specific input prior to merging. R,<br>G, B, A. | (0, 0, 0, 0) | 
🔳  |  BOOLEAN  | Invert the final merged output | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project