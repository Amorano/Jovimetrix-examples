# COLOR BLIND (JOV) 👁‍🗨

## JOVIMETRIX 🔺🟩🔵/ADJUST

The `Color Blind` node facilitates the simulation of color blindness effects on images, aiding in accessibility testing and design adjustments. It offers options to simulate various types of color deficiencies, adjust the severity of the effect, and apply the simulation using different simulators. This node is valuable for ensuring inclusivity in visual content and design processes.

![COLOR BLIND](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COLOR%20BLIND/COLOR%20BLIND.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
DEFICIENCY | STRING | type of color deficiency: red<br>(protanopia), green<br>(deuteranopia), blue<br>(tritanopia) | PROTAN | PROTAN, DEUTAN, TRITAN
SIMULATOR | STRING | solver to use when translating<br>to new color space | AUTOSELECT | AUTOSELECT, BRETTEL1997,<br>COBLISV1, COBLISV2, MACHADO2009,<br>VIENOT1999, VISCHECK
\# | FLOAT | value | 1 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project