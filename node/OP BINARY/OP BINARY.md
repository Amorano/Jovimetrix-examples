## [OP BINARY (JOV) 🌟](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/OP%20BINARY/OP%20BINARY.md)

## JOVIMETRIX 🔺🟩🔵/CALC

Execute binary operations like addition, subtraction, multiplication, division, and bitwise operations on input values, supporting various data types and vector sizes.

![OP BINARY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/OP%20BINARY/OP%20BINARY.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️  |  *  | Passes a raw value directly, or supplies<br>defaults for any value inputs without<br>connections |  | 
🅱️  |  *  | Passes a raw value directly, or supplies<br>defaults for any value inputs without<br>connections |  | 
⚒️  |  STRING  | Arithmetic operation to perform | ADD | ADD, SUBTRACT, MULTIPLY, DIVIDE, DIVIDE<br>FLOOR, MODULUS, POWER, MAXIMUM, MINIMUM,<br>DOT PRODUCT, CROSS PRODUCT, BIT AND, BIT<br>NAND, BIT OR, BIT NOR, BIT XOR, BIT XNOR,<br>BIT LSHIFT, BIT RSHIFT, UNION,<br>INTERSECTION, DIFFERENCE
❓  |  STRING  | Output type desired from resultant<br>operation | INT | BOOLEAN, FLOAT, INT, VEC2, VEC2INT, VEC3,<br>VEC3INT, VEC4, VEC4INT, COORD2D
🙃  |  BOOLEAN  | Flip Input A and Input B with each other | False | 
🅰️🅰️  |  VEC4  | value vector | (0, 0, 0, 0) | 
🅱️🅱️  |  VEC4  | value vector | (0, 0, 0, 0) | 

## OUTPUT

name | type | desc
:---:|:---:|---
❔  |  *  | Unknown 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project