# VALUE (JOV) 🧬

## JOVIMETRIX 🔺🟩🔵/CALC

The Value Node supplies raw or default values for various data types, supporting vector input with components for X, Y, Z, and W. It also provides a string input option.

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
🦄  |  BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D  | Any Type 
🇽  |  BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D  | X 
🇾  |  BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D  | Y 
🇿  |  BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D  | Z 
🇼  |  BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D  | Width 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project