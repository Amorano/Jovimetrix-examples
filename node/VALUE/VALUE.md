# [VALUE (JOV) 🧬](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/VALUE/VALUE.md)

## JOVIMETRIX 🔺🟩🔵/CALC

Supplies raw or default values for various data types, supporting vector input with components for X, Y, Z, and W. It also provides a string input option.

![VALUE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/VALUE/VALUE.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️  |  *  | Passes a raw value directly, or supplies<br>defaults for any value inputs without<br>connections |  | 
❓  |  STRING  | Take the input and convert it into the<br>selected type. | BOOLEAN | BOOLEAN, FLOAT, INT, VEC2, VEC2INT, VEC3,<br>VEC3INT, VEC4, VEC4INT, COORD2D, STRING,<br>LIST, DICT
🇽  |  *  | X | 0 | 
🇾  |  *  | Y | 0 | 
🇿  |  *  | Z | 0 | 
🇼  |  *  | Width | 0 | 
🅰️🅰️  |  VEC4  | default value vector for A | (0, 0, 0, 0) | 
seed  |  INT  | Random generator's initial value | 0 | 
🅱️🅱️  |  VEC4  | default value vector for B | (1, 1, 1, 1) | 
📝  |  STRING  | String Entry |  | 

### OUTPUT

name | type | desc
:---:|:---:|---
🦄  |  *  | Any Type 
🇽  |  *  | X 
🇾  |  *  | Y 
🇿  |  *  | Z 
🇼  |  *  | Width 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project