## [QUEUE (JOV) 🗃](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/QUEUE/QUEUE.md)

## JOVIMETRIX 🔺🟩🔵/UTILITY


Manage a queue of items, such as file paths or data. Supports various formats including images, videos, text files, and JSON files. You can specify the current index for the queue item, enable pausing the queue, or reset it back to the first index. The node outputs the current item in the queue, the entire queue, the current index, and the total number of items in the queue.


![QUEUE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/QUEUE/QUEUE.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
Q  |  STRING  | Queue | ./res/img/test-a.png | 
RECURSE  |  BOOLEAN  | Search within sub-directories | False | 
BATCH  |  BOOLEAN  | Load all items, if they are loadable<br>items, i.e. batch load images from the<br>Queue's list. This can consume a lot of<br>memory depending on the list size and each<br>item size. | False | 
VAL  |  INT  | The current index for the current queue<br>item | 0 | 
✋🏽  |  BOOLEAN  | Hold the item at the current queue index | False | 
STOP  |  BOOLEAN  | When the Queue is out of items, send a<br>`HALT` to ComfyUI. | False | 
🔄  |  BOOLEAN  | If the queue should loop around the end<br>when reached. If `False`, at the end of<br>the Queue, if there are more iterations,<br>it will just send the previous image. | True | 
RESET  |  BOOLEAN  | Reset the queue back to index 1 | False | 

## OUTPUT

name | type | desc
:---:|:---:|---
🦄  |  *  | Any Type 
q  |  *  |  
current  |  STRING  |  
index  |  INT  |  
total  |  INT  |  
⚡  |  BOOLEAN  | Trigger 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project