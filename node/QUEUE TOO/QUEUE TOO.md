## [QUEUE TOO (JOV) 🗃](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/QUEUE%20TOO/QUEUE%20TOO.md)

## JOVIMETRIX 🔺🟩🔵/UTILITY


Manage a queue of specific items: media files. Supports various image and video formats. You can specify the current index for the queue item, enable pausing the queue, or reset it back to the first index. The node outputs the current item in the queue, the entire queue, the current index, and the total number of items in the queue.


![QUEUE TOO](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/QUEUE%20TOO/QUEUE%20TOO.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
Q  |  STRING  | Queue | ./res/img/test-a.png | 
VAL  |  INT  | The current index for the current queue<br>item | 0 | 
✋🏽  |  BOOLEAN  | Hold the item at the current queue index | False | 
RESET  |  BOOLEAN  | Reset the queue back to index 1 | False | 
BATCH  |  BOOLEAN  | Load all items, if they are loadable<br>items, i.e. batch load images from the<br>Queue's list | False | 
RECURSE  |  BOOLEAN  | Search within sub-directories | False | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT
🇼🇭  |  VEC2INT  | Width and Height as a Vector2 (x,y) | [512, 512] | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4INT  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | [0, 0, 0, 255] | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 
current  |  *  |  
index  |  INT  |  
total  |  INT  |  

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project