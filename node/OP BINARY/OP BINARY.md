  
Execute binary operations like addition, subtraction, multiplication, division, and bitwise operations on input values, supporting various data types and vector sizes.  
![OP BINARY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/OP%20BINARY/OP%20BINARY.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 🅰️ | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D, COORD3D | Passes a raw value directly, or supplies defaults for any value inputs without connections |  |  |
| 🅱️ | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D, COORD3D | Passes a raw value directly, or supplies defaults for any value inputs without connections |  |  |
| ⚒️ | STRING | Arithmetic operation to perform | ADD | ADD, SUBTRACT, MULTIPLY, DIVIDE, DIVIDE FLOOR, MODULUS, POWER, MAXIMUM, MINIMUM, DOT PRODUCT, CROSS PRODUCT, BIT AND, BIT NAND, BIT OR, BIT NOR, BIT XOR, BIT XNOR, BIT LSHIFT, BIT RSHIFT, UNION, INTERSECTION, DIFFERENCE, BASE |
| ❓ | STRING | Output type desired from resultant operation | INT | BOOLEAN, FLOAT, INT, VEC2, VEC2INT, VEC3, VEC3INT, VEC4, VEC4INT, COORD2D |
| 🙃 | BOOLEAN | Flip Input A and Input B with each other | False |  |
| 🅰️🅰️ | VEC4 | value vector | [0, 0, 0, 0] |  |
| 🅱️🅱️ | VEC4 | value vector | [0, 0, 0, 0] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| ❔ | \* | O |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project