  
Manage a queue of specific items: media files. Supports various image and video formats. You can specify the current index for the queue item, enable pausing the queue, or reset it back to the first index. The node outputs the current item in the queue, the entire queue, the current index, and the total number of items in the queue.  
![QUEUE TOO](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/QUEUE%20TOO/QUEUE%20TOO.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| Q | STRING | Current items to process during Queue iteration. | ./res/img/test-a.png |  |
| RECURSE | BOOLEAN | Search within sub-directories | False |  |
| BATCH | BOOLEAN | Load all items, if they are loadable items, i.e. batch load images from the Queue's list | False |  |
| VAL | INT | Current index for the current queue item | 0 |  |
| ✋🏽 | BOOLEAN | Hold the item at the current queue index | False |  |
| STOP | BOOLEAN | When the Queue is out of items, send a `HALT` to ComfyUI. | False |  |
| 🔄 | BOOLEAN | If the queue should loop. If `False` and there are more iterations, will send the previous image. | True |  |
| RESET | BOOLEAN | Reset the queue back to index 1 | False |  |
| MODE | STRING | Decide whether the images should be resized to fit | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT, RESIZE MATTE |
| 🇼🇭 | VEC2INT | Width and Height | [512, 512] |  |
| 🎞️ | STRING | Method for resizing images. | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
| MATTE | VEC4INT | Background color for padding | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha |
| 😷 | MASK | Single channel mask output |
| current | STRING | Current item selected from the Queue list as a string |
| index | INT | Current index for the selected item in the Queue list |
| total | INT | Total items in the current Queue List |
| ⚡ | BOOLEAN | Send a True signal when the queue end index is reached |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project