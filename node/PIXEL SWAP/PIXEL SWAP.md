## [PIXEL SWAP (JOV) 🔃](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/PIXEL%20SWAP/PIXEL%20SWAP.md)

## JOVIMETRIX 🔺🟩🔵/COMPOSE


Swap pixel values between two input images based on specified channel swizzle operations. Options include pixel inputs, swap operations for red, green, blue, and alpha channels, and constant values for each channel. The swap operations allow for flexible pixel manipulation by determining the source of each channel in the output image, whether it be from the first image, the second image, or a constant value.


![PIXEL SWAP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/PIXEL%20SWAP/PIXEL%20SWAP.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
👾B  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
SWAP R  |  STRING  | Replace input Red channel with target<br>channel or constant | RED_A | RED A, GREEN A, BLUE A, ALPHA A, RED B,<br>GREEN B, BLUE B, ALPHA B, CONSTANT
🟥  |  INT  | Red | 0 | 
SWAP G  |  STRING  | Replace input Green channel with target<br>channel or constant | GREEN_A | RED A, GREEN A, BLUE A, ALPHA A, RED B,<br>GREEN B, BLUE B, ALPHA B, CONSTANT
🟩  |  INT  | Green | 0 | 
SWAP B  |  STRING  | Replace input Blue channel with target<br>channel or constant | BLUE_A | RED A, GREEN A, BLUE A, ALPHA A, RED B,<br>GREEN B, BLUE B, ALPHA B, CONSTANT
🟦  |  INT  | Blue | 0 | 
SWAP A  |  STRING  | Replace input Alpha channel with target<br>channel or constant | ALPHA_A | RED A, GREEN A, BLUE A, ALPHA A, RED B,<br>GREEN B, BLUE B, ALPHA B, CONSTANT
⬜  |  INT  | Alpha | 0 | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project