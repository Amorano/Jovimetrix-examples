# COLOR MATCH (JOV) 💞

## JOVIMETRIX 🔺🟩🔵/ADJUST

The `Color Match` node allows you to adjust the color scheme of one image to match another using various methods. You can choose from different color matching modes such as LUT, Histogram, and Reinhard. Additionally, you can specify options like color maps, the number of colors, and whether to flip or invert the images. This node supports the creation of seamless and cohesive visuals by matching colors accurately, making it ideal for texture work or masking in motion graphics and design projects.

![COLOR MATCH](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20MATCH/COLOR%20MATCH.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾A | * | pixel data (rgba, rgb or<br>grayscale) |  | 
👾B | * | pixel data (rgba, rgb or<br>grayscale) |  | 
MODE | STRING | scaling mode | REINHARD | REINHARD, LUT, HISTOGRAM
MAP | STRING | custom image that will be<br>transformed into a lut or a<br>built-in cv2 lut | USER_MAP | USER MAP, PRESET MAP
🇸🇨 | STRING | one of two dozen cv2 built-in<br>colormap lut (look up table)<br>presets | HSV | AUTUMN, BONE, JET, WINTER,<br>RAINBOW, OCEAN, SUMMER, SPRING,<br>COOL, HSV, PINK, HOT, PARULA,<br>MAGMA, INFERNO, PLASMA, VIRIDIS,<br>CIVIDIS, TWILIGHT, TWILIGHT<br>SHIFTED, TURBO, DEEPGREEN
\# | INT | value | 255 | 
🙃 | BOOLEAN | flip input a and input b with<br>each other | False | 
🔳 | BOOLEAN | color inversion | False | 
MATTE | VEC4 | background color | (0, 0, 0, 255) | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project