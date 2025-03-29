  
Routes the input data from the optional input ports to the output port, preserving the order of inputs. The `PASS\_IN` optional input is directly passed through to the output, while other optional inputs are collected and returned as tuples, preserving the order of insertion.  
![ROUTE](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/ROUTE/ROUTE.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 🚌 | BUS | Pass through another route node to pre-populate the outputs. |  |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🚌 | BUS | P |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project