  
Visualize a series of data points over time. It accepts a dynamic number of values to graph and display, with options to reset the graph or specify the number of values. The output is an image displaying the graph, allowing users to analyze trends and patterns.  
![GRAPH](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GRAPH/GRAPH.png)
### OUTPUT NODE?: True
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| RESET | BOOLEAN | Clear the graph history | False |  |
| VAL | INT | Number of values to graph and display | 60 |  |
| 🇼🇭 | VEC2INT | Width and Height of the graph output | [512, 512] |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | T |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project