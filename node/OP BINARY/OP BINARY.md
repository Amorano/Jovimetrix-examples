# OP BINARY (JOV) 🌟

## JOVIMETRIX 🔺🟩🔵/CALC

The Binary Operation node executes binary operations like addition, subtraction, multiplication, division, and bitwise operations on input values, supporting various data types and vector sizes.

![OP BINARY](./OP%20BINARY.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️ | * | input a |  | 
🅱️ | * | input b |  | 
⚒️ | STRING | function | ADD | ADD, SUBTRACT, MULTIPLY, DIVIDE,<br>DIVIDE FLOOR, MODULUS, POWER,<br>MAXIMUM, MINIMUM, DOT PRODUCT,<br>CROSS PRODUCT, BIT AND, BIT<br>NAND, BIT OR, BIT NOR, BIT XOR,<br>BIT XNOR, BIT LSHIFT, BIT<br>RSHIFT, UNION, INTERSECTION,<br>DIFFERENCE
❓ | STRING | type | INT | BOOLEAN, FLOAT, INT, VEC2,<br>VEC2INT, VEC3, VEC3INT, VEC4,<br>VEC4INT
🙃 | BOOLEAN | flip input a and input b with<br>each other | False | 
🇽 | FLOAT | x | 0 | 
🅰️2 | VEC2 | 2-value vector | (0, 0) | 
🅰️3 | VEC3 | 3-value vector | (0, 0, 0) | 
🅰️4 | VEC4 | 4-value vector | (0, 0, 0, 0) | 
🇾 | FLOAT | y | 0 | 
🅱️2 | VEC2 | 2-value vector | (0, 0) | 
🅱️3 | VEC3 | 3-value vector | (0, 0, 0) | 
🅱️4 | VEC4 | 4-value vector | (0, 0, 0, 0) | 

### OUTPUT

name | type | desc
:---:|:---:|---
❔ | * | Unknown 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project