# [QUEUE (JOV) 🗃](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/QUEUE/QUEUE.md)

## JOVIMETRIX 🔺🟩🔵/UTILITY

Manage a queue of items, such as file paths or data. It supports various formats including images, videos, text files, and JSON files. Users can specify the current index for the queue item, enable pausing the queue, or reset it back to the first index. The node outputs the current item in the queue, the entire queue, the current index, and the total number of items in the queue.

![QUEUE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/QUEUE/QUEUE.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
Q  |  STRING  | Queue | ./res/img/test-a.png | 
VAL  |  INT  | the current index for the current queue<br>item | 0 | 
✋🏽  |  BOOLEAN  | Hold the item at the current queue index | False | 
RESET  |  BOOLEAN  | reset the queue back to index 1 | False | 
BATCH  |  BOOLEAN  | load all items, if they are loadable<br>items, i.e. batch load images from the<br>Queue's list | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🦄  |  *  | Any Type 
Q  |  *  | Queue 
CURRENT  |  *  | Current 
INDEX  |  INT  | Current item index in the Queue list 
TOTAL  |  INT  | Total items in the current Queue List 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project