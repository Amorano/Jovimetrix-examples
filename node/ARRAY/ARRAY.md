# ARRAY (JOV) 📚

## JOVIMETRIX 🔺🟩🔵/UTILITY

Processes a batch of data based on the selected mode, such as merging, picking, slicing, random selection, or indexing. Allows for flipping the order of processed items and dividing the data into chunks.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
MODE| COMBO[STRING] | scaling mode | MERGE | MERGE, PICK, SLICE, INDEX_LIST, RANDOM
INDEX| INT | current item index in the queue<br>list | 0 | 
RANGE| VEC3 | start index, ending index (0 means<br>full length) and how many items to<br>skip per step | (0, 0, 1) | 
📝| STRING | string entry |  | 
SEED| INT | seed | 0 | 
🙃| BOOLEAN | flip input a and input b with each<br>other | False | 
CHUNK| INT | how many items to put per output.<br>default (0) is all items | 0 | 

### OUTPUT

name|type|desc
:---:|:---:|---
VALUE| INT | Value 
🔮| * | Any Type 
🧾| * | List 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project