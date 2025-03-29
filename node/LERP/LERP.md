  
Calculate linear interpolation between two values or vectors based on a blending factor (alpha).  
  
The node accepts optional start (IN\_A) and end (IN\_B) points, a blending factor (FLOAT), and various input types for both start and end points, such as single values (X, Y), 2-value vectors (IN\_A2, IN\_B2), 3-value vectors (IN\_A3, IN\_B3), and 4-value vectors (IN\_A4, IN\_B4).  
  
Additionally, you can specify the easing function (EASE) and the desired output type (TYPE). It supports various easing functions for smoother transitions.  
![LERP](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/LERP/LERP.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 🅰️ | \* | Custom Start Point |  |  |
| 🅱️ | \* | Custom End Point |  |  |
| 🛟 | VEC4 | Blend Amount. 0 = full A, 1 = full B | [0.5, 0.5, 0.5, 0.5] |  |
| 🅰️🅰️ | VEC4 | default value vector for A | [0, 0, 0, 0] |  |
| 🅱️🅱️ | VEC4 | default value vector for B | [1, 1, 1, 1] |  |
| ❓ | STRING | Output type desired from resultant operation | FLOAT | BOOLEAN, FLOAT, INT, VEC2, VEC2INT, VEC3, VEC3INT, VEC4, VEC4INT, COORD2D |
| EASE | STRING | Easing function | NONE | NONE, QUAD IN, QUAD OUT, QUAD IN OUT, CUBIC IN, CUBIC OUT, CUBIC IN OUT, QUARTIC IN, QUARTIC OUT, QUARTIC IN OUT, QUINTIC IN, QUINTIC OUT, QUINTIC IN OUT, SIN IN, SIN OUT, SIN IN OUT, CIRCULAR IN, CIRCULAR OUT, CIRCULAR IN OUT, EXPONENTIAL IN, EXPONENTIAL OUT, EXPONENTIAL IN OUT, ELASTIC IN, ELASTIC OUT, ELASTIC IN OUT |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🦄 | \* | O |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project