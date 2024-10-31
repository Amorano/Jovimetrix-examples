[QUEUE TOO (JOV) 🗃](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/QUEUE%20TOO/QUEUE%20TOO.md)
---------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/UTILITY
  
Manage a queue of specific items: media files. Supports various image and video formats. You can specify the current index for the queue item, enable pausing the queue, or reset it back to the first index. The node outputs the current item in the queue, the entire queue, the current index, and the total number of items in the queue.  
![QUEUE TOO](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/QUEUE%20TOO/QUEUE%20TOO.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| Q | STRING | Queue | ./res/img/test-a.png |  |
| RECURSE | BOOLEAN | Search within sub-directories | False |  |
| BATCH | BOOLEAN | Load all items, if they are loadable items, i.e. batch load images from the Queue's list | False |  |
| VAL | INT | The current index for the current queue item | 0 |  |
| ✋🏽 | BOOLEAN | Hold the item at the current queue index | False |  |
| STOP | BOOLEAN | When the Queue is out of items, send a `HALT` to ComfyUI. | False |  |
| 🔄 | BOOLEAN | If the queue should loop around the end when reached. If `False`, at the end of the Queue, if there are more iterations, it will just send the previous image. | True |  |
| RESET | BOOLEAN | Reset the queue back to index 1 | False |  |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT, RESIZE MATTE |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [512, 512] |  |
| 🎞️ | STRING | Select the method for resizing images. Options range from nearest neighbor to advanced methods like Lanczos, ensuring the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
| MATTE | VEC4INT | Define a background color for padding, if necessary. This is useful when images do not fit perfectly into the designated area and need a filler color | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
| current | STRING |  |
| index | INT |  |
| total | INT |  |
| ⚡ | BOOLEAN | Trigger |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project