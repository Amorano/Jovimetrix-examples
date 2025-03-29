  
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
| RANGE | VEC3INT | The start, end and step for the range | [0, 0, 1] |  |
| 📝 | STRING | Comma separated list of indicies to export |  |  |
| seed | INT | Random seed value | 0 |  |
| COUNT | INT | How many items to return | 0 |  |
| 🙃 | BOOLEAN | reverse the calculated output list | False |  |
| CHUNK | INT | How many items to put inside each 'batched' output. 0 means put all items in a single batch. | 0 |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🦄 | \* | Output list from selected operation |
| length | INT | Length of output list |
| 🧾 | \* | The elements as a COMFYUI list output |
| full size | INT | Length of all input elements |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project