## [SWIZZLE (JOV) 😵](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/SWIZZLE/SWIZZLE.md)

## JOVIMETRIX 🔺🟩🔵/CALC


Swap components between two vectors based on specified swizzle patterns and values. It provides flexibility in rearranging vector elements dynamically.


![SWIZZLE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/SWIZZLE/SWIZZLE.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️  |  *  | Input A |  | 
🅱️  |  *  | Input B |  | 
❓  |  STRING  | Output type desired from resultant<br>operation | VEC3 | VEC2, VEC2INT, VEC3, VEC3INT, VEC4,<br>VEC4INT, COORD2D
SWAP X  |  STRING  | Replace input Red channel with target<br>channel or constant | A_X | A X, A Y, A Z, A W, B X, B Y, B Z, B W,<br>CONSTANT
🇽  |  FLOAT  | X | 0 | 
SWAP Y  |  STRING  | Replace input Red channel with target<br>channel or constant | A_Y | A X, A Y, A Z, A W, B X, B Y, B Z, B W,<br>CONSTANT
🇾  |  FLOAT  | Y | 0 | 
SWAP Z  |  STRING  | Replace input Red channel with target<br>channel or constant | A_Z | A X, A Y, A Z, A W, B X, B Y, B Z, B W,<br>CONSTANT
🇿  |  FLOAT  | Z | 0 | 
SWAP W  |  STRING  | Replace input W channel with target<br>channel or constant | A_W | A X, A Y, A Z, A W, B X, B Y, B Z, B W,<br>CONSTANT
🇼  |  FLOAT  | Width | 0 | 

## OUTPUT

name | type | desc
:---:|:---:|---
🦄  |  *  | Any Type 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project