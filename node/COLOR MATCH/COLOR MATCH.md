## [COLOR MATCH (JOV) 💞](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/COLOR%20MATCH/COLOR%20MATCH.md)

## JOVIMETRIX 🔺🟩🔵/COMPOSE


Adjust the color scheme of one image to match another with the Color Match Node. Choose from various color matching LUTs or Reinhard matching. You can specify a custom user color maps, the number of colors, and whether to flip or invert the images.


![COLOR MATCH](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20MATCH/COLOR%20MATCH.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
👾B  |  *  | Pixel Data (RGBA, RGB or Grayscale) |  | 
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | REINHARD | REINHARD, LUT
MAP  |  STRING  | Custom image that will be transformed into<br>a LUT or a built-in cv2 LUT | USER_MAP | USER MAP, PRESET MAP
🇸🇨  |  STRING  | One of two dozen CV2 Built-in Colormap LUT<br>(Look Up Table) Presets | HSV | AUTUMN, BONE, JET, WINTER, RAINBOW, OCEAN,<br>SUMMER, SPRING, COOL, HSV, PINK, HOT,<br>PARULA, MAGMA, INFERNO, PLASMA, VIRIDIS,<br>CIVIDIS, TWILIGHT, TWILIGHT SHIFTED,<br>TURBO, DEEPGREEN
VAL  |  INT  | The number of colors to use from the LUT<br>during the remap. Will quantize the LUT<br>range. | 255 | 
🙃  |  BOOLEAN  | Flip Input A and Input B with each other | False | 
🔳  |  BOOLEAN  | Invert the color match output | False | 
MATTE  |  VEC4INT  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | [0, 0, 0, 255] | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project