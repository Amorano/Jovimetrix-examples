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
❓ | STRING | type | BOOLEAN | BOOLEAN, FLOAT, INT, VEC2,<br>VEC2INT, VEC3, VEC3INT, VEC4,<br>VEC4INT, COORD2D, STRING, LIST,<br>DICT
🇽 | * | x | 0 | 
🇾 | * | y | 0 | 
🇿 | * | z | 0 | 
🇼 | * | width | 0 | 
🅰️🅰️ | VEC4 | default value vector for a | (0, 0, 0, 0) | 
seed | INT | random generator's initial value | 0 | 
🅱️🅱️ | VEC4 | default value vector for b | (1, 1, 1, 1) | 
📝 | STRING | string entry |  | 

### OUTPUT

name | type | desc
:---:|:---:|---
🦄 | BOOLEAN,FLOAT,INT,VEC2,VEC3,VEC4,VEC2INT,VEC3INT,VEC4INT,COORD2D | Any Type 
🇽 | BOOLEAN,FLOAT,INT,VEC2,VEC3,VEC4,VEC2INT,VEC3INT,VEC4INT,COORD2D | X 
🇾 | BOOLEAN,FLOAT,INT,VEC2,VEC3,VEC4,VEC2INT,VEC3INT,VEC4INT,COORD2D | Y 
🇿 | BOOLEAN,FLOAT,INT,VEC2,VEC3,VEC4,VEC2INT,VEC3INT,VEC4INT,COORD2D | Z 
🇼 | BOOLEAN,FLOAT,INT,VEC2,VEC3,VEC4,VEC2INT,VEC3INT,VEC4INT,COORD2D | Width 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project