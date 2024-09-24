[SWIZZLE (JOV) 😵](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/SWIZZLE/SWIZZLE.md)
-----------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/CALC
  
Swap components between two vectors based on specified swizzle patterns and values. It provides flexibility in rearranging vector elements dynamically.  
![SWIZZLE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/SWIZZLE/SWIZZLE.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 🅰️ | \* | Input A |  |  |
| 🅱️ | \* | Input B |  |  |
| ❓ | STRING | Output type desired from resultant operation | VEC3 | VEC2, VEC2INT, VEC3, VEC3INT, VEC4, VEC4INT, COORD2D |
| SWAP X | STRING | Replace input Red channel with target channel or constant | A\_X | A X, A Y, A Z, A W, B X, B Y, B Z, B W, CONSTANT |
| SWAP Y | STRING | Replace input Red channel with target channel or constant | A\_Y | A X, A Y, A Z, A W, B X, B Y, B Z, B W, CONSTANT |
| SWAP Z | STRING | Replace input Red channel with target channel or constant | A\_Z | A X, A Y, A Z, A W, B X, B Y, B Z, B W, CONSTANT |
| SWAP W | STRING | Replace input W channel with target channel or constant | A\_W | A X, A Y, A Z, A W, B X, B Y, B Z, B W, CONSTANT |
| VECTOR | VEC4 | Compound value of type float, vec2, vec3 or vec4 | [0, 0, 0, 0] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🦄 | \* | Any Type |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project