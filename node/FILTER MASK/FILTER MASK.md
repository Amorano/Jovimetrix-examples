  
Create masks based on specific color ranges within an image. Specify the color range using start and end values and an optional fuzziness factor to adjust the range. This node allows for precise color-based mask creation, ideal for tasks like object isolation, background removal, or targeted color adjustments.  
![FILTER MASK](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/FILTER%20MASK/FILTER%20MASK.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾A | IMAGE, MASK | Pixel Data (RGBA, RGB or Grayscale) |  |  |
| START | VEC3INT | Start of the range | [128, 128, 128] |  |
| 🇴 | BOOLEAN | use an end point (start->end) when calculating the filter range | False |  |
| END | VEC3INT | End of the range | [128, 128, 128] |  |
| 🛟 | VEC3 | the fuzziness use to extend the start and end range(s) | [0.5, 0.5, 0.5] |  |
| MATTE | VEC4INT | Background color for padding | [0, 0, 0, 255] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Full channel [RGBA] image. If there is an alpha, the image will be masked out with it when using this output. |
| 🌈 | IMAGE | Three channel [RGB] image. There will be no alpha. |
| 😷 | MASK | Single channel mask output. |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project