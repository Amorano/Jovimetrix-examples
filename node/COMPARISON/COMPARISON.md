# COMPARISON (JOV) 🕵🏽

## JOVIMETRIX 🔺🟩🔵/FLOW

The Comparison node evaluates two inputs based on a specified operation. It accepts two inputs (A and B), comparison operators, and optional values for successful and failed comparisons. The node performs the specified operation element-wise between corresponding elements of A and B. If the comparison is successful for all elements, it returns the success value; otherwise, it returns the failure value. The node supports various comparison operators such as EQUAL, GREATER_THAN, LESS_THAN, AND, OR, IS, IN, etc.

![COMPARISON](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COMPARISON/COMPARISON.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️ | * | input a |  | 
🅱️ | * | input b |  | 
😍 | * | pass this data on a successful<br>condition |  | 
🥵 | * | pass this data on a failure<br>condition |  | 
🕵🏽‍♀️ | STRING | comparison function. will pass<br>the data in 😍 on successful<br>comparison | EQUAL | EQUAL, NOT EQUAL, LESS THAN,<br>LESS THAN EQUAL, GREATER THAN,<br>GREATER THAN EQUAL, AND, NAND,<br>OR, NOR, XOR, XNOR, IS, IS NOT,<br>IN, NOT IN
🙃 | BOOLEAN | flip input a and input b with<br>each other | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
🔮 | * | Any Type 
VECTOR | * | Compound value of type float, vec2, vec3<br>or vec4 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project