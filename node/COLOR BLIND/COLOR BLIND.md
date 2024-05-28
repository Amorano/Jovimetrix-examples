# COLOR BLIND (JOV) 👁‍🗨

## JOVIMETRIX 🔺🟩🔵/ADJUST

The `Color Blind` node facilitates the simulation of color blindness effects on images, aiding in accessibility testing and design adjustments. It offers options to simulate various types of color deficiencies, adjust the severity of the effect, and apply the simulation using different simulators. This node is valuable for ensuring inclusivity in visual content and design processes.

![COLOR BLIND](./COLOR%20BLIND.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
MODE | STRING | scaling mode | PROTAN | DEUTAN, PROTAN, TRITAN
MAP | STRING | custom image that will be<br>transformed into a lut or a<br>built-in cv2 lut | AUTOSELECT | AUTOSELECT, BRETTEL1997,<br>COBLISV1, COBLISV2, MACHADO2009,<br>VIENOT1999, VISCHECK
\# | FLOAT | value | 1 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project