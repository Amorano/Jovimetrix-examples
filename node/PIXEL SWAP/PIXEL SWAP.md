# PIXEL SWAP (JOV) 🔃

## JOVIMETRIX 🔺🟩🔵/COMPOSE

Swap pixel values between two input images based on specified channel swizzle operations. Options include pixel inputs, swap operations for red, green, blue, and alpha channels, and constant values for each channel. The swap operations allow for flexible pixel manipulation by determining the source of each channel in the output image, whether it be from the first image, the second image, or a constant value.

![PIXEL SWAP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/PIXEL%20SWAP/PIXEL%20SWAP.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
👾B | * | pixel data (rgba, rgb or<br>grayscale) |  | 
SWAP R | STRING | replace input red channel with<br>target channel or constant | RED_A | RED A, GREEN A, BLUE A, ALPHA A,<br>RED B, GREEN B, BLUE B, ALPHA B,<br>CONSTANT
🟥 | INT | red | 0 | 
SWAP G | STRING | replace input green channel with<br>target channel or constant | GREEN_A | RED A, GREEN A, BLUE A, ALPHA A,<br>RED B, GREEN B, BLUE B, ALPHA B,<br>CONSTANT
🟩 | INT | green | 0 | 
SWAP B | STRING | replace input blue channel with<br>target channel or constant | BLUE_A | RED A, GREEN A, BLUE A, ALPHA A,<br>RED B, GREEN B, BLUE B, ALPHA B,<br>CONSTANT
🟦 | INT | blue | 0 | 
SWAP A | STRING | replace input alpha channel with<br>target channel or constant | ALPHA_A | RED A, GREEN A, BLUE A, ALPHA A,<br>RED B, GREEN B, BLUE B, ALPHA B,<br>CONSTANT
⬜ | INT | alpha | 0 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project