# QUEUE (JOV) 🗃

## JOVIMETRIX 🔺🟩🔵/UTILITY

The Queue node manages a queue of items, such as file paths or data. It supports various formats including images, videos, text files, and JSON files. Users can specify the current index for the queue item, enable pausing the queue, or reset it back to the first index. The node outputs the current item in the queue, the entire queue, the current index, and the total number of items in the queue.

![QUEUE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/QUEUE/QUEUE.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
Q | STRING | queue | ./res/img/test-a.png | 
VAL | INT | value | 0 | 
✋🏽 | BOOLEAN | wait | False | 
RESET | BOOLEAN | reset | False | 
BATCH | BOOLEAN | output as a batch (all images in<br>a single tensor) or as a list of<br>images (each image processed<br>separately) | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🦄 | * | Any Type 
Q | * | Queue 
CURRENT | * | Current 
INDEX | INT | Current item index in the Queue list 
TOTAL | INT | Total items in the current Queue List 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project