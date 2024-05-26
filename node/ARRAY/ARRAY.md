# ARRAY (JOV) 📚

## JOVIMETRIX 🔺🟩🔵/UTILITY



#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
MODE|COMBO[STRING]|scaling mode|MERGE|MERGE, PICK, SLICE, INDEX_LIST, RANDOM
INDEX|INT|current item index in the queue list|0|
RANGE|VEC3|start index, ending index (0 means full<br>length) and how many items to skip per<br>step|(0, 0, 1)|
📝|STRING|string entry||
SEED|INT|seed|0|
🙃|BOOLEAN|flip input a and input b with each other|False|
CHUNK|INT|how many items to put per output.<br>default (0) is all items|0|

### OUTPUT

name|type|desc
:---:|:---:|---
#️⃣|Value|INT
🔮|Any Type|*
🧾|List|*

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project