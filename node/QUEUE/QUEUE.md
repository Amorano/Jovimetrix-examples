  
Manage a queue of items, such as file paths or data. Supports various formats including images, videos, text files, and JSON files. You can specify the current index for the queue item, enable pausing the queue, or reset it back to the first index. The node outputs the current item in the queue, the entire queue, the current index, and the total number of items in the queue.  
![QUEUE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/QUEUE/QUEUE.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| Q | STRING | Current items to process during Queue iteration. | ./res/img/test-a.png |  |
| RECURSE | BOOLEAN | Recurse through all subdirectories found | False |  |
| BATCH | BOOLEAN | Load all items, if they are loadable items, i.e. batch load images from the Queue's list. | False |  |
| VAL | INT | The current index for the current queue item | 0 |  |
| ✋🏽 | BOOLEAN | Hold the item at the current queue index | False |  |
| STOP | BOOLEAN | When the Queue is out of items, send a `HALT` to ComfyUI. | False |  |
| 🔄 | BOOLEAN | If the queue should loop. If `False` and if there are more iterations, will send the previous image. | True |  |
| RESET | BOOLEAN | Reset the queue back to index 1 | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🦄 | \* | Current item selected from the Queue list |
| q | \* | The entire Queue list |
| current | STRING | Current item selected from the Queue list as a string |
| index | INT | Current index for the selected item in the Queue list |
| total | INT | Total items in the current Queue List |
| ⚡ | BOOLEAN | Send a True signal when the queue end index is reached |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project