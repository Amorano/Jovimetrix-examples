# PIXEL MERGE (JOV) 🫂

## JOVIMETRIX 🔺🟩🔵/COMPOSE

The Pixel Merge Node combines individual color channels (red, green, blue) along with an optional mask channel to create a composite image. This node is useful for merging separate color components into a single image for visualization or further processing.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
🟥|*|red||
🟩|*|green||
🟦|*|blue||
⬜|*|alpha||
MATTE|VEC4|background color|(0, 0, 0, 255)|

### OUTPUT

name|type|desc
:---:|:---:|---
🖼️|Image|IMAGE
🌈|RGB (no alpha) Color|IMAGE
😷|Mask or Image to use as Mask to control<br>where adjustments are applied|MASK

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project