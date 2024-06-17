# ARRAY (JOV) 📚

## JOVIMETRIX 🔺🟩🔵/UTILITY

Processes a batch of data based on the selected mode, such as merging, picking, slicing, random selection, or indexing. Allows for flipping the order of processed items and dividing the data into chunks.

![ARRAY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/ARRAY/ARRAY.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
MODE | STRING | decide whether the images should<br>be resized to fit a specific<br>dimension. available modes<br>include scaling to fit within<br>given dimensions or keeping the<br>original size | MERGE | MERGE, PICK, SLICE, INDEX LIST,<br>RANDOM, CARTESIAN
INDEX | INT | current item index in the queue<br>list | 0 | 
RANGE | VEC3 | start index, ending index (0<br>means full length) and how many<br>items to skip per step | (0, 0, 1) | 
📝 | STRING | string entry |  | 
seed | INT | random generator's initial value | 0 | 
🙃 | BOOLEAN | flip input a and input b with<br>each other | False | 
CHUNK | INT | how many items to put per<br>output. default (0) is all items | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
VAL | INT | Value 
🦄 | * | Any Type 
🧾 | * | List 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project