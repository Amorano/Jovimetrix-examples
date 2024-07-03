# SWIZZLE (JOV) 😵

## JOVIMETRIX 🔺🟩🔵/CALC

The Swap Node swaps components between two vectors based on specified swizzle patterns and values. It provides flexibility in rearranging vector elements dynamically.

![SWIZZLE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/SWIZZLE/SWIZZLE.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️ | VEC2,VEC3,VEC4,VEC2INT,VEC3INT,VEC4INT,COORD2D | input a |  | 
🅱️ | VEC2,VEC3,VEC4,VEC2INT,VEC3INT,VEC4INT,COORD2D | input b |  | 
❓ | STRING | type | VEC3 | VEC2, VEC2INT, VEC3, VEC3INT,<br>VEC4, VEC4INT, COORD2D
SWAP X | STRING | replace input red channel with<br>target channel or constant | A_X | A X, A Y, A Z, A W, B X, B Y, B<br>Z, B W, CONSTANT
🇽 | FLOAT | x | 0 | 
SWAP Y | STRING | replace input red channel with<br>target channel or constant | A_Y | A X, A Y, A Z, A W, B X, B Y, B<br>Z, B W, CONSTANT
🇾 | FLOAT | y | 0 | 
SWAP Z | STRING | replace input red channel with<br>target channel or constant | A_Z | A X, A Y, A Z, A W, B X, B Y, B<br>Z, B W, CONSTANT
🇿 | FLOAT | z | 0 | 
SWAP W | STRING | replace input w channel with<br>target channel or constant | A_W | A X, A Y, A Z, A W, B X, B Y, B<br>Z, B W, CONSTANT
🇼 | FLOAT | width | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🦄 | VEC2,VEC3,VEC4,VEC2INT,VEC3INT,VEC4INT,COORD2D | Any Type 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project