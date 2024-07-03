# COMPARISON (JOV) 🕵🏽

## JOVIMETRIX 🔺🟩🔵/CALC

The Comparison node evaluates two inputs based on a specified operation. It accepts two inputs (A and B), comparison operators, and optional values for successful and failed comparisons. The node performs the specified operation element-wise between corresponding elements of A and B. If the comparison is successful for all elements, it returns the success value; otherwise, it returns the failure value. The node supports various comparison operators such as EQUAL, GREATER_THAN, LESS_THAN, AND, OR, IS, IN, etc.

![COMPARISON](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COMPARISON/COMPARISON.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🅰️ | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4,<br>VEC2INT, VEC3INT, VEC4INT, COORD2D, IMAGE,<br>MASK | Master Comparator |  | 
🅱️ | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4,<br>VEC2INT, VEC3INT, VEC4INT, COORD2D, IMAGE,<br>MASK | Secondary Comparator |  | 
😍 | * | pass this data on a successful condition |  | 
🥵 | * | pass this data on a failure condition |  | 
🕵🏽‍♀️ | STRING | Comparison function. Will pass the data in<br>😍 on successful comparison | EQUAL | EQUAL, NOT EQUAL, LESS THAN, LESS THAN<br>EQUAL, GREATER THAN, GREATER THAN EQUAL,<br>AND, NAND, OR, NOR, XOR, XNOR, IS, IS NOT,<br>IN, NOT IN
🙃 | BOOLEAN | Flip Input A and Input B with each other | False | 

### OUTPUT

name | type | desc
:---:|:---:|---
⚡ | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D | Trigger 
VAL | BOOLEAN, FLOAT, INT, VEC2, VEC3, VEC4, VEC2INT, VEC3INT, VEC4INT, COORD2D | Value 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project