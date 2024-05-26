# COMPARISON (JOV) 🕵🏽

## JOVIMETRIX 🔺🟩🔵/FLOW

The Comparison node evaluates two inputs based on a specified comparison operation. It accepts two inputs (A and B), comparison operators, and optional values for successful and failed comparisons. The node performs the specified comparison operation element-wise between corresponding elements of A and B. If the comparison is successful for all elements, it returns the success value; otherwise, it returns the failure value. The node supports various comparison operators such as EQUAL, GREATER_THAN, LESS_THAN, AND, OR, IS, IN, etc.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|---|---
🅰️|*|input a||
🅱️|*|input b||
😍|*|pass this data on a successful condition||
🥵|*|pass this data on a failure condition||
🕵🏽‍♀️|COMBO[STRING]|comparison function. will pass the data<br>in 😍 on successful comparison|EQUAL|EQUAL, NOT_EQUAL, LESS_THAN, LESS_THAN_EQUAL, GREATER_THAN,<br>GREATER_THAN_EQUAL, AND, NAND, OR, NOR, XOR, XNOR, IS,<br>IS_NOT, IN, NOT_IN
🙃|BOOLEAN|flip input a and input b with each other|False|

### OUTPUT

name|type|desc
:---:|:---:|---
🔮|Any Type|*
VECTOR|Compound value of type float, vec2, vec3<br>or vec4|*

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project