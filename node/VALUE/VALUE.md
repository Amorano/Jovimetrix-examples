# VALUE (JOV) 🧬

## JOVIMETRIX 🔺🟩🔵/CALC

The Value Node supplies raw or default values for various data types, supporting vector input with components for X, Y, Z, and W. It also provides a string input option.

![VALUE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/VALUE/VALUE.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️ | * | input a |  | 
❓ | STRING | type | BOOLEAN | BOOLEAN, FLOAT, INT, VEC2,<br>VEC2INT, VEC3, VEC3INT, VEC4,<br>VEC4INT, STRING, LIST, DICT,<br>COORD2D
🇽 | * | x | 0 | 
🇾 | * | y | 0 | 
🇿 | * | z | 0 | 
🇼 | * | width | 0 | 
🅰️🅰️ | VEC4 | default value vector for a | (0, 0, 0, 0) | 
seed | INT | random generator's initial value | 0 | 
🅱️🅱️ | VEC4 | default value vector for b | (0, 0, 0, 0) | 
📝 | STRING | string entry |  | 

### OUTPUT

name | type | desc
:---:|:---:|---
🦄 | * | Any Type 
🇽 | * | X 
🇾 | * | Y 
🇿 | * | Z 
🇼 | * | Width 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project