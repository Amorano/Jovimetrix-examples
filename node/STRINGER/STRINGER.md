## [STRINGER (JOV) 🪀](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/STRINGER/STRINGER.md)

## JOVIMETRIX 🔺🟩🔵/CALC


Manipulate strings through filtering


![STRINGER](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/STRINGER/STRINGER.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
⚒️  |  STRING  | Operation to perform on the input string | SPLIT | SPLIT, JOIN, FIND, REPLACE, SLICE
🔑  |  STRING  | Delimiter (SPLIT/JOIN) or string to use as<br>search string (FIND/REPLACE). |  | 
REPLACE  |  STRING  | String to use as replacement |  | 
RANGE  |  VEC3INT  | Start, End and Step. Values will clip to<br>the actual list size(s). | [0, -1, 1] | 

## OUTPUT

name | type | desc
:---:|:---:|---
📝  |  STRING  | String Entry 
count  |  INT  |  

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project