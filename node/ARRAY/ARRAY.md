[ARRAY (JOV) 📚](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/ARRAY/ARRAY.md)
-----------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/UTILITY
  
Processes a batch of data based on the selected mode, such as merging, picking, slicing, random selection, or indexing. Allows for flipping the order of processed items and dividing the data into chunks.  
![ARRAY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/ARRAY/ARRAY.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| MODE | STRING | Select a single index, specific range, custom index list or randomized | MERGE | MERGE, PICK, SLICE, INDEX LIST, RANDOM, CARTESIAN |
| INDEX | INT | Selected list position | 0 |  |
| RANGE | VEC3INT | start index, ending index (0 means full length) and how many items to skip per step | [0, 0, 1] |  |
| 📝 | STRING | Comma separated list of indicies to export |  |  |
| seed | INT | Random generator's initial value | 0 |  |
| COUNT | INT | How many items to return | 0 |  |
| 🙃 | BOOLEAN | invert the calculated output list | False |  |
| CHUNK | INT | How many items to put per output. Default (0) is all items | 0 |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🦄 | \* | Any Type |
| length | INT |  |
| 🧾 | \* | List |
| full size | INT |  |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project