[COMPARISON (JOV) 🕵🏽](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/COMPARISON/COMPARISON.md)
---------------------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/CALC
  
Evaluates two inputs (A and B) with a specified comparison operators and optional values for successful and failed comparisons. The node performs the specified operation element-wise between corresponding elements of A and B. If the comparison is successful for all elements, it returns the success value; otherwise, it returns the failure value. The node supports various comparison operators such as EQUAL, GREATER\_THAN, LESS\_THAN, AND, OR, IS, IN, etc.  
![COMPARISON](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/COMPARISON/COMPARISON.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 🅰️ | \* | Master Comparator | 0 |  |
| 🅱️ | \* | Secondary Comparator | 0 |  |
| 😍 | \* | pass this data on a successful condition | 0 |  |
| 🥵 | \* | pass this data on a failure condition | 0 |  |
| 🕵🏽‍♀️ | STRING | Comparison function. Will pass the data in 😍 on successful comparison | EQUAL | EQUAL, NOT EQUAL, LESS THAN, LESS THAN EQUAL, GREATER THAN, GREATER THAN EQUAL, AND, NAND, OR, NOR, XOR, XNOR, IS, IS NOT, IN, NOT IN |
| 🙃 | BOOLEAN | Flip Input A and Input B with each other | False |  |
| 🔳 | BOOLEAN | reverse the successful and failure inputs | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| ⚡ | \* | Trigger |
| val | \* |  |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project