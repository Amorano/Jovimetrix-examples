# PIXEL SWAP (JOV) 🔃

## JOVIMETRIX 🔺🟩🔵/COMPOSE

The Pixel Swap Node swaps pixel values between two input images based on the specified channel swizzle operations. Each channel of the output image is determined by a separate swizzle operation, allowing for flexible pixel manipulation and composition.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
👾A|*|pixel data (rgba, rgb or grayscale)||
👾B|*|pixel data (rgba, rgb or grayscale)||
SWAP R|COMBO[STRING]|replace input red channel with<br>target channel or constant|RED_A|RED_A, GREEN_A, BLUE_A, ALPHA_A, RED_B,<br>GREEN_B, BLUE_B, ALPHA_B, CONSTANT
🟥|INT|red|0|
SWAP G|COMBO[STRING]|replace input green channel with<br>target channel or constant|GREEN_A|RED_A, GREEN_A, BLUE_A, ALPHA_A, RED_B,<br>GREEN_B, BLUE_B, ALPHA_B, CONSTANT
🟩|INT|green|0|
SWAP B|COMBO[STRING]|replace input blue channel with<br>target channel or constant|BLUE_A|RED_A, GREEN_A, BLUE_A, ALPHA_A, RED_B,<br>GREEN_B, BLUE_B, ALPHA_B, CONSTANT
🟦|INT|blue|0|
SWAP A|COMBO[STRING]|replace input alpha channel with<br>target channel or constant|ALPHA_A|RED_A, GREEN_A, BLUE_A, ALPHA_A, RED_B,<br>GREEN_B, BLUE_B, ALPHA_B, CONSTANT
⬜|INT|alpha|0|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|IMAGE|Image
🌈|IMAGE|RGB (no alpha) Color
😷|MASK|Mask or Image to use as Mask to control<br>where adjustments are applied

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project