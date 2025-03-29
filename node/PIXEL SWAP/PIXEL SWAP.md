  
Swap pixel values between two input images based on specified channel swizzle operations. Options include pixel inputs, swap operations for red, green, blue, and alpha channels, and constant values for each channel. The swap operations allow for flexible pixel manipulation by determining the source of each channel in the output image, whether it be from the first image, the second image, or a constant value.  
![PIXEL SWAP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/PIXEL%20SWAP/PIXEL%20SWAP.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾A | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| 👾B | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| SWAP R | STRING | Replace input Red channel with target channel or constant | RED\_A | RED A, GREEN A, BLUE A, ALPHA A, RED B, GREEN B, BLUE B, ALPHA B, CONSTANT |
| SWAP G | STRING | Replace input Green channel with target channel or constant | GREEN\_A | RED A, GREEN A, BLUE A, ALPHA A, RED B, GREEN B, BLUE B, ALPHA B, CONSTANT |
| SWAP B | STRING | Replace input Blue channel with target channel or constant | BLUE\_A | RED A, GREEN A, BLUE A, ALPHA A, RED B, GREEN B, BLUE B, ALPHA B, CONSTANT |
| SWAP A | STRING | Replace input Alpha channel with target channel or constant | ALPHA\_A | RED A, GREEN A, BLUE A, ALPHA A, RED B, GREEN B, BLUE B, ALPHA B, CONSTANT |
| MATTE | VEC4INT | Background color for padding | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output. |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha. |
| 😷 | MASK | Single channel mask output. |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project