# SWAP (JOV) 😵

## JOVIMETRIX 🔺🟩🔵/CALC

The Swap Node swaps components between two vectors based on specified swizzle patterns and values. It provides flexibility in rearranging vector elements dynamically.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
🅰️| * | input a |  | 
🅱️| * | input b |  | 
SWAP X| COMBO[STRING] | replace input red channel with<br>target channel or constant | A_X | A_X, A_Y, A_Z, A_W, B_X, B_Y, B_Z, B_W,<br>CONSTANT
🇽| FLOAT | x | 0 | 
SWAP Y| COMBO[STRING] | replace input red channel with<br>target channel or constant | A_Y | A_X, A_Y, A_Z, A_W, B_X, B_Y, B_Z, B_W,<br>CONSTANT
🇾| FLOAT | y | 0 | 
SWAP Z| COMBO[STRING] | replace input red channel with<br>target channel or constant | A_Z | A_X, A_Y, A_Z, A_W, B_X, B_Y, B_Z, B_W,<br>CONSTANT
🇿| FLOAT | z | 0 | 
SWAP W| COMBO[STRING] | replace input w channel with target<br>channel or constant | A_W | A_X, A_Y, A_Z, A_W, B_X, B_Y, B_Z, B_W,<br>CONSTANT
🇼| FLOAT | width | 0 | 

### OUTPUT

name|type|desc
:---:|:---:|---
🔮| * | Any Type 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project