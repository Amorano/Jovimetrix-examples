[PIXEL SWAP (JOV) 🔃](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/PIXEL%20SWAP/PIXEL%20SWAP.md)
------------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/COMPOSE
  
Swap pixel values between two input images based on specified channel swizzle operations. Options include pixel inputs, swap operations for red, green, blue, and alpha channels, and constant values for each channel. The swap operations allow for flexible pixel manipulation by determining the source of each channel in the output image, whether it be from the first image, the second image, or a constant value.  
![PIXEL SWAP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/PIXEL%20SWAP/PIXEL%20SWAP.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾A | \* | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 👾B | \* | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| SWAP R | STRING | Replace input Red channel with target channel or constant | RED\_A | RED A, GREEN A, BLUE A, ALPHA A, RED B, GREEN B, BLUE B, ALPHA B, CONSTANT |
| SWAP G | STRING | Replace input Green channel with target channel or constant | GREEN\_A | RED A, GREEN A, BLUE A, ALPHA A, RED B, GREEN B, BLUE B, ALPHA B, CONSTANT |
| SWAP B | STRING | Replace input Blue channel with target channel or constant | BLUE\_A | RED A, GREEN A, BLUE A, ALPHA A, RED B, GREEN B, BLUE B, ALPHA B, CONSTANT |
| SWAP A | STRING | Replace input Alpha channel with target channel or constant | ALPHA\_A | RED A, GREEN A, BLUE A, ALPHA A, RED B, GREEN B, BLUE B, ALPHA B, CONSTANT |
| MATTE | VEC4INT | Define a background color for padding, if necessary. This is useful when images do not fit perfectly into the designated area and need a filler color | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project