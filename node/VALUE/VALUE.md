  
Supplies raw or default values for various data types, supporting vector input with components for X, Y, Z, and W. It also provides a string input option.  
![VALUE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/VALUE/VALUE.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 🅰️ | \* | Passes a raw value directly, or supplies defaults for any value inputs without connections |  |  |
| ❓ | STRING | Take the input and convert it into the selected type. | BOOLEAN | BOOLEAN, FLOAT, INT, VEC2, VEC2INT, VEC3, VEC3INT, VEC4, VEC4INT, COORD2D, STRING, LIST, DICT |
| 🇽 | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D, COORD3D | X | 0 |  |
| 🇾 | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D, COORD3D | Y | 0 |  |
| 🇿 | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D, COORD3D | Z | 0 |  |
| 🇼 | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D, COORD3D | Width | 0 |  |
| 🅰️🅰️ | VEC4 | default value vector for A | [0, 0, 0, 0] |  |
| seed | INT | Random generator's initial value | 0 |  |
| 🅱️🅱️ | VEC4 | default value vector for B | [1, 1, 1, 1] |  |
| 📝 | STRING | String Entry |  |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project