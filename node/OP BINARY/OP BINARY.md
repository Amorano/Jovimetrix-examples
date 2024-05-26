# OP BINARY (JOV) 🌟

## JOVIMETRIX 🔺🟩🔵/CALC

The Binary Operation node executes binary operations like addition, subtraction, multiplication, division, and bitwise operations on input values, supporting various data types and vector sizes.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
🅰️|*|input a||
🅱️|*|input b||
⚒️|COMBO[STRING]|function|ADD|ADD, SUBTRACT, MULTIPLY, DIVIDE, DIVIDE_FLOOR, MODULUS,<br>POWER, MAXIMUM, MINIMUM, DOT_PRODUCT, CROSS_PRODUCT,<br>BIT_AND, BIT_NAND, BIT_OR, BIT_NOR, BIT_XOR, BIT_XNOR,<br>BIT_LSHIFT, BIT_RSHIFT, UNION, INTERSECTION, DIFFERENCE
❓|COMBO[STRING]|type|INT|BOOLEAN, FLOAT, INT, VEC2, VEC2INT, VEC3, VEC3INT, VEC4,<br>VEC4INT
🙃|BOOLEAN|flip input a and input b with each other|False|
🇽|FLOAT|x|0|
🅰️2|VEC2|2-value vector|(0, 0)|
🅰️3|VEC3|3-value vector|(0, 0, 0)|
🅰️4|VEC4|4-value vector|(0, 0, 0, 0)|
🇾|FLOAT|y|0|
🅱️2|VEC2|2-value vector|(0, 0)|
🅱️3|VEC3|3-value vector|(0, 0, 0)|
🅱️4|VEC4|4-value vector|(0, 0, 0, 0)|

### OUTPUT

name|type|desc
:---:|:---:|---
❔|Unknown|*

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project