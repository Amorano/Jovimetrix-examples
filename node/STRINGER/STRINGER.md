[STRINGER (JOV) 🪀](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/STRINGER/STRINGER.md)
--------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/CALC
  
Manipulate strings through filtering  
![STRINGER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STRINGER/STRINGER.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| ⚒️ | STRING | Operation to perform on the input string | SPLIT | SPLIT, JOIN, FIND, REPLACE, SLICE |
| 🔑 | STRING | Delimiter (SPLIT/JOIN) or string to use as search string (FIND/REPLACE). |  |  |
| REPLACE | STRING | String to use as replacement |  |  |
| RANGE | VEC3INT | Start, End and Step. Values will clip to the actual list size(s). | [0, -1, 1] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 📝 | STRING | String Entry |
| count | INT |  |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project